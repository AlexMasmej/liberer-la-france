import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
references = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


def replace_once(text, before, after):
    assert text.count(before) == 1, (before, text.count(before))
    return text.replace(before, after, 1)


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, proposed, reason, notes, substantive, removed=None, benefit=None,
        repeal_scope=None):
    source = by_number[number]
    a = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft',
             substantive_impact=substantive)
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal_scope:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal_scope)
    if benefit:
        a['benefit_review'] = benefit
    a['reference_checks'] = []
    answers[number] = a
    return a


# 237 bis A : les vingt alinéas d'origine sont conservés, sauf les coupes indiquées.
p = by_number['237 bis A']['source_xml']
p = replace_once(p,
    "sont déductibles pour l'assiette de l'impôt sur les sociétés ou de l'impôt sur le revenu exigible au titre de l'exercice au cours duquel elles sont réparties entre les salariés. L'application de cette disposition est subordonnée au dépôt de l'accord de participation à la direction départementale du travail et de l'emploi du lieu où cet accord a été conclu.",
    "sont déductibles pour la détermination du bénéfice imposable à l'impôt sur les sociétés ou à l'impôt sur le revenu au titre de l'exercice au cours duquel elles sont réparties entre les salariés.")
p = replace_once(p, 'peut, sur autorisation du ministre chargé des finances, transférer', 'peut transférer')
p += """<p>V. – À compter de l'entrée en vigueur de la présente loi, la déduction prévue au I n'est plus subordonnée au dépôt de l'accord auprès de l'administration du travail. Les obligations de dépôt résultant du code du travail conservent leur régime propre ; leur seule méconnaissance ne suffit pas à écarter cette déduction lorsque ses conditions de fond sont remplies. Aucun dépôt fiscal, récépissé ou justificatif spécial ne remplace la condition supprimée. Le transfert prévu au 6 du II est réalisé sans autorisation administrative préalable, dans les limites résultant du même II et du IV.</p>
<p>Ces suppressions s'appliquent aux déductions et transferts effectués à compter de cette entrée en vigueur, y compris au titre d'accords ou de plans antérieurs. Les demandes d'autorisation encore pendantes à cette date deviennent sans objet, sans nouvelle demande. Les droits, dettes, restitutions et recours relatifs aux déductions et transferts antérieurs restent régis par les dispositions qui leur étaient applicables.</p>
<p>Pour les bénéfices relevant de l'impôt sur les sociétés à la distribution, les déductions, provisions et reprises prévues au présent article sont prises en compte une seule fois dans le résultat fiscal de référence et dans les bénéfices correspondants. Ni la clôture de l'exercice, ni la répartition aux salariés de sommes réellement dues au titre des dispositifs visés par le présent article, ni la seule reprise d'une provision n'entraînent l'exigibilité de cet impôt sur les bénéfices conservés dans l'entreprise. Les conditions et délais propres aux provisions demeurent applicables à leur qualification fiscale ; ils n'imposent pas un délai d'investissement aux autres bénéfices conservés.</p>
<p>Les fractions définitivement exonérées et les bénéfices déjà soumis à l'impôt sur les sociétés conservent leur protection lors d'une distribution ultérieure ; une provision dont l'imposition est seulement différée n'est pas réputée définitivement exonérée. Une même somme ne peut procurer deux déductions, être transférée deux fois ou être imposée deux fois. Les règles de l'impôt sur le revenu et les régimes d'imposition distincts conservent leur champ.</p>"""
add('237 bis A', p,
    "Réforme de fond : retrait de la condition fiscale de dépôt de l'accord et de l'autorisation ministérielle de transfert du droit à provision du II, 6, sans déclaration équivalente. Coordination nécessaire de l'exercice de déduction avec l'IS à la distribution : le résultat de référence subsiste, sans IS ordinaire sur les bénéfices conservés. Les vingt alinéas sources sont maintenus pour le reste, notamment les droits historiques des II, 1 et 2, leur extinction au IV et le régime encore ouvert du II, 3 ; aucun avantage expiré n'est présenté comme un droit nouveau.",
    "I : suppression de la seule condition fiscale, non du dépôt autonome prévu par le droit du travail ; la direction départementale citée dans la source n'est pas remplacée par un nouveau guichet fiscal. II : 50 %, 25 %, moitié, 35 %, 75 %, seuil de cent salariés, durée de deux ans du fonds, seuils de capital, septième année, intérêts de 1727 et délais de deux/quatre ans conservés. II, 6 : l'autorisation est supprimée dans le seul champ qui demeure ouvert après le IV ; ce n'est pas une extension générale des provisions depuis 2012. Les délais de provision conditionnent un avantage particulier et ne rétablissent pas l'IS annuel. Le 223 A fourni est un projet de regroupement de paiement, différent du droit officiel d'intégration : le calcul et le transfert internes de provision restent expressément opérants. Le suivi du résultat est coordonné avec les XI à XIII de 209 et les V et VI de 219 consultés dans le corpus, sans nouveau renvoi numéroté. Les anciens bénéfices déjà taxés et les provisions seulement différées sont distingués. La note de 2024 fixe le droit source au 1er janvier 2025, non la date de la présente réforme. Les textes réglementaires du dépôt fiscal et du visa de transfert doivent être alignés, sans prétendre les avoir tous réécrits.",
    impact('material_reduction',
        "Deux conditions fiscales expresses disparaissent : dépôt de l'accord comme préalable à la déduction et visa du transfert de provision. Les déductions et franchises subsistent ; la coordination d'exigibilité ne constitue pas une nouvelle abolition d'IS.",
        "Les dépôts et protections autonomes du code du travail restent dus. Le visa de transfert n'est retiré que pour les droits encore utilisables après le IV. Le coût administratif et fiscal net n'est pas chiffré.",
        "Aucune charge nouvelle identifiée : aucun dépôt de remplacement ni nouvel état n'est créé. Le calcul unique des déductions et la distinction des provisions utilisent les comptes fiscaux du régime de distribution déjà coordonné.", [
            effect('relief_extended', 'participation-fin-condition-depot-fiscal',
                "Extension de la déduction aux situations où le dépôt manque, sans suppression du dépôt social autonome.",
                "La déduction des sommes de participation est conditionnée au dépôt auprès de la direction départementale du travail et de l'emploi.",
                "La déduction est ouverte si ses conditions de fond sont remplies ; l'absence de dépôt ne suffit plus à la refuser. Les taux et assiettes de l'IR et de l'IS ne sont pas fixés par cette coupe.",
                'other', "Entreprises répartissant une réserve spéciale de participation à leurs salariés.",
                "Déductions effectuées dès l'entrée en vigueur, y compris pour les accords antérieurs ; anciennes dettes et voies de recours conservées.",
                "Aucun dépôt fiscal ni récépissé de remplacement ; le dépôt autonome du code du travail n'est pas aboli.",
                "L'application de cette disposition est subordonnée au dépôt de l'accord de participation à la direction départementale du travail et de l'emploi du lieu où cet accord a été conclu.",
                "la déduction prévue au I n'est plus subordonnée au dépôt de l'accord auprès de l'administration du travail."),
            effect('authorization_removed', 'participation-transfert-provision-sans-visa',
                "Suppression du visa ministériel pour transférer le droit à provision dans le groupe éligible.",
                "Le transfert du droit à provision du II, 6 exige l'autorisation du ministre des finances, sous la restriction du IV aux provisions du II, 3.",
                "Le transfert respecte les mêmes limites de contribution et de groupe, sans autorisation administrative préalable ; aucune provision expirée n'est rouverte.",
                'legal_duty', "Sociétés du groupe titulaires de droits à provision encore admis après le IV.",
                "Transferts futurs et demandes encore pendantes ; droits antérieurs conservés.",
                "Aucune déclaration ni seconde décision administrative substituée au visa supprimé.",
                "chacune de ces sociétés peut, sur autorisation du ministre chargé des finances, transférer tout ou partie de son droit à constitution de ladite provision",
                "Le transfert prévu au 6 du II est réalisé sans autorisation administrative préalable, dans les limites résultant du même II et du IV.")]),
    removed=[
        "La condition fiscale du I subordonnant la déduction de participation au dépôt de l'accord à l'administration du travail est supprimée pour les déductions futures.",
        "L'autorisation préalable du ministre des finances pour les transferts de droit à provision au II, 6 est supprimée dans le champ maintenu par le IV."
    ],
    benefit="La déduction de la participation du I demeure ouverte aux répartitions futures éligibles, sans sanction fiscale fondée sur le seul défaut de dépôt. Les provisions des II, 1 et 2 conservent tous leurs taux historiques de 25 %, 50 %, 35 % ou 75 %, leur réduction de moitié et leurs conditions pour les périodes auxquelles elles restent applicables ; le IV n'est ni effacé ni étendu. Le II, 3 demeure ouvert aux futures SCOP éligibles, y compris les exceptions de capital, transformations avec engagement sur sept ans et groupements de SCOP ; les dotations de réserve légale et de fonds de développement restent utilisables. Les délais de deux ou quatre ans, l'emploi en formation, la contribution effective et les transferts des II, 4 à 6 subsistent, avec suppression du seul visa du 6. Une exonération devenue définitive reste protégée à la distribution et les bénéfices déjà taxés ne subissent pas un second IS ; une provision temporaire n'est pas assimilée à une exonération définitive. Les droits des salariés ne dépendent ni d'un seuil d'ancienneté de rupture ni du type ancien de contrat.")

add('237 ter', None,
    "Maintien intégral utile après examen : l'article ouvre la déduction des versements de l'entreprise aux plans d'épargne légalement constitués et n'impose ni agrément, déclaration, délai minimal ou pièce fiscale supplémentaire. Supprimer ce texte ferait perdre un avantage alors que l'IR et l'IS à la distribution subsistent. Le titre III visé est celui de l'épargne salariale, sans exigence de CDD ni seuil d'indemnité de rupture.",
    "Le bénéfice est conservé pour les versements futurs éligibles et les droits antérieurs. La déduction du bénéfice ne constitue pas, par elle-même, un fait générateur annuel d'IS : les résultats de référence sont maintenus par le régime de distribution de 209/219. Les trois cibles de travail fournies ont été examinées ; aucun renvoi direct à leurs règles de contrat, préavis ou indemnité n'existe ici. La note d'ordonnance de 2007 est une concordance de la source, non un calendrier de réforme.",
    impact('retained_necessary',
        "La déduction fiscale des versements d'épargne salariale est maintenue entière ; aucune nouvelle réduction de prélèvement ou formalité supprimée n'est revendiquée.",
        "Le montant et les conditions des plans restent régis par le titre III du code du travail. Le maintien ne chiffre pas l'incidence globale de l'IS à la distribution ni celle des plans.",
        "Aucune charge nouvelle identifiée : aucun nouveau corps, formulaire, dépôt ou condition d'emploi ne remplace la déduction conservée."))

p = by_number['237 ter A']['source_xml']
p += """<p>III. – Pour les exercices relevant de l'impôt sur les sociétés à la distribution, les sommes déductibles en application des I et II restent prises en compte une seule fois dans le résultat fiscal de référence et dans les bénéfices correspondants. Les versements qui remplissent les conditions du I et les dividendes d'actions de travail qui bénéficient du II ne constituent pas, pour l'entreprise qui les verse, une distribution de bénéfices imposable à ce titre du seul fait de leur versement ou de leur dénomination. Cette règle ne s'étend pas aux dividendes des actions de capital ni aux avantages personnels dissimulés et ne modifie pas la fiscalité propre des bénéficiaires. Elle ne rend pas l'impôt exigible sur les bénéfices conservés et ne permet pas deux déductions d'une même somme.</p>
<p>Les dispositions des I et II demeurent applicables aux exercices antérieurs, ainsi qu'aux droits, dettes, restitutions, prescriptions et recours qui s'y rapportent.</p>"""
add('237 ter A', p,
    "Coordination nécessaire : maintien intégral des I et II et ajout d'une règle empêchant le nouvel IS à la distribution de traiter comme un dividende de capital les actions de travail déjà admises au régime de l'intéressement. La déduction de l'intéressement payé en espèces et son extension aux sociétés anonymes à participation ouvrière sont conservées sans double déduction. Le renvoi aux premier et troisième alinéas de L3315-1 garde ses exclusions propres ; aucune formalité autonome ne justifie une coupe dans ce texte favorable.",
    "L3315-1 a été lu dans le corpus : son premier alinéa ouvre la déduction des espèces versées ; son troisième exclut exploitants individuels, associés de sociétés de personnes non soumises à l'IS et conjoints collaborateurs ou associés. Ces exclusions propres ne sont pas modifiées par le contrat unique. L'extension aux actions de travail depuis le 1er janvier 1991 n'est pas confondue avec le dividende ordinaire d'un associé : une précision expresse est nécessaire face au nouveau fait générateur de l'IS. Les dépenses sont retenues une seule fois dans le résultat de référence ; l'article ne rend pas l'impôt annuel exigible. Les dividendes de capital, avantages dissimulés et impôts personnels restent distincts. Aucun renvoi numéroté nouveau, changement de taux ou de droits sociaux n'est ajouté.",
    impact('coordination_only',
        "L'avantage d'intéressement et l'assimilation favorable des actions de travail sont préservés face au nouveau fait générateur de distribution ; ce maintien explicite n'est pas une seconde réduction d'IS.",
        "Les personnes exclues par le troisième alinéa de L3315-1 restent hors de cet avantage ; la règle ne couvre pas les actions de capital ni les avantages dissimulés et ne modifie pas la fiscalité personnelle des bénéficiaires.",
        "Aucune charge nouvelle identifiée : aucune pièce, déclaration, condition d'ancienneté ou autorisation nouvelle n'est créée ; la prise en compte unique utilise les calculs fiscaux existants.", [
            effect('coordination', 'is-distribution',
                "Préservation de la qualification déductible de l'intéressement et des dividendes d'actions de travail sous le nouvel IS.",
                "Le I déduit l'intéressement en espèces sous L3315-1 ; le II applique cette déduction aux dividendes des actions de travail depuis 1991.",
                "Même déduction dans le résultat de référence, sans IS de distribution du seul fait de ces versements qualifiés ; les dividendes de capital restent distincts, sans changement de taux personnel.",
                'other', "Entreprises versant l'intéressement éligible et sociétés anonymes à participation ouvrière pour les seules actions de travail.",
                "Exercices relevant de l'IS à la distribution ; source entière maintenue pour les exercices et droits antérieurs.",
                "Aucun document ou registre nouveau ; pas de double déduction ni d'extension aux dividendes ordinaires.",
                "les dividendes des actions de travail qui sont attribuées aux salariés des sociétés anonymes à participation ouvrière régies par la loi du 26 avril 1917 bénéficient des dispositions du I.",
                "Les versements qui remplissent les conditions du I et les dividendes d'actions de travail qui bénéficient du II ne constituent pas, pour l'entreprise qui les verse, une distribution de bénéfices imposable à ce titre du seul fait de leur versement ou de leur dénomination.")]))

p = """<p>Les dons reçus par une entreprise ayant subi un sinistre survenu à la suite d'une catastrophe naturelle constatée par arrêté pris en application de l'article L. 125-1 du code des assurances ou d'un événement ayant des conséquences dommageables ne sont pas pris en compte pour la détermination des résultats imposables.</p>
<p>Pour les dons reçus à compter de l'entrée en vigueur de la présente loi, l'exclusion relative à un événement ayant des conséquences dommageables ne requiert aucun arrêté particulier ni aucun agrément fiscal préalable. La réalité du sinistre et la réception du don peuvent être établies par tout moyen dans les conditions du contrôle fiscal de droit commun, sans attestation spéciale ni déclaration supplémentaire. Aucune condition nouvelle d'affectation du don n'est imposée.</p>
<p>Cette exclusion demeure applicable aux bénéfices relevant de l'impôt sur les sociétés à la distribution : le don ainsi exclu n'entre pas dans l'assiette de cet impôt lors d'une distribution ultérieure et ne peut être exclu deux fois. Les dons reçus avant l'entrée en vigueur restent régis par les dispositions qui leur étaient applicables, y compris les déductions transitoires, restitutions, prescriptions et recours.</p>"""
add('237 quater', p,
    "Réforme de fond favorable : la non-imposition des dons reçus par les entreprises sinistrées devient directement applicable sans arrêté contresigné par le ministre du budget. La constatation des catastrophes naturelles par l'arrêté d'assurance demeure une voie d'éligibilité, mais les autres événements dommageables ne nécessitent plus une reconnaissance fiscale discrétionnaire. La réalité du sinistre et la réception du don restent contrôlables par les preuves ordinaires, sans procédure de remplacement ni nouvelle condition d'affectation.",
    "L'exclusion de résultat vaut pour l'IR et pour l'IS ; elle demeure définitive lors de la distribution du montant exonéré, sans double exclusion. Le renvoi existant à L125-1 du code des assurances est maintenu dans son champ assurantiel ; son texte n'est pas fourni dans reference-targets et aucune modification de son régime n'est affirmée. La note source conserve son rôle pour les exercices ouverts depuis 2002 et les dons 1999–2001 déductibles du premier exercice ouvert à compter du 1er janvier 2002 ; ces périodes ne datent pas la réforme. Les nouveaux dons peuvent être liés à un événement antérieur. Les dispositions d'application et arrêtés de reconnaissance fiscale doivent être rendus compatibles ; aucune nouvelle procédure d'agrément ou de déclaration ne doit être réintroduite. Le coût de l'élargissement n'est pas chiffré.",
    impact('material_reduction',
        "La reconnaissance ministérielle propre aux événements dommageables autres que la voie des catastrophes naturelles cesse de conditionner l'exonération ; les futurs dons éligibles peuvent en bénéficier directement.",
        "L'allègement porte sur les dons reçus après la bascule. Il ne supprime ni le contrôle des faits, ni les impôts sur les autres produits, ni les conditions assurantielles autonomes ; la perte de recettes est inconnue.",
        "Aucune charge nouvelle identifiée : la preuve libre du sinistre et du don remplace l'arrêté sans attestation, dépôt ou agrément nouveau ; les preuves ordinaires des produits restent disponibles pour le contrôle.", [
            effect('relief_extended', 'dons-sinistres-fin-reconnaissance-fiscale',
                "Retrait de l'arrêté fiscal conditionnant l'exclusion des dons liés à un événement dommageable.",
                "Hors catastrophe naturelle constatée, un événement dommageable doit être mentionné dans un arrêté contresigné par le ministre du budget pour ouvrir l'exclusion du résultat imposable.",
                "Le sinistre et la réception du don sont des faits démontrables sans décision fiscale préalable ; les dons correspondants sont exclus de l'assiette IR/IS, sans modification de leurs taux ni nouvelle condition d'affectation.",
                'other', "Entreprises sinistrées recevant des dons après un événement dommageable.",
                "Dons reçus à compter de l'entrée en vigueur ; ancien droit et ses déductions transitoires conservés pour les dons anciens.",
                "Aucun arrêté particulier, agrément, formulaire ou attestation de remplacement.",
                "ou d'un événement ayant des conséquences dommageables, mentionné par un arrêté contresigné par le ministre du budget pris en application du présent dispositif,",
                "l'exclusion relative à un événement ayant des conséquences dommageables ne requiert aucun arrêté particulier ni aucun agrément fiscal préalable.")]),
    removed=["La nécessité d'un arrêté contresigné par le ministre du budget identifiant l'événement dommageable est supprimée pour l'exclusion fiscale des dons futurs liés à cet événement."])

add('237 sexies', None,
    "Maintien intégral utile de la règle spéciale de rattachement à l'encaissement des pénalités reçues et au paiement des pénalités versées. Elle évite notamment d'imposer un produit de retard non encaissé et conserve la symétrie des charges. Elle ne crée ni déclaration, autorisation ni délai d'attente propre ; son abrogation rétablirait une contrainte d'acquisition des produits défavorable.",
    "Les deux subdivisions et le champ historique des créances et dettes nées à compter de l'entrée en vigueur de la loi du 15 mai 2001 sont maintenus. Les renvois à L441-9 et au II de L441-10 du code de commerce restent les pénalités commerciales, sans rapport avec le préavis individuel ou une pénalité fiscale. Ces cibles extérieures ne sont pas fournies dans reference-targets ; aucun contenu nouveau ne leur est attribué. Le rattachement au résultat de référence pour l'IS à la distribution ne rend pas cet impôt annuel exigible et ne constitue pas un nouveau report d'impôt accordé par ce lot.",
    impact('retained_necessary',
        "La règle de caisse favorable pour les produits de pénalités de retard est préservée avec son volet charges. Aucun report supplémentaire ni nouvelle suppression n'est revendiqué.",
        "La règle porte sur les pénalités commerciales du champ cité et sur leur rattachement fiscal ; elle ne supprime pas les pénalités elles-mêmes ni les obligations de paiement des dettes.",
        "Aucune charge nouvelle identifiée : le maintien reprend exactement les deux subdivisions, sans nouveau registre, justificatif ou calendrier déclaratif."))

add('237 septies', None,
    "Maintien intégral nécessaire après examen de ses deux mécanismes : l'étalement historique du changement de méthode par composants, avec faculté de renonciation sous 150 000 €, et l'interdiction d'un nouvel amortissement des anciennes charges à répartir déjà transférées à l'actif. Supprimer indistinctement le II pourrait permettre une seconde déduction des mêmes charges ; il conserve la correction corrélative des plus ou moins-values et ses exceptions favorables.",
    "I : premier exercice ouvert à compter du 1er janvier 2005, cinq parts égales, seuil de 150 000 € et option de renonciation conservés. II : champ des transferts depuis les exercices ouverts en 2004, exclusion des droits de mutation, honoraires, commissions et frais d'actes, et correction de l'article 39 duodecies conservés. Les immobilisations encore détenues peuvent rendre ces dispositions historiques utiles ; aucun stock résiduel nul n'est présumé. Le III n'habilite qu'à l'application du I et ne crée aucune autorisation particulière. Les résultats de référence de l'IS nouveau n'entraînent pas de paiement annuel au seul titre de cet article.",
    impact('retained_necessary',
        "Les modalités transitoires et l'absence de double amortissement restent entières, avec leur option et leurs exceptions. Aucune simplification ou baisse nouvelle n'est établie par ce maintien.",
        "L'existence et le montant des immobilisations historiques encore concernées ne sont pas connus ; l'examen de cet article ne démontre pas l'extinction de ses effets sur les futures cessions.",
        "Aucune charge nouvelle identifiée : les calculs historiques sont conservés sans nouvel état, registre, délai ni justificatif ajouté."))

add('238-0 A', None,
    "Maintien intégral nécessaire de la définition et des modalités de classement des Etats et territoires non coopératifs. Les critères de transparence, la motivation du classement et les voies de retrait ont une fonction de lutte contre la fraude et de sécurité juridique qui subsiste sous l'IS à la distribution. L'arrêté et sa mise à jour ne sont pas des agréments individuels imposés aux entreprises et ne sont pas retirés au titre des formalités économiques.",
    "Les 1, 2 a à c, 2 bis 1°/2°, 2 ter et 3 sont conservés, notamment les douze conventions, dates de 2009/2010/2017, délai d'ajout au premier jour du troisième mois et cessation dès publication du retrait. Les conditions de sortie et ce délai protecteur demeurent pour les classements futurs aussi. Le classement européen cité reste distinct d'une taxe nationale : l'article ne prouve pas à lui seul qu'un prélèvement particulier est exigé par le droit de l'Union. Aucune liste actuelle n'a été recherchée à l'extérieur. La note de 2018 est historique ; elle ne fixe pas la date de la réforme. Aucun renvoi rendu vide par le contrat unique ou les successions n'est identifié.",
    impact('retained_necessary',
        "La définition anti-fraude et les garanties de calendrier et de retrait sont maintenues. Aucun prélèvement ou devoir déclaratif individuel supplémentaire n'est institué ni supprimé dans cet article.",
        "Le maintien ne vérifie pas la liste administrative des Etats actuellement classés ni tous les usages de cette définition dans les autres impôts ou conventions.",
        "Aucune charge nouvelle identifiée : critères, consultations, mise à jour et délais restent exactement ceux de la source, sans nouvelle collecte auprès des entreprises."))

p = by_number['238 A']['source_xml']
ending = "si elles y avaient été domiciliées ou établies.</p>"
p = replace_once(p, ending,
    "si elles y avaient été domiciliées ou établies. Lorsque l'impôt français de droit commun est exigible à la distribution, cette comparaison est effectuée en supposant que les bénéfices ou revenus considérés sont intégralement distribués, selon les taux, assiettes, exonérations et autres avantages de droit commun qui leur seraient applicables en France. Cette hypothèse de comparaison ne crée aucune obligation de distribution et ne rend pas exigible un impôt sur les bénéfices effectivement conservés dans une entreprise.</p>")
p += """<p>La précision apportée au deuxième alinéa pour l'impôt à la distribution s'applique aux comparaisons afférentes aux exercices relevant de ce régime. Les exercices antérieurs restent régis par les dispositions qui leur étaient applicables. Les preuves des opérations réelles, de leur caractère normal et, dans le cas du troisième alinéa, de leur objet et effet principalement autres que la localisation dans un Etat ou territoire non coopératif, ainsi que l'exception des emprunts antérieurs au 1er mars 2010 ou assimilables à ceux-ci, demeurent inchangées.</p>"""
add('238 A', p,
    "Coordination nécessaire, sans nouvelle réduction comptée : la comparaison avec la fiscalité française doit rester opérante alors que l'IS ordinaire français devient exigible à la distribution. La référence hypothétique est le même bénéfice intégralement distribué, avec les taux et avantages applicables ; l'absence de distribution réelle ne transforme pas artificiellement toute référence française en zéro. Les quatre alinéas sources sont autrement conservés, avec la preuve des dépenses réelles et normales, la clause de sauvegarde ETNC et l'exception des emprunts anciens.",
    "La différence d'au moins 40 % demeure. La référence ne rétablit ni l'ancien taux français ordinaire de 25 % pour les exercices nouveaux, ni une annualité sur les bénéfices conservés ; les avantages français de droit commun sont pris en compte. La comparaison au régime étranger reste faite sur les impôts qui y sont dus selon son droit, sans inventer un taux étranger. Le renvoi existant à 238-0 A a été vérifié sur la source entière et maintenu : le classement, son calendrier et la clause probatoire du troisième alinéa sont distincts. La preuve de réalité/normalité et d'objet principalement différent protège la lutte contre la fraude tout en permettant les opérations licites ; aucune suppression arbitraire de ces sauvegardes n'est retenue. La note du 1er janvier 2020 reste un historique. Les textes d'application et conventions fiscales doivent être contrôlés pour la comparabilité temporelle ; aucune conformité conventionnelle générale n'est présumée.",
    impact('coordination_only',
        "La référence française du seuil de régime privilégié est adaptée à l'IS à la distribution. Ce changement de comparateur ne supprime ni la preuve ni une taxe distincte et ne compte pas comme une seconde baisse d'IS.",
        "Le résultat de la comparaison dépend des assiettes et avantages de chaque situation française et étrangère. Son incidence nette et l'articulation des conventions ne sont pas chiffrées ni entièrement établies ici.",
        "Aucune nouvelle déclaration, pièce, autorisation ou condition d'ancienneté n'est créée. Le calcul comparatif existant emploie désormais une distribution hypothétique ; aucun paiement ni distribution réelle n'est imposé à ce titre.", [
            effect('coordination', 'is-distribution',
                "Adaptation du comparateur français pour caractériser un régime fiscal privilégié.",
                "Comparaison au montant d'impôt de droit commun qui aurait été dû en France sur les mêmes bénéfices ou revenus ; seuil d'écart de 40 % ou plus.",
                "Lorsque la France impose à la distribution, calcul de la référence sur une distribution intégrale hypothétique avec taux, assiettes et avantages applicables ; même seuil de 40 %, sans fait générateur français ajouté.",
                'other', "Débiteurs français des paiements étrangers et versements sur comptes entrant dans les premier, troisième et quatrième alinéas.",
                "Exercices entrant dans le nouveau régime seulement ; anciennes comparaisons et exception des emprunts antérieurs au 1er mars 2010 conservées.",
                "Pas de nouvelle formalité ; maintien du calcul et des preuves antérieurs, sans IS sur le bénéfice conservé.",
                "dont le montant est inférieur de 40 % ou plus à celui de l'impôt sur les bénéfices ou sur les revenus dont elles auraient été redevables dans les conditions de droit commun en France",
                "cette comparaison est effectuée en supposant que les bénéfices ou revenus considérés sont intégralement distribués, selon les taux, assiettes, exonérations et autres avantages de droit commun qui leur seraient applicables en France.")]))

# 238 bis : conservation textuelle de toutes les autres dispositions.
p = by_number['238 bis']['source_xml']
p = replace_once(p,
    "Ces organismes délivrent aux fonds de dotation une attestation justifiant le montant et l'affectation des versements effectués à leur profit.",
    "Le montant et l'affectation des versements effectués à leur profit sont établis par les pièces ordinaires permettant d'en justifier, sans attestation distincte obligatoire au profit des fonds de dotation.")
p = replace_once(p,
    "l'excédent de versement donne lieu à réduction d'impôt au titre des cinq exercices suivants,",
    "l'excédent de versement donne lieu à réduction d'impôt au titre des exercices suivants, sans limitation de durée,")
p = replace_once(p,
    "les dons versés aux organismes agréés dans les conditions prévues à l'article 1649 nonies et dont l'objet exclusif est",
    "les dons versés aux organismes dont l'objet exclusif est")
p = replace_once(p,
    "L'agrément est délivré à l'organisme s'il s'engage à respecter continûment l'ensemble des conditions suivantes :",
    "L'organisme bénéficie du présent 4 sans agrément fiscal préalable, dès lors qu'il respecte continûment l'ensemble des conditions suivantes :")
p = replace_once(p,
    "peut également se voir délivrer l'agrément, sous réserve du respect des conditions mentionnées aux 1°, 2°, 4° et 5°",
    "relève également du présent 4, sans agrément fiscal préalable, sous réserve du respect des conditions mentionnées aux 1°, 2°, 4° et 5°")
p = replace_once(p,
    "les organismes agréés en application du présent 4 peuvent également se voir délivrer l'agrément sous réserve qu'elles présentent",
    "les organismes remplissant les conditions du présent 4 bénéficient également de ce dispositif, sans agrément fiscal préalable, sous réserve qu'elles présentent")
p = replace_once(p,
    "L'agrément accordé aux organismes qui le sollicitent pour la première fois porte sur une période comprise entre la date de sa notification et le 31 décembre de la deuxième année qui suit cette date. En cas de demande de renouvellement d'agrément, ce dernier, s'il est accordé, l'est pour une période de cinq ans.",
    "L'application du présent 4 n'est subordonnée ni à une demande initiale ni à un renouvellement périodique. Les conditions de fond sont appréciées pour les dons et aides concernés ; les agréments antérieurement délivrés demeurent utilisables pour établir les éléments qu'ils constatent, sans nouvelle attestation.")
p = replace_once(p,
    "Un décret fixe les modalités d'application du présent article, notamment les dispositions relatives aux statuts des organismes bénéficiaires des dons, les conditions de retrait de l'agrément et les informations relatives aux entreprises aidées que les organismes communiquent au ministre ayant délivré l'agrément.",
    "Un décret fixe les modalités d'application du présent article, notamment les dispositions relatives aux statuts des organismes bénéficiaires des dons, sans rétablir l'agrément supprimé au présent 4, son renouvellement ou la communication d'informations au seul titre de cet agrément. Les obligations de suivi et de contrôle résultant directement des règlements de l'Union européenne mentionnés au présent 4 conservent leur champ.")
p = replace_once(p,
    "4 bis. Ouvrent également droit à la réduction d'impôt les dons et versements effectués au profit d'organismes agréés dans les conditions prévues à l'article 1649 nonies dont le siège est situé dans un Etat membre de l'Union européenne ou dans un autre Etat partie à l'accord sur l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative en vue de lutter contre la fraude et l'évasion fiscales. L'agrément est accordé lorsque l'organisme poursuit des objectifs et présente des caractéristiques similaires aux organismes dont le siège est situé en France répondant aux conditions fixées par le présent article.",
    "4 bis. Ouvrent également droit à la réduction d'impôt les dons et versements effectués au profit d'organismes dont le siège est situé dans un Etat membre de l'Union européenne ou dans un autre Etat partie à l'accord sur l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative en vue de lutter contre la fraude et l'évasion fiscales, lorsque l'organisme poursuit des objectifs et présente des caractéristiques similaires aux organismes dont le siège est situé en France répondant aux conditions fixées par le présent article.")
p = replace_once(p,
    "Lorsque les dons et versements ont été effectués au profit d'un organisme non agréé dont le siège est situé dans un Etat membre de l'Union européenne ou dans un autre Etat partie à l'accord sur l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative en vue de lutter contre la fraude et l'évasion fiscales, la réduction d'impôt obtenue fait l'objet d'une reprise, sauf lorsque le contribuable a produit dans le délai de dépôt de déclaration les pièces justificatives attestant que cet organisme poursuit des objectifs et présente des caractéristiques similaires aux organismes dont le siège est situé en France répondant aux conditions fixées par le présent article.",
    "La réduction prévue au présent 4 bis n'est subordonnée ni à un agrément fiscal préalable de l'organisme ni à la production de pièces justificatives lors du dépôt de la déclaration. Le contribuable doit être en mesure d'établir l'équivalence des objectifs et caractéristiques à la demande de l'administration, dans le cadre du contrôle fiscal de droit commun et du 5 bis. Les agréments déjà délivrés demeurent utilisables comme éléments de preuve, sans renouvellement obligatoire.")
p = replace_once(p,
    "Un décret fixe les conditions d'application du présent 4 bis et notamment la durée de validité ainsi que les modalités de délivrance, de publicité et de retrait de l'agrément.",
    "Un décret précise les conditions d'application du présent 4 bis sans instaurer d'agrément fiscal préalable, de renouvellement ou de dépôt systématique des preuves d'équivalence.")
p = replace_once(p, "les pièces justificatives, répondant à un modèle fixé par l'administration, attestant la réalité des dons et versements.",
    "les pièces justificatives attestant la réalité des dons et versements, sans modèle obligatoire.")
p = replace_once(p,
    "6. Les entreprises qui effectuent au cours d'un exercice plus de 10 000 € de dons et versements ouvrant droit à la réduction d'impôt prévue au présent article déclarent à l'administration fiscale le montant et la date de ces dons et versements, l'identité des bénéficiaires ainsi que, le cas échéant, la valeur des biens et services reçus, directement ou indirectement, en contrepartie.",
    "6. La déclaration supplémentaire des dons et versements qui était prévue au présent 6 est supprimée pour les transmissions dont l'échéance intervient à compter de l'entrée en vigueur de la présente loi, y compris lorsqu'elles concernent un exercice antérieur. Aucun dépôt de rattrapage n'est exigé sur ce seul fondement après cette date. Les déclarations déjà déposées n'ont pas à être refaites.")
p = replace_once(p,
    "Ces informations sont transmises sur un support électronique dans le même délai que celui prévu pour le dépôt de la déclaration de résultats de l'exercice au cours duquel les dons et versements mentionnés au premier alinéa du présent 6 sont effectués, suivant des modalités fixées par décret.",
    "Cette suppression n'emporte ni disparition des éléments nécessaires au calcul de la réduction dans la déclaration fiscale de droit commun ni suppression de la preuve prévue au 5 bis. Aucune déclaration, liste de bénéficiaires ou transmission périodique de remplacement n'est instituée au titre du présent 6.")
p += """<p>9. Les suppressions de formalités et d'agréments prévues aux 1, 4, 4 bis et 5 bis s'appliquent aux dons et versements effectués à compter de l'entrée en vigueur de la présente loi. Les demandes d'agrément relevant exclusivement des 4 ou 4 bis encore pendantes à cette date deviennent sans objet ; la disparition de cette procédure ne fait pas obstacle à l'application directe de la réduction aux futurs versements remplissant les conditions de fond. Les versements antérieurs, leurs droits, contrôles, reprises, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables, sous réserve du 6 et de la loi répressive plus douce dans son champ.</p>
<p>L'absence de limite de durée du report de versements prévu au 3 s'applique aux excédents nés à compter de cette entrée en vigueur et aux excédents dont le délai de report n'est pas expiré à cette date. Elle ne rétablit pas les excédents déjà expirés. Chaque fraction reportée demeure soumise au plafond annuel et à son taux d'origine ; une fraction déjà utilisée pour calculer une réduction ne peut être utilisée une seconde fois. Ce report des versements est distinct du report d'une réduction déjà calculée.</p>
<p>Pour les entreprises relevant de l'impôt sur les sociétés à la distribution, la réduction est constatée au titre des versements ouvrant droit à l'avantage, sans exiger de distribution au cours du même exercice. Son imputation et le report de son solde relèvent de l'article 220 E. Le 8 demeure applicable au résultat fiscal de référence ; un versement ne peut à la fois procurer la réduction du présent article et une déduction du bénéfice. Les associés mentionnés au 7 conservent l'avantage dans les mêmes proportions et conditions.</p>"""
add('238 bis', p,
    "Réforme de fond : suppression des agréments fiscaux et renouvellements des organismes d'aide aux PME du 4 et de la voie d'agrément du 4 bis, avec maintien de toutes leurs conditions matérielles et européennes ; pour ces organismes étrangers, fin du dépôt systématique des preuves à la déclaration, contrôle a posteriori conservé. Suppression de l'état annuel supplémentaire au-delà de 10 000 €, du modèle obligatoire des justificatifs et de l'attestation séparée aux fonds de dotation. L'excédent de versements du 3 reste reportable sans péremption, sous les mêmes plafonds et taux. Les autres catégories, exclusions, calculs et conditions sources sont intégralement maintenus ; il ne s'agit pas d'une simple reformulation du mécénat.",
    "Lecture des 49 paragraphes et de la note en entier. Maintien des a à g, y compris les e bis à e sexies, les six alinéas du f et les renvois internes du g, demeurés exacts. Les agréments du d (ordonnance de recherche de 1958), du f culturel et ceux repris au g ne sont pas supprimés : leur objet de qualification spécifique et de protection du patrimoine n'est pas remplacé par la seule qualité d'organisme d'aide aux PME. Le b et le véhicule de collecte agréé par statuts gardent leur régime distinct. Au 4, la dispense de visa est expresse et les conditions de fond sont continues : 20 % des ressources, exclusions de l'article 35, règlements 651/2014, 2023/2831, 1408/2013 et 717/2014 conservés ; elle ne dispense pas des contraintes européennes de suivi et de contrôle. 1649 nonies a été lu : il règle les agréments légalement requis et ne doit pas réintroduire ceux que le 4 supprime expressément. Mettre en cohérence décrets, arrêtés et formulaires de ces deux agréments et de l'état du 6 ; ces textes ne sont pas déclarés entièrement réécrits. Le plafond d'assiette de 20 000 € ou 5 pour mille, les taux 60/40 %, le seuil 2 millions et les exceptions de l'aide aux personnes restent entiers. La restriction relative à la mode ultra-express et l'anomalie ponctuelle « 2. ; » sont conservées et signalées, sans correction fiscale silencieuse. Le report de dépenses du 3 ne doit pas doubler le report d'impôt déjà coordonné à 220 E, dont source et proposition ont été lues ; ce nouveau renvoi, absent de reference-targets, vise exclusivement l'imputation de la réduction à l'IS. L'ancien délai de cinq exercices n'est pas ressuscité par un formulaire. La métadonnée ABROGE_DIFF avec fin de version au 1er janvier 2027 appelle une coordination de la version législative future non jointe ; aucun achèvement de cette coordination temporelle n'est revendiqué et aucun avantage n'est réservé aux seuls dons passés. La note de 2025 sur les aides depuis 2024 conserve sa portée historique. Aucun solde budgétaire ni conformité européenne générale n'est déduit de la suppression des visas.",
    impact('material_reduction',
        "Le dispositif de mécénat conserve ses réductions, mais perd des visas et renouvellements, l'état annuel supplémentaire et des formes documentaires imposées ; les excédents de versements encore valides cessent d'expirer après cinq exercices.",
        "Les agréments de recherche et de patrimoine, les conditions européennes et les justificatifs de réalité restent dans leur champ. Le coût net, les règlements d'exécution et la succession de version législative de 2027 restent à coordonner.",
        "Aucune charge nouvelle identifiée : les conditions matérielles préexistaient à l'agrément, les preuves ne sont exigées qu'au contrôle et aucun dossier ni état périodique ne remplace les suppressions. Le suivi des reports sert le droit optionnel existant et n'ajoute pas de registre autonome.", [
            effect('authorization_removed', 'mecenat-pme-fin-agrement-fiscal',
                "Retrait de l'agrément initial et du renouvellement périodique des organismes d'aide aux PME et de leurs fédérations éligibles.",
                "Agrément préalable sous 1649 nonies, première période jusqu'au 31 décembre de la deuxième année suivante, puis renouvellement pour cinq ans.",
                "Application directe si les mêmes conditions de gestion, d'aide, de plafonnement et de droit européen sont remplies, sans agrément ni renouvellement.",
                'legal_duty', "Organismes d'aide aux PME, fédérations ou unions éligibles au 4 et entreprises donatrices.",
                "Dons futurs ; demandes pendantes sans objet, agréments antérieurs utilisables comme preuve, droits anciens conservés.",
                "Aucune déclaration ou autorisation de remplacement ; les exigences européennes autonomes subsistent.",
                "L'agrément est délivré à l'organisme s'il s'engage à respecter continûment l'ensemble des conditions suivantes :",
                "L'organisme bénéficie du présent 4 sans agrément fiscal préalable, dès lors qu'il respecte continûment l'ensemble des conditions suivantes :"),
            effect('obligation_removed', 'mecenat-europe-fin-depot-preuves',
                "Suppression du circuit d'agrément et de la production systématique à la déclaration des preuves d'équivalence des organismes européens.",
                "Au 4 bis, agrément ou production des justificatifs d'équivalence au plus tard au dépôt de la déclaration, à défaut reprise de la réduction.",
                "Même territoire et mêmes caractéristiques éligibles ; preuve d'équivalence à la demande dans le contrôle ordinaire, sans agrément ni dépôt systématique.",
                'legal_duty', "Donateurs à des organismes UE ou EEE conventionnés remplissant les caractéristiques équivalentes.",
                "Versements futurs ; pas de réouverture générale des réductions anciennes définitivement perdues.",
                "La preuve substantielle existait déjà ; aucune nouvelle pièce spécifique ou procédure ne la remplace.",
                "sauf lorsque le contribuable a produit dans le délai de dépôt de déclaration les pièces justificatives attestant que cet organisme poursuit des objectifs et présente des caractéristiques similaires",
                "La réduction prévue au présent 4 bis n'est subordonnée ni à un agrément fiscal préalable de l'organisme ni à la production de pièces justificatives lors du dépôt de la déclaration."),
            effect('obligation_removed', 'mecenat-fin-etat-annuel-supplementaire',
                "Suppression de l'état électronique annuel supplémentaire des dons dépassant 10 000 €.",
                "Au-delà de 10 000 € de dons par exercice : déclaration de montant, date, bénéficiaires et contreparties, au délai de la déclaration de résultats.",
                "Aucun état supplémentaire ni liste périodique de remplacement ; calcul de la réduction dans la déclaration de droit commun et preuve au contrôle maintenus.",
                'legal_duty', "Entreprises dépassant 10 000 € de dons et versements éligibles au cours d'un exercice.",
                "Transmissions dont l'échéance survient dès la réforme, même pour un exercice ancien ; aucun nouveau dépôt de rattrapage après la bascule.",
                "Pas de suppression de la déclaration fiscale commune ou de la conservation des pièces de réalité.",
                "Les entreprises qui effectuent au cours d'un exercice plus de 10 000 € de dons et versements ouvrant droit à la réduction d'impôt prévue au présent article déclarent à l'administration fiscale le montant et la date de ces dons et versements, l'identité des bénéficiaires",
                "La déclaration supplémentaire des dons et versements qui était prévue au présent 6 est supprimée pour les transmissions dont l'échéance intervient à compter de l'entrée en vigueur de la présente loi, y compris lorsqu'elles concernent un exercice antérieur."),
            effect('compliance_cost_reduced', 'mecenat-justificatifs-sans-forme-imposee',
                "Fin du modèle justificatif imposé et de l'attestation séparée destinée aux fonds de dotation.",
                "Un modèle administratif de justificatif est imposé au 5 bis ; les organismes doivent délivrer au fonds de dotation une attestation de montant et d'affectation au g, 2°.",
                "Justificatifs de réalité sans modèle obligatoire ; pièces ordinaires de montant et d'affectation sans attestation distincte obligatoire.",
                'legal_duty', "Entreprises donatrices, fonds de dotation et organismes destinataires concernés.",
                "Dons et versements futurs ; pièces anciennes restent utilisables, sans obligation de les refaire.",
                "L'exigence de preuve est conservée ; aucun nouveau registre ni renseignement ajouté.",
                "Ces organismes délivrent aux fonds de dotation une attestation justifiant le montant et l'affectation des versements effectués à leur profit.",
                "Le montant et l'affectation des versements effectués à leur profit sont établis par les pièces ordinaires permettant d'en justifier, sans attestation distincte obligatoire au profit des fonds de dotation."),
            effect('relief_extended', 'mecenat-excedents-versements-sans-peremption',
                "Suppression de la péremption à cinq exercices du report de versements dépassant le plafond annuel d'assiette.",
                "Excédent reportable cinq exercices, sous le plafond annuel 20 000 € ou 5 pour mille du chiffre d'affaires et au taux d'origine de 60 % ou 40 % selon le 2.",
                "Même plafond, mêmes taux et ordre d'imputation, mais report sans limite de durée ; aucune fraction convertie en réduction ne sert deux fois.",
                'other', "Entreprises dont les dons éligibles dépassent le plafond annuel du 3.",
                "Excédents nouveaux et reports non expirés à l'entrée en vigueur, sans résurrection des reports déjà expirés.",
                "Pas de remboursement nouveau, de nouvelle déclaration distincte ni de relèvement du plafond annuel.",
                "l'excédent de versement donne lieu à réduction d'impôt au titre des cinq exercices suivants,",
                "l'excédent de versement donne lieu à réduction d'impôt au titre des exercices suivants, sans limitation de durée,")]),
    removed=[
        "L'agrément fiscal initial, ses renouvellements et la transmission d'informations au seul titre de cet agrément sont supprimés pour les organismes et fédérations du 4.",
        "La voie d'agrément du 4 bis et l'obligation alternative de produire les preuves d'équivalence lors du dépôt de déclaration sont supprimées au profit de la preuve au contrôle ordinaire.",
        "La déclaration électronique annuelle supplémentaire du 6 portant sur les dons dépassant 10 000 € est supprimée, sans état périodique de remplacement ni rattrapage futur.",
        "Le modèle administratif obligatoire des pièces du 5 bis et l'attestation distincte du g, 2° aux fonds de dotation sont supprimés, sans retirer l'obligation de justifier les faits.",
        "La péremption du report d'excédents de versements au terme de cinq exercices est supprimée pour les excédents nouveaux ou encore reportables, sous plafond annuel inchangé."
    ],
    benefit="Toutes les catégories favorables du 1 sont maintenues : intérêt général et épargne de fondation, organismes reconnus, cultes et Alsace-Moselle, enseignement supérieur ou artistique et consulaire, recherche agréée, spectacles et art contemporain, doctorat, exposition universelle, programmes culturels et formations musicales, gestion forestière durable, patrimoine privé ou exploité sous ses conditions, et fonds de dotation redistributifs. Les noms d'entreprises associés aux opérations restent admis ; les dons en nature restent valorisés au coût de revient et le mécénat de salariés conserve le plafond de trois PASS. Les taux 60 % jusqu'à 2 millions et 40 % au-delà restent, ainsi que le 60 % sans consommation de ce seuil pour l'aide aux personnes listée au 2. L'exclusion de la mode ultra-express n'est pas présentée comme un avantage et demeure. Le plafond de 20 000 € ou 5 pour mille le plus élevé est conservé ; les excédents encore valides ne périment plus après cinq exercices, sans double utilisation et sans rétablir ceux déjà expirés. Les aides aux PME et fédérations du 4 conservent l'éligibilité sous les mêmes limites de fond et européennes, sans visa ; les organismes UE/EEE équivalents du 4 bis restent ouverts aux dons futurs, avec preuve au contrôle. Le 5 protège toujours les biens culturels en conflit armé et la représentation française délibérative. Le partage aux associés des entités transparentes du 7 reste entier. Le contrôle de réalité du 5 bis subsiste sans forme imposée, l'état du 6 disparaît, et le non-cumul déduction/réduction du 8 reste. La constatation et le report à l'IS sont articulés avec 220 E, sans exiger de distribution immédiate ni créer de remboursement. Aucune réduction n'est réservée aux seuls dons antérieurs à la réforme.")

p = by_number['238 bis-0 A']['source_xml']
p = replace_once(p,
    'Les versements doivent faire l\'objet d\'une acceptation par les ministres chargés de la culture et du budget.',
    "Les versements doivent faire l'objet d'une acceptation par le ministre chargé de la culture. Aucune acceptation distincte du ministre chargé du budget n'est requise.")
p += """<p>Pour les exercices relevant de l'impôt sur les sociétés à la distribution, la réduction est constatée au titre de l'exercice au cours duquel les versements sont acceptés, même en l'absence de distribution. Elle s'impute sur l'impôt effectivement dû à raison des distributions, dans la limite de 50 % de cet impôt au titre de chaque exercice, apprécié conformément à l'article 219 et, pour les sociétés membres d'un groupe au sens des articles 223 A ou 223 A bis, pour l'ensemble de ce groupe par référence à l'impôt dû par la société mère. Le solde non imputé est reportable sur les exercices suivants sans limitation de durée, sous la même limite annuelle. Le paiement mensuel ne renouvelle pas cette limite. Une même fraction de réduction n'est utilisée qu'une fois ; ce report ne constitue pas une créance remboursable. Les versements demeurent non déductibles du résultat fiscal de référence.</p>
<p>La suppression de l'acceptation budgétaire s'applique aux décisions d'acceptation prises à compter de l'entrée en vigueur de la présente loi, y compris sur les demandes en cours, sans nouveau dépôt ni remise en cause d'une acceptation déjà acquise. Les règles de constatation et de report propres à l'impôt à la distribution s'appliquent aux versements acceptés au cours des exercices relevant de ce régime et aux réductions qui demeurent légalement imputables lors de son ouverture ; elles ne rétablissent pas des droits déjà définitivement perdus. Les versements et impositions antérieurs, ainsi que les restitutions, prescriptions et recours qui s'y rapportent, conservent leur régime.</p>"""
add('238 bis-0 A', p,
    "Réforme de fond : la double acceptation culture/budget est réduite à l'acceptation culturelle, sans déclaration fiscale de remplacement. L'identification des trésors nationaux, l'offre publique d'achat et l'avis motivé pour les autres biens d'intérêt majeur sont conservés. Coordination favorable de la réduction de 90 % avec l'IS à la distribution : constatation sans distribution imposée et solde reportable sans péremption, sous le plafond de 50 % de l'impôt dû et sans double emploi.",
    "Les six alinéas sources sont repris dans leur ordre ; seule la double acceptation est modifiée et les règles nouvelles sont ajoutées après l'habilitation finale. Le renvoi au I de 219 demeure pour les périodes anciennes ; les V et VI du projet de 219 lus dans le corpus définissent le nouvel impôt et le plafond de réduction porte sur cet impôt réellement dû, sans recréer un IS annuel. Le renvoi 223 A fourni a été lu entier en droit officiel et en proposition ; il organise désormais un regroupement de paiement, ce qui impose l'appréciation du plafond au niveau de l'impôt effectivement dû par la mère. Le renvoi existant 223 A bis n'est pas fourni dans reference-targets ; sa source, sa note et sa proposition ont été lues en entier dans le corpus : il concerne les groupes d'EPIC consolidés, dont le projet préserve le périmètre sous le même calendrier de distribution sans IS annuel fictif. Aucune vérification facultative de cette cible n'est ajoutée à reference_checks. Les renvois au patrimoine L111-4/L121-1 conservent leur objet culturel et ne deviennent pas des autorisations fiscales nouvelles. Adapter le décret d'application pour retirer le visa budgétaire et traiter les reports ; ce décret extérieur au lot n'est pas présenté comme réécrit. Aucun rendement ou coût public national n'est inventé.",
    impact('material_reduction',
        "La décision budgétaire supplémentaire disparaît ; la réduction culturelle de 90 % peut être conservée et imputée plus tard lorsque l'IS dépend d'une distribution, sans relever le plafond annuel de 50 %.",
        "L'acceptation culturelle et les qualifications patrimoniales restent requises. Les règlements d'application doivent être alignés sur le retrait du visa budgétaire et les reports ; le coût du report non périssable n'est pas mesuré.",
        "Aucune charge nouvelle identifiée : pas de dossier, registre ou attestation de remplacement du visa budgétaire. Le suivi du solde de réduction évite le double emploi et utilise les déclarations fiscales du régime de distribution.", [
            effect('authorization_removed', 'tresors-nationaux-fin-visa-budget',
                "Suppression de l'acceptation du ministre du budget, en conservant l'acceptation culturelle.",
                "Versements ouvrant droit à la réduction soumis à l'acceptation des ministres de la culture et du budget.",
                "Acceptation du seul ministre de la culture ; les conditions patrimoniales et le taux de 90 % sont inchangés.",
                'legal_duty', "Entreprises finançant les achats de biens culturels éligibles à 238 bis-0 A.",
                "Décisions futures, y compris demandes en cours ; acceptations acquises conservées sans nouveau dépôt.",
                "Pas de déclaration fiscale ou avis budgétaire substitué ; acceptation culturelle maintenue.",
                "Les versements doivent faire l'objet d'une acceptation par les ministres chargés de la culture et du budget.",
                "Les versements doivent faire l'objet d'une acceptation par le ministre chargé de la culture. Aucune acceptation distincte du ministre chargé du budget n'est requise."),
            effect('relief_extended', 'tresors-nationaux-report-reduction-distribution',
                "Conservation de la réduction non imputée lorsque l'impôt est déclenché par la distribution.",
                "Réduction de 90 % imputée sur l'IS de l'exercice d'acceptation, limitée à 50 % de l'impôt de cet exercice, sans report prévu par cet article.",
                "Même taux de 90 % et plafond annuel de 50 % de l'IS dû ; pour les exercices nouveaux, solde conservé sans limite de durée jusqu'aux distributions imposables.",
                'other', "Entreprises éligibles relevant du nouvel IS à la distribution et groupes concernés.",
                "Versements acceptés dans le régime nouveau et réductions légalement encore imputables à son ouverture ; aucun droit déjà perdu n'est rétabli.",
                "Aucune distribution obligatoire ni créance remboursable ; solde suivi une seule fois, plafond annuel non renouvelé chaque mois.",
                "La réduction d'impôt s'applique sur l'impôt sur les sociétés dû au titre de l'exercice au cours duquel les versements sont acceptés.",
                "Le solde non imputé est reportable sur les exercices suivants sans limitation de durée, sous la même limite annuelle.")]),
    removed=[
        "L'acceptation distincte du ministre chargé du budget est supprimée pour les décisions futures, seule l'acceptation culturelle nécessaire à la qualification patrimoniale restant requise.",
        "Pour l'IS à la distribution, la limitation de l'imputation de la réduction au seul exercice d'acceptation est supprimée, avec report du solde sous plafond annuel de 50 % inchangé."
    ])

p = by_number['238 bis AB']['source_xml']
p = replace_once(p,
    "L'entreprise doit inscrire à un compte de réserve spéciale au passif du bilan une somme égale à la déduction opérée en application du premier alinéa. Cette somme est réintégrée au résultat imposable en cas de changement d'affectation ou de cession de l'œuvre ou de l'instrument ou de prélèvement sur le compte de réserve.",
    "L'entreprise n'est pas tenue d'inscrire à un compte de réserve spéciale au passif du bilan une somme égale à la déduction opérée en application du premier alinéa. Les sommes déduites sont réintégrées au résultat imposable en cas de changement d'affectation ou de cession de l'œuvre ou de l'instrument. Leur montant est établi par la comptabilité et les pièces ordinaires justifiant les déductions, sans registre distinct.")
p += """<p>La suppression de la réserve spéciale s'applique aux déductions opérées à compter de l'entrée en vigueur de la présente loi. Les sommes figurant dans une réserve spéciale constituée avant cette date peuvent être prélevées à compter de cette entrée en vigueur sans réintégration au seul motif de ce prélèvement ; les obligations d'exposition, de prêt gratuit et la reprise en cas de changement d'affectation ou de cession demeurent. Les dettes et recours afférents aux prélèvements ou autres faits antérieurs conservent leur régime ; aucune restitution générale n'est instituée.</p>
<p>Pour les bénéfices relevant de l'impôt sur les sociétés à la distribution, les déductions et réintégrations sont prises en compte une seule fois dans le résultat fiscal de référence et dans les bénéfices correspondants. Leur constatation ne requiert pas une distribution et ne rend pas cet impôt exigible sur les bénéfices conservés. Les fractions déjà taxées ou définitivement exonérées conservent leur protection contre une seconde imposition ; une même charge ou déduction ne peut être utilisée deux fois.</p>"""
add('238 bis AB', p,
    "Réforme de fond : suppression de l'inscription et du maintien d'une réserve spéciale au passif, ainsi que de la reprise déclenchée par son seul prélèvement. La déduction sur cinq exercices, le plafond commun avec le mécénat et les contreparties culturelles restent entiers ; la cession ou le changement d'affectation déclenche toujours la reprise. Les comptes et pièces ordinaires suffisent au calcul, sans registre de remplacement. Coordination des déductions et reprises avec le résultat de référence de l'IS à la distribution.",
    "Six alinéas sources intégralement traités ; les premier à quatrième et sixième sont reproduits sans changement. Dates conservées : achats à compter du 1er janvier 2002 et avant le 31 décembre 2028. Cinq fractions égales, exposition publique ou aux salariés hors bureaux pendant l'exercice d'achat et les quatre années suivantes, prêt gratuit des instruments et règle de provision pour dépréciation maintenus. Le renvoi au premier alinéa du 3 de 238 bis a été vérifié sur le texte complet de ce lot : plafond 20 000 € ou 5 pour mille et minoration par les autres versements inchangés. Les reprises pour changement d'affectation ou cession ne sont pas supprimées, seulement leur exigibilité coordonnée à l'IS nouveau ; les exercices antérieurs gardent leurs dettes. Aucune nouvelle cible numérotée n'est ajoutée. Les dispositions d'application et rubriques comptables fiscales de la réserve doivent être alignées, sans transformer les pièces ordinaires en un état autonome. Le coût fiscal de la libération des réserves n'est pas chiffré.",
    impact('material_reduction',
        "La réserve spéciale obligatoire et la reprise fiscale attachée au seul prélèvement sur cette réserve disparaissent ; les obligations d'usage culturel et les reprises pour cession ou changement d'affectation sont conservées.",
        "La suppression n'étend pas la fenêtre d'acquisition au-delà de 2028 et ne modifie pas le plafond annuel ou les cinq fractions. Le gain fiscal dépend des retraits de réserves concernés et n'est pas chiffré.",
        "Aucune charge nouvelle identifiée : l'immobilisation et les preuves des déductions existaient déjà ; aucun registre, déclaration ou autorisation ne remplace le compte de réserve supprimé.", [
            effect('obligation_removed', 'mecenat-art-fin-reserve-speciale',
                "Fin de l'obligation de constituer et maintenir une réserve spéciale pour la déduction d'art et d'instruments.",
                "Inscription au passif d'une réserve égale aux déductions, avec réintégration en cas de prélèvement, même sans cession ou changement d'affectation.",
                "Aucune réserve spéciale imposée ; pas de reprise pour le seul prélèvement. Déduction, immobilisation, exposition ou prêt et reprises pour cession/changement d'affectation maintenus, aux taux d'impôt de droit commun.",
                'legal_duty', "Entreprises déduisant les achats éligibles d'œuvres originales ou d'instruments de musique.",
                "Nouvelles déductions et prélèvements futurs sur réserves anciennes ; prélèvements antérieurs et leurs droits restent soumis à l'ancien régime.",
                "Comptabilité et pièces ordinaires existantes, sans registre distinct ou nouveau dépôt.",
                "L'entreprise doit inscrire à un compte de réserve spéciale au passif du bilan une somme égale à la déduction opérée en application du premier alinéa.",
                "L'entreprise n'est pas tenue d'inscrire à un compte de réserve spéciale au passif du bilan une somme égale à la déduction opérée en application du premier alinéa.")]),
    removed=[
        "L'obligation d'inscrire et de conserver au passif une réserve spéciale égale aux déductions d'œuvres ou instruments est supprimée sans registre spécial de remplacement.",
        "La réintégration fiscale résultant du seul prélèvement sur la réserve spéciale est supprimée pour les prélèvements futurs, y compris sur une réserve constituée antérieurement."
    ])

add('238 bis B', None,
    "Maintien intégral nécessaire de deux exonérations de tous impôts et taxes relatives aux attributions et acquisitions de biens de presse visées par la loi du 2 août 1954 et aux dations en paiement de cette même loi. L'article n'impose aucune autorisation ou déclaration propre. Le caractère historique du dispositif ne démontre pas l'extinction de ses créances ou opérations éligibles ; l'abroger pourrait retirer une immunité alors que des impôts généraux subsistent.",
    "Les renvois aux articles 9/15, au premier alinéa de l'article 1er et aux articles 11/13/24 de la loi de 1954 sont conservés dans leurs objets distincts. Cette loi extérieure n'est pas jointe à reference-targets ; aucun achèvement de sa vérification historique ni extension à des ventes de presse ordinaires n'est affirmé. L'immunité fiscale demeure aussi pour les situations futures recevables dans ce champ légal ; elle n'est pas limitée aux seules opérations déjà payées. La suppression des successions ou l'IS à la distribution ne justifie pas de retirer cette exemption générale et autonome.",
    impact('retained_necessary',
        "Les deux gratuités fiscales autonomes sont maintenues exactement, sans être comptées comme de nouvelles taxes supprimées. Aucun devoir administratif propre n'est à retirer de cet article.",
        "L'existence de futurs règlements éligibles dépend du champ de la loi de 1954 ; l'inventaire de ses situations résiduelles et leur montant ne sont pas établis par cette seule source.",
        "Aucune charge nouvelle identifiée : aucun nouveau corps ni nouvelle condition n'est ajouté aux exonérations conservées."))

p = by_number['238 bis C']['source_xml']
p = replace_once(p,
    "1° Que la répartition intervienne dans un délai maximal d'un an à compter de l'encaissement effectif des sommes reçues au titre de l'indemnité ou de la date de la loi n° 57-198 du 22 février 1957 si l'encaissement a eu lieu antérieurement;",
    "1° Que la répartition porte sur les indemnités effectivement encaissées, sans délai maximal de répartition ;")
p += """<p>III. – La suppression du délai maximal prévue au 1° du I s'applique aux répartitions effectuées à compter de l'entrée en vigueur de la présente loi, y compris lorsque les indemnités ont été encaissées antérieurement ou que l'ancien délai d'un an est déjà expiré. Elle ne remet pas en cause les impositions légalement dues au titre de répartitions antérieures ; leurs contrôles, restitutions, prescriptions et recours restent régis par les dispositions qui leur étaient applicables. L'exonération demeure applicable lorsque l'impôt sur les sociétés est dû à la distribution ; elle ne peut être utilisée deux fois sur une même somme.</p>"""
add('238 bis C', p,
    "Réforme de fond favorable : suppression du délai maximal d'un an qui conditionnait l'immunité des répartitions d'indemnités de nationalisation ou d'expropriation étrangère. L'exonération du règlement initial, la qualité des personnes françaises, l'exploitation directe des établissements à l'étranger et l'imputation aux postes de passif correspondants demeurent. Les répartitions futures restent exonérées même après l'ancien délai, sans régularisation artificielle des impositions antérieures.",
    "I, 1° et 2° et emplacement II « Sans objet » conservés ; ce dernier n'est pas un emplacement « Réservé ». La référence au 22 février 1957 ne subsiste pas comme point de départ d'un délai désormais supprimé et reste disponible dans la source entière. La preuve que les sommes réparties sont celles des indemnités encaissées explicite le même objet, sans exiger de dépôt, de délai minimal ou de document nouveau ; le 2° conserve sa fonction de traçabilité. Les cibles de contrat unique imposées par reference-targets ont été lues : les indemnités sont ici celles de l'expropriation étrangère, non des indemnités salariales. L'absence de délai de répartition ne déclenche pas de distribution et préserve l'exonération lors du fait générateur éventuel de l'IS nouveau. La note de l'ordonnance de 2011 reste une concordance historique. Le coût fiscal de l'extension aux répartitions futures d'anciennes indemnités n'est pas mesuré.",
    impact('material_reduction',
        "L'exonération des répartitions n'est plus perdue au-delà d'un an ; les autres conditions de provenance, de bénéficiaire et de rattachement comptable sont conservées. Il s'agit d'un allègement fiscal de condition, non d'une suppression du régime d'IS.",
        "Seules les indemnités de mesures étrangères et leurs répartitions qualifiées sont visées. Les sommes déjà réparties et imposées avant la réforme ne bénéficient pas d'une restitution générale ; l'effet de recettes reste inconnu.",
        "Aucune charge nouvelle identifiée : la provenance des sommes était déjà inhérente à l'exonération ; aucun document spécifique, déclaration ou autorisation ne remplace le délai supprimé.", [
            effect('relief_extended', 'indemnites-etranger-repartition-sans-delai',
                "Maintien de l'immunité fiscale après suppression du délai maximal de répartition d'un an.",
                "Exonération IR/IS de la répartition limitée aux sommes réparties dans l'année de l'encaissement, ou de la loi du 22 février 1957 pour les encaissements antérieurs.",
                "Exonération IR/IS conservée sans délai maximal pour les mêmes indemnités et destinataires, sous imputation au passif correspondante ; aucun taux général d'IR/IS n'est modifié.",
                'other', "Sociétés françaises ayant exploité directement les établissements étrangers concernés et actionnaires, porteurs de parts ou titulaires de droits similaires.",
                "Répartitions futures, même sur indemnités anciennes et après expiration de l'ancien délai ; impositions des répartitions antérieures préservées.",
                "Aucun dépôt, délai minimal, agrément ni attestation nouveau ; condition comptable du 2° maintenue.",
                "Que la répartition intervienne dans un délai maximal d'un an à compter de l'encaissement effectif des sommes reçues au titre de l'indemnité",
                "Que la répartition porte sur les indemnités effectivement encaissées, sans délai maximal de répartition ;")]),
    removed=["Le délai maximal d'un an après encaissement, ou après la loi du 22 février 1957 pour les encaissements antérieurs, conditionnant l'exonération des répartitions d'indemnités étrangères est supprimé pour les répartitions futures."])

p = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la cotisation sur les boissons alcooliques prévue à l'article L. 245-7 du code de la sécurité sociale.</p>
<p>Aucune interdiction de déduire au titre du présent article ne s'applique à une cotisation afférente à des produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur, cette cotisation étant supprimée pour ces produits. Aucune déduction d'une cotisation inexistante n'est ouverte.</p>
<p>Pour les produits pour lesquels l'accise est devenue exigible avant cette date, les dispositions antérieures du présent article continuent de régir la non-déductibilité de la cotisation, même lorsque son paiement ou l'établissement de l'impôt intervient ultérieurement. Les dettes, restitutions, prescriptions, contrôles et recours relatifs à ces produits demeurent régis par les dispositions qui leur étaient applicables ; aucune restitution générale n'est instituée.</p>
<p>La présente abrogation ne supprime ni l'accise sur les alcools ni ses exonérations, ni les obligations sanitaires ou les autres impôts et cotisations ayant un fondement autonome. Aucun prélèvement, déclaration ou justificatif de remplacement n'est créé.</p>"""
add('238 bis GA', p,
    "Abrogation de coordination, sans seconde baisse comptée : la non-déductibilité du CGI n'a plus d'objet pour la cotisation accessoire sur les boissons alcooliques que le projet du CSS supprime. La frontière reprend l'exigibilité de l'accise, sans faire disparaître la non-déductibilité des cotisations anciennes payées après la réforme. Ce texte ne crée ni déduction fictive ni suppression de l'accise distincte.",
    "Les sources officielles et les propositions de L245-7, L245-8, L245-9, L245-11 et L245-12 ont été lues dans le corpus public en lecture seule ; les propositions sont des projets et non le droit en vigueur. L245-7 source institue la cotisation au-delà de 18 %, L245-8 rattache son exigibilité à l'accise, L245-11 reprend la non-déductibilité ; les projets concordent sur une suppression pour les produits dont l'accise devient exigible après la bascule et la conservation intégrale des anciennes périodes. Le renvoi existant à L245-7 désigne la cotisation dont la loi de suppression fixe la bascule ; aucun nouveau renvoi numéroté n'est ajouté. Cette abrogation ne constate pas à elle seule l'adoption effective de la suppression du CSS ; elle doit entrer en vigueur avec elle. La mesure est dédupliquée sous cotisation-alcools-suppression et n'est pas chiffrée comme une seconde recette perdue. CIBS, santé publique, mineurs, accise et exonérations autonomes restent hors de cette coupe. Aucun nouveau tarif ou calendrier d'indexation n'est inventé.",
    impact('coordination_only',
        "L'article de non-déductibilité est abrogé seulement dans le prolongement de la suppression de la cotisation accessoire ; les produits anciens restent non déductibles et aucun nouvel avantage fictif n'est créé.",
        "La suppression effective du prélèvement repose sur les articles du CSS et leur loi d'entrée en vigueur, non sur cet article du CGI. Les accises et leurs contraintes européennes ne sont pas supprimées ; aucun coût national supplémentaire n'est calculé.",
        "Aucune charge nouvelle identifiée : pas de nouvelle déduction, déclaration ou justification ; la règle ancienne reste utilisable seulement pour les produits antérieurs et les contrôles correspondants.", [
            effect('coordination', 'cotisation-alcools-suppression',
                "Extinction prospective du renvoi CGI de non-déductibilité après suppression de la cotisation correspondante.",
                "Non-déductibilité IR/IS de la cotisation sur les boissons alcooliques prévue par L245-7, conformément à L245-11 ; aucun taux d'impôt propre à cet article.",
                "Pas de cotisation nouvelle ni de déduction fictive après la suppression coordonnée ; non-déductibilité conservée pour les produits dont l'accise était déjà exigible.",
                'other', "Consommateurs entrant dans le champ de la non-déductibilité de la cotisation accessoire sur les boissons alcooliques.",
                "Même date et frontière d'exigibilité que la loi de suppression du CSS ; ancien stock, recours et non-déductibilité maintenus.",
                "Aucun prélèvement ou document de remplacement ; l'accise et les normes sanitaires demeurent.",
                "Le montant de la cotisation perçue sur les boissons alcooliques prévue par l'article L. 245-7 du code de la sécurité sociale n'est pas déductible",
                "Aucune déduction d'une cotisation inexistante n'est ouverte.")]),
    repeal_scope="Abrogation prospective du renvoi fiscal interdisant la déduction de la cotisation accessoire sur les boissons alcooliques, uniquement pour les produits couverts par sa suppression ; maintien de la non-déductibilité et des droits afférents aux produits antérieurs.")


# Contrôles de renvois : exactement les cibles requises, même lorsqu'elles sont inapplicables.
K_GROUP = 'LEGITEXT000006069577|LEGIARTI000048834056'
K_NOTICE = 'LEGITEXT000006072050|LEGIARTI000006901112'
K_CONTRACT = 'LEGITEXT000006072050|LEGIARTI000019071087'
K_SEVERANCE = 'LEGITEXT000006072050|LEGIARTI000035644154'
K_BIC = 'LEGITEXT000006069577|LEGIARTI000033817773'
checks = {
    '237 bis A': {
        K_GROUP: "Le II, 5 vise la réserve globale de participation d'un groupe 223 A et les contributions effectives de chaque société, non une indemnité de rupture. Le droit officiel d'intégration et la proposition de regroupement de paiement ont été distingués : le calcul global et les transferts de provision restent prévus dans cet article, tandis que le seul groupe ne rend pas annuellement exigible l'IS sur les bénéfices conservés. Les conventions et droits antérieurs restent protégés ; aucun seuil d'ancienneté ni notification de rupture n'intervient dans ce renvoi fiscal.",
        K_NOTICE: "L1234-1 règle le préavis de licenciement, anciennement un ou deux mois selon ancienneté et, dans le projet, quinze jours calendaires pour les contrats nouveaux avec protections distinctes. Le I de 237 bis A vise les sommes réparties aux salariés, non un préavis : aucune condition de notification ou ancienneté de rupture ne peut être ajoutée à la déduction. Les préavis anciens et procédures collectives restent hors de cette coupe fiscale.",
        K_CONTRACT: "L1221-2 proposé impose le contrat unique à durée indéterminée aux nouvelles embauches, sans terme de mission ou formation et sans renouvellement créant un CDD. Le présent article ne réserve pas l'épargne salariale aux CDD ou anciens contrats : les futurs salariés éligibles du contrat unique conservent les avantages de participation et de provision, sous les seules conditions fiscales et collectives propres. Les accords historiques ne sont pas des durées d'emploi.",
        K_SEVERANCE: "L1234-9 traite l'indemnité ordinaire patronale : projet nul avant un an à la fin effective avec préavis inclus, puis 0,20 mois sur toute l'ancienneté, fractions par mois complets, plafond six mois et anciennes composantes préservées. Aucune somme du présent article n'est cette indemnité ; ces seuils, la notification et la faute grave ne doivent pas conditionner les déductions de participation. Salaires, congés, dommages et indemnités spéciales restent distincts."
    },
    '237 ter': {
        K_NOTICE: "La cible L1234-1 distingue le préavis des anciens contrats et les quinze jours calendaires des contrats uniques nouveaux. Le titre III de l'épargne salariale auquel renvoie 237 ter ne vise ni cette durée ni une notification de licenciement ; les versements de l'entreprise restent déductibles sans ancienneté de rupture. Aucune procédure collective n'est retirée par ce maintien fiscal.",
        K_CONTRACT: "L1221-2 proposé supprime les nouvelles embauches à terme, en conservant la transition des anciens contrats et en distinguant la durée d'une formation de celle de l'emploi. La déduction des versements au plan d'épargne n'est pas attachée à un CDD : elle reste applicable aux situations futures éligibles du contrat unique sans nouvelle condition de durée ou de terme, et aux versements des anciens plans.",
        K_SEVERANCE: "L1234-9 proposé ouvre l'indemnité ordinaire à un an au terme effectif, préavis compris, puis sur toute l'ancienneté à 0,20 mois par an, mois complets au prorata, plafond six mois ; anciens droits et indemnités spéciales restent séparés. 237 ter déduit des versements d'épargne salariale et ne cite pas cette indemnité : ni ce seuil ni une notification de rupture ne limitent son avantage."
    },
    '237 ter A': {
        K_NOTICE: "Le préavis individuel de L1234-1 et sa transition ne sont pas visés par les premier et troisième alinéas de L3315-1 auxquels renvoie cet article fiscal. La déduction de l'intéressement en espèces ne devient ni une indemnité de préavis ni un droit conditionné par son ancienneté ou sa notification. Les quinze jours nouveaux ne suppriment aucune procédure collective ou protection spéciale par l'effet de ce maintien.",
        K_CONTRACT: "La proposition de L1221-2 réserve les nouveaux emplois au contrat unique indéterminé ; elle ne ferme pas l'intéressement aux salariés ainsi embauchés. Le présent avantage ne comporte aucune condition de CDD à convertir. Les dividendes d'actions de travail et l'intéressement restent régis par leur objet propre, pour les situations futures éligibles comme pour les anciennes, sans terme d'emploi tiré de la durée de l'accord.",
        K_SEVERANCE: "La cible L1234-9 vise la rupture patronale : un an au terme effectif préavis inclus, barème 0,20 mois par année totale au prorata des mois complets et plafond six mois, avec droits anciens et spéciaux séparés. L'intéressement et les actions de travail de 237 ter A ne relèvent pas de ce barème ; aucune ancienneté de rupture ni notification ne leur est imposée. Le troisième alinéa réellement pertinent est celui de L3315-1, lu dans le corpus."
    },
    '238 bis': {
        K_BIC: "Le 4, 5° exclut les entreprises qui exercent principalement une activité visée par l'article 35 ; la source entière de 35 et sa proposition ont été lues. Il s'agit des BIC immobiliers, intermédiaires, locations équipées ou meublées, concessions, navires et opérations financières énumérées, non du contrat de travail. L'option de quinze jours du 8° de 35 porte sur une catégorie fiscale de contrats financiers ; ce n'est pas un préavis salarial. La suppression du visa au 4 ne retire pas cette exclusion de fond ni ne crée de condition d'ancienneté ou de notification."
    },
    '238 bis-0 A': {
        K_GROUP: "La source 223 A organise l'intégration et le projet son remplacement par le regroupement de déclaration/paiement de l'IS à la distribution, avec transition des groupes anciens. Le plafond de 50 % de 238 bis-0 A doit donc porter sur l'IS réellement dû par la mère pour le groupe, sans résultat annuel taxé fictivement ni multiplication de la limite au mois. La réserve culturelle et son report sont appréciés à ce niveau ; aucun seuil d'ancienneté de salarié, notification de rupture ou indemnité ordinaire n'entre dans le renvoi."
    },
    '238 bis C': {
        K_NOTICE: "L1234-1 traite du préavis de licenciement selon ancienneté dans la source, puis des quinze jours calendaires et des contrats anciens dans le projet. Les indemnités de 238 bis C sont allouées à raison d'une expropriation ou nationalisation étrangère : elles ne sont ni des salaires ni des indemnités de préavis. La suppression de l'année de répartition ne change aucune notification de rupture, procédure collective ou durée de préavis.",
        K_CONTRACT: "L1221-2 proposé régit les nouveaux contrats de travail privés indéterminés et préserve les anciens contrats dans leur transition. 238 bis C concerne des mesures prises par un gouvernement étranger contre un établissement exploité à l'étranger ; il n'est pas un régime de CDD privé ou d'agent public. Aucun terme d'emploi, condition d'ancienneté ni contrat unique n'est artificiellement rattaché à son exonération.",
        K_SEVERANCE: "L1234-9 est sans application aux indemnités de nationalisation, expropriation ou mesure similaire étrangères et à leur répartition entre porteurs de droits sociaux. Le seuil proposé d'un an au terme effectif avec préavis inclus et le barème patronal de 0,20 mois par année totale au prorata des mois complets, plafonné à six mois, ne limitent pas ces sommes. L'ancien délai fiscal d'un an supprimé ici n'est pas l'ancienneté de rupture ; indemnités spéciales et droits anciens du travail restent à leur champ."
    }
}
for number, a in answers.items():
    key = a['code_id'] + '|' + a['source_id']
    required = references['requirements'][key]
    assert set(checks.get(number, {})) == set(required)
    a['reference_checks'] = [dict(target_key=k,
        view_sha256=references['targets'][k]['view_sha256'],
        assessment=checks[number][k]) for k in required]

output = [answers[source['number']] for source in sources]
assert len(output) == 14


def complete_paragraph_quote(xml, excerpt):
    paragraphs = re.findall(r'<p\b[^>]*>(.*?)</p>', xml, flags=re.S)
    paragraphs += re.split(r'<br\s*/?>', xml)
    candidates = [plain(x).strip() for x in paragraphs if excerpt in plain(x).strip()]
    assert candidates, excerpt
    return min(candidates, key=len)


for source, a in zip(sources, output):
    for e in a['substantive_impact']['effects']:
        e['source_quote'] = complete_paragraph_quote(source['source_xml'], e['source_quote'])
        e['proposed_quote'] = complete_paragraph_quote(a['proposed_xml'], e['proposed_quote'])

for source, a in zip(sources, output):
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[key] == a[key]
    si = a['substantive_impact']
    for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(si[key]) >= 40
    for e in si['effects']:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(source['source_xml']), (a['number'], e['source_quote'])
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], e['proposed_quote'])
    if source.get('benefit_check_required'):
        assert len(a.get('benefit_review', '')) >= 100
    for ref in a['reference_checks']:
        assert len(ref['assessment']) >= 80
    for removed in a.get('removed_provisions', []):
        assert len(removed) >= 30
    if a.get('change_type') == 'full_repeal':
        assert len(a['repeal_scope']) >= 30
        assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
    if a['proposed_xml'] is None:
        assert a['classification'] == si['classification'] == 'retained_necessary'
        assert si['effects'] == []

(ROOT / 'answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(articles=len(output), rewritten=sum(a['proposed_xml'] is not None for a in output),
                      retained=sum(a['proposed_xml'] is None for a in output),
                      effects=sum(len(a['substantive_impact']['effects']) for a in output)), ensure_ascii=False))
