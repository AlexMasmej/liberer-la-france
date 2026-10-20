import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answer = []


def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:100], text.count(old))
    return text.replace(old, new, 1)


def plain(text):
    return unescape(re.sub('<[^>]+>', '', text))


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def impact(classification, assessment, limitations, burdens, effects):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects)


def make(number, text, reason, notes):
    a = by_number[number]
    return {**{k: a[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']},
            'proposed_xml': text, 'reason': reason, 'review_notes': notes,
            'status': 'rewrite_draft'}


def checks(number):
    a = by_number[number]
    key = a['code_id'] + '|' + a['source_id']
    result = []
    for target_key in references['requirements'][key]:
        t = references['targets'][target_key]
        n = t['number']
        if n == '44 sexies':
            assessment = (
                "Le I de 220 terdecies vise l'exonération de bénéfices de 44 sexies, et non une règle de rupture. "
                "La source de cette cible maintient vingt-trois mois d'exonération puis les fractions quart, moitié et trois quarts ; "
                "le renvoi et l'accès au crédit malgré exonération sont conservés pour les entreprises éligibles créées jusqu'au 31 décembre 2027, sans réduire l'échéance propre du crédit au 31 décembre 2031. "
                "La proposition fournie de 44 sexies conserve encore la formule CDI ou contrat d'au moins six mois pour les trois salariés des professions libérales : "
                "le contrat unique nouveau satisfait la branche CDI sans attente de six mois ; les anciens contrats conservent leur branche propre. "
                "La cible doit encore être coordonnée à l'IS à la distribution pour conserver les fractions exonérées jusqu'à leur distribution. "
                "Ni le préavis ni l'indemnité de licenciement ne sont visés par ce renvoi ; aucune condition de notification ou d'ancienneté de rupture n'est ajoutée ici."
            )
        elif n == '219 ter':
            assessment = (
                "223 bis est la procédure de demande du taux historique favorable de 219 ter pour les indemnités de guerre, "
                "pas une règle de contrat de travail. La source de 219 ter exige une demande ; sa proposition fournie retient le plus faible "
                "du taux normal et du taux historique sans demande distincte et reporte l'imposition à la distribution pour les exercices concernés. "
                "L'abrogation de 223 bis retire donc la demande dans la déclaration de l'exercice du versement et l'envoi systématique de justificatifs, "
                "tout en conservant le bénéfice et les contrôles sur pièces existantes, les demandes anciennes et les recours non prescrits. "
                "Aucun délai de préavis, seuil d'ancienneté professionnelle ou notification de licenciement n'a de rapport avec ce renvoi. "
                "La proposition cible est un projet à adopter conjointement, non le droit officiel en vigueur."
            )
        else:
            scope = (
                "Les a et b du 1° du III de " + number + " distinguent les dépenses de personnel permanent et non permanent affecté aux opérations culturelles ; "
                "ils ne renvoient à aucun de ces articles de rupture. Le texte coordonne seulement l'éligibilité des affectations temporaires au sein d'un emploi à durée indéterminée. "
            ) if number != '223 bis' else (
                "223 bis concerne exclusivement les indemnités versées aux entreprises sinistrées par faits de guerre et la demande fiscale de 219 ter. "
                "Il ne concerne ni l'indemnisation d'un salarié ni un emploi permanent ou temporaire. Cette cible de travail est sans application à sa procédure. "
            )
            if n == 'L1234-1':
                assessment = scope + (
                    "La source de L1234-1 fixe, hors faute grave, le préavis selon six mois et deux ans de services continus ; "
                    "la proposition vise quinze jours calendaires pour les contrats nouveaux et garde le régime des anciens contrats. "
                    "Aucun de ces seuils ne conditionne le crédit ou le taux historique. La notification écrite et son point de départ relèvent de L1234-3, "
                    "non fourni comme cible et non ajouté comme renvoi ; les procédures collectives et autorisations spéciales demeurent distinctes."
                )
            elif n == 'L1221-2':
                assessment = scope + (
                    "La source de L1221-2 autorise encore le CDD dans les cas du titre IV ; la proposition interdit tout terme automatique pour les embauches nouvelles, "
                    "y compris à la fin d'une formation ou d'une mission. Les contrats antérieurs et leurs droits restent transitoirement régis par leurs règles. "
                    "Aucun nouveau CDD n'est permis par le crédit culturel ou par l'abrogation fiscale ; aucune ancienneté ou notification de rupture n'est exigée pour l'avantage."
                )
            elif n == 'L1234-9':
                assessment = scope + (
                    "La source de L1234-9 ouvre l'indemnité de licenciement après huit mois, sauf faute grave ; le projet fourni distingue les nouveaux contrats "
                    "avec seuil d'un an à la fin effective, préavis inclus, puis 0,20 mois par année totale, fractions en mois complets et plafond de six mois, employeur seul. "
                    "Il protège les composantes anciennes et les indemnités spéciales. Ni cette ancienneté ni la notification de rupture ne sont une condition de l'avantage fiscal ici ; "
                    "aucune règle de calcul salarial ou d'indemnité n'est modifiée par cet article fiscal."
                )
            else:
                raise AssertionError(n)
        result.append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))
    return result


regimes = {
    '220 terdecies': ('IV', '220 X', 'jeux-video-fin-agrements', 'créateurs de jeux vidéo'),
    '220 quindecies': ('III', '220 S', 'spectacle-musical-fin-agrements', 'producteurs de spectacles musicaux ou de variétés'),
    '220 sexdecies': ('III', '220 T', 'theatre-cirque-fin-agrements', 'producteurs de représentations théâtrales ou de cirque'),
    '220 septdecies': ('III', '220 Q bis', 'edition-musicale-fin-agrements', 'entreprises d’édition musicale'),
}

is_paragraph = (
    "Pour les entreprises relevant d'une imposition à la distribution des bénéfices, l'absence de distribution ou de cotisation d'impôt sur les sociétés "
    "ne fait obstacle ni à la naissance du crédit d'impôt ni à la restitution de son excédent au titre de l'exercice de la dépense, dans les conditions de l'article {article}. "
    "Aucune distribution n'est exigée pour obtenir cette restitution. Les dépenses sont retenues dans le résultat de référence selon les mêmes règles que pour la détermination "
    "du résultat imposable. L'exonération de tout ou partie des bénéfices ne prive pas du crédit une entreprise entrant dans le champ du I. "
    "Le calcul annuel du crédit ne rend pas imposables les bénéfices conservés. Chaque montant de crédit ne peut être imputé, remboursé ou utilisé qu'une fois ; "
    "les créances antérieures et leurs possibilités légales de cession ou de nantissement sont conservées."
)

work_paragraph = (
    "La distinction, au III, entre les frais de personnel permanent et les frais de personnel non permanent ne constitue pas une condition de recours à un contrat à durée déterminée. "
    "Les rémunérations d'artistes, de techniciens et des autres personnels affectés pour une période limitée aux opérations éligibles restent prises en compte dans la catégorie de dépenses "
    "correspondante lorsqu'ils sont employés par contrat à durée indéterminée, dans les mêmes limites et sous les mêmes conditions d'affectation. "
    "Une même dépense ne peut être comptée dans les deux catégories. La durée de cette affectation ne fixe pas le terme de l'emploi. "
    "Les contrats antérieurs à l'entrée en vigueur de la loi instituant le contrat de travail unique et les droits nés de leur exécution restent soumis à leurs règles transitoires."
)

europe_notes = (
    " La suppression des agréments nationaux ne constate aucune autorisation européenne de modification du régime d'aide : vérifier les décisions de la Commission, "
    "les conditions de dispense de notification et, si nécessaire, coordonner la notification et l'interdiction de mise à exécution avant autorisation au titre de l'article 108, paragraphe 3, du TFUE. "
    "Aucun texte européen complet ni décision d'aide n'est fourni dans le lot ; cette vérification reste identifiée et aucune conformité n'est présumée. "
    "Les nouvelles dépenses avant obtention d'un agrément devenant éligibles constituent un élargissement réel à apprécier à ce titre, sans nouveau taux."
)

for number, (division, linked, measure, population) in regimes.items():
    a = by_number[number]
    text = a['source_xml']
    old_result = "dès lors qu'elles entrent dans la détermination du résultat imposable"
    new_result = "dès lors qu'elles entrent dans la détermination du résultat imposable ou, pour les entreprises relevant d'une imposition à la distribution, du résultat de référence"
    text = replace_once(text, old_result, new_result)
    if number == '220 terdecies':
        text = replace_once(text, 'en vue de la création de jeux vidéo agréés.', 'en vue de la création de jeux vidéo répondant aux conditions du présent article.')
        old_approval = "2. – Les dépenses mentionnées au 1 ouvrent droit au bénéfice du crédit d'impôt à compter de la date de réception par le président du Centre national du cinéma et de l'image animée d'une demande d'agrément provisoire. Cet agrément est délivré après sélection par un comité d'experts chargé de vérifier que le jeu vidéo remplit les conditions prévues au III."
        new_approval = (
            "2. – Les dépenses mentionnées au 1 ouvrent droit au bénéfice du crédit d'impôt dès leur engagement, sous réserve du respect des conditions du présent article. "
            "Aucun agrément national provisoire ou définitif, ni demande préalable ou déclaration de commencement de la création, n'est exigé pour l'obtention du crédit d'impôt. "
            "Le respect des conditions prévues au III, y compris le barème de points et les exclusions du 2 de ce III, demeure soumis au contrôle fiscal."
        )
        text = replace_once(text, old_approval, new_approval)
        old_window = "Seules ouvrent droit au crédit d'impôt les dépenses exposées dans les trente-six mois qui précèdent la date de délivrance de l'agrément définitif mentionnée à l'article 220 X ."
        new_window = (
            "Par dérogation à l'article 220 X, les dépenses relevant du présent 2 ne sont soumises à aucune limitation d'ancienneté calculée à partir de la délivrance d'un agrément. "
            "Aucun reversement ou reprise du crédit ne peut être fondé sur l'absence, le refus ou le délai d'obtention d'un agrément provisoire ou définitif, "
            "y compris les délais de trente-six ou de soixante-douze mois prévus à cet article. "
            "Le contrôle et la reprise d'un crédit ne satisfaisant pas aux conditions substantielles du présent article demeurent applicables."
        )
        text = replace_once(text, old_window, new_window)
        text = replace_once(text,
            "VII. – Les conditions d'application du présent article, notamment celles relatives à la délivrance de l'agrément provisoire et aux obligations déclaratives incombant aux entreprises, sont fixées par décret.",
            "VII. – Les conditions d'application du présent article, notamment les modalités de calcul et de déclaration fiscale du crédit d'impôt, sont fixées par décret. "
            "Ce décret ne peut rétablir d'agrément, de demande préalable ou de déclaration de commencement de la création. "
            "La suppression des agréments n'impose aucun nouveau registre, attestation ou dépôt de pièces auprès du Centre national du cinéma et de l'image animée.")
        transition = (
            "Les dispositions du 2 du IV et du VII supprimant les agréments et les limitations qui en dépendent s'appliquent aux dépenses engagées à compter de l'entrée en vigueur de la loi qui les institue, "
            "y compris pour des jeux vidéo dont la création a commencé avant cette date. Les dépenses antérieures, leurs crédits, créances, restitutions, contrôles et recours restent régis par les dispositions antérieures, "
            "notamment le délai de soixante-douze mois propre aux jeux dont le coût de développement dépasse 10 millions d'euros. "
            "Les agréments et procédures afférents à ces dépenses antérieures ne peuvent conditionner l'éligibilité des dépenses nouvelles. "
            "Les décisions et agréments antérieurs conservent leurs effets favorables dans leur champ et leur durée d'application, y compris pour les dépenses ultérieures qui en remplissent les conditions, "
            "sans nouvelle demande ni prorogation d'un régime expiré. "
            "Aucune dépense antérieure exclue ne devient éligible rétroactivement. La date limite du 31 décembre 2031 demeure applicable. "
            "Les règles de l'Union européenne relatives aux aides d'État demeurent applicables."
        )
        text += '<p>VIII. – ' + is_paragraph.format(article=linked) + '</p>\n<p>' + transition + '</p>\n'
        removed = [
            "Suppression de l'agrément provisoire du CNC, de la demande préalable et de la sélection par comité d'experts, sans déclaration de commencement de remplacement.",
            "Suppression, pour les dépenses nouvelles, de l'agrément définitif et des reprises liées à son absence, son refus ou aux délais de trente-six ou soixante-douze mois de 220 X.",
            "Suppression de la fenêtre de trente-six mois précédant l'agrément définitif pour les dépenses nouvelles, sans restriction des dépenses antérieures ou du délai favorable de soixante-douze mois.",
        ]
        benefits = (
            "Le crédit de 30 % reste ouvert aux créateurs futurs éligibles jusqu'au 31 décembre 2031, y compris aux entreprises exonérées selon chacun des neuf articles cités au I. "
            "Sont intégralement conservés l'assimilation des résidents français aux citoyens français, l'admission sous conditions des jeux destinés aux adultes, les cinq postes de dépenses, "
            "la sous-traitance plafonnée à 2 millions d'euros par exercice, le plafond de crédit de 6 millions avec proratisation des exercices et la restitution de 220 X malgré absence d'IS distribué. "
            "La suppression des agréments et de la fenêtre de trente-six mois élargit l'accès pour les dépenses nouvelles ; les exclusions pornographie et très grande violence subsistent. "
            "Pour les dépenses anciennes, toutes les conditions et possibilités antérieures, dont le délai de soixante-douze mois pour les jeux de plus de 10 millions, sont protégées ; "
            "aucun crédit n'est utilisé deux fois. La déduction des subventions n'est pas un avantage : elle prévient un double financement et reste entière. "
            "Le seuil de 100 000 €, le barème culturel et le respect de la législation sociale sont conservés comme critères du régime d'aide, non transformés en approbation administrative."
        )
        notes = (
            "Source et note 2026 lues intégralement. II et III entiers : coût de 100 000 €, commercialisation, nationalités/résidence, barème et exception des jeux adultes conservés. "
            "IV 1° à 5°, V et VI reproduits sans amputation, sauf coordination explicite du résultat de référence : 30 %, 2 millions, 6 millions et prorata inchangés. "
            "220 X, source et note 2013 lues intégralement, impose actuellement agrément définitif, délais 36/72 mois, reprise et fenêtre 36 mois pour jeux de plus de 10 millions. "
            "La dérogation expresse du IV 2 neutralise ces seules exigences pour les dépenses nouvelles ; 220 X doit être rédigé conjointement pour rendre sa lettre cohérente, "
            "sans toucher imputation, restitution, cession L313-23 à L313-35 ni anciens projets. "
            "Annexe III 46 quater-0 YZG, YZH et YZI lus : calcul des salaires, amortissements, déclaration fiscale et ordre d'imputation restent à leur champ. "
            "L'envoi de la copie au CNC de YZH n'est pas supprimé par ce seul texte et n'est pas compté comme gain ; sa coordination avec les procédures du code du cinéma et de l'image animée "
            "doit accompagner la fin des agréments, sans créer un dossier de remplacement. "
            "Le renvoi de III 2 au barème mentionné au 4° du 1 est lu avec l'alinéa qui suit l'énumération et applique ce barème aux conditions des 3° et 4° ; "
            "cette présentation ne justifie pas de retirer la dérogation favorable aux jeux destinés aux adultes. "
            "La cible 44 sexies fournie reste à coordonner à la distribution ; les huit autres exonérations citées au I ne sont ni supprimées ni prétendues auditées par ce lot. "
            "Le renvoi à 220 X est déjà présent dans la source ; aucun nouveau renvoi au code du travail n'est ajouté. "
            "Le calendrier des crédits reste annuel pour leur naissance et leur restitution, sans IS annuel sur les bénéfices conservés. Aucun rendement budgétaire ou autofinancement n'est allégué."
        ) + europe_notes
        reason = (
            "Réforme de fond : retrait des agréments provisoire et définitif, de la sélection préalable et des délais fiscaux dépendant de leur délivrance pour les dépenses nouvelles. "
            "Les conditions objectives culturelles, la protection des utilisateurs, le contrôle fiscal et toutes les dépenses, taux et plafonds favorables sont conservés. "
            "La coordination avec l'IS à la distribution maintient la naissance annuelle et la restitution du crédit sans imposer une distribution. "
            "Les critères et les énumérations laissés intacts sont maintenus à droit constant pour conserver le régime d'aide, sans prétendre les avoir simplifiés."
        )
    else:
        prefix = 'VI. – ' if number == '220 quindecies' else 'VI.-'
        if number == '220 quindecies':
            old_approval = "VI. – Les dépenses mentionnées au III ouvrent droit au crédit d'impôt à compter de la date de réception par le ministre chargé de la culture d'une demande d'agrément provisoire. Cet agrément, délivré après avis d'un comité d'experts, atteste que le spectacle remplit les conditions prévues au II. Les modalités de fonctionnement du comité d'experts et les conditions de délivrance de l'agrément provisoire sont fixées par décret."
        elif number == '220 sexdecies':
            old_approval = "VI.-Les dépenses mentionnées au III ouvrent droit au crédit d'impôt à compter de la date de réception par le ministre chargé de la culture d'une demande d'agrément provisoire. Cet agrément, délivré après avis d'un comité d'experts, atteste que le spectacle remplit les conditions prévues au II. Les modalités de fonctionnement du comité d'experts et les conditions de délivrance de l'agrément provisoire sont fixées par décret."
        else:
            old_approval = "VI.-Les dépenses mentionnées au III du présent article ouvrent droit au crédit d'impôt à compter de la date de réception par le ministre chargé de la culture d'une demande d'agrément provisoire. Cet agrément, délivré après avis d'un comité d'experts, atteste que les conditions prévues au II sont remplies. Les modalités de fonctionnement du comité d'experts et les conditions de délivrance de l'agrément provisoire sont fixées par décret."
        new_approval = prefix + (
            "Les dépenses mentionnées au III ouvrent droit au crédit d'impôt dès leur engagement, sous réserve du respect des conditions du présent article. "
            "Aucun agrément national provisoire ou définitif, ni demande préalable ou déclaration de commencement des opérations, n'est exigé pour l'obtention du crédit d'impôt. "
            "Par dérogation à l'article " + linked + ", aucun reversement ou reprise du crédit ne peut être fondé sur l'absence, le refus ou le délai d'obtention d'un agrément provisoire ou définitif. "
            "Les conditions substantielles prévues au présent article, ainsi que le respect des obligations légales, fiscales et sociales applicables, demeurent soumis au contrôle fiscal. "
            "Le crédit reste déclaré selon ses modalités fiscales de liquidation ; la suppression des agréments n'impose aucun nouveau registre, attestation ou dépôt de pièces auprès du ministre chargé de la culture ou d'un comité d'experts. "
            "Les dispositions réglementaires d'application ne peuvent rétablir les agréments ni une formalité préalable de remplacement."
        )
        text = replace_once(text, old_approval, new_approval)
        transition = (
            "Les dispositions du VI supprimant les agréments et les reprises qui en dépendent s'appliquent aux dépenses engagées à compter de l'entrée en vigueur de la loi qui les institue, "
            "y compris pour des opérations commencées avant cette date. Les dépenses antérieures, leurs crédits, créances, restitutions, contrôles et recours restent régis par les dispositions antérieures, "
            "y compris les agréments et les dérogations de délai qui leur sont applicables. Ces procédures ne peuvent conditionner l'éligibilité des dépenses nouvelles. "
            "Les décisions et agréments antérieurs conservent leurs effets favorables dans leur champ et leur durée d'application, y compris pour les dépenses ultérieures qui en remplissent les conditions, "
            "sans nouvelle demande ni prorogation d'un régime expiré. "
            "Aucune dépense antérieure exclue ne devient éligible rétroactivement. La date limite du 31 décembre 2027 demeure applicable. "
            "Les dates de dépôt de demandes d'agrément qui déterminaient la rédaction applicable aux dépenses antérieures conservent leur portée pour ces seules dépenses."
        )
        text += '<p>X. – ' + work_paragraph + '</p>\n<p>' + is_paragraph.format(article=linked) + '</p>\n<p>' + transition + '</p>\n'
        removed = [
            "Suppression de l'agrément provisoire ministériel, du dépôt préalable et de l'avis du comité d'experts comme conditions d'ouverture du crédit pour les dépenses nouvelles.",
            "Suppression, pour les dépenses nouvelles, de l'agrément définitif et des reversements ou reprises liés à son absence, son refus ou son délai d'obtention, sans procédure de remplacement.",
        ]
        common_benefits = (
            "Le taux de 15 % et sa majoration à 30 % pour les micro, petites et moyennes entreprises sont maintenus pour les futures opérations recevables jusqu'au 31 décembre 2027. "
            "Toutes les catégories de dépenses, droits d'auteur, salaires et charges, numérisation ou édition, rémunérations des petits dirigeants sous plafond légal de 50 000 € "
            "et frais d'hébergement sous plafond légal de 270 € sont conservées. Les montants réglementaires inférieurs, lorsqu'applicables, ne sont pas rehaussés par la copie des plafonds légaux. "
            "L'emploi à durée indéterminée dans une affectation limitée n'exclut pas les dépenses auparavant rattachées au personnel non permanent. "
            "L'absence d'IS ordinaire sur bénéfices conservés ne ferme ni le crédit ni la restitution prévue à " + linked + ", sans double utilisation. "
            "Les déductions de subventions et le non-cumul d'une même dépense entre crédits restent, ainsi que l'article 53 du règlement européen. "
        )
        if number == '220 quindecies':
            benefits = common_benefits + (
                "Sont spécialement conservées la coproduction avec responsabilité d'employeur assumée par au moins un coproducteur, la dérogation d'une date de musiques actuelles jusqu'à 2 900 places, "
                "les représentations promotionnelles et toutes les représentations éligibles, le plafond d'assiette de 500 000 € par spectacle, le plafond de crédit de 750 000 € avec prorata et le partage proportionnel en coproduction. "
                "La dérogation ancienne prolongeant de quinze mois l'agrément de spectacles agréés entre le 1er juillet 2019 et le 2 juin 2021 reste applicable à leurs dépenses anciennes ; "
                "aucun agrément n'est requis pour les nouvelles dépenses, qui bénéficient donc d'une ouverture plus large."
            )
            notes = (
                "I à V et VII à IX maintenus intégralement, avec la seule coordination du résultat de référence au III ; listes professionnelles et de frais sans omission. "
                "Conserver quatre représentations/trois lieux, jauge réglementaire et dérogation 2 900 places comme ciblage du régime culturel ; le présent projet retire le circuit d'agréments sans leur substituer une sélection. "
                "Taux 15/30 %, rémunération dirigeant plafond légal 50 000 €, cinq minima conventionnels artistes, hébergement plafond légal 270 €, assiette 500 000 €, crédit 750 000 €, prorata et coproduction intacts. "
                "220 S lu entier : imputation, créance cessible selon CMF et restitution conservées ; délai normal 36 mois et prolongation de quinze mois pour agréments du 1er juillet 2019 au 2 juin 2021 "
                "subsistent pour les dépenses anciennes. La dérogation du VI neutralise les reprises d'agrément pour les nouvelles dépenses ; la lettre de 220 S reste à coordonner dans son propre article, non réécrit dans ce lot. "
                "Les trois notes sources sont lues et les dates de dépôt restent utiles aux anciens régimes. La note relative à la loi 2023-1322 cite article 59 puis article 58 : incohérence préexistante à vérifier, non corrigée implicitement. "
                "Annexe III 46 quater-0 ZY octies à duodecies lus : plafond effectif dirigeant 45 000 €, hébergement 270/200 € selon lieux et déclaration annuelle déjà commune conservés. "
                "Aucune nouvelle fusion de formulaire n'est donc comptée. Les procédures ministérielles externes d'agrément doivent être retirées pour le nouveau champ ; leur numérotation complète n'est pas documentée ici. "
            )
        elif number == '220 sexdecies':
            benefits = common_benefits + (
                "Les dépenses des soixante premières représentations restent couvertes, avec l'exception favorable du petit matériel du f pris en totalité au cours des mêmes exercices ; "
                "la numérisation conserve sa fenêtre d'exercices, le plafond d'assiette de 500 000 € par spectacle, le crédit de 750 000 € et sa proratisation demeurent. "
                "La première exploitation, les 90 % de professionnels, six artistes, vingt services de répétition et plus de vingt dates en douze mois dans deux lieux demeurent les critères culturels "
                "du dispositif conservé ; ils ne sont pas présentés comme des avantages ni supprimés sous couvert de fin d'agrément. Aucun ancien crédit ou régime de cirque n'est fermé."
            )
            notes = (
                "Source et note lues en entier. I à V et VII à IX conservés sans omission : théâtre et cirque, première exploitation, 90 % de professionnels, six artistes, vingt services, "
                "plus de vingt dates/douze mois/deux lieux et moitié en France. Ces critères de ciblage culturel restent, sans nouvelle autorisation. "
                "III conserve toutes ses listes, les soixante premières représentations, l'exception du f pour petit matériel et les exercices de numérisation ; 15/30 %, "
                "50 000 €, cinq minima conventionnels, 270 €, 500 000 €, 750 000 € et prorata intacts. "
                "220 T, source et note lues en entier : créance, restitution et cession demeurent ; la dérogation du VI supprime pour les nouvelles dépenses l'exigence finale, "
                "la reprise et le délai de trente-six mois. La lettre de 220 T reste à coordonner dans son article, sans prétendre l'avoir réécrite ici. "
                "Annexe III 46 quater-0 ZY terdecies à septdecies lus : plafond effectif dirigeant 45 000 €, hébergement 270/200 € et déclaration déjà commune conservés. "
                "Aucun second dépôt fiscal n'est supprimé fictivement ; les actes ministériels d'agrément extérieurs doivent être coordonnés, leur numérotation complète n'étant pas fournie. "
            )
        else:
            benefits = common_benefits + (
                "Sont en outre préservés le contrat avec nouveau talent conclu dès le 1er janvier 2022, la règle d'une moitié d'œuvres en français ou langue régionale, "
                "la dérogation microentreprise pour les autres langues à concurrence du répertoire éligible, l'exclusion du personnel au cachet du seuil d'effectif, "
                "le plafond de 300 000 € de dépenses par contrat, la sous-traitance de 1 600 000 € par exercice, le crédit de 500 000 € par entreprise/exercice et le partage proportionnel en coédition. "
                "Les droits de préférence de propriété intellectuelle sont distincts du contrat de travail et demeurent. L'absence de proratisation du plafond annuel de crédit dans cette source est conservée."
            )
            notes = (
                "I à V et VII à IX reproduits entièrement, sauf coordination du résultat de référence au III. Les trois listes de métiers et toutes les dépenses a à f, a à d, a à k demeurent. "
                "Contrats dès le 1er janvier 2022, deux albums, seuil de 50 %, moitié de répertoire linguistique et dérogation microentreprises/cachets préservés ; "
                "le contrat d'édition et le droit de préférence de L132-4 CPI ne sont pas un contrat privé de travail. "
                "Plafonds légaux de rémunérations 50 000 €, hébergement 270 €, dépenses par contrat 300 000 €, sous-traitance 1 600 000 €, crédit 500 000 € inchangés ; "
                "ne pas introduire de prorata d'exercice absent de cette source. Coédition proportionnelle, taux 15/30 %, non-cumul et subventions conservés. "
                "220 Q bis, source et note lues en entier, conserve imputation, restitution, créance et cession ; la dérogation du VI écarte ses agréments, délai 36 mois et reprises "
                "pour les dépenses nouvelles, sa lettre devant être coordonnée dans son propre article. "
                "Annexe III 46 quater-0 YV, YW, YW bis, YW ter, YW quater lus : plafond effectif dirigeant 45 000 €, hébergement 270/200 €, dépôt avec relevé de solde et copie CNM. "
                "La copie CNM n'est pas supprimée par le présent texte ni comptée comme gain. Les notes de YV et YW parlent de péremption de 220 decies alors que leur corps vise 220 septdecies : "
                "anomalie de provenance à vérifier, sans suppression automatique de ces dépenses favorables. Les procédures ministérielles externes doivent être coordonnées, leur numérotation complète restant non fournie. "
            )
        notes += (
            "Les articles de liquidation cités sont des renvois de coordination supplémentaires à la source assignée ; ils ont été lus dans le corpus public, "
            "mais ne sont pas ajoutés à reference_checks dont les seules cibles requises restent celles de reference-targets.json. "
            "L'éligibilité au crédit demeure annuelle même sans distribution, sans restaurer un acompte ou un IS annuel ordinaire ; aucune fiscalité personnelle des associés ni minimum international n'est modifié. "
            "Les références de travail fournies ne sont pas des renvois de ces crédits ; aucune indemnité, procédure collective ou protection spéciale n'est modifiée. "
            "Le coût de l'élargissement des dépenses antérieures à toute demande pour l'avenir n'est pas chiffré ; aucun autofinancement ou solde public net n'est affirmé."
        ) + europe_notes
        reason = (
            "Réforme de fond : suppression du double agrément culturel et des reprises fondées seulement sur son absence ou son délai pour les dépenses nouvelles, "
            "avec ouverture dès l'engagement et contrôle fiscal des conditions substantielles. Les taux, listes de dépenses, majorations PME, plafonds et dérogations favorables sont maintenus à droit constant. "
            "Coordination nécessaire du personnel affecté temporairement au contrat unique sans nouveau CDD et de la restitution du crédit à l'IS déclenché par la distribution, "
            "sans imposer de bénéfices simplement conservés ni de nouveau dépôt préalable."
        )

    obj = make(number, text, reason, notes)
    obj.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
               removed_provisions=removed, benefit_review=benefits + " Les effets favorables des décisions et agréments antérieurs sont également préservés pour les dépenses ultérieures de leur opération, dans leur champ et leur durée légaux, sans nouvelle demande.", reference_checks=checks(number))
    effects = [effect(
        'authorization_removed', measure,
        "Suppression du circuit provisoire/définitif d'agrément national et de sa sélection préalable, sans formalité de début de remplacement.",
        "Agrément provisoire demandé avant les dépenses éligibles, puis agrément définitif dans les délais de liquidation ; refus ou retard entraînant reprise.",
        "Dépenses nouvelles éligibles dès leur engagement sans agrément national ; mêmes taux, assiette substantielle et plafonds, sous contrôle fiscal et droit européen.",
        'legal_duty', population,
        "Dépenses engagées dès l'entrée en vigueur de la loi ; projets déjà commencés inclus pour leurs seules dépenses nouvelles. Régimes et avantages anciens conservés.",
        "Aucune déclaration de commencement, attestation, comité ou registre nouveau. Les déclarations fiscales de crédit, les contrôles et les contraintes européennes demeurent.",
        plain(old_approval),
        "Aucun agrément national provisoire ou définitif, ni demande préalable ou déclaration de commencement de la création, n'est exigé pour l'obtention du crédit d'impôt." if number == '220 terdecies' else
        "Aucun agrément national provisoire ou définitif, ni demande préalable ou déclaration de commencement des opérations, n'est exigé pour l'obtention du crédit d'impôt."
    )]
    if number == '220 terdecies':
        effects.append(effect(
            'relief_extended', measure,
            "Retrait de la fenêtre de dépenses calculée en remontant trente-six mois depuis l'agrément définitif pour les dépenses nouvelles.",
            "Crédit de 30 % sur les dépenses éligibles seulement dans les trente-six mois avant l'agrément définitif ; plafond 6 millions d'euros par exercice et sous-traitance 2 millions.",
            "Crédit de 30 % sur les mêmes dépenses nouvelles sans fenêtre liée à l'agrément ; plafonds 6 millions et 2 millions, échéance 31 décembre 2031 maintenus.",
            'other', population,
            "Dépenses nouvelles seulement ; pour les anciennes, maintien du régime 36/72 mois et des contrôles, sans remboursement rétroactif général.",
            "Aucun taux ou délai de réinvestissement ajouté ; contraintes d'aides d'État à coordonner, coût public non chiffré.",
            old_window,
            "Par dérogation à l'article 220 X, les dépenses relevant du présent 2 ne sont soumises à aucune limitation d'ancienneté calculée à partir de la délivrance d'un agrément."
        ))
    effects.append(effect(
        'coordination', 'is-distribution',
        "Conservation du calcul et de la restitution annuels du crédit en l'absence de distribution et donc d'IS ordinaire ; aucune deuxième baisse d'IS décomptée.",
        "Crédit calculé par année ou exercice sur les dépenses entrant dans le résultat imposable ; restitution par " + linked + " de l'excédent sur l'IS dû.",
        "Même crédit et restitution au titre de la dépense malgré conservation des bénéfices ; résultat de référence remplace l'assiette annuelle pour le nouveau régime.",
        'regime', population,
        "Pour les entreprises et exercices relevant du régime de distribution ; créances antérieures conservées, chaque crédit utilisé une seule fois.",
        "Pas de nouveau suivi distinct de crédit imposé ici ; liquidation existante, sans exigence de dividende ni d'acompte annuel sur bénéfices conservés.",
        old_result,
        "Le calcul annuel du crédit ne rend pas imposables les bénéfices conservés."
    ))
    if number != '220 terdecies':
        effects.append(effect(
            'coordination', 'contrat-unique-duree-indeterminee',
            "Maintien des dépenses des personnels affectés pour une période limitée dans les nouvelles embauches à durée indéterminée ; aucun nouveau CDD fiscal.",
            "Dépenses distinguées entre personnel permanent et non permanent sans condition expresse de CDD dans le texte fiscal.",
            "Distinction des catégories conservée selon l'affectation ; durée indéterminée de l'emploi n'excluant pas les personnels affectés temporairement.",
            'regime', population + " et leurs personnels affectés aux opérations éligibles",
            "Contrats nouveaux à durée indéterminée ; droits et contrats antérieurs soumis à leur transition, sans terme d'emploi lié à l'opération.",
            "Pas de déclaration d'emploi ni d'attestation nouvelle ; mêmes catégories et plafonds, pas de double décompte d'une rémunération.",
            "Les frais de personnel non permanent de l'entreprise",
            "La durée de cette affectation ne fixe pas le terme de l'emploi."
        ))
    obj['substantive_impact'] = impact(
        'material_reduction',
        "Par rapport à l'intégralité de la source officielle, la charge réellement retirée est le circuit d'agréments avec ses conditions de dépôt et de délai, non le crédit qui est conservé. "
        "L'accès aux dépenses nouvelles dès leur engagement élargit l'avantage, sous les règles européennes applicables. "
        "La conservation du crédit dans le contrat unique et l'IS à la distribution constitue une coordination et non une seconde suppression de taxe.",
        "Aucun solde net de complexité ou de coût pour l'ensemble des codes n'est établi. Les dépenses antérieures gardent leur régime ; les dates finales du dispositif ne sont pas prorogées. "
        "Les textes de liquidation et procédures ministérielles doivent être coordonnés conjointement ; les décisions et contraintes européennes ne sont pas réputées modifiées par la loi française.",
        "Aucune charge nouvelle n'est identifiée dans cette proposition : les déclarations fiscales de liquidation et contrôles existaient déjà ; ni registre, ni dossier préalable, ni attestation de remplacement ne sont créés. "
        "La conservation des preuves comptables reste celle du droit applicable. Le coût public d'un élargissement d'aide et des contrôles n'est pas chiffré ; aucun bilan global des codes n'est revendiqué.",
        effects)
    answer.append(obj)


text222 = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p>"
    "<p>Aucune déclaration d'existence, de modification du pacte social ou des conditions d'exercice de la profession ne peut être exigée sur le seul fondement du présent article "
    "ou de ses dispositions réglementaires d'application lorsque son échéance intervient à compter de cette date, y compris si elle concerne un événement antérieur. "
    "Aucune déclaration, attestation ou mise à jour de remplacement n'est instituée.</p>"
    "<p>Les formalités civiles, commerciales, sociales et fiscales reposant sur un fondement distinct demeurent applicables dans leur champ propre. "
    "La suppression de cette déclaration ne modifie ni l'assujettissement, ni une exonération, ni une option fiscale valablement exercée. "
    "Elle ne crée aucune imposition annuelle sur les bénéfices conservés relevant du régime d'imposition à la distribution.</p>"
    "<p>Les déclarations dont l'échéance est antérieure à cette entrée en vigueur, les contrôles, créances, restitutions, prescriptions et recours qui s'y rattachent restent régis "
    "par les dispositions antérieures, sous réserve de l'application des dispositions répressives plus douces. Aucune déclaration déjà déposée n'est à refaire.</p>"
)
obj = make('222', text222,
    "Abrogation de fond des déclarations fiscales distinctes d'existence et de modification du pacte social ou de l'activité, et de l'habilitation à fixer leurs délais et contenus. "
    "Ce circuit séparé ajoute un dépôt événementiel aux formalités d'identification et aux déclarations fiscales autonomes ; sa conservation générale n'a pas de fonction essentielle démontrée. "
    "Aucune déclaration équivalente n'est créée. Les déclarations de résultat nécessaires au suivi de l'IS à la distribution et les formalités distinctes restent à leur champ.",
    "La source et sa note ont été lues en entier. Annexe IV 23 A à E et 23 G lus intégralement : dépôt initial et modifications sous un mois, catégories de titres et apports, "
    "dirigeants, sociétés étrangères, établissements et organismes publics, et dispense déjà acquise aux organismes du 5 de 206. Aucun 23 F actif n'est présent dans le corpus fourni : "
    "ne pas prétendre avoir réécrit sept règlements. Les six articles actifs doivent recevoir la coordination d'abrogation pour les échéances nouvelles ; ils ne peuvent maintenir la déclaration sur l'ancien fondement de 222. "
    "Le 206 officiel et sa proposition ont été lus : assujettissement, franchise associative et régimes patrimoniaux autonomes restent sans changement ; "
    "la société étrangère n'est pas exclue de l'allègement mais les obligations autonomes de représentant fiscal ne sont pas supprimées. "
    "223, source et proposition lues, conserve la déclaration de référence et le suivi des distributions sans IS annuel ordinaire ; ce lot ne la réécrit pas. "
    "Les textes du guichet de formalités et d'immatriculation hors corpus ne sont pas déclarés modifiés ; aucune disponibilité universelle de leurs données n'est supposée, "
    "aucun accès nouveau à une donnée n'est créé. La suppression est celle d'un dépôt autonome, au-delà du seul réemploi déjà prévu par le CRPA. "
    "Les gains de traitement et de coût ne sont pas chiffrés ; la moindre notification spontanée doit être prise en compte dans l'organisation des contrôles existants.")
obj.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
           repeal_scope="Suppression des déclarations fiscales distinctes d'existence et de modification du pacte social et de l'activité pour toutes échéances à compter de la réforme, sans formulaire de remplacement.",
           reference_checks=[])
obj['substantive_impact'] = impact(
    'material_reduction',
    "La source entière n'institue qu'un circuit de déclarations événementielles et son habilitation réglementaire. Ce circuit est supprimé pour les échéances nouvelles ; "
    "le gain est le retrait réel du dépôt séparé et non une simple réutilisation de données ou un changement de mots.",
    "Les anciennes échéances gardent leurs effets sous réserve de la loi répressive plus douce. Immatriculation, options et autres obligations fiscales ou sociales ne sont pas abolies. "
    "La coordination de l'annexe IV reste à adopter ; aucun solde de coût ou de complexité de tous les codes n'est établi.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration équivalente, de registre, de transmission au guichet ni d'accès aux données supplémentaire. "
    "Les contrôles et les formalités sur fondement autonome étaient déjà applicables ; leur coût public reste inconnu.",
    [effect('obligation_removed', 'is-fin-declarations-existence-modifications',
        "Retrait du dépôt fiscal distinct d'existence et de modification de la personne morale.",
        "Sociétés, entreprises et associations de 206 : déclarations d'existence et de modification, avec modalités et délais réglementaires, dont un mois pour les cas de 23 A et 23 B.",
        "Aucun dépôt sur le fondement de 222 ou de ses règlements pour les échéances nouvelles ; mêmes obligations autonomes et options fiscales.",
        'legal_duty', "Sociétés, entreprises et associations visées à 206, y compris les organismes et sociétés étrangères dans leur champ actuel.",
        "Échéances à compter de l'entrée en vigueur, même pour événements antérieurs ; échéances déjà expirées et recours anciens préservés.",
        "Aucun dépôt de substitution ; les déclarations de résultat et formalités indépendantes subsistent sans extension.",
        "Les sociétés, entreprises et associations visées à l'article 206 sont tenues de faire des déclarations d'existence, de modification du pacte social et des conditions d'exercice de la profession",
        "Aucune déclaration, attestation ou mise à jour de remplacement n'est instituée.")])
answer.append(obj)


text222bis = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p>"
    "<p>Les organismes émettant des reçus, attestations ou autres documents ouvrant droit aux réductions d'impôt des articles 200, 238 bis et 978 ne sont plus tenus, "
    "sur le seul fondement du présent article, de déclarer annuellement le montant global des dons et versements et le nombre de documents délivrés. "
    "Cette suppression s'applique aux déclarations dont l'échéance intervient à compter de cette entrée en vigueur, même lorsqu'elles portent sur une année ou un exercice antérieur. "
    "Aucun état, dépôt ou déclaration de remplacement n'est exigé.</p>"
    "<p>Les réductions d'impôt des articles 200, 238 bis et 978 demeurent ouvertes aux dons et versements futurs qui remplissent leurs conditions. "
    "Leur bénéfice n'est pas subordonné au dépôt de l'état supprimé. Les règles distinctes relatives aux reçus et justificatifs des donateurs, à l'éligibilité des organismes, "
    "aux contrôles et à la répression des reçus irréguliers demeurent applicables. La dispense déjà prévue pour les organismes du 3 de l'article 200 ne peut être remise en cause par cette abrogation.</p>"
    "<p>Les déclarations dont l'échéance est antérieure à cette entrée en vigueur, les contrôles, prescriptions et recours correspondants restent régis par les dispositions antérieures, "
    "sous réserve de l'application des dispositions répressives plus douces. Aucun état déjà déposé n'est à refaire. "
    "La suppression de cet état ne dispense pas des déclarations dues sur un autre fondement ; leur contenu ne peut être augmenté pour rétablir l'état supprimé.</p>"
)
obj = make('222 bis', text222bis,
    "Abrogation de fond du reporting annuel agrégé des reçus de dons : deux totaux et un modèle fiscal distinct sont supprimés, sans état de remplacement. "
    "La fonction de contrôle de l'éligibilité et des reçus ne justifie pas à elle seule de conserver ce dépôt systématique de tous les organismes ; les pouvoirs de contrôle sur fondement autonome sont préservés. "
    "Les réductions pour dons, leurs bénéficiaires futurs et les pièces utiles aux donateurs restent expressément protégés.",
    "Source et note 2021 lues intégralement. L'abrogation porte uniquement sur la déclaration de montants globaux et de nombre de reçus, pas sur les réductions de 200, 238 bis et 978, "
    "ni sur les reçus eux-mêmes. La dispense du 3 de 200 reste protégée, y compris pour l'avenir ; aucun état n'est rétabli pour cette catégorie. "
    "Le renvoi à l'échéance de 223 devient sans objet pour ce seul état, sans retirer les déclarations annuelles autonomes. "
    "Les formulaires administratifs d'application et leurs rubriques de déclaration des dons doivent être retirés pour les nouvelles échéances ; leur contenu intégral n'est pas fourni. "
    "Le LPF, notamment les contrôles des reçus fiscaux et les pouvoirs distincts, et les sanctions autonomes ne sont pas réécrits dans le lot ; vérifier leurs renvois à 222 bis, "
    "en retirant seulement ceux destinés à sanctionner l'état aboli. Aucune nouvelle obligation documentaire n'est créée pour compenser la perte de l'agrégat. "
    "Les réclamations concernant les réductions des donateurs et la lutte contre les faux reçus restent distinctes. Aucun rendement ni coût public net du contrôle n'est inventé.")
obj.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
           repeal_scope="Suppression de la déclaration annuelle obligatoire des montants globaux de dons et du nombre de reçus pour les échéances nouvelles, avec maintien intégral des réductions pour dons et des contrôles autonomes.",
           reference_checks=[])
obj['substantive_impact'] = impact(
    'material_reduction',
    "La comparaison à toute la source établit le retrait de la déclaration annuelle de deux agrégats et de son modèle obligatoire. Les reçus et les avantages fiscaux ne sont pas abrogés ; "
    "il ne s'agit ni d'une baisse de leur taux ni d'une suppression des contrôles contre la fraude.",
    "Seules les échéances nouvelles sont dispensées ; les échéances déjà expirées gardent leur régime sous réserve répressive. Les pouvoirs de contrôle du LPF et les formulaires restent à coordonner, "
    "sans modification présumée de leur contenu non fourni. Aucun solde net de coûts de tous les codes n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : ni agrégat de remplacement, ni dépôt avec les reçus, ni registre nouveau. Les justificatifs et contrôles des dons sur fondement distinct préexistaient. "
    "La charge publique de contrôle après retrait de l'état n'est pas chiffrée.",
    [effect('obligation_removed', 'dons-fin-etat-annuel-recus',
        "Suppression de l'état annuel agrégé des dons et reçus délivrés, sans supprimer les réductions des donateurs.",
        "Organismes hors 200, 3 : déclaration annuelle du montant global des dons et du nombre de documents, à l'échéance de 223 et sur modèle fiscal imposé.",
        "Plus d'état annuel fondé sur 222 bis ; reçus, conditions des réductions 200/238 bis/978 et contrôles autonomes maintenus.",
        'legal_duty', "Organismes délivrant des documents ouvrant droit aux réductions pour dons, hors organismes déjà dispensés au 3 de 200.",
        "Échéances à compter de l'entrée en vigueur, y compris pour périodes antérieures ; régimes des échéances passées et recours préservés.",
        "Aucune déclaration de remplacement ni augmentation d'une autre déclaration pour reconstituer l'état ; obligations autonomes préexistantes conservées.",
        "le montant global des dons et versements mentionnés sur ces documents",
        "Aucun état, dépôt ou déclaration de remplacement n'est exigé.")])
answer.append(obj)


text223bis = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p>"
    "<p>Pour les liquidations et réclamations restant à effectuer à compter de cette date, dans les délais de prescription et de recours applicables, "
    "le bénéfice de l'article 219 ter n'est subordonné ni à une demande dans la déclaration des résultats de l'exercice du versement de l'indemnité, "
    "ni à un envoi systématique de justificatifs à l'appui d'une telle demande. Aucun formulaire, option ou attestation de remplacement n'est exigé. "
    "Le taux le plus favorable prévu à l'article 219 ter est appliqué à partir des éléments comptables et fiscaux établissant l'indemnité et la déduction d'origine. "
    "Les pouvoirs de contrôle et de demande de justifications sur un fondement distinct demeurent applicables.</p>"
    "<p>L'avantage de l'article 219 ter demeure ouvert aux indemnités futures qui en remplissent les conditions. "
    "Pour les bénéfices relevant de l'imposition à la distribution, il reste applicable lors de leur distribution sans impôt ordinaire sur leur seule conservation "
    "et sans seconde imposition d'une fraction déjà taxée. La dispense de demande ne constitue pas un crédit remboursable en l'absence d'impôt dû.</p>"
    "<p>Les demandes déjà présentées, les créances, contrôles, restitutions, prescriptions et recours antérieurs conservent leurs effets. "
    "La suppression de la demande distincte n'impose de refaire aucune demande ni déclaration antérieure, ne rouvre aucun délai expiré et ne crée aucune restitution générale d'une imposition définitive.</p>"
)
obj = make('223 bis', text223bis,
    "Abrogation de la seule norme procédurale de l'article : demande spéciale, dépôt obligatoire dans l'exercice du versement et envoi systématique de toutes justifications utiles. "
    "Coordination de fond avec le 219 ter proposé, qui applique automatiquement le taux historique lorsqu'il est plus favorable ; l'avantage reste ouvert aux indemnités futures et aux situations non prescrites. "
    "Les contrôles sur pièces et les droits anciens restent, sans nouvelle déclaration et sans déclencher d'IS ordinaire à la seule perception de l'indemnité conservée.",
    "Source officielle entière et 219 ter source/proposition de reference-targets.json lus. Le 219 ter officiel comporte une option pouvant être défavorable si le taux historique dépasse le taux normal ; "
    "sa proposition fournie retient le minimum et supprime la demande. 223 bis doit être adopté conjointement avec cette réécriture de 219 ter : il ne faut pas laisser dans celui-ci la formule officielle sur demande. "
    "Le présent texte ne supprime pas le régime du taux historique, n'invente pas son montant et ne rembourse pas un crédit sans impôt français. "
    "Le calcul doit conserver la fraction éligible jusqu'à sa distribution et exclure toute seconde imposition d'anciennes réserves déjà taxées. "
    "Les déclarations fiscales générales et leurs rubriques d'option doivent être coordonnées sans rétablir la demande supprimée ; les modalités administratives non fournies ne sont pas présentées comme réécrites. "
    "Les trois cibles de travail imposées par requirements sont sans lien avec cet article : le mot indemnité concerne un sinistre de guerre subi par une entreprise et non une rupture d'emploi. "
    "Aucune ancienneté d'un an, fraction de 0,20 mois, plafond salarial ou préavis de quinze jours ne doit être importé ici. "
    "L'économie de démarche est dédupliquée avec 219 ter sous une seule mesure, sans deuxième avantage fiscal ou baisse d'IS compté. Pas de recette compensatrice ni de gain national chiffré.")
obj.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
           repeal_scope="Suppression de la demande fiscale spéciale et de son envoi systématique de justificatifs pour obtenir le taux favorable des indemnités de guerre, sans extinction de l'avantage de 219 ter.",
           reference_checks=checks('223 bis'))
obj['substantive_impact'] = impact(
    'coordination_only',
    "Toute la source est une obligation de demande et de justification. Son abrogation matérialise la dispense déjà décidée dans la proposition de 219 ter. "
    "La démarche disparaît bien par rapport à la source officielle, mais ne constitue pas une seconde mesure ou baisse de taux à additionner à 219 ter.",
    "Adoption conjointe de 219 ter indispensable, sa source officielle exigeant encore une demande. Les situations prescrites ou définitivement imposées ne sont pas rouvertes. "
    "Le taux historique dépend des exercices de déduction et n'est pas chiffré ici ; aucune baisse nette de fiscalité ou de complexité de tout le corpus n'est établie.",
    "Aucune charge nouvelle n'est identifiée : pas d'option, formulaire ou attestation de remplacement ; les éléments comptables d'origine et les pouvoirs de contrôle étaient déjà nécessaires. "
    "La constatation du taux favorable reste un traitement fiscal existant et aucun registre distinct n'est institué.",
    [effect('coordination', 'indemnites-guerre-taux-favorable-sans-demande',
        "Retrait du support procédural de la demande, coordonné à son abolition dans 219 ter sans double comptage.",
        "Demande dans la déclaration de l'exercice où l'indemnité est versée, accompagnée de toutes justifications utiles, pour le régime historique de 219 ter.",
        "Taux le plus favorable de 219 ter sans demande spéciale ni dépôt systématique de pièces ; contrôles et régime de distribution conservés.",
        'legal_duty', "Entreprises sinistrées par faits de guerre percevant les indemnités de réparation d'immobilisations ou de remplacement de stocks de 219 ter.",
        "Liquidations et réclamations restant à effectuer dès l'entrée en vigueur, dans les délais existants ; demandes anciennes et avantage futur protégés.",
        "Aucune procédure équivalente ; pas d'automatisme de remboursement sans dette fiscale, pas de pièces nouvelles hors pouvoirs légaux distincts.",
        "les entreprises doivent en faire la demande dans la déclaration des résultats de l'exercice au cours duquel lesdites indemnités sont versées",
        "Aucun formulaire, option ou attestation de remplacement n'est exigé.")])
answer.append(obj)


assert len(answer) == len(sources) == 7
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json écrit :', len(answer), 'articles')
