import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []

def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))

def impact(classification, assessment, limitations, burdens, effects):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens, effects=effects)

def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

for source in sources:
    previous = source['previous_draft']
    answers.append({**{k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
                    'proposed_xml': previous['proposed_xml'], 'reason': previous['reason'],
                    'review_notes': previous['review_notes'], 'status': 'rewrite_draft'})

# L5132-6-1 : conserver une transition opératoire et le bénéfice de l'aide ciblée.
a = answers[0]
a['proposed_xml'] = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée.</p><p>Les personnes âgées d'au moins cinquante-sept ans rencontrant des difficultés sociales et professionnelles particulières restent éligibles à l'emploi à durée indéterminée prévu à l'article L. 5132-6, dans les conditions de l'article L. 1251-58-1. L'abrogation de la dérogation spéciale ne retire ni les aides financières attachées à leur emploi en contrat à durée indéterminée d'inclusion, ni les exonérations ou mesures d'accompagnement dont elles remplissent les autres conditions d'attribution. Ces avantages restent ouverts aux situations futures éligibles ; ils ne sont pas réservés aux contrats antérieurs.</p><p>Le plafond de trente-six mois ne s'applique pas aux missions convenues à compter de cette entrée en vigueur. Aucune condition d'âge ou de durée préalable du parcours fondée sur le présent article ne subordonne la conclusion d'un contrat unique. Les durées d'affectation conventionnelles applicables auprès de l'entreprise utilisatrice restent régies par leurs dispositions propres, sans fixer le terme de l'emploi.</p><p>Les contrats et missions valablement convenus avant cette date et les rémunérations, ancienneté, congés, aides et recours qui en résultent restent soumis aux règles qui leur étaient applicables. L'abrogation ne prolonge pas automatiquement une mission antérieure et n'éteint pas le contrat à durée indéterminée à la fin de cette mission. Une conversion convenue conserve toute l'ancienneté et les créances acquises, sans double compte. Les missions futures ne donnent lieu ni à un nouveau CDD ni à un nouvel essai du seul fait de leur succession. Les garanties de rémunération et de prise en compte des intermissions de l'emploi à durée indéterminée demeurent applicables.</p>"""
a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
         repeal_scope="Abrogation prospective du régime dérogatoire de conclusion du CDI d'inclusion et de son plafond spécial de trente-six mois par mission ; maintien autonome des aides ciblées et des situations antérieures.")
a['reason'] = "Réforme de fond conservée après seconde lecture : la généralisation du contrat unique rend inutile une permission de CDI réservée aux personnes d'au moins cinquante-sept ans. Le plafond spécial de trente-six mois est effectivement retiré pour les missions nouvelles. La rédaction précise davantage que la disparition du support législatif ne ferme pas les aides du CDI d'inclusion aux futurs bénéficiaires éligibles. Aucune coupe supplémentaire des garanties salariales ou des aides n'est justifiée : elles protègent l'insertion et le revenu, sans créer un second contrat. L'abrogation suppose l'entrée en vigueur simultanée du nouveau L5132-6 ; la permission source n'était pas un agrément administratif et sa suppression n'est pas comptée comme un agrément retiré."
a['review_notes'] = "L5132-6 et L1251-58-1 sont fournis comme propositions, non comme droit positif. L1251-58-4 et L1251-58-5 ont aussi été lus dans le corpus : les exceptions et substitutions propres au CDI intérimaire restent distinctes. Compagnons lus, non réécrits dans ce lot : R5132-10-13-1 ouvre une aide dans la limite des postes conventionnés ; D5132-10-15 vise un délai préalable de douze mois et un examen de parcours ; D5132-10-16 prévoit la déclaration de l'embauche et de la rupture par téléservice. Coordonner précisément leurs renvois à l'article abrogé : ne pas laisser le délai préalable interdire le nouvel emploi indéterminé ; ne pas retirer l'aide ciblée ni la remplacer par une nouvelle attestation. La nécessité et le réemploi des données du téléservice sont à traiter dans son propre article, sans prétendre que cette seule abrogation supprime toute déclaration légale d'embauche. Les conditions autonomes d'attribution de l'aide ne sont pas abolies. Aucun résultat financier chiffré n'est établi."
a['benefit_review'] = "L'avantage source est l'accès au CDI d'inclusion, dérogatoire à L5132-6 pour les personnes d'au moins cinquante-sept ans en difficulté ; il devient accessible sous la règle générale du contrat unique sans exclure ce public. L'aide financière de R5132-10-13-1, l'accompagnement, les exonérations applicables, la rémunération garantie et les droits d'intermission restent expressément préservés, y compris pour les futurs cas éligibles et dans la limite des postes conventionnés pour l'aide. Le plafond de trente-six mois est une limite, non un avantage ; il est retiré pour les missions nouvelles sans prolongation forcée des missions anciennes. Les renvois réglementaires à l'article abrogé restent à coordonner, sans extinction implicite de l'aide."
a['proposed_xml'] = a['proposed_xml'].replace(
    "Ces avantages restent ouverts aux situations futures éligibles ; ils ne sont pas réservés aux contrats antérieurs.",
    "Ces avantages restent ouverts aux situations futures éligibles ; ils ne sont pas réservés aux contrats antérieurs. L'absence de contrat à durée déterminée antérieur ne peut, à elle seule, faire obstacle à leur attribution.")
a['benefit_review'] += " La condition de support en ancien CDD ne peut donc empêcher l'aide des futurs contrats uniques, sans extension automatique des crédits ou postes conventionnés."
a['substantive_impact'] = impact('material_reduction',
    "La source officielle entière impose un plafond spécial de trente-six mois aux missions de ce CDI d'inclusion. La proposition le retire pour les missions nouvelles et remplace la dérogation de CDI par la règle commune. Elle conserve une coupe déjà présente au brouillon ; elle n'en revendique pas une seconde au titre de la nouvelle rédaction des aides.",
    "Pas de suppression des durées d'affectation conventionnelles ni des conditions autonomes d'aide. Les compagnons réglementaires et le nouveau L5132-6 doivent entrer en cohérence ; aucune baisse nationale de coût n'est chiffrée.",
    "Aucune charge nouvelle propre à cet article n'est identifiée : pas de déclaration, justificatif ou agrément de remplacement. Les garanties existantes du CDI restent dues et les conditions d'aide extérieures conservent leur champ.", [
    effect('obligation_removed','missions-inclusion-sans-plafond-special',
        'Suppression du plafond légal spécial de durée de mission du CDI inclusion.',
        "Mission du dispositif des personnes d'au moins cinquante-sept ans limitée à trente-six mois au total.",
        "Aucun plafond de trente-six mois pour les missions convenues après la réforme ; les limites conventionnelles d'affectation restent distinctes.",
        'legal_duty', "Entreprises de travail temporaire d'insertion et salariés du dispositif de L5132-6-1.",
        "Missions convenues à compter de l'entrée en vigueur ; les missions antérieures ne sont pas prolongées automatiquement.",
        "Aucun contrôle ou document substitutif ; l'emploi et ses garanties ne cessent pas avec la mission.",
        "Dans ce cadre, la durée totale d'une mission ne peut excéder trente-six mois.",
        "Le plafond de trente-six mois ne s'applique pas aux missions convenues à compter de cette entrée en vigueur."),
    effect('coordination','contrat-unique-duree-indeterminee',
        "Suppression du support dérogatoire de CDI, en coordination avec sa généralisation.",
        "Faculté spéciale de CDI réservée dans cet article aux personnes d'au moins cinquante-sept ans en difficulté.",
        "Accès au contrat unique de L5132-6 sans condition d'âge propre à cette permission ; aides ciblées préservées.",
        'regime', "Public du CDI d'inclusion et autres recrutements éligibles de L5132-6.",
        "Entrée en vigueur simultanée du contrat unique ; droits et créances anciens conservés.",
        "Règle commune d'emploi indéterminé ; aucune autorisation administrative équivalente.",
        "Par dérogation aux dispositions de l'article L. 5132-6, les entreprises de travail temporaire d'insertion peuvent conclure des contrats à durée indéterminée",
        "Aucune condition d'âge ou de durée préalable du parcours fondée sur le présent article ne subordonne la conclusion d'un contrat unique.")])

# L5132-11 : droits salariaux et rectification de concordance, sans nouvelle coupe.
a=answers[1]
a['reason'] = "Seconde passe sans coupe supplémentaire justifiée : l'égalité salariale, les jours fériés sous condition de bénéfice chez l'utilisateur et la possibilité de rémunération horaire ou forfaitaire ont une fonction de protection ou de souplesse identifiable. Le brouillon est conservé pour corriger le renvoi L2212-1 devenu inexact, conformément à la note officielle qui le transfère à L2211-1, et coordonner le volume contractuel garanti. La distinction des activités relevant de L5132-9 demeure. Aucune réduction de prélèvement ou de formalité n'est attribuée à cette reformulation."
a['review_notes'] = "L5132-9, L2211-1 et L2212-1 lus dans le corpus : L2212-1 actuel traite des formations communes au dialogue social ; la substitution est justifiée par la note source de la loi du 21 janvier 2008, article 3-2°. L'expression après période d'essai qualifie le salarié de comparaison et ne retarde pas l'égalité salariale. Le deuxième alinéa conserve le forfait uniquement hors des activités de L5132-9 ; il ne transforme pas le temps garanti en heures effectivement exécutées. Les restrictions de mise à disposition de L5132-9 ne sont pas abrogées ici. L3123-6 lu impose déjà une durée contractuelle : aucune nouvelle pièce ou plancher général n'est ajouté. La correction du renvoi empêche le maintien intégral avec proposition nulle."
a['substantive_impact']=impact('coordination_only',
    "Comparée à la source entière, la proposition conserve les trois règles de rémunération et rectifie un renvoi matériellement périmé. Elle ne réduit ni le salaire dû ni une taxe et n'allège aucune formalité démontrée.",
    "Le plafond et les autorisations de mise à disposition de L5132-9 ne relèvent pas de cette correction. Aucun effet net sur les charges de l'ensemble des associations ou codes n'est établi.",
    "Aucune charge nouvelle n'est identifiée : le volume garanti explicite la durée déjà stipulée au contrat à temps partiel ; aucun registre, justificatif ou nouveau délai n'est créé.",[
    effect('coordination','associations-intermediaires-jours-feries',
        "Rétablissement de la concordance du champ des employeurs pour les jours fériés.",
        "Renvoi à L2212-1 malgré la note officielle de transfert à L2211-1 ; bénéfice conditionné aux jours fériés payés chez l'utilisateur.",
        "Renvoi exprès à L2211-1 et maintien de la même condition de paiement chez l'utilisateur.",
        'legal_duty', "Salariés des associations intermédiaires mis à disposition des employeurs du champ de L2211-1.",
        "Rectification de concordance sans extinction des créances salariales anciennes.",
        "Aucune démarche ni donnée nouvelle pour obtenir le paiement.",
        "des employeurs mentionnés à l'article L. 2212-1 (1)",
        "d'un employeur mentionné à l'article L. 2211-1")])

# L5134-29 : la dispense de préavis est nécessaire, pas une nouvelle réduction.
a=answers[2]
a['reason'] = "Coordination conservée après examen des charges : le 2° vise désormais le contrat unique, avec transition des offres et contrats anciens déjà conclus ; la dispense de préavis reste ouverte pour les futurs cas éligibles. Ni les six mois anciens propres à une offre de CDD ni le terme d'une aide ne deviennent une durée d'emploi. Aucune coupe supplémentaire de l'accord du 1° n'est retenue : il organise l'absence et la mise en situation avec l'employeur qui reste lié au salarié ; le 2° reste, comme dans la source, exempt de cet accord. La sortie sans préavis est un avantage conservé et non une nouvelle réduction de quinze jours."
a['review_notes'] = "L5134-24, L5134-25 et L5134-28 ont été lus dans le corpus : emploi de droit privé, aide et accompagnement à durée propre, mobilité distincte. Le nouveau 2° ne permet aucun CDD spécial. Les contrats d'offre déjà conclus avant la réforme conservent les droits de suspension et de sortie même si les effets sont ultérieurs ; un simple projet de CDD non conclu ne bénéficie pas de cette réserve. La rupture sans préavis est une dispense spéciale à l'initiative de mobilité du salarié ; elle ne fonde pas un licenciement sans procédure. Les régimes de formation, d'aide et d'indemnité spéciale ne sont pas modifiés. Aucun nouveau renvoi normatif n'est ajouté."
a['substantive_impact']=impact('coordination_only',
    "Le remplacement de la référence future aux CDD par le contrat unique coordonne une mesure commune. La suspension, ses deux voies et la dispense de préavis existaient dans toute la source : elles sont maintenues sans être comptées comme coupes nouvelles.",
    "L'emploi aidé exige la coordination propre de L5134-24 à L5134-28 ; l'article ne réduit pas les durées ou les conditions de l'aide et ne change pas le régime des agents publics.",
    "Aucune charge administrative nouvelle n'est identifiée : ni déclaration ni agrément substitutif. La continuité de l'emploi relève du contrat unique, dont la durée se distingue de l'accompagnement.",[
    effect('coordination','contrat-unique-duree-indeterminee',
        "Coordination de la suspension pour accomplir un essai et de la sortie favorable avec le contrat unique.",
        "Essai d'un CDI ou d'un CDD d'au moins six mois ; sortie sans préavis après embauche.",
        "Essai du contrat unique pour les offres nouvelles ; anciens contrats déjà conclus protégés, sortie sans préavis conservée.",
        'regime', "Salariés en contrat d'accompagnement dans l'emploi effectuant une mobilité éligible.",
        "Réforme prospective ; les droits afférents aux contrats d'offre conclus avant elle restent ouverts.",
        "Pas d'accord patronal ajouté au 2° ; aucun justificatif de remplacement.",
        "une embauche en contrat de travail à durée indéterminée ou à durée déterminée au moins égale à six mois.",
        "D'accomplir la période d'essai afférente à une offre d'emploi en contrat unique à durée indéterminée.")])

# L5134-57 : le champ résiduel fermé en 2007 ne doit pas être artificiellement rouvert.
a=answers[3]
a['reason'] = "Le brouillon est conservé pour rendre opératoire la réserve historique de la note officielle et protéger les départs futurs des contrats encore éligibles. La dispense de préavis pour alternance ou formation ne présente aucune charge à supprimer pour le bénéficiaire. Une coupe supplémentaire de ce droit serait contraire à l'orientation de conservation des avantages. La fermeture des nouveaux contrats jeunes provient de la loi de 2007, pas de cette réforme ; les autres aides et futurs apprentissages restent distincts."
a['review_notes'] = "Incohérence documentaire préexistante : source_state indique VIGUEUR mais la note cite l'article 127 III de la loi du 24 décembre 2007 qui abroge ce groupe d'articles sous réserve des contrats ayant ouvert droit au soutien antérieurement. La proposition explicite ce champ sans inventer une réouverture ni une date de réforme passée. L5134-54 lu n'efface pas cette réserve. Le renvoi à l'ancien L322-4-6 est historique et n'est pas assimilé à un article actuel. La dispense prime le préavis individuel de quinze jours pour les ruptures résiduelles éligibles ; les nouveaux dispositifs d'alternance ne recréent pas un CDD."
a['benefit_review'] = "L'avantage est la dispense totale de préavis à l'initiative du salarié pour accéder à un apprentissage, une professionnalisation ou une action de formation continue de L6313-1. Il est conservé pour toutes les ruptures futures encore recevables dans le champ résiduel légal de 2007, y compris vers une phase d'alternance du nouveau contrat unique. La réforme ne ferme aucun droit encore ouvert et n'oppose pas les quinze jours à la dispense. Elle ne rouvre pas le soutien de l'État déjà fermé par le législateur en 2007 ; cette limite préexistante n'est pas une suppression actuelle d'aide."
a['substantive_impact']=impact('coordination_only',
    "Le texte conserve intégralement les motifs favorables de départ sans préavis et explicite la réserve de la note source. Il adapte leur destination au contrat unique sans compter la dispense préexistante comme une nouvelle baisse de délai.",
    "Seuls les contrats ayant ouvert droit au soutien dans le champ historique de 2007 sont concernés. Aucun effectif résiduel ni coût n'est connu ; aucune aide contemporaine n'est rouverte.",
    "Aucune charge nouvelle n'est identifiée : aucun certificat de formation supplémentaire, nouveau délai ou formalité d'autorisation n'est institué pour exercer la dispense.",[
    effect('coordination','contrat-unique-duree-indeterminee',
        "Maintien de la dispense résiduelle pour une destination d'alternance exercée dans le contrat unique.",
        "Rupture sans préavis pour embauche en apprentissage ou professionnalisation, sous le champ résiduel de la note officielle.",
        "Même dispense pour la destination future en phase d'apprentissage ou de professionnalisation d'un contrat unique ; pas de nouveau contrat jeune.",
        'regime', "Salariés titulaires d'un ancien contrat jeune encore couvert par la réserve de 2007.",
        "Toute rupture future éligible ; la loi de 2007 continue de déterminer les contrats sources recevables.",
        "Aucun remplacement de la dispense par un préavis de quinze jours.",
        "D'être embauché dans le cadre d'un contrat d'apprentissage ou d'un contrat de professionnalisation",
        "à une phase d'apprentissage ou de professionnalisation exécutée dans ce contrat unique.")])

# L5213-3-1 : la fusion documentaire ne doit pas éliminer le consentement.
a=answers[4]
a['reason'] = "La coupe du brouillon est conservée : lorsque la rééducation est assurée chez l'employeur, la convention tripartite signée détermine déjà son exécution et tient lieu d'avenant ; le second acte portant sur les mêmes modalités est retiré. La rémunération, les indemnités journalières et la déduction intégrale de la mise à disposition sur l'essai restent à droit constant. Pas de coupe supplémentaire de l'accord tripartite ou des avis médicaux : ils garantissent le consentement, la compatibilité avec l'arrêt et le versement de la prestation. La convention avec une entreprise d'accueil reste distincte et n'est pas supprimée sans coordination de L8241-2."
a['review_notes'] = "Conservation des I à IV et des deux alinéas internes de II et III. CSS L323-3-1 fourni en source seule impose l'accord du médecin traitant, l'avis du médecin-conseil et l'accord de caisse ; ils subsistent. L8241-2 lu maintient le consentement au prêt, l'accord interentreprises, les mentions de poste, le retour dans l'entreprise et les consultations ; la suppression du second acte porte seulement sur la rééducation chez l'employeur. R5213-15 lu conserve le montant total au moins égal à la rémunération avant arrêt, la durée maximale de dix-huit mois et l'information par la caisse ; R5213-16 dispense déjà d'avis préalable de la commission du handicap. Coordonner le décret sans rétablir l'avenant séparé. La déduction de l'essai est intégrale seulement pour l'entreprise de rééducation et un emploi similaire. Le renvoi rural L752-5-2 n'est pas fourni et sa concordance demeure à vérifier hors du présent corpus ; aucune modification n'en est inférée. La date du 1er juillet 2022 est historique."
a['substantive_impact']=impact('material_reduction',
    "La source entière cumule convention tripartite et avenant pour une rééducation chez le même employeur. La proposition retire le second instrument pour les mêmes modalités ; cette suppression déjà acquise au brouillon est une fusion documentaire réelle, sans suppression de l'accord du salarié.",
    "Le prêt de main-d'œuvre chez un tiers garde les actes de L8241-2. Les contrôles médicaux et la prestation journalière ne sont pas supprimés. Aucun coût en euros ni solde global de conformité n'est mesuré.",
    "Aucune charge nouvelle n'est identifiée : la convention et ses signatures existent déjà au I ; elle reçoit l'effet d'avenant sans nouveau modèle, dépôt ou accord médical supplémentaire.",[
    effect('obligation_merged','reeducation-convention-valant-avenant',
        "Fusion de l'avenant d'exécution avec la convention de rééducation déjà conclue.",
        "Convention entre employeur, salarié et caisse au I, plus avenant au contrat lorsque l'employeur assure la rééducation au II.",
        "La convention signée vaut avenant pour les mêmes modalités ; aucun second acte exigé et rémunération contractuelle préservée.",
        'legal_duty', "Employeurs et salariés concluant une rééducation assurée chez le même employeur, avec leur caisse.",
        "Conventions conclues après l'entrée en vigueur de la modification ; conventions et avenants anciens valables sans réfection.",
        "Aucun document équivalent substitutif, consentement tripartite et contrôles médicaux inchangés.",
        "elle fait l'objet d'un avenant au contrat de travail, qui ne peut modifier la rémunération prévue par celui-ci.",
        "Aucun avenant distinct portant sur les mêmes modalités n'est exigé.")])

# L5213-13-3 : pas de renvoi prospectif vers une carence abrogée.
a=answers[5]
a['proposed_xml']=a['proposed_xml'].replace("Par dérogation à l'article L. 1251-36, aucun délai de carence n'est applicable :", "Aucun délai de carence n'est applicable :")
a['reason'] = "Conservation de la réforme du brouillon : les contrats nouveaux sont indéterminés, sans plafond légal de mission, sans demande de dérogation au plancher général supprimé et sans seuil de deux mois pour la dispense de carence. Correction supplémentaire du renvoi prospectif à L1251-36 dont la proposition fournie prévoit l'abrogation ; ses effets anciens subsistent dans la transition, sans renvoi opératoire orphelin pour l'avenir. Le volume garanti, les minima conventionnels, l'accompagnement renforcé et les aides sont nécessaires au public handicapé. Leur suppression ne constitue pas une simplification recevable. La garantie mensuelle et les intermissions deviennent obligatoires pour tous les nouveaux emplois, alors que la source permettait encore des contrats de mission : cette charge est explicitement recensée."
a['review_notes'] = "L1251-12 et L1251-12-1 délimitent les anciennes durées de contrats de mission ; le CDI est déjà dispensé du plafond légal par L1251-58-6. La proposition ne retire donc pas une seconde fois un plafond de vingt-quatre mois à un CDI existant. Les durées conventionnelles d'affectation de L1251-12 et l'interdiction de pourvoir durablement un poste permanent par une mission gardent leur champ ; elles ne deviennent pas un terme d'emploi. L1251-58-2 et L1251-58-3 maintiennent ancienneté, congés d'intermission et rémunération mensuelle : aucune réduction proportionnelle de cette garantie n'est déduite du volume horaire adapté. L1251-36 proposé abroge déjà la carence, et L1251-58-4 lu l'exclut déjà pour le CDI ; le présent article ne compte pas autant de délais retirés que de renvois. L3123-27 et L3123-19 lus distinguent plancher légal supprimé et minima conventionnels maintenus. L5213-13-1 et L5213-19 lus maintiennent public reconnu handicapé, conditions d'aide et crédits annuels. Le 1er janvier 2024 demeure historique. Le renvoi L1251-58-6 fourni nécessite lui-même une concordance avec l'abrogation proposée de L1251-12-1, sans rétablir sa limite."
a['benefit_review'] = "La source ouvre des dérogations favorables : mission jusqu'à vingt-quatre mois au lieu du plafond ordinaire, durée hebdomadaire inférieure au minimum si la situation le justifie, possibilité de CDI intérimaire et deux dispenses de carence. Pour les emplois futurs, le CDI devient la règle et conserve sa dispense de plafond légal, sa rémunération mensuelle et les intermissions ; le plancher général de vingt-quatre heures et sa justification disparaissent sans enlever les minima conventionnels favorables ou leurs dérogations. Les deux dispenses de carence subsistent, sans exiger deux mois d'embauche en contrat unique. Les anciens contrats gardent leurs dérogations, primes et recours, sans nouveau renouvellement de CDD. L'accompagnement renforcé, les aides et exonérations du public éligible restent ouverts aux futurs recrutements selon leurs conditions et crédits propres."
a['substantive_impact']=impact('mixed',
    "L'article coordonne le contrat unique, la fin du plancher légal et la suppression générale de carence ; ces renvois ne sont pas des réductions indépendantes supplémentaires. Par rapport à toute la source, la voie future du contrat de mission disparaît et les garanties du CDI intérimaire deviennent obligatoires pour tous les nouveaux recrutements. Le solde net de coût n'est pas établi.",
    "Les avantages de durée et de carence étaient déjà attachés au CDI intérimaire optionnel. Les conditions d'aide, les durées d'affectation conventionnelles et les anciens contrats ne sont pas supprimés. Aucun gain financier universel n'est démontré.",
    "Charge substantielle identifiée : généraliser le CDI étend aux nouveaux salariés qui auraient relevé d'un contrat de mission la garantie mensuelle et les droits des intermissions. Aucun nouveau registre, agrément, justificatif de dérogation ou déclaration de remplacement n'est ajouté.",[
    effect('coordination','contrat-unique-duree-indeterminee',
        "Mise en cohérence de l'emploi adapté temporaire avec l'interdiction des nouveaux contrats à terme.",
        "Contrats de mission pouvant atteindre vingt-quatre mois renouvellement compris, avec option de CDI intérimaire.",
        "Contrat unique obligatoire pour les nouveaux emplois ; missions distinctes de l'emploi, sans plafond légal de durée selon le régime CDI.",
        'regime', "Entreprises adaptées de travail temporaire et travailleurs de L5213-13-1 recrutés après la réforme.",
        "Contrats anciens et droits préservés, aucun nouveau CDD ni renouvellement après la réforme ; conversion avec ancienneté conservée.",
        "Les règles du CDI s'imposent désormais, y compris garanties entre missions décrites séparément ; pas de contrat distinct par mission.",
        "Les entreprises adaptées de travail temporaire concluent des contrats de mission",
        "les entreprises adaptées de travail temporaire concluent ce contrat avec les travailleurs mentionnés à l'article L. 5213-13-1"),
    effect('coordination','temps-partiel-sans-plancher-general',
        "Maintien de la souplesse horaire sans justification d'une dérogation au plancher légal supprimé.",
        "Dérogation à la durée minimale de L3123-27 lorsque la situation du salarié le justifie.",
        "Absence du plancher légal général de vingt-quatre heures ; volume contractuel garanti et minima conventionnels plus favorables conservés.",
        'legal_duty', "Nouveaux emplois des entreprises adaptées de travail temporaire.",
        "Anciennes dérogations maintenues pour les contrats antérieurs ; règles conventionnelles distinctes.",
        "Pas de demande ou justificatif de remplacement pour écarter le minimum légal général.",
        "par dérogation à l'article L. 3123-27, lorsque la situation du salarié le justifie.",
        "Aucun plancher légal général de vingt-quatre heures par semaine ne s'applique ; il n'est plus nécessaire de justifier une dérogation à ce plancher."),
    effect('coordination','suppression-carence-interim',
        "Maintien des dispenses sans renvoi prospectif au texte de carence abrogé.",
        "Dispense entre contrats de mission du même salarié pendant le parcours et pour embauche à l'issue en CDD d'au moins deux mois.",
        "Absence de carence entre missions du même parcours et vers l'embauche en contrat unique, sans durée minimale ; pas de réduction distincte du régime général.",
        'legal_duty', "Salariés accompagnés et entreprises utilisatrices qui les recrutent.",
        "Dispenses des anciens contrats préservées, aucune embauche nouvelle en CDD autorisée.",
        "Aucune procédure nouvelle ni délai substitutif.",
        "En cas d'embauche du salarié par l'entreprise utilisatrice, à l'issue de son contrat de mission, en contrat à durée déterminée d'une durée d'au moins deux mois.",
        "En cas d'embauche du salarié par l'entreprise utilisatrice à l'issue d'une mission en contrat unique à durée indéterminée, sans durée minimale d'emploi exigée au titre de cette dispense."),
    effect('obligation_added','contrat-unique-garanties-intermissions',
        "Extension obligatoire du financement des garanties du CDI intérimaire aux nouveaux emplois de ce dispositif.",
        "Le CDI intérimaire et sa garantie mensuelle sont une option ; le contrat de mission reste possible.",
        "La garantie mensuelle de L1251-58-3 et les droits d'intermission de L1251-58-2 accompagnent tous les nouveaux contrats uniques.",
        'legal_duty', "Entreprises adaptées de travail temporaire employant les nouveaux salariés entre deux missions.",
        "Contrats uniques nouveaux ; les garanties des CDI déjà existants ne sont pas une obligation nouvellement créée.",
        "Coût potentiel de rémunération et droits entre missions ; aucune estimation monétaire ou neutralité nette affirmée.",
        "Elles peuvent également conclure les contrats de travail à durée indéterminée intérimaires mentionnés à l'article L. 1251-58-1.",
        "La rémunération mensuelle minimale de l'article L. 1251-58-3 demeure garantie.")])

# L5422-12 : garder les minorations et supprimer les seules majorations.
a=answers[6]
a['reason'] = "La suppression des majorations patronales, déjà acquise au brouillon, est conservée après comparaison intégrale avec la source ; le pouvoir de minorer et toutes les exclusions du 1° restent ouverts aux futurs cas éligibles. Pas de coupe supplémentaire de la règle d'équilibre ou des données strictement nécessaires au calcul des minorations : la première finance l'allocation, les secondes permettent le bénéfice et la contestation du bonus. La fin d'une mission sans fin d'emploi ne devient pas une rupture salariale. La réforme supprime une faculté de malus, non la cotisation chômage entière ; son montant dépend des règles d'application non chiffrées ici."
a['review_notes'] = "Conservation des cinq critères et de toutes les exclusions du 1° : démissions, inaptitude L1226-2-1, fautes grave ou lourde, contrats de travail et de mise à disposition des structures L5132-4, contrats de mission du 2° de L1251-1 ; l'inscription sur la liste L5411-1 demeure cumulative. L1251-1 fourni distingue contrat commercial de mise à disposition, lettre de mission future et anciens contrats de mission : la fin de l'emploi ne se déduit pas d'une fin d'affectation ; les fins de mise à disposition restent à leur champ distinct pour calculer une minoration. L5422-20 lu appelle une coordination des accords agréés et du règlement pour ne pas maintenir le malus des périodes nouvelles ni neutraliser la coupe par le taux non modulé. Les données autorisées restent nécessaires, non publiques et sans nouveau fichier. Le financement perdu et les effets sur les allocations ne sont pas chiffrés ; la règle d'équilibre n'autorise pas à recréer le malus supprimé. La transition porte sur la période d'emploi et préserve les minorations et restitutions anciennes."
a['substantive_impact']=impact('material_reduction',
    "La source entière autorise de minorer ou de majorer la contribution patronale selon cinq critères. La proposition retire la majoration pour les périodes nouvelles et conserve les minorations. C'est une suppression de surcotisation possible, déjà décidée au brouillon, et non l'abolition de l'assurance chômage.",
    "Le taux non modulé, les paramètres de malus et les montants individuels relèvent des textes d'application ; aucun taux effectif, rendement, solde budgétaire ou gain uniforme n'est démontré ici.",
    "Aucune charge nouvelle n'est identifiée : les données de calcul déjà autorisées servent aux minorations restantes ; aucune déclaration, compensation fiscale ou taux de remplacement n'est créé.",[
    effect('tax_removed','assurance-chomage-suppression-malus',
        "Suppression prospective des majorations patronales fondées sur les cinq critères de cet article.",
        "Majoration possible du taux de contribution chômage patronale selon fins de contrats, nature et durée, âge, taille et secteur ; taux et assiette effectifs fixés par les textes d'application, non déterminés dans cet article.",
        "Aucune majoration sur ces critères pour les périodes d'emploi nouvelles ; contribution de base et minorations conservées sur leur assiette propre, sans taux compensatoire créé.",
        'percent', "Employeurs dont la contribution d'assurance chômage pourrait être majorée sur ces critères.",
        "Périodes d'emploi à compter de l'entrée en vigueur ; créances, bonus, régularisations, restitutions et recours anciens conservés.",
        "Ni supplément équivalent ni hausse du taux non modulé destinée à neutraliser cette suppression ; financement à documenter, non inventé.",
        "Le taux de contribution de chaque employeur peut être minoré ou majoré en fonction :",
        "aucune majoration du taux patronal ne peut être établie sur le fondement des critères du présent article pour les périodes d'emploi postérieures à cette entrée en vigueur.")])

# L5521-2 : pas d'application du contrat privé au régime territorial de retraite.
a=answers[7]
a['reason'] = "Le brouillon est conservé comme coordination territoriale et temporelle nécessaire. La substitution renvoie au régime mahorais de validation de droits à retraite, non à une déclaration ou taxe autonome ; la supprimer retirerait une protection sans simplifier le contrat. La limite au 1er janvier 2028 provient de l'état ABROGE_DIFF et de valid_until. La transition préserve les périodes anciennes et les recours ultérieurs, sans prolongation artificielle ni fermeture supplémentaire des droits sociaux futurs."
a['review_notes'] = "L5132-11-1 et L5132-15-1 fournis ont été lus intégralement, sources et propositions : la référence sociale vise la validation des trimestres et non la durée du contrat. Leurs minima spéciaux de vingt heures ne sont pas le plancher général de vingt-quatre heures. Leurs propositions maintiennent un renvoi à L3123-27 comme seuil de cumul alors que ce dernier ne fixe plus de minimum général : cette discordance préexistante du projet doit être corrigée dans ces cibles, sans supprimer les dérogations favorables ; elle n'est pas résolue par la substitution mahoraise. La proposition de L5132-11-1 conserve aussi une mention de neuvième alinéa dans sa source alors que le positionnement diffère : ne pas valider cette référence implicitement. Le texte de l'article 7 de l'ordonnance du 27 mars 2002 et l'acte de raccordement de 2028 ne sont pas joints ; ils restent à contrôler hors corpus. La date de 2028 est recopiée des métadonnées source, non inventée comme date de la présente réforme."
a['substantive_impact']=impact('coordination_only',
    "La source complète est une substitution de référence sociale pour Mayotte ; elle est maintenue avec sa borne d'abrogation différée et une protection des périodes antérieures. Aucune cotisation, durée de travail ou formalité n'est supprimée par cet article.",
    "Le contenu exact de l'ordonnance mahoraise et le raccordement de 2028 ne sont pas fournis. Le texte ne prétend ni les réécrire ni établir les droits postérieurs par une prorogation de cette substitution.",
    "Aucune charge nouvelle n'est identifiée : aucune preuve de trimestre supplémentaire, déclaration ou condition d'accès à la retraite n'est ajoutée ; les voies de constatation et recours restent celles du régime compétent.",[
    effect('coordination','mayotte-validation-retraite-insertion',
        "Explicitation temporelle de l'adaptation de référence pour la validation de droits sociaux.",
        "Substitution de l'article 7 de l'ordonnance de 2002 à CSS L351-2 dans deux articles d'insertion ; fin différée au 1er janvier 2028 dans les métadonnées.",
        "Même substitution jusqu'au 31 décembre 2027 et maintien des droits relatifs à ces périodes, même constatés ultérieurement.",
        'other', "Salariés en insertion relevant de ces dispositions à Mayotte pour les périodes antérieures à 2028.",
        "Pas d'extension aux périodes à compter de 2028 ; droits futurs régis par leurs propres règles territoriales.",
        "Aucune nouvelle formalité, aucune extinction des droits déjà constitués.",
        "Pour l'application des articles L. 5132-11-1 et L. 5132-15-1 à Mayotte",
        "Jusqu'au 31 décembre 2027, pour l'application à Mayotte des articles L. 5132-11-1 et L. 5132-15-1")])

# L6131-1 : deux suppressions à leurs propres échéances, sans doublage des mesures.
a=answers[8]
a['proposed_xml']=a['proposed_xml'].replace(
    "3° Le versement de la contribution supplémentaire à l'apprentissage mentionnée à l'article L. 6242-1 ;",
    "3° Le versement de la contribution supplémentaire à l'apprentissage mentionnée à l'article L. 6242-1 pour les années civiles antérieures à celles commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression. Pour ces années, la contribution et ses seuils, assiette, taux, exonérations, exclusions, réduction territoriale, arrondis, échéance, recouvrement, restitutions, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables, même si le paiement ou le remboursement intervient ultérieurement. Pour les années nouvelles, aucune contribution supplémentaire, déclaration d'assiette ou transmission exclusivement justifiée par celle-ci n'est exigée ; aucun prélèvement de remplacement n'est dû sur son seul fondement. La créance imputable sur le solde de la taxe d'apprentissage et l'aide au recrutement dont les bénéficiaires sont définis à l'article L. 6242-1 restent accessibles selon leurs conditions propres, y compris aux futures entreprises éligibles ;")
a['proposed_xml']=a['proposed_xml'].replace(
    "Les contributions des 2°, 3° et 5° restent soumises à leurs conditions, exclusions, exonérations et taux propres, sans hausse destinée à remplacer la contribution supprimée.",
    "Les financements des 1°, 2° et 5° restent soumis à leurs conditions propres ; les contributions maintenues conservent leurs exclusions, exonérations et taux, sans hausse destinée à remplacer les contributions supprimées. La suppression d'une recette n'impose aucune restitution des aides ou droits valablement ouverts du seul fait de cette suppression.")
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=[
    "Retrait de l'obligation de versement de la contribution CPF-CDD pour les rémunérations des périodes de travail futures, y compris lorsque l'ancien contrat se poursuit.",
    "Retrait du versement et des formalités exclusivement attachées à la contribution supplémentaire à l'apprentissage pour les années nouvelles définies par L6242-1 proposé."])
a['reason'] = "Seconde passe avec correction substantielle de coordination : le brouillon maintenait à tort sans limite la contribution supplémentaire à l'apprentissage du 3°, alors que L6242-1 fourni la supprime à partir du 1er janvier suivant l'entrée en vigueur. Le 3° devient un reliquat des années anciennes et préserve les avantages autonomes. La suppression CPF-CDD du 4° reste acquise pour les périodes de travail futures, y compris des anciens CDD. Ces deux échéances sont différentes et ne sont pas fusionnées. Les 1°, 2° et 5° sont maintenus : formation directement fournie aux salariés, financement principal de formation et alternance, et engagements collectifs autonomes ; leur suppression globale n'est pas déduite de ce renvoi récapitulatif. Les deux coupes sont comptées sous leurs mesures d'assiette, non comme deux taxes supplémentaires supprimées dans la liste."
a['review_notes'] = "L6331-6 fourni fixe le 1 % sur les revenus d'activité retenus pour les cotisations sociales des titulaires de CDD : même critère de période travaillée que le 4°, et non date de paiement. L6242-1 fourni prévoit la suppression de la CSA pour les années civiles nouvelles et maintient le quotient et le seuil de 5 % nécessaires à la créance de taxe d'apprentissage ainsi que l'aide au recrutement ; le 3° ne rétablit ni taxe ni déclaration annuelle à zéro. Dans sa source, CSA : entreprises d'au moins 250 salariés, quotient inférieur à 5 %, exonération à 3 % avec progression de 10 %, taux de 0,4 %, 0,6 %, 0,2 %, 0,1 % et 0,05 %, réduction territoriale à 52 % ; ces paramètres demeurent pour les anciennes années, pas comme taux nouveaux. L6131-2, L6131-3, L6131-4 et L6332-1-2 lus : le recouvrement, l'affectation et les contributions conventionnelles nécessitent leurs coordinations sans recette de remplacement inventée. L6241-2 et L6243-1-2 lus : créance sur le solde sans report ni restitution, dans la limite de deux points et avec montant ministériel entre 2,50 et 5,00 euros, et aide au recrutement à conserver, sans transmission annuelle des seuls anciens redevables pour les années supprimées. Les références CSP L6133-1 et L6133-4, CASF L312-7 et CSS L243-1-2 ne sont pas toutes jointes au paquet de cibles ; les catégories du II sont recopiées sans en modifier le champ, leur concordance extérieure reste à vérifier. La note de 2024 ne date pas la réforme. Aucune économie ou compensation chiffrée n'est avancée."
a['substantive_impact']=impact('coordination_only',
    "La source entière récapitule les cinq voies de financement. La proposition retire prospectivement les obligations de versement CSA et CPF-CDD aux échéances respectives des articles d'assiette. Cette coordination n'est pas comptée comme une seconde suppression de chacune de ces contributions ; les autres financements restent dus.",
    "Le coût total de formation et la perte de recettes ne sont pas évalués. La CSA et le CPF-CDD ont des transitions distinctes ; la contribution unique, les accords conventionnels, leurs exonérations et les exclusions du II restent à leur champ.",
    "Aucune charge nouvelle n'est identifiée : ni contribution de remplacement ni déclaration à zéro pour les sommes supprimées. Les calculs d'une créance favorable demeurent ceux déjà prévus, sans nouvelle liste à transmettre sur le seul fondement de la CSA.",[
    effect('coordination','suppression-contribution-cpf-cdd',
        "Coordination du 4° avec l'extinction de la contribution CPF-CDD de L6331-6.",
        "Versement du CPF-CDD, dont L6331-6 fixe le taux de 1 % sur le revenu d'activité soumis aux cotisations sociales des titulaires de CDD, avec exclusions formation, alternance et saisonniers.",
        "Aucun CPF-CDD sur les rémunérations des périodes travaillées après la réforme, même d'un ancien CDD ; 1 % et exclusions conservés pour les seules périodes anciennes.",
        'percent', "Employeurs relevant du I et rémunérant un CDD auparavant dans l'assiette de L6331-6.",
        "Périodes de travail à compter de l'entrée en vigueur du contrat unique, sans dépendre du jour de versement ; restitutions anciennes conservées.",
        "Pas de taxe équivalente sur le contrat unique ou la mission, pas de déclaration exclusivement liée à une recette éteinte.",
        "Le versement de la contribution dédiée au financement du compte personnel de formation pour les titulaires d'un contrat à durée déterminée mentionnée à l'article L. 6331-6",
        "Cette contribution est supprimée pour les périodes de travail à compter de cette entrée en vigueur, y compris pour les CDD antérieurs qui se poursuivent."),
    effect('coordination','suppression-contribution-supplementaire-apprentissage',
        "Coordination du 3° avec la suppression de la CSA dans L6242-1 proposé.",
        "Versement annuel de CSA pour les entreprises d'au moins 250 salariés et quotient d'alternants inférieur à 5 % ; assiette des rémunérations de taxe d'apprentissage, taux variables 0,4 %, 0,6 %, 0,2 %, 0,1 % et 0,05 %, avec exonérations et taux territoriaux favorables.",
        "Aucune CSA ni assiette à déclarer pour les années civiles nouvelles ; anciennes assiettes, taux et exonérations conservés, créance favorable sur taxe d'apprentissage distincte maintenue.",
        'percent', "Entreprises entrant dans le champ de la CSA ; futurs bénéficiaires de la créance sur le solde et de l'aide au recrutement préservés.",
        "1er janvier de l'année suivant celle de l'entrée en vigueur de la suppression, sans remboursement général des années anciennes.",
        "Pas de complément de taxe ni de transmission exclusivement liée à la contribution supprimée ; suivi nécessaire à l'avantage autonome maintenu.",
        "Le versement de la contribution supplémentaire à l'apprentissage mentionnée à l'article L. 6242-1",
        "Pour les années nouvelles, aucune contribution supplémentaire, déclaration d'assiette ou transmission exclusivement justifiée par celle-ci n'est exigée")])

# L6222-5 : retirer les neuf engagements redondants, pas leurs règles protectrices.
a=answers[9]
a['proposed_xml']=a['proposed_xml'].replace(
    "La déclaration comporte l'engagement de respecter les conditions prévues aux articles suivants :",
    "La déclaration n'a pas à reproduire un engagement de respecter les articles énumérés ci-après. Aucun engagement distinct, attestation ou signature supplémentaire portant seulement sur le respect de ces articles n'est exigé. Leurs dispositions restent applicables de plein droit, dans leur champ :")
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=[
    "Suppression de l'obligation de faire figurer dans la déclaration familiale un engagement exprès répétant les neuf groupes de dispositions légales déjà applicables à l'apprentissage."])
a['reason'] = "Coupe supplémentaire par rapport au brouillon : la déclaration n'a plus à réitérer un engagement de satisfaire à neuf groupes de règles légales, déjà obligatoires sans cette promesse. Aucun engagement ou justificatif équivalent ne la remplace. La déclaration substitutive, les neuf numéros et les règles matérielles qu'ils désignent restent entiers : formation, salaire, protection contre l'employeur défaillant et compte au nom du mineur. La coordination du contrat unique est conservée sans confondre durée pédagogique et durée de l'emploi ; le 4° décrit correctement les dates de début de L6222-12. Les signatures requises pour constater l'emploi du mineur ne sont pas supprimées."
a['review_notes'] = "Les neuf groupes de textes ont été lus dans le corpus. L6222-4 impose un écrit et des signatures ; la déclaration remplace cet écrit selon la dérogation spéciale, sans double contrat. R6224-8, également lu, impose la signature de l'apprenti, le visa du directeur du CFA et la procédure de dépôt ; L6224-1 lu organise la transmission à l'opérateur. Ces garanties de consentement et de formation subsistent ; elles ne peuvent servir à exiger de nouveau les neuf engagements redondants supprimés. Coordonner le modèle ou formulaire de déclaration et toute instruction d'usage imposant ces mentions : acte extérieur non joint, non présenté comme réécrit. R6222-6 et R6222-7 lus portent sur la convention d'aménagement pédagogique et son modèle, non sur la déclaration familiale ; ne pas les attribuer à cette formalité. L6222-12 fixe des dates de début et non une durée d'emploi ; cette inexactitude descriptive préexistante est rectifiée sans changer le numéro. L6222-16 rédigé dans ce lot conserve toute la durée pour rémunération et ancienneté et supprime l'essai rétabli par convention pour les nouveaux contrats. L6225-4 et L6225-5 maintiennent le salaire en suspension et l'indemnité spéciale jusqu'au terme de la période d'apprentissage ; le zéro d'indemnité ordinaire avant un an ne les neutralise pas. L6227-12 lu exclut cet article du secteur public non industriel et commercial ; L6235-4 lu conserve ses exceptions transfrontalières, sans extension implicite. Aucun taux de salaire ni fraction du salaire à placer sur le compte n'est inventé."
a['substantive_impact']=impact('mixed',
    "Par rapport à la source entière, la déclaration subsiste mais son contenu n'a plus à porter neuf engagements redondants. C'est une coupe supplémentaire effective au brouillon. La coordination du contrat unique impose aussi la poursuite indéterminée de l'emploi après la phase pédagogique ; son coût et le solde net ne sont pas établis.",
    "Ni dépôt, ni signature de l'apprenti, ni visa existant du CFA ne sont abrogés par cet article. Les obligations légales de formation et de protection, le compte au nom du mineur et les règles extérieures des formulaires restent à leur champ.",
    "Aucune charge administrative nouvelle n'est identifiée : aucun engagement ou justificatif ne remplace les mentions retirées. L'emploi indéterminé obligatoire relève de la mesure commune et peut prolonger les obligations salariales après la formation ; ce coût n'est pas déclaré compensé par la coupe documentaire.",[
    effect('obligation_removed','apprentissage-familial-sans-engagements-redondants',
        "Suppression de la répétition formelle des neuf engagements légaux dans la déclaration familiale.",
        "La déclaration doit comporter l'engagement exprès de satisfaire aux neuf groupes d'articles énumérés, en plus de leur applicabilité légale.",
        "Les neuf groupes restent applicables de plein droit ; aucune répétition d'engagement, attestation ou signature supplémentaire à cette seule fin.",
        'legal_duty', "Ascendants employant un apprenti mineur dans le champ de la déclaration substitutive.",
        "Déclarations des engagements nouveaux ; anciennes déclarations valables sans nouvelle formalité, droits et aides préservés.",
        "Déclaration existante conservée comme substitut du contrat, aucune nouvelle pièce remplaçant les engagements retirés.",
        "Elle comporte l'engagement de satisfaire aux conditions prévues par les articles :",
        "La déclaration n'a pas à reproduire un engagement de respecter les articles énumérés ci-après."),
    effect('coordination','contrat-unique-duree-indeterminee',
        "Coordination de l'effet contractuel de la déclaration avec une phase d'apprentissage sans terme d'emploi.",
        "Déclaration assimilée à un contrat d'apprentissage, lequel peut encore être à durée limitée selon le droit source.",
        "Pour les engagements nouveaux, déclaration constatant le contrat unique et sa phase pédagogique ; la fin de formation ne rompt pas l'emploi.",
        'regime', "Apprentis mineurs employés par un ascendant relevant du dispositif de L6222-5.",
        "Critère de conclusion de l'engagement ; déclarations antérieures et droits acquis préservés, sans nouveau renouvellement de CDD.",
        "Continuité salariale de l'emploi indéterminé à anticiper ; pas de nouveau contrat ou essai à la fin de la phase.",
        "Cette déclaration est assimilée dans tous ses effets à un contrat d'apprentissage.",
        "elle constate ce contrat unique comportant une phase d'apprentissage ; la fin de la phase de formation n'entraîne pas la fin de l'emploi.")])

# L6222-16 : rendre la date de la réforme explicite, sans ajouter une nouvelle coupe fictive.
a=answers[10]
a['proposed_xml'] = "<p>À compter de l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, lorsque l'apprentissage est effectué dans un tel contrat, la relation de travail se poursuit dans le même contrat à l'issue de la phase d'apprentissage, sans nouvelle période d'essai. Lorsque l'apprentissage est suivi de la signature d'un nouveau contrat unique dans la même entreprise, aucune période d'essai ne peut être imposée, quelle que soit la date de conclusion du contrat dans lequel l'apprentissage a été effectué. Une disposition conventionnelle ne peut permettre de rétablir cet essai.</p><p>Toute la durée de l'apprentissage est prise en compte pour le calcul de la rémunération et de l'ancienneté du salarié, sans compter deux fois une même période. Cette prise en compte n'est pas limitée à la durée écoulée après l'entrée en vigueur de cette loi.</p><p>Les contrats de travail conclus avant cette entrée en vigueur à la suite de l'apprentissage restent soumis, pour leur période d'essai, aux règles antérieures : aucun essai ne peut être imposé, sauf disposition conventionnelle contraire alors applicable. La durée du contrat d'apprentissage reste intégralement prise en compte pour la rémunération et l'ancienneté. Cette transition n'autorise ni nouveau CDD ni renouvellement de CDD après cette date.</p>"
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=[
    "Suppression, pour les nouvelles relations après apprentissage dans la même entreprise, de la possibilité conventionnelle d'imposer une nouvelle période d'essai malgré la dispense légale."])
a['reason'] = "La coupe du brouillon demeure : la réserve conventionnelle permettant d'imposer un nouvel essai après l'apprentissage est supprimée pour les nouveaux emplois ; la transition en protège le régime pour les contrats déjà conclus. La nouvelle rédaction identifie explicitement la loi dont dépend cette entrée en vigueur. Pas de coupe supplémentaire de la reprise d'ancienneté et de rémunération : elle évite une perte de droits et le fractionnement artificiel de la relation chez le même employeur. Le CDI d'apprentissage existait déjà ; sa simple poursuite ne peut être comptée une deuxième fois comme fusion."
a['review_notes'] = "L6222-7 et L6222-7-1 lus distinguent relation indéterminée et phase pédagogique. Coordonner le 5° de L6222-5 dans ce lot ; la cible L6222-16 de reference-targets porte l'ancien brouillon et n'est pas une norme en vigueur. La modification finale ne change que l'explicitation de la date et conserve l'absence de nouvel essai et toute l'ancienneté. Pour le nouveau barème ordinaire, cette durée reconnue compte au seuil d'un an à la fin effective, préavis inclus, puis dans toute l'assiette d'ancienneté à 0,20 mois par année totale et au prorata des mois complets, plafond de six mois ; la première année n'est pas soustraite. L1234-3 et R1234-1 ont été lus hors du paquet de cibles, sans ajouter de renvoi normatif ici. Les règles de procédure et indemnités spéciales restent distinctes. L6227-12 lu exclut L6222-16 de l'apprentissage du secteur public non industriel et commercial : aucune extension à un statut d'agent public n'est inférée."
a['substantive_impact']=impact('material_reduction',
    "La source entière laisse une convention collective rétablir un essai après l'apprentissage. La proposition supprime cette possibilité pour les contrats nouveaux de la même entreprise et maintient la reprise intégrale d'ancienneté. La coupe existait déjà au brouillon ; l'explicitation de la date n'est pas une seconde réduction.",
    "Les contrats conclus antérieurement restent soumis à la réserve conventionnelle alors applicable. Ni l'essai initial chez un nouvel employeur ni les statuts publics exclus de cet article ne sont modifiés.",
    "Aucune charge administrative nouvelle n'est identifiée : pas de certificat de fin de formation, nouveau contrat imposé pour la simple poursuite ou formalité d'ancienneté supplémentaire. L'employeur ne peut plus rétablir l'essai supprimé.",[
    effect('obligation_removed','apprentissage-sans-nouvel-essai',
        "Suppression de la possibilité conventionnelle d'assujettir le salarié à un nouvel essai après apprentissage.",
        "Dispense d'essai dans la même entreprise, sauf dispositions conventionnelles contraires ; durée d'apprentissage reprise pour le salaire et l'ancienneté.",
        "Aucun nouvel essai imposable dans la même entreprise pour les nouveaux contrats ou la poursuite du contrat unique, même par convention ; durée intégralement reprise.",
        'legal_duty', "Salariés poursuivant l'emploi dans la même entreprise après apprentissage dans le champ privé de cet article.",
        "Relations conclues après la réforme ; anciens contrats post-apprentissage soumis aux règles d'essai antérieures.",
        "Aucun document ou délai substitutif ; la simple fin de phase ne crée pas une nouvelle embauche.",
        "aucune période d'essai ne peut être imposée, sauf dispositions conventionnelles contraires.",
        "Une disposition conventionnelle ne peut permettre de rétablir cet essai.")])

# L6222-18-2 : préserver les six mois et leurs champs particuliers.
a=answers[11]
a['proposed_xml'] = a['proposed_xml'].replace(
    "Ces garanties s'appliquent également à la rupture d'un contrat unique à durée indéterminée pendant sa période d'apprentissage.",
    "Ces garanties s'appliquent également, dans le champ et sous les exceptions territoriales et transfrontalières applicables au présent article, à la rupture d'un contrat unique à durée indéterminée pendant sa période d'apprentissage.")
a['reason'] = "Le brouillon est conservé pour coordonner explicitement les nouveaux contrats uniques avec les six mois de formation après rupture. Les deux obligations du centre, poursuite théorique et aide à trouver un employeur, sont les prestations favorables elles-mêmes, non un doublon documentaire ; les supprimer fermerait un droit. Le statut de stagiaire reste nécessaire à la continuité de protection. Aucune réduction supplémentaire de taxe ou de formalité ne peut être attribuée à cet article ; le droit source couvrait déjà l'apprentissage en CDI et n'est pas présenté comme une aide nouvelle."
a['review_notes'] = "L6222-18 fourni a été lu en entier, source, note et proposition. La source distingue les quarante-cinq jours pratiques, les contrats postérieurs au 1er janvier 2019 et les ruptures ultérieures ; la proposition entend coordonner les nouveaux contrats uniques et préserver les anciens, mais sa réserve finale doit continuer de protéger les contrats encore antérieurs à 2019. La durée de six mois est celle de la poursuite de formation, pas un terme d'emploi ni un salaire à la charge de l'ancien employeur. L6332-14 II et L6341-1 lus maintiennent les voies de prise en charge et de rémunération du stagiaire dans leur champ ; leur financement doit être coordonné sans recette inventée. L6235-4 lu conserve les exceptions transfrontalières : maintien de L6222-18-2 quand la pratique est à l'étranger, exclusion de son premier alinéa lorsque la théorie est dans le pays frontalier ; le nouvel alinéa de coordination ne contourne pas cette exclusion. L'apprentissage public reste régi par ses textes propres et n'est pas assimilé à un CDI d'agent public par cette garantie."
a['substantive_impact']=impact('coordination_only',
    "La source entière impose déjà au centre six mois de poursuite théorique, une aide à la recherche d'employeur et le statut de stagiaire. La proposition préserve ces prestations lors de la réforme du contrat, sans revendiquer une nouvelle durée, une nouvelle aide ou une réduction de prélèvement.",
    "Le coût et la prise en charge de la formation ne sont pas chiffrés. Les exceptions transfrontalières, les contrats anciens et les règles du secteur public restent à leur champ propre ; six mois ne bornent pas l'emploi.",
    "Aucune charge nouvelle propre à l'article n'est identifiée : le centre accomplissait déjà les mêmes prestations pour la rupture d'un apprentissage ; aucun registre, condition d'aide ou justificatif supplémentaire n'est ajouté.",[
    effect('coordination','contrat-unique-duree-indeterminee',
        "Maintien de la continuité de formation en cas de rupture de l'apprentissage porté par le contrat unique.",
        "Six mois de formation théorique, aide à un nouvel employeur et statut de stagiaire après rupture visée à L6222-18, y compris apprentissage en CDI.",
        "Mêmes prestations et durée de six mois pour les ruptures de contrat unique pendant l'apprentissage, sans fin automatique du contrat à la fin de la phase.",
        'regime', "Apprentis dont le contrat est rompu dans le champ de L6222-18-2 et leurs centres de formation.",
        "Anciens droits maintenus ; application coordonnée aux nouveaux emplois, sous les exceptions territoriales et transfrontalières existantes.",
        "Aucune attestation ou condition d'inscription nouvelle ; aucun salaire post-rupture ajouté à la charge de l'ancien employeur.",
        "L'apprenti bénéficie pendant cette période du statut de stagiaire de la formation professionnelle.",
        "Ces garanties s'appliquent également, dans le champ et sous les exceptions territoriales et transfrontalières applicables au présent article, à la rupture d'un contrat unique à durée indéterminée pendant sa période d'apprentissage.")])

# Les réductions conservées doivent elles aussi porter leurs métadonnées de réforme.
for i, removals in {
    4: ["Suppression de l'avenant séparé pour les modalités d'exécution d'une rééducation chez l'employeur déjà fixées dans la convention tripartite signée."],
    5: ["Suppression prospective de la voie du contrat de mission à durée déterminée dans l'entreprise adaptée, remplacée par l'emploi unique indéterminé avec garanties d'intermission.",
        "Suppression de la justification d'une dérogation au plancher légal général de vingt-quatre heures, en coordination avec sa suppression, et du seuil de deux mois pour la dispense de carence en embauche directe nouvelle."],
    6: ["Suppression du pouvoir de majorer la contribution patronale d'assurance chômage selon les cinq critères de modulation de cet article, pour les périodes d'emploi postérieures à la réforme."]
}.items():
    answers[i].update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removals)

# Appréciations propres à chaque article pour les trois cibles communes.
common = {
 'L1234-1': [
    "L'article abrogé n'établit aucun délai de rupture. La proposition de L1234-1 fixe quinze jours calendaires pour le nouvel emploi privé et conserve les anciens délais ; elle ne plafonne pas la mission à quinze jours et ne supprime pas les garanties d'intermission ni les autorisations protectrices.",
    "L'égalité salariale de L5132-11 ne renvoie pas au préavis : les quinze jours proposés à L1234-1 ne retardent pas l'égalité jusqu'à l'expiration d'un essai ou d'un préavis. Les anciens contrats conservent leurs délais et le paiement des jours fériés garde sa condition chez l'utilisateur.",
    "L1234-1 vise une rupture patronale, tandis que la sortie de L5134-29 est une mobilité du salarié avec dispense spéciale déjà prévue. Le nouveau préavis de quinze jours ne peut être opposé à cette dispense ; les délais et protections collectives demeurent hors de son objet.",
    "L1234-1 règle le préavis patronal, non le départ favorable du salarié prévu ici. Il n'autorise pas à opposer quinze jours à la dispense du contrat jeune encore éligible. Les anciens préavis et procédures restent distincts et aucun nouvel emploi public n'est transformé en contrat privé.",
    "L1234-1 ne régit ni la durée de rééducation ni la démission du III. Sa proposition de quinze jours pour le contrat nouveau ne supprime pas les protections de santé, l'accord de caisse ou les autorisations spéciales, et les anciens contrats gardent les délais réservés par la cible.",
    "Le préavis de quinze jours de L1234-1 porte sur la rupture de l'emploi par l'entreprise adaptée, jamais sur la fin d'une mission. Il ne dispense pas des procédures collectives ou autorisations protectrices. Les anciens contrats à terme conservent leurs règles propres, non un préavis nouveau ajouté à leur échéance.",
    "Les quinze jours de L1234-1 ne définissent pas un critère fiscal de modulation chômage et ne font pas d'une fin de mission une fin d'emploi. La suppression du malus n'abrège aucune procédure de licenciement ; les droits de préavis des anciens contrats demeurent réservés.",
    "Le préavis privé de L1234-1 est sans objet pour la substitution de référence mahoraise de retraite : elle ne vise aucune rupture ni ancienneté de préavis. Aucun délai de quinze jours ne peut être déduit pour valider les trimestres ou modifier les règles territoriales de 2028.",
    "L1234-1 n'est pas le fait générateur des contributions de formation. Ses quinze jours ne déplacent ni la période travaillée du CPF-CDD ni l'année civile de suppression de la CSA ; la cotisation ancienne reste déterminée par sa propre transition, pas par la notification d'un licenciement.",
    "La déclaration familiale ne déroge pas au préavis de l'emploi privé nouveau. L1234-1 proposé conserve quinze jours et les protections distinctes ; il n'autorise ni la fin automatique de l'emploi après la phase d'apprentissage ni la suppression du salaire en suspension de L6225-4.",
    "L'absence de nouvel essai après apprentissage ne supprime pas le préavis patronal du contrat unique : quinze jours selon L1234-1 et calcul selon L1234-3 lu hors paquet. Les anciens contrats conservent leurs règles ; une fin de formation n'est ni notification de rupture ni nouveau point de départ d'ancienneté.",
    "Le délai de quinze jours de rupture patronale ne se confond pas avec les six mois de formation après rupture. La garantie de L6222-18-2 ne vaut ni notification ni dispense de procédure ; les préavis antérieurs et les protections de l'apprenti demeurent dans leurs régimes respectifs."
 ],
 'L1221-2': [
    "La source de L1221-2 permet encore le CDD, tandis que sa proposition rend le contrat unique obligatoire pour les recrutements futurs. Cette entrée en vigueur doit coïncider avec l'abrogation de la permission spéciale ; aucune condition d'âge ne ferme alors le CDI, et les aides ciblées demeurent autonomes.",
    "La proposition de L1221-2 distingue emploi indéterminé et affectation limitée. Les modes de rémunération et les jours fériés de L5132-11 s'appliquent dans ce champ sans rétablir un CDD par le nombre d'heures forfaitaires. Les contrats anciens et leur ancienneté ne sont pas convertis d'office.",
    "Le 2° est coordonné avec L1221-2 proposé : l'offre nouvelle porte sur un emploi sans terme, même si l'essai ou l'accompagnement est limité. Le CDD d'au moins six mois ne demeure qu'au titre d'un contrat déjà conclu avant la réforme, sans renouvellement nouveau autorisé.",
    "L1221-2 proposé n'ouvre pas de nouveau contrat jeune fermé en 2007 ; il régit seulement le support du futur emploi d'apprentissage ou de professionnalisation qui motive un départ résiduel. La phase de formation peut finir sans terminer cet emploi, et les droits du contrat source ancien demeurent.",
    "La convention de rééducation n'est pas un contrat de travail à terme. Selon L1221-2 proposé, sa fin n'éteint pas le nouvel emploi ; sa signature valant avenant ne conclut pas un nouveau contrat ou un nouvel essai. Les anciens emplois et leur ancienneté conservent leur transition.",
    "L1221-2 proposé interdit le nouveau CDD même dans une entreprise adaptée. L'affectation ou le parcours reste limité sans terme d'emploi ; la garantie du CDI devient générale. Les vingt-quatre mois de contrat de mission et la faculté de CDD de deux mois sont strictement anciens, sans renouvellement futur.",
    "Le nouveau L1221-2 interdit un terme d'emploi lié à la mission ou à la formation. Le critère du 2° de L5422-12 s'apprécie donc par l'objet et la durée de phase pour préserver une minoration, sans ressusciter le CDD ; la fin de mission n'est pas une fin de contrat salarial si l'emploi continue.",
    "L1221-2 proposé concerne la forme du contrat privé, pas la validation d'assurance vieillesse de Mayotte. Les deux articles d'insertion doivent le coordonner eux-mêmes ; la substitution sociale n'autorise ni CDD futur ni suppression des vingt heures spéciales ou des droits territoriaux.",
    "L1221-2 proposé écarte les nouveaux CDD ; cela ne suffit pas à éteindre le CPF-CDD des rémunérations d'un ancien CDD continuant. Le 4° et L6331-6 coordonnent expressément ces périodes futures sans prélèvement de remplacement ; la formation reste une phase et non un terme d'emploi.",
    "L1221-2 proposé s'applique à la relation privée constatée par la déclaration substitutive : une phase pédagogique limitée n'autorise pas un contrat à terme. Les anciennes déclarations et leurs droits restent soumis à leur régime et aucun renouvellement postérieur de CDD n'est rendu possible.",
    "L1221-2 proposé explique la poursuite du même contrat après la phase pédagogique et exclut une nouvelle embauche à terme. L6222-16 reprend toute la durée d'apprentissage, même antérieure à la réforme, sans remettre l'ancienneté à zéro ni autoriser un nouveau CDD après cette date.",
    "La proposition de L1221-2 sépare la durée de formation de l'emploi indéterminé. Les six mois de L6222-18-2 suivent une vraie rupture et non la seule fin d'une phase ; ils ne fixent pas un terme au contrat unique. Les garanties des anciens apprentis restent ouvertes dans leurs règles propres."
 ],
 'L1234-9': [
    "L1234-9 proposé ne concerne que l'indemnité ordinaire de rupture patronale, non l'aide d'inclusion. Seuil d'un an à la fin effective, préavis inclus, puis 0,20 mois par année totale et mois complets, plafond six mois ; anciens droits et indemnités spéciales préservés, sans remettre l'ancienneté à zéro lors d'une conversion.",
    "L1234-9 ne modifie ni le salaire de comparaison ni les jours fériés. Le zéro ordinaire avant un an n'efface aucune créance de L5132-11 ; pour un nouveau contrat, seuil au terme effectif préavis inclus, puis 0,20 mois sur toute l'ancienneté avec mois complets et plafond de six mois, selon la cible.",
    "La mobilité de L5134-29 n'est pas une rupture à l'initiative de l'employeur et ne crée pas l'indemnité ordinaire de L1234-9. Le seuil d'un an au terme effectif préavis inclus et le barème 0,20 mois sur ancienneté totale ne conditionnent ni la suspension ni la dispense ; salaires et congés restent dus.",
    "La dispense de préavis à l'initiative du salarié n'ouvre pas l'indemnité ordinaire de L1234-9. Le seuil d'un an à la fin effective et le calcul à 0,20 mois par année totale avec mois complets et plafond six mois sont étrangers à ce bénéfice ; anciens droits et réparations d'une illégalité demeurent distincts.",
    "L1234-9 proposé ne soumet pas les indemnités journalières de rééducation au seuil d'un an et ne les plafonne pas à six mois. Son barème de 0,20 mois par année totale et mois complets ne vise que l'ordinaire patronal ; toute ancienneté reconnue compte au terme effectif préavis inclus, avec réserves des indemnités spéciales et anciens droits.",
    "Les intermissions comptées par L1251-58-2 entrent dans l'ancienneté reconnue pour L1234-9 : seuil d'un an à la fin effective, préavis inclus, puis 0,20 mois par année totale et mois complets, plafond six mois, sans retrancher la première année. Ce zéro initial n'abolit ni garantie mensuelle, ni congés, ni primes anciennes ou indemnités spéciales.",
    "L1234-9 ne fixe aucune assiette ou taux de contribution chômage : son seuil d'un an au terme effectif et ses 0,20 mois par année totale concernent uniquement la rupture ordinaire patronale. L'exclusion du malus ne dispense donc pas d'indemnités dues ni ne supprime une minoration en fonction du motif ancien.",
    "L1234-9 est sans effet sur la substitution de retraite mahoraise : son année d'ancienneté, préavis inclus, et les 0,20 mois par année totale ne définissent ni les trimestres validés ni une cotisation de retraite. Aucune condition de rupture privée n'est ajoutée aux périodes protégées avant 2028.",
    "L1234-9 ne déclenche ni la CSA ni le CPF-CDD : son année d'ancienneté au terme effectif et ses 0,20 mois par année totale ne sont pas une assiette de formation. La suppression des recettes ne retire ni salaires ou congés ni l'indemnité patronale éventuellement due ; les anciennes composantes restent distinctes.",
    "La déclaration ne transforme pas les indemnités spéciales de protection du mineur en indemnité ordinaire. Pour cette dernière seulement, L1234-9 proposé fixe un an à la fin effective préavis inclus, puis 0,20 mois sur toute l'ancienneté avec mois complets et plafond six mois ; L6225-4 et L6225-5 conservent salaire et réparation spéciale.",
    "Toute la durée d'apprentissage reprise alimente L1234-9 proposé : un an au terme effectif préavis inclus, puis 0,20 mois par année totale, fractions en mois complets, plafond six mois. La première année n'est pas retirée et aucune période n'est doublée ; la cible maintient les composantes antérieures et les indemnités spéciales.",
    "La poursuite de formation et le statut de stagiaire ne dépendent pas du seuil d'un an de L1234-9. Son barème ordinaire de 0,20 mois sur toute l'ancienneté, mois complets et plafond six mois concerne une rupture patronale éligible, non six mois de formation ; droits anciens et réparations spéciales ne sont pas neutralisés."
 ]
}

specific = {
 (0,'L1251-58-1'): "La proposition de L1251-58-1 rend le CDI unique obligatoire pour les nouveaux recrutements et maintient contrat commercial et lettre de mission. L'abrogation de L5132-6-1 ne supprime pas ces documents ni les droits des CDI antérieurs : seul disparaît le besoin d'une permission spéciale de CDI, pas l'emploi lui-même.",
 (0,'L5132-6'): "L5132-6 source exclut la section 4 bis et prévoit contrats de mission et limite de vingt-quatre mois ; sa proposition réintègre le CDI intérimaire, ses garanties et les futurs droits d'aide. L'abrogation de la dérogation de L5132-6-1 doit être simultanée, faute de quoi l'accès favorable au CDI d'inclusion serait privé de son relais général.",
 (3,'L1237-1'): "L1237-1 proposé prévoit quinze jours calendaires notifiés selon L1234-3 mais réserve les dispenses légales particulières. L5134-57 est précisément cette dispense résiduelle : aucune notification ne peut la transformer en quinze jours de travail imposé, et une démission ordinaire n'ouvre pas l'indemnité patronale de L1234-9.",
 (4,'L1237-1'): "La démission du III demeure celle de L1237-1 : quinze jours calendaires pour le contrat unique selon notification écrite et calcul de L1234-3, anciens préavis pour les anciens contrats. L5213-3-1 n'ajoute pas de dispense de préavis ; le bénéfice éventuel de l'indemnité journalière ne dépend pas du seuil d'indemnité patronale.",
 (4,'L323-3-1'): "La cible appartient au code de la sécurité sociale et n'est fournie qu'en source officielle. Elle permet la formation avec accord du médecin traitant, avis du médecin-conseil, compatibilité avec l'arrêt et accord de caisse, et mentionne la convention de rééducation au 2°. Fusionner l'avenant ne supprime aucune de ces garanties ni ne privatise un régime public.",
 (5,'L1251-12-1'): "La source fixe les plafonds de dix-huit, neuf, vingt-quatre ou trente-six mois et le minimum de six mois d'une commande export ; sa proposition abroge ce régime pour les contrats nouveaux. Les vingt-quatre mois de L5213-13-3 restent une dérogation des anciens contrats seulement ; la dispense déjà acquise au CDI par L1251-58-6 ne constitue pas un deuxième allègement.",
 (5,'L1251-12'): "La source permet à l'accord de branche étendu de fixer la durée du contrat de mission sans pourvoir durablement un poste permanent. La proposition limite cette faculté à l'affectation auprès de l'utilisateur et préserve l'interdiction. L5213-13-3 n'abolit pas ces limites conventionnelles et n'en fait pas un terme de l'emploi indéterminé.",
 (5,'L1251-36'): "La source définit la carence en jours d'ouverture ; sa proposition l'abroge pour les affectations ou embauches nouvelles et fait cesser les délais en cours, avec recours antérieurs préservés. Le renvoi prospectif du brouillon de L5213-13-3 est retiré : les deux dispenses demeurent explicites sans s'appuyer sur un fondement abrogé ni recréer un CDD.",
 (5,'L1251-58-1'): "L1251-58-1 source autorise le CDI intérimaire et sa proposition l'impose aux recrutements futurs. La lettre de mission et la mise à disposition restent nécessaires pour l'affectation, sans contrat salarial distinct ni fin d'emploi à son échéance ; les CDI antérieurs conservent leur ancienneté et leurs garanties.",
 (5,'L1251-58-2'): "La cible assimile les intermissions à du travail effectif pour les congés et l'ancienneté et exige un écrit avec huit rubriques. Le renvoi de L5213-13-3 préserve cette assimilation et les mentions, notamment mobilité respectant la vie familiale et garantie mensuelle ; un changement de mission ne remet pas ancienneté ou essai à zéro.",
 (5,'L1251-58-3'): "La garantie source est au moins le SMIC multiplié par les heures de durée légale du mois, compte tenu des rémunérations de mission. La proposition la conserve même entre missions. Le volume adapté de L5213-13-3 ne crée aucune minoration implicite de cette garantie ; son extension obligatoire aux nouveaux recrutements est recensée comme charge, pas comme économie.",
 (5,'L1251-58-6'): "La source dispense déjà le salarié en CDI du plafond légal de L1251-12-1 et la proposition l'étend explicitement au contrat unique. L5213-13-3 conserve cette dispense, sans lui appliquer vingt-quatre mois. La cible doit coordonner son propre renvoi au plafond législatif dont l'abrogation est proposée ; cette discordance n'autorise pas à le rétablir.",
 (6,'L1251-1'): "L1251-1 distingue au 1° le contrat commercial de mise à disposition et au 2° le contrat de mission salarial ; la proposition du 2° prévoit une lettre de mission pour l'emploi indéterminé et garde les anciens contrats. L'exclusion du 1° de L5422-12 est conservée pour les anciens contrats de mission ; la simple fin d'une lettre ne devient pas une rupture d'emploi, ni l'utilisateur public un employeur privé.",
 (7,'L5132-15-1'): "Dans cette cible, le renvoi à CSS L351-2 vise la validation des trimestres au sein de l'alinéa de durée du travail ; le minimum spécial est vingt heures et connaît ses propres dérogations. La substitution mahoraise ne modifie pas ces heures. La proposition conserve un renvoi problématique à L3123-27 désormais sans plancher : correction à faire dans la cible sans fermer l'avantage ni prolonger la substitution après 2027.",
 (7,'L5132-11-1'): "La validation de trimestres de CSS L351-2, et non la durée indéterminée, est l'objet de la substitution. La cible source impose vingt heures sauf cumul, distinctes des vingt-quatre heures générales. Sa proposition doit corriger le seuil de cumul lié au L3123-27 modifié et les références d'alinéa : L5521-2 ne les valide pas et ne peut effacer les dérogations favorables ou les droits anciens.",
 (8,'L6331-6'): "La cible source fixe 1 % du revenu d'activité soumis aux cotisations sociales des titulaires de CDD, avec exclusions formation/alternance et saisonniers. Sa proposition supprime la recette sur les périodes travaillées après la réforme, même d'un CDD ancien : le 4° reprend exactement cette transition, préserve les exclusions et ne substitue pas un critère de date de paiement.",
 (8,'L6242-1'): "Contrairement au brouillon du 3°, la proposition fournie de L6242-1 supprime la CSA dès l'année civile suivant l'entrée en vigueur et garde les anciennes années. Elle maintient quotient et seuil de 5 % pour la créance sur le solde et l'aide au recrutement, avec périodes d'alternance des contrats uniques ; le 3° est rectifié sans rétablir une liste annuelle de redevables ou une taxe compensatoire.",
 (9,'L6222-16'): "La source de L6222-16 exclut l'essai sauf convention contraire et reprend l'apprentissage pour rémunération et ancienneté. La vue proposée supprime la réserve pour les nouveaux contrats et conserve les anciens ; notre texte final du même lot explicite sa date d'entrée en vigueur. Le 5° maintient ce champ, la durée totale reprise et l'absence d'essai nouveau, sans double compte ni réinitialisation du seuil d'un an.",
 (11,'L6222-18'): "La source permet la rupture durant quarante-cinq jours pratiques puis prévoit accord, motifs spéciaux, médiation et liquidation ; sa note réserve les contrats antérieurs à 2019. La proposition vise quinze jours pour le contrat unique, notification et indemnité ordinaire sous conditions, tout en conservant les anciens droits. Le renvoi de L6222-18-2 ouvre toujours six mois de formation après rupture, sans lier cette prestation au seuil d'un an ni faire disparaître les indemnités spéciales ; la cible doit garder clairement sa transition pré-2019."
}

for i, a in enumerate(answers):
    source_key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in references['requirements'][source_key]:
        target = references['targets'][target_key]
        number = target['number']
        assessment = common[number][i] if number in common else specific[(i,number)]
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

# Vérifications de forme et des preuves, sans prétention de validation juridique.
allowed_tags = {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
from html.parser import HTMLParser
class XMLCheck(HTMLParser):
    def handle_starttag(self, tag, attrs):
        assert tag in allowed_tags, tag
        assert all(k in {'rowspan','colspan'} and v.isdigit() for k,v in attrs), attrs
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

assert len(answers) == len(sources) == 12
for source, a in zip(sources, answers):
    for k in ('code_id','source_id','source_sha256','number'):
        assert a[k] == source[k]
    assert a['status'] == 'rewrite_draft' and a['proposed_xml']
    XMLCheck().feed(a['proposed_xml'])
    b = a['substantive_impact']
    assert b['version'] == 1
    for k in ('assessment','scope_limitations','new_burdens_review'):
        assert len(b[k]) >= 40
    if source['benefit_check_required']:
        assert len(a.get('benefit_review','')) >= 100
    if a.get('change_type') == 'full_repeal':
        assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé'))
        assert len(a['repeal_scope']) >= 30
    if a.get('change_type') == 'normative_reduction':
        assert all(len(x) >= 30 for x in a['removed_provisions'])
    seen = set()
    seen_measures = set()
    for e in b['effects']:
        pair = (e['measure_id'],e['kind'])
        assert pair not in seen, (a['number'], pair)
        assert e['measure_id'] not in seen_measures, (a['number'],e['measure_id'])
        seen.add(pair)
        seen_measures.add(e['measure_id'])
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        for q,k in [('source_quote','source_xml'),('proposed_quote','proposed_xml')]:
            quote = e[q]
            target_text = plain(source[k] if k == 'source_xml' else a[k])
            assert len(quote) >= 12 and quote in target_text, (a['number'],q,quote)
    key = a['code_id']+'|'+a['source_id']
    assert [c['target_key'] for c in a['reference_checks']] == references['requirements'][key]
    for c in a['reference_checks']:
        assert c['view_sha256'] == references['targets'][c['target_key']]['view_sha256']
        assert len(c['assessment']) >= 80

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'output_file':'answer.json','article_count':len(answers)},ensure_ascii=False))
