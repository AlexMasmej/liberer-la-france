import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answer = []


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


def paras(number):
    return re.findall(r'<p>.*?</p>', by_number[number]['source_xml'], re.S)


def impact(classification, assessment, scope, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=scope, new_burdens_review=burdens, effects=effects or [])


def add(number, reason, notes, assessment, scope, xml=None, classification='retained_necessary',
        burdens=None, removed=None, repeal=None, benefit=None):
    src = by_number[number]
    obj = {k: src[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    obj.update(proposed_xml=xml, reason=reason, review_notes=notes,
               status='retained_unchanged' if xml is None else 'rewrite_draft')
    if xml is None:
        obj['classification'] = 'retained_necessary'
    if removed:
        obj.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if repeal:
        obj.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    if benefit:
        obj['benefit_review'] = benefit
    obj['substantive_impact'] = impact(classification, assessment, scope,
        burdens or "Aucune charge nouvelle n'est identifiée : le texte source est maintenu intégralement, sans nouvelle donnée, demande, durée minimale ou condition d'accès.")
    obj['reference_checks'] = []
    answer.append(obj)
    return obj


def effect(obj, kind, measure, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    assert source_quote in plain(by_number[obj['number']]['source_xml']), (obj['number'], source_quote)
    assert proposed_quote in plain(obj['proposed_xml']), (obj['number'], proposed_quote)
    assert min(len(source_quote), len(proposed_quote)) >= 12
    obj['substantive_impact']['effects'].append(dict(kind=kind, measure_id=measure, description=description,
        before=before, after=after, unit=unit, affected_population=population,
        conditions_and_transition=transition, replacement_or_new_burdens=burdens,
        source_quote=source_quote, proposed_quote=proposed_quote))


add('L371-3',
    "Maintien intégral nécessaire : le cumul de couvertures AT-MP et maladie ou maternité protège les risques distincts, tandis que l'interdiction de cumuler deux indemnités journalières empêche un double remplacement du revenu. La dispense de nouvelle carence est conservée. Aucune formalité autonome ni cotisation accessoire n'est créée par cet article et aucune coupe supplémentaire n'est retenue.",
    "L313-1 est un renvoi aux conditions sociales d'ouverture du droit lors de l'accident, non à une ancienneté de licenciement. Sa proposition supprime seulement l'affiliation minimale du II ; le renvoi conserve cette amélioration sans réintroduire un délai. L323-4 règle le calcul de l'IJ et L331-3 le repos maternité (6/10 semaines, exceptions de naissances multiples et prématurité conservées). Ne pas appliquer le gel des pensions aux IJ. Aucun prélèvement successoral n'est en cause.",
    "La source entière maintient des droits à prestations pour une maladie indépendante ou une grossesse et une dispense de carence, avec non-cumul des IJ ; aucun allègement nouveau n'est revendiqué.",
    "Ce maintien ne supprime pas les conditions de rémunération ou d'heures du régime ni les règles AT-MP. Il ne chiffre ni cotisations ni droits futurs de retraite.")

add('L371-4',
    "Maintien intégral nécessaire de l'accès à l'invalidité pour une aggravation non indemnisable au titre AT-MP. La liquidation indépendante, le minimum global et le plafond au salaire du travailleur valide organisent la coordination de deux prestations ; leur suppression supprimerait une garantie ou modifierait sans décision le revenu de remplacement. Aucun dossier distinct, agrément ou prélèvement n'est imposé ici.",
    "L341-5, lu dans le corpus public, fixe un minimum qui ne peut être inférieur à l'allocation aux vieux travailleurs salariés ; la note de 2004 conserve les titulaires historiques. Le minimum vise ici le total rente-pension et non chaque prestation séparément. Le plafond est un salaire de comparaison, non le PASS et non le plafond de six mois de rupture. Le taux d'incapacité reste à son texte réglementaire ; aucun taux n'est inventé.",
    "La règle assure une couverture d'invalidité complémentaire d'une rente AT-MP et évite de confondre les minima et plafonds de deux prestations. Aucune réduction réelle de charge n'est ajoutée.",
    "Les conditions médicales et le taux réglementaire d'incapacité ne sont pas révisés. La capitalisation des salariés privés n'est pas étendue à ces prestations d'invalidité.")

add('L371-5',
    "Maintien intégral nécessaire du versement provisionnel de l'assurance maladie lorsque la caisse conteste l'origine professionnelle et de l'acquisition définitive des prestations même en cas d'échec judiciaire. La condition sociale de L313-1 détermine le droit ; la source n'impose pas une pièce spécifique répétée dont la suppression serait démontrée.",
    "La proposition de L313-1 supprime la seule ancienneté d'affiliation du II pour les périodes nouvelles ; le présent renvoi ne la rétablit pas. Les conditions de rémunération ou de travail et les assimilations favorables restent distinctes. L'échec dans l'action judiciaire ne devient ni un indu ni un motif de remboursement par l'assuré.",
    "Le maintien protège la continuité des prestations pendant le litige AT-MP et leur conservation après celui-ci, sans suppression démontrée d'une nouvelle obligation administrative.",
    "Il n'est pas décidé d'étendre toutes les prestations en espèces sans conditions contributives ; la prise en charge des soins et le contentieux AT-MP gardent leur champ.")

p = paras('L371-6')
p[2] = "<p>Dans le cas mentionné au premier alinéa, les indemnités journalières prévues à l'article L. 323-4 leur sont servies pendant des périodes déterminées, sans qu'une interruption d'une durée minimale soit exigée entre ces périodes, sous réserve qu'ils remplissent les conditions d'attribution lors de chaque interruption de travail.</p>"
p.append("<p>La suppression de l'interruption minimale entre périodes s'applique aux indemnités dues pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque l'interruption de travail a commencé auparavant. Elle ne réduit ni une durée d'indemnisation ni une dispense de participation et ne permet pas un double paiement pour une même période. Les droits, créances, régularisations, prescriptions et recours afférents aux périodes antérieures restent régis par les dispositions alors applicables.</p>")
o = add('L371-6',
    "Réduction de fond : suppression de l'interruption minimale imposée entre deux périodes d'IJ des assurés malades ou blessés de guerre. La durée des périodes indemnisables et les conditions de chaque arrêt demeurent ; les quatre autres alinéas sont intégralement conservés, dont la gratuité relative aux autres maladies, la preuve de l'origine contestée et l'exclusion spéciale des pensionnés interdits de tout travail.",
    "Coordonner les règlements déterminant les périodes et interruptions de cette section : aucun espacement minimal supprimé ne peut être réintroduit par leur application. Aucun nombre de jours n'est déduit d'un texte réglementaire non fourni. Le renvoi grammatical au pluriel « desdits articles » après le seul L212-1 est une anomalie préexistante conservée, sans inventer de second article militaire. La preuve de non-rattachement aux pensions militaires est maintenue pour départager les financeurs, non assimilée à une ancienneté d'emploi. Le coût des IJ supplémentaires reste à évaluer.",
    "L'attente obligatoire entre périodes d'indemnisation est effectivement retirée. Les soins militaires, la couverture des autres affections et la dispense de participation restent ouverts aux futures situations éligibles.",
    "La durée maximale d'indemnisation et les conditions médicales et contributives de chaque arrêt ne sont pas supprimées. Le gain de jours et le coût budgétaire ne sont pas chiffrés faute des paramètres réglementaires complets.",
    ''.join(p), 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : aucun dépôt ni justificatif de remplacement n'est ajouté. La caisse verse les IJ selon le circuit existant ; l'élargissement des périodes payables peut accroître la dépense sociale, sans solde public chiffré.",
    removed=["Exigence d'une interruption d'une durée minimale entre deux périodes d'indemnités journalières des assurés malades ou blessés de guerre."],
    benefit="Les soins personnels relevant des pensions militaires restent garantis par le premier alinéa. Pour les autres affections, la prise en charge L160-1, les IJ L321-1 et du chapitre 3, ainsi que la dispense du pourcentage de participation médicale, pharmaceutique et autre restent intégrales pour les cas futurs recevables. L'IJ L323-4 n'est plus subordonnée à un espacement minimal entre périodes, sans réduction de durée indemnisable. L'exclusion des titulaires de l'indemnité de soins interdits de travail n'est pas une exonération de prélèvement : elle répartit des prestations incompatibles et demeure. La preuve d'origine contestée est conservée dans son champ propre.")
effect(o, 'obligation_removed', 'pensions-guerre-fin-interruption-minimale-ij',
    "Retrait de l'espacement minimal entre périodes d'IJ de maladie des pensionnés de guerre.",
    "IJ versées par périodes séparées par une interruption minimale, dont le nombre de jours n'est pas fixé dans cet article.",
    "Aucune interruption minimale entre périodes ; conditions d'attribution et durée des périodes maintenues.", 'legal_duty',
    "Assurés malades ou blessés de guerre relevant du premier alinéa.",
    "IJ des périodes courant dès l'entrée en vigueur, même pour un arrêt déjà commencé ; droits antérieurs préservés.",
    "Pas de déclaration ou justificatif de remplacement ; dépenses d'IJ potentiellement accrues, non chiffrées.",
    "séparées par une interruption d'une durée minimale",
    "sans qu'une interruption d'une durée minimale soit exigée entre ces périodes")

add('L371-7',
    "Maintien intégral de l'assurance invalidité pour une aggravation non réparable par la pension militaire, avec liquidation indépendante, minimum global et plafond du salaire valide. Il s'agit d'une garantie contributive complémentaire, non d'une taxe ou d'une autorisation. Les supprimer au titre de l'allègement retirerait des droits sans décision correspondante.",
    "Le minimum de L341-5 est celui du total pension militaire-pension d'invalidité. Le taux d'incapacité et les règles de liquidation du chapitre Ier du titre IV ne sont pas remplacés par le barème de rupture d'emploi. Le maintien des deux prestations ne promet pas deux minima indépendants. Les notes historiques de L341-5 ont été examinées dans le corpus public.",
    "Le texte maintient un droit complémentaire et coordonne deux revenus de remplacement. Aucun nouveau taux, délai ou prélèvement supprimé n'est revendiqué.",
    "Les pensions militaires et d'invalidité restent dans leurs régimes propres ; le gel partiel proposé des pensions de retraite n'est pas appliqué ici.")

add('L372-1',
    "Maintien intégral nécessaire : suspension des versements pendant le service ou l'appel sous les drapeaux, pension d'invalidité pour la maladie extérieure au service non indemnisée militairement, retour aux prestations maladie et protection familiale pendant le service. Supprimer ce texte ferait perdre une dispense et une continuité de couverture ; il n'institue aucune déclaration ou taxe accessoire autonome.",
    "D712-6, lu intégralement dans le corpus public, étend L372-1 et L372-2 aux fonctionnaires sous les drapeaux ; ses notes visent notamment magistrats, stagiaires et fonctionnaires civils outre-mer. Ce champ public ne relève pas du contrat privé unique ni de son préavis. L'expression historique « retour dans ses foyers » ne crée pas un nouveau délai minimal. Les prestations décès visées ne sont pas des droits fiscaux de succession.",
    "La dispense de versement et les garanties de l'assuré et de sa famille sont conservées dans leur totalité ; aucune baisse supplémentaire n'est inventée.",
    "La suspension légale du service national ne justifie pas d'effacer les situations encore couvertes d'appel sous les drapeaux. Aucun raccordement des régimes publics à la capitalisation privée n'est décidé.")

add('L372-2',
    "Maintien intégral de la neutralisation du temps sous les drapeaux dans les périodes servant à ouvrir les prestations au retour. Les renvois L313-1 et L341-2 portent sur les conditions sociales de prestations, non sur le seuil d'un an de rupture. La source n'exige pas une attestation autonome à retirer ; supprimer la neutralisation ferait perdre un avantage.",
    "L341-2 officiel, lu intégralement dans le corpus, exige affiliation minimale et cotisations ou heures pour l'invalidité ; la proposition fournie de L313-1 ne maintient plus de durée d'affiliation distincte au II pour les IJ et la maternité. Le renvoi permet cette amélioration sans recréer le délai supprimé. D712-6 conserve l'extension aux fonctionnaires sous les drapeaux ; ni contrat unique ni barème de licenciement ne s'y substituent.",
    "La neutralisation favorable du service militaire demeure pour les futurs retours éligibles ; les conditions contributives distinctes restent celles des articles visés.",
    "Cette conservation ne supprime pas les conditions propres à l'invalidité et ne chiffre aucun effet de financement ou de complexité à l'échelle du code.")

xml = "<p>Le présent article est abrogé pour les risques réalisés à compter de l'entrée en vigueur de la loi portant la présente abrogation. Aucun remboursement des prestations de maladie, de maternité, de décès, d'invalidité ou d'accident du travail ne peut être réclamé à l'employeur sur son seul fondement pour ces risques, en raison de l'absence du contrôle médical ou de la présentation de son justificatif.</p><p>Les créances légalement nées à raison de risques réalisés avant cette entrée en vigueur, leur liquidation et leur répartition entre employeurs successifs demeurent régies par les dispositions antérieures, y compris le plafond réglementaire et la prescription de deux ans à compter du versement des prestations, ainsi que leurs restitutions, prescriptions et voies de recours. Il n'est institué aucune restitution générale des sommes légalement dues.</p><p>La présente abrogation ne supprime ni les droits de l'assuré aux prestations, ni les obligations de suivi de santé et de sécurité au travail, ni les règles d'entrée, de séjour et d'emploi des étrangers, ni les responsabilités ou sanctions fondées sur une autre disposition. Aucune obligation déclarative, attestation ou garantie de remplacement n'est instituée.</p>"
o = add('L374-1',
    "Abrogation prospective de fond du remboursement patronal spécial de toutes les prestations déclenché par le seul défaut de contrôle médical d'immigration ou de preuve de présentation. Ce remboursement, sans lien causal exigé avec la maladie ou l'accident, double les obligations de santé et les sanctions autonomes d'emploi irrégulier ; sa fonction financière ne justifie pas ici de conserver cette charge accessoire. Les prestations et protections de santé restent distinctes.",
    "Coordonner les dispositions réglementaires prises pour le plafond et la date d'application de L374-1, ainsi que les éventuels renvois CESEDA L322-1, sans modifier ce code extérieur au lot. La récupération ancienne reste plafonnée et prescrite par deux ans à compter de chaque versement. La réalisation du risque, non la date d'une réclamation future, sépare les périodes. Les règles de droit répressif plus doux s'appliquent si une mesure est juridiquement qualifiée de sanction. Aucun gain national n'est chiffré.",
    "Suppression effective de la dette spéciale patronale de remboursement des prestations pour les risques nouveaux ; aucun remboursement de droit commun ni cotisation ordinaire n'est supprimé.",
    "Les obligations médicales, la sécurité au travail et les règles internationales ou de séjour demeurent hors de cette abolition ciblée. Les créances antérieures et la perte de recettes restent à documenter financièrement.",
    xml, 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : le remboursement spécial disparaît sans déclaration, agrément ou garantie substitutive ; les protections autonomes et leur circuit existant demeurent.",
    repeal="Remboursement spécial par les employeurs des prestations versées aux travailleurs étrangers en l'absence de contrôle médical d'immigration ou de preuve de sa présentation, pour les risques nouveaux.")
effect(o, 'obligation_removed', 'emploi-etrangers-fin-remboursement-medical-special',
    "Fin de la dette spéciale de remboursement des prestations à la charge de l'employeur.",
    "Employeur tenu au remboursement des prestations maladie, maternité, décès, invalidité et AT si le contrôle ou sa preuve fait défaut ; plafond réglementaire et prorata entre employeurs.",
    "Aucune dette sur ce fondement pour les risques réalisés dès l'entrée en vigueur ; principal des cotisations et responsabilités autonomes inchangés.", 'legal_duty',
    "Employeurs des travailleurs étrangers visés par les premier et deuxième alinéas.",
    "Risques nouveaux seulement ; risques antérieurs soumis aux anciennes garanties et à la prescription biennale.",
    "Aucun justificatif de remplacement ; perte de recettes non évaluée, suivi de santé maintenu.",
    "est tenu de rembourser aux organismes de sécurité sociale le montant des prestations",
    "Aucun remboursement des prestations de maladie, de maternité, de décès, d'invalidité ou d'accident du travail ne peut être réclamé à l'employeur sur son seul fondement")

add('L375-1',
    "Maintien intégral de l'exclusion des seules prestations en argent en cas de faute intentionnelle de l'assuré. Cette règle protège contre la provocation volontaire du risque et la fraude, sans exclure les soins ni sanctionner une simple imprudence. Aucun agrément, déclaration ou prélèvement à retirer n'est institué par cet article.",
    "La note source renvoie historiquement à L615-21 ; ce numéro n'est pas présent dans l'édition publique active du corpus consulté. Cette note documentaire ne crée pas à elle seule une nouvelle extension aux indépendants. Le corps normatif est maintenu avec son exigence d'intention ; ne pas transformer celle-ci en négligence ou en faute médicale. Aucun renvoi numérique nouveau n'est ajouté.",
    "La restriction maintenue est ciblée sur le risque volontaire et les prestations monétaires ; elle conserve l'accès aux soins et ne constitue pas une suppression de taxe.",
    "L'applicabilité historique indiquée dans la note L615-21 n'est pas certifiée au-delà des textes actifs disponibles. Aucun régime distinct n'est étendu par analogie.")

p = paras('L376-1')
p[6] = "<p>La personne victime, les établissements de santé, le tiers responsable et son assureur sont tenus d'informer la caisse de la survenue des lésions causées par un tiers dans des conditions fixées par décret. Pour un même accident et une même caisse, une information complète régulièrement délivrée par l'une de ces personnes dispense les autres de la transmettre à nouveau. Aucun envoi de confirmation de cette même information n'est exigé ; les informations nécessaires qui n'ont pas encore été transmises restent dues selon les règles applicables.</p>"
p[8] = "<p>Aucune indemnité forfaitaire de frais de recours ne peut être établie au titre des remboursements obtenus à compter de l'entrée en vigueur de la loi portant sa suppression. Cette suppression vaut également lorsque l'indemnité serait calculée sur les sommes dont le recouvrement aurait été obtenu si l'obligation d'information avait été respectée, pour les manquements commis à compter de cette date. Pour les remboursements obtenus avant cette date, les dispositions suivantes demeurent applicables : " + p[8][3:-4].strip() + " Le remboursement des prestations au titre du recours subrogatoire demeure dû dans les conditions du présent article.</p>"
p[9] = p[9].replace("Cette indemnité est établie", "L'indemnité forfaitaire due au titre des seuls remboursements antérieurs mentionnés au neuvième alinéa est établie")
p[10] = p[10].replace("l'indemnité est recouvrée", "l'indemnité forfaitaire due au titre de ces seuls remboursements antérieurs est recouvrée")
p.append("<p>La dispense de transmission répétée prévue au septième alinéa s'applique aux informations délivrées à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour un accident antérieur. Elle ne dispense pas d'informer la caisse d'un règlement amiable dans les conditions des articles L. 376-3 et L. 376-4. Les actes de procédure, recours, prescriptions, régularisations et restitutions relatifs aux périodes antérieures demeurent régis par les dispositions alors applicables, sans préjudice de l'application des règles répressives plus douces. Aucune restitution générale des indemnités forfaitaires légalement dues n'est instituée.</p>")
o = add('L376-1',
    "Réduction de fond en deux mesures : suppression de l'indemnité forfaitaire de gestion ajoutée au remboursement des prestations pour les remboursements nouveaux ; information unique de la caisse pour le même accident au lieu des transmissions répétées par les personnes énumérées. L'intégralité des huit premiers alinéas utiles est conservée, sous la seule dispense au septième ; les garanties de subrogation poste par poste, priorité de la victime, contradictoire et nullité biennale subsistent. Les alinéas de recouvrement de l'ancienne indemnité sont maintenus à leur place pour le stock antérieur.",
    "Les alinéas 7, 8 et 9 à 12 gardent leurs positions pour les renvois existants. D376-1, lu intégralement, impose déjà les délais 15 jours/3 mois et dispense le tiers ayant informé son assureur : le gain nouveau est la dispense transversale une fois la même caisse complètement informée, non cette dispense existante. Coordonner D376-1 I/III/V et son IV, qui calcule une indemnité même lorsque le recours n'a pu être exercé, afin qu'aucune indemnité nouvelle ne renaisse ; cette hypothèse est expressément exclue pour les manquements nouveaux au neuvième alinéa proposé. R376-1 permet l'évaluation forfaitaire du principal : elle demeure distincte. Les montants sources 91/910 euros sont indexés depuis 2007 et ne sont pas présentés comme les montants actuels ; leur règle complète et la date de 2007 restent reproduites pour les remboursements anciens. Recenser l'arrêté annuel de frais hors lot. L221-3-1 a été lu intégralement : son 3° permet de confier une mission à un organisme du réseau et reste pertinent pour la cession du douzième alinéa. Code civil et règles agricoles de recouvrement restent autonomes. Les nouveaux renvois à L376-3 et L376-4, sources assignées entièrement lues, ne sont pas des cibles fournies pour cet article et sont signalés ici sans ajout à reference_checks. Coût net non établi.",
    "L'accessoire financier de gestion est supprimé pour les remboursements nouveaux, sans abandon de la créance subrogatoire principale. Une seconde transmission du même accident à la même caisse est désormais expressément dispensée.",
    "Les indemnisations de la victime, remboursements de prestations, délais de déclaration encore utiles et information propre au règlement amiable restent dus. Aucun taux de cotisations ni économie nationale n'est déduit de cette coupe.",
    ''.join(p), 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : aucun fichier partagé ni attestation de dispense n'est créé. Les données légalement reçues suffisent ; l'information encore manquante demeure exigible. La caisse conserve ses missions, dont le financement privé accessoire est réduit sans compensation présumée.",
    removed=["Indemnité forfaitaire de frais de recours due au tiers des remboursements obtenus, avec minimum et maximum indexés, pour les remboursements nouveaux.", "Transmissions répétées à la même caisse des mêmes informations complètes sur un accident par la victime, l'établissement, le tiers responsable ou son assureur."])
effect(o, 'tax_removed', 'recours-tiers-suppression-indemnite-forfaitaire',
    "Suppression de l'accessoire forfaitaire de gestion, distinct du remboursement des prestations.",
    "Tiers responsable redevable du tiers des remboursements de prestations, sous minimum 91 euros et maximum 910 euros en valeurs légales initiales révisées chaque année depuis 2007.",
    "Zéro indemnité de frais pour les remboursements obtenus dès l'entrée en vigueur ; principal subrogatoire conservé.", 'euro',
    "Tiers responsables et leurs assureurs dans le champ des recours maladie, y compris agricole.",
    "Créances liées aux remboursements antérieurs conservées avec leurs limites et révisions ; aucune restitution générale.",
    "Aucune taxe ou déclaration de remplacement ; recettes de gestion perdues à évaluer.",
    "Le montant de cette indemnité est égal au tiers des sommes dont le remboursement a été obtenu",
    "Aucune indemnité forfaitaire de frais de recours ne peut être établie au titre des remboursements obtenus à compter de l'entrée en vigueur de la loi portant sa suppression.")
effect(o, 'obligation_merged', 'recours-tiers-information-unique',
    "Une transmission complète à la même caisse libère les autres personnes de la répétition des mêmes données.",
    "Obligations de la victime, de l'établissement, du responsable et de son assureur ; D376-1 ne dispense déjà que le tiers ayant informé son assureur.",
    "Une information complète régulièrement délivrée à la même caisse pour le même accident ; seules données manquantes restent dues.", 'legal_duty',
    "Victimes, établissements de santé, tiers responsables et assureurs.",
    "Informations délivrées dès la réforme, même pour accidents antérieurs ; information du règlement amiable distincte.",
    "Aucun registre, accès aux données nouveau ou certificat de dispense ; aucune confirmation de données identiques.",
    "La personne victime, les établissements de santé, le tiers responsable et son assureur sont tenus d'informer la caisse de la survenue des lésions causées par un tiers",
    "Pour un même accident et une même caisse, une information complète régulièrement délivrée par l'une de ces personnes dispense les autres de la transmettre à nouveau.")

add('L376-2',
    "Maintien intégral de la priorité de la victime ou de ses ayants droit sur les caisses pour l'action en remboursement des déboursés. Le rapprochement avec la priorité de L376-1 ne suffit pas à démontrer un doublon de champ parfait ; abroger cette règle ferait courir un risque sur une garantie favorable sans retirer d'obligation déclarative ni de taxe.",
    "La proposition de L376-1 de ce lot conserve la subrogation poste par poste et la priorité de la victime ; elle supprime seulement les frais forfaitaires nouveaux et les informations répétées. Le renvoi reste opérant et aucune coordination textuelle supplémentaire n'est nécessaire ici. La note L615-21 est historique, numéro absent du corpus actif ; elle n'est pas utilisée pour inventer une extension normative nouvelle.",
    "La priorité d'indemnisation personnelle demeure intégrale. Elle est une protection de la victime, non une réduction additionnelle de l'indemnité forfaitaire supprimée par L376-1.",
    "L'étendue des déboursés réparables reste celle du droit commun et du recours social. Aucun gain fiscal, contentieux ou budgétaire supplémentaire n'est établi.")

xml = "<p>Le règlement amiable pouvant intervenir entre le tiers et l'assuré ne peut être opposé à la caisse de sécurité sociale qu'autant que celle-ci a été invitée à y participer par lettre recommandée et ne devient définitif que quinze jours après l'envoi de cette lettre. Toutefois, lorsque la caisse a participé au règlement et y a expressément consenti, celui-ci peut devenir définitif dès ce consentement sans attendre l'expiration du délai de quinze jours.</p><p>Cette faculté s'applique aux règlements amiables qui ne sont pas encore devenus définitifs à la date d'entrée en vigueur de la loi portant la présente réforme et aux règlements conclus à compter de cette date. Elle ne vaut ni renonciation tacite de la caisse à son recours ni réouverture d'un règlement déjà définitif ; les droits de la victime et les règles d'information de l'article L. 376-4 demeurent applicables.</p>"
o = add('L376-3',
    "Réduction de fond ciblée : le délai incompressible de quinze jours ne bloque plus un règlement auquel la caisse a effectivement participé et expressément consenti. Le recommandé, l'invitation préalable, l'opposabilité et le délai protecteur en l'absence de consentement sont maintenus ; il ne s'agit pas du préavis de rupture d'emploi.",
    "Le délai conservé court de l'envoi de la lettre, comme dans la source, non de sa réception. La dispense repose sur un accord exprès dans une procédure déjà existante, sans assimilation du silence à un consentement. Coordination avec L376-4 pour l'information du règlement ; ce renvoi nouveau dans cet article vise un texte assigné entièrement lu mais non fourni comme cible requise, et n'est donc pas ajouté à reference_checks. La note L615-21 demeure une indication historique non recodifiée ici.",
    "L'attente de quinze jours disparaît seulement lorsque sa finalité de participation et de consentement de la caisse est déjà satisfaite. Aucun autre délai légal ni recours de la caisse n'est supprimé.",
    "Sans participation et consentement exprès de la caisse, la règle des quinze jours subsiste. Le nombre effectif de jours gagnés dépend de la date de consentement et n'est pas chiffré.",
    xml, 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : l'accord exprès est une faculté pour accélérer un règlement déjà négocié, sans formulaire ni demande supplémentaire imposés ; le circuit ordinaire reste disponible.",
    removed=["Attente obligatoire jusqu'au quinzième jour après l'envoi de l'invitation, même lorsque la caisse a participé au règlement amiable et y a déjà expressément consenti."])
effect(o, 'deadline_reduced', 'recours-tiers-accord-expres-fin-attente',
    "Fin de l'attente obligatoire après consentement exprès de la caisse participante.",
    "Règlement non définitif avant quinze jours après l'envoi de la lettre, y compris si la caisse l'a déjà approuvé.",
    "Règlement définitif possible dès le consentement exprès de la caisse participante ; sinon quinze jours inchangés.", 'calendar_days',
    "Assurés victimes, tiers et caisses parties à un règlement amiable.",
    "Règlements futurs et ceux non encore définitifs lors de l'entrée en vigueur ; aucune réouverture des règlements définitifs.",
    "Aucun dossier nouveau ; la dispense suppose un consentement réel, sans consentement présumé.",
    "ne devient définitif que quinze jours après l'envoi de cette lettre",
    "celui-ci peut devenir définitif dès ce consentement sans attendre l'expiration du délai de quinze jours.")

p = paras('L376-4')
p[2] = p[2].replace("Une seule pénalité est due à raison du même sinistre.", "Une seule pénalité est due à raison du même sinistre. Aucune pénalité ne peut être prononcée pour l'absence d'une transmission dont l'intéressé est dispensé par le septième alinéa de l'article L. 376-1.")
p[4] = p[4].replace("La pénalité est recouvrée selon les modalités définies au neuvième alinéa du I de l'article L. 114-17-2.", "La pénalité peut être recouvrée par retenues sur les prestations à venir, dans les conditions définies au neuvième alinéa du I de l'article L. 114-17-2.")
p.append("<p>La dispense prévue au troisième alinéa s'applique aux manquements qui n'ont pas donné lieu à une sanction définitive à la date d'entrée en vigueur de la loi portant la présente réforme, ainsi qu'aux manquements postérieurs. Les droits de recours et les règles d'application dans le temps de la loi répressive plus douce demeurent applicables.</p>")
o = add('L376-4',
    "Coordination nécessaire avec l'information unique prévue à L376-1 : le défaut de répétition d'une transmission désormais dispensée ne peut être puni. Le renvoi de recouvrement est précisé dans sa portée réelle de retenue sur prestations à venir, sans ajout d'une majoration ou d'une contrainte. Les informations utiles sur le règlement amiable, l'inopposabilité de prescription, la pénalité proportionnée à la gravité et les plafonds favorables sont intégralement maintenus ; aucune deuxième suppression du devoir d'information n'est comptée.",
    "Le renvoi au septième alinéa de L376-1 demeure exact, les alinéas de ce dernier n'étant pas déplacés. Le plafond de 50 % et celui de 30 000 euros pour le particulier, l'unicité par sinistre, le contentieux social et la prescription de deux ans à compter de l'envoi de notification sont maintenus. L114-17-2 a été lu en entier dans le corpus : le neuvième alinéa du I permet des retenues sur prestations à venir, alors que mise en demeure, contrainte et majoration de 10 % figurent au huitième. La proposition explicite donc la portée étroite du renvoi existant au neuvième, sans le remplacer par le huitième : elle ne crée ni nouveau titre de contrainte ni majoration de 10 %. L'absence de référence source à une procédure générale de recouvrement est signalée, sans réparer cette lacune par une nouvelle charge. L'indemnité de gestion supprimée dans L376-1 ne doit pas être rétablie au nom de cette pénalité distincte. L114-17-2 est un renvoi source conservé, non une cible nouvelle inventée.",
    "La réforme ne crée pas une nouvelle suppression de taxe : elle empêche la sanction d'une information répétée devenue légalement inutile, tout en préservant la sanction du défaut d'information encore due.",
    "Les obligations relatives à la survenue des lésions non encore signalées et au règlement amiable subsistent. Le montant net des sanctions ou des coûts de conformité n'est pas évalué.",
    ''.join(p), 'coordination_only',
    "Aucune charge nouvelle n'est identifiée : aucune donnée, preuve périodique ou attestation de dispense ne remplace la transmission supprimée ; les contrôles et recours sont ceux du dispositif existant.")
effect(o, 'coordination', 'recours-tiers-information-unique',
    "Exclusion des pénalités pour absence d'une répétition désormais dispensée.",
    "Le troisième alinéa sanctionne le non-respect de l'obligation du septième alinéa de L376-1, sous réserve d'une seule pénalité par sinistre.",
    "Cette sanction ne peut viser l'absence de transmission dispensée par L376-1 ; information utile et plafonds inchangés.", 'legal_duty',
    "Tiers responsables et assureurs soumis à l'information des caisses.",
    "Manquements futurs et sanctions non définitives ; réserve de la loi répressive plus douce.",
    "Aucune sanction ni formalité de remplacement ; même mesure que le septième alinéa de L376-1.",
    "Le deuxième alinéa du présent article est également applicable à l'assureur du tiers responsable ou au tiers responsable lorsqu'ils ne respectent pas l'obligation d'information de la caisse prévue au septième alinéa de l'article L. 376-1.",
    "Aucune pénalité ne peut être prononcée pour l'absence d'une transmission dont l'intéressé est dispensé par le septième alinéa de l'article L. 376-1.")
effect(o, 'coordination', 'penalites-sociales-portee-renvoi-retenues',
    "Identification exacte du mode de recouvrement réellement visé par le neuvième alinéa du I de L114-17-2.",
    "Renvoi global aux modalités du neuvième alinéa, lequel permet seulement des retenues sur prestations futures dans son champ.",
    "Possibilité de retenues sur prestations expressément identifiée ; aucune importation de la contrainte ou de la majoration de 10 % du huitième alinéa.", 'legal_duty',
    "Tiers responsables ou assureurs débiteurs de la pénalité, lorsque des prestations peuvent légalement faire l'objet d'une retenue.",
    "Précision du renvoi existant, sans augmentation de pénalité ni extension de son champ ; prescription biennale maintenue.",
    "Aucun mode de recouvrement nouveau, titre ou majoration supplémentaire n'est institué.",
    "La pénalité est recouvrée selon les modalités définies au neuvième alinéa du I de l'article L. 114-17-2.",
    "La pénalité peut être recouvrée par retenues sur les prestations à venir, dans les conditions définies au neuvième alinéa du I de l'article L. 114-17-2.")

penal_transition = "<p>La présente abrogation s'applique dès l'entrée en vigueur de la loi qui la prévoit. Les faits antérieurs n'ayant pas donné lieu à une condamnation passée en force de chose jugée bénéficient des règles d'application de la loi pénale plus douce. Les décisions irrévocables ne sont pas remises en cause, sans préjudice des règles de cessation d'exécution d'une peine lorsque le fait n'a plus le caractère d'une infraction pénale.</p>"
xml = "<p>Le présent article est abrogé. La seule offre ou fourniture, contre une rémunération convenue à l'avance, de services destinés à permettre à un assuré d'obtenir les prestations qui lui sont dues ne constitue plus l'infraction prévue par le présent article.</p>" + penal_transition + "<p>Les renvois au présent article ne peuvent maintenir cette incrimination dans un autre régime ou pour une autre prestation. Les dispositions autonomes relatives à la fraude, aux menaces, à l'abus d'autorité, aux pratiques commerciales illicites et à l'exercice des professions réglementées restent applicables. Aucune autorisation, déclaration ou interdiction générale de remplacement n'est instituée.</p>"
o = add('L377-2',
    "Abrogation de fond de l'interdiction pénale générale de l'intermédiation rémunérée à prix convenu pour obtenir des prestations dues. Le seul caractère payant de l'aide ne démontre ni fraude ni abus ; les infractions de coercition, détournement de patients et fausse déclaration restent autonomes. Suppression des amendes spéciales de 3 750 et 7 500 euros, sans agrément substitutif.",
    "L821-5, lu entièrement dans le corpus, étend expressément L377-2 et L377-4 à l'AAH à son quatrième alinéa : retirer ce renvoi dans ce texte hors lot, sans toucher incessibilité, prescription biennale et financement de l'AAH. La clause anti-rétablissement rend dès ici l'abrogation applicable à cette extension. Les notes citent L623-1, L721-8 et L721-14 pour la vieillesse/cultes ; ces mentions historiques ne correspondent pas au L623-1 actuel relatif à maternité/paternité, entièrement lu. L'ordonnance n° 2002-411, article 47 III, est une coordination extérieure à identifier sans prétendre la réécrire. La réserve d'interprétation de 2025 sur la filiation de deux femmes reste étrangère à l'abrogation pénale et pleinement préservée.",
    "La prestation d'aide rémunérée licite n'est plus interdite pénalement par principe. Les protections contre fraude et coercition demeurent, sans taxe ni autorisation de remplacement.",
    "Les professions réglementées et infractions autonomes ne sont pas libéralisées par ce texte. Les renvois extérieurs historiques ne sont pas tous recodifiés dans ce lot ; aucun volume d'amendes évitées n'est établi.",
    xml, 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : la suppression ne remplace pas la prohibition par une carte, un registre, une déclaration ou une condition nouvelle d'obtention des prestations.",
    repeal="Incrimination générale de l'offre d'intermédiation rémunérée à l'avance pour obtenir les prestations sociales dues, et ses deux montants d'amende, avec extinction des extensions par renvoi.")
effect(o, 'obligation_removed', 'prestations-sociales-fin-interdiction-aide-payante',
    "Suppression d'une interdiction pénale portant sur la seule intermédiation payante.",
    "Offre rémunérée à l'avance passible de 3 750 euros, 7 500 euros en récidive dans un an, indépendamment d'une fraude particulière.",
    "Cette seule offre ou fourniture n'est plus l'infraction de L377-2 ; fraudes, abus et professions réglementées inchangés.", 'legal_duty',
    "Intermédiaires et assurés recourant à une aide payante pour leurs prestations, y compris extensions légales par renvoi.",
    "Dès l'entrée en vigueur avec application de la loi pénale plus douce et règles de cessation d'exécution dans leur champ.",
    "Aucun agrément ou enregistrement de remplacement ; recours contre les abus maintenus.",
    "tout intermédiaire convaincu d'avoir offert ou fait offrir ses services moyennant émoluments convenus à l'avance à un assuré social",
    "ne constitue plus l'infraction prévue par le présent article.")

add('L377-3',
    "Maintien intégral nécessaire de la protection du libre choix des soins contre menaces, abus d'autorité et captation par avantages financiers ou ristournes. La suppression de l'intermédiation payante ordinaire de L377-2 n'autorise pas ces conduites portant atteinte au consentement ou à la probité. La source n'impose pas une formalité administrative générale que l'on puisse retirer.",
    "Montants conservés : 3 750 euros et six mois, ou l'une des peines seulement. L'abrogation proposée de L377-4 supprime le maximum automatiquement obligatoire en récidive, sans supprimer les peines de L377-3 et sans en augmenter les plafonds. L'extension documentaire de l'article 47 III de l'ordonnance de 2002 reste à coordonner hors des cinq codes, sans déduction sur son champ non fourni.",
    "La règle maintenue vise des pratiques de coercition ou de captation des patients, protection essentielle distincte d'une simple aide administrative rémunérée.",
    "Aucun bilan d'efficacité pénale ni chiffrage de coûts n'est fourni. Les infractions et règles déontologiques autonomes restent distinctes.")

xml = "<p>Le présent article est abrogé. L'application obligatoire du maximum des deux peines en raison d'une condamnation antérieure pour la même infraction et la publication du jugement aux frais du condamné sur son seul fondement sont supprimées.</p>" + penal_transition + "<p>Les renvois au présent article ne peuvent rétablir l'application automatique du maximum ni cette publication particulière. Les peines prévues par les autres articles du présent chapitre et les règles générales d'individualisation et de récidive demeurent applicables dans leur champ propre, sans augmentation de leurs maxima.</p>"
o = add('L377-4',
    "Abrogation de fond du maximum pénal obligatoire dès une précédente condamnation pour la même infraction et de la publication spéciale du jugement plafonnée à 7,5 euros. Ces automatismes ne sont pas nécessaires au maintien des incriminations de fraude et coercition ; le juge conserve leurs peines et les règles générales d'individualisation sans nouveau plafond. La suppression de cette petite charge ne vaut pas économie nationale chiffrée.",
    "Coordonner le quatrième alinéa de L821-5 (AAH), lu dans le corpus, et les renvois historiques cultes L721-8/L721-14 et ordonnance de 2002 article 47 III. La clause de non-rétablissement couvre leurs effets sans prétendre avoir réécrit ces articles extérieurs au lot. Le plafond source de publication est exactement 7,5 euros ; il n'est ni actualisé ni remplacé par un montant supérieur. La loi pénale plus douce vaut pour les procédures non définitivement jugées ; aucune révision générale des décisions irrévocables n'est promise.",
    "Le juge n'est plus tenu de prononcer les maxima sur le seul antécédent et la publication particulière payante disparaît. Les infractions restantes du chapitre et leurs plafonds sont conservés.",
    "Les règles générales de récidive ne sont pas abolies. Le nombre de décisions concernées et les coûts réels de publication ne sont pas établis.",
    xml, 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : aucune publication, sanction ou obligation de suivi ne remplace le dispositif spécial ; l'individualisation judiciaire repose sur les règles générales existantes.",
    repeal="Maximum obligatoire des deux peines après une condamnation pour la même infraction et pouvoir spécial de publication du nouveau jugement aux frais du condamné, limité à 7,5 euros.")
effect(o, 'obligation_removed', 'sanctions-sociales-fin-maxima-et-publication',
    "Suppression du prononcé obligatoire des maxima et de la publication spéciale payante.",
    "Maximum des deux peines toujours appliqué en présence d'une précédente condamnation pour la même infraction ; publication facultative aux frais du condamné plafonnée à 7,5 euros.",
    "Aucun maximum automatique ni publication sur L377-4 ; peines des autres articles et individualisation de droit commun maintenues.", 'legal_duty',
    "Personnes poursuivies pour les infractions encore applicables du chapitre et ses extensions.",
    "Entrée en vigueur et loi pénale plus douce pour les affaires non définitivement jugées ; décisions irrévocables sous leurs règles propres.",
    "Aucune sanction ou formalité nouvelle ; maxima des incriminations autonomes non augmentés.",
    "Le maximum des deux peines sera toujours appliqué au délinquant lorsqu'il aura déjà subi une condamnation pour la même infraction",
    "L'application obligatoire du maximum des deux peines en raison d'une condamnation antérieure pour la même infraction et la publication du jugement aux frais du condamné sur son seul fondement sont supprimées.")

add('L377-5',
    "Maintien intégral nécessaire de la possibilité judiciaire d'exclusion des praticiens et des sanctions de fausse déclaration intentionnelle ou collusion avec les assurés. Ces protections ciblent la fraude et la probité de l'assurance sociale ; elles ne justifient aucune nouvelle déclaration. L'abrogation de l'intermédiation payante ordinaire n'exclut pas les autres infractions du chapitre.",
    "Les 3 750 euros et six mois, ou une seule de ces peines, restent intacts et ne deviennent plus automatiquement des maxima par L377-4. Le premier alinéa garde une portée effective pour L377-3 ; il ne rétablit pas L377-2 abrogé. L'exclusion reste facultative selon la source ; aucune exclusion automatique, durée inventée ou taxe de contrôle n'est créée. Extension de l'ordonnance de 2002 signalée dans la note, hors lot.",
    "La répression intentionnelle de la fraude médicale et la faculté d'exclusion sont conservées ; aucune formalité administrative ou réduction de prélèvement n'est nouvellement comptée.",
    "Le pouvoir de sanction autonome demeure nécessaire. Les régimes déontologiques et les procédures extérieures ne sont pas remaniés ou déclarés entièrement vérifiés.")

old = by_number['L378-1']['source_xml']
xml = old.replace("mentionné à l'article L. 3142-22 du code du travail", "mentionné à l'article L. 3142-16 du code du travail ou, pour les congés accordés sous l'empire des dispositions antérieures, à l'article L. 3142-22 de ce code dans sa rédaction alors applicable")
o = add('L378-1',
    "Coordination nécessaire du fondement du congé de proche aidant vers L3142-16, avec sauvegarde expresse des congés accordés sur l'ancien fondement L3142-22. La reprise d'activité, l'absence de rémunération de l'aide familiale et la neutralisation de la période restent intégrales ; aucune réécriture stylistique ou baisse fictive n'est ajoutée.",
    "L3142-16, L3142-22 et L3142-24 officiels ont été lus intégralement dans le corpus public. L3142-16 définit désormais les neuf liens ou situations de proche aidant ; L3142-22 garantit le retour à un emploi équivalent et n'est plus le fondement initial cité par la version de 2015. Nouveau renvoi à L3142-16 non fourni parmi les cibles requises : signalé ici sans ajouter de cible à reference_checks. L341-2 reste le régime propre d'invalidité ; L313-1 proposé n'autorise pas à réintroduire une affiliation minimale supprimée pour les prestations nouvelles.",
    "La modification répare un renvoi de fondement du congé en conservant la neutralisation et les congés anciens. Elle ne réduit pas une durée ou un prélèvement par elle-même.",
    "Le champ des personnes aidées reste celui des textes du congé ; aucune extension automatique aux agents publics ou aux pensions militaires n'est déduite du contrat unique.",
    xml, 'coordination_only',
    "Aucune charge nouvelle n'est identifiée : les mêmes conditions de reprise et de rémunération subsistent ; le renvoi corrigé ne crée ni justificatif, ni notification, ni durée minimale supplémentaire.")
effect(o, 'coordination', 'proche-aidant-coordination-fondement-conge',
    "Actualisation du fondement du congé, avec référence historique conservée pour les anciens congés.",
    "Le texte de 2015 cite L3142-22 pour le congé ; l'article actif L3142-22 concerne désormais le retour à l'emploi.",
    "L3142-16 identifie le congé actuel ; l'ancien L3142-22 reste visé dans sa rédaction applicable aux congés anciens.", 'regime',
    "Assurés reprenant leur activité à l'issue d'un congé de proche aidant.",
    "Situations futures éligibles et congés accordés sous les dispositions antérieures ; neutralisation inchangée.",
    "Aucun nouveau régime d'emploi ni nouveau document ; simple coordination du droit social maintenu.",
    "congé de proche aidant mentionné à l'article L. 3142-22 du code du travail",
    "congé de proche aidant mentionné à l'article L. 3142-16 du code du travail")

xml = "<p>Le présent article est abrogé pour les années d'assujettissement commençant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant la présente abrogation. Aucune cotisation subsidiaire maladie ne peut être établie ou recouvrée au titre de ces années sur son fondement.</p><p>Pour les années antérieures, les règles d'assujettissement, d'assiette et de calcul, les exclusions liées aux revenus d'activité et à ceux du conjoint ou partenaire, aux pensions, rentes et allocations de chômage, l'abattement, le plafond, la dégressivité, les assiettes minimales favorables des travailleurs indépendants et agricoles et les autres exonérations et dérogations applicables demeurent régis par les dispositions alors en vigueur. Le recouvrement l'année suivante, les contrôles, régularisations, restitutions, prescriptions et recours correspondants restent possibles selon ces dispositions, sans restitution générale des sommes légalement dues et sans double paiement.</p><p>Aucune déclaration ni communication de données exclusivement destinée à l'établissement ou au recouvrement de cette cotisation pour les années supprimées ne peut être exigée ou effectuée sur le fondement du présent article, y compris par renvoi réglementaire. Les échanges légalement nécessaires aux seules années antérieures et les traitements fondés sur une autre disposition conservent leur régime.</p><p>La prise en charge des frais de santé dans les conditions de l'article L. 160-1 demeure garantie sans subordination au paiement d'une cotisation supprimée. Aucun prélèvement de remplacement, aucune extension d'assiette d'un autre prélèvement et aucune nouvelle formalité d'affiliation ne sont institués par la présente abrogation. Les cotisations et contributions légalement autonomes, notamment la cotisation prévue à l'article L. 380-3-1, conservent leur champ propre.</p>"
o = add('L380-2',
    "Abrogation prospective de fond de la cotisation subsidiaire maladie et de ses obligations propres : ce prélèvement accessoire sur revenus du patrimoine et moyens d'existence n'est pas une condition du droit aux soins de L160-1 et peut être retiré sans supprimer l'affiliation. La suppression est entière pour les nouvelles années, avec préservation des allègements pour les années anciennes. Aucune recette ou cotisation de remplacement n'est créée.",
    "D380-1 officiel a été lu : formule 6,5 % × (A − 0,5 PASS) × [1 − R/(0,2 PASS)], A plafonné à 8 PASS, prorata et non-cumul avec L380-3-1. Ces valeurs ne sont pas inventées ni requalifiées en taux uniforme sur tout patrimoine. Coordonner D380-1, les règles réglementaires d'appel et d'échanges fiscaux et les affectations financières ; aucune de ces coordinations hors lot n'est déclarée réécrite. Le renvoi source au cinquième alinéa pour les revenus d'activité est une incohérence préexistante : la source place l'abattement au cinquième et le calcul dégressif après ; pas de correction silencieuse du stock ancien. Le renvoi source L633-1 doit également être vérifié dans sa version applicable. L152 LPF conserve ses autres finalités, mais non un échange exclusivement destiné aux nouvelles années supprimées. Le nouveau renvoi de sauvegarde à L380-3-1 vise une source assignée entièrement lue mais non fournie comme cible requise de cet article ; il est signalé ici sans ajout à reference_checks. Perte de recettes maladie, égalité entre catégories et financement durable à évaluer, sans compensation inventée ni condition de financement ajoutée à cette abolition.",
    "La cotisation annuelle est entièrement supprimée pour les années nouvelles, avec ses déclarations et échanges exclusivement nécessaires à son établissement. Le droit aux soins demeure et le régime frontalier suisse n'est pas aboli par assimilation.",
    "La suppression commence au 1er janvier suivant l'entrée en vigueur ; les revenus d'une année antérieure ne sont pas exonérés par le seul report de recouvrement. Les autres cotisations et contributions restent autonomes ; solde public net inconnu.",
    xml, 'material_reduction',
    "Aucune charge nouvelle n'est identifiée : aucun dossier, taux, déclaration, délai minimal ou registre ne remplace la cotisation. Les seules obligations anciennes restent bornées aux années taxables antérieures ; les droits maladie restent servis par le circuit existant.",
    repeal="Cotisation subsidiaire maladie annuelle sur revenus patrimoniaux, plus-values, bénéfices non professionnels et moyens d'existence des assurés à faibles revenus d'activité, ainsi que déclarations et échanges exclusivement nécessaires aux nouvelles années.",
    benefit="Sont examinés et conservés pour toute année antérieure encore liquidable : seuil d'activité de l'assuré et du conjoint ou partenaire, exclusion en présence de pension de retraite ou d'invalidité, rente ou chômage chez l'un des membres du couple, abattement, plafond d'assiette, dégressivité jusqu'à taux nul, planchers favorables de revenus d'activité des indépendants et agriculteurs, prorata et non-cumul avec L380-3-1 constatés dans D380-1. Pour les nouvelles années la cotisation entière est supprimée : ces avantages deviennent sans objet uniquement à son égard, sans prélèvement équivalent, extension d'assiette ni restriction de l'accès L160-1. Les futurs assurés éligibles bénéficient également de l'absence de cotisation ; aucune exonération autonome d'un autre impôt n'est retirée.")
effect(o, 'tax_removed', 'cotisation-subsidiaire-maladie-suppression',
    "Suppression entière de la cotisation subsidiaire maladie pour les nouvelles années.",
    "Cotisation annuelle des assurés satisfaisant les conditions 1° et 2° ; assiette de revenus patrimoniaux et non professionnels et moyens d'existence. D380-1 : 6,5 % × (A − 0,5 PASS) × [1 − R/(0,2 PASS)], A limité à 8 PASS, prorata et exclusions applicables.",
    "Zéro cotisation L380-2 pour les années nouvelles ; assiette de ce prélèvement supprimée, aucun prélèvement de remplacement.", 'percent',
    "Personnes relevant de L160-1 à faibles revenus d'activité, sans pension, rente ou chômage au sens des conditions légales du ménage.",
    "Années débutant le 1er janvier suivant l'entrée en vigueur ; années antérieures, abattements, exemptions, remboursements et recours protégés.",
    "Aucune taxe ou condition d'affiliation nouvelle ; perte de financement de l'assurance maladie non chiffrée.",
    "Les personnes mentionnées à l'article L. 160-1 sont redevables d'une cotisation annuelle lorsqu'elles remplissent les conditions suivantes :",
    "Aucune cotisation subsidiaire maladie ne peut être établie ou recouvrée au titre de ces années sur son fondement.")
effect(o, 'coordination', 'cotisation-subsidiaire-maladie-suppression',
    "Extinction des déclarations et échanges exclusivement liés à la cotisation supprimée, sans nouvelle mesure fiscale comptée.",
    "Déclarations réglementaires des assujettis et communication fiscale nominative pour établir la cotisation annuelle.",
    "Aucune déclaration ou communication sur ce seul fondement pour les années supprimées ; échanges légalement utiles au stock ancien et finalités autonomes conservés.", 'legal_duty',
    "Anciens assujettis, administrations fiscales et organismes de recouvrement.",
    "Suit exactement la séparation des années de la suppression de L380-2 ; pas de nouvelle déclaration annuelle résiduelle pour une année exonérée en totalité.",
    "Pas de collecte de remplacement ni d'accès aux données supplémentaire.",
    "Un décret détermine le taux et les modalités de calcul de cette cotisation ainsi que les obligations déclaratives incombant aux assujettis.",
    "Aucune déclaration ni communication de données exclusivement destinée à l'établissement ou au recouvrement de cette cotisation pour les années supprimées ne peut être exigée ou effectuée sur le fondement du présent article, y compris par renvoi réglementaire.")

p = paras('L380-3-1')
p[3] = p[3].replace("à l'article L. 380-2.", "à l'article L. 380-2. L'exclusion de cette dernière cotisation demeure applicable à toutes les années pour lesquelles elle peut encore être établie en vertu des dispositions transitoires de cet article.")
o = add('L380-3-1',
    "Coordination limitée à la cotisation subsidiaire maladie supprimée : la non-soumission des frontaliers demeure explicite pour toute année ancienne encore taxable. Les I à III et les autres dispositions du IV restent intégralement maintenus, notamment le droit d'option issu de l'accord, ses transitions et les exclusions CSG, CRDS et L131-9. La cotisation propre d'assurance maladie des frontaliers est un financement principal d'une couverture choisie dans un cadre international, distinct du prélèvement accessoire L380-2 ; elle n'est pas supprimée par analogie.",
    "D380-2, lu intégralement, fixe 8 % × (A − 0,25 PASS), assiette de revenus du dernier exercice connu, dates d'entrée/sortie et prorata ; ces modalités et leur abattement demeurent. Le IV renvoie au IV de CGI1417 (définition du revenu), non aux seuils de taxe foncière des I/II. Le II est une transition de douze ans depuis l'accord de 1999, non une faculté nouvelle de douze ans ni une réouverture de l'assurance privée aujourd'hui. Il est conservé pour ses effets historiques. L'accord Suisse-UE et les droits d'option doivent être coordonnés par leurs voies propres, sans présumer une abrogation nationale des obligations suisses.",
    "Le seul changement explicite la survie de l'exclusion de L380-2 pour les années antérieures ; le régime international et sa cotisation spécifique ne changent pas. Aucune seconde cotisation supprimée n'est comptée.",
    "Aucune exemption suisse ne peut être créée par la seule loi française. Cette coordination ne ferme pas les futures options légalement ouvertes par l'accord ni ne réactive une transition expirée.",
    ''.join(p), 'coordination_only',
    "Aucune charge nouvelle n'est identifiée : aucune option, déclaration ou preuve de contrat supplémentaire n'est ajoutée. Les exigences historiques du II et le financement propre du IV demeurent dans leur champ temporel.",
    benefit="Le droit de demander l'exemption suisse et l'affiliation française des travailleurs puis, par III, des pensionnés et de leurs ayants droit est maintenu dans les limites de l'accord. La faculté historique d'assurance privée du II, sa couverture complète des soins, ses exclusions de 2006 et la renonciation à tout moment restent intégrales, sans réouvrir sa fenêtre expirée. Les exclusions de CSG L136-1, CRDS de l'ordonnance de 1996, L131-9 et L380-2 restent expressément applicables ; pour L380-2, elles valent aussi pour le stock ancien. Le taux propre de D380-2 reste distinct avec l'abattement de 0,25 PASS et le prorata, sans hausse pour compenser l'abolition de la cotisation subsidiaire. Les futures situations recevables au titre de l'accord gardent ces avantages.")
effect(o, 'coordination', 'cotisation-subsidiaire-maladie-suppression',
    "Maintien de l'exclusion des frontaliers pour les anciennes années encore taxables à L380-2.",
    "Exclusion des cotisations L131-9 et L380-2 au IV, parallèlement à la cotisation spécifique des frontaliers.",
    "Exclusion L380-2 expressément conservée pour le stock taxable ; aucune cotisation subsidiaire future et aucune modification du taux propre frontalier.", 'regime',
    "Frontaliers et titulaires de pensions ou rentes suisses relevant de l'option française.",
    "Anciennes années restant liquidables ou contestables ; affiliations nouvelles sous l'accord toujours recevables selon leurs règles.",
    "Aucun nouveau justificatif, prélèvement ou formalité ; pas une seconde suppression fiscale.",
    "ne sont pas redevables des cotisations visées à l'article L. 131-9 et à l'article L. 380-2.",
    "L'exclusion de cette dernière cotisation demeure applicable à toutes les années pour lesquelles elle peut encore être établie en vertu des dispositions transitoires de cet article.")

add('L380-4',
    "Maintien intégral de l'affiliation des pupilles de l'État : cette protection de mineurs sans soutien parental n'impose aucune déclaration, prélèvement, délai minimal ou autorisation à supprimer. Elle garde une utilité autonome après l'abolition proposée de L380-2 ; la résidence et la prise en charge des soins ne sont pas fermées.",
    "L'affiliation au titre du chapitre ne vaut pas assujettissement à une cotisation désormais supprimée. La proposition de L380-2 maintient expressément le droit aux soins et distingue les années antérieures. Aucun transfert de charges sur les pupilles, tuteurs ou familles d'accueil n'est créé.",
    "La règle maintenue assure une affiliation protectrice ; aucune nouvelle simplification matérielle n'est attribuée à cette conservation.",
    "Les règles civiles de tutelle et de prise en charge demeurent extérieures à ce texte. Aucun effet budgétaire ni nombre de personnes n'est calculé.")

add('L381-1',
    "Maintien intégral de l'assurance vieillesse des parents sans activité ou à temps partiel recevant les prestations familiales visées. Les conditions de ressources, d'âge et de nombre d'enfants délimitent cette solidarité ; la cotisation incombe exclusivement aux organismes, sans paiement nouveau du parent. L'exclusion d'un double avantage pour la même période et le même enfant coordonne des validations équivalentes et ne ferme pas les droits futurs éligibles.",
    "L351-5 proposé actualise le congé parental vers L1225-47/48 et garde le fondement ancien ; le non-cumul du dernier alinéa demeure pertinent. D381-1/2/2-1, lus dans le corpus avec leurs notes 2023 et 2026, précisent ressources, enfants et activité : ils ne justifient pas de remplacer une affiliation solidaire par la capitalisation du salarié privé. Le 1° de L9 des pensions civiles et militaires est une validation du régime public, non un contrat privé ni une indemnité de rupture. Aucun plafond de six mois ou seuil d'un an n'est ajouté à l'affiliation.",
    "Les droits de retraite solidaires financés par les organismes familiaux sont intégralement conservés. Ils ne sont ni une taxe privée à supprimer ni un transfert chiffré vers la capitalisation.",
    "Les ressources et validations équivalentes demeurent contrôlées selon les règles existantes. Le maintien ne démontre aucune baisse de prélèvement ou économie nationale.")

xml = by_number['L381-2']['source_xml'].replace(
    "La somme des durées d'affiliation à l'assurance vieillesse du régime général de sécurité sociale au titre des deuxième et troisième alinéas du présent article ne peut excéder une durée totale d'un an sur l'ensemble de la carrière.",
    "Pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente réforme, la somme des durées d'affiliation à l'assurance vieillesse du régime général de sécurité sociale au titre des deuxième et troisième alinéas du présent article n'est plus limitée à une durée totale d'un an sur l'ensemble de la carrière. Les périodes d'affiliation antérieures ne réduisent pas les droits ouverts au titre de ces périodes nouvelles, y compris lorsqu'un congé ou une interruption d'activité a commencé avant cette entrée en vigueur. Les conditions de chaque affiliation et les limites propres au congé ou à l'allocation demeurent applicables ; les droits et recours afférents aux périodes antérieures sont conservés sans réouverture générale ni double validation.")
o = add('L381-2',
    "Réduction de fond d'une restriction : suppression, pour les périodes nouvelles, du plafond global d'un an d'affiliation vieillesse au titre du congé de proche aidant ou de l'interruption d'activité indépendante. Le reste de l'article est maintenu intégralement : AJPP, AJPA, exception des agents couverts par leur retraite spéciale, demandes nécessaires aux périodes non indemnisées, dispense de cessation déclarée/radiation, trois catégories handicap et financement CAF/CNSA. Le droit n'est pas réservé aux seuls anciens bénéficiaires.",
    "Le quatrième alinéa est remplacé sur place, sans déplacer les deuxième/troisième alinéas ni le dernier renvoi aux deuxième à avant-dernier alinéas. D381-4, lu en entier, règle la demande et les justificatifs aux salariés/indépendants et les dates de congé ; ces démarches sont maintenues pour établir les périodes non connues, sans nouveau formulaire. Coordonner toute disposition réglementaire plafonnant l'affiliation à un an. La durée des congés et des allocations L168-8/L544-1 n'est pas étendue : il faut toujours une période éligible effectivement justifiée. La cotisation exclusive des organismes et le remboursement CNSA sont inchangés dans leur mécanisme mais couvrent davantage de périodes ; coût public et ressources à évaluer, sans prétendre cette extension gratuite ou une économie nationale. Ne pas la financer deux fois par les réformes d'IS ou de retraite.",
    "Le plafond d'un an sur la carrière est effectivement retiré pour les périodes futures admissibles, ce qui étend une protection retraite. Cette amélioration augmente potentiellement les cotisations prises en charge par les organismes, sans nouvelle charge privée ni taux diminué.",
    "Pas de réouverture générale des périodes anciennes ni d'extension des durées de congé/AJPA/AJPP. Le coût et le solde public net ne sont pas établis ; les règles des régimes publics distincts restent réservées.",
    xml, 'mixed',
    "Aucune nouvelle démarche ou charge privée n'est identifiée : demandes et justificatifs existants sont conservés. L'extension des périodes accroît en revanche la charge de financement obligatoire des organismes de prestations familiales et du remboursement CNSA selon le dernier alinéa ; montant non chiffré, sans compensation inventée.",
    removed=["Plafond global d'un an sur l'ensemble de la carrière des affiliations vieillesse au titre des deuxième et troisième alinéas, pour les périodes nouvelles éligibles."])
effect(o, 'relief_extended', 'assurance-vieillesse-aidants-fin-plafond-carriere',
    "Extension de l'affiliation solidaire vieillesse au-delà d'un an sur la carrière.",
    "Somme des affiliations des deuxième et troisième alinéas limitée à un an sur toute la carrière, salariés en congé et indépendants interrompant leur activité.",
    "Aucun plafond global d'un an pour les périodes courant dès la réforme ; conditions d'affiliation et durées des congés et allocations propres inchangées.", 'regime',
    "Proches aidants salariés et travailleurs non salariés ou conjoints collaborateurs éligibles aux deuxième et troisième alinéas.",
    "Périodes nouvelles même si le congé est déjà commencé ou le plafond déjà consommé ; pas de réouverture générale du passé ni de double validation.",
    "Demandes existantes maintenues ; financement CAF/CNSA accru pour les périodes supplémentaires, coût inconnu.",
    "ne peut excéder une durée totale d'un an sur l'ensemble de la carrière.",
    "n'est plus limitée à une durée totale d'un an sur l'ensemble de la carrière.")
effect(o, 'obligation_added', 'assurance-vieillesse-aidants-fin-plafond-carriere',
    "Extension corrélative du financement des cotisations solidaires aux périodes auparavant exclues.",
    "Financement exclusif des organismes familiaux et remboursement CNSA dans les limites d'affiliation, dont un an global aux deuxième et troisième alinéas.",
    "Même répartition de financement et assiettes forfaitaires, mais prise en charge des périodes nouvelles admissibles au-delà d'un an ; pas de montant calculé.", 'financing',
    "Organismes débiteurs des prestations familiales, CNAF et CNSA.",
    "Seulement périodes d'affiliation nouvelles effectivement éligibles après la réforme ; aucun financement rétroactif général.",
    "Accroissement de charge publique identifié, sans nouvelle recette présumée ; aucun paiement imposé à l'aidant.",
    "La somme des durées d'affiliation à l'assurance vieillesse du régime général de sécurité sociale au titre des deuxième et troisième alinéas du présent article ne peut excéder une durée totale d'un an sur l'ensemble de la carrière.",
    "Pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente réforme, la somme des durées d'affiliation à l'assurance vieillesse du régime général de sécurité sociale au titre des deuxième et troisième alinéas du présent article n'est plus limitée à une durée totale d'un an sur l'ensemble de la carrière.")

# Les références militaires anciennes sont conservées comme références historiques
# explicites : aucune concordance numérique extérieure au corpus n'est inventée.
xml = by_number['L381-20']['source_xml']
xml = xml.replace("de l'article L. 57 du code des pensions militaires d'invalidité et des victimes de la guerre", "de l'ancien article L. 57 du code des pensions militaires d'invalidité et des victimes de la guerre, dans sa rédaction applicable avant sa recodification, ou des dispositions qui en assurent la continuité pour la même catégorie d'orphelins")
xml = xml.replace("de l'article L. 189 du code des pensions militaires d'invalidité et des victimes de la guerre", "de l'ancien article L. 189 du code des pensions militaires d'invalidité et des victimes de la guerre, dans sa rédaction applicable avant sa recodification, ou des dispositions qui en assurent la continuité pour les aveugles de la Résistance")
xml = xml.replace("au 6° de l'article L. 136 bis du code des pensions militaires d'invalidité et des victimes de la guerre", "au 6° de l'ancien article L. 136 bis du code des pensions militaires d'invalidité et des victimes de la guerre, dans sa rédaction applicable avant sa recodification, ou par les dispositions qui en assurent la continuité pour ces mêmes victimes civiles")
xml += "<p>Les catégories mentionnées aux 4° à 6° restent ouvertes aux personnes qui en remplissent les conditions après l'entrée en vigueur de la loi portant la présente coordination. La qualification historique des références ne réserve pas le bénéfice de la présente section aux seules pensions déjà attribuées et ne modifie pas les conditions de fond des catégories concernées.</p>"
o = add('L381-20',
    "Coordination nécessaire des références militaires héritées de l'ancien code : leur caractère historique est rendu explicite sans inventer de nouveaux numéros et sans supprimer les catégories qu'elles désignent. Les sept catégories, le seuil d'incapacité, les situations de non-assurance, la condition de veuvage, le constat juridictionnel du 4° et les conditions du 7° sont intégralement préservés. Les situations futures recevables ne sont pas fermées.",
    "Incohérence préexistante signalée : la source actuelle cite encore L57, L189 et L136 bis de l'ancien code militaire, contrairement au renvoi moderne L212-1 de L371-6. Aucun texte de concordance militaire n'est fourni par les cibles ou le corpus des cinq codes ; la proposition maintient donc ces définitions historiques et leur continuité expressément, plutôt que de leur attribuer un numéro actuel incertain. Vérification extérieure nécessaire des concordances de chacune des trois catégories ; elle n'est pas déclarée achevée. D160-18, lu en entier, conserve lui aussi L57 pour la demande et les recours ; sa coordination historique devra suivre sans suppression de l'initiative possible du service des anciens combattants ni nouvelle demande pour les personnes déjà rattachées. L381-23 et R381-80, lus dans le corpus, gardent leur financement, le seuil d'incapacité d'au moins 85 % pour les catégories concernées et la règle des ascendants de plus de 65 ans, leurs exclusions et autres conditions ; aucune coupe ne les vise. Le renvoi actif L142-1 porte sur la juridiction de l'incapacité au 4°, non sur une rupture du contrat privé. La note de 2019 règle seulement la transition du contentieux (au plus tard 1er janvier 2020), pas l'entrée en vigueur de cette réforme.",
    "La qualification explicite des renvois historiques conserve l'affiliation des sept catégories sans prétendre vérifier les concordances militaires manquantes. Aucune suppression de cotisation ou de formalité n'est comptée.",
    "La concordance chiffrée des trois anciens articles militaires reste non établie dans les sources autorisées ; les définitions historiques sont conservées, sans créer de catégorie nouvelle ni fermer les futures admissions éligibles.",
    xml, 'coordination_only',
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle preuve, juridiction, durée d'assurance ou autorisation n'est exigée. La précision historique et la continuité ne modifient pas les sept conditions d'affiliation existantes.")
effect(o, 'coordination', 'invalides-guerre-renvois-historiques-affiliation',
    "Qualification historique des références militaires non recodifiées dans la source.",
    "Trois renvois à des numéros de l'ancien code militaire sans indication de leur caractère historique.",
    "Définitions historiques conservées et continuité des mêmes catégories explicitée, sans numéro actuel inventé et avec admissions futures préservées.", 'regime',
    "Orphelins de guerre majeurs, aveugles de la Résistance et victimes civiles des catégories 4° à 6°.",
    "Pensions anciennes et personnes satisfaisant à l'avenir aux conditions des mêmes catégories ; aucune extension substantielle annoncée.",
    "Aucune formalité nouvelle ; concordances numériques externes restant à vérifier explicitement.",
    "les aveugles de la Résistance, bénéficiaires de l'article L. 189 du code des pensions militaires d'invalidité et des victimes de la guerre",
    "les aveugles de la Résistance, bénéficiaires de l'ancien article L. 189 du code des pensions militaires d'invalidité et des victimes de la guerre")


contexts = {
    'L371-3': "L371-3 coordonne les IJ maladie/maternité et AT-MP pour des risques distincts ; il ne règle aucune rupture d'emploi.",
    'L371-5': "L371-5 garantit des prestations maladie provisionnelles pendant une contestation AT-MP, acquises même si l'assuré perd son procès.",
    'L371-6': "L371-6 vise soins et IJ des pensionnés de guerre ; l'interruption d'indemnisation supprimée n'est pas une rupture du contrat privé.",
    'L372-2': "L372-2 neutralise le temps sous les drapeaux lors de l'ouverture des prestations au retour, y compris pour des fonctionnaires via D712-6.",
    'L376-1': "L376-1 organise subrogation, indemnisation de la victime et information des caisses après une lésion due à un tiers.",
    'L376-2': "L376-2 donne priorité à la victime pour ses déboursés dans le recours contre le tiers ; il ne traite pas du licenciement.",
    'L376-4': "L376-4 sanctionne le défaut d'information du règlement amiable ou de la lésion, sous plafonds et recours propres.",
    'L377-2': "L377-2 est une incrimination d'intermédiation payante, abrogée par la proposition, et non une règle de contrat ou d'ancienneté.",
    'L378-1': "L378-1 conserve l'ouverture des prestations après congé de proche aidant et neutralise la période de congé ; le renvoi de congé est corrigé.",
    'L380-2': "L380-2 établit une cotisation annuelle liée aux revenus et à la résidence, supprimée pour les nouvelles années dans ce lot.",
    'L381-1': "L381-1 affilie à la vieillesse les parents bénéficiaires de prestations familiales et coordonne des validations équivalentes de périodes.",
    'L381-2': "L381-2 affilie à la vieillesse des parents et aidants ; la suppression du plafond d'un an concerne l'affiliation sur la carrière, pas l'ancienneté d'emploi.",
    'L381-20': "L381-20 délimite sept catégories de pensionnés ou ayants droit de guerre affiliables et un constat juridictionnel d'incapacité au 4°.",
}
labour = {
    'L1234-1': "La cible officielle prévoit les préavis selon l'ancienneté ; sa proposition réserve quinze jours calendaires aux nouveaux contrats et garde les anciens droits. Ce préavis individuel n'est ni un délai de soins, ni un délai de recours, ni une suppression des procédures collectives ou des autorisations spéciales. Aucun renvoi direct à L1234-1 n'existe dans cet article social.",
    'L1221-2': "La cible proposée crée le contrat unique indéterminé pour les embauches nouvelles, avec maintien des anciens contrats et sans terme automatique de mission ou de formation. Cette règle privée ne modifie pas les conditions d'affiliation, de couverture ou de prestations de l'article examiné, ouvertes aux futures situations éligibles ; elle ne s'applique pas implicitement aux agents publics.",
    'L1234-9': "La cible proposée concerne l'indemnité patronale ordinaire : zéro avant un an à la fin effective préavis inclus, puis 0,20 mois par année totale, prorata des mois complets, plafond six mois, avec transitions et indemnités spéciales préservées. Aucune de ces limites ne s'applique aux prestations ou recours de l'article examiné, qui ne renvoie pas directement à cette indemnité.",
}

specific = {
    ('L371-3','L331-3'): "Le renvoi exprès du deuxième alinéa vise l'IJ de maternité : six semaines prénatales et dix postnatales, cessation minimale de huit semaines, durées majorées pour naissances multiples et prématurité de la source entière. L371-3 conserve le non-cumul AT-MP et la dispense de carence ; le contrat unique, son seuil d'un an et son préavis ne réduisent aucun de ces droits.",
    ('L371-3','L313-1'): "Le premier alinéa exige les conditions sociales de L313-1 lors de l'accident. La proposition cible conserve rémunérations/heures du I mais retire l'affiliation minimale du II pour les prestations nouvelles, y compris les arrêts commencés avant. Le renvoi général ne peut réintroduire ce délai ; ni le seuil d'ancienneté d'emploi ni la notification de rupture ne s'y substituent.",
    ('L371-3','L323-4'): "L323-4 fixe l'IJ comme fraction du revenu d'activité antérieur plafonné, calculée d'après les dernières payes ; sa note distingue les arrêts de juillet 2020 et certains arrêts antérieurs. L371-3 ne change pas ce calcul : il règle non-cumul et carence. Ce salaire de référence n'est pas celui de l'indemnité ordinaire plafonnée à six mois.",
    ('L371-5','L313-1'): "La condition expresse de L313-1 est contributive, appréciée pour le versement provisionnel. La proposition cible supprime l'affiliation minimale supplémentaire du II et garde les heures, rémunérations et assimilations ; le maintien de L371-5 reçoit cette amélioration sans exiger un justificatif de durée supprimée. Un procès perdu ne remet pas en cause les prestations acquises, anciens comme futurs contrats.",
    ('L371-6','L323-4'): "Le troisième alinéa renvoie au montant journalier calculé sur les dernières rémunérations plafonnées par L323-4. La proposition retire seulement l'espacement minimal entre périodes et ne modifie ni fraction, ni plafond, ni valeur journalière. Les périodes d'IJ ne deviennent ni un préavis de quinze jours ni une indemnité de licenciement.",
    ('L371-6','L321-1'): "Le deuxième alinéa vise les IJ de maladie de L321-1 : incapacité physique constatée par un professionnel compétent, conditions des arrêts et exception des cures thermales justifiées. Le retrait de l'interruption minimale ne dispense pas du constat médical ni ne ferme ces dérogations. La note de 2025 concerne l'entrée en vigueur de ce droit officiel, non la réforme proposée.",
    ('L372-2','L313-1'): "Au retour sous les drapeaux, la neutralisation de L372-2 porte sur les périodes de référence des conditions contributives de L313-1. La cible proposée ne conserve plus de durée d'affiliation autonome au II pour les nouvelles périodes ; la neutralisation ne la rétablit pas. L341-2 invalidité garde ses conditions propres ; le service public ne devient pas un contrat privé unique.",
    ('L376-2','L376-1'): "Le renvoi exprès vise l'action en indemnisation de la victime et la subrogation limitée aux postes pris en charge. La vue fournie est la source officielle, non la proposition de ce lot : celle-ci conserve ces règles et la préférence de la victime, tout en supprimant les frais forfaitaires nouveaux. L376-2 reste cohérent et ne supprime pas une seconde fois le même accessoire financier.",
    ('L376-4','L376-1'): "Le troisième alinéa vise précisément le septième alinéa de L376-1 : information sur les lésions causées par un tiers. La vue fournie est officielle ; dans la proposition de ce lot cet alinéa garde sa place mais dispense de répétition quand la caisse est complètement informée. La sanction est coordonnée pour ne pas punir cette dispense ; plafonds, principal subrogatoire et information du règlement demeurent.",
    ('L377-2','L623-1'): "La note de L377-2 qualifie historiquement L623-1 de règle de vieillesse, alors que la cible officielle entière régit maternité, paternité, adoption, deuil et élus locaux des indépendants. Aucun renvoi à l'intermédiation pénale n'y figure. Son repos minimal, ses allocations et IJ, ses revalorisations et la réserve QPC de 2025 sur la reconnaissance conjointe ne sont affectés ni par cette abrogation ni par le contrat privé unique.",
    ('L378-1','L313-1'): "Le renvoi direct vise les conditions de rémunération ou de travail et les périodes de référence des prestations au retour du congé ; la période aidant est neutralisée. La cible proposée retire l'affiliation minimale supplémentaire du II et préserve les assimilations : L378-1 ne recrée ni cette durée ni le seuil d'un an de rupture et conserve les congés anciens et futurs éligibles.",
    ('L380-2','1417'): "L380-2 reprend uniquement les modalités de définition des revenus au IV de CGI1417 ; les seuils d'exonération foncière des I et II, indexations et parts ne sont pas des seuils de cotisation maladie. Le IV et ses réintégrations restent utiles au stock ancien ; l'abrogation ne supprime aucune exonération foncière ni ne transforme l'abattement maladie en abattement d'IR.",
    ('L380-2','L213-1'): "Le dernier alinéa de L380-2 vise les Urssaf destinataires de données fiscales pour cette cotisation. L213-1 proposé conserve leurs autres missions, borne déjà la C3S et le CPF-CDD à leur champ et reprend la réutilisation de données. Aucune mission générale de recouvrement ne peut fonder une cotisation L380-2 pour une année supprimée ; les données restent utilisables pour les anciennes années et finalités légales autonomes.",
    ('L380-3-1','1417'): "Le deuxième alinéa du IV reprend seulement la définition des revenus du IV de CGI1417 pour la cotisation propre aux frontaliers ; il ne renvoie pas aux limites de revenus foncières des I/II. Cette base de cotisation demeure distincte de la cotisation subsidiaire supprimée et de la fiscalité personnelle des dividendes. L'abattement réglementaire 0,25 PASS et les exclusions du IV ne sont ni retirés ni remplacés par un taux fiscal de 20 %.",
    ('L381-1','L351-5'): "Le dernier alinéa interdit une affiliation pour le même enfant et la même période déjà validée par majoration de congé parental. La cible proposée remplace l'ancien L122-28-1 par L1225-47 1° et L1225-48 et conserve l'ancien droit ; elle garde le choix plus favorable par rapport à L351-4. La coordination reste opérante pour les futurs contrats uniques sans réduire la durée du congé ou supprimer la majoration.",
    ('L381-1','L142-1'): "L381-1 ne renvoie pas directement à L142-1 ; les litiges d'affiliation et de retraite restent néanmoins dans le 1° du contentieux social. La proposition cible conserve ce champ et les autres compétences. Les renvois de son 3° au code du travail ne transforment pas la validation parentale en indemnité de rupture et ne créent ici ni condition de notification ni ancienneté d'un an.",
    ('L381-1','L168-8'): "L381-1 vise complément familial, allocation de base et prestation partagée d'éducation, non l'AJPA de L168-8. La cible distingue les salariés, personnes L544-8 et agents publics éligibles au congé aidant avec conditions de séjour/résidence. Cette allocation reste dans son champ propre de L381-2 ; elle ne doit ni remplacer les prestations de L381-1 ni limiter leur affiliation aux anciens contrats.",
    ('L381-2','L168-8'): "Le deuxième alinéa de L381-2 vise l'AJPA et, séparément, les périodes de congé aidant sans AJPA sur demande. L168-8 ouvre l'allocation aux bénéficiaires du congé, à certaines personnes L544-8 et aux agents publics sous conditions de séjour/résidence. Retirer le plafond d'affiliation vieillesse n'étend pas la durée de l'allocation et ne supprime pas l'exception des agents couverts par leur régime spécial.",
    ('L381-2','L544-1'): "Le premier alinéa rattache l'affiliation vieillesse au bénéfice de l'AJPP de L544-1, pour un enfant gravement malade, handicapé ou accidenté dont l'état exige présence soutenue et soins contraignants. Le droit vise également les agents publics selon leurs règles ; L381-2 réserve ceux dont le congé est validé dans le régime spécial. La suppression du plafond des seuls deuxième/troisième alinéas ne modifie pas l'AJPP ni la durée de ce premier alinéa.",
    ('L381-20','L142-1'): "Le 4° renvoie expressément à la juridiction compétente pour l'incapacité à travailler de l'orphelin de guerre majeur. L142-1, notamment ses compétences sociales et d'invalidité/inaptitude, reste ce cadre contentieux dans la source et dans la proposition fournie. Le passage au contrat privé unique ne supprime ni ce constat juridictionnel ni les droits des pensionnés militaires et ne leur impose aucune ancienneté d'emploi.",
}

for obj in answer:
    key = obj['code_id'] + '|' + obj['source_id']
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        number = t['number']
        if number in labour:
            assessment = contexts[obj['number']] + ' ' + labour[number]
        else:
            assessment = specific[(obj['number'], number)]
        obj['reference_checks'].append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))

assert len(answer) == len(sources) == 24
assert [o['source_id'] for o in answer] == [a['source_id'] for a in sources]
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles')
