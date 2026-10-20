import html
import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}


def paragraphs(xml):
    return re.findall(r'<p>(.*?)</p>', xml, re.S)


def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml))


def followup_decision(paragraph):
    text = plain(paragraph)
    return text[text.index('Celui-ci'):text.index('Cet administrateur')].strip()


def base(number):
    source = by_number[number]
    return {key: source[key] for key in
            ('code_id', 'source_id', 'source_sha256', 'number')}


answer = []

a = base('L422-3-1')
a.update(
    proposed_xml=None,
    reason=(
        "Maintien intégral utile, sans nouveau corps ni gain de simplification revendiqué. "
        "L'obligation porte uniquement sur la présence des locataires dans l'organe de "
        "gouvernance d'une coopérative HLM qui gère des locations ; elle protège la "
        "participation des occupants aux décisions de leur bailleur. Les modalités sont "
        "déjà laissées aux statuts : l'article n'ajoute ni agrément, ni déclaration, ni "
        "justificatif, ni délai minimal, ni prélèvement. L. 422-3-2 vise spécialement "
        "les SCIC-HLM et ne permet pas de supprimer la garantie pour les autres "
        "coopératives. Après examen de la source entière et du précédent brouillon, "
        "sa reformulation purement stylistique est abandonnée au profit du texte source."
    ),
    review_notes=(
        "Source, notes vides et previous_draft lus intégralement. Le 8° de SRU 149, "
        "fourni en entier, rétablit expressément cette représentation ; cette filiation "
        "ne justifie pas sa suppression. Comparaison locale avec L. 422-3-2 et les "
        "clauses pertinentes de l'annexe à R. 422-6 : cette dernière prévoit au moins "
        "un représentant des coopérateurs locataires désigné par l'assemblée générale, "
        "pour le conseil d'administration comme pour le conseil de surveillance. "
        "L'article n'impose pas lui-même un scrutin, un nombre de sièges ou une "
        "adhésion nouvelle des locataires. Ne pas confondre cette garantie avec la "
        "révision coopérative périodique supprimée dans les coordinations L. 422-3 "
        "et L. 422-3-2. Incohérence préexistante signalée : les clauses 8A et 8B des "
        "annexes I et II à R. 423-86 se réfèrent à une dernière élection prévue par "
        "L. 422-3-1, alors que ce dernier renvoie aux statuts et que la clause type "
        "de R. 422-6 prévoit une désignation par l'assemblée. Le calcul des voix de "
        "ces collèges appelle une coordination propre de ces annexes, non rédigée "
        "dans ce lot ; aucun scrutin fictif n'est créé ici. Aucun tableau ni pièce "
        "source_companions dans la source assignée. Aucun achèvement du volet "
        "SRU 149 entier ou des 209 articles n'est affirmé."
    ),
    status='retained_unchanged',
    classification='retained_necessary',
    benefit_review=(
        "La représentation des locataires est un droit de participation maintenu "
        "intégralement pour les activités locatives présentes et futures, dans les "
        "deux formes de gouvernance visées. La latitude statutaire sur ses modalités "
        "reste intacte. L'article ne comporte aucune exonération fiscale ou sociale "
        "et aucune dispense de formalité qu'il serait nécessaire de réécrire."
    ),
    substantive_impact={
        'version': 1,
        'classification': 'retained_necessary',
        'assessment': (
            "Aucun changement normatif par rapport à la source officielle entière : "
            "la représentation des locataires demeure obligatoire seulement pour "
            "les coopératives exerçant une gestion locative, selon leurs statuts. "
            "La protection et son champ justifient ce maintien ; le précédent "
            "changement de formulation ne constituait pas une réduction."
        ),
        'scope_limitations': (
            "Aucune baisse de taxe, de coût ou d'obligation n'est démontrée pour "
            "cet article. Les règles de représentation des autres organismes et "
            "la difficulté du calcul des voix dans les annexes à R. 423-86 ne "
            "sont pas réécrites ici ; ce maintien ne solde pas SRU 149."
        ),
        'new_burdens_review': (
            "Aucune charge nouvelle n'est identifiée : aucun texte n'est ajouté "
            "et l'obligation existante de représentation demeure à l'identique, "
            "sans nouveau registre, donnée, délai ou condition statutaire. "
            "Aucun solde global de complexité n'en est déduit."
        ),
        'effects': [],
    },
)
answer.append(a)


source = by_number['L422-8']
old = paragraphs(source['source_xml'])
assert len(old) == 5
new = old[:3]
new.append(
    "Pendant une durée de deux ans à l'issue de la mission de l'administrateur "
    "provisoire, ce dernier peut être invité à assister aux réunions du conseil "
    "d'administration ou du conseil de surveillance de la société et aux assemblées "
    "générales des actionnaires. La société n'est pas tenue de le convoquer à ces "
    "réunions et il ne dispose pas d'un droit automatique d'y assister."
)
new.append(old[4].replace(
    "Celui-ci, en accord avec le ministre de l'économie et des finances, peut, aprés",
    "Celui-ci peut, après",
))
assert new[4] != old[4]
new.append(
    "La suppression de la convocation obligatoire et du droit automatique "
    "d'assistance s'applique aux réunions tenues à compter de l'entrée en vigueur "
    "de la présente loi, y compris lorsque la mission a pris fin auparavant. "
    "La suppression de l'accord du ministre de l'économie et des finances "
    "s'applique aux décisions prises à compter de cette même date, y compris "
    "dans les procédures en cours, sans reprise de la procédure du seul fait "
    "de cette suppression. Les décisions antérieures, les mandats en cours, "
    "les droits acquis et les recours sont préservés. Les contrôles de l'Agence "
    "nationale de contrôle du logement social demeurent applicables. La période "
    "de deux ans n'est ni interrompue ni renouvelée."
)
proposed = '\n'.join('<p>' + p.strip() + '</p>' for p in new)

a = base('L422-8')
a.update(
    proposed_xml=proposed,
    reason=(
        "Réduction de fond, comparée aux cinq alinéas entiers de la source : "
        "la convocation à chaque réunion et le droit automatique d'assistance "
        "de l'ancien administrateur provisoire pendant deux ans sont supprimés, "
        "conformément à la coordination déjà retenue. Coupe supplémentaire de "
        "seconde passe : le ministre chargé du logement décide des mesures du "
        "suivi sans devoir obtenir l'accord du ministre de l'économie et des "
        "finances. Ce second accord est un circuit de codécision administrative, "
        "non une expertise, une garantie financière ou une condition d'aide "
        "distinctement définie par cet article ; les observations de la société, "
        "le contrôle public et le recours subsistent. Aucun accord, dépôt ou "
        "déclaration de remplacement n'est institué. Les trois premiers alinéas "
        "sont maintenus intégralement : l'agrément du capital et des actions "
        "pendant la mission protège un redressement encore en cours ; la "
        "recapitalisation soutenue par la Caisse et la reconstitution des organes "
        "de gouvernance restent opérantes. Le signalement, la durée du suivi, "
        "les mesures de sauvegarde et la réunion de l'assemblée demeurent."
    ),
    review_notes=(
        "Source, notes vides et brouillon précédent lus intégralement. Les cinq "
        "positions d'alinéas sont conservées et une transition finale est ajoutée. "
        "La suppression des convocations déjà acquise est conservée ; la suppression "
        "du second accord ministériel est nouvelle. Les deux ans du quatrième "
        "alinéa sont le suivi après mission et non la durée de l'administration "
        "provisoire. L. 342-14, lu intégralement dans le corpus, maintient notamment "
        "le transfert des pouvoirs sous réserve de ceux de l'assemblée, la durée "
        "maximale de deux ans de la mission et la dissolution-sanction avec son "
        "affectation spéciale du boni. Les renvois à cet article et au livre II "
        "du code de commerce, notamment L. 225-129, L. 225-204 et L. 228-23, sont "
        "conservés : aucun pouvoir de l'administrateur en fonction n'est retiré. "
        "Le code de commerce n'est pas joint au corpus des cinq codes : sa "
        "concordance complète n'est pas présentée comme vérifiée. La Caisse de "
        "garantie du logement social, les plans de sauvegarde comme de redressement, "
        "le refus de l'assemblée et la décision de recapitalisation de la Caisse "
        "sont maintenus sans nouvelle condition. Le ministre du logement doit "
        "toujours entendre la société ; ni liquidation automatique supplémentaire "
        "ni transmission périodique ne sont créées. Adapter les circuits et "
        "éventuelles instructions de suivi à l'absence d'accord du ministre de "
        "l'économie, sans nouveau visa ; ces textes extérieurs et les actes "
        "individuels ne sont pas réécrits ici. SRU 149, lu en entier, modifiait "
        "notamment le contrôle du capital et le plan de redressement ; la version "
        "actuelle renvoie à L. 342-14 et vise aussi les plans de sauvegarde. "
        "Les deux alinéas de suivi ne figurent pas dans le texte initial fourni : "
        "leur filiation exacte n'est pas établie par ce dossier. Leur allègement "
        "repose sur l'orientation actuelle, pas sur une attribution globale à SRU. "
        "Aucun tableau ni source_companions. La correction d'accent de « aprés » "
        "en « après » ne constitue pas une réduction. Aucun rendement budgétaire "
        "ni solde national de complexité n'est chiffré."
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Convocation obligatoire de l'ancien administrateur provisoire à toutes "
        "les réunions du conseil et assemblées générales pendant les deux ans "
        "suivant la fin de sa mission, avec droit automatique d'assistance.",
        "Accord préalable du ministre de l'économie et des finances à la décision "
        "du ministre chargé du logement prise après signalement d'une défaillance "
        "du redressement pendant la période de suivi de deux ans.",
    ],
    benefit_review=(
        "Les dérogations au livre II du code de commerce pendant l'administration "
        "provisoire restent intégrales, y compris l'agrément et sa nullité ; elles "
        "organisent un contrôle ciblé, non une exonération fiscale. La faculté "
        "pour l'administrateur de proposer la recapitalisation nécessaire aux "
        "plans approuvés et la décision de la Caisse en cas de refus de l'assemblée "
        "restent ouvertes à tous les futurs plans éligibles, de sauvegarde comme "
        "de redressement. La possibilité de suspendre et de redresser plutôt que "
        "de dissoudre, ainsi que les observations de la société et les recours, "
        "demeurent. Le droit d'assistance de l'ancien administrateur est retiré "
        "conformément à la décision explicite de coordination : il s'agit d'une "
        "prérogative de suivi attachée à une fonction terminée, pas d'une "
        "exonération ou dérogation favorable aux sociétés ou aux locataires. "
        "L'accord du ministre de l'économie est une codécision institutionnelle, "
        "non une aide ou une dispense ; sa suppression ne ferme aucun régime "
        "de soutien ni aucune voie de contestation. Les décisions antérieures, "
        "mandats, droits acquis et contrôles autonomes sont préservés."
    ),
    substantive_impact={
        'version': 1,
        'classification': 'material_reduction',
        'assessment': (
            "Par rapport à la source officielle entière, suppression effective "
            "des convocations systématiques et de l'assistance de droit après "
            "mission, déjà prévue au brouillon, et suppression supplémentaire "
            "de la codécision du ministre de l'économie pour les mesures de "
            "suivi. Les agréments pendant la mission, le signalement, les deux "
            "ans de suivi et les garanties de redressement sont maintenus. "
            "Aucune baisse de prélèvement n'est revendiquée."
        ),
        'scope_limitations': (
            "Le gain administratif du retrait du second accord concerne le "
            "circuit entre ministres ; aucune diminution chiffrée de délai "
            "ou de coût pour la société n'est démontrée. Les agréments de "
            "capital et de cession pendant la mission restent. Les circuits "
            "extérieurs doivent être coordonnés ; le solde net de coût de "
            "l'ensemble des codes demeure inconnu."
        ),
        'new_burdens_review': (
            "Aucune charge nouvelle n'est identifiée : l'invitation de l'ancien "
            "administrateur est facultative ; aucun rapport, registre, envoi, "
            "nouvelle donnée, condition d'aide ou autorisation de remplacement "
            "n'est créé. Le signalement et le contradictoire restent ceux de "
            "la source, sans redémarrage de la période de suivi."
        ),
        'effects': [
            {
                'kind': 'obligation_removed',
                'measure_id': 'hlm-administration-provisoire-fin-convocations-systematiques',
                'description': (
                    "Suppression de la convocation obligatoire et du droit "
                    "automatique d'assistance de l'ancien administrateur ; "
                    "une invitation reste facultative."
                ),
                'before': (
                    "La société convoque l'ancien administrateur à toutes les "
                    "réunions du conseil d'administration ou de surveillance "
                    "et aux assemblées générales pendant deux ans après sa "
                    "mission ; celui-ci peut y assister de droit."
                ),
                'after': (
                    "Aucune convocation obligatoire ni assistance de droit "
                    "au titre de cette ancienne fonction ; une invitation "
                    "volontaire reste possible pendant le suivi de deux ans."
                ),
                'unit': 'legal_duty',
                'affected_population': (
                    "Sociétés HLM sortant d'administration provisoire et "
                    "anciens administrateurs concernés."
                ),
                'conditions_and_transition': (
                    "Réunions tenues dès l'entrée en vigueur de la loi, "
                    "même si la mission a pris fin avant ; période de deux "
                    "ans non interrompue ni renouvelée, droits antérieurs "
                    "et contrôles autonomes conservés."
                ),
                'replacement_or_new_burdens': (
                    "Aucune convocation, déclaration ou transmission de "
                    "remplacement ; le signalement existant demeure."
                ),
                'source_quote': plain(old[3]).strip(),
                'proposed_quote': new[3],
            },
            {
                'kind': 'authorization_removed',
                'measure_id': 'hlm-suivi-administration-fin-accord-ministre-economie',
                'description': (
                    "Retrait du second accord ministériel pour les décisions "
                    "de suivi, la compétence du ministre du logement étant conservée."
                ),
                'before': (
                    "Pendant les deux ans de suivi, le ministre du logement "
                    "ne prend les mesures du cinquième alinéa qu'en accord "
                    "avec le ministre de l'économie et des finances et après "
                    "observations de la société."
                ),
                'after': (
                    "Le ministre du logement prend ces mêmes mesures après "
                    "observations de la société, sans l'accord distinct du "
                    "ministre de l'économie et des finances."
                ),
                'unit': 'legal_duty',
                'affected_population': (
                    "Ministres chargés du logement et de l'économie ; "
                    "sociétés HLM faisant l'objet du suivi après mission."
                ),
                'conditions_and_transition': (
                    "Décisions prises dès l'entrée en vigueur, y compris "
                    "procédures en cours sans reprise du seul fait de la "
                    "suppression ; décisions anciennes et recours préservés."
                ),
                'replacement_or_new_burdens': (
                    "Aucun visa ni dossier de substitution ; pouvoir de "
                    "dissolution ou de nouvelle suspension, observations "
                    "de la société et contrôle juridictionnel conservés."
                ),
                'source_quote': followup_decision(old[4]),
                'proposed_quote': followup_decision(new[4]),
            },
        ],
    },
)
answer.append(a)


source = by_number['L422-8-1']
old = paragraphs(source['source_xml'])
assert len(old) == 2
new = [
    "Pendant la durée des opérations de liquidation consécutives à une "
    "dissolution prononcée dans les conditions prévues à l'article L. 342-14, "
    "toute opération portant sur le capital de la société est soumise à "
    "l'agrément du liquidateur, à peine de nullité. Les cessions d'actions "
    "qui ne modifient pas le capital social sont dispensées de cet agrément "
    "et de toute formalité équivalente fondée sur la seule liquidation. "
    "Les règles de cession applicables sur un autre fondement demeurent applicables.",
    old[1].strip(),
    "La dispense d'agrément des cessions d'actions sans modification du capital "
    "social s'applique aux cessions conclues à compter de l'entrée en vigueur "
    "de la présente loi, y compris lorsqu'une liquidation est déjà en cours. "
    "Les demandes d'agrément présentées au liquidateur qui portent exclusivement "
    "sur ces cessions deviennent sans objet. Les cessions conclues avant cette "
    "date demeurent régies par les dispositions antérieurement applicables ; "
    "aucune validation rétroactive n'est opérée. Les droits des tiers et les "
    "recours relatifs aux actes antérieurs sont préservés.",
]
proposed = '\n'.join('<p>' + p + '</p>' for p in new)
a = base('L422-8-1')
a.update(
    proposed_xml=proposed,
    reason=(
        "Réduction de fond supplémentaire par rapport au brouillon qui ne "
        "changeait que la rédaction : suppression de l'agrément spécial du "
        "liquidateur et de la nullité attachée à son absence pour les seules "
        "cessions d'actions sans modification du capital social. Le changement "
        "de titulaire des titres ne soustrait pas, par lui-même, d'actif à la "
        "liquidation et ne dessaisit pas le liquidateur de sa mission ; "
        "les règles autonomes de prix, de cession et d'affectation des actifs "
        "restent applicables. Ce contrôle supplémentaire n'est donc pas "
        "maintenu pour une simple cession. En revanche, l'agrément et la "
        "nullité demeurent pour les opérations sur le capital, qui affectent "
        "directement la structure patrimoniale en liquidation. Le second "
        "alinéa est maintenu intégralement : l'autorisation du ministre du "
        "logement permet de surmonter le refus d'une cession d'actif par "
        "l'assemblée sans laisser le liquidateur écarter seul ce refus. "
        "Aucune déclaration ou autorisation équivalente ne remplace l'agrément "
        "retiré ; la transition distingue les cessions nouvelles des actes anciens."
    ),
    review_notes=(
        "Source, notes vides, précédent brouillon et texte initial SRU 149 "
        "lus intégralement ; aucun tableau ni source_companions. La création "
        "de L. 422-8-1 figure au 5° de SRU 149. Le texte actuel vise L. 342-14 "
        "et le ministre chargé du logement, là où le texte initial visait "
        "L. 422-7 et l'autorité administrative : ces renvois actuels sont "
        "conservés, sans retour au texte de 2000. L. 342-14, L. 422-11, "
        "L. 422-12, L. 423-4 et L. 423-5 ont été lus dans le corpus. "
        "La dispense ne concerne ni une augmentation ou réduction du capital, "
        "ni un rachat suivi d'une réduction du capital, ni l'agrément de "
        "L. 422-8 pendant l'administration provisoire, ni une liquidation "
        "volontaire. Les plafonds de prix, le dépôt de l'acte de cession "
        "dans son champ propre et les autres causes de nullité de L. 423-4 "
        "ne sont pas abolis. Les clauses de cession des annexes à R. 422-6 "
        "(7) et R. 422-37 (6), lues entièrement, gardent leurs dispenses pour "
        "succession, liquidation de communauté et cessions au conjoint, à "
        "un ascendant ou à un descendant ; les agréments autonomes pour "
        "certains transferts à des tiers ne sont pas supprimés. Ces clauses "
        "évoquent aussi une dérogation au prix de cession dans les conditions "
        "de L. 423-4, dont la source actuelle lue ne prévoit pas cette "
        "habilitation : incohérence préexistante à vérifier dans ces "
        "annexes, sans supprimer ici une dérogation favorable ni inventer "
        "une nouvelle autorité d'octroi. Les règles de capital de L. 423-5 et leurs "
        "dérogations demeurent. Le contrôle des cessions d'actif après refus "
        "de l'assemblée est une garantie distincte et une voie de déblocage "
        "maintenue, y compris pour les liquidations futures. Le paiement "
        "du passif, le remboursement du capital effectivement versé et "
        "l'affectation de l'actif de L. 422-11 restent distincts ; la "
        "dissolution-sanction garde l'affectation spéciale du boni prévue "
        "par L. 342-14. Il existe une différence de bénéficiaires et de "
        "périmètre entre ces deux règles d'affectation, non nivelée ici. "
        "La recherche des renvois explicites dans le corpus CCH n'a pas "
        "trouvé de renvoi direct imposant de réécrire un autre article pour "
        "cette seule dispense ; les clauses statutaires et actes de mission "
        "qui reprennent l'ancien agrément spécial doivent cesser de l'exiger "
        "dans le champ dispensé. Leur inventaire extérieur n'est pas déclaré "
        "exhaustif. Les règles de cession du code de commerce hors corpus "
        "ne sont ni abrogées ni présentées comme intégralement vérifiées. "
        "Les baux, droits des occupants, sûretés, créances, aides et "
        "obligations autonomes de service d'intérêt économique général "
        "demeurent ; aucun remboursement, droit de distribution ou garantie "
        "publique nouvelle n'est créé. Cet examen de ce descendant n'achève "
        "pas l'article 149 de SRU ni le périmètre des 209 articles."
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Agrément spécial du liquidateur, assorti d'une nullité, exigé "
        "pour chaque cession d'actions sans modification du capital "
        "pendant une liquidation consécutive à une dissolution de L. 342-14.",
    ],
    benefit_review=(
        "L'autorisation du ministre après refus d'une cession d'actif "
        "par l'assemblée constitue aussi une possibilité de débloquer "
        "la liquidation : elle reste intégralement ouverte aux situations "
        "futures éligibles. La dispense nouvelle ne restreint aucune "
        "dérogation autonome relative aux cessions, au capital ou aux actifs, "
        "et ne modifie pas les droits des créanciers ou des locataires. "
        "Les dispenses des clauses types pour successions, liquidations de "
        "communauté et transferts au conjoint, aux ascendants ou descendants "
        "restent applicables dans leur champ aux situations futures également. "
        "L'agrément retiré pour les seuls transferts de titres n'est pas "
        "une exonération fiscale ; le contrôle patrimonial des opérations "
        "sur le capital reste assorti de sa nullité."
    ),
    substantive_impact={
        'version': 1,
        'classification': 'material_reduction',
        'assessment': (
            "Par rapport aux deux alinéas entiers de la source officielle, "
            "un agrément préalable et la cause de nullité correspondante "
            "sont effectivement retirés pour les cessions d'actions sans "
            "modification du capital. Les opérations modifiant le capital "
            "et les cessions d'actif refusées par l'assemblée conservent "
            "leurs contrôles. Il s'agit d'une coupe nouvelle de seconde "
            "passe, non d'une suppression générale des contrôles de liquidation."
        ),
        'scope_limitations': (
            "Le retrait concerne uniquement l'agrément dû en raison de la "
            "liquidation imposée de L. 342-14. Les agréments et règles "
            "autonomes de cession, les prix maximaux, les dépôts et les "
            "droits des tiers gardent leur champ ; notamment, l'agrément "
            "statutaire de certaines cessions à des tiers peut subsister. "
            "Aucune liberté générale de cession n'est revendiquée. Aucun coût, délai "
            "économisé ou solde global n'est chiffré ; les clauses "
            "et actes extérieurs restent à coordonner."
        ),
        'new_burdens_review': (
            "Aucune charge nouvelle n'est identifiée : la dispense n'est "
            "remplacée ni par déclaration, registre ou attestation ni par "
            "un autre accord lié à la liquidation. La réserve des règles "
            "sur un autre fondement maintient les obligations existantes "
            "sans créer un dépôt ni un contrôle supplémentaires."
        ),
        'effects': [
            {
                'kind': 'authorization_removed',
                'measure_id': 'hlm-liquidation-fin-agrement-cessions-actions',
                'description': (
                    "Suppression de l'agrément du liquidateur pour les "
                    "cessions d'actions ne modifiant pas le capital et "
                    "de la nullité pour le seul défaut de cet agrément."
                ),
                'before': (
                    "Toute cession d'action pendant la liquidation "
                    "consécutive à une dissolution de L. 342-14 est "
                    "soumise à l'agrément du liquidateur, à peine de nullité."
                ),
                'after': (
                    "Les cessions d'actions sans modification du capital "
                    "sont dispensées de cet agrément et d'une formalité "
                    "équivalente fondée sur la seule liquidation ; les "
                    "opérations sur le capital restent agréées à peine "
                    "de nullité et les règles autonomes de cession demeurent."
                ),
                'unit': 'legal_duty',
                'affected_population': (
                    "Cédants, acquéreurs et liquidateurs des sociétés "
                    "HLM dissoutes dans le champ de L. 342-14."
                ),
                'conditions_and_transition': (
                    "Cessions conclues dès l'entrée en vigueur, même "
                    "dans une liquidation en cours ; demandes portant "
                    "exclusivement sur elles sans objet ; actes antérieurs "
                    "et recours préservés, sans validation rétroactive."
                ),
                'replacement_or_new_burdens': (
                    "Aucune formalité de remplacement liée à la liquidation. "
                    "Les contrôles de capital et l'autorisation ministérielle "
                    "de cession d'actif après refus de l'assemblée restent "
                    "des règles distinctes déjà présentes."
                ),
                'source_quote': plain(old[0]).strip(),
                'proposed_quote': new[0],
            },
        ],
    },
)
answer.append(a)

Path('answer.json').write_text(
    json.dumps(answer, ensure_ascii=False, indent=2) + '\n'
)
print('answer.json :', len(answer), 'articles')
