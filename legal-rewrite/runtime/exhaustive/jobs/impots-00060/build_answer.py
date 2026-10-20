import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
targets = json.loads(Path('reference-targets.json').read_text())
answers = []


def base(i):
    source = sources[i]
    return {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}


def retained(i, reason, notes, assessment, limitations, burdens):
    answer = base(i)
    answer.update(
        proposed_xml=None,
        reason=reason,
        review_notes=notes,
        status='retained_unchanged',
        classification='retained_necessary',
        substantive_impact={
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limitations,
            'new_burdens_review': burdens,
            'effects': [],
        },
        reference_checks=[],
    )
    answers.append(answer)
    return answer


retained(0,
    "Maintien intégral après examen : le calcul séparé de chaque entité apatride empêche de diluer sa sous-imposition dans celle d'autres entités. Il ne crée ni déclaration distincte ni agrément. Supprimer cette séparation altérerait le minimum international que la coordination conserve ; aucune réécriture stylistique n'est proposée.",
    "Articulation contrôlée avec 223 WB, qui calcule normalement par Etat ou territoire, et 223 WD quater, qui exclut les apatrides du de minimis. La note conserve son application aux exercices ouverts à compter du 31 décembre 2023. Ce minimum demeure distinct de l'IS ordinaire à la distribution.",
    "La source officielle entière est conservée : aucun impôt, calcul séparé ou délai n'est supprimé. La séparation est nécessaire au traitement d'une entité sans rattachement territorial.",
    "La décision ne statue pas sur le montant dû par un groupe particulier ni sur les données de calcul hors de cet article ; aucun gain budgétaire ou de conformité n'est démontré.",
    "Aucune charge nouvelle identifiée : le texte source reste seul applicable et aucun relevé, registre ou condition de réinvestissement n'est ajouté.")

retained(1,
    "Maintien nécessaire du recalcul consécutif à une correction d'impôts couverts ou de résultat qualifié. Il assure la cohérence de la liquidation et des options favorables auxquelles les renvois se rapportent ; il ne s'agit pas d'une contribution additionnelle au nouvel IS ordinaire. Aucune formalité autonome retirable n'est prescrite ici.",
    "Lecture des cibles publiques 223 VO decies, VU sexies, VX, VX quater et WS quinquies, ainsi que du III de 223 WH bis : respectivement imputation immobilière, reprise de différés, correction d'impôts, impayés et reprises du régime éligible des distributions. Le renvoi à WS quinquies n'étend pas ce dernier à un nouveau régime français de 2026 : 223 VK, 39°, exige notamment une entrée en vigueur au plus tard le 1er juillet 2021. L'exercice de recalcul reste celui de l'exigibilité de l'additionnel ; note historique du 31 décembre 2023 inchangée.",
    "Aucune réduction n'est attribuée à ce maintien : la source conserve le recalcul de l'exercice antérieur et l'exigibilité de l'additionnel pendant l'exercice du nouveau calcul.",
    "Les effets des corrections peuvent différer selon les groupes. La conformité du futur IS à la distribution et le solde de finances publiques ne sont pas établis par cet article.",
    "Aucune charge nouvelle identifiée : les renvois et l'exigibilité existants sont maintenus sans seconde déclaration ni autorisation de remplacement.")

retained(2,
    "Maintien de la règle d'affectation lorsque le nouveau calcul porte sur un exercice antérieur mais qu'aucun bénéfice qualifié net n'existe dans l'exercice courant. Le quotient définit un bénéfice qualifié pour cette affectation, non un nouvel impôt autonome ; le retirer laisserait une liquidation sans clé d'attribution.",
    "223 WB ter répartit selon les bénéfices ; 223 WB quater prend les bénéfices des exercices corrigés lorsqu'aucun bénéfice net n'est constaté. La division par le taux minimum n'est ni le barème de l'IS ordinaire ni une taxe sur les réserves. Note de 2025 : exercices clos à compter du 31 décembre 2024, sans substitution par une date de réforme future.",
    "La source entière demeure : l'affectation de l'additionnel en situation de résultat courant non bénéficiaire est conservée, sans baisse de montant ni report nouveau.",
    "Aucun montant par entité n'est calculable sans les impôts et bénéfices du groupe. L'article ne traite ni des groupes hors du champ de 223 VL ni de la fiscalité personnelle.",
    "Aucune charge nouvelle identifiée : aucune donnée, option, notification ni pièce justificative supplémentaire n'est introduite par le maintien.")

retained(3,
    "Maintien intégral de la clé de répartition de l'additionnel de 223 VT quater : quotient par le taux minimum, prorata des écarts et limitation aux seules entités auxquelles ce régime s'applique. Ces trois règles sont complémentaires et leur retrait élargirait ou désorganiserait la répartition, sans charge formelle redondante à supprimer.",
    "La source publique de 223 VT quater conserve l'option permettant de reporter l'écart au lieu de payer l'additionnel immédiatement ; cet article de répartition ne la neutralise pas. Les affectations de 223 WB ter et quater restent visées. La note d'application aux exercices ouverts à compter du 31 décembre 2023 est conservée.",
    "Aucune simplification nouvelle revendiquée : la règle entière reste nécessaire pour affecter l'impôt aux entités concernées, sans le reporter sur toutes les entités du groupe.",
    "L'option de report relève de 223 VT quater et ne constitue pas une suppression de taxe. Son incidence de trésorerie n'est pas chiffrée dans ce lot.",
    "Aucune charge nouvelle identifiée : maintien des seules opérations de liquidation existantes, sans état de suivi ni déclaration supplémentaire créé ici.")

retained(4,
    "Maintien du rattachement des bénéficiaires d'une affectation d'additionnel aux règles de collecte des sous-sections 2 et 3 de la section V. Cette qualification est nécessaire pour que l'impôt déjà calculé ait un redevable ; elle n'instaure pas une deuxième taxe ni une procédure de classement sur demande.",
    "Les sous-sections visées correspondent à l'inclusion du revenu et aux bénéfices insuffisamment imposés ; elles ne désignent pas l'IS ordinaire. La distinction entre apatrides et entités territorialisées, les clés de 223 WB ter/quater et la note d'application du 31 décembre 2023 sont conservées.",
    "La disposition officielle entière est maintenue sans nouvelle qualification ni nouveau prélèvement. Aucun gain ne découle d'une simple suppression de mots dans cette règle de collecte.",
    "La qualification ne préjuge pas du montant finalement recouvré après les imputations et exclusions applicables, maintenues ailleurs dans le lot.",
    "Aucune charge nouvelle identifiée : aucune demande de reconnaissance, autorisation ou preuve d'une qualification fiscale n'est ajoutée.")

a = retained(5,
    "Maintien intégral de l'exclusion de minimis, favorable aux implantations de faible activité : moyennes de trois exercices, chiffre d'affaires strictement inférieur à dix millions d'euros et perte ou bénéfice strictement inférieur à un million d'euros. L'option garde l'accès à un impôt complémentaire nul ; ni ses seuils ni ses exercices de référence ne sont resserrés.",
    "Renvois contrôlés vers 223 WD bis/ter/quater pour l'exercice de l'option, les exercices absents et les entités exclues, et vers la définition du bénéfice net de 223 VK, 1°. Les ajustements de résultat demeurent ceux de la sous-section 1 de la section III. Pas de nouvelle attestation de faible activité. Note du 31 décembre 2023 conservée.",
    "La source conserve un avantage existant, y compris pour les implantations futures éligibles. Il ne s'agit ni d'une exonération nouvelle ni d'une nouvelle baisse démontrée.",
    "Les entités apatrides et d'investissement restent soumises à 223 WD quater ; les groupes et années non éligibles ne bénéficient pas d'une extinction générale du minimum.",
    "Aucune charge nouvelle identifiée : les deux conditions et l'option existantes sont maintenues sans dossier, agrément ou justification supplémentaire.")
a['benefit_review'] = "L'avantage est la mise à zéro de l'impôt complémentaire territorial sur option lorsque les deux moyennes respectent les seuils de dix millions et d'un million d'euros, ou lorsque la seconde est une perte. Tous ces éléments restent applicables aux exercices futurs éligibles ; aucune restriction aux seuls droits antérieurs, aucun plafond nouveau et aucune pièce supplémentaire ne sont introduits."

retained(6,
    "Maintien du support unique de l'option de minimis et de sa reconduction tacite. La déclaration de 223 WW est déjà due au titre du minimum international ; cet article n'exige ni formulaire autonome ni renouvellement positif annuel. Retirer la reconduction ou le droit de renoncer rendrait l'option moins favorable ou son exercice incertain.",
    "Le II de 223 WW, lu dans le corpus public, porte la déclaration d'informations ; l'option est exercée la première année et la renonciation sur la déclaration du dernier exercice d'application. Le maintien de ce circuit n'est pas un rétablissement de l'annualité de l'IS ordinaire. Note du 31 décembre 2023 inchangée.",
    "Maintien d'une formalité minimale déjà intégrée à une déclaration existante et d'un renouvellement tacite favorable. Aucune nouvelle fusion ni suppression d'obligation n'est comptée.",
    "La déclaration internationale générale de 223 WW n'est pas réécrite dans ce lot ; son coût total et les possibilités d'échanges internationaux restent à examiner dans son propre champ.",
    "Aucune charge nouvelle identifiée : aucune confirmation annuelle, dossier d'option séparé ni délai de renonciation supplémentaire n'est ajouté.")

retained(7,
    "Maintien nécessaire du calcul des moyennes en l'absence d'activité pertinente pendant un des deux exercices antérieurs. Exclure cet exercice du dénominateur rend opératoire le régime de minimis pour une implantation récente sans exiger de reconstituer des données inexistantes ; la condition source n'est pas élargie par paraphrase.",
    "La source vise l'absence de chiffre d'affaires ou de perte qualifiée dans les termes exacts de l'article ; aucune substitution silencieuse par une autre définition d'inactivité. Les 1° et 2° de 223 WD restent les moyennes concernées. Note d'application du 31 décembre 2023 maintenue.",
    "La règle particulière de moyenne est conservée pour les futures périodes éligibles, sans nouvel avantage comptabilisé et sans suppression du de minimis.",
    "L'incidence sur les seuils dépend des exercices effectivement présents ; aucune économie d'impôt uniforme ne peut être déduite de ce maintien.",
    "Aucune charge nouvelle identifiée : aucune comptabilité d'un exercice inexistant, attestation négative ou déclaration spécifique n'est créée.")

retained(8,
    "Maintien des exclusions des apatrides et des entités d'investissement du de minimis et du calcul de ses moyennes. Ces entités relèvent d'un traitement séparé ; enlever la seconde phrase pourrait relever les moyennes des autres entités et leur faire perdre l'avantage. Aucune formalité autonome à retirer n'est contenue dans la disposition.",
    "Articulation avec le calcul distinct des apatrides de 223 WB quinquies et le régime séparé des entités d'investissement de 223 WT à WT quinquies, dont le champ n'est pas assimilé à celui de l'IS ordinaire. La note conserve les exercices ouverts à compter du 31 décembre 2023.",
    "La source entière conserve le périmètre du de minimis sans dilution de calcul ni aggravation pour les autres entités. Aucun allègement nouveau n'est revendiqué.",
    "Le maintien ne dispense pas les entités exclues du minimum auquel elles sont soumises dans leur régime propre ; il ne chiffre aucun solde pour le groupe.",
    "Aucune charge nouvelle identifiée : les exclusions existantes restent des règles de calcul, sans registre ou démarche d'autorisation ajouté.")

retained(9,
    "Maintien des quatre définitions nécessaires au traitement des détentions minoritaires. Le seuil de participation inférieur ou égal à 30 %, les titres de contrôle et les détentions directes ou indirectes sont conservés ; les remplacer par une catégorie unique modifierait le périmètre du minimum et ses répartitions plutôt que supprimer une formalité.",
    "Les catégories commandent les calculs distincts de 223 WE bis et WE ter. Le seuil de 30 % concerne la participation de l'entité mère ultime, pas une exonération de participation ni un taux fiscal. Aucune obligation de créer un sous-groupe juridique n'est ajoutée. Note du 31 décembre 2023 conservée.",
    "Les quatre catégories officielles demeurent intégralement. Leur conservation ne constitue pas une fusion de régimes ni une réduction de prélèvement.",
    "La qualification requiert les liens de participation réels ; le lot ne détermine pas la qualification d'un groupe donné ni le coût global de sa consolidation.",
    "Aucune charge nouvelle identifiée : maintien de définitions fiscales, sans nouvelle personne morale, registre des participations ou autorisation préalable imposé ici.")

retained(10,
    "Maintien de la détermination séparée du taux et de l'impôt du sous-groupe minoritaire, avec exclusion corrélative de ses impôts et résultats du groupe principal. Cette exclusion évite de comptabiliser deux fois les mêmes éléments ; supprimer un seul des deux alinéas créerait un déséquilibre sans alléger une obligation indépendante.",
    "Le traitement distinct vaut pour les sections III à VII dans leur champ fiscal. Le paragraphe 1 de la sous-section 3 de la section III reste la référence au calcul du taux effectif. Aucun élargissement du seuil de 30 % de 223 WE ; note du 31 décembre 2023 préservée.",
    "Maintien intégral d'un calcul séparé et de sa contrepartie de non-double comptage. Aucune nouvelle réduction de taxe ni de déclaration n'est démontrée.",
    "La suppression du calcul distinct supposerait une coordination du minimum international, non décidée ici. Aucun gain net de complexité n'est présumé.",
    "Aucune charge nouvelle identifiée : aucun compte, déclaration ou structure distincte supplémentaire ne résulte de la conservation des deux alinéas.")

retained(11,
    "Maintien du calcul séparé de l'entité minoritaire isolée, de l'exclusion de ses impôts et résultats du groupe et de la priorité du régime des entités d'investissement. Le troisième alinéa protège ce champ spécial ; son retrait ne serait pas une simplification neutre. Aucun agrément, délai minimal ou dossier redondant n'est prescrit ici.",
    "Les sources publiques de 223 WT et WT quinquies confirment le calcul séparé et la part attribuable au groupe pour les entités d'investissement. Le renvoi complet WT à WT quinquies reste applicable ; le maintien ne supprime aucune option propre à ce régime. Note du 31 décembre 2023 inchangée.",
    "La source officielle entière est conservée : traitement de l'entité isolée et réserve du régime d'investissement, sans gain nouveau attribué à leur maintien.",
    "Les résultats peuvent dépendre des options spéciales et des participations ; aucune réduction nette du minimum ni de la charge comptable n'est calculée.",
    "Aucune charge nouvelle identifiée : aucun second calcul pour les entités déjà régies exclusivement par l'exception du troisième alinéa n'est ajouté.")

# Le corps de 223 WF est intégral : seules l'obligation de désignation et sa
# transition sont modifiées, sans toucher au prélèvement ni à ses exonérations.
a = base(12)
proposed = sources[12]['source_xml'].replace(
    'le groupe d\'entreprises multinationales ou le groupe national désigne comme redevable',
    'le groupe d\'entreprises multinationales ou le groupe national peut désigner comme redevable',
    1,
).replace(
    "A défaut de désignation d'une entité redevable dans les conditions prévues au premier alinéa du présent IV bis, le redevable",
    "A défaut de désignation d'une entité redevable dans les conditions prévues au premier alinéa du présent IV bis, et sans qu'une désignation soit requise, le redevable",
    1,
)
proposed += "<p>Le caractère facultatif de la désignation prévue au IV bis s'applique à compter de l'entrée en vigueur de la loi rendant cette désignation facultative, y compris au titre d'un exercice antérieur lorsque cette désignation n'a pas encore été effectuée. Les désignations valablement effectuées avant cette entrée en vigueur demeurent applicables aux exercices pour lesquels elles ont été faites. Cette modification ne remet en cause ni les exonérations, ni les créances, paiements, restitutions, prescriptions et recours relatifs aux exercices antérieurs.</p>"
a.update(
    proposed_xml=proposed,
    reason="Réduction de fond ciblée : la désignation d'une autre entité redevable au IV bis devient une faculté. L'entité française admissible ayant déclaré le bénéfice qualifié le plus élevé était déjà le redevable de secours : ce mécanisme suffit et rend inutile d'imposer une sélection expresse au groupe. Aucune déclaration équivalente ne remplace la désignation. Tous les autres éléments du corps, y compris les exonérations, l'assiette, les clés d'affectation et le régime des coentreprises, sont maintenus à droit constant. L'impôt national complémentaire n'est pas supprimé : sa suppression isolée pourrait déplacer la collecte du minimum vers d'autres Etats plutôt qu'alléger la charge du groupe.",
    review_notes="Le I, le II et sa définition autonome de l'exercice de transition, le III, les quatre alinéas du IV, les trois alinéas du IV bis, le V et les deux alinéas du VI sont conservés dans leur ordre. L'option n'élargit pas les entités admissibles au paiement : exclusion des entités d'investissement, d'investissement d'assurance et des véhicules de titrisation inchangée. L'absence de toute autre entité française conserve son exonération. Pas de nouvelle option déclarative, agrément ou renvoi créé. La transition vise les désignations encore non effectuées, même pour un exercice ancien, mais préserve les désignations valables, dettes et recours. Les notes distinguent les exercices clos à compter du lendemain de la publication de la loi de finances pour 2026 et les exercices ouverts à compter du 31 décembre 2023 ; elles ne datent pas la présente réforme. Le caractère qualifié de l'impôt national dans le cadre international reste à coordonner, sans validation présumée. Le seuil de 750 millions d'euros vient de 223 VL ; le nouveau régime français de distribution ne bénéficie pas automatiquement de 223 VK, 39°/223 WS. Le coût public consolidé n'est pas chiffré.",
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=["L'obligation pour le groupe de désigner expressément une autre entité française redevable au IV bis est retirée ; le redevable légal par défaut demeure et le choix devient facultatif."],
    benefit_review="L'exonération du I pour les entités d'investissement cotées sur un marché réglementé français, européen ou étranger reste entière. Au IV bis, les entités d'investissement, d'investissement d'assurance et véhicules de titrisation restent à l'abri d'une désignation comme redevables ; leur exonération en l'absence de toute autre entité constitutive admissible située en France subsiste pour les groupes futurs éligibles aussi. Les règles d'assiette, de transition et d'affectation ainsi que le régime distinct des coentreprises restent intacts ; la simplification n'est ni une réduction d'exonération ni une remise de la dette du groupe.",
    substantive_impact={
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Une seule obligation est retirée par rapport à la source officielle : la désignation expresse impérative du IV bis devient facultative. Le redevable par défaut existait déjà ; aucun automatisme nouveau ni baisse du minimum international n'est revendiqué.",
        'scope_limitations': "Allègement limité aux groupes concernés par le IV bis et aux désignations non encore faites. Aucun montant d'impôt, économie nationale ou gain net de coût administratif n'est démontré ; l'imposition minimale et ses déclarations générales subsistent.",
        'new_burdens_review': "Aucune charge nouvelle identifiée : mêmes entités admissibles, même redevable par défaut et aucune désignation, notification, donnée, registre ou attestation de remplacement. Le choix d'une autre entité reste libre dans le champ antérieur.",
        'effects': [{
            'kind': 'obligation_removed',
            'measure_id': 'impot-minimum-designation-redevable-facultative',
            'description': "Retrait du caractère obligatoire de la désignation du redevable national pour l'impôt afférent aux entités d'investissement, d'investissement d'assurance et véhicules de titrisation.",
            'before': "Le groupe doit désigner une autre entité constitutive française admissible ; à défaut, celle ayant le bénéfice qualifié le plus élevé est déjà redevable. Assiette, taux et somme dus inchangés par cette obligation de choix.",
            'after': "Désignation facultative ; à défaut de choix, le même redevable légal supporte le même montant, sans sélection expresse requise. Aucune baisse de taux ni d'assiette n'est avancée.",
            'unit': 'legal_duty',
            'affected_population': "Groupes relevant du IV bis de 223 WF comportant une entité française admissible autre qu'une entité d'investissement, d'investissement d'assurance ou un véhicule de titrisation.",
            'conditions_and_transition': "Dès l'entrée en vigueur de la loi rendant la désignation facultative, y compris pour les exercices antérieurs sans désignation encore effectuée ; désignations antérieures valables et droits fiscaux anciens conservés.",
            'replacement_or_new_burdens': "Aucune formalité de remplacement ; recours au redevable par défaut déjà prévu par la source. Les déclarations fiscales générales existantes demeurent.",
            'source_quote': "le groupe d'entreprises multinationales ou le groupe national désigne comme redevable une autre entité constitutive membre du même groupe",
            'proposed_quote': "le groupe d'entreprises multinationales ou le groupe national peut désigner comme redevable une autre entité constitutive membre du même groupe",
        }],
    },
    reference_checks=[],
)
answers.append(a)

a = retained(13,
    "Maintien intégral des ajustements propres à l'impôt national complémentaire qualifié. Les dérogations visent des impôts ou différés réaffectés entre entités et ne sont pas des dispenses déclaratives. Leur suppression pourrait modifier l'ordre de collecte et le caractère qualifié de l'impôt, sans suppression démontrée de la charge globale du groupe.",
    "Lecture des sources 223 VW, VW ter, VW quater, VW quinquies et VW nonies I : affectations respectives aux établissements stables, sociétés étrangères contrôlées, hybrides et entités distributrices. Le I exclut des montants sortants et le II des montants affectés à des entités françaises pour ce seul calcul national ; aucun crédit d'impôt général n'est abrogé. La note de 2026 vise les exercices clos à compter du lendemain de la publication de la loi, pas une date de la réforme proposée.",
    "Aucun nouvel allègement revendiqué : maintien des deux paragraphes qui délimitent les impôts couverts du calcul national, sans suppression de taxe ni création d'une nouvelle formalité.",
    "L'effet sur l'impôt national, l'inclusion étrangère et les crédits dépend des groupes. Aucune baisse nette ni validation du caractère qualifié n'est démontrée par ce maintien seul.",
    "Aucune charge nouvelle identifiée : aucun retraitement, état de suivi ou justificatif supplémentaire n'est ajouté au mécanisme source conservé.")
a['benefit_review'] = "Les termes « Par dérogation » ne désignent pas ici une exonération de résultat, un taux réduit ni un crédit remboursable : ils excluent certains impôts couverts et différés du calcul national après leur réaffectation. Le I et le II sont maintenus intégralement, y compris leurs limites, pour les exercices futurs ; aucun avantage éventuel d'allocation n'est retiré et aucun crédit existant n'est supprimé sous couvert de coordination."

retained(14,
    "Maintien nécessaire des cinq catégories de mères redevables de l'inclusion du revenu et de toutes leurs exceptions. Les conditions des 3°, 4° et 5° évitent des impositions concurrentes dans les chaînes de contrôle. Cette collecte du minimum international n'est pas une contribution additionnelle à l'IS ordinaire que la réforme de distribution supprime.",
    "Contrôle des définitions de 223 VK, 16° et 17°, et des exclusions de 223 VL bis. Les participations visées sont celles des mères intermédiaires ou partiellement détenues, sans assimilation à la participation minoritaire de 30 % de 223 WE. Les cas France/étranger/apatride et les exceptions des derniers alinéas des 4° et 5° restent entiers. Note du 31 décembre 2023 conservée.",
    "La source entière, y compris ses exceptions anti-cumul, est conservée. Aucun redevable ni impôt n'est nouvellement supprimé et aucun agrément de collecte n'est créé.",
    "Une suppression nationale de l'inclusion du revenu exigerait une coordination européenne non décidée ; aucun montant net ou avantage uniforme pour les groupes n'est établi ici.",
    "Aucune charge nouvelle identifiée : maintien des seules catégories fiscales et de leurs exceptions, sans demande, notification ou registre supplémentaire.")

retained(15,
    "Maintien de la composition de l'impôt d'inclusion : montant propre de la mère et part afférente aux autres entités faiblement imposées. Les deux éléments ne sont pas des prélèvements indépendants à fusionner ; les réduire sans tenir compte des imputations modifierait le minimum international maintenu.",
    "223 WG définit les mères redevables ; la part du 2° est déterminée par 223 WH ter et réduite, s'il y a lieu, par 223 WH bis et WI. Ces dispositifs empêchent de confondre somme brute et double imposition finale. Note du 31 décembre 2023 inchangée.",
    "Maintien des deux composantes du calcul officiel sans baisse de taux, d'assiette ou du nombre de formalités revendiquée.",
    "Le montant final requiert les ratios, impôts nationaux et impôts des mères intermédiaires. Le maintien ne démontre pas une dette supplémentaire ni une économie.",
    "Aucune charge nouvelle identifiée : aucune déclaration séparée pour chacune des deux composantes n'est ajoutée au texte existant.")

retained(16,
    "Maintien intégral de l'imputation de l'impôt national et du mécanisme dispensant d'inclusion du revenu lorsque ses trois conditions sont satisfaites. La voie de la norme locale, l'alternative entre obligation légale d'états financiers et audit externe, et le suivi des impayés après quatre exercices sont complémentaires au minimum international, sans double justificatif imposé ici.",
    "Le II de 223 VN, lu dans le corpus public et visé au 1° du II, concerne les principes comptables admis lorsque le résultat est difficile à déterminer dans la norme de consolidation. Le II de 223 WH bis exige normes, conditions de calcul et évaluation par les pairs cumulativement, mais ses a)/b) sont alternatifs. Le III déclenche la reprise après quatre exercices de non-paiement, et le renvoi de 223 WC à ce III reste cohérent. Note : exercices clos à compter du 31 décembre 2024. Le régime n'accorde pas automatiquement le report international au nouvel IS français de distribution.",
    "Les imputations et la dispense conditionnelle existantes restent ouvertes aux groupes futurs éligibles. Le maintien n'est compté ni comme exonération nouvelle ni comme nouvelle baisse d'impôt.",
    "La qualification des impôts étrangers et le processus international ne sont pas validés ici. Le montant d'imputation ne peut être chiffré sans les données et paiements réels des groupes.",
    "Aucune charge nouvelle identifiée : pas de nouvel audit cumulatif, d'agrément national ou de rapport d'équivalence ajouté aux alternatives et conditions sources.")

a = retained(17,
    "Maintien du ratio d'inclusion qui écarte la part attribuable aux autres détenteurs, avec ses cinq hypothèses comptables. La dérogation à un ratio égal à 1 pour certaines entités d'investissement est conservée : le résultat de ces entités est déjà limité à la part du groupe par 223 WT quinquies. Supprimer la dérogation pourrait appliquer deux fois la même réduction.",
    "Le renvoi du I à 223 WB bis définit l'impôt à répartir ; 223 WT quinquies renvoie lui-même au premier alinéa du II pour établir la part de résultat qualifié du groupe. Les hypothèses de consolidation du III sont des règles de calcul, non une obligation de constituer une nouvelle consolidation juridique. Le ratio et les cinq conditions restent entiers. Note de 2025 : exercices clos à compter du 31 décembre 2024.",
    "Maintien de la limitation à la part de bénéfice pertinente et de sa coordination avec le régime d'investissement. Aucun nouvel abattement ni allègement de consolidation n'est revendiqué.",
    "L'avantage individuel dépend des participations et de la norme comptable. Le lot ne démontre pas le montant d'impôt évité ni le solde de conformité d'un groupe.",
    "Aucune charge nouvelle identifiée : aucune obligation d'établir des comptes hypothétiques distincts ou de déposer une attestation supplémentaire n'est ajoutée au texte source.")
a['benefit_review'] = "Le II préserve l'exclusion de la part de bénéfice des autres détenteurs du ratio d'inclusion de la mère, donc la limitation de son impôt à la fraction pertinente. Pour les entités d'investissement et d'investissement d'assurance, le ratio réputé égal à 1 coordonne une part de résultat déjà déterminée selon 223 WT quinquies ; ce n'est pas une suppression de l'avantage de participation. Tous les calculs et leurs cinq hypothèses restent applicables aux situations futures ; aucune catégorie de détenteur n'est exclue nouvellement."

retained(18,
    "Maintien intégral de la réduction de l'impôt de la mère française à concurrence de l'inclusion déjà due par la mère intermédiaire ou partiellement détenue pour la même entité. C'est une protection contre la cascade d'impositions et non une formalité redondante ; elle reste essentielle lorsque le minimum international subsiste.",
    "La réduction porte sur la même entité faiblement imposée et la même règle d'inclusion, pas sur tout impôt du groupe ni sur un crédit remboursable sans dette. Les catégories correspondent à celles de 223 WG ; note du 31 décembre 2023 conservée. Aucun lien avec la suppression des contributions additionnelles à l'IS ordinaire.",
    "La réduction anti-cascade est conservée pour toutes les situations futures remplissant ses conditions. Son maintien n'est pas compté comme une baisse nouvelle.",
    "Le montant imputable reste limité à l'impôt pertinent de la chaîne de détention ; aucun remboursement ou crédit excédentaire nouveau n'est décidé.",
    "Aucune charge nouvelle identifiée : aucun certificat, agrément ou dossier distinct d'imputation n'est créé par le maintien de la source.")

retained(19,
    "Maintien du champ de la règle relative aux bénéfices insuffisamment imposés, de ses trois cas et des exclusions des entités d'investissement et véhicules de titrisation. Cette règle de collecte résiduelle relève du minimum international conservé ; son nom ne suffit pas à la traiter comme une surtaxe de l'IS ordinaire supprimable sans coordination européenne.",
    "223 WK limite et répartit le montant à collecter ; les entités françaises restent celles du groupe dans le champ de 223 VL. Notes conservées : exercices ouverts à compter du 31 décembre 2024 ; anticipation au 31 décembre 2023 pour les groupes relevant de l'option de l'article 50 de la directive ; exclusion nouvelle de 2026 applicable aux exercices clos à compter du lendemain de publication de cette loi. Aucune de ces dates n'est transformée en date de la réforme proposée.",
    "Le texte source entier, ses exclusions et son déclenchement résiduel sont maintenus. Aucun montant, redevable ou prélèvement n'est supprimé dans cet article.",
    "Le maintien ne valide pas la qualification de chaque régime étranger ni les coordinations européennes futures. Il ne démontre aucun gain net de charge ou de recettes.",
    "Aucune charge nouvelle identifiée : les mêmes redevables et exclusions subsistent, sans nouveau registre ni autorisation de paiement.")

retained(20,
    "Maintien intégral du calcul et de la répartition internationale : somme des impôts complémentaires, neutralisation ou réduction des parts déjà soumises à l'inclusion, et pondération par moitié des effectifs et actifs corporels. La périodicité du minimum reste propre à ce régime ; elle ne rétablit pas un IS ordinaire annuel sur les bénéfices conservés.",
    "Le III vise les effectifs en équivalent temps plein, y compris indépendants et intérimaires au sens fiscal de 223 W, 1°, lu en entier. Aucun renvoi au code du travail ne figure dans le corps. Les références à WB à WB quinquies, WK bis et WK ter assurent le calcul distinct et la répartition ; WK ter est coordonné dans ce lot pour ses dénominateurs. Les deux moitiés, valeurs nettes comptables et territoires appliquant une règle qualifiée restent intacts. Notes des 31 décembre 2024 et, dans le cas spécial de l'article 50, 31 décembre 2023 conservées.",
    "Aucune baisse nouvelle : conservation des clés de répartition, ainsi que des mises à zéro et diminutions anti-cumul existantes, sans transformer chaque renvoi en taxe supprimée.",
    "La part française dépend d'effectifs, actifs et impôts étrangers réels ; aucun gain ni hausse de montant n'est calculé. Les procédures de rupture et indemnités privées ne sont pas régies par cet article.",
    "Aucune charge nouvelle identifiée : aucune collecte supplémentaire de contrats, anciennetés, notifications de rupture ou indemnités n'est ajoutée au calcul fiscal.")

# Correction explicite d'un renvoi à un I inexistant ; aucune formule réécrite.
a = base(21)
proposed = sources[21]['source_xml'].replace('en application du I du présent article', 'en application du 1° du présent article', 1)
a.update(
    proposed_xml=proposed,
    reason="Coordination nécessaire du 2° : le renvoi au « I du présent article » est inexistant dans un article subdivisé en 1°, 2° et 3°. Il est remplacé expressément par le 1°, seul passage qui attribue effectifs et actifs aux établissements stables. Les trois règles et les exclusions des entités d'investissement et véhicules de titrisation sont maintenues ; aucune réduction fiscale ou formelle nouvelle n'est revendiquée.",
    review_notes="Incohérence préexistante signalée : le 2° visait un I inexistant ; la correction vers le 1° n'est pas présentée comme une simple copie ni comme une suppression d'obligation. Autre difficulté préexistante conservée et signalée : la seconde phrase du 1° énonce une non-prise en compte des employés et actifs attribués à l'Etat de l'établissement stable sans préciser pour quelle entité, alors que la première impose leur prise en compte pour l'établissement. Sa portée de non-double comptage appelle une confrontation au texte européen intégral ; aucune nouvelle exclusion ou formule n'est inférée dans la proposition. Les affectations du 2° aux entités du territoire de création de l'interposée et l'exclusion du 3° sont intactes. Les clés de 223 WK III et WK quater ne changent pas. Notes d'application : 31 décembre 2024, exception de l'article 50 au 31 décembre 2023, puis modification de 2026 applicable aux exercices clos à compter du lendemain de la publication de la loi ; aucune date future inventée.",
    status='rewrite_draft',
    substantive_impact={
        'version': 1,
        'classification': 'coordination_only',
        'assessment': "La seule différence par rapport à la source entière corrige le renvoi du 2° au 1° existant. Elle rend utilisable l'exception d'affectation aux établissements stables sans changer les effectifs, valeurs d'actifs ou exclusions.",
        'scope_limitations': "Aucune baisse de taux, d'assiette ou d'obligation démontrée. L'ambiguïté distincte de la seconde phrase du 1° reste expressément signalée, sans prétendre valider son interprétation européenne.",
        'new_burdens_review': "Aucune charge nouvelle identifiée : seules les coordonnées du renvoi sont rectifiées ; ni nouvel état d'actifs, ni donnée d'emploi, ni justificatif ou délai n'est exigé.",
        'effects': [{
            'kind': 'coordination',
            'measure_id': 'minimum-mondial-affectation-effectifs-actifs',
            'description': "Rectification du renvoi interne de l'attribution des effectifs et actifs d'une entité interposée vers la règle des établissements stables effectivement numérotée 1°.",
            'before': "Le 2° réserve les attributions à un établissement stable par un renvoi à un I inexistant ; les règles correspondantes sont au 1°.",
            'after': "Le 2° réserve expressément les attributions du 1° ; valeurs nettes comptables et règle territoriale existantes sont conservées.",
            'unit': 'other',
            'affected_population': "Groupes soumis à la règle des bénéfices insuffisamment imposés comprenant une entité interposée ou un établissement stable.",
            'conditions_and_transition': "Coordination du renvoi sans changement du champ ou des dates d'application historiques de l'article et sans remise en cause autonome de droits ou dettes anciens.",
            'replacement_or_new_burdens': "Aucune obligation de remplacement ni nouveau calcul ; correction des seules coordonnées de la disposition applicable.",
            'source_quote': "Sauf s'ils sont attribués à un établissement stable en application du I du présent article",
            'proposed_quote': "Sauf s'ils sont attribués à un établissement stable en application du 1° du présent article",
        }],
    },
    reference_checks=[],
)
answers.append(a)

a = base(22)
proposed = sources[22]['source_xml'].replace(
    "respectivement mentionnés au III de l'article 223 WK et à l'article 223 WK bis",
    "respectivement mentionnés aux 1° et 2° du III de l'article 223 WK",
    1,
)
a.update(
    proposed_xml=proposed,
    reason="Coordination nécessaire du II : les deux dénominateurs relatifs aux effectifs et aux actifs sont ceux des 1° et 2° du III de 223 WK. L'article 223 WK bis règle leur attribution mais ne définit pas le second rapport. Le renvoi défectueux est corrigé explicitement ; exclusion territoriale, condition d'impôt non intégralement prélevé et exception du III sont conservées intégralement, sans gain fiscal nouveau revendiqué.",
    review_notes="Incohérence préexistante : le II faisait correspondre les deux rapports au III de 223 WK et à 223 WK bis, alors que ce dernier n'énonce aucun dénominateur autonome. La lecture complète de WK III et WK bis confirme les deux rapports aux 1° et 2° du III de WK ; seule cette adresse est remplacée. Les effectifs et actifs du territoire concerné restent exclus des dénominateurs, son allocation future réputée nulle reste au I et la réserve lorsque tous les territoires sont dans ce cas reste au III. Pas de modification des pondérations de moitié ni d'un montant d'impôt. Les notes des exercices ouverts à compter du 31 décembre 2024 et du cas spécial au 31 décembre 2023 sont conservées, sans nouvelle date de réforme.",
    status='rewrite_draft',
    substantive_impact={
        'version': 1,
        'classification': 'coordination_only',
        'assessment': "La proposition corrige seulement l'adresse des dénominateurs dans la source officielle entière. Elle ne supprime ni l'impôt résiduel ni son mécanisme de réaffectation aux territoires collecteurs.",
        'scope_limitations': "Aucune économie fiscale ou baisse de coût démontrée ; la correction ne résout pas à elle seule les qualifications étrangères ni l'ambiguïté distincte signalée au 1° de WK bis.",
        'new_burdens_review': "Aucune charge nouvelle identifiée : mêmes données d'effectifs et d'actifs, mêmes territoires et même exception générale, sans déclaration ni preuve supplémentaire.",
        'effects': [{
            'kind': 'coordination',
            'measure_id': 'minimum-mondial-affectation-effectifs-actifs',
            'description': "Correction de la double référence des dénominateurs vers les deux rapports réellement définis à 223 WK III, sans nouvelle mesure de réduction.",
            'before': "Le II renvoie respectivement à 223 WK III et à 223 WK bis pour deux dénominateurs ; seul WK III définit les rapports d'effectifs et d'actifs.",
            'after': "Le II renvoie respectivement aux 1° et 2° du III de 223 WK ; l'exclusion territoriale des effectifs et actifs conserve son champ.",
            'unit': 'other',
            'affected_population': "Groupes multinationaux pour lesquels une allocation antérieure d'impôt résiduel n'a pas été intégralement prélevée dans un territoire.",
            'conditions_and_transition': "Correction de coordination sans changer les périodes historiques d'application, la condition d'impayé antérieur ou l'exception lorsque tous les territoires ont une allocation réputée nulle.",
            'replacement_or_new_burdens': "Aucun nouveau prélèvement, relevé, délai ou registre ; maintien de la répartition internationale existante.",
            'source_quote': "respectivement mentionnés au III de l'article 223 WK et à l'article 223 WK bis",
            'proposed_quote': "respectivement mentionnés aux 1° et 2° du III de l'article 223 WK",
        }],
    },
    reference_checks=[],
)
answers.append(a)

retained(23,
    "Maintien nécessaire de la répartition du montant français entre plusieurs entités, par moitiés des effectifs et des actifs corporels. Le texte répartit une somme déjà attribuée à la France ; il n'ajoute pas un prélèvement. Aucun agrément, minimum de durée d'emploi ou justificatif de rupture n'y figure à supprimer.",
    "Lecture croisée de 223 WK I/III, WK bis et 223 W, 1° : mêmes effectifs en équivalent temps plein, indépendants et intérimaires compris, et mêmes valeurs nettes comptables. La répartition nationale ne rétablit pas le CDD et ne dépend ni de l'ancienneté du salarié ni d'un préavis ou de l'indemnité ordinaire. La correction de WK bis est coordonnée sans changer ces deux moitiés. Notes : exercices ouverts à compter du 31 décembre 2024, ou du 31 décembre 2023 dans le cas de l'article 50 de la directive.",
    "La source complète conserve la ventilation nationale du montant d'impôt international. Aucune taxe, obligation, condition de durée ni formalité n'est nouvellement supprimée.",
    "La somme française totale n'est pas diminuée par une répartition entre redevables. Le coût de calcul et l'incidence pour chaque entité ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : aucune pièce sur les contrats, notification, ancienneté ou indemnité n'est créée ; les seules données fiscales d'effectifs et d'actifs existantes demeurent.")

# Contrôles ciblés exactement sur les cibles requises, sans les transformer en
# nouveaux renvois normatifs à des dispositions de droit privé étrangères au calcul.
checks = {
    20: [
        "L1234-1 vise le préavis de licenciement, avec seuils de six mois/deux ans dans la source et quinze jours calendaires sans ancienneté pour les nouveaux contrats dans la proposition ; les anciens contrats gardent leur régime. 223 WK vise seulement les effectifs fiscaux ETP de 223 W et ne renvoie pas à L1234-1. Aucun seuil de préavis ni condition de notification écrite ne doit donc entrer dans son rapport d'effectifs ; les procédures collectives restent distinctes.",
        "L1221-2 proposé impose la durée indéterminée aux nouveaux contrats privés, sans terme de mission, et préserve les contrats antérieurs. 223 WK inclut aussi indépendants et intérimaires selon l'activité sous autorité et contrôle de 223 W, pas selon un CDI ou CDD. Le contrat unique ne modifie donc pas la formule fiscale ; la mission peut finir sans terminer l'emploi et aucun renvoi au contrat privé n'est ajouté pour des personnes ou régimes publics hors de son champ.",
        "L1234-9 source ouvre l'indemnité à huit mois hors faute grave ; sa proposition exige un an au terme effectif avec préavis inclus pour le nouveau contrat, puis 0,20 mois sur toute l'ancienneté, mois complets au prorata, plafond six mois, employeur seul, et protège l'ancienne composante ainsi que les indemnités spéciales. Aucun de ces critères n'est visé par 223 WK : ni indemnité, ni date de notification ne conditionne le décompte fiscal ETP. La cible ne justifie aucun nouveau renvoi ni modification de l'assiette de ce calcul.",
    ],
    23: [
        "Le préavis de L1234-1 est une règle de rupture privée, avec anciens seuils et garanties conservés pour les anciens contrats, et quinze jours pour les nouveaux selon la proposition. La ventilation entre entités de 223 WK quater repose sur leurs effectifs ETP ; elle ne vise ni ce préavis ni sa notification ou l'ancienneté. Aucune proratisation fiscale nouvelle à quinze jours n'est introduite et les autorisations/procédures collectives ne sont pas supprimées par cette ventilation.",
        "La cible L1221-2 distingue la source permettant des CDD des nouveaux emplois indéterminés proposés, même lorsque la formation ou la mission est limitée ; les situations antérieures restent protégées. Les intérimaires de 223 WK quater sont inclus au sens autonome de 223 W, sans subordonner l'effectif au terme de leur contrat. Ce texte fiscal n'autorise donc aucun nouveau CDD et le contrat unique n'étend pas artificiellement son champ aux indépendants ou agents publics décomptés fiscalement.",
        "L1234-9 proposé fixe, pour les nouveaux contrats, zéro indemnité ordinaire avant un an atteint à la fin effective, préavis inclus ; après ce seuil, 0,20 mois par année totale avec mois complets au prorata et plafond six mois, à la charge de l'employeur. Anciennes composantes et indemnités spéciales demeurent distinctes. 223 WK quater ne renvoie pas à ce régime : le nombre d'employés ETP n'est pas un nombre de salariés indemnisables et ne dépend ni de l'ancienneté ni d'une notification de rupture. Aucun renvoi fiscal n'est rectifié vers cette cible inapplicable.",
    ],
}

for i, answer in enumerate(answers):
    key = f"{answer['code_id']}|{answer['source_id']}"
    required = targets['requirements'][key]
    if required:
        answer['reference_checks'] = [
            {'target_key': target, 'view_sha256': targets['targets'][target]['view_sha256'], 'assessment': checks[i][j]}
            for j, target in enumerate(required)
        ]

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answers)} articles')
