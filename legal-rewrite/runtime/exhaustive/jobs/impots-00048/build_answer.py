import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SOURCES = json.loads((ROOT / 'source.json').read_text())
REFS = json.loads((ROOT / 'reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWERS = []


def text_of(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))


def p(text):
    return '<p>' + html.escape(text, quote=False) + '</p>'


def clean(xml):
    return re.sub(r'\s+align="[^"]*"', '', xml).strip()


def replace_once(xml, old, new):
    assert xml.count(old) == 1, old
    return xml.replace(old, new, 1)


def effect(number, kind, measure_id, description, before, after, unit,
           population, transition, replacement, source_quote, proposed_quote):
    assert source_quote in text_of(BY_NUMBER[number]['source_xml']), (number, source_quote)
    assert len(source_quote) >= 12
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, xml, reason, notes, impact_class, assessment, limitations,
        burdens, effects=None, benefit=None, checks=None, removed=None,
        repeal=None):
    source = BY_NUMBER[number]
    a = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='retained_unchanged' if xml is None else 'rewrite_draft')
    if xml is None:
        a['classification'] = 'retained_necessary'
    if benefit is not None:
        a['benefit_review'] = benefit
    assert not source.get('benefit_check_required') or len(benefit or '') >= 100
    a['substantive_impact'] = dict(version=1, classification=impact_class,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=effects or [])
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal)
    required = REFS['requirements'][source['code_id'] + '|' + source['source_id']]
    checks = checks or {}
    assert set(checks) == {REFS['targets'][key]['number'] for key in required}
    a['reference_checks'] = [dict(target_key=key,
        view_sha256=REFS['targets'][key]['view_sha256'],
        assessment=checks[REFS['targets'][key]['number']]) for key in required]
    ANSWERS.append(a)
    return a


IS = 'is-a-la-distribution'
FORMAL = 'restructurations-engagements-formels-suppression'

# 210 A : conservation du corps et des valeurs fiscales, suppression de l'acte
# d'engagement fiscal distinct, coordination effective du fait générateur.
x = clean(BY_NUMBER['210 A']['source_xml'])
x = replace_once(x,
    "3. L'application de ces dispositions est subordonnée à la condition que la société absorbante s'engage, dans l'acte de fusion, à respecter les prescriptions suivantes :",
    "3. La société absorbante est tenue de plein droit de respecter les prescriptions suivantes, sans engagement particulier dans l'acte de fusion :")
x = replace_once(x,
    "Toutefois, la cession d'un bien amortissable entraîne l'imposition immédiate de la fraction de la plus-value afférente à ce bien qui n'a pas encore été réintégrée.",
    "Toutefois, la cession d'un bien amortissable entraîne la prise en compte immédiate, dans le résultat fiscal de référence de l'exercice de cession, de la fraction de la plus-value afférente à ce bien qui n'a pas encore été réintégrée. Pour les exercices relevant du régime de distribution, l'exigibilité de l'impôt correspondant est déterminée conformément au 7 ; dans les autres cas, cette fraction est imposable immédiatement.")
x += '\n' + p("7. Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, les réintégrations et reprises prévues au présent article déterminent les résultats de référence, les valeurs fiscales et les fractions de bénéfice à prendre en compte selon l'article 209. Elles ne rendent pas exigible l'impôt sur les sociétés ordinaire du seul fait de la fusion, de l'écoulement d'une période de réintégration, de la disparition de l'objet d'une provision ou de la cession d'un bien lorsque le bénéfice demeure dans l'entreprise, y compris en trésorerie. L'impôt devient exigible lors de la distribution, sous réserve des impositions de sortie et des régimes distincts expressément maintenus par ces articles.")
x += '\n' + p("Les montants des comptes de bénéfices protégés d'un second impôt et des compartiments de bénéfices différés afférents aux éléments transmis sont repris par la société absorbante selon l'article 209, sans double inscription, double déduction ni perte d'une exonération définitive ou d'un taux plus favorable. Les montants déjà taxés ne sont pas taxés une seconde fois ; les montants seulement en sursis ne sont pas réputés déjà taxés. Les déficits et crédits ne sont transmis que dans les conditions propres à leur transfert et ne peuvent être utilisés deux fois. Aucun état ou registre distinct supplémentaire n'est institué par le présent article.")
x += '\n' + p("La suppression de l'engagement particulier prévue au 3 s'applique aux fusions réalisées à compter de l'entrée en vigueur de la loi portant cette suppression. Les obligations fiscales de fond des opérations antérieures, les impositions déjà exigibles, les créances, restitutions, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables. Les sursis et reports non encore dénoués lors de l'entrée dans le régime de distribution suivent ce régime sans rétablir une cotisation annuelle sur les bénéfices conservés. L'impôt minimum international prévu aux articles 223 VJ et suivants conserve son champ propre.")
add('210 A', x,
    "Réforme de fond ciblée : suppression de l'engagement fiscal à insérer dans l'acte de fusion, dont le contenu devient directement légal et contrôlable. La neutralité de la fusion, les valeurs fiscales, les reprises de provisions, les durées de quinze et cinq ans, le seuil de 90 % et les règles anti-double déduction sont conservés. Coordination nécessaire de l'imposition dite immédiate et des réintégrations avec l'IS à la distribution ; ce volet ne supprime pas une seconde taxe.",
    "Lecture intégrale des vingt paragraphes et de la note d'application aux acquisitions de fonds commerciaux à compter du 18 juillet 2022. Le renvoi au troisième alinéa du 2° du 1 de 39 vise bien l'amortissement temporairement déductible des fonds commerciaux, dont la cible fournie va jusqu'au 31 décembre 2029 ; la qualification alternative au c est conservée. Les réserves historiques à 10, 15, 18, 19 et 25 % ne sont pas de nouveaux taux. Nouveaux renvois non inclus dans les cibles obligatoires : 206, 12 ; 209, XI à XIII ; 219, V et VI ; 223 VJ et suivants. Les propositions publiques de 206, 209 et 219 ont été consultées dans leur partie pertinente : elles sont des projets, non le droit officiel. Les articles 54 septies, 210-0 A, 210 B, 210 C, 145, 216, 209 II et les dispositions de crédits gardent leur objet propre ; la seule fusion ne transfère pas librement un crédit ou déficit. Les états de 54 septies ne sont pas supprimés ici. La directive 2009/133/CE et les impositions de sortie ne sont pas réputées écartées. Aucun rendement budgétaire ni solde net national n'est calculé.",
    'mixed',
    "Un engagement écrit propre à la fusion disparaît réellement, tandis que la continuité fiscale qu'il garantissait demeure. La proposition coordonne aussi l'IS différé et la transmission des nouveaux comptes fiscaux ; ce suivi de catégories s'ajoute au suivi des valeurs prévu par la source. Le solde net de complexité n'est donc pas établi.",
    "La dispense porte sur l'engagement de l'article 210 A, non sur tous les actes, agréments ou états de restructuration. Les dettes anciennes, sorties du champ français et minimum international restent distincts ; aucune perte de recettes ni économie de conformité nationale n'est chiffrée.",
    "Le suivi des comptes protégés et compartiments du nouvel IS constitue une donnée fiscale nouvelle par rapport à la source ; il est coordonné sous la même mesure d'IS et sans registre ni dépôt supplémentaire créé ici. La reprise des valeurs et provisions était déjà obligatoire. La suppression de l'engagement n'est remplacée par aucune déclaration équivalente ; le solde de coûts demeure inconnu.",
    effects=[
        effect('210 A','obligation_removed',FORMAL,
            "Suppression de l'engagement fiscal particulier dans l'acte de fusion, avec maintien direct des conditions de continuité.",
            "La société absorbante devait s'engager dans l'acte à respecter les prescriptions du 3, sous peine de perdre le régime.",
            "Les prescriptions s'imposent de plein droit, sans engagement particulier ni dépôt de remplacement.",'legal_duty',
            "Sociétés absorbantes demandant le régime de neutralité fiscale.",
            "Fusions réalisées à compter de l'entrée en vigueur de la loi ; obligations de fond antérieures conservées.",
            "Aucune déclaration équivalente ; contrôle des prescriptions substantielles maintenu.",
            "3. L'application de ces dispositions est subordonnée à la condition que la société absorbante s'engage, dans l'acte de fusion, à respecter les prescriptions suivantes :",
            "3. La société absorbante est tenue de plein droit de respecter les prescriptions suivantes, sans engagement particulier dans l'acte de fusion :"),
        effect('210 A','coordination',IS,
            "La réintégration et la cession alimentent les résultats de référence sans recréer l'IS annuel sur les bénéfices conservés.",
            "La cession rendait immédiatement imposable la fraction de plus-value d'apport non encore réintégrée.",
            "Dans le régime nouveau, cette fraction attend la distribution ; les taux favorables et impositions distinctes conservent leur champ.",'other',
            "Sociétés absorbantes entrant dans le régime ordinaire à la distribution.",
            "Exercices entrant dans le régime nouveau ; dettes déjà exigibles et anciens recours préservés.",
            "Coordination de la même mesure d'IS, sans nouvelle suppression de taxe décomptée.",
            "Toutefois, la cession d'un bien amortissable entraîne l'imposition immédiate de la fraction de la plus-value afférente à ce bien qui n'a pas encore été réintégrée.",
            "L'impôt devient exigible lors de la distribution, sous réserve des impositions de sortie et des régimes distincts expressément maintenus par ces articles."),
        effect('210 A','complexity_added',IS,
            "Transmission des catégories du nouvel IS, en complément du suivi des valeurs et provisions déjà imposé.",
            "La source impose la reprise des provisions, réserves et valeurs ; elle ne comporte pas les nouveaux comptes d'IS à la distribution.",
            "Reprise des comptes protégés et compartiments afférents aux éléments transmis, sans double inscription.",'legal_duty',
            "Sociétés absorbantes relevant du nouvel IS et détenant des montants transmis de ces catégories.",
            "Seulement lors de l'application du régime nouveau ; pas de compte réputé taxé pour les simples sursis.",
            "Données supplémentaires du régime commun de distribution, sans état ou registre distinct supplémentaire ; coût non établi.",
            "a) Elle doit reprendre à son passif :",
            "Les montants des comptes de bénéfices protégés d'un second impôt et des compartiments de bénéfices différés afférents aux éléments transmis sont repris par la société absorbante selon l'article 209, sans double inscription, double déduction ni perte d'une exonération définitive ou d'un taux plus favorable.")
    ],
    benefit="Le 1 conserve la neutralité des plus-values et profits d'apport et de l'annulation des propres titres ; l'interdiction de déduire le mali technique et la moins-value déjà couverte par les produits mère-fille évitent un double avantage sur une même base, sans supprimer l'exonération. Le 2 maintient les provisions tant qu'elles gardent leur objet. Le 3 conserve les valeurs, les étalements de quinze ou cinq ans et la durée moyenne pondérée au-delà de 90 %, avec calcul des amortissements sur la valeur d'apport. Les 5 et 6 conservent les assimilations favorables de crédit-bail et de titres. Les réserves définitivement taxées et taux favorables restent protégés, les simples sursis ne sont pas traités comme déjà taxés. Tous ces bénéfices demeurent ouverts aux fusions futures éligibles ; aucun impôt ordinaire n'est exigé sur le seul bénéfice conservé.",
    checks={'39': "Le d du 3 vise le troisième alinéa du 2° du 1 de l'article 39, qui autorise l'amortissement des fonds commerciaux acquis de 2022 à 2029, avec exclusions des acquisitions liées. Ce n'est pas un contrat de travail. L'alternative d/c selon la déduction effective de l'amortissement est conservée, ainsi que la note propre à 210 A du 18 juillet 2022 ; aucun seuil d'ancienneté salariale ni notification de rupture n'est ajouté. Les provisions de fluctuation du 5° du 1 gardent leur traitement historique distinct."},
    removed=["L'engagement fiscal particulier à insérer dans l'acte de fusion pour bénéficier de la neutralité est supprimé ; les prescriptions de fond deviennent directement applicables."])

# 210 B : fin de l'agrément discrétionnaire et de la conservation imposée trois ans.
x = clean(BY_NUMBER['210 B']['source_xml'])
x = replace_once(x,
    "3. En l'absence d'apport d'une ou plusieurs branches complètes d'activité ou d'éléments assimilés, les dispositions de l'article 210 A s'appliquent aux apports partiels d'actif et aux scissions sur agrément délivré dans les conditions prévues à l'article 1649 nonies.",
    "3. En l'absence d'apport d'une ou plusieurs branches complètes d'activité ou d'éléments assimilés, les dispositions de l'article 210 A s'appliquent de plein droit aux apports partiels d'actif et aux scissions qui remplissent les conditions ci-dessous, sans agrément ni déclaration particulière de remplacement.")
x = replace_once(x,"L'agrément est délivré lorsque, compte tenu des éléments faisant l'objet de l'apport :",
    "Les conditions suivantes sont appréciées compte tenu des éléments faisant l'objet de l'apport :")
x = replace_once(x,
    "a. L'opération est justifiée par un motif économique, se traduisant notamment par l'exercice par la société bénéficiaire de l'apport d'une activité autonome et l'amélioration des structures, ainsi que par une association entre les parties formalisée par un engagement de conservation pendant trois ans des titres remis en contrepartie de l'apport ;",
    "a. L'opération est justifiée par un motif économique, se traduisant notamment par l'exercice par la société bénéficiaire de l'apport d'une activité autonome et l'amélioration des structures ;")
x = replace_once(x, "b. L'article 210-0 A est respecté ;",
    "b. Les conditions de l'article 210-0 A sont respectées. Pour l'application du présent 3, l'exigence d'une branche complète d'activité prévue au 4° du I de ce même article ne fait pas obstacle à l'éligibilité d'un apport d'éléments ne constituant pas une telle branche. Les autres caractéristiques de l'opération et les conditions de ses II et III demeurent applicables ;")
old = "Pour les opérations de scission, l'obligation de conservation des titres mentionnée au a n'est exigée que des associés qui détiennent dans la société scindée, à la date d'approbation de la scission, 5 % au moins des droits de vote ou qui y exercent ou y ont exercé dans les six mois précédant cette date, directement ou par l'intermédiaire de leurs mandataires sociaux ou préposés, des fonctions de direction, d'administration ou de surveillance et détiennent au moins 0,1 % des droits de vote dans la société."
x = replace_once(x, old,
    "Aucun engagement ni durée minimale de conservation des titres n'est exigé au titre du présent 3, y compris lorsque ses conditions sont rendues applicables par un renvoi d'un autre article. Les obligations de conservation instituées par un fondement autonome demeurent distinctes.")
x += '\n' + p("4. Le 3, dans sa rédaction issue de la loi supprimant l'agrément, s'applique aux opérations réalisées à compter de son entrée en vigueur. Une demande d'agrément en cours ne fait pas obstacle à l'application de plein droit de ce régime et n'a pas à être remplacée par une déclaration. Les opérations antérieures, les engagements qui s'y rapportent, les droits acquis, les créances, restitutions, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables. Les règles anti-fraude et les conditions territoriales des articles 210-0 A et 210 C demeurent applicables.")
x += '\n' + p("Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, les valeurs fiscales, exclusions de plus-values et modalités d'imposition future mentionnées au présent article s'appliquent dans les conditions du 7 de l'article 210 A. Ni l'apport, ni la scission, ni la seule cession ultérieure d'un bien ou d'un titre ne rendent exigible l'impôt sur les sociétés ordinaire sur les bénéfices conservés, sous réserve des impositions distinctes ou de sortie prévues par ces dispositions.")
add('210 B', x,
    "Réduction de fond : application directe du régime aux apports ou scissions sans branche complète lorsque les conditions économiques, anti-fraude et de continuité fiscale sont réunies ; suppression de l'agrément 1649 nonies et de l'engagement de conservation de trois ans. Les seuils de plus de 50 % du capital et de plus de 30 % des droits de vote du 1, l'ancienneté fiscale du 1 bis et le calcul du 2 restent identiques. Coordination du fait générateur avec 210 A, sans seconde réduction d'IS comptée.",
    "Le 7 bis de 38 a été lu dans la source et la proposition : son troisième alinéa impose la plus-value à hauteur de la soulte et son quatrième exclut le sursis si la soulte dépasse 10 % de la valeur nominale ou la plus-value. Ces conditions restent applicables aux apports assimilés, avec l'ancienneté fiscale du 1 bis. Le 3 a, b et c n'est pas renuméroté : le renvoi de 115, 2 bis a, reprend ces conditions sans ressusciter l'engagement de conservation supprimé ici. L'agrément propre à 115, 2 bis, son engagement autonome des associés et ses dispenses restent toutefois distincts et nécessitent un examen hors de ce lot ; ils ne sont pas annoncés supprimés. Incohérence préexistante : 210-0 A I, 4° exige une branche complète, alors que 210 B, 3 ouvre le régime sans une telle branche. Le b est donc expressément coordonné pour écarter cette seule exigence dans le champ du 3 ; les autres caractéristiques et les garanties anti-fraude des II et III de 210-0 A, ainsi que le rattachement de 210 C, sont conservés. Nouveaux renvois de coordination non fournis dans reference-targets : 206, 12 ; 219, V et VI ; 210 A, 7 rédigé dans ce lot, et subdivisions désormais explicites de 210-0 A, dont la source a été lue intégralement. Aucune modification du contrat de travail.",
    'material_reduction',
    "La procédure préalable d'agrément et le blocage des titres pendant trois ans sont effectivement retirés pour les nouvelles opérations relevant du 3. Les règles de base des branches complètes et les sursis restent disponibles. La coordination à l'IS à la distribution ne constitue pas une deuxième taxe supprimée.",
    "L'allègement ne supprime ni le régime autonome d'agrément des distributions de 115 ni les contrôles anti-fraude, les règles territoriales ou les autres engagements légaux. Les opérations antérieures gardent leur régime ; aucun montant de coût ou de recettes n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les conditions économiques, territoriales et de continuité préexistent, et ni déclaration, ni dossier, ni notification de remplacement ne sont créés. Les suivis du nouvel IS sont ceux coordonnés en 210 A, sans dispositif supplémentaire propre à 210 B.",
    effects=[
        effect('210 B','authorization_removed','restructurations-agrement-210b-suppression',
            "Accès de plein droit à la neutralité des opérations sans branche complète satisfaisant aux conditions de fond.",
            "Agrément fiscal délivré selon 1649 nonies pour les apports et scissions relevant du 3.",
            "Aucun agrément ni déclaration de remplacement au titre du 3 ; conditions de fond contrôlables.",'legal_duty',
            "Sociétés réalisant les apports ou scissions visés au 3.",
            "Opérations réalisées à compter de l'entrée en vigueur ; demandes en cours devenues inutiles, anciens agréments et droits préservés.",
            "Aucune formalité équivalente ; agréments autonomes d'autres articles non supprimés.",
            "3. En l'absence d'apport d'une ou plusieurs branches complètes d'activité ou d'éléments assimilés, les dispositions de l'article 210 A s'appliquent aux apports partiels d'actif et aux scissions sur agrément délivré dans les conditions prévues à l'article 1649 nonies.",
            "3. En l'absence d'apport d'une ou plusieurs branches complètes d'activité ou d'éléments assimilés, les dispositions de l'article 210 A s'appliquent de plein droit aux apports partiels d'actif et aux scissions qui remplissent les conditions ci-dessous, sans agrément ni déclaration particulière de remplacement."),
        effect('210 B','obligation_removed','restructurations-conservation-titres-210b-suppression',
            "Suppression de l'engagement et de la durée minimale de conservation propres au 3.",
            "Conservation de trois ans ; pour les scissions, obligation limitée aux associés franchissant les seuils de 5 % ou de 0,1 % avec fonctions dirigeantes.",
            "Aucune conservation minimale sur le seul fondement du 3 ; les engagements autonomes d'autres régimes restent distincts.",'legal_duty',
            "Apporteuses et associés auparavant tenus à l'engagement du 3, dont associés concernés de sociétés scindées.",
            "Opérations nouvelles ; engagements des opérations antérieures maintenus.",
            "Aucun délai, engagement ou déclaration de remplacement.",
            "a. L'opération est justifiée par un motif économique, se traduisant notamment par l'exercice par la société bénéficiaire de l'apport d'une activité autonome et l'amélioration des structures, ainsi que par une association entre les parties formalisée par un engagement de conservation pendant trois ans des titres remis en contrepartie de l'apport ;",
            "Aucun engagement ni durée minimale de conservation des titres n'est exigé au titre du présent 3, y compris lorsque ses conditions sont rendues applicables par un renvoi d'un autre article."),
        effect('210 B','coordination',IS,
            "Le maintien de l'imposition future des plus-values respecte le nouveau fait générateur de distribution.",
            "Le c exige que l'opération assure l'imposition future des plus-values en sursis, dans le cadre de l'IS annuel source.",
            "Le maintien des valeurs et bases n'entraîne plus à lui seul une cotisation annuelle dans le régime nouveau.",'other',
            "Entreprises du régime ordinaire nouveau réalisant une opération éligible.",
            "Exercices relevant de la distribution ; impositions distinctes et de sortie réservées.",
            "Même mesure d'IS ; aucun nouveau prélèvement supprimé par ce renvoi.",
            "c. Les modalités de l'opération permettent d'assurer l'imposition future des plus-values mises en sursis d'imposition.",
            "Ni l'apport, ni la scission, ni la seule cession ultérieure d'un bien ou d'un titre ne rendent exigible l'impôt sur les sociétés ordinaire sur les bénéfices conservés, sous réserve des impositions distinctes ou de sortie prévues par ces dispositions.")
    ],
    checks={'38': "Le renvoi du 1 vise exactement les troisième et quatrième alinéas du 7 bis : soulte prise en compte à hauteur de son montant, seuil de 10 % de la valeur nominale et exclusion si la soulte dépasse la plus-value. Ces dispositions sont conservées dans la proposition cible. Le 1 bis reporte la date d'acquisition des éléments apportés pour l'ancienneté des titres ; il ne s'agit pas d'ancienneté d'emploi. Aucun renvoi n'est étendu au contrat unique ni à sa notification de rupture."},
    removed=["L'agrément fiscal préalable prévu au 3 pour les apports et scissions sans branche complète, avec son dossier propre, est supprimé sans déclaration équivalente.",
             "L'engagement de conservation de trois ans des titres remis en contrepartie de l'apport et son application aux associés concernés d'une scission sont supprimés pour les opérations nouvelles."])

# 210 C : champ territorial autonome, aucune cotisation annuelle instituée.
add('210 C', None,
    "Maintien intégral nécessaire après examen des charges : l'article délimite le régime de neutralité entre personnes passibles de l'IS, assure la continuité du droit français d'imposer par le rattachement à un établissement stable et exclut le transfert vers une SICAV exonérée. Il n'institue ni agrément, ni déclaration, ni délai de conservation, ni imposition annuelle propre. Modifier son vocabulaire n'apporterait aucun allègement.",
    "Les trois paragraphes et la note d'application aux opérations réalisées à compter du 1er janvier 2018 ont été lus. La suppression de l'agrément du 3 de 210 B ne modifie pas la condition d'assujettissement du 1 ni le rattachement du 2. Une personne reste passible de l'IS lorsqu'elle relève du régime de distribution, même si ses bénéfices conservés ne déclenchent pas l'IS ordinaire. Le 3 ne supprime pas une exonération de la SICAV ; il empêche qu'une opération avec une société non exonérée efface une base différée sans continuité. Les cadres de la directive 2009/133/CE, des conventions et des impositions de sortie ne sont pas prétendus supprimés. Aucune mesure SRU ni règle de contrat privé dans la source.",
    'retained_necessary',
    "Aucun changement normatif : les trois règles de champ et de continuité fiscale sont utiles à la neutralité préservée des restructurations. Aucun prélèvement ou formalisme supplémentaire supprimable n'est identifié dans cet article ; il n'est compté ni réécrit ni simplifié.",
    "Le maintien porte sur ce seul champ de restructuration, sans validation générale de toutes les conditions transfrontières ni des régimes distincts des SICAV. Aucune réduction nette de coût ou de recettes n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée puisque le texte source est conservé intégralement. Le rattachement à l'établissement stable préexiste ; aucun dossier, registre, délai ou justificatif additionnel n'est créé.",
    benefit="Les 1 et 2 maintiennent l'accès des personnes et organismes passibles de l'IS à la neutralité des fusions, scissions et apports, y compris pour les futures opérations au profit d'une personne morale étrangère dont les éléments restent rattachés à l'établissement stable français. Le 3 n'accorde pas un avantage à retirer : il exclut un transfert vers une SICAV susceptible de soustraire définitivement les plus-values à la continuité fiscale. Cette exclusion ne retire ni l'exonération propre de la SICAV ni les autres opérations éligibles. L'absence d'IS sur les bénéfices conservés ne fait pas perdre la qualité de personne passible de cet impôt.")

# 210 D : les cinq annuités et reports restent des règles de base, non d'exigibilité.
x = clean(BY_NUMBER['210 D']['source_xml'])
x += '\n' + p("Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, les règles du présent article déterminent les valeurs fiscales et les résultats de référence pris en compte selon l'article 209. Le report du a et les réintégrations par cinquième du b ne rendent pas exigible l'impôt sur les sociétés ordinaire sur un bénéfice qui demeure dans la société, y compris en trésorerie. Lors de leur dénouement, les montants non encore taxés sont pris en compte une seule fois dans le compartiment correspondant ; ils deviennent imposables à la distribution, sous réserve des impositions de sortie et régimes distincts expressément maintenus. Les montants déjà soumis à l'impôt ne subissent pas une seconde imposition.")
x += '\n' + p("Cette coordination s'applique aux exercices ouverts à compter de l'entrée en vigueur de la loi instituant le régime de distribution, y compris au dénouement ultérieur des reports et réintégrations antérieurs qui n'étaient pas déjà exigibles. Elle ne remet en cause ni les dettes déjà exigibles, ni les créances, prescriptions et recours des périodes antérieures, ni les règles de l'impôt minimum international prévues aux articles 223 VJ et suivants.")
add('210 D', x,
    "Coordination nécessaire, sans réforme stylistique : les reports sur immobilisations non amortissables et les réintégrations par cinquième restent des règles de valeur et de résultat, sans exigibilité annuelle automatique dans le nouvel IS. Le prix fiscal historique, les amortissements sur valeur d'opération et l'interdiction de déduire l'écart de valorisation sont intégralement maintenus.",
    "Lecture des quatre paragraphes, des cessions à titre onéreux visées au a et de la note relative à la loi du 31 juillet 2014. Le texte n'abroge ni la loi coopérative n° 78-763, articles 48 et 49, ni ses règles patrimoniales extérieures aux cinq codes ; celles-ci restent à leur champ et ne sont pas présentées comme réécrites. Les renvois ajoutés à 206, 12 ; 209, XI à XIII ; 219, V et VI ; 223 VJ et suivants ne figurent pas dans reference-targets. Les propositions fiscales pertinentes de 206/209/219 ont été consultées ; elles ne sont pas le droit en vigueur. Les reports antérieurs simplement différés restent distingués des dettes déjà exigibles et des réserves déjà taxées. Le suivi général de 54 septies demeure distinct. Aucune économie nationale chiffrée ni réduction des aides à l'innovation n'est déduite de cette coordination.",
    'coordination_only',
    "Le calendrier de prise en compte par cinquième et le report jusqu'à la cession sont préservés mais ne déclenchent plus l'IS ordinaire sur des bénéfices conservés lorsque le régime de distribution s'applique. Il s'agit de la même réforme d'IS, sans nouvelle réduction autonome de taux ou d'assiette dans cet article.",
    "Seules les sociétés coopératives et opérations déjà visées sont concernées. Les impositions anciennes exigibles, les sorties du droit français d'imposer et le minimum international ne sont pas effacés ; leur coût net n'est pas établi.",
    "Aucune charge nouvelle propre à 210 D n'est identifiée : les valeurs fiscales et réintégrations étaient déjà suivies. Le compartiment du nouvel IS est celui du régime commun de 209 ; aucun état, registre, agrément ou délai distinct n'est ajouté ici.",
    effects=[effect('210 D','coordination',IS,
        "Articulation du report et des cinquièmes avec l'exigibilité à la distribution.",
        "Les plus-values sur les autres immobilisations étaient réintégrées par cinquième dans les excédents imposables pendant cinq ans.",
        "Les mêmes cinquièmes déterminent les résultats de référence, sans IS ordinaire tant que le bénéfice reste dans la société.",'other',
        "SCOP issues d'une opération visée à l'article 48 de la loi de 1978 et relevant du régime nouveau.",
        "Exercices ouverts à compter de l'entrée en vigueur du nouvel IS ; dettes déjà exigibles préservées.",
        "Aucun mécanisme de remplacement annuel ; suivi commun des compartiments, sans dépôt supplémentaire propre.",
        "Les plus-values afférentes aux autres immobilisations sont réintégrées, par cinquième, dans les excédents nets de gestion imposables sur une période de cinq ans suivant la transformation.",
        "Le report du a et les réintégrations par cinquième du b ne rendent pas exigible l'impôt sur les sociétés ordinaire sur un bénéfice qui demeure dans la société, y compris en trésorerie.")])

# 210 E bis : supprimer les deux états annuels, pas les valeurs et avantages.
x = clean(BY_NUMBER['210 E bis']['source_xml'])
x = replace_once(x,
    "L'application des 1° à 5° du présent I est subordonnée à la condition que la société bénéficiaire de l'apport s'engage, dans l'acte d'apport, à respecter les prescriptions prévues au 3 de l'article 210 A.",
    "Pour l'application des 1° à 5° du présent I, la société bénéficiaire de l'apport est tenue de plein droit de respecter les prescriptions prévues au 3 de l'article 210 A, sans engagement particulier dans l'acte d'apport.")
x = replace_once(x,
    "se substitue à l'entreprise dont l'ensemble du patrimoine ou une branche complète d'activité est apporté pour la réintégration restant à effectuer ;",
    "se substitue à l'entreprise dont l'ensemble du patrimoine ou une branche complète d'activité est apporté pour la réintégration restant à effectuer. Cette substitution ne fait pas obstacle à la faculté d'imposition au nom de l'entreprise apporteuse prévue au second alinéa du 3° du III de l'article 151 octies D ;")
x = replace_once(x,
    "Un état de suivi de la valeur fiscale des titres de la société bénéficiaire de l'apport détenus par l'entreprise soumise à l'impôt sur les sociétés à la suite de l'une des options prévues aux mêmes 1 ou 2, conforme au modèle fourni par l'administration, est joint à la déclaration, prévue à l'article 223, de l'entreprise individuelle ou de l'entreprise individuelle à responsabilité limitée au titre de l'exercice en cours à la date de l'apport et des exercices suivants.",
    "Aucun état distinct de suivi de la valeur fiscale des titres n'est joint à la déclaration prévue à l'article 223 au titre du présent II. Les valeurs nécessaires au calcul des plus-values restent déterminées conformément au premier alinéa et justifiables à partir de la comptabilité et des pièces soumises aux obligations légales de conservation déjà applicables, sans registre supplémentaire.")
x = replace_once(x,
    "IV. - La société bénéficiaire de l'apport joint à sa déclaration de résultat, à compter de l'exercice de l'apport, un état conforme au modèle fourni par l'administration faisant apparaître les renseignements nécessaires au suivi des plus-values.",
    "IV. - La société bénéficiaire de l'apport est dispensée de joindre à sa déclaration de résultat un état distinct de suivi des plus-values au titre du présent article. Les règles de calcul, de reprise des valeurs et de réintégration prévues au I demeurent applicables ; leur contrôle s'effectue à partir de la comptabilité et des pièces soumises aux obligations légales de conservation déjà applicables, sans état annuel ni registre de remplacement.")
x = replace_once(x,
    "lorsque l'attribution intervient dans un délai d'un an à compter de la réalisation de l'apport.",
    "quelle que soit la date de l'attribution postérieure à la réalisation de l'apport.")
x += '\n' + p("VII. - Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, les résultats, provisions et plus-values visés au I sont pris en compte selon le 7 de l'article 210 A et l'article 209, sans exigibilité de l'impôt sur les sociétés ordinaire du seul fait de l'apport, d'une reprise, d'une réintégration ou d'une cession lorsque le bénéfice demeure dans l'entreprise, y compris en trésorerie. Les attributions de titres bénéficiant de la neutralité du V ne constituent pas une distribution soumise à ce nouvel impôt ; la neutralité d'impôt sur le revenu prévue au VI est maintenue. Les reports dont le titulaire demeure personnellement imposable à l'impôt sur le revenu, notamment ceux de l'article 151 octies D, conservent leur régime propre.")
x += '\n' + p("Les comptes de bénéfices protégés et compartiments de bénéfices différés afférents aux éléments apportés suivent leur transmission dans les conditions du 7 de l'article 210 A, sans double emploi des bases, pertes, crédits ou montants déjà taxés. Leur suivi relève du régime commun de l'article 209 ; aucun dépôt ni registre supplémentaire n'est exigé par le présent article.")
x += '\n' + p("La suppression de l'engagement particulier du I s'applique aux apports réalisés à compter de l'entrée en vigueur de la loi portant cette suppression. Les dispenses d'états prévues aux II et IV s'appliquent à toutes les échéances déclaratives postérieures à cette entrée en vigueur, y compris lorsqu'elles concernent des apports antérieurs ; aucun état omis n'est à déposer après cette date sur ces seuls fondements. La suppression du délai du V s'applique aux attributions de titres intervenant à compter de cette entrée en vigueur, y compris à la suite d'apports antérieurs. Les options et droits acquis, les dettes déjà exigibles, les restitutions, les contrôles, prescriptions et recours des périodes antérieures restent régis par les dispositions qui leur étaient applicables. Les impositions de sortie et l'impôt minimum international demeurent distincts.")
add('210 E bis', x,
    "Réduction de fond : suppression de l'engagement formel de la bénéficiaire, des états fiscaux distincts annuels de l'apporteuse et de la bénéficiaire, et du délai maximal d'un an pour l'attribution neutre des titres du V. L'option conjointe du III, qui choisit un régime fiscal de valeurs et reports, reste dans l'acte : elle n'est pas un agrément supprimé remplacé par une déclaration. Les 1° à 5°, le crédit-bail, les valeurs comptables et la neutralité d'IR du VI demeurent. Coordination de l'IS à la distribution et de son suivi transmis.",
    "Lecture des quatorze paragraphes et des deux notes d'application aux apports et exercices à compter du 1er janvier 2026 ; ces dates historiques ne fixent pas la date de la réforme proposée. L'état personnel d'IR et les options propres de 151 octies D ne sont pas supprimés : les III, 1° et 2° y préservent le report lors du passage des titres au patrimoine privé, et le III, 3° contient une possibilité propre de taxation par l'entreprise apporteuse. L'articulation préexistante de cette dernière possibilité avec la substitution apparemment inconditionnelle du I, 3° de 210 E bis est signalée et coordonnée par une réserve expresse de cette faculté dans le texte proposé. Le renvoi ajouté à ce second alinéa du 3° du III n'est pas une cible fournie : sa source publique entière a été lue. 1655 sexies, 1 et 2, vise EI/EIRL assimilée à EURL/EARL, non un CDD ni une durée d'emploi. Le V porte textuellement sur une branche, tandis que le VI vise aussi l'ensemble du patrimoine : cette dissymétrie source est signalée, sans étendre silencieusement le V à toute cessation. Les dispenses d'états retirent les dépôts expressément créés ici ; elles n'abolissent pas un état autonome de 151 octies D ou de 54 septies pour une autre opération. Autres nouveaux renvois non fournis en cibles obligatoires : 206, 12 ; 209 ; 219, V/VI et 210 A, 7 rédigé dans le lot. Aucun gain national, CIR supprimé ou remboursement fiscal nouveau n'est supposé.",
    'mixed',
    "Deux transmissions fiscales annuelles distinctes, l'engagement fiscal de la bénéficiaire et le délai d'attribution d'un an sont retirés. Le suivi des catégories du nouvel IS est coordonné avec celui transmis en 210 A ; il ajoute une distinction de données par rapport à la source. Les baisses de formalités sont réelles mais leur solde de coûts n'est pas établi.",
    "Seuls les apports du présent article, les états qu'il institue et les attributions du V sont couverts. Les options, reports personnels d'IR, régimes de sortie et obligations autonomes d'autres articles ne disparaissent pas ; aucune perte de recettes n'est chiffrée.",
    "Aucun état ni registre de remplacement n'est créé pour les deux dépôts supprimés. La comptabilité, les pièces conservées et l'option conjointe existaient déjà. Le suivi transmis des comptes protégés et compartiments de l'IS est une donnée nouvelle commune à la réforme, recensée sous la même mesure qu'en 210 A ; son coût et le solde net restent inconnus.",
    effects=[
        effect('210 E bis','coordination',FORMAL,
            "La disparition de l'engagement d'apport coordonne la même suppression d'engagements formels que 210 A.",
            "Le bénéfice des 1° à 5° dépendait d'un engagement particulier de la bénéficiaire dans l'acte.",
            "La bénéficiaire respecte les prescriptions de plein droit, sans clause fiscale particulière.",'legal_duty',
            "Sociétés bénéficiaires d'apports d'EI ou EIRL à l'IS.",
            "Apports réalisés à compter de l'entrée en vigueur ; engagements antérieurs réservés.",
            "Pas de déclaration équivalente ; option conjointe préexistante du III conservée.",
            "L'application des 1° à 5° du présent I est subordonnée à la condition que la société bénéficiaire de l'apport s'engage, dans l'acte d'apport, à respecter les prescriptions prévues au 3 de l'article 210 A.",
            "Pour l'application des 1° à 5° du présent I, la société bénéficiaire de l'apport est tenue de plein droit de respecter les prescriptions prévues au 3 de l'article 210 A, sans engagement particulier dans l'acte d'apport."),
        effect('210 E bis','obligation_removed','apports-ei-etats-annuels-distincts-suppression',
            "Suppression des états annuels de valeur fiscale des titres et de suivi des plus-values institués aux II et IV.",
            "L'apporteuse joint chaque année un état modèle de valeur fiscale des titres ; la bénéficiaire joint chaque année son état modèle de plus-values.",
            "Les deux états ne sont plus joints, sans formulaire ou registre de remplacement ; valeurs et contrôle sur pièces demeurent.",'legal_duty',
            "EI/EIRL apporteuses à l'IS et sociétés bénéficiaires visées par l'article.",
            "Toutes échéances postérieures à l'entrée en vigueur, même pour les apports antérieurs ; aucun rattrapage sur ces seuls fondements.",
            "Aucun dépôt équivalent ; les états autonomes d'autres articles gardent leur champ.",
            "IV. - La société bénéficiaire de l'apport joint à sa déclaration de résultat, à compter de l'exercice de l'apport, un état conforme au modèle fourni par l'administration faisant apparaître les renseignements nécessaires au suivi des plus-values.",
            "IV. - La société bénéficiaire de l'apport est dispensée de joindre à sa déclaration de résultat un état distinct de suivi des plus-values au titre du présent article."),
        effect('210 E bis','relief_extended','apports-ei-attribution-titres-sans-delai',
            "Ouverture de la neutralité d'attribution de titres du V au-delà de l'année suivant l'apport.",
            "Neutralité d'IS des plus-values ou moins-values des titres attribués au patrimoine personnel seulement si attribution dans l'année de l'apport de branche.",
            "Même neutralité pour les attributions éligibles de branche quelle que soit leur date après l'apport ; IR du VI maintenu.",'other',
            "Entrepreneurs individuels retirant les titres d'une société bénéficiaire de l'apport de branche visé au V.",
            "Attributions à compter de l'entrée en vigueur, y compris à la suite d'apports antérieurs ; pas de restitution générale d'un impôt ancien exigible.",
            "Aucune durée, demande ou condition nouvelle ; le champ branche du V n'est pas étendu à l'ensemble du patrimoine.",
            "lorsque l'attribution intervient dans un délai d'un an à compter de la réalisation de l'apport.",
            "quelle que soit la date de l'attribution postérieure à la réalisation de l'apport."),
        effect('210 E bis','coordination',IS,
            "Les plus-values et provisions reportées suivent le fait générateur de distribution pour l'IS ordinaire uniquement.",
            "Le 2° et le 3° renvoient aux réintégrations de 210 A, dans une assiette d'IS annuelle.",
            "La prise en compte des mêmes bases ne déclenche pas l'IS ordinaire sur le seul bénéfice conservé ; IR personnel distinct.",'other',
            "Apporteuses et bénéficiaires entrant dans le régime ordinaire de distribution.",
            "Exercices du régime nouveau ; dettes exigibles et reports personnels d'IR préservés.",
            "La transmission des comptes de 210 A est coordonnée ; aucune deuxième réforme d'IS décomptée.",
            "2° L'imposition des plus-values afférentes aux autres immobilisations est effectuée au nom de la société bénéficiaire de l'apport selon les modalités prévues au d du 3 de l'article 210 A ;",
            "Les reports dont le titulaire demeure personnellement imposable à l'impôt sur le revenu, notamment ceux de l'article 151 octies D, conservent leur régime propre.")
    ],
    checks={},
    removed=["L'engagement particulier de reprise des prescriptions de 210 A dans l'acte d'apport est supprimé ; ces prescriptions restent directement applicables.",
             "L'état distinct annuel de suivi de la valeur fiscale des titres joint par l'entreprise apporteuse à sa déclaration 223 au titre du II est supprimé.",
             "L'état distinct annuel des plus-values joint par la bénéficiaire à sa déclaration de résultat au titre du IV est supprimé, sans registre ou état de remplacement.",
             "La condition d'attribution au patrimoine personnel dans l'année de l'apport de branche, prévue au V, est supprimée pour les attributions nouvelles."])

# 210 F : pérenniser le taux favorable sans inventer de taux ni de subvention.
x = clean(BY_NUMBER['210 F']['source_xml'])
marker = "<p>II. – L'application du I"
assert marker in x
x = x.replace(marker,
    p("Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, les plus-values éligibles au présent I conservent le taux de 19 % mentionné au IV de l'article 219, sous réserve d'une exonération ou d'un taux plus favorable. Elles sont prises en compte dans le compartiment correspondant prévu à l'article 209 et ne donnent lieu à l'impôt sur les sociétés ordinaire qu'à leur distribution. Leur réalisation ou leur conservation, y compris en trésorerie, ne suffit pas à rendre cet impôt exigible.") + '\n' + marker, 1)
x = replace_once(x,
    "En cas de fusion de sociétés, l'engagement de transformation ou de construction souscrit par la société absorbée n'est pas rompu lorsque la société absorbante s'engage, dans l'acte de fusion, à se substituer à la société absorbée pour le respect de l'engagement de transformation ou de construction dans le délai restant à courir.",
    "En cas de fusion de sociétés, la société absorbante est substituée de plein droit à la société absorbée pour le respect de l'engagement de transformation ou de construction dans le délai restant à courir. Aucun engagement particulier dans l'acte de fusion n'est exigé à ce titre et l'absence d'une telle clause ne rompt pas l'engagement initial.")
x = replace_once(x,
    "III. – Sur demande de l'acquéreur, une prolongation des délais de quatre et six ans mentionnés au II peut être accordée par l'autorité compétente de l'Etat du lieu de la situation des immeubles pour une durée n'excédant pas un an. Cette prolongation peut, dans les mêmes conditions, être renouvelée une fois. L'absence de notification d'un refus motivé de l'administration dans les deux mois de la réception de la demande vaut acceptation.",
    "III. – Les délais de quatre et six ans mentionnés au II sont prolongés de plein droit de deux ans, sans demande, décision administrative ou justificatif particulier de prolongation. Les prolongations déjà accordées s'imputent sur ces deux ans ; elles ne sont pas cumulées une seconde fois avec cette prolongation de plein droit. Une durée supérieure légalement acquise demeure applicable.")
x = replace_once(x,
    "2° Aux cessions à titre onéreux réalisées après le 31 décembre 2026 si une promesse unilatérale ou synallagmatique de vente a été conclue au plus tard à cette date et si la cession a été réalisée au plus tard deux ans après la date de la promesse.",
    "2° Aux cessions à titre onéreux réalisées après le 31 décembre 2026, sans condition de date de la promesse ni délai entre cette promesse et la cession au titre du présent IV.")
x += '\n' + p("V. – La substitution de plein droit du II s'applique aux fusions réalisées à compter de l'entrée en vigueur de la loi supprimant l'engagement particulier. Le III s'applique aux acquisitions réalisées à compter de cette entrée en vigueur ainsi qu'aux délais qui ne sont pas expirés à cette date, compte tenu des prolongations déjà accordées. Les demandes de prolongation régulièrement déposées avant cette entrée en vigueur et encore en cours bénéficient de cette règle sans nouveau dossier, même si le délai a expiré pendant leur instruction. En dehors de ce cas, le III ne rouvre pas un délai déjà expiré. Le 2° du IV, dans sa rédaction issue de cette loi, s'applique aux cessions réalisées à compter de cette entrée en vigueur. Les cessions antérieures conservent leurs taux, exonérations et autres droits dans les conditions qui leur étaient applicables. Les dettes déjà exigibles, les contrôles, restitutions, prescriptions et recours sont préservés, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.")
x += '\n' + p("La coordination du I avec le régime de distribution s'applique aux exercices ouverts à compter de l'entrée en vigueur de la loi instituant ce régime. Elle ne rend pas remboursables les impositions antérieures légalement dues et ne permet aucune seconde utilisation d'une réserve déjà taxée, d'un déficit ou d'un crédit. L'impôt personnel des associés, les impositions de sortie et l'impôt minimum international conservent leur champ propre.")
add('210 F', x,
    "Réforme de fond favorable : les deux années de prolongation auparavant soumises à décisions sont acquises de plein droit, sans demande ; suppression de la clause particulière de substitution en fusion et de la date butoir des cessions futures. Le taux source de 19 % est conservé, sans nouveau taux, et son exigibilité est coordonnée à la distribution, avec maintien des taux ou exonérations plus favorables. Les zones tendues, locaux, liens de dépendance exclus, 75 % de surface, délais initiaux de quatre/six ans, seuil de 20 000 m², déclaration d'achèvement et exception de circonstances indépendantes de la volonté restent intégralement maintenus.",
    "Lecture des douze paragraphes et de la note d'application aux cessions depuis le 1er janvier 2024. Le IV de 219 consulté dans le corpus public fixe bien 19 % ; les V et VI proposés conservent les catégories inférieures à 20 %. Le nouveau paragraphe fiscal est placé après les trois alinéas initiaux du I afin de ne pas déplacer les définitions du deuxième alinéa ni le premier alinéa visé par renvoi. Le 12 de 39 est la dépendance par majorité/pouvoir de décision ou contrôle commun ; 206 distingue le droit commun des revenus patrimoniaux et autres régimes propres, qui ne sont pas étendus ici. La demande de prolongation et le délai d'instruction de deux mois disparaissent ; le délai matériel maximal ordinaire devient six ans ou huit ans par acquisition, en incluant les deux années déjà possibles, sans nouveau cycle pour les prolongations accordées. 1764 III, source entière lue, demeure applicable à l'engagement de fond ; son économie d'impôt de référence doit être coordonnée au taux et au fait générateur nouveaux sans compter un simple IS différé comme impôt définitivement économisé. Cette coordination de sanction est identifiée hors du lot et n'est pas annoncée faite. Nouveaux renvois non fournis comme cibles : 209 et 219, V/VI, consultés dans leurs propositions pertinentes ; 206, 12, est dans la cible fournie. Les droits SRU de quota/carence ne sont pas recréés. Aucun financement, recette induite ou effet national sur le logement n'est chiffré.",
    'mixed',
    "Les décisions préalables de prolongation et une clause fiscale de fusion sont retirées ; l'avantage est pérennisé pour les futures cessions éligibles. Le taux réduit de 19 % préexiste, donc sa simple conservation n'est pas une nouvelle baisse. Le rattachement à un compartiment du nouvel IS ajoute un suivi de catégorie commun au régime ; le solde net de coûts et de recettes reste inconnu.",
    "L'avantage reste limité aux locaux et terrains, zones et transformations ou constructions définis par la source. Les anciens délais expirés ne sont pas rouverts, hors demandes régulières encore en cours d'instruction et réserve du droit répressif plus doux. Le calcul de la sanction de 1764 III reste à coordonner ; aucune production de logements ni économie budgétaire n'est démontrée.",
    "Le rattachement des plus-values au compartiment de taux favorable est une exigence de suivi nouvelle du régime de distribution par rapport à la source, partagée avec 209 et sans état distinct créé ici. Aucune demande ou attestation ne remplace les autorisations supprimées. L'engagement de réaliser des logements, la preuve d'achèvement et le contrôle des surfaces préexistaient ; aucun quota ou condition géographique nouveau n'est ajouté.",
    effects=[
        effect('210 F','authorization_removed','transformation-logements-prolongations-de-plein-droit',
            "Suppression de l'autorisation administrative et du renouvellement de prolongation des travaux.",
            "Délais initiaux quatre ans, ou six ans pour emprise d'au moins 20 000 m² ; jusqu'à une année de prolongation sur demande, renouvelable une fois par décision.",
            "Deux années supplémentaires de plein droit, soit six ou huit ans au total, sans demande ni décision ; années déjà accordées imputées.",'legal_duty',
            "Acquéreurs et absorbantes réalisant les transformations ou constructions éligibles.",
            "Nouvelles acquisitions et délais non expirés à l'entrée en vigueur, demandes en cours incluses ; droits plus favorables acquis conservés.",
            "Aucune déclaration ou attestation de prolongation de remplacement ; achèvement et objet de l'engagement restent contrôlables.",
            "III. – Sur demande de l'acquéreur, une prolongation des délais de quatre et six ans mentionnés au II peut être accordée par l'autorité compétente de l'Etat du lieu de la situation des immeubles pour une durée n'excédant pas un an.",
            "III. – Les délais de quatre et six ans mentionnés au II sont prolongés de plein droit de deux ans, sans demande, décision administrative ou justificatif particulier de prolongation."),
        effect('210 F','coordination',FORMAL,
            "La substitution légale de l'absorbante retire la clause fiscale de fusion, dans la même mesure de suppression d'engagements formels.",
            "La continuité de l'engagement de logements dépendait d'une clause spécifique de substitution dans l'acte de fusion.",
            "L'absorbante continue l'engagement initial de plein droit, dans le délai restant à courir, sans clause distincte.",'legal_duty',
            "Sociétés absorbantes d'un acquéreur ayant souscrit l'engagement de logements.",
            "Fusions réalisées à compter de l'entrée en vigueur ; pas de dispense d'exécuter les travaux.",
            "Aucun acte ou dépôt équivalent n'est exigé ; l'engagement matériel de logements est maintenu.",
            "En cas de fusion de sociétés, l'engagement de transformation ou de construction souscrit par la société absorbée n'est pas rompu lorsque la société absorbante s'engage, dans l'acte de fusion, à se substituer à la société absorbée pour le respect de l'engagement de transformation ou de construction dans le délai restant à courir.",
            "En cas de fusion de sociétés, la société absorbante est substituée de plein droit à la société absorbée pour le respect de l'engagement de transformation ou de construction dans le délai restant à courir."),
        effect('210 F','relief_extended','transformation-logements-taux-reduit-perennisation',
            "Pérennisation de l'éligibilité au taux réduit pour les cessions futures répondant aux autres conditions.",
            "Taux de 19 % des plus-values nettes éligibles, sous conditions ; cessions avant fin 2026, ou promesse avant cette date suivie d'une cession sous deux ans.",
            "Taux de 19 % préservé, sous réserve d'un régime plus favorable, pour les mêmes plus-values éligibles sans date limite de promesse ou de cession au IV ; exigibilité nouvelle à la distribution dans son champ.",'percent',
            "Personnes morales cédantes à l'IS de droit commun et personnes morales acquéreuses remplissant les conditions de l'article.",
            "Cessions à compter de l'entrée en vigueur ; anciennes cessions et leurs droits préservés. Zones, dépendance, usages et surfaces inchangés.",
            "Aucun taux nouveau ni obligation de remplacement ; engagement de logements préexistant conservé.",
            "2° Aux cessions à titre onéreux réalisées après le 31 décembre 2026 si une promesse unilatérale ou synallagmatique de vente a été conclue au plus tard à cette date et si la cession a été réalisée au plus tard deux ans après la date de la promesse.",
            "2° Aux cessions à titre onéreux réalisées après le 31 décembre 2026, sans condition de date de la promesse ni délai entre cette promesse et la cession au titre du présent IV."),
        effect('210 F','coordination',IS,
            "Le taux favorable suit le fait générateur de distribution au lieu de taxer la plus-value conservée.",
            "Le I soumet les plus-values de cession au taux de 219 IV, dans l'IS annuel de droit commun.",
            "Même catégorie à 19 % ou régime plus favorable, exigible seulement à distribution pour les exercices du nouvel IS ordinaire.",'other',
            "Cédants relevant du droit commun de l'IS à la distribution.",
            "Exercices ouverts à compter de l'entrée en vigueur du régime nouveau ; impositions personnelles, de sortie et minimum distincts.",
            "Suivi des compartiments, même mesure d'IS ; aucune seconde baisse de taux décomptée.",
            "I. – Les plus-values nettes dégagées lors de la cession d'un local à usage de bureau ou à usage commercial ou industriel ou d'un terrain à bâtir par une personne morale soumise à l'impôt sur les sociétés dans les conditions de droit commun sont soumises à l'impôt sur les sociétés au taux mentionné au IV de l'article 219 lorsque la cession est réalisée au profit d'une personne morale.",
            "Elles sont prises en compte dans le compartiment correspondant prévu à l'article 209 et ne donnent lieu à l'impôt sur les sociétés ordinaire qu'à leur distribution.")
    ],
    benefit="Le taux réduit source de 19 % sur les plus-values nettes éligibles est conservé, avec les taux ou exonérations plus favorables du nouvel IS, et reste ouvert aux cessions futures sans fermeture fin 2026. Le régime de surfaces mixtes à partir de 75 %, avec proratisation par le rapport de surfaces, demeure entier. Le délai spécial de six ans pour les opérations d'au moins 20 000 m² est conservé avec deux ans supplémentaires de plein droit ; les prolongations déjà obtenues ne sont pas perdues ni comptées deux fois. La continuation en fusion est facilitée par substitution légale. La dispense d'amende pour circonstances exceptionnelles indépendantes de la volonté demeure applicable aux acquéreurs et absorbantes futurs. La date d'achèvement, les zones éligibles et les exclusions de dépendance restent définies. Les anciens droits et réclamations sont préservés sans remboursement général nouveau.",
    checks={
        '39': "Le 12 de l'article 39 définit les liens de dépendance par majorité du capital ou pouvoir de décision et par contrôle commun ; le I les conserve comme exclusion des cessions entre parties liées. Ni la source ni la proposition de cette cible ne transforme ce lien capitalistique en contrat de travail. Les contrôles de rémunérations de 39 et la réforme du préavis individuel sont étrangers à ce renvoi ; aucune condition d'ancienneté salariale n'est ajoutée.",
        '206': "Le I vise les personnes morales soumises à l'IS dans les conditions de droit commun. Le 12 proposé de 206 les maintient passibles tout en reportant l'IS ordinaire à distribution pour les exercices ouverts après la bascule. Les 5/5 bis, 5 ter, tonnage et minimum restent des régimes distincts : la proposition de 210 F ne les assimile pas aux cédants de droit commun. Les anciens exercices gardent leur régime ; aucune notification de rupture ou ancienneté d'emploi n'intervient."},
    removed=["La demande d'autorisation de prolongation d'un an et sa demande de renouvellement, avec décision administrative et attente de deux mois, sont supprimées au profit des deux années de plein droit déjà disponibles au maximum.",
             "L'engagement particulier de substitution à insérer dans l'acte de fusion de l'acquéreur est supprimé ; l'absorbante reprend de plein droit l'engagement de fond restant à exécuter.",
             "La date limite de promesse au 31 décembre 2026 et le délai maximal de deux ans entre promesse et cession pour les cessions postérieures sont supprimés pour l'avantage futur."])

# 210 quinquies : conserver la neutralité des subventions et la règle anti-cumul.
x = clean(BY_NUMBER['210 quinquies']['source_xml'])
x += '\n' + p("Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, les dispositions du présent article déterminent les valeurs fiscales et les résultats de référence pris en compte selon l'article 209. La reprise d'une subvention à concurrence de l'amortissement ne rend pas exigible l'impôt sur les sociétés ordinaire tant que le bénéfice correspondant demeure dans l'organisme, y compris en trésorerie. L'exigibilité suit la distribution, sous réserve des régimes distincts et des impositions de sortie expressément maintenus ; les organismes qui n'entrent pas dans ce régime conservent leurs règles propres.")
x += '\n' + p("Cette coordination s'applique aux exercices ouverts à compter de l'entrée en vigueur de la loi instituant ce régime, y compris aux fractions de subventions antérieures non encore reprises et non encore exigibles. Les valeurs fiscales, exclusions et reprises demeurent prises en compte une seule fois ; aucune créance ou réserve déjà taxée n'est utilisée deux fois. Les impositions déjà exigibles, les droits aux exonérations, les restitutions, prescriptions et recours des périodes antérieures demeurent régis par les dispositions qui leur étaient applicables. L'impôt minimum international conserve son champ propre.")
add('210 quinquies', x,
    "Coordination nécessaire de la reprise annuelle des subventions avec l'IS à la distribution. L'exclusion de la subvention lors de son versement, la réduction du prix de revient et la reprise limitée à l'amortissement lorsque la subvention réduit le service d'emprunt sont maintenues en entier. Aucun régime favorable ni aide future n'est supprimé ; aucun nouveau taux n'est proposé.",
    "Lecture intégrale des trois alinéas séparés par br, sans notes annexes. La déduction du prix de revient empêche le double usage de la subvention pour amortissements et plus-values ; elle n'est ni une taxe additionnelle ni un agrément. L'habilitation des organismes bénéficiaires de la PEEC est distincte de cet article et n'est pas réputée supprimée. La référence à l'exercice reste utile pour le résultat de référence, mais ne constitue pas un nouveau fait générateur annuel de l'IS. Renvois nouveaux non fournis dans reference-targets : 206, 12 ; 209 ; 219, V et VI, dont les propositions pertinentes du corpus ont été consultées. Les organismes au régime patrimonial de 206, 5, restent hors du régime ordinaire tant que leur texte propre s'applique. Pas de baisse des aides publiques ni de recettes dynamiques comptées ; le chiffrage net reste à établir séparément.",
    'coordination_only',
    "La source exonère déjà la subvention au versement et évite un double avantage sur son emploi. Ces règles sont maintenues ; seule leur articulation avec l'exigibilité de l'IS à distribution est précisée. Aucun nouveau prélèvement supprimé ni gain autonome de taux n'est revendiqué.",
    "Le dispositif reste limité aux versements à fonds perdus de PEEC aux sociétés ou organismes habilités. Les régimes patrimoniaux et autres impôts distincts ne sont pas différés ; aucune économie ou recette publique nette n'est calculée.",
    "Aucune charge nouvelle propre à cet article n'est identifiée : le suivi du prix de revient et des amortissements existait déjà. La coordination n'ajoute ni déclaration, registre, justificatif, habilitation ni délai et utilise le régime commun de l'IS à la distribution.",
    effects=[effect('210 quinquies','coordination',IS,
        "La reprise des subventions au rythme de l'amortissement n'impose pas un bénéfice conservé dans le régime nouveau.",
        "La subvention annuelle réduisant le service d'emprunt est rapportée au bénéfice imposable à hauteur de l'amortissement de chaque exercice.",
        "Les mêmes reprises calculent le résultat de référence ; l'IS ordinaire attend la distribution pour les organismes relevant du nouveau régime.",'other',
        "Organismes habilités recevant la PEEC et entrant dans le nouvel IS ordinaire.",
        "Exercices ouverts après la bascule et fractions antérieures non exigibles ; régimes propres des autres organismes réservés.",
        "Aucun formulaire ou registre nouveau ; même mesure d'IS, sans nouvelle baisse autonome.",
        "elle est rapportée au bénéfice imposable à concurrence du montant de l'amortissement pratiqué à la clôture de chaque exercice sur le prix de revient de cet immeuble.",
        "La reprise d'une subvention à concurrence de l'amortissement ne rend pas exigible l'impôt sur les sociétés ordinaire tant que le bénéfice correspondant demeure dans l'organisme, y compris en trésorerie.")])

# 210 sexies : retirer les plafonds propres, conserver le droit commun anti-abus.
x = p("La rémunération prévue à l'article L. 225-45 du code de commerce allouée au titre d'un exercice aux membres du conseil d'administration ou du conseil de surveillance des sociétés anonymes est déductible du résultat fiscal de référence dans les conditions de l'article 39 du présent code, lorsqu'elle correspond à un travail effectif et n'est pas excessive eu égard à l'importance du service rendu. Aucun plafond propre calculé à partir des rémunérations des salariés les mieux rémunérés ou du nombre de salariés de la société n'est applicable au titre du présent article.")
x += '\n' + p("Cette règle s'applique également aux sociétés anonymes employant moins de cinq personnes, sans plafond forfaitaire par membre du conseil. Elle ne permet ni la déduction d'une rémunération fictive ou excessive ni une double déduction des mêmes frais ou rémunérations. Une rémunération correspondant à un travail effectif et non excessive n'est pas une distribution du seul fait du dépassement des plafonds supprimés par le présent article ; la fiscalité personnelle du bénéficiaire conserve son régime propre.")
x += '\n' + p("La suppression des plafonds s'applique aux rémunérations allouées au titre des exercices ouverts à compter de l'entrée en vigueur de la loi portant cette suppression. Les exercices antérieurs, les déductions, impositions, restitutions, prescriptions et recours qui s'y rapportent demeurent régis par les dispositions qui leur étaient applicables. Pour les exercices relevant du régime de distribution prévu au 12 de l'article 206 et aux V et VI de l'article 219, la détermination du résultat de référence selon l'article 209 ne rend pas exigible l'impôt sur les sociétés ordinaire sur les bénéfices conservés. Les rémunérations réelles versées ne constituent pas, par elles-mêmes, une distribution ; les avantages personnels dissimulés conservent leur qualification propre.")
add('210 sexies', x,
    "Réduction de fond des restrictions de déduction : suppression du plafond de 5 % du produit des salaires de référence par le nombre de conseillers et du plafond de 457 € par membre pour les sociétés de moins de cinq salariés. Le renvoi aux cinq/dix salariés les mieux rémunérés devient inutile et disparaît. La déduction est ouverte selon le travail effectif et la rémunération non excessive de 39, avec contrôle des avantages personnels et sans nouvelle formalité. La coordination d'IS évite d'assimiler une dépense professionnelle réelle à une distribution.",
    "Lecture des trois paragraphes entiers. Le plafond de 457 € n'est pas remplacé par un montant inventé : sa suppression donne accès aux mêmes conditions générales, y compris pour les petites sociétés futures. La cible 39, 5 définit cinq ou dix personnes selon le seuil de 200 salariés ; ces définitions restent valables pour ses autres emplois mais ne sont plus utilisées pour plafonner les conseils. Les conditions du 1, 1° sur travail effectif et non-excès et le non-double emploi du 3 restent utiles. L'article L225-45 du code de commerce désigne la rémunération visée, non les contrats de travail ; son contenu n'est pas réécrit dans ce lot. Nouveaux renvois non fournis comme cibles : 206, 12 ; 209 ; 219, V/VI, consultés dans les propositions pertinentes du corpus. Ni rémunérations fictives ni avantages personnels dissimulés ne sont défiscalisés. L'effet sur l'assiette effectivement distribuée dépend des rémunérations et autres limites applicables ; aucun rendement ni compensation n'est inventé.",
    'material_reduction',
    "Les deux plafonds fiscaux particuliers disparaissent par rapport à la source officielle entière. Les rémunérations réelles et non excessives auparavant plafonnées deviennent déductibles selon le droit commun ; il s'agit d'une extension conditionnelle de déduction, sans promesse de réduction chiffrée pour chaque société et sans baisse du taux personnel des administrateurs.",
    "Seules les rémunérations L225-45 des conseils des SA et les nouveaux exercices sont couverts. Travail effectif, non-excès et autres règles de déduction demeurent. Les montants bénéficiaires et le coût public net ne sont pas établis ; le régime d'emploi des dirigeants ne change pas.",
    "Aucune charge nouvelle propre au dispositif n'est identifiée : les conditions de travail effectif et de non-excès proviennent déjà de 39 et aucun état, preuve spéciale, registre ou autorisation ne remplace le calcul des plafonds. Les données ordinaires de rémunération restent utilisables pour le contrôle existant.",
    effects=[effect('210 sexies','relief_extended','remunerations-conseils-sa-plafonds-suppression',
        "Suppression des deux plafonds propres de déductibilité des rémunérations de conseil.",
        "Déduction limitée à 5 % de la moyenne des rémunérations déductibles des salariés de référence multipliée par le nombre de conseillers ; dans le cas des SA de moins de cinq personnes non conformes au 5 de 39, plafond de 457 € par membre.",
        "Déduction des mêmes rémunérations sans ces plafonds, sous les conditions générales de travail effectif et de non-excès ; aucune modification d'un taux d'impôt.",'other',
        "Sociétés anonymes versant les rémunérations L225-45 aux membres de leur conseil d'administration ou de surveillance.",
        "Rémunérations allouées au titre des exercices ouverts à compter de l'entrée en vigueur ; exercices et droits antérieurs conservés.",
        "Aucune déclaration nouvelle ; contrôle de rémunérations effectives et non excessives préexistant.",
        "La rémunération prévue à l'article L. 225-45 du code de commerce allouée au titre d'un exercice aux membres du conseil d'administration ou du conseil de surveillance des sociétés anonymes est déductible de l'assiette de l'impôt sur les sociétés dans la limite de 5 % du produit obtenu en multipliant la moyenne des rémunérations déductibles attribuées au cours de cet exercice aux salariés les mieux rémunérés de l'entreprise par le nombre des membres composant le conseil.",
        "Aucun plafond propre calculé à partir des rémunérations des salariés les mieux rémunérés ou du nombre de salariés de la société n'est applicable au titre du présent article.")],
    checks={'39': "La source renvoie au 5 de 39 pour les cinq ou dix salariés les mieux rémunérés, selon l'effectif de 200 salariés. Ce renvoi servant uniquement au plafond retiré disparaît ; les définitions de la cible restent intactes pour ses autres usages. Le nouveau renvoi aux conditions du 1, 1° et au non-double emploi du 3 conserve le travail effectif et le contrôle du montant excessif. Le nombre de salariés ne fixe plus la déduction du conseil, et aucune durée d'emploi ou notification de rupture n'est créée."},
    removed=["Le plafond spécial de déduction égal à 5 % du produit de la moyenne des salaires de référence par le nombre de membres du conseil est supprimé.",
             "Le plafond forfaitaire de 457 euros par membre du conseil pour les sociétés anonymes de moins de cinq personnes concernées est supprimé.",
             "Le calcul particulier des salaires de référence des personnes les mieux rémunérées, requis pour ce seul plafond de conseil, n'est plus exigé au titre de cet article."])

# 211 et 211 bis : conserver le droit à déduction et l'interdiction de doubler des frais.
add('211', None,
    "Maintien intégral utile : la déduction des rémunérations de gérants et associés pour un travail effectif est un avantage à préserver, et son articulation avec l'IR de l'article 62 empêche de traiter ces paiements comme bénéfices sans bénéficiaire imposé. Les règles de majorité familiale et les exclusions des sociétés transparentes gardent un objet de qualification ; aucune autorisation ou transmission particulière ne peut être supprimée ici. Le texte ne fixe pas une échéance annuelle d'IS sur le bénéfice conservé.",
    "Lecture des huit paragraphes, sans notes. Le 3 de 39 et 211 bis visent le non-cumul des allocations forfaitaires avec le remboursement des mêmes frais ; ils restent cohérents et ne sont pas abrogés par les suppressions de plafonds de 210 sexies. 206, 3, vise des options fiscales pour des personnes ou groupements précisément énumérés, non des contrats de travail. Son 12 proposé ne fait pas perdre l'assujettissement et ne supprime pas l'impôt personnel du bénéficiaire. Les exceptions de 1655 ter et des options 239 bis AA/AB demeurent intégrales, ainsi que le a périmé, qui n'est pas un emplacement Réservé. Aucune condition d'ancienneté, indemnité de licenciement ni préavis de quinze jours n'est en jeu. La coordination générale de 209 fait du bénéfice le résultat de référence ; aucune cotisation annuelle autonome ne résulte de cet article et aucune modification propre n'est nécessaire.",
    'retained_necessary',
    "Aucun changement de fond : le droit à déduction pour les rémunérations réelles et les qualifications de leurs bénéficiaires sont conservés. Les contrôles de réalité et de double emploi sont nécessaires ; aucun dossier ou prélèvement propre susceptible d'être retiré n'est institué par cette source. L'article ne compte pas comme simplifié.",
    "Le maintien ne modifie ni les régimes d'IR des bénéficiaires ni les options fiscales des sociétés et n'évalue pas leur coût. Les nouvelles règles de rupture du contrat privé ne sont pas applicables à ces renvois fiscaux en tant que tels.",
    "Aucune charge nouvelle n'est identifiée, le texte et ses conditions restant intégralement ceux de la source. Aucune attestation de travail, déclaration, donnée de famille ou preuve supplémentaire n'est ajoutée aux règles existantes.",
    checks={
        '39': "Le premier alinéa du I vise le 3 de 39 : l'allocation forfaitaire de représentation ou déplacement n'est pas déductible si les charges comprennent déjà les frais habituels remboursés. Le renvoi conserve sa portée et la déduction pour un travail effectif demeure, sans renvoi aux plafonds de conseil supprimés. Ce contrôle fiscal ne dépend ni d'une ancienneté d'emploi d'un an ni d'une notification de rupture ; il n'est pas le barème du contrat unique.",
        '206': "Le renvoi à 206, 3 vise l'option à l'IS des sociétés en commandite simple, SNC, sociétés en participation et sociétés civiles visées par 211. Le 12 proposé de la cible maintient leur assujettissement dans le régime de distribution et préserve les options de sociétés de personnes. Le droit à déduction et l'IR du bénéficiaire de 211 restent cohérents pour les exercices nouveaux comme anciens ; aucune option fiscale n'est une durée de contrat ou un préavis individuel."})

add('211 bis', None,
    "Maintien intégral nécessaire : l'article définit, selon les formes sociales à l'IS, les dirigeants auxquels s'applique l'interdiction de déduire deux fois des frais déjà remboursés prévue au 3 de 39. Il ne plafonne pas la rémunération, ne demande pas de formalité nouvelle et conserve les exclusions favorables des sociétés immobilières transparentes et SARL aux régimes 239 bis AA/AB. Sa suppression étendrait ou désorganiserait la règle de non-double emploi, sans allègement administratif démontré.",
    "Lecture des cinq paragraphes et de tous les br ; absence de note. Le premier alinéa du 3 de 39 reste présent dans la source et la proposition de référence, avec son contrôle des mêmes frais habituels déjà remboursés. Le II b/c de 211 et les exceptions b/c de 211 bis ne sont pas fusionnés : ils visent des champs distincts. Le a périmé n'est ni une obligation future ni un emplacement Réservé. Le renvoi n'impose aucun IS annuel sur un bénéfice conservé ; il qualifie seulement une déduction dans le résultat de référence. La suppression des plafonds propres de 210 sexies n'abroge pas cette règle générale de double emploi. Les fonctions spéciales de dirigeants ne constituent pas une catégorie de CDD et ne rétablissent ni une autorisation collective de rupture ni une durée d'emploi.",
    'retained_necessary',
    "Les qualifications et exceptions de la source restent intégralement applicables ; aucun avantage ou taux n'est modifié. La règle sert seulement le contrôle d'une déduction en double et ne porte pas de transmission ou agrément propre à retirer. Aucune simplification matérielle n'est comptée.",
    "Le maintien est limité à la définition des dirigeants et aux exceptions de non-double emploi. La fiscalité personnelle, le droit des mandats sociaux et les contrats de travail éventuels conservent leurs régimes ; aucun coût net global n'est établi.",
    "Aucune charge nouvelle n'est identifiée car la source demeure entière. Le texte ne crée ni état de frais distinct, ni donnée supplémentaire, ni délai, registre ou autorisation et n'ajoute aucune condition aux exceptions maintenues.",
    checks={'39': "La cible 39, 3, premier alinéa écarte seulement le double emploi de frais habituels de représentation ou déplacement déjà remboursés avec des allocations forfaitaires. 211 bis complète la définition des dirigeants pour les sociétés relevant du régime des capitaux ; son champ et ses exclusions restent nécessaires. La proposition cible conserve cette règle. Ni le seuil d'un an d'indemnité, ni l'ancienneté, ni la notification du contrat unique n'y sont visés, et le renvoi n'est pas détourné vers ces régimes."})

# 211 ter : la limite législative entre en tension avec l'ouverture déjà écrite
# dans l'annexe III 41 A. Pas de faux gain monétaire annoncé sur ce fondement.
x = p("Le présent article est abrogé pour l'établissement de l'impôt sur les sociétés au titre des aides versées à compter de l'entrée en vigueur de la loi portant cette abrogation. La limitation de l'application de l'article 39 quinquies aux seules entreprises industrielles, commerciales ou agricoles cesse de s'appliquer pour cet impôt. La déduction prévue à l'article 39 quinquies demeure ouverte aux entreprises qui remplissent ses autres conditions, quelle que soit la nature de leur activité, sans nouvelle option, déclaration ou habilitation du donateur au titre du présent article.")
x += '\n' + p("Les aides versées avant cette entrée en vigueur, les déductions et avantages qui s'y rapportent, les impositions déjà exigibles, restitutions, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables, y compris les dispositions plus favorables dont les contribuables pouvaient légalement bénéficier. La présente abrogation ne remet pas en cause les conditions propres aux organismes destinataires, le caractère définitif du versement ni l'interdiction d'un avantage personnel au dirigeant ou à sa famille ; elle ne modifie pas les règles propres à l'impôt sur le revenu et ne crée aucune restitution générale d'impositions anciennes.")
add('211 ter', x,
    "Abrogation prospective de la seule restriction de nature d'activité pour la déduction d'aides au logement à l'IS ; maintien du fondement favorable de 39 quinquies et de ses autres conditions. La source ne contient aucune autre règle à reproduire. Il s'agit surtout d'une coordination : l'annexe III 41 A admet déjà les professions non commerciales, ce qui interdit de présenter leur accès comme une baisse d'impôt entièrement nouvelle démontrée par ce seul article.",
    "La phrase source entière a été lue. 39 quinquies et sa note renvoyant aux articles 41 A à 41 D de l'annexe III ont été consultés ; les articles publics disponibles 41 A, 41 B et 41 D ont été lus intégralement. 41 A vise déjà les contribuables de profession non commerciale, en tension avec l'exclusivité littérale de 211 ter. Ce conflit préexistant est signalé et retiré au niveau législatif pour l'IS, sans revendiquer un avantage chiffré inédit ; 41 A doit être coordonné à l'ouverture statutaire sans affaiblir les droits d'IR qu'il accorde. 41 B maintient l'affectation logement, la perte définitive des fonds et l'absence d'avantage aux dirigeants ou à leur famille ; 41 D maintient son champ de destinataires. Aucun 41 C actif n'a été trouvé dans ce fichier public ; il n'est pas supposé lu ou abrogé. Pas de nouveaux renvois normatifs en dehors des articles déjà visés par la source ; les articles d'annexe sont des références documentaires de contrôle. L'habilitation des organismes destinataires n'est pas un agrément d'employeur supprimé ici. Aucune cotisation PEEC ou dépense publique n'est abolie par ce texte.",
    'coordination_only',
    "La restriction législative d'activité est retirée pour l'avenir à l'IS, avec conservation de la déduction de logement. L'annexe III prévoit déjà les professions non commerciales : l'effet fiscal additionnel n'est donc pas démontré et aucune nouvelle baisse monétaire n'est décomptée. Le retrait résout une contradiction de champ plutôt qu'il ne prouve un gain national.",
    "L'ouverture concerne l'IS et conserve les conditions de l'aide et de son destinataire ; l'IR n'est pas réformé. Les champs réglementaires restent à coordonner, et l'existence d'une nouvelle population réellement privée de déduction sous le droit complet n'est pas établie.",
    "Aucune charge nouvelle n'est identifiée : la restriction est retirée sans option, déclaration, agrément ou donnée de remplacement. Les garanties d'affectation, de versement à fonds perdus et de non-avantage personnel sont déjà prévues par les textes d'application.",
    effects=[effect('211 ter','coordination','aides-logement-restriction-activite-suppression',
        "Retrait de la restriction législative de nature d'activité, en coordination avec l'ouverture déjà écrite en annexe III.",
        "211 ter limite littéralement 39 quinquies aux activités industrielles, commerciales ou agricoles ; 41 A admet déjà les professions non commerciales.",
        "La limitation ne subsiste plus à l'IS, sans retirer les autres conditions ni revendiquer une nouvelle déduction déjà ouverte par le règlement.",'regime',
        "Entreprises à l'IS versant une aide éligible au logement, quelle que soit leur activité.",
        "Aides versées à compter de l'entrée en vigueur ; droits plus favorables et litiges antérieurs conservés.",
        "Aucune option ou déclaration de remplacement ; coordination de l'annexe III restant à effectuer.",
        "Les dispositions de l'article 39 quinquies ne sont applicables qu'aux entreprises industrielles, commerciales ou agricoles.",
        "La limitation de l'application de l'article 39 quinquies aux seules entreprises industrielles, commerciales ou agricoles cesse de s'appliquer pour cet impôt.")],
    repeal="Suppression prospective de la restriction exclusive aux activités industrielles, commerciales ou agricoles pour les aides au logement déductibles à l'IS, sans abroger la déduction ni ses autres garanties.")

# 212 : une incohérence de subdivision préexistante exige une coordination.
x = clean(BY_NUMBER['212']['source_xml'])
x = replace_once(x, "mentionnées au 1 du VI de l'article 212 bis.",
    "mentionnées au 1 du VIII de l'article 212 bis.")
x += '\n' + p("V. – La rectification du renvoi au III bis s'applique aux déductions opérées à compter de l'entrée en vigueur de la loi portant cette rectification. Elle n'éteint ni le solde d'intérêts demeurant reportable ni les déductions antérieures régulièrement obtenues ; les contrôles, restitutions, prescriptions et recours antérieurs sont préservés. Une même charge ne peut être déduite deux fois.")
x += '\n' + p("Les déductions complémentaires légalement applicables en vertu de l'article 212 bis ne sont pas écartées par cette rectification du renvoi. Le IV demeure applicable aux sociétés coopératives qui en remplissent les conditions, y compris pour les situations éligibles futures.")
add('212', x,
    "Coordination nécessaire du renvoi préexistant du III bis : le report des charges financières non déduites se trouve au 1 du VIII de l'article 212 bis actuel, et non au 1 du VI. Aucune nouvelle déduction ni suppression de plafonnement n'est revendiquée. L'alternative de taux indépendant plus élevé, les subdivisions abrogées et la dispense de capital entièrement libéré pour les sociétés coopératives sont intégralement maintenues.",
    "Lecture des sept paragraphes et de la note d'application aux exercices clos à compter du 31 décembre 2025, qui n'est pas une date de réforme à inventer. 212 bis a été lu intégralement dans le corpus public : son VI porte sur la déduction complémentaire de 75 % liée au ratio de fonds propres d'un groupe consolidé, tandis que son VIII, 1, porte le report des charges financières non déduites. L'ancien renvoi « 1 du VI » est donc une incohérence de subdivision expressément signalée ; sa rectification ne supprime pas les limites de 212 bis et ne crée pas un report sans conditions. Ce nouvel emplacement de cible n'est pas fourni dans reference-targets ; aucune reference_check supplémentaire n'est ajoutée aux exigences vides de cet article. Le I conserve les renvois de taux et de dépendance à 39 ; le IV conserve l'exception coopérative au deuxième alinéa du 3° du 1 de 39. Dans le régime nouveau, la déduction établit le résultat de référence selon 209, sans exiger d'IS ordinaire annuel sur le bénéfice conservé ; aucun échéancier propre n'est institué ici. Les limitations de financement, régimes de groupe et contraintes européennes de lutte contre l'évasion gardent leur champ ; aucune conformité globale n'est présumée.",
    'coordination_only',
    "Le droit au report du reliquat d'intérêts antérieur à 2019 est rendu lisible par son rattachement à la subdivision actuelle qui contient effectivement ce report. Le droit visé reste soumis aux mêmes conditions générales ; aucune baisse de taux, nouvelle déduction autonome ou suppression des plafonds financiers n'est comptée.",
    "La coordination est limitée au reliquat défini au III bis et aux déductions nouvelles ; elle n'abroge ni les taux de référence du I ni 212 bis ou les régimes de groupe. Les anciennes déductions, réclamations et l'exception coopérative demeurent, sans coût net chiffré.",
    "Aucune charge nouvelle n'est identifiée : seul l'emplacement du report est rectifié, sans état, calcul distinct, donnée, option, délai ou justificatif supplémentaire. La règle de non-double déduction précise la continuité du même reliquat et ne crée pas une procédure de remplacement.",
    effects=[effect('212','coordination','interets-anciens-report-renvoi-212bis',
        "Correction explicite d'un renvoi incohérent au mécanisme actuel de report des charges financières non déduites.",
        "Le III bis renvoie au 1 du VI de 212 bis, dont le VI actuel traite d'une déduction complémentaire de groupe et ne porte pas le report visé.",
        "Le III bis renvoie au 1 du VIII de 212 bis, qui organise la déduction ultérieure du reliquat sous ses limites.",'other',
        "Entreprises disposant du solde d'intérêts non imputé au dernier exercice ouvert avant le 1er janvier 2019.",
        "Déductions à compter de l'entrée en vigueur ; déductions régulières, soldes, restitutions et recours antérieurs préservés.",
        "Aucune formalité nouvelle ni plafond retiré ; pas de deuxième usage de la même charge.",
        "mentionnées au 1 du VI de l'article 212 bis.",
        "mentionnées au 1 du VIII de l'article 212 bis.")],
    benefit="L'alternative permettant de déduire les intérêts au taux de marché indépendant lorsqu'il excède le taux de référence du 3° du 1 de 39 demeure entière. Le reliquat antérieur à 2019 n'est ni éteint ni amputé par la correction de subdivision ; il suit le mécanisme de report réellement présent au VIII, 1 de 212 bis, sans double déduction, et les déductions complémentaires légalement applicables de cet article ne sont pas écartées. Le IV conserve pour les coopératives la dispense de capital entièrement libéré visée au deuxième alinéa du 3° du 1 de 39. Ces deux avantages de taux et de dispense restent ouverts aux situations futures éligibles ; le solde ancien garde son titulaire et ses droits de réclamation.")


assert [a['number'] for a in ANSWERS] == [a['number'] for a in SOURCES]
assert len(ANSWERS) == 12
for a in ANSWERS:
    imp = a['substantive_impact']
    for f in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(imp[f]) >= 40
    if a['proposed_xml'] is not None:
        for e in imp['effects']:
            assert len(e['proposed_quote']) >= 12
            assert e['proposed_quote'] in text_of(a['proposed_xml']), (a['number'], e['proposed_quote'])
    for c in a['reference_checks']:
        assert len(c['assessment']) >= 80
    for description in a.get('removed_provisions', []):
        assert len(description) >= 30
    if a.get('change_type') == 'full_repeal':
        assert len(a['repeal_scope']) >= 30

(ROOT / 'answer.json').write_text(json.dumps(ANSWERS, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(ANSWERS)}, ensure_ascii=False))
