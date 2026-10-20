import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}

def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))

def clean(xml):
    return re.sub(r'\s+align="[^"]*"', '', xml).strip()

def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])

retained = {
'L325-2': (
    "Maintien intégral nécessaire : le conseil d'administration, le budget prévisionnel annuel et l'affiliation par les caisses assurent la solvabilité et le service d'une assurance obligatoire locale. Le plafond de 3 % encadre une faculté de financement sanitaire, non une taxe ni un dossier imposé aux assurés. Aucun double rapport, agrément individuel ou prélèvement accessoire n'est institué ici et aucune suppression supplémentaire n'est retenue.",
    "Le I conserve l'état prévisionnel pour l'exercice suivant, les deux affectations facultatives et leur plafond commun de 3 % des dépenses de prestations constatées. Le II conserve les CPAM métropolitaines et les CGSS outre-mer ; ce champ de gestion ne modifie pas les bénéficiaires du régime local. Aucun effet chiffré ni réforme des décrets de composition n'est revendiqué.",
    "La source entière organise une assurance locale et la responsabilité financière de son gestionnaire ; la maintenir n'est ni une baisse de cotisation ni une simplification matérielle.",
    "L'examen ne porte pas sur les taux du régime local ni sur le contenu des décrets de gouvernance, qui ne sont pas modifiés par cet article.",
    "Aucune charge nouvelle n'est identifiée : ni état supplémentaire, ni nouvelle pièce d'affiliation, ni nouveau contrôle préalable n'est ajouté au texte source."),
'L325-3': (
    "Maintien intégral de l'action sanitaire et sociale prioritaire en faveur des personnes exposées à la précarité. La réserve d'équilibre financier protège la continuité des prestations ; la retirer ne supprimerait aucun prélèvement ou dossier et fragiliserait ce droit d'action favorable.",
    "La priorité sociale et la réserve d'équilibre demeurent cumulatives. Aucun crédit budgétaire, taux de cotisation ou obligation déclarative n'est créé ou supprimé.",
    "L'habilitation sociale favorable est conservée en entier après examen ; elle ne comporte pas de formalité distincte retirable et aucun gain matériel nouveau n'est compté.",
    "Le financement et l'exécution des actions du régime local restent à leur champ ; aucun montant d'aide ni économie nationale n'est déduit de ce maintien.",
    "Aucune charge nouvelle n'est identifiée, puisque l'habilitation et sa condition de soutenabilité financière sont conservées sans dépôt ni compte rendu supplémentaire."),
'L331-1': (
    "Maintien intégral nécessaire du champ des bénéficiaires et de l'absence de participation aux frais de maternité. Les trois catégories familiales renvoyées à L161-1 et la gratuité ne doivent pas être retranchées au titre d'une réduction des charges ; cet article ne crée ni cotisation ni justificatif autonome.",
    "L161-1 et L160-9 ont été lus dans le corpus public : conjoint/concubin/PACS, enfants et membre du ménage du 3° restent couverts dans leurs conditions respectives. L'absence de participation de L160-9 est concordante ; la répétition protectrice n'impose aucun second dossier et reste conservée.",
    "La gratuité et les bénéficiaires sont maintenus, y compris pour les futures situations éligibles. Cette préservation n'est pas une nouvelle réduction de prélèvement.",
    "Les conditions des prestations en espèces et les périodes de prise en charge ne sont pas élargies par ce maintien du champ personnel et de la gratuité des soins.",
    "Aucune charge nouvelle n'est identifiée : maintien sans changement, sans demande, attestation ou participation financière supplémentaire."),
'L331-3': (
    "Maintien intégral des indemnités et des durées de repos maternel, y compris naissances multiples et grande prématurité avec hospitalisation. La cessation de travail et les huit semaines minimales protègent la santé maternelle et l'objet du revenu de remplacement ; ce ne sont ni une ancienneté minimale dans l'entreprise ni un délai de rupture. Les supprimer compromettrait une protection essentielle et la coordination européenne des congés de maternité.",
    "Contrôle des quatre alinéas : six/dix semaines ; douze ou vingt-quatre semaines prénatales et vingt-deux postnatales ; transfert maximal de quatre semaines pour deux enfants ; garanties de seize, trente-quatre ou quarante-six semaines et supplément pour naissance plus de six semaines avant terme avec hospitalisation. La note de 2006 couvre les accouchements depuis le 1er janvier 2006. Le renvoi à L331-4 est conservé et les quatre alinéas restent à leur place.",
    "Le droit et ses adaptations favorables sont maintenus entièrement ; les conditions de repos ont une fonction sanitaire propre et aucun prélèvement ou double dossier n'est supprimé ici.",
    "Aucune modification des durées européennes, des règles de calcul des indemnités ou du champ des contrats antérieurs n'est réalisée ; l'ouverture sociale reste distincte de l'ancienneté de rupture.",
    "Aucune charge nouvelle n'est identifiée : les conditions de cessation d'activité et le minimum protecteur de repos demeurent ceux de la source, sans justificatif ajouté."),
'L331-3-1': (
    "Maintien intégral de la dérogation permettant à l'élue locale de poursuivre son mandat et de percevoir ses indemnités de fonction pendant l'indemnisation du travail salarié. L'indemnisation supplémentaire en cas d'interruption du mandat reste ouverte aux futures situations éligibles ; sa condition de cessation évite d'indemniser une activité poursuivie et ne constitue pas un agrément redondant.",
    "Le premier alinéa de L331-3 vise la cessation du travail salarié et non la fin du mandat. Le renvoi à L313-1 doit suivre sa proposition supprimant la durée minimale d'affiliation du II, sans rétablir celle-ci par le présent maintien. La rémunération ou les heures de travail demeurent distinctes de l'ancienneté d'entreprise.",
    "La dérogation et le cumul autorisé sont conservés ; aucune coupe n'est revendiquée pour le maintien de cet avantage social et électif.",
    "Le mandat local n'est pas transformé en contrat privé ; les conditions de liquidation de l'indemnité propre au mandat restent distinctes et aucun taux n'est modifié.",
    "Aucune charge nouvelle n'est identifiée : aucun formulaire, agrément ou délai d'information de l'élue ou de l'employeur n'est ajouté."),
'L331-4': (
    "Maintien intégral de l'allongement favorable du repos indemnisé pour l'assurée ou le ménage ayant déjà deux enfants, ou pour l'assurée ayant mis au monde deux enfants viables. La faculté de déplacer deux semaines et l'absence de réduction pour naissance anticipée restent ouvertes. Les conditions de charge d'enfant ont pour fonction d'identifier l'avantage, sans déclaration autonome instituée ici.",
    "Huit semaines avant et dix-huit après, transfert maximal de deux semaines et total de vingt-six semaines sont conservés. L521-2 a été lu : ses premier et quatrième alinéas concernent la charge effective et les enfants confiés à l'ASE ; ces assimilations ne sont pas supprimées. L331-3 premier alinéa reste inchangé.",
    "Le supplément de durée et ses deux voies d'éligibilité sont maintenus intégralement ; aucune baisse de charge nouvelle ne résulte de cette conservation.",
    "Ni le nombre d'enfants requis ni les règles propres au congé de maternité ne sont étendus à d'autres prestations ; aucune réforme du régime des agents publics n'en découle.",
    "Aucune charge nouvelle n'est identifiée : les seules conditions sont celles de la source, sans nouvelle preuve de filiation ou de charge imposée."),
'L331-4-1': (
    "Maintien intégral de l'option de report prénatal vers le postnatal. La prescription médicale et la limite de trois semaines assurent la sécurité d'un aménagement volontaire du repos ; l'annulation en cas d'arrêt de travail ouvre l'indemnité dès le premier jour et prévient une perte de protection. Aucune pièce redondante n'est instituée par cet article et la prescription n'est pas supprimée.",
    "L331-3 et L331-4 restent entiers : la réduction prénatale augmente d'autant le postnatal, puis le report est réduit à due concurrence en cas d'arrêt. La demande est une option de l'assurée, non une autorisation d'embauche ; l'ancienneté et le préavis du contrat unique ne changent pas ce calcul.",
    "Le report choisi, la prescription protectrice et le versement dès le premier jour d'arrêt sont conservés, sans allègement nouveau comptabilisé.",
    "Ce maintien ne lève pas les prescriptions médicales protectrices ni ne réduit les repos minimaux ; il ne préjuge pas des démarches réglementaires extérieures au présent article.",
    "Aucune charge nouvelle n'est identifiée : la demande volontaire et la prescription existantes ne sont complétées par aucun document, registre ou délai nouveau."),
'L331-5': (
    "Maintien intégral du report d'indemnisation après hospitalisation prolongée de l'enfant et des deux semaines supplémentaires sur prescription médicale. La priorité donnée à la période supplémentaire de grande prématurité coordonne deux droits favorables et ne retire pas leur durée. L'hospitalisation et la prescription ont une fonction médicale propre, sans agrément administratif à supprimer ici.",
    "La sixième semaine, le report total ou partiel après hospitalisation, le dernier alinéa de L331-3 et le plafond supplémentaire de deux semaines sont conservés. Note de 2006 maintenue pour les naissances depuis le 1er janvier 2006. Incohérence préexistante relevée dans le corpus : R331-6 vise le deuxième alinéa de L331-5 pour le supplément pathologique, situé au troisième dans la source actuelle ; sa correction réglementaire est à effectuer hors lot, sans déplacer les alinéas de L331-5.",
    "Les reports et l'allongement médical sont maintenus en entier ; leur conservation n'est pas une nouvelle simplification ni une baisse de prélèvement.",
    "La coordination réglementaire du renvoi ordinal de R331-6 reste à faire et n'est pas présentée comme achevée ; le présent maintien ne modifie pas l'ordre des alinéas.",
    "Aucune charge nouvelle n'est identifiée : aucune confirmation périodique ni certificat supplémentaire ne s'ajoute à la demande de report et à la prescription existantes."),
'L331-6': (
    "Maintien intégral du relais d'indemnisation après décès de la mère : droit du père pour la durée restante, dispense des conditions de L313-1, report après hospitalisation et bénéficiaire subsidiaire conjoint/PACS/concubin. La cessation de travail est liée au remplacement de revenu. Supprimer ces règles retirerait des avantages essentiels ; le décès visé ne déclenche aucun droit fiscal de succession.",
    "Les deux bornes alternatives (fin d'indemnisation maternité ou fin du maintien de traitement), la durée restante, la dispense entière de L313-1 et la priorité du père sont conservées. Le premier alinéa de L331-5 est bien la faculté de report pour hospitalisation. L'absence de demande du père ouvre le droit subsidiaire, sans ancienneté de rupture ni nouveau terme d'emploi.",
    "Le relais, la dispense et le report sont intégralement conservés pour les futurs décès éligibles ; aucune baisse de charge nouvelle n'est revendiquée.",
    "Le maintien de traitement peut relever d'un régime public distinct ; il ne devient pas une indemnité de rupture du contrat unique et les formalités réglementaires ne sont pas réécrites ici.",
    "Aucune charge nouvelle n'est identifiée : aucun certificat fiscal de décès, autorisation de transfert ou nouvelle preuve de durée d'affiliation n'est ajouté."),
'L331-7': (
    "Maintien intégral des indemnités d'adoption ou d'accueil, de leurs allongements et de la dérogation pour le mandat local. Les conditions d'accueil de L161-6 protègent la régularité du placement et l'enfant ; elles ne sont pas un agrément d'emploi remplaçable par une déclaration. Cesser le travail pendant l'indemnisation reste cohérent avec la fonction de remplacement de revenu.",
    "Seize semaines, vingt-deux pour adoptions multiples et dix-huit à partir de trois enfants à charge restent distincts. L161-6 deuxième alinéa, L521-2 premier/quatrième alinéas et L1225-37 ont été lus intégralement : le champ du placement, les enfants confiés à l'ASE, le délai et le fractionnement correspondent aux renvois. Le cumul mandat/indemnité de fonction et l'indemnité pour mandat interrompu restent ouverts ; L313-1 suit sa proposition favorable.",
    "Les durées et cumuls autorisés sont conservés sans changement ; il n'existe ici ni nouvelle suppression de taxe ni allègement de démarche démontré.",
    "Les agréments civils d'adoption et l'entrée régulière de l'enfant gardent leur régime ; le contrat unique ne transforme pas ces conditions en terme d'emploi.",
    "Aucune charge nouvelle n'est identifiée : aucune demande additionnelle d'adoption, pièce relative au mandat ou notification de rupture n'est créée."),
'L331-8': (
    "Maintien intégral des droits à indemnité de paternité et d'accueil, de la prolongation pour hospitalisation et du régime favorable des élus locaux. La cessation d'activité et le minimum de quatre jours participent au repos et au revenu de remplacement. Les non-cumuls évitent deux remplacements du même revenu ; aucune autorisation ou transmission redondante n'est instituée dans cet article.",
    "Vingt-cinq/trente-deux jours, troisième alinéa pour l'hospitalisation et quatrième alinéa pour non-cumuls/mandat sont conservés. L1225-35 lu au corpus : ses troisième et dernier alinéas restent les bonnes cibles ; sa proposition retire l'annonce distincte de date prévisionnelle sans déplacer la période de quatre jours. La réserve QPC 2025-1155 relative à la filiation par reconnaissance conjointe d'un couple de femmes reste applicable ; aucune restriction de bénéficiaire n'est ajoutée ici.",
    "Le droit de paternité et ses dérogations sont conservés intégralement. Le maintien des délais de congé n'annule pas l'allègement d'information proposé dans L1225-35 et ne compte pas comme une nouvelle coupe.",
    "Le préavis de rupture du contrat unique ne remplace pas les délais de prise du congé. D331-4, lu, contient encore un renvoi au quatrième alinéa de L1225-35 pour l'hospitalisation, située au dernier alinéa : coordination réglementaire à faire hors lot.",
    "Aucune charge nouvelle n'est identifiée : aucun préavis de rupture, rapport ou attestation supplémentaire n'est ajouté aux conditions de la source."),
'L331-9': (
    "Maintien intégral de l'indemnisation du congé de deuil, de la subrogation de plein droit et de la durée de quinze jours pour les bénéficiaires du maintien de droits. La cessation d'activité et les quatre exclusions préviennent le double remplacement du revenu ; la subrogation évite une double perception sans imposer un agrément. Il ne s'agit d'aucun prélèvement sur une succession.",
    "L3142-1-1 et L3142-2 lus au corpus : congé de huit jours pour enfant/personne à charge de moins de vingt-cinq ans, fractionnement, prise dans l'année et rémunération maintenue. Les quinze jours du dernier alinéa de L331-9 concernent L161-8/L311-5 et ne sont pas le préavis de rupture. Les notes d'application 2026 restent applicables à l'ajout du congé supplémentaire de naissance dans le non-cumul. D331-8 vise le huitième alinéa, qui est bien le dernier de la source.",
    "Le droit de deuil et le maintien favorable aux personnes hors emploi sont préservés ; la source ne crée pas de démarche redondante dont une suppression autonome serait démontrée.",
    "Les durées de congé salarié et d'indemnisation hors emploi restent distinctes ; les délais de notification et les conditions du code du travail ne sont pas supprimés par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : la subrogation reste automatique, sans option, déclaration ou autorisation de remplacement imposée à l'employeur ou à l'assuré."),
'L332-2': (
    "Maintien intégral de la prise en charge maladie dès constatation d'une grossesse ou de suites de couches pathologiques, avec accès éventuel aux droits propres et dérivés de l'assurance invalidité. Le constat de l'état morbide assure le fondement médical ; il ne s'agit pas d'une ancienneté ou autorisation administrative supprimable sans affecter la protection.",
    "Les chapitres 1er et 2 du titre IV sont ceux des droits propres et dérivés de l'assurance invalidité. L341-2 est réformé dans ce lot pour supprimer la durée minimale d'affiliation distincte ; le présent renvoi ne la rétablit pas. La note de 2001 mentionne enfants nés/adoptés depuis 2002, y compris certaines naissances antérieures prévues après 2001 : elle est conservée comme note historique sans en faire une date future.",
    "La continuité maladie-invalidité en cas de pathologie est conservée entière ; aucune nouvelle réduction de cotisation n'est prétendue.",
    "Le renvoi éventuel n'attribue pas automatiquement une pension d'invalidité : les critères médicaux et les conditions contributives non supprimées restent requis.",
    "Aucune charge nouvelle n'est identifiée : aucun second constat médical, nouvelle pièce ou nouveau délai d'ouverture n'est ajouté."),
'L333-2': (
    "Maintien intégral du versement dès la suspension du contrat, sans carence ajoutée, et de l'arrêt du versement lorsque ses conditions cessent. Cette borne évite de poursuivre indûment un revenu de remplacement, sans agrément initial, renouvellement ou délai minimal autonome à supprimer.",
    "Le début est la suspension décidée par l'employeur, non la date d'une rupture. La suppression/suspension de l'allocation ne peut résulter que de la disparition des conditions d'attribution. Note de 2001 conservée ; les suspensions protectrices sont actualisées dans L333-1 sans déplacer la présente règle.",
    "La règle de service immédiat et sa borne de fin sont maintenues ; ce maintien n'est pas compté comme une réduction nouvelle.",
    "Le présent texte n'autorise aucune rupture automatique du contrat et ne réforme ni les délais de recours ni les garanties de notification des décisions de la caisse.",
    "Aucune charge nouvelle n'est identifiée : aucun renouvellement périodique, contrôle d'ancienneté de rupture ou certificat nouveau n'est introduit."),
'L333-3': (
    "Maintien intégral des six exclusions de cumul de l'allocation de dispense de travail. Elles évitent de financer plusieurs fois la même cessation d'activité, tout en conservant la limitation du 2° aux prestations compensant cette cessation et celle du 5° à l'ouverture de la PreParE partielle. Les élargir sous couvert de simplification supprimerait des avantages ; aucune déclaration distincte n'est imposée ici.",
    "Les 1° à 6° sont conservés sans renumérotation. L544-1 comprend l'AJPP des salariés et des agents publics, sans rattacher ces derniers au contrat privé. L331-8-1 reste une indemnité de naissance distincte ; son montant est rendu non dégressif dans ce lot sans suppression du non-cumul. Les renvois CASF L245-3 1°, CSS L541-1 et L531-4 ne changent pas ; leur contrôle documentaire n'est pas étendu ici à tout leur dispositif. Notes d'application 2026 conservées.",
    "Les exclusions ciblées et leurs limites favorables restent entières ; aucune formalité ou taxe nouvelle n'est supprimée par ce maintien.",
    "Le maintien n'étend pas la réforme du contrat unique aux agents publics ni le non-cumul à toute aide au handicap ; le solde financier des prestations n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle déclaration de cumul ou condition d'activité ne s'ajoute aux six règles existantes."),
'L341-1': (
    "Maintien intégral de la définition du droit à pension d'invalidité fondée sur la capacité de travail ou de gain. La référence à la rémunération soumise à prélèvements est un étalon de perte de capacité, non une cotisation nouvelle. Supprimer l'évaluation ou son champ professionnel retirerait une protection essentielle ou rendrait la prestation indéterminée.",
    "Les deux dates alternatives (interruption suivie d'invalidité ou constatation médicale), la profession antérieure et la fraction de rémunération restent conservées. Note : application depuis le 1er janvier 2020. Cette pension d'invalidité n'est pas assimilée à la pension de vieillesse visée par la transition de capitalisation ou de désindexation.",
    "Le fondement médical et économique de la pension est conservé sans changement ; il ne prouve aucune baisse de prélèvement ni simplification nouvelle.",
    "La fraction réglementaire et les montants de pension ne sont pas modifiés ; l'assouplissement distinct de L341-2 ne dispense pas de l'invalidité requise.",
    "Aucune charge nouvelle n'est identifiée : le maintien n'impose ni évaluation supplémentaire ni déclaration de revenu nouvelle."),
'L341-3': (
    "Maintien intégral de l'appréciation individualisée de l'invalidité et de ses quatre moments possibles. La capacité restante, l'état général, l'âge, les facultés, les aptitudes et la formation évitent une appréciation mécanique défavorable. Le 3° permet de ne pas attendre l'épuisement des indemnités maladie ; supprimer ces voies fermerait des droits et non une charge inutile.",
    "Les 1° à 4° et leur ordre sont conservés : accident non professionnel après consolidation, fin de période maladie, stabilisation anticipée, usure prématurée dès constat médical. Le renvoi L321-1 porte bien sur les indemnités maladie, pas sur un contrat de travail ni une indemnité de rupture. R341-8/R341-9 lus au corpus conservent l'évaluation médicale, l'information et les décisions à réception certaine ; ils ne sont pas réécrits dans ce lot.",
    "L'examen individualisé et les quatre voies d'accès sont maintenus entièrement ; aucun allègement nouveau n'est compté pour leur conservation.",
    "La liquidation et le délai de demande de R341-8 restent à leur champ propre ; les voies d'accès ne créent ni terme d'emploi ni dispense médicale générale.",
    "Aucune charge nouvelle n'est identifiée : aucun nouvel examen périodique, dossier ou délai d'attente ne s'ajoute aux critères existants."),
'L341-4': (
    "Maintien intégral des trois catégories pour déterminer le montant de pension, dont la majoration liée au besoin de tierce personne. La distinction entre activité encore possible, incapacité professionnelle et assistance pour les actes de la vie est nécessaire au calibrage des droits ; fusionner les catégories sans barème conserverait mal ces avantages.",
    "Les trois catégories et leurs qualifications cumulatives sont conservées : capacité d'activité rémunérée, incapacité absolue d'exercer toute profession, puis besoin de tierce personne pour les actes ordinaires. Aucun taux de pension ni droit futur de retraite n'est inventé ; la source ne comporte pas de tableau supprimable.",
    "Le classement nécessaire au montant et à la protection de la dépendance est maintenu intégralement, sans réduction nouvelle de charge revendiquée.",
    "La terminologie de la source et les barèmes extérieurs ne sont pas réformés ; aucune assimilation à une pension de vieillesse n'est opérée.",
    "Aucune charge nouvelle n'est identifiée : le classement reste celui de la source et n'exige pas une nouvelle attestation de tierce personne."),
}

answer = []
for s in sources:
    a = {k: s[k] for k in ['code_id','source_id','source_sha256','number']}
    a['reference_checks'] = []
    if s['number'] in retained:
        reason, notes, assessment, limitations, burdens = retained[s['number']]
        a.update(proposed_xml=None, reason=reason, review_notes=notes,
                 status='retained_unchanged', classification='retained_necessary',
                 substantive_impact=impact('retained_necessary',assessment,limitations,burdens))
    answer.append(a)

out = {a['number']: a for a in answer}

def effect(number, kind, measure_id, description, before, after, unit,
           population, transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def rewrite(number, xml, reason, notes, classification, assessment, limitations, burdens, effects, removed=None):
    a=out[number]
    a.update(proposed_xml=clean(xml),reason=reason,review_notes=notes,status='rewrite_draft',
             substantive_impact=impact(classification,assessment,limitations,burdens,effects))
    if removed:
        a.update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)

n='L330-1'
xml="""<p>L'assurance maternité a pour objet :</p>
<p>1° La couverture des frais visés à l'article L. 160-9 ;</p>
<p>2° L'octroi d'indemnités journalières dans les conditions visées aux articles L. 331-3 à L. 331-7 et L. 333-1 à L. 333-3, pour le compte de la Caisse nationale des allocations familiales dans les proportions et sous les conditions de remboursement prévues à l'article L. 223-1 ;</p>
<p>3° L'octroi des indemnités journalières visées aux articles L. 331-8, L. 331-8-1 et L. 331-9 pour le compte de la Caisse nationale des allocations familiales et contre remboursement dans les conditions prévues à l'article L. 223-1.</p>
<p>La rectification des renvois et des proportions de remboursement ne modifie ni les conditions d'ouverture ni les montants des prestations. Les dispositions relatives au congé supplémentaire de naissance restent applicables aux enfants nés ou adoptés à compter du 1er janvier 2026 ainsi qu'aux enfants nés avant cette date dont la naissance était censée intervenir à compter de cette date.</p>"""
rewrite(n,xml,
    "Coordination nécessaire, sans nouvelle réduction : le 3° vise L331-8-1 qui institue l'indemnité supplémentaire de naissance, au lieu de L331-8-2 qui règle ses non-cumuls. Le 2° renvoie expressément aux proportions de L223-1 plutôt que de qualifier indistinctement de partiel un remboursement comprenant l'adoption intégralement remboursée. Soins et toutes indemnités sont maintenus.",
    "L223-1 6° a) conserve 60 % pour L331-3 à L331-6/L333-1 à L333-3 ; b) conserve la totalité pour L331-7 sous sa réserve de prise en charge patronale et pour L331-8/L331-9 ; d) rembourse la totalité de L331-8-1. Aucun remboursement n'est créé au profit d'un assuré au titre de L331-8-2. Application 2026 de la note conservée ; aucun transfert supplémentaire de financement ni économie publique n'est revendiqué.",
    'coordination_only',
    "Deux incohérences de désignation de la source sont coordonnées : article créateur de l'indemnité et proportions déjà fixées par L223-1. Le champ matériel et les financements légaux existants demeurent.",
    "Les simplifications propres au gestionnaire proposées dans L223-1 ne sont pas de nouvelles coupes dans L330-1 ; les régimes publics et agricoles du 6° à 8° de la cible ne sont pas réformés ici.",
    "Aucune charge nouvelle n'est identifiée : aucun rapport, donnée, délai, demande de remboursement ou prélèvement n'est ajouté par les renvois corrigés.",
    [effect(n,'coordination','maternite-renvois-indemnites-financement',
      "Rattachement de l'indemnité de naissance à son article créateur, avec renvoi aux proportions légales de remboursement.",
      "Le 3° cite L331-8-2, liste de non-cumuls ; le 2° parle d'une prise en charge en partie comprenant L331-7.",
      "Le 3° cite L331-8-1 ; le 2° applique les proportions déjà fixées à L223-1, sans changement d'assiette ou de taux de cotisation.",
      'other','Assurés des congés familiaux, CNAF et organismes servant les prestations.',
      "Droits inchangés ; application historique du congé supplémentaire de naissance depuis les naissances/adoptions éligibles de 2026 conservée.",
      "Aucune formalité ou source de financement supplémentaire ; coordination sans seconde économie.",
      "L'octroi des indemnités journalières visées aux articles L. 331-8, L. 331-8-2 et L. 331-9",
      "L'octroi des indemnités journalières visées aux articles L. 331-8, L. 331-8-1 et L. 331-9")])

n='L331-8-1'
xml=clean(by_number[n]['source_xml']).replace(
    "Ce montant peut être rendu dégressif entre le premier et le second mois de ce congé.",
    "Le montant journalier applicable au premier mois est maintenu au second mois, sans préjudice d'un montant plus favorable. La suppression de la dégressivité ne peut réduire le montant applicable au premier mois.")
xml+="""<p>La suppression de la dégressivité s'applique aux journées indemnisées à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsque le congé a commencé auparavant. Pour ces journées, le coefficient plus favorable applicable au premier mois à la veille de cette entrée en vigueur constitue le minimum applicable aux deux mois, y compris pour les futures ouvertures de droit. Les périodes antérieures, leurs créances, régularisations, restitutions, prescriptions et recours restent régis par les dispositions antérieures, sans double paiement.</p>
<p>Les dispositions relatives au congé supplémentaire de naissance restent applicables aux enfants nés ou adoptés à compter du 1er janvier 2026 ainsi qu'aux enfants nés avant cette date dont la naissance était censée intervenir à compter de cette date.</p>"""
rewrite(n,xml,
    "Réduction de fond : suppression de la faculté de diminuer l'indemnité au second mois de congé supplémentaire de naissance. Le montant du premier mois et tout montant plus favorable sont préservés ; aucun nouveau taux intermédiaire n'est créé. Le premier alinéa, les revenus de référence, le plafond et la détermination réglementaire restent conservés, avec application aux journées futures des congés en cours et aux futurs droits.",
    "R331-5-1, lu intégralement au corpus, applique actuellement des coefficients de 0,7 puis 0,6 aux modalités des deux premiers alinéas de R331-5. Il doit être coordonné pour appliquer au second mois le coefficient favorable du premier (0,7 actuellement), sans rétablir 0,6 ni abaisser le premier mois ; ce règlement n'est pas modifié dans ce lot. L313-1 proposé supprime l'affiliation minimale du II, sans retirer les conditions contributives du I. Le délai de prévenance de L1225-46-2 est celui d'un congé, pas celui de la rupture ; les notes d'application 2026 restent conservées. Coût supplémentaire de prestations et remboursement CNAF à chiffrer ; aucune économie ou compensation n'est présumée.",
    'mixed',
    "La faculté légale de dégressivité, effectivement mise en œuvre par R331-5-1, est retirée pour les journées futures : le second mois conserve le niveau favorable du premier. Cette restriction de prestation levée s'accompagne d'un nouveau plancher légal de paiement pour la caisse ; ce n'est pas une baisse de cotisation et le solde public net est inconnu.",
    "La mise en cohérence de R331-5-1 reste nécessaire ; aucun solde budgétaire net n'est établi. Les anciens mois définitivement servis ne sont pas recalculés et les autres conditions d'accès au congé subsistent.",
    "Aucune charge administrative nouvelle n'est identifiée : aucun dossier, registre ou justificatif de remplacement. Un nouveau plancher légal impose toutefois à la caisse le niveau favorable du premier mois pour les deux mois ; la CNAF finance cette prestation selon L223-1. Cette obligation de paiement accrue et son coût public restent non chiffrés.",
    [effect(n,'relief_extended','naissance-supplementaire-fin-degressivite',
      "Suppression de la minoration du second mois d'indemnité supplémentaire de naissance, avec plancher égal au niveau favorable existant du premier mois.",
      "Le montant pouvait légalement diminuer du premier au second mois ; R331-5-1 prévoit 0,7 puis 0,6 sur la même indemnité de référence.",
      "Le second mois conserve le montant du premier, au minimum son coefficient plus favorable existant lors de l'entrée en vigueur ; aucun taux de cotisation ou assiette contributive n'est modifié.",
      'other','Assurés éligibles au congé supplémentaire de naissance prenant un second mois indemnisé.',
      "Journées indemnisées dès l'entrée en vigueur, congés déjà commencés inclus ; futures situations éligibles couvertes, périodes anciennes et non-cumuls conservés.",
      "Aucune pièce nouvelle ; charge de prestation accrue pour les organismes, financement net non établi.",
      "Ce montant peut être rendu dégressif entre le premier et le second mois de ce congé.",
      "Le montant journalier applicable au premier mois est maintenu au second mois, sans préjudice d'un montant plus favorable."),
     effect(n,'obligation_added','naissance-supplementaire-fin-degressivite',
      "Corollaire public du même avantage : plancher légal de paiement des deux mois fondé sur le coefficient favorable existant du premier mois, sans seconde réduction comptée.",
      "L'autorité réglementaire pouvait dégrader le second mois ; aucun plancher légal commun aux deux mois ne résultait de cette phrase de L331-8-1.",
      "La caisse doit payer les deux mois au moins au coefficient favorable du premier mois en vigueur à la veille de la réforme, dans la même assiette plafonnée de revenus antérieurs ; aucune donnée nouvelle n'est exigée.",
      'legal_duty',"Organismes payeurs et CNAF pour les assurés prenant le second mois de congé supplémentaire de naissance.",
      "Même mesure et mêmes journées futures que l'extension de l'avantage, congés en cours et futurs inclus ; anciens paiements non recalculés.",
      "Obligation de paiement accrue pour la caisse, remboursement par la CNAF à son champ existant ; coût et solde net inconnus, sans nouvelle procédure privée.",
      "Ce montant peut être rendu dégressif entre le premier et le second mois de ce congé.",
      "Pour ces journées, le coefficient plus favorable applicable au premier mois à la veille de cette entrée en vigueur constitue le minimum applicable aux deux mois, y compris pour les futures ouvertures de droit.")],
    ["Suppression de la faculté de réduire le montant journalier au seul passage du premier au second mois du congé supplémentaire de naissance."])

n='L331-8-2'
xml=clean(by_number[n]['source_xml']).replace(
    "2° Les indemnités journalières mentionnées aux articles L. 331-3 à L. 331-9 ;",
    "2° Les indemnités journalières mentionnées aux articles L. 331-3 à L. 331-8 et à l'article L. 331-9 ;")
rewrite(n,xml,
    "Coordination nécessaire de la liste de non-cumul : l'intervalle L331-3 à L331-9 englobait L331-8-1, indemnité dont le présent article règle précisément le versement, et L331-8-2 lui-même. Le 2° vise désormais les indemnités de maternité, adoption, paternité/accueil et deuil, sans autocumul impossible. Les trois autres exclusions demeurent intégralement.",
    "Le 2° conserve L331-3, L331-3-1, L331-4, L331-4-1, L331-5, L331-6, L331-7, L331-8 et L331-9 dans leur champ propre, sans prétendre que chaque texte crée une indemnité autonome. L321-1 et L433-1 restent les exclusions maladie et AT-MP. Les notes 2026 et la transition de L331-8-1 restent applicables ; l'erreur préexistante de l'intervalle ne justifie ni suppression d'un droit ni perception de deux revenus de remplacement.",
    'coordination_only',
    "La portée de la liste est rendue cohérente en retirant sa référence réflexive à l'indemnité qu'elle régit. Aucun cumul de prestations distinctes supplémentaire ni réduction de taxe n'est créé.",
    "Les non-cumuls maladie, autres congés familiaux, AT-MP et chômage restent applicables ; ce correctif n'est pas compté comme une obligation supprimée.",
    "Aucune charge nouvelle n'est identifiée : les quatre rubriques demeurent, sans nouvelle déclaration de cumul, preuve ou délai.",
    [effect(n,'coordination','naissance-supplementaire-non-cumul',
      "Correction de l'intervalle incluant à tort sa propre indemnité, sans élargir les cumuls entre prestations distinctes.",
      "Le 2° vise L331-3 à L331-9, intervalle qui inclut aussi L331-8-1 et L331-8-2.",
      "Le 2° vise L331-3 à L331-8 et L331-9 ; seuls les articles du congé supplémentaire lui-même sortent de cet intervalle.",
      'other',"Bénéficiaires de l'indemnité supplémentaire de naissance et organismes payeurs.",
      "Correction de portée sans remise en cause des créances et notes d'application de 2026, ni double paiement.",
      "Aucune nouvelle donnée, formalité ou compensation de revenu.",
      "2° Les indemnités journalières mentionnées aux articles L. 331-3 à L. 331-9 ;",
      "2° Les indemnités journalières mentionnées aux articles L. 331-3 à L. 331-8 et à l'article L. 331-9 ;")])

n='L332-1'
xml=by_number[n]['source_xml']
old="L'action de l'assuré pour le paiement des prestations en espèces de l'assurance maladie se prescrit par deux ans, à compter du premier jour du trimestre suivant celui auquel se rapportent lesdites prestations ; pour le paiement des prestations en espèces de l'assurance maternité, elle se prescrit par deux ans à partir de la date de la première constatation médicale de la grossesse."
new="L'action de l'assuré pour le paiement des prestations en espèces des assurances maladie et maternité se prescrit par deux ans, à compter du premier jour du trimestre suivant celui auquel se rapportent lesdites prestations."
assert old in xml
xml=xml.replace(old,new)
xml+="""<p>Le point de départ de la prescription des prestations en espèces de l'assurance maternité prévu au premier alinéa s'applique aux actions non prescrites à la date d'entrée en vigueur de la loi portant la présente rédaction et aux droits à prestations afférents aux périodes postérieures. Il ne peut abréger un délai déjà ouvert. Les prescriptions acquises avant cette date ne sont pas rouvertes. Les règles de prescription du capital décès et de l'action en recouvrement de l'indu, ainsi que les causes de suspension et d'interruption des prescriptions, demeurent applicables.</p>"""
rewrite(n,xml,
    "Réduction de fond de la contrainte de réclamation : suppression du départ anticipé de la prescription des indemnités de maternité à la première constatation de grossesse. Les prestations maladie et maternité ont le même délai de deux ans à partir du trimestre suivant la période concernée ; cela permet aussi un repère intelligible pour adoption et paternité, sans grossesse de l'assuré. Le capital décès et l'indu, y compris l'exception fraude ou fausse déclaration, restent intacts.",
    "Le délai reste de deux ans, aucun taux ou montant de prestation n'est changé. Application favorable aux actions non encore prescrites sans raccourcir un délai ouvert, et aux nouvelles périodes ; pas de réouverture des prescriptions acquises. La source ne réglait pas explicitement comment une première constatation de grossesse s'appliquait aux autres bénéficiaires de l'assurance maternité : incohérence identifiée, supprimée par le point de départ commun. Les délais de recours contre une décision de caisse restent distincts. L361-1 lu : le capital décès est une prestation, non un droit de succession ; sa prescription est conservée.",
    'material_reduction',
    "Le délai de réclamation de maternité ne commence plus avant la période indemnisée : la prescription anticipée liée au constat de grossesse est retirée. Le délai maladie et les règles capital décès/indu ne changent pas.",
    "L'allongement exact dépend des dates individuelles et n'est pas chiffré en jours ; aucune action déjà prescrite n'est rouverte ni aucun délai distinct de recours administratif ou contentieux modifié.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration ni preuve additionnelle du point de départ n'est créée. Les caisses peuvent devoir traiter des demandes plus tardives ; leur coût reste non chiffré et aucun gain national net n'est présumé.",
    [effect(n,'relief_extended','maternite-prescription-periode-indemnisee',
      "Suppression du point de départ anticipé fondé sur le constat de grossesse ; rattachement des deux ans aux périodes de prestations.",
      "Pour les indemnités de maternité : deux ans dès la première constatation médicale de grossesse, antérieure aux périodes normalement indemnisées.",
      "Pour les indemnités de maternité comme de maladie : deux ans dès le premier jour du trimestre suivant la période à laquelle les prestations se rapportent, sans raccourcir un délai ouvert.",
      'other',"Assurés demandant les prestations en espèces de l'assurance maternité, y compris ses congés familiaux.",
      "Actions non prescrites à l'entrée en vigueur et périodes postérieures ; délais déjà ouverts non abrégés, prescriptions acquises non rouvertes ; capital décès et indu inchangés.",
      "Aucun dépôt ou justificatif de remplacement ; traitement possible de réclamations plus tardives, coût public non établi.",
      "pour le paiement des prestations en espèces de l'assurance maternité, elle se prescrit par deux ans à partir de la date de la première constatation médicale de la grossesse.",
      new)],
    ["Suppression, pour les indemnités de maternité, du point de départ de prescription anticipé fixé à la première constatation médicale de la grossesse."])

n='L333-1'
xml=by_number[n]['source_xml'].replace(
    "articles L. 122-25-1-1 et L. 122-25-1-2 du code du travail",
    "articles L. 1225-10 et L. 1225-14 du code du travail")
rewrite(n,xml,
    "Coordination nécessaire à droit constant : remplacement des deux numéros de l'ancien code du travail par les articles actuels qui suspendent le contrat de la salariée faute de reclassement hors travail de nuit ou risque pour la grossesse. L'allocation, ses conditions contributives, les périodes assimilées et ses garanties de calcul et de saisissabilité restent intégrales ; aucune réduction matérielle n'est attribuée à cette correction.",
    "Nouveaux numéros absents du paquet reference-targets.json, donc vérifiés dans le corpus public travail.json : L1225-10 (LEGIARTI000006900889) et L1225-14 (LEGIARTI000006900893), sources et propositions lues en entier, renvoient tous deux expressément à L333-1 ; L1225-9/L1225-12 précisent les situations et le postnatal. Les identifiants anciens sont ceux de la source ; la correction ne crée pas de nouveau régime. L313-1 I 2° ne porte pas la durée minimale d'affiliation du II supprimée dans sa proposition ; L313-2 conserve les assimilations. L323-4 et L323-5 sont maintenus. La dispense d'ancienneté de l'indemnité patronale complémentaire des cibles travail ne devient pas le seuil d'un an de l'indemnité ordinaire de rupture. Note historique 2001/2002 conservée.",
    'coordination_only',
    "Les deux renvois obsolètes sont remplacés par les dispositions actuelles de suspension protectrice ; aucun changement de montant, de population ou de durée n'est revendiqué.",
    "Les règles de transmission proposées dans L1225-10 ne sont pas réécrites ni comptées comme une nouvelle coupe ici ; les régimes publics ne sont pas assimilés au contrat unique privé.",
    "Aucune charge nouvelle n'est identifiée : aucune demande, notification médicale ou condition d'ancienneté supplémentaire n'est créée par l'actualisation des numéros.",
    [effect(n,'coordination','maternite-suspension-renvois-recodifies',
      "Actualisation des renvois de suspension du contrat, en conservant l'allocation des salariées dispensées de travail.",
      "L333-1 vise les anciens L122-25-1-1 et L122-25-1-2 du code du travail.",
      "L333-1 vise L1225-10 et L1225-14, qui prévoient la suspension et citent l'allocation L333-1, sans modifier son assiette ou ses conditions.",
      'other',"Salariées enceintes ou ayant accouché dispensées de travail de nuit ou d'exposition à un risque faute de reclassement.",
      "Même protection hors congé légal de maternité, pour les contrats existants et futurs éligibles ; aucune rupture automatique.",
      "Aucune formalité ou condition d'ancienneté nouvelle ; les garanties de rémunération demeurent.",
      "Les salariées dont le contrat de travail est suspendu en application des articles L. 122-25-1-1 et L. 122-25-1-2 du code du travail",
      "Les salariées dont le contrat de travail est suspendu en application des articles L. 1225-10 et L. 1225-14 du code du travail")])

n='L341-2'
xml="""<p>Pour recevoir une pension d'invalidité, l'assuré doit justifier, au cours d'une période de référence, soit d'un montant minimum de cotisations fixé par référence au salaire minimum de croissance, soit d'un nombre minimum d'heures de travail salarié ou assimilé.</p>
<p>Aucune durée minimale d'affiliation distincte de ces conditions de cotisations ou d'heures de travail ne peut être exigée. Aucun justificatif de cette seule durée ne peut être demandé. Les périodes de référence, les périodes assimilées, les maintiens de droits et les dérogations plus favorables demeurent applicables.</p>
<p>La suppression de cette condition distincte s'applique aux arrérages de pension dus à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsque l'invalidité a été constatée auparavant. Elle ne dispense pas des conditions médicales d'invalidité ni des conditions de cotisations ou de travail salarié ou assimilé. Les arrérages afférents aux périodes antérieures, leurs créances, régularisations, restitutions, prescriptions et recours restent régis par les dispositions antérieures. Les prescriptions acquises et les décisions juridictionnelles irrévocables ne sont pas remises en cause ; aucun double paiement n'est permis.</p>"""
rewrite(n,xml,
    "Réduction de fond : suppression de la durée minimale d'affiliation cumulée avec un minimum contributif ou d'heures. La période de référence et l'alternative cotisations/heures restent l'ancrage assurantiel ; l'invalidité médicale demeure requise. Le délai d'affiliation distinct et le justificatif exclusivement associé ne sont remplacés par aucune déclaration, autorisation ou attente équivalente. Les assimilations et dérogations favorables restent ouvertes aux futures situations.",
    "Coordonner R313-5, lu au corpus : sa première phrase impose douze mois d'affiliation au premier jour du mois de l'interruption ou du constat ; seule cette condition doit disparaître. Ses branches a)/b) (2 030 SMIC ou 600 heures sur leurs périodes de douze mois/365 jours) ne sont pas supprimées ni transformées en ancienneté d'entreprise. R313-7/R313-8 lus : conserver professions saisonnières/discontinues, services à la personne et toutes assimilations. Le droit de demander la pension et les délais de R341-8 restent distincts ; pas de réouverture de prescription acquise. Notes de la source : rédaction applicable depuis le 1er janvier 2020 ; cette date n'est pas celle de la réforme future. L313-1 proposé supprime un délai similaire pour d'autres prestations, sans que cela suffise à supprimer celui, autonome, de l'invalidité. Droits nouveaux et coût social à chiffrer, sans compensation présumée.",
    'material_reduction',
    "La source exigeait simultanément une affiliation minimale et un minimum de cotisations ou d'heures. La condition temporelle autonome et sa preuve disparaissent ; le second test alternatif et l'appréciation médicale demeurent.",
    "R313-5 doit être coordonné ; le minimum contributif et ses périodes de référence restent opposables. Aucune baisse de taux de cotisation ni pension inchangée pour tous les statuts n'est démontrée, et le coût des droits supplémentaires reste inconnu.",
    "Aucune charge administrative nouvelle n'est identifiée : pas d'attestation ou contrôle de remplacement. Des pensions auparavant exclues par l'affiliation minimale pourront être servies, avec un coût pour l'assurance invalidité non chiffré ; les contrôles médicaux existants subsistent.",
    [effect(n,'obligation_removed','invalidite-fin-affiliation-minimale',
      "Retrait de la durée minimale d'affiliation et de la preuve de cette seule durée, en conservant le rattachement contributif et médical.",
      "Assurés : affiliation minimale cumulée avec l'alternative montant minimum de cotisations ou heures minimales ; R313-5 fixe l'affiliation distincte à douze mois.",
      "Assurés : aucun minimum autonome d'affiliation ; cotisations ou heures minimales et périodes de référence conservées, avec assimilations et dérogations favorables.",
      'legal_duty',"Assurés du régime général ouvrant un droit à pension d'invalidité, y compris invalidité constatée avant la réforme pour les arrérages futurs.",
      "Arrérages dus à compter de l'entrée en vigueur ; périodes antérieures, prescriptions acquises et décisions irrévocables protégées, sans double paiement.",
      "Aucune démarche de remplacement ; accès supplémentaire à pension et coût social à évaluer, aucune réduction de cotisation revendiquée.",
      "l'assuré doit justifier à la fois d'une durée minimale d'affiliation",
      "Aucune durée minimale d'affiliation distincte de ces conditions de cotisations ou d'heures de travail ne peut être exigée.")],
    ["Suppression de la durée minimale d'affiliation exigée en plus du minimum alternatif de cotisations ou d'heures de travail, ainsi que du justificatif de cette seule durée."])

out['L331-4-1']['benefit_review'] = "L'avantage est le choix de déplacer jusqu'à trois semaines de repos indemnisé prénatal vers le postnatal, avec augmentation égale de ce dernier. Il demeure ouvert pour les futures grossesses éligibles et les reports déjà engagés. La prescription médicale sécurise cet aménagement ; en cas d'arrêt, l'indemnité commence dès le premier jour et le reliquat reporté est ajusté, sans perte de la protection correspondante. Les régimes de base et allongements de L331-3/L331-4 sont conservés, sans condition d'ancienneté de rupture."
out['L331-8']['benefit_review'] = "Les avantages conservés sont l'indemnisation de vingt-cinq jours, portée à trente-deux en cas de naissances multiples, et la prolongation indemnisée pour hospitalisation immédiate de l'enfant dans le champ de L1225-35. L'élu local peut poursuivre son mandat et percevoir ses indemnités de fonction avec l'indemnité liée à son activité salariée ; s'il interrompt aussi le mandat et remplit L313-1, l'indemnité supplémentaire propre à ce titre reste possible. Ces avantages restent ouverts aux futures situations éligibles, y compris les bénéficiaires de la réserve QPC sur la filiation par reconnaissance conjointe, sans les réserver aux contrats anciens. Les non-cumuls ne constituent pas des exonérations supprimées et demeurent ciblés sur les autres revenus de remplacement."

# Les analyses de renvois sont renseignées explicitement dans le fichier suivant.
exec(Path('reference_assessments.py').read_text())

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2)+'\n')
