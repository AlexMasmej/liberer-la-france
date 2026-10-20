import json
import re
import html
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFERENCES = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}
RESULT = {}


def text(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))


def paras(number):
    return re.findall(r'<p>(.*?)</p>', BY_NUMBER[number]['source_xml'], re.S)


def wrap(parts):
    return '\n'.join('<p>' + p + '</p>' for p in parts)


def retain(number, reason, notes, assessment, limits, burdens):
    s = BY_NUMBER[number]
    RESULT[number] = {
        **{k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']},
        'proposed_xml': None, 'reason': reason, 'review_notes': notes,
        'status': 'retained_unchanged', 'classification': 'retained_necessary',
        'substantive_impact': {
            'version': 1, 'classification': 'retained_necessary',
            'assessment': assessment, 'scope_limitations': limits,
            'new_burdens_review': burdens, 'effects': [],
        },
    }


def rewrite(number, parts, reason, notes, classification, assessment, limits, burdens, removed=None):
    s = BY_NUMBER[number]
    RESULT[number] = {
        **{k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']},
        'proposed_xml': wrap(parts), 'reason': reason, 'review_notes': notes,
        'status': 'rewrite_draft',
        'substantive_impact': {
            'version': 1, 'classification': classification,
            'assessment': assessment, 'scope_limitations': limits,
            'new_burdens_review': burdens, 'effects': [],
        },
    }
    if removed:
        RESULT[number].update(change_type='normative_reduction',
                              reform_policy_id='editorial_direction_2026_10_19',
                              removed_provisions=removed)


def effect(number, kind, measure_id, description, before, after, unit, population,
           transition, new_burdens, source_quote, proposed_quote):
    assert source_quote in text(BY_NUMBER[number]['source_xml']), (number, source_quote)
    assert proposed_quote in text(RESULT[number]['proposed_xml']), (number, proposed_quote)
    RESULT[number]['substantive_impact']['effects'].append({
        'kind': kind, 'measure_id': measure_id, 'description': description,
        'before': before, 'after': after, 'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': new_burdens,
        'source_quote': source_quote, 'proposed_quote': proposed_quote,
    })


retain('L442-5',
    "Maintien intégral du renvoi aux contrôles médicaux des articles L. 315-1 et L. 315-2 : il étend aux accidents du travail les compétences médicales, les garanties de défense et de secret, les avis et les recours. Ce renvoi évite un régime de contrôle parallèle. Ses effets suivront les modifications coordonnées des cibles, sans nouvelle réécriture de cet article.",
    "Les deux cibles ont été lues intégralement, sources et propositions distinguées. Les retraits proposés du contrôle systématique fondé sur le seul volume statistique et des accords préalables exclusivement économiques ne sont pas comptés une seconde fois ici. Les contrôles individuels médicalement justifiés, les droits des assurés et les règles propres aux accidents du travail demeurent. Aucun renvoi à une règle de préavis ou d'indemnité ordinaire de rupture.",
    "L'article source ne crée ni déclaration autonome, ni cotisation, ni délai supplémentaire : il mutualise un contrôle médical nécessaire. Aucun allègement propre à cet article n'est démontré.",
    "Les réductions portées par les propositions L. 315-1 et L. 315-2 restent des mesures de ces cibles ; le présent maintien ne constitue ni leur adoption en droit positif ni une nouvelle économie.",
    "Aucune charge nouvelle identifiée : le texte source est maintenu sans ajouter formulaire, donnée, convocation ou condition d'ancienneté.")

retain('L442-6',
    "Maintien intégral de la fixation par la caisse de la guérison ou de la consolidation sur avis du médecin traitant. Cette décision détermine le passage entre soins, incapacité temporaire et réparation permanente ; supprimer la compétence ou l'avis médical fragiliserait les droits, sans enlever une formalité redondante identifiée.",
    "La note de la loi du 24 décembre 2019 concerne l'application aux contestations et recours, au plus tard le 1er janvier 2022 ; elle ne fixe pas la date de la réforme proposée. Aucun délai minimal, agrément ou prélèvement autonome dans cet article. Les procédures de contestation ne sont pas supprimées.",
    "La règle conserve un fondement médical à une décision qui ouvre et articule des prestations. L'examen entier de la source ne révèle pas de circuit doublonné à retirer dans cette disposition.",
    "Le maintien ne tranche pas les désaccords médicaux individuels et ne modifie pas les règles de calcul des prestations ou les voies de recours situées ailleurs.",
    "Aucune charge nouvelle identifiée : ni nouvelle pièce médicale ni nouvelle échéance n'est créée par le maintien de la compétence existante.")

retain('L442-7',
    "Maintien intégral de l'extension des articles L. 145-1 et L. 145-4 aux soins des victimes d'accidents du travail. La discipline des fautes, abus et fraudes des soignants et ses adaptations aux pharmaciens et auxiliaires médicaux protègent les patients et les fonds sociaux ; ce n'est pas un agrément supplémentaire à l'accès aux soins.",
    "L. 145-1 et L. 145-4 ont été lus dans le corpus public : le premier organise les sections des assurances sociales des juridictions ordinales ; le second habilite les adaptations et la procédure. Aucun renvoi au contrat unique et aucun avantage fiscal à supprimer. Les garanties procédurales des professionnels restent applicables.",
    "L'extension d'un cadre disciplinaire commun évite une procédure propre à l'AT-MP et conserve une protection essentielle contre les abus de soins. Aucune réduction normative nouvelle n'est revendiquée.",
    "Les textes réglementaires de discipline ne sont pas réécrits par ce maintien ; aucune appréciation des sanctions d'une affaire individuelle n'est effectuée.",
    "Aucune charge nouvelle identifiée : maintien du seul renvoi source, sans registre, autorisation, déclaration ou justificatif ajouté.")
RESULT['L442-7']['benefit_review'] = (
    "L'avantage possible est l'accès des victimes d'accidents du travail à la même protection contre les fautes, abus et fraudes de soins que les autres assurés, avec les adaptations pour pharmaciens et auxiliaires. Il reste ouvert aux soins futurs comme aux situations antérieures selon leurs règles. Il ne s'agit pas d'une exonération de prélèvement ; aucune garantie de prise en charge ni aucun recours n'est retiré.")

retain('L442-8',
    "Maintien intégral de la prise en charge par la caisse des déplacements imposés à la victime et à ses ayants droit, ainsi que des honoraires et déplacements des médecins concernés. Cette charge sociale rend les contrôles et expertises accessibles. La seule mise à charge possible concerne les examens demandés par l'intéressé dans une contestation judiciairement reconnue manifestement abusive.",
    "Le renvoi à L. 322-5, lu intégralement dans le corpus, porte sur le tarif de transport ; il ne transforme pas une convocation de contrôle en nouvelle obligation de prescription pour toute expertise. Le tarif médical relève d'un décret en Conseil d'État. Les réformes proposées de L. 322-5 gardent leur champ et ne sont pas un gain supplémentaire ici. Aucun transfert vers l'indemnité ordinaire de rupture.",
    "La source finance les frais nécessaires à l'exercice des droits et au contrôle médical. Supprimer cette prise en charge déplacerait le coût sur les victimes ; le maintien ne compte pas comme simplification.",
    "Les montants tarifaires réglementaires ne sont pas fournis par cet article. La réserve judiciaire pour abus manifeste demeure strictement limitée aux actes demandés par la victime ou ses ayants droit.",
    "Aucune charge nouvelle identifiée : bénéficiaires, tarifs de référence et exception judiciaire sont maintenus sans attestation ni avance de frais nouvelle.")

p = paras('L443-1')
p[1] += " Toutefois, les intervalles minimaux prévus au présent alinéa ne sont pas opposables à une demande de la victime tendant à l'augmentation des réparations en raison d'une modification de son état mentionnée au premier alinéa. Cette demande et la nouvelle fixation qui l'accueille peuvent intervenir sans attendre l'expiration de l'intervalle, sans accord préalable de la caisse. Les intervalles demeurent opposables aux révisions à l'initiative de la caisse, sauf accord de la victime pour les diminuer."
p.append("La suppression de l'intervalle minimal pour les demandes d'augmentation s'applique aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente réforme ainsi qu'aux demandes en cours n'ayant pas donné lieu à une décision irrévocable, y compris lorsque l'accident, la guérison ou la consolidation sont antérieurs. Elle n'exige ni nouveau dossier pour une demande en cours fondée sur la même modification médicalement constatée, ni attestation de dispense. Elle ne rouvre pas les prescriptions acquises ni les décisions irrévocables et ne rend pas rétroactivement dues des prestations qui ne l'étaient pas. Les conditions médicales, le contrôle et les droits des ayants droit prévus au présent article demeurent applicables.")
rewrite('L443-1', p,
    "Réduction de fond ciblée : après la période initiale de libre révision, l'intervalle minimal ne bloque plus une demande d'augmentation liée à une modification médicalement constatée. L'accord de la caisse pour avancer cette demande disparaît. Les intervalles protecteurs contre les révisions imposées par la caisse restent opposables. Les cinq alinéas sources, la présomption favorable de décès et leurs renvois sont conservés à leur place ; une transition est ajoutée.",
    "R. 443-1, lu dans le corpus, fixe respectivement deux ans et un an : coordonner son intervalle annuel, sans supprimer la protection contre les révisions imposées. Aucun nombre de jours équivalent à l'année n'est inventé. L. 434-2, troisième alinéa, vise bien la prestation complémentaire de tierce personne ; la durée réglementaire de perception et d'assistance n'est ni supprimée ni remplacée par l'ancienneté professionnelle. L. 431-2 conserve ses prescriptions. La présomption bénéficie aussi aux futurs ayants droit éligibles.",
    'material_reduction',
    "L'article officiel subordonne les révisions postérieures à la période initiale à des intervalles, diminuables d'un commun accord. La proposition retire réellement cette attente et cet accord pour les seules demandes d'augmentation de la victime, tout en conservant les garanties contre une baisse imposée.",
    "Aucun taux de rente ni montant de prestation n'est modifié. Le coût de l'instruction et des droits reconnus plus tôt n'est pas chiffré ; les contrôles médicaux, prescriptions et décisions irrévocables restent réservés.",
    "Aucune charge nouvelle de dossier, donnée ou délai n'est identifiée : la demande et la constatation médicale existaient déjà. Des demandes plus rapprochées peuvent accroître l'activité des caisses, sans solde public net démontré.",
    ["Suppression de l'intervalle minimal et de l'accord nécessaire à sa diminution pour une demande de la victime tendant à augmenter ses réparations sur modification médicalement constatée."])
effect('L443-1', 'deadline_reduced', 'atmp-revision-victime-sans-intervalle',
       "Retrait de l'attente minimale entre révisions demandées pour augmenter la réparation de la victime.",
       "Après les deux premières années suivant guérison ou consolidation, intervalle d'un an fixé par R. 443-1 ; réduction possible seulement d'un commun accord.",
       "Aucun intervalle minimal ni accord préalable pour la demande d'augmentation de la victime fondée sur une modification médicalement constatée ; rythme protecteur conservé pour l'initiative de la caisse.",
       'other', "Victimes d'accidents du travail et, par application du livre IV, de maladies professionnelles.",
       "Demandes présentées après l'entrée en vigueur et demandes encore en cours sans décision irrévocable, accidents anciens inclus ; pas de redépôt ; prescriptions acquises et décisions irrévocables réservées.",
       "Aucun formulaire ou certificat de dispense ; instruction médicale existante, avec activité et dépenses supplémentaires possibles non chiffrées.",
       "Les intervalles peuvent être diminués de commun accord.",
       "Cette demande et la nouvelle fixation qui l'accueille peuvent intervenir sans attendre l'expiration de l'intervalle, sans accord préalable de la caisse.")

retain('L443-2',
    "Maintien intégral de l'obligation de statuer sur la prise en charge de la rechute dès qu'une aggravation nécessite un traitement, avec ou sans nouvelle incapacité temporaire. Il s'agit d'une garantie d'accès aux soins, sans agrément distinct imposé à l'assuré ni seconde déclaration créée par cet article.",
    "R. 443-2, lu dans le corpus, traite les frais et l'articulation de l'indemnité journalière avec la rente maintenue. La suppression d'intervalle de L. 443-1 ne ferme ni ne conditionne ce régime autonome de rechute. Les conditions médicales et les voies de contestation demeurent.",
    "La source oblige la caisse à se prononcer sur une aggravation nécessitant des soins, même sans arrêt de travail. Aucun doublon ni prélèvement accessoire n'est établi dans cette règle.",
    "Les montants de frais, les délais d'instruction et les prescriptions relèvent d'autres dispositions ; ce maintien ne les abolit ni ne les chiffre.",
    "Aucune charge nouvelle identifiée : ni certificat supplémentaire ni condition d'emploi ou d'ancienneté n'est ajouté au droit existant.")

retain('L444-1',
    "Maintien intégral de l'habilitation à adapter le traitement des accidents hors du territoire métropolitain et des collectivités de L. 751-1. Les modalités territoriales et internationales ne peuvent être abolies sans connaître les règles applicables et les garanties de coordination ; l'article ne crée lui-même aucune déclaration ni taxe particulière.",
    "L. 751-1, lu dans le corpus, énumère Guadeloupe, Guyane, Martinique, La Réunion, Saint-Barthélemy et Saint-Martin, y compris les professions agricoles. Le renvoi vise ces collectivités, sans assimilation au contrat privé ni extension automatique d'une réforme française aux obligations internationales. Les règles réglementaires particulières ne sont pas déclarées réécrites.",
    "L'habilitation permet une couverture territoriale adaptée ; sa suppression ne démontre aucune formalité concrètement retirée et pourrait priver les victimes d'un cadre utile.",
    "Aucun inventaire exhaustif des conventions internationales ou décrets territoriaux n'est revendiqué. Les obligations européennes ou conventionnelles ne sont pas effacées implicitement.",
    "Aucune charge nouvelle identifiée : le maintien de l'habilitation ne prescrit ni nouvel enregistrement ni autorisation supplémentaire.")

retain('L451-1',
    "Maintien intégral de l'articulation entre réparation sociale et droit commun, avec toutes les exceptions des articles L. 452-1 à L. 452-5, L. 454-1, L. 455-1, L. 455-1-1 et L. 455-2. Supprimer isolément cette architecture modifierait la responsabilité et le financement des accidents sans suppression justifiée d'une formalité. Les réparations spéciales ne sont pas une indemnité ordinaire de rupture.",
    "La conformité citée par la source est assortie de la réserve du considérant 18 de la décision 2010-8 QPC : ne pas lire l'article comme fermant la réparation des préjudices non couverts en cas de faute inexcusable. La décision intégrale n'est pas jointe ; sa note est conservée comme réserve, sans en revendiquer une nouvelle validation. Les allègements proposés à L. 452-4 et L. 454-1 ne suppriment aucun des cas d'ouverture visés ici.",
    "Aucune suppression isolée et sûre n'est identifiée dans la règle qui coordonne réparation forfaitaire et exceptions de responsabilité. Le maintien protège la cohérence des recours et ne compte comme aucune baisse.",
    "Le montant global de la réparation dépend des articles d'indemnisation et de leur interprétation juridictionnelle. La réserve constitutionnelle indiquée dans la source demeure déterminante.",
    "Aucune charge nouvelle identifiée : maintien des seules limites et exceptions existantes, sans plafonnement par l'ancienneté ou par six mois de salaire.")

retain('L452-1',
    "Maintien intégral du droit à indemnisation complémentaire pour faute inexcusable de l'employeur ou de la personne substituée à la direction. Cette responsabilité protège la santé et la réparation des victimes ; elle n'est ni un prélèvement accessoire ni une formalité administrative remplaçable.",
    "Le renvoi aux articles suivants garde L. 452-2 et L. 452-3, leur paiement par la caisse et leur récupération. La modification ciblée du cinquième alinéa de L. 452-4 ne supprime ni la responsabilité ni la réparation. Aucune condition d'ancienneté, de notification d'une rupture ou de qualification CDI/CDD n'est importée.",
    "Le droit source est la garantie essentielle d'une réparation supplémentaire d'un dommage professionnel imputable à une faute inexcusable de prévention. Aucun allègement de formalité propre à cet article n'est démontré.",
    "La preuve et la qualification de la faute inexcusable restent contrôlables ; ce maintien ne tranche aucune affaire individuelle ni ne chiffre les indemnités.",
    "Aucune charge nouvelle identifiée : les mêmes responsables et bénéficiaires conservent leur régime, sans nouvelle autorisation ou procédure.")

retain('L452-2',
    "Maintien intégral des majorations d'indemnités pour faute inexcusable : plafonds distincts du capital, de la rente et du total des ayants droit, ajustement au départ d'un bénéficiaire, rétablissement du survivant et revalorisation. Le paiement par la caisse et la récupération du capital auprès de l'employeur garantissent la réparation ; supprimer ces charges reviendrait à supprimer des droits.",
    "Conserver les six alinéas et le renvoi du cinquième aux troisième et quatrième. L. 434-9, troisième alinéa, lu dans le corpus, rétablit sous réserves la rente du conjoint, partenaire ou concubin ; L. 434-17 prévoit la revalorisation au 1er avril. La transition source du 1er avril 2013 pour les majorations reste applicable. Ni gel de pensions de retraite ni plafond ordinaire de rupture n'est étendu à ces majorations.",
    "Les plafonds et modalités source articulent une réparation effectivement versée et son financement par le responsable. Aucun accessoire autonome à supprimer sans affaiblir ces droits n'est identifié dans cet article.",
    "Les barèmes réglementaires du capital représentatif ne sont pas modifiés. La réforme de l'assurance et de la cotisation à L. 452-4 ne dispense pas l'employeur de rembourser les majorations.",
    "Aucune charge nouvelle identifiée : maintien intégral des bénéficiaires, plafonds, revalorisations et règles de récupération déjà applicables.")

retain('L452-3',
    "Maintien intégral des réparations des souffrances, préjudices esthétiques et d'agrément, pertes de promotion, du forfait en cas d'incapacité de 100 % et du préjudice moral des ayants droit, ascendants et descendants. Le versement direct par la caisse protège l'effectivité de ces droits, avec récupération contre l'employeur.",
    "La note constitutionnelle 2010-8 QPC réserve le considérant 18 : la liste ne doit pas être présentée comme excluant tous les préjudices non couverts par le livre IV. La décision intégrale n'est pas jointe. Le forfait au salaire minimum légal s'apprécie à la consolidation, non à la rupture d'emploi ; 100 % n'est pas le seuil d'un an ni le plafond de six mois du contrat unique. Les bénéficiaires sans rente restent expressément inclus.",
    "La source organise une réparation personnelle et un paiement garanti aux victimes, distincts de toute taxe ou indemnité de licenciement. Aucun doublon supprimable n'est démontré dans ces trois alinéas.",
    "Les chefs de préjudice et leur articulation avec les autres prestations demeurent soumis aux règles et réserves applicables. Aucun coût national ni montant individuel nouveau n'est avancé.",
    "Aucune charge nouvelle identifiée : maintien des recours, du forfait et du circuit de paiement, sans justificatif ou formalité supplémentaire.")

retain('L452-3-1',
    "Maintien intégral de l'effet d'une décision judiciaire définitive reconnaissant la faute inexcusable : l'employeur reste tenu des sommes prévues à L. 452-1 à L. 452-3 malgré les conditions de son information par la caisse lors de la reconnaissance professionnelle. Supprimer cette règle ferait d'une irrégularité administrative un moyen d'échapper à une réparation judiciairement établie.",
    "La note source vise les actions introduites à compter du 1er janvier 2013 ; aucune rétroactivité différente n'est créée. Le texte exige une décision passée en force de chose jugée et ne supprime pas les droits de défense dans l'action en faute inexcusable. Les renvois conservent les majorations et indemnités, sans préavis ni seuil d'ancienneté.",
    "La charge du responsable est une dette de réparation après jugement, non une cotisation accessoire susceptible d'être retirée sans perte d'indemnisation. Aucun allègement propre à cet article n'est retenu.",
    "Le maintien ne valide pas une procédure de reconnaissance professionnelle irrégulière et ne modifie pas les effets de cette procédure dans les autres contentieux.",
    "Aucune charge nouvelle identifiée : maintien de la seule dette judiciaire existante, sans nouvelle information ou déclaration imposée.")

p = paras('L452-4')
p[4] = "La reconnaissance d'une faute inexcusable à l'origine de l'accident, y compris lorsque l'employeur est assuré contre ses conséquences, ne permet plus d'imposer une cotisation supplémentaire sur le fondement du présent article. Les cotisations supplémentaires prévues à l'article L. 242-7 demeurent applicables lorsqu'elles reposent sur les risques exceptionnels ou les manquements aux mesures de prévention prévus par cet article. Le seul constat d'une faute inexcusable ou de la souscription d'une assurance ne vaut pas constat de ces risques ou manquements."
p.append("La suppression du fondement spécial de cotisation supplémentaire antérieurement prévu au cinquième alinéa s'applique aux périodes courant à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsqu'une décision antérieure la prévoit. Les cotisations correspondant aux périodes antérieures, leurs affectations, recouvrements, restitutions, prescriptions et recours conservent leur régime, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives. La suppression ne réduit ni les indemnités dues à la victime ou à ses ayants droit, ni leur paiement par la caisse, ni la récupération de leur montant auprès du responsable ou de son assureur dans les conditions applicables.")
rewrite('L452-4', p,
    "Réduction de fond : retrait de l'habilitation spéciale à imposer une cotisation supplémentaire pour l'accident dû à la faute inexcusable d'un employeur assuré. Ce fondement ajoute une charge à la réparation et pénalise l'assurance sans constater un risque distinct. Les cotisations de prévention pour risques exceptionnels de L. 242-7 restent possibles sur leur fondement propre, avec constatation de leurs conditions. Tous les autres alinéas sont maintenus : accord ou juge, patrimoine personnel, assurance facultative, prévention, privilège et mise en cause de l'organisme accueillant un stagiaire.",
    "Le cinquième alinéa conserve sa place et distingue expressément le pouvoir autonome de L. 242-7, dont la proposition supprime déjà le minimum forfaitaire : cette autre réduction n'est pas recomptée. Coordonner les arrêtés d'application pour ne pas rétablir une cotisation spéciale de faute inexcusable assurée ; aucun taux n'est inventé. Le privilège de L. 243-4 a été lu dans le corpus. Les a et b du 2° de L. 412-8 concernent des élèves et étudiants, sans contrat de travail nécessaire ; les deux renvois ruraux restent à leur champ agricole et leur texte intégral n'est pas joint. La note du 1er juillet 2026 reste l'histoire d'entrée en vigueur de la version source, non la date de cette suppression.",
    'material_reduction',
    "Le prélèvement accessoire propre aux accidents dus à la faute inexcusable des employeurs assurés disparaît pour les périodes futures, même sur décision ancienne. La réparation, son remboursement et le financement de prévention reposant sur des risques réellement caractérisés sont conservés ; l'article n'est pas abrogé.",
    "Le taux de la cotisation et son produit effectif ne sont pas contenus dans la source. L'économie par employeur et la perte de recettes de prévention restent inconnues ; aucune suppression générale de L. 242-7 ou de cotisations AT-MP n'est revendiquée.",
    "Aucune charge nouvelle identifiée : l'assurance demeure facultative et aucun visa, signalement ou taxe de remplacement n'est créé. Les fondements autonomes de prévention restent soumis à leurs conditions existantes.",
    ["Suppression pour les périodes futures de la cotisation supplémentaire propre à l'employeur assuré contre sa faute inexcusable et de l'affectation future de ce produit supprimé."])
effect('L452-4', 'tax_removed', 'atmp-suppression-cotisation-assurance-faute',
       "Suppression de la cotisation accessoire propre à l'accident dû à une faute inexcusable assurée.",
       "Cotisation supplémentaire facultativement imposée à l'employeur assuré lorsqu'un accident est dû à sa faute inexcusable ; taux et assiette renvoyés à L. 242-7 et aux arrêtés, non chiffrés dans cet article.",
       "Aucun prélèvement sur ce seul fondement pour les périodes futures ; pas de taxe de remplacement. Les cotisations ordinaires et les surcotisations fondées sur les risques exceptionnels de L. 242-7 subsistent.",
       'financing', "Employeurs assurés contre leur faute inexcusable ou celle des personnes substituées à la direction.",
       "Périodes à compter de l'entrée en vigueur, y compris décisions anciennes ; dettes des périodes antérieures et recours préservés, sous réserve répressive plus douce.",
       "Aucun agrément, déclaration ou contribution équivalente ajouté ; indemnisation et prévention autonome conservées.",
       text(paras('L452-4')[4]), text(p[4]))

retain('L452-5',
    "Maintien intégral de la réparation de droit commun du dommage non couvert en cas de faute intentionnelle de l'employeur ou d'un préposé, du service des prestations par la caisse et de son recours. La constitution des rentes dans les deux mois sécurise le paiement. La cotisation pour faute intentionnelle conserve ici une fonction de prévention et de responsabilité distincte de la seule souscription d'assurance.",
    "Le renvoi à L. 242-7 a été lu en source et proposition : la suppression proposée de son minimum forfaitaire ne ferme ni ristournes ni cotisations justifiées ; elle n'est pas recomptée ici. La suppression de L. 452-4 vise le seul déclencheur assurance, pas la faute intentionnelle. La note QPC conserve sa réserve. L'appellation historique « caisse nationale de prévoyance » nécessite une concordance institutionnelle extérieure au lot ; aucun organisme nouveau ni tarif n'est inventé, aucune suppression de la garantie de rente n'en est déduite.",
    "Les obligations de l'auteur d'une faute intentionnelle garantissent l'indemnisation effective et contribuent à prévenir une atteinte volontaire. Aucun prélèvement sans fonction essentielle distincte n'est isolé dans ce régime.",
    "Les tarifs de constitution et la concordance institutionnelle de la caisse nationale de prévoyance ne sont pas intégralement documentés dans le lot. Le maintien ne prétend pas régler ces points extérieurs.",
    "Aucune charge nouvelle identifiée : maintien du délai maximal de deux mois, du recours subrogatoire et des seules responsabilités existantes, sans rapport avec le préavis de quinze jours.")

p = paras('L453-1')
p[1] = "La rente prévue au titre III du présent livre ne peut être diminuée en raison d'une faute inexcusable de la victime qui ne constitue pas une faute intentionnelle. Les exclusions de droits résultant d'une faute intentionnelle demeurent régies par les premier et troisième alinéas du présent article. Les décisions prises pour l'application du présent article restent susceptibles de recours devant la juridiction compétente."
p.append("La suppression de la diminution pour faute inexcusable non intentionnelle s'applique aux arrérages correspondant aux périodes courant à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les rentes attribuées avant cette date. Les caisses rétablissent d'office, pour ces périodes, le montant de la rente sans cette diminution, sans demande ni nouvelle pièce à la charge du bénéficiaire. Les arrérages des périodes antérieures et les recours qui s'y rapportent restent soumis aux règles antérieures ; aucun remboursement rétroactif général n'est créé. La présente disposition ne supprime ni les obligations de sécurité, ni les responsabilités ou sanctions reposant sur un autre fondement.")
rewrite('L453-1', p,
    "Réduction de fond d'une restriction aux droits : suppression de la diminution discrétionnaire de rente pour faute inexcusable non intentionnelle de la victime. La prévention demeure assurée par les obligations de sécurité et responsabilités autonomes ; amputer durablement la réparation n'est pas conservé comme instrument supplémentaire. Les actes intentionnels restent exclus, la prise en charge des soins demeure possible sous L. 375-1, et les droits de l'ayant droit auteur intentionnel restent transférés aux enfants, descendants ou autres ayants droit. Le rétablissement des échéances futures est d'office.",
    "Maintien de trois alinéas initiaux, deuxième remplacé et transition ajoutée. L. 375-1, lu dans le corpus, exclut les prestations en argent pour faute intentionnelle, sans retirer ici l'éventuelle prise en charge des soins. L. 434-10 conserve les catégories d'enfants et descendants, les limites d'âge et relèvements ; la correction d'un renvoi France Travail proposée dans sa vue reste propre à cette cible. Identifier les décisions de réduction existantes pour calculer les seules échéances futures sans minoration ; charge de traitement et surcroît de prestations non chiffrés.",
    'mixed',
    "La source autorise la caisse à diminuer une rente en raison d'une faute inexcusable de la victime. Ce pouvoir disparaît pour les échéances futures. Un rétablissement d'office est ajouté aux caisses afin que les titulaires de rentes anciennes bénéficient aussi de la suppression, sans nouveau dossier privé.",
    "Ni la faute intentionnelle de la victime ni celle d'un ayant droit n'est amnistiée. L'augmentation des prestations et le coût de recalcul peuvent alourdir la dépense sociale ; aucun solde public net ni financement de compensation n'est établi.",
    "Charge nouvelle identifiée pour les caisses : repérer les rentes minorées et rétablir d'office leurs échéances futures. Aucune donnée, déclaration ou condition nouvelle n'est demandée aux bénéficiaires ; ce transfert de traitement justifie le classement mixed.",
    ["Suppression du pouvoir de diminuer la rente d'une victime en raison de sa faute inexcusable non intentionnelle, pour les échéances postérieures à l'entrée en vigueur."])
effect('L453-1', 'relief_extended', 'atmp-fin-minoration-faute-victime',
       "Retrait de la minoration pour faute inexcusable non intentionnelle, y compris sur les rentes déjà attribuées pour leurs échéances futures.",
       "Rente du titre III susceptible d'être diminuée par le conseil d'administration de la caisse ou son comité ; aucun pourcentage de minoration fixé par cet article.",
       "Rente calculée sans cette minoration pour les périodes futures ; exclusions pour acte intentionnel et responsabilités autonomes maintenues.",
       'other', "Victimes dont une faute inexcusable non intentionnelle peut être retenue, nouveaux bénéficiaires et titulaires de rentes anciennes.",
       "Échéances correspondant aux périodes après entrée en vigueur ; pas de restitution générale des périodes antérieures, contentieux historiques conservés.",
       "Rétablissement d'office par les caisses ; coût de gestion et prestations supplémentaires inconnus ; aucune démarche de remplacement pour la victime.",
       text(paras('L453-1')[1]), text(p[1]))
effect('L453-1', 'obligation_added', 'atmp-fin-minoration-faute-victime',
       "Traitement d'office ajouté aux caisses pour rendre la suppression effective sur les rentes anciennes.",
       "La source prévoit la faculté de diminuer la rente et le recours du bénéficiaire, sans rétablissement automatique général des rentes déjà minorées.",
       "La caisse doit rétablir d'office les seules échéances futures sans nouvelle pièce du bénéficiaire.",
       'legal_duty', "Caisses servant des rentes minorées pour faute inexcusable non intentionnelle de la victime.",
       "Application aux périodes postérieures à l'entrée en vigueur, sans remise en cause générale des arrérages antérieurs.",
       "Obligation de traitement administratif et coût supplémentaire possibles, sans nouvelle transmission de données ni registre prescrit.",
       text(paras('L453-1')[1]),
       "Les caisses rétablissent d'office, pour ces périodes, le montant de la rente sans cette diminution, sans demande ni nouvelle pièce à la charge du bénéficiaire.")

p = paras('L454-1')
p[4] += " L'information effectivement reçue par la caisse de l'une de ces personnes satisfait, pour les autres, à cette obligation dans la mesure où elle comporte les informations qui leur sont respectivement imposées. Ces autres personnes ne sont tenues ni de renouveler cet envoi ni d'attester qu'il a été effectué. Les compléments nécessaires non encore portés à la connaissance de la caisse restent dus par les personnes auxquelles ils incombent. Les dispenses d'information existantes demeurent applicables."
p[7] = ("Aucune indemnité forfaitaire de gestion n'est due au titre du présent article à raison des remboursements obtenus à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour un accident antérieur. Aucune indemnité équivalente ne peut naître après cette entrée en vigueur sur le seul fondement du présent article à raison de sommes dont le recouvrement aurait pu être obtenu. Les indemnités légalement nées avant cette entrée en vigueur conservent leur régime, leurs affectations, restitutions, prescriptions et recours, sans remboursement général. Pour ces seules indemnités antérieures, les règles suivantes demeurent applicables : " + p[7])
p.append("La dispense d'envoi redondant prévue au cinquième alinéa s'applique aux informations à fournir à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour des accidents antérieurs. Elle n'impose ni nouveau dépôt ni attestation aux personnes déjà dispensées. Les manquements antérieurs gardent leur régime, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives. La suppression de l'indemnité forfaitaire de gestion ne réduit ni la réparation due à la victime ou à ses ayants droit ni le remboursement des prestations effectivement dues à la caisse ; les frais judiciaires fondés sur des règles autonomes restent distincts.")
rewrite('L454-1', p,
    "Deux réductions de fond : suppression pour l'avenir de l'indemnité forfaitaire de gestion ajoutée au remboursement des prestations et dispense légale des envois redondants entre victime, établissement, tiers et assureur lorsqu'un signalement suffisant a déjà atteint la caisse. Le remboursement du principal, les préjudices personnels réservés, la priorité amiable, le partage de responsabilité, le capital ou la constitution de rente sous deux mois et la cession de créances sont maintenus. Les onze alinéas sources gardent leur place ; le huitième réserve intégralement l'ancienne formule et les neuvième et dixième son recouvrement aux seules créances anciennes.",
    "Aucune suppression de L. 376-1 ou de ses forfaits distincts n'est revendiquée. Les montants source 910 € et 91 €, le tiers du recouvrement et leur indexation depuis 2007 restent exclusivement pour les créances anciennes ; ce ne sont pas les plafonds nominaux actuels, modifiés par arrêtés non joints. D. 454-1, lu en entier, comporte déjà les dispenses victime et tiers ayant informé l'assureur : elles restent, sans nouveau gain compté ; coordonner ses II, III, V et la preuve de l'information pour la dispense nouvelle, et son IV pour empêcher la renaissance du forfait supprimé. R. 454-1 distingue l'évaluation forfaitaire des prestations remboursées du forfait de gestion ici supprimé. L. 454-2 reste coordonné, son renvoi au cinquième alinéa est inchangé. Les renvois ruraux de recouvrement restent réservés aux anciennes indemnités ; code rural et arrêtés hors lot à coordonner. L'appellation historique de la caisse nationale de prévoyance requiert une concordance institutionnelle extérieure sans suppression de la garantie de rente.",
    'material_reduction',
    "La comparaison avec la source entière démontre le retrait du forfait accessoire de gestion pour les faits nouveaux et une dispense supplémentaire d'informations déjà reçues, au-delà des seules dispenses existantes de D. 454-1. Les prestations remboursées et la réparation personnelle restent dues ; il ne s'agit ni d'un report du forfait ni d'une baisse des cotisations AT-MP.",
    "La perte de recettes de gestion et la baisse des coûts privés ne sont pas chiffrées. Les frais de justice autonomes subsistent ; les délais d'information non dispensés et les règles spéciales agricoles ne sont pas effacés. Aucun solde net sur l'ensemble des codes n'est établi.",
    "Aucune charge nouvelle identifiée : pas de registre partagé, attestation ou accès nouveau aux données. Les informations non encore reçues restent dues dans le circuit existant ; la caisse exploite les signalements déjà reçus, avec incidence de gestion non chiffrée.",
    ["Suppression de l'indemnité forfaitaire de gestion accessoire au recours AT-MP contre le tiers pour les remboursements nouveaux et de toute réactivation de ce forfait sur recouvrement empêché.",
     "Suppression des envois et attestations redondants des personnes légalement tenues d'informer la caisse lorsqu'un autre signalement lui a déjà fourni les informations requises."])
effect('L454-1', 'tax_removed', 'atmp-suppression-forfait-gestion-recours',
       "Retrait du prélèvement forfaitaire accessoire au remboursement contre le tiers responsable.",
       "Indemnité à la charge du tiers égale au tiers des remboursements, encadrée par les montants source 91 € et 910 € revalorisés annuellement ; assiette distincte des prestations principales.",
       "Aucune indemnité de gestion au titre de cet article sur les remboursements obtenus après l'entrée en vigueur, même pour accidents anciens ; aucun prélèvement équivalent sur recouvrement empêché né après cette date.",
       'financing', "Tiers responsables et assureurs débiteurs dans le champ du recours AT-MP, y compris le champ agricole visé par la source.",
       "Créances d'indemnité légalement nées avant la réforme conservées avec formule, indexation, affectation, recouvrement et recours ; aucune restitution générale.",
       "Aucune contribution de remplacement ; remboursements principaux et frais judiciaires sur fondement autonome inchangés. Perte de recettes non chiffrée.",
       "Le montant de cette indemnité est égal au tiers des sommes dont le remboursement a été obtenu, dans les limites d'un montant maximum de 910 euros et d'un montant minimum de 91 euros.",
       "Aucune indemnité forfaitaire de gestion n'est due au titre du présent article à raison des remboursements obtenus à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour un accident antérieur.")
effect('L454-1', 'obligation_merged', 'atmp-signalement-tiers-sans-doublon',
       "Un signalement suffisant déjà reçu libère les autres personnes des seuls envois portant les mêmes informations.",
       "Obligations distinctes de victime, établissement, tiers et assureur, avec les dispenses préexistantes notamment de D. 454-1 ; pas quatre déclarations systématiquement dues dans tous les cas.",
       "Pas de nouvel envoi ni d'attestation pour l'information déjà effectivement reçue ; seuls les compléments nécessaires manquants demeurent dus par leur débiteur.",
       'legal_duty', "Victimes, établissements de santé, tiers responsables et assureurs soumis au cinquième alinéa.",
       "Informations à fournir après l'entrée en vigueur, accidents anciens inclus ; sanctions antérieures sous réserve répressive plus douce et dispenses préexistantes conservées.",
       "Aucun nouvel identifiant, registre, confirmation ou accès aux données ; le contenu utile et les délais résiduels demeurent.",
       text(paras('L454-1')[4]),
       "Ces autres personnes ne sont tenues ni de renouveler cet envoi ni d'attester qu'il a été effectué.")

p = paras('L454-2')
p[1] = p[1].replace("la prescription de leur créance", "la prescription de la créance de la caisse")
p[2] += " Aucun défaut d'information ne peut être retenu au titre de ce cinquième alinéa pour un envoi ou une attestation dont la personne est dispensée par ce même alinéa."
p[4] = p[4].replace("au septième alinéa du IV de l'article L. 162-1-14", "au huitième alinéa du I de l'article L. 114-17-2")
p.append("La coordination du recouvrement s'applique aux actes de recouvrement accomplis à compter de l'entrée en vigueur de la loi portant la présente réforme. Elle ne remet en cause ni les actes régulièrement accomplis auparavant ni les prescriptions acquises, et ne rouvre aucun délai de recours expiré. La dispense d'information du cinquième alinéa de l'article L. 454-1 et l'application des dispositions répressives plus douces aux sanctions non définitives sont réservées.")
rewrite('L454-2', p,
    "Coordinations nécessaires : la pénalité ne peut sanctionner les doubles envois ou attestations dont L. 454-1 dispense désormais l'assureur ou le tiers. Le renvoi de recouvrement devenu sans cible à L. 162-1-14 est remplacé par l'alinéa actuel de mise en demeure et contrainte de L. 114-17-2. L'ambiguïté source « leur créance » est expressément rectifiée en « créance de la caisse ». Les plafonds de 50 %, 30 000 €, la pénalité unique par sinistre, le juge et la prescription de deux ans demeurent.",
    "L. 162-1-14 est absent du corpus courant ; L. 114-17-2 a été lu intégralement et son huitième alinéa du I porte la mise en demeure, la contrainte et la majoration de 10 %. R. 454-4, lu intégralement, prévoit déjà cette majoration de 10 % mais vise lui-même une ancienne subdivision de L. 114-17-1 : coordonner ce règlement sans hausse ni nouveau cumul ; conserver ses délais contradictoires d'un mois, de paiement de deux mois puis de mise en demeure d'un mois. R. 454-5, lu en entier, conserve ses plafonds favorables 4 000 €/50 %, 15 000 €/40 %, 20 000 €/30 %, puis 20 %, et ses conditions de récidive. L. 114-17-2 est une cible nouvelle pour cet article, lue dans le corpus public mais absente du paquet reference-targets : elle est signalée ici sans ajout à la liste fermée reference_checks. Les sanctions du défaut d'information du règlement amiable restent distinctes de la dispense du signalement initial.",
    'coordination_only',
    "La dispense de doubles signalements appartient à la mesure L. 454-1 et n'est pas une seconde obligation supprimée ici. La correction du recouvrement rend le renvoi opérant sans modifier les plafonds ni compter comme baisse une pénalité antifraude maintenue.",
    "La source historique intégrale de L. 162-1-14 n'est pas jointe ; la correction s'appuie sur la règle actuelle de L. 114-17-2 et sur le règlement R. 454-4, qui atteste déjà la majoration de 10 %. Aucune identité exhaustive des versions historiques n'est présumée.",
    "Aucune charge nouvelle identifiée dans les données, déclarations ou délais : pénalité, mise en demeure, contrainte et majoration de 10 % sont déjà prévues dans les textes de recouvrement lus. Aucun défaut de doublon supprimé ne peut les déclencher.")
effect('L454-2', 'coordination', 'atmp-signalement-tiers-sans-doublon',
       "Coordination des pénalités avec la dispense de double information de L. 454-1.",
       "Pénalité applicable au manquement à l'obligation du cinquième alinéa de L. 454-1, une seule par sinistre.",
       "Même dispositif, avec impossibilité explicite de sanctionner un envoi ou une attestation désormais dispensé ; aucune deuxième réduction comptée.",
       'legal_duty', "Assureurs et tiers responsables relevant de L. 454-2.",
       "Dispense selon la transition de L. 454-1 et réserve des dispositions répressives plus douces.",
       "Aucune formalité substitutive ; information sur l'accord amiable, plafonds et recours subsistent.",
       text(paras('L454-2')[2]),
       "Aucun défaut d'information ne peut être retenu au titre de ce cinquième alinéa pour un envoi ou une attestation dont la personne est dispensée par ce même alinéa.")
effect('L454-2', 'coordination', 'atmp-renvoi-recouvrement-penalite',
       "Rattachement de la procédure de recouvrement à sa subdivision actuelle.",
       "Renvoi au septième alinéa du IV de L. 162-1-14, absent du corpus courant ; la procédure est déjà précisée par R. 454-4.",
       "Renvoi au huitième alinéa du I de L. 114-17-2 pour mise en demeure et contrainte ; les délais réglementaires et recours restent.",
       'other', "Caisses, assureurs et tiers concernés par le recouvrement d'une pénalité.",
       "Actes futurs ; actes anciens valables, prescriptions acquises et délais de recours expirés préservés.",
       "Aucune majoration nouvelle : celle de 10 % figure déjà dans R. 454-4. Concordance réglementaire encore à rédiger hors lot.",
       "La pénalité est recouvrée selon les modalités définies au septième alinéa du IV de l'article L. 162-1-14.",
       "La pénalité est recouvrée selon les modalités définies au huitième alinéa du I de l'article L. 114-17-2.")

retain('L455-1',
    "Maintien intégral de l'exception ouvrant un recours contre l'auteur d'un accident de trajet, même lorsqu'il s'agit de l'employeur, d'un préposé ou d'un membre de la même entreprise. Le renvoi à L. 454-1 et L. 455-2 préserve réparation, subrogation, droits de procédure et priorité de la victime ; ce n'est pas un régime d'emploi temporaire à supprimer.",
    "L. 411-2, lu dans le corpus, définit les trajets résidence/travail et repas, avec détour de covoiturage régulier et autres conditions. Ces critères restent autonomes. Le renvoi L. 454-1 suivra la suppression du forfait et des doubles envois sans nouvelle coupe comptée dans L. 455-1. La mise en cause de la caisse et la priorité de la victime de L. 455-2 restent applicables.",
    "L'article étend favorablement le recours de droit commun aux accidents de trajet au sein de la même entreprise. Le retirer fermerait un droit utile sans suppression démontrée d'une formalité propre.",
    "La couverture du trajet et la responsabilité se déterminent selon leurs conditions propres. Aucun taux de cotisation ni effet budgétaire global ne découle de ce seul maintien.",
    "Aucune charge nouvelle identifiée : les personnes et recours restent identiques ; aucun préavis, délai d'ancienneté ou contrat spécial n'est créé.")

retain('L455-1-1',
    "Maintien intégral du droit à réparation complémentaire pour l'accident du travail sur voie publique impliquant un véhicule terrestre à moteur conduit par l'employeur, un préposé ou une personne de la même entreprise. La référence à la loi du 5 juillet 1985 protège le régime propre d'indemnisation de la circulation ; la supprimer retirerait un avantage aux victimes.",
    "L. 411-1, lu dans le corpus, définit l'accident par le fait ou à l'occasion du travail sans condition CDI/CDD. Le renvoi à L. 454-1 conserve les adaptations proposées dans son champ ; L. 455-2 garde la priorité de la victime et la mise en cause de la caisse. Le texte intégral de la loi 85-677 n'est pas joint dans ce lot : aucun de ses délais, assureurs ou garanties n'est déclaré modifié.",
    "La règle écarte une limitation de recours pour une catégorie précise d'accidents de circulation ; sa conservation maintient une dérogation favorable pour les victimes futures.",
    "La loi extérieure du 5 juillet 1985 conserve son champ. Aucune suppression de sa procédure ni allègement nouveau des obligations d'assurance n'est démontré ici.",
    "Aucune charge nouvelle identifiée : maintien du dispositif et des mêmes conditions de voie publique, véhicule et conducteur, sans nouvelle déclaration.")

retain('L455-2',
    "Maintien intégral des communications de pièces, de l'accès aux résultats de l'enquête, de la mise en cause de la caisse et de la priorité de la victime sur les caisses. L'appel en jugement commun garantit le contradictoire et évite des décisions incompatibles ; la nullité spéciale protège la partie omise. Aucune seconde assignation lorsque la caisse est déjà régulièrement partie n'est créée par ce texte.",
    "La faute de frappe source « la victimes » est signalée et non utilisée pour fabriquer une réécriture. Les premier et troisième alinéas visent L. 452-1 à L. 452-5, L. 453-1 et L. 454-1 ; le deuxième vise seulement L. 452-1 à L. 452-4 et le quatrième L. 452-5 et L. 454-1. Le délai de nullité reste deux ans après la décision définitive, avec titulaires et intérêt requis. R. 454-2 et R. 454-3 ont été lus : assignation identifiée et information d'audience par le greffe ont des objets distincts. La minoration supprimée à L. 453-1 n'efface pas les fautes intentionnelles toujours visées.",
    "Le texte organise la preuve, la présence de la caisse et la priorité indemnitaire du lésé. L'examen des alinéas et des règlements ne démontre pas un double circuit de même objet à supprimer sans affecter le contradictoire.",
    "La procédure pénale et les règles générales de mise en cause restent extérieures au lot. Le maintien ne compte ni la priorité existante ni la communication des pièces comme un gain nouveau.",
    "Aucune charge nouvelle identifiée : deux ans, personnes habilitées, pièces et droits d'accès sont intégralement maintenus, sans appel supplémentaire ni délai nouveau.")

retain('L455-3',
    "Maintien intégral du droit de la victime, sur demande, à la communication du rapport d'enquête de la caisse régionale. Les secrets de la vie privée et des affaires ne lui sont pas opposables pour les seuls faits qui lui sont personnels. Retirer ce droit ou élargir l'opposabilité du secret compromettrait la preuve et l'accès au juge.",
    "L. 455-2, deuxième alinéa, vise les résultats complets et renseignements en cas de faute inexcusable ; L. 455-3 ouvre plus généralement le rapport éventuel à la victime. Leurs champs ne sont pas identiques, ce qui justifie le maintien des deux garanties. La limite aux faits personnels de la victime n'autorise pas une diffusion publique des données de tiers.",
    "La source est une dispense ciblée d'opposabilité du secret au bénéfice de la victime et une garantie de preuve. Aucun prélèvement ou dossier redondant susceptible d'être retiré n'est identifié.",
    "Le rapport reste celui que la caisse peut établir ; aucun rapport obligatoire supplémentaire ni publication n'est créé. Les faits et droits des tiers restent protégés.",
    "Aucune charge nouvelle identifiée : maintien de la communication à la demande, sans nouvelle collecte, registre ou rapport périodique.")

p = paras('L461-1')
p[7] = p[7].replace("à l'article L. 315-1", "au I de l'article L. 315-2")
rewrite('L461-1', p,
    "Coordination nécessaire du seul renvoi relatif à l'opposabilité de l'avis du comité : le caractère contraignant de l'avis médical pour la caisse est énoncé au I de L. 315-2, tandis que L. 315-1 définit les missions du contrôle médical. Tous les neuf alinéas, les trois dates assimilées, la présomption des tableaux, les voies complémentaires, les conditions d'incapacité et le traitement des pathologies psychiques sont maintenus sans nouvelle condition.",
    "L. 315-1 et L. 315-2 ont été lus intégralement dans reference-targets, sources et propositions distinguées. Le nouveau renvoi au I de L. 315-2 vise la règle d'opposabilité des avis médicaux : cette cible est expressément requise pour cet article et son analyse figure dans reference_checks avec son empreinte exacte. Le cinquième alinéa reste la présomption des tableaux ; les sixième et septième restent les deux voies complémentaires ; l'avant-dernier reste l'avis du comité. La note fixe l'entrée en vigueur de la version source au 30 septembre 2026, sans fixer celle des réformes proposées. Les prescriptions de L. 431-2, l'incapacité de L. 434-2 et le diagnostic scientifique de 2026 demeurent.",
    'coordination_only',
    "L'erreur de cible pour l'effet obligatoire de l'avis est corrigée, sans supprimer la reconnaissance complémentaire ni élargir ses conditions. La proposition n'est ni une nouvelle exonération ni une simplification de dossier revendiquée.",
    "Les pourcentages d'incapacité et pièces réglementaires du comité ne sont pas modifiés. Les tableaux et le diagnostic scientifique continuent de nécessiter leurs textes propres ; aucune économie globale n'est établie.",
    "Aucune charge nouvelle identifiée : le renvoi corrigé n'ajoute ni avis, ni certificat, ni délai ; il rattache l'effet existant à la disposition qui l'énonce.")
effect('L461-1', 'coordination', 'atmp-avis-medical-renvoi-opposabilite',
       "Correction du renvoi qui détermine l'effet de l'avis du comité sur la caisse.",
       "L. 461-1 renvoie à L. 315-1 pour l'effet obligatoire, alors que cette cible décrit les missions du contrôle médical.",
       "Renvoi au I de L. 315-2, qui impose les avis médicaux à l'organisme de prise en charge ; aucune étape ajoutée.",
       'other', "Caisses et demandeurs de reconnaissance d'une maladie par la voie complémentaire du comité régional.",
       "Même régime de reconnaissance et mêmes dates d'ouverture ; pas de réouverture de prescriptions ou de remise en cause de décisions antérieures par cette correction.",
       "Aucune formalité ni charge nouvelle ; l'avis motivé du comité existait déjà.",
       "L'avis du comité s'impose à la caisse dans les mêmes conditions que celles fixées à l'article L. 315-1.",
       "L'avis du comité s'impose à la caisse dans les mêmes conditions que celles fixées au I de l'article L. 315-2.")

retain('L461-2',
    "Maintien intégral des présomptions par tableaux, de leur révision après avis du Conseil d'orientation des conditions de travail, de l'ouverture favorable aux maladies constatées avant un nouveau tableau et de la substitution évitant un double paiement du même dommage. Les listes indicatives pour les intoxications et limitatives pour les autres catégories gardent leur qualification exacte ; ce ne sont pas des listes d'autorisations administratives à abolir.",
    "Le renvoi au cinquième alinéa de L. 461-1 vise bien la présomption des tableaux après ses trois subdivisions de dates ; les voies complémentaires des sixième et septième alinéas subsistent si une condition de tableau manque. L. 412-1, lu dans le corpus, vise les maladies constatées après le 31 décembre 1946 ; cette borne historique et la prise d'effet non antérieure au nouveau tableau demeurent. L. 461-3 réserve la dérogation aux tableaux publiés après le 30 novembre 1955. La note du 1er juillet 2018 reste à son champ de déclarations.",
    "Les délais de prise en charge déterminent une présomption médicale et non une attente administrative imposée à la victime. Les supprimer isolément réécrirait sans base scientifique les tableaux ; les dérogations favorables restent entièrement ouvertes.",
    "Les tableaux réglementaires eux-mêmes ne sont pas assignés et leur examen scientifique n'est pas prétendu achevé. Le maintien ne ferme aucune voie de reconnaissance complémentaire.",
    "Aucune charge nouvelle identifiée : tableaux, avis scientifique, non-cumul et dates sont maintenus sans demande d'agrément ni justificatif supplémentaire.")
RESULT['L461-2']['benefit_review'] = (
    "Sont préservés les trois ensembles de présomptions d'origine professionnelle, le caractère indicatif des travaux pour les intoxications et la possibilité de compléter les tableaux. Le quatrième alinéa permet aux victimes dont la première constatation est antérieure au tableau nouveau d'en bénéficier pour l'avenir, à compter de son entrée en vigueur ; cette dérogation reste ouverte aux futurs tableaux recevables, sous L. 461-3. La substitution aux prestations de même maladie et la prise en compte de la réparation de droit commun empêchent un double paiement sans supprimer le droit AT-MP. Le délai après fin d'exposition limite la présomption seulement ; les voies complémentaires de L. 461-1 restent accessibles.")

retain('L461-3',
    "Maintien intégral de la disposition qui délimite historiquement la dérogation du quatrième alinéa de L. 461-2 et coordonne les avantages alloués pour une même maladie. La date du 30 novembre 1955 n'est pas une date limite fermant les nouveaux tableaux : elle permet au contraire l'application de la dérogation à tous les tableaux publiés après cette date, y compris futurs.",
    "Le quatrième alinéa de L. 461-2 conserve l'ouverture aux premières constatations antérieures au tableau, sans effet des prestations avant son entrée en vigueur. La substitution aux assurances sociales et la prise en compte du droit commun sont distinctes d'une taxe ou d'une indemnité de rupture. La note d'application aux maladies déclarées à compter du 1er juillet 2018 reste conservée ; aucun renvoi ordinal n'est déplacé.",
    "La disposition garantit la portée temporelle d'un avantage de reconnaissance et évite le cumul de réparations de même objet. Aucun doublon de déclaration ni délai minimal d'attente n'est démontré dans cet article.",
    "Le maintien ne rouvre pas toutes les maladies antérieures à 1947 ni les tableaux publiés avant la borne de 1955. Les prescriptions et règles de preuve conservent leur champ.",
    "Aucune charge nouvelle identifiée : les mêmes bornes historiques et règles de substitution restent applicables, sans formulaire ni contrôle supplémentaire.")
RESULT['L461-3']['benefit_review'] = (
    "L'avantage visé est la reconnaissance favorable, selon L. 461-2 quatrième alinéa, d'une maladie médicalement constatée avant l'entrée en vigueur d'un tableau nouveau. La limite aux tableaux publiés après le 30 novembre 1955 laisse cet avantage ouvert aux nouvelles situations éligibles et aux tableaux futurs ; elle n'est pas convertie en simple maintien de droits acquis. La substitution aux avantages d'assurances sociales et l'imputation des réparations de droit commun restent limitées à la même maladie et n'abolissent aucune exonération ou prestation autonome.")


CONTEXTS = {
    'L442-5': "l'application aux accidents du travail des contrôles médicaux des articles L. 315-1 et L. 315-2",
    'L443-1': "la révision de réparations après modification de l'état de la victime et la présomption de décès lié à l'accident",
    'L451-1': "l'articulation entre réparation sociale des accidents et maladies professionnels et exceptions de droit commun",
    'L452-2': "les majorations du capital et des rentes pour faute inexcusable, y compris les droits du survivant",
    'L452-3': "les préjudices personnels, le forfait d'incapacité de 100 % et le préjudice moral des proches",
    'L452-3-1': "la dette de réparation de l'employeur après une décision judiciaire définitive de faute inexcusable",
    'L452-4': "la faute inexcusable, l'assurance, le privilège et la mise en cause de l'organisme accueillant un élève ou étudiant",
    'L452-5': "la réparation et les garanties de rente en cas de faute intentionnelle de l'employeur ou d'un préposé",
    'L453-1': "la faute personnelle de la victime ou d'un ayant droit et les effets sur les prestations et rentes",
    'L454-1': "le recours contre le tiers, les prestations principales, le forfait de gestion et le signalement des lésions",
    'L454-2': "les sanctions de l'omission d'information sur l'accident ou le règlement amiable et leur recouvrement",
    'L455-1': "le recours contre un membre de la même entreprise pour un accident de trajet au sens de L. 411-2",
    'L455-1-1': "la réparation d'un accident de circulation sur voie publique avec un véhicule conduit par un membre de l'entreprise",
    'L455-2': "la communication des pièces, la mise en cause de la caisse et la priorité indemnitaire de la victime",
    'L461-1': "les dates assimilées à l'accident, les présomptions et les reconnaissances complémentaires de maladies professionnelles",
    'L461-2': "les tableaux de maladies professionnelles, leurs extensions favorables et les délais médicaux de présomption",
    'L461-3': "l'application de la dérogation aux tableaux publiés après le 30 novembre 1955 et le non-cumul pour la même maladie",
}


def labor_check(number, target):
    context = CONTEXTS[number]
    if target == 'L1234-1':
        return (
            f"L'article règle {context}, sans renvoi au préavis de licenciement. "
            "La source de L. 1234-1 conserve ses paliers d'ancienneté pour les anciens contrats ; sa proposition prévoit quinze jours calendaires pour le nouveau contrat privé, à compter du lendemain de la présentation ou réception de la notification écrite selon la coordination, avec les procédures collectives et protections distinctes. Aucun de ces délais de rupture ne remplace les délais médicaux, judiciaires ou de paiement de cet article."
        )
    if target == 'L1221-2':
        extra = {
            'L452-4': " Les stages des a et b du 2° de L. 412-8 sont précisément des situations d'élèves ou étudiants, pas nécessairement des contrats de travail ; les régimes agricoles et publics visés ne sont pas convertis artificiellement en contrat privé.",
            'L453-1': " La faute intentionnelle d'un ayant droit et la filiation des enfants bénéficiaires ne dépendent pas de la durée du contrat de la victime.",
            'L461-2': " La durée d'exposition aux agents nocifs est une condition de présomption, pas une durée autorisée d'emploi.",
            'L461-3': " La date d'un tableau médical est indépendante de la date d'embauche et de la fin d'une formation.",
        }.get(number, " Les prestations et recours restent ouverts aux victimes des nouvelles relations éligibles ; aucune fin de mission ou de formation n'est ajoutée comme terme de l'emploi.")
        return (
            f"L'article concerne {context} et ne renvoie pas à L. 1221-2. "
            "La source distingue CDI et recours aux CDD ; la proposition impose l'emploi privé nouveau à durée indéterminée, sans nouveau CDD ou renouvellement après la bascule, avec droits des contrats antérieurs conservés. Cette règle d'embauche n'est pas une condition supplémentaire de réparation AT-MP."
            + extra
        )
    if target == 'L1234-9':
        extra = ""
        if number == 'L452-3':
            extra = " Le forfait au salaire minimum en cas d'incapacité de 100 % reste distinct, sans plafond de six mois ni condition d'un an."
        elif number == 'L453-1':
            extra = " La faute inexcusable ou intentionnelle de la victime au sens de cet article n'est pas l'exception de faute grave du licenciement et ne se déduit pas de celle-ci."
        elif number == 'L452-4':
            extra = " Le privilège garantissant le capital représentatif et l'indemnisation d'un stagiaire ne sont pas plafonnés comme une indemnité ordinaire de rupture."
        return (
            f"L'article porte sur {context}, sans renvoi à l'indemnité de licenciement. "
            "La proposition L. 1234-9 réserve l'indemnité ordinaire à la rupture patronale, zéro avant un an mesuré à la fin effective préavis inclus ; ensuite 0,20 mois sur l'ancienneté totale, mois complets au prorata, plafond légal de six mois et exception de faute grave. Les droits anciens et indemnités spéciales restent distincts. Ces paramètres ne réduisent aucune réparation de dommage professionnel ni aucun droit d'ayant droit du présent article."
            + extra
        )
    raise KeyError((number, target))


SPECIFIC_CHECKS = {
    ('L442-5', 'L315-1'): "Le renvoi direct étend le contrôle médical aux accidents du travail : missions médicales, contrôle des abus, contre-examen, défense et secret restent pertinents. La proposition cible retire seulement le contrôle systématique obligatoire fondé sur le seul niveau statistique de prescription, avec transition pour contrôles futurs ; le renvoi actuel l'appliquera sans nouvelle réécriture ni nouvelle suppression comptée ici. Les quarante-huit heures du rapport de contre-visite ne sont pas un préavis de rupture.",
    ('L442-5', 'L315-2'): "Le renvoi direct couvre l'avis médical opposable, l'accord préalable, l'information avant suspension et les recours. La proposition cible interdit les motifs exclusivement économiques mais conserve les deux motifs médicaux et les accords favorables déjà obtenus, y compris pour des soins futurs sur prescription ancienne. La suppression se situe dans la cible ; aucune déclaration ou autorisation équivalente n'est ajoutée dans L. 442-5.",
    ('L443-1', 'L434-2'): "Le quatrième alinéa de L. 443-1 vise exactement le troisième alinéa de L. 434-2 relatif à la prestation complémentaire pour recours à tierce personne, et non ses seuils de rente des autres alinéas. La durée de perception de cette prestation et l'assistance effective conditionnent la présomption de décès, sans ancienneté d'emploi ni notification de rupture. Le retrait d'intervalle de révision ne supprime pas cette présomption, ouverte aux futurs ayants droit éligibles.",
    ('L451-1', 'L452-3'): "L. 452-3, source seule dans la vue fournie, appartient bien à l'exception L. 452-1 à L. 452-5 : réparation des préjudices personnels, forfait à 100 % et préjudice moral des proches, avec paiement par la caisse. Le renvoi reste cohérent et la réserve constitutionnelle signalée dans les notes doit être respectée. Ces dommages ne deviennent pas une indemnité ordinaire de rupture conditionnée par l'ancienneté.",
    ('L451-1', 'L455-2'): "L. 455-2 est expressément réservé par L. 451-1 : communication des pièces pénales et d'enquête, présence de la caisse, nullité spéciale et priorité de la victime. Ce renvoi maintient un cadre de recours nécessaire ; le délai de deux ans pour la nullité n'est ni le délai d'un préavis ni celui de l'ancienneté. La source cible seule reste inchangée dans le présent lot.",
    ('L451-1', 'L452-5'): "L. 452-5 maintient l'exception de faute intentionnelle avec recours de droit commun pour le dommage non couvert et recours de la caisse. La réserve de L. 451-1 demeure donc utile et le délai de deux mois pour constituer une rente reste distinct de toute notification de rupture. La suppression ciblée de la cotisation spéciale de faute inexcusable assurée de L. 452-4 ne supprime pas ce régime intentionnel.",
    ('L451-1', 'L452-2'): "L. 452-2 reste dans la plage L. 452-1 à L. 452-5 : majoration de capital ou rente, plafond sur salaire annuel, maintien global aux ayants droit et revalorisation. La plage conserve ces droits en entier ; le capital représentatif recouvré n'est pas la cotisation d'assurance supprimée à L. 452-4. Aucun calcul à 0,20 mois ni seuil d'un an ne lui est applicable.",
    ('L451-1', 'L454-1'): "L'exception visant L. 454-1 conserve les recours contre un tiers et la réparation non couverte ; la vue fournie est sa source officielle, pas une proposition. Dans ce lot, le forfait de gestion et les doublons d'information sont retirés sans fermer cette exception, ni les préjudices personnels ni le remboursement principal. Le renvoi n'est donc pas orphelin et ne compte pas comme une deuxième suppression du forfait.",
    ('L451-1', 'L452-4'): "L. 452-4 demeure dans la plage utile pour accord amiable ou juge, responsabilité, assurance et privilège, ainsi que mise en cause de l'accueil d'un stagiaire. Le cinquième alinéa seulement est réduit dans ce lot pour la cotisation spéciale de faute inexcusable assurée ; aucune exception de réparation n'est supprimée. Ni le statut d'élève ni une durée de stage ne deviennent un nouveau CDD.",
    ('L452-3-1', 'L452-3'): "La plage L. 452-1 à L. 452-3 couvre exactement la majoration de rente et les réparations personnelles récupérables après reconnaissance judiciaire définitive. L. 452-3 reste intégralement maintenu, y compris 100 %, salaire minimum à consolidation et droits des proches sans rente. L'information de l'employeur lors de la reconnaissance professionnelle ne devient pas une notification de rupture ni un seuil d'ancienneté.",
    ('L452-3-1', 'L452-2'): "La décision définitive de faute inexcusable rend exigible envers l'employeur le remboursement des majorations de L. 452-2, malgré les conditions d'information initiale par la caisse. La source cible garde ses plafonds, rétablissements et revalorisations. La transition du 1er janvier 2013 de L. 452-3-1 et celle du 1er avril 2013 de L. 452-2 restent distinctes ; aucune première année d'emploi n'est retirée du calcul.",
    ('L452-4', 'L452-3'): "Le premier alinéa vise bien les indemnités personnelles de L. 452-3 dans la recherche d'accord et, à défaut, la saisine du juge. Le retrait du prélèvement spécial de faute inexcusable assurée n'affecte ni ces indemnités ni leur avance par la caisse ni leur récupération ; la vue source seule ne contient aucun plafond ordinaire de rupture à leur appliquer. L'accès des ayants droit et proches reste ouvert.",
    ('L452-4', 'L242-7'): "La source de L. 242-7 autorise ristournes et cotisations pour risques exceptionnels ou manquements de prévention ; sa proposition retire seulement le minimum forfaitaire et corrige le recours, avec périodes anciennes réservées. L. 452-4 retire ici son fondement spécial de cotisation pour faute inexcusable d'un employeur assuré, sans le rétablir par le renvoi à L. 242-7 : un risque ou manquement autonome doit être caractérisé. Les ristournes et avances futures demeurent ouvertes ; la réduction déjà portée par la cible n'est pas recomptée.",
    ('L452-4', 'L452-2'): "Le sixième alinéa garantit le capital représentatif de la majoration versée par la caisse au titre de L. 452-2 ; ce capital reste entièrement récupérable et privilégié. Il ne correspond pas à la cotisation supplémentaire retirée du cinquième alinéa. Le renvoi et son alinéa sont conservés à leur place, sans condition d'ancienneté ni plafond de six mois de salaire.",
    ('L452-4', 'L412-8'): "Le dernier alinéa vise exclusivement les a ou b du 2° de L. 412-8, élèves et étudiants couverts pendant enseignements, ateliers, laboratoires ou stages. La proposition cible modernise d'autres renvois mais conserve ces catégories et distingue expressément les stages sans emploi du contrat privé unique. L'appel de l'organisme d'accueil dans la même instance protège le stagiaire ; la durée pédagogique ne fixe pas le terme d'un emploi et les renvois ruraux distincts ne sont pas réattribués au contrat privé.",
    ('L452-5', 'L242-7'): "Le dernier alinéa conserve la cotisation pour faute intentionnelle, dont la fonction de prévention et de responsabilité est distincte de la cotisation spéciale pour faute inexcusable assurée de L. 452-4. Le renvoi à L. 242-7 garde ses conditions et ses ristournes ; la proposition de cette cible supprime le minimum forfaitaire sans imposer un taux nouveau. Les créances anciennes, recours et périodes demeurent traités selon leurs transitions propres.",
    ('L453-1', 'L434-10'): "Le troisième alinéa transfère les droits de l'ayant droit auteur intentionnel aux enfants et descendants définis à L. 434-10, puis aux autres ayants droit à défaut. Les filiations, enfants recueillis, limites d'âge et relèvements restent pertinents. La proposition de la cible remplace un renvoi à l'ancienne institution de l'emploi, sans fermer l'avantage aux futures situations. Le retrait de la minoration pour faute non intentionnelle de la victime n'efface pas cette déchéance intentionnelle.",
    ('L454-1', 'L431-1'): "Le septième alinéa vise précisément le 4° de L. 431-1 : capital ou rente d'incapacité permanente et rentes aux ayants droit. La réparation complémentaire et l'option de capital ou constitution d'une rente dans les deux mois conservent leur fondement. Ce délai sécurise le paiement et n'est pas le préavis individuel de rupture ; le forfait de gestion supprimé n'est aucune de ces prestations.",
    ('L454-2', 'L454-1'): "Le troisième alinéa vise toujours le cinquième alinéa de L. 454-1, conservé à cette place. La source cible seule impose le signalement ; le présent lot y ajoute la dispense lorsque l'information requise est déjà reçue. L. 454-2 exclut explicitement la sanction du doublon dispensé mais conserve celle des informations réellement manquantes et du règlement amiable non signalé, sans majorer plafonds ou délais.",
    ('L455-1', 'L455-2'): "Pour l'accident de trajet causé dans la même entreprise, le renvoi étend bien les garanties de communication, mise en cause et priorité de L. 455-2. Les renvois internes distincts de ses quatre alinéas restent maintenus, ainsi que la nullité sous deux ans avec intérêt à agir. Aucun raccourcissement au préavis du contrat unique n'est possible : il s'agit d'un contentieux d'accident, pas de rupture.",
    ('L455-1', 'L454-1'): "Le renvoi applique le régime du tiers au responsable de l'accident de trajet même membre de l'entreprise. La proposition de ce lot retire le forfait de gestion futur et le signalement répété, sans supprimer réparation, remboursement principal, partage de responsabilité ou garanties de rente. Ces effets suivent le renvoi ; ils ne sont pas une seconde réduction attribuée à L. 455-1.",
    ('L455-1-1', 'L455-2'): "Le renvoi conserve les garanties de procédure et la priorité de la victime pour l'accident de circulation relevant de cet article. Il ne remplace pas la loi du 5 juillet 1985 par une procédure de rupture. Les pièces, la présence de la caisse et le délai de deux ans pour demander la nullité spéciale gardent leurs conditions ; aucune ancienneté d'emploi n'en ferme le bénéfice.",
    ('L455-1-1', 'L454-1'): "L. 454-1 fournit le recours et la coordination des prestations pour cet accident de circulation au sein de la même entreprise. La source fournie de la cible et sa proposition nouvelle dans le lot sont distinguées : les retraits du forfait et des doublons suivent le renvoi, tandis que la réparation complémentaire et la loi spéciale de circulation restent entières. Aucun prélèvement supprimé n'est recréé par ce renvoi.",
    ('L455-2', 'L452-3'): "L. 452-3 est inclus dans les plages des premier, deuxième et troisième alinéas de L. 455-2 : pièces et enquête utiles à la faute inexcusable, présence de la caisse et nullité spéciale. Il n'est pas dans le seul renvoi du quatrième alinéa à L. 452-5 et L. 454-1. Les chefs personnels et le forfait à 100 % restent intacts, sans indemnité ordinaire liée à l'ancienneté.",
    ('L455-2', 'L452-5'): "La faute intentionnelle de L. 452-5 est visée par les premier et troisième alinéas pour les pièces pénales et la mise en cause, puis par le quatrième pour la priorité de la victime. Elle n'entre pas dans la plage plus courte L. 452-1 à L. 452-4 du deuxième alinéa. Le délai de constitution de rente de deux mois de la cible ne se confond ni avec la nullité sous deux ans ni avec quinze jours de préavis.",
    ('L455-2', 'L452-2'): "Les majorations de L. 452-2 appartiennent aux trois premières plages de L. 455-2. Communication et présence de la caisse garantissent le débat sur les sommes et leur remboursement, sans nouvelle action distincte ni limitation par le barème de rupture. Les six alinéas de la cible, dont le rétablissement du survivant et la revalorisation, restent intégralement maintenus.",
    ('L455-2', 'L453-1'): "Les premier et troisième alinéas de L. 455-2 visent expressément L. 453-1, pas le deuxième ni le quatrième. La suppression proposée de la minoration pour faute non intentionnelle ne fait pas disparaître la faute intentionnelle de la victime ou d'un ayant droit, donc le renvoi demeure utile pour ces litiges, leurs pièces et le contradictoire. Aucun droit de communication ni priorité n'est retiré à l'occasion de cette réduction.",
    ('L455-2', 'L454-1'): "L. 454-1 reste visé aux premier et troisième alinéas pour les pièces et la présence de la caisse, et au quatrième pour la priorité de la victime sur le remboursement social. Le retrait du forfait de gestion dans la proposition de ce lot ne supprime pas le principal du recours : le renvoi demeure opérant et protecteur. Les doublons de signalement administratif retirés ne sont pas assimilés à la mise en cause juridictionnelle.",
    ('L455-2', 'L452-4'): "L. 452-4 est inclus dans les trois premières plages de L. 455-2. Son premier alinéa et L. 455-2 articulent la présence nécessaire de la caisse, sans imposer de second appel d'une caisse déjà partie. Dans le présent lot, seul le prélèvement spécial de faute inexcusable assurée disparaît de L. 452-4 ; la responsabilité, le juge, le privilège et l'appel de l'organisme d'accueil demeurent, donc les garanties de procédure gardent leur objet.",
    ('L461-1', 'L431-2'): "Le 3° de L. 461-1 fixe spécialement le point de départ pour la prescription de L. 431-2 à l'information médicale du lien professionnel possible, tandis que les 1° et 2° concernent la date assimilée à l'accident pour les autres effets. La prescription source est de deux ans avec ses interruptions et cas propres. Aucune ancienneté de licenciement ni notification de rupture ne remplace le certificat médical, et la correction du renvoi d'avis du comité ne modifie pas ces règles.",
    ('L461-1', 'L434-2'): "Le septième alinéa de L. 461-1 renvoie à L. 434-2 pour évaluer l'incapacité permanente d'une maladie hors tableau, non pour exiger un âge ou une ancienneté d'emploi. Les critères médicaux, aptitudes et qualifications de la cible restent utiles ; le pourcentage minimal relève de la règle réglementaire propre. Le présent lot ne ferme ni cette voie ni la reconnaissance de pathologies psychiques et ne remplace pas la rente par l'indemnité ordinaire du contrat unique.",
    ('L461-1', 'L315-1'): "La dernière phrase de l'avant-dernier alinéa vise actuellement L. 315-1 pour l'avis du comité qui s'impose à la caisse. La source et la proposition de cette cible définissent les missions du contrôle et ne portent pas la règle d'opposabilité ; celle-ci est au I de L. 315-2, également fourni et lu dans le paquet. La proposition L. 461-1 corrige explicitement ce renvoi sans deuxième avis, nouvelle condition ou délai. Le retrait du contrôle systématique statistique dans L. 315-1 ne supprime pas l'avis du comité.",
    ('L461-1', 'L315-2'): "Le I de L. 315-2, identique sur ce point dans la source officielle et la proposition fournie, dispose que les avis médicaux s'imposent à l'organisme de prise en charge. Il constitue donc la cible exacte de la dernière phrase de l'avant-dernier alinéa de L. 461-1 pour l'avis motivé du comité régional, en remplacement du renvoi aux missions de L. 315-1. Ce rattachement ne transforme pas l'avis du comité en accord préalable de soins du II : les motifs économiques retirés dans la proposition cible n'affectent ni les deux voies complémentaires de reconnaissance ni les pathologies psychiques. Il ne crée aucun avis supplémentaire, délai d'attente, condition d'ancienneté ou notification de rupture ; les demandes anciennes et futures restent régies par les conditions médicales et temporelles propres à la maladie professionnelle.",
    ('L461-3', 'L461-2'): "Le renvoi au quatrième alinéa est exact : cet alinéa de L. 461-2 étend un tableau nouveau aux premières constatations antérieures, avec effet des prestations au plus tôt à son entrée en vigueur et règles de substitution. L. 461-3 conserve cette dérogation pour tous les tableaux publiés après le 30 novembre 1955, donc aussi les futurs tableaux éligibles ; la note du 1er juillet 2018 demeure. Ce n'est pas une ancienneté d'emploi ni un délai de notification.",
}


for number, result in RESULT.items():
    source = BY_NUMBER[number]
    source_key = source['code_id'] + '|' + source['source_id']
    checks = []
    for key in REFERENCES['requirements'][source_key]:
        target = REFERENCES['targets'][key]
        target_number = target['number']
        if target['code_id'] == 'LEGITEXT000006072050':
            assessment = labor_check(number, target_number)
        else:
            assessment = SPECIFIC_CHECKS[(number, target_number)]
        checks.append({'target_key': key, 'view_sha256': target['view_sha256'],
                       'assessment': assessment})
    result['reference_checks'] = checks

RESULT['L454-1']['review_notes'] += " Le 3° de L. 221-3-1, lu intégralement dans le corpus, permet bien au directeur général de confier des missions à certains organismes du réseau : la cession du onzième alinéa garde ce fondement."
RESULT['L461-1']['review_notes'] += " L. 461-5, lu intégralement dans le corpus, contient la déclaration visée au 2°, des exemplaires de certificat et une transmission à l'inspection : ces formalités ne sont pas supprimées par le présent renvoi ; leur éventuelle réduction doit porter sur L. 461-5, hors des 24 sources assignées."

for number in ('L443-1', 'L452-2', 'L452-3', 'L461-1'):
    RESULT[number]['review_notes'] += (
        " La source assignée porte l'état ABROGE_DIFF et une fin de validité au 1er novembre 2026. "
        "Cet état documentaire n'est ni une abrogation décidée dans ce lot ni la date d'entrée en vigueur de la réforme proposée. "
        "L'examen porte sur l'intégralité de cette version ; la rédaction officielle qui lui succédera n'est pas fournie parmi les sources assignées. "
        "La coordination avec cette version ultérieure, notamment des subdivisions et règles transitoires, reste identifiée sans en inventer le contenu."
    )
    RESULT[number]['substantive_impact']['scope_limitations'] += (
        " La version assignée est annoncée jusqu'au 1er novembre 2026 ; les effets sur une rédaction officielle ultérieure non fournie ne sont pas démontrés."
    )

RESULT['L452-4']['review_notes'] += (
    " La proposition distincte de L. 243-4 limite son privilège général aux cotisations ; "
    "le sixième alinéa de L. 452-4 maintient néanmoins son fondement spécial pour le capital de réparation de L. 452-2, "
    "en ne renvoyant à L. 243-4 que pour les conditions et le rang. Cette coordination ne doit pas faire disparaître cette garantie spéciale."
)

RESULT['L454-1']['review_notes'] += (
    " La dispense nouvelle porte sur l'obligation légale d'envoi spontané de chaque débiteur lorsque le signalement complet d'un autre est déjà reçu, "
    "au-delà de la seule interdiction de redemander une information prévue par le CRPA. "
    "Elle n'est pas comptée comme une nouvelle règle générale de réemploi et ne modifie pas l'information distincte sur le règlement amiable de L. 454-2."
)

ordered = [RESULT[s['number']] for s in SOURCES]
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(ordered)} articles ; {sum(x["status"] == "rewrite_draft" for x in ordered)} nouveaux corps ; {sum(x["status"] == "retained_unchanged" for x in ordered)} maintiens ; {sum(len(x["reference_checks"]) for x in ordered)} vérifications de cibles.')
