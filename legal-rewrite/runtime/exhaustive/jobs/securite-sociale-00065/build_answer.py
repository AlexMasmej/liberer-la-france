import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = json.loads((ROOT / 'source.json').read_text())
REFS = json.loads((ROOT / 'reference-targets.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}
ANSWER = {}


def paragraphs(number):
    return re.findall(r'<p>.*?</p>', BY_NUMBER[number]['source_xml'], re.S)


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml))).strip()


def finish_last_paragraph(parts, transition):
    result = list(parts)
    assert result[-1].endswith('</p>')
    result[-1] = result[-1][:-4].rstrip() + ' ' + transition + '</p>'
    return '\n'.join(result)


def effect(kind, measure, description, before, after, population, transition,
           source_quote, proposed_quote, unit='other', burdens='Aucune charge obligatoire de remplacement ; les autres conditions du régime demeurent.'):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def put(number, reason, notes, assessment, limitations, burdens,
        proposed=None, classification='retained_necessary', effects=None,
        removed=None, benefit=None):
    src = BY_NUMBER[number]
    obj = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft',
               classification=classification,
               substantive_impact=dict(version=1, classification=classification,
                   assessment=assessment, scope_limitations=limitations,
                   new_burdens_review=burdens, effects=effects or []),
               reference_checks=[])
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if benefit:
        obj['benefit_review'] = benefit
    ANSWER[number] = obj


def keep(number, reason, notes, assessment, limitations, benefit=None):
    put(number, reason, notes, assessment, limitations,
        "Aucune charge nouvelle n'est identifiée : le corps officiel est conservé intégralement, sans registre, pièce, déclaration, délai ou condition supplémentaire. Aucun solde de l'ensemble des codes n'est chiffré.",
        benefit=benefit)


# L512-2 : supprimer la condition supplémentaire propre aux enfants étrangers.
p = paragraphs('L512-2')
child_rule = "Pour les étrangers mentionnés au deuxième alinéa, et sous réserve des conditions propres à l'adoption ou à l'accueil en vue d'adoption prévues à l'article L. 512-4, l'ouverture du droit aux prestations familiales n'est subordonnée à aucune condition tenant au lieu de naissance, à la nationalité ou à la régularité de l'entrée ou du séjour de leurs enfants. Aucun justificatif de ces circonstances n'est exigé pour l'ouverture de ce droit, sans préjudice des éléments nécessaires à l'identification de l'enfant et à la preuve de sa charge et de sa résidence. Les autres conditions propres à chaque prestation demeurent applicables."
proposal = '\n'.join(p[:2] + ['<p>' + child_rule + '</p>',
    "<p>Un décret fixe la liste des titres et justifications attestant de la régularité de l'entrée et du séjour des bénéficiaires étrangers.</p>",
    "<p>La suppression des conditions et justificatifs propres à l'entrée et au séjour des enfants s'applique aux prestations dues à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris pour les enfants déjà à charge et les demandes en cours. Les droits, créances, restitutions, prescriptions et recours relatifs aux périodes antérieures restent régis par les dispositions qui leur sont applicables ; aucune restitution générale n'est créée.</p>"])
measure = 'prestations-familiales-fin-condition-sejour-enfant'
put('L512-2',
    "Réforme de fond : suppression de la condition supplémentaire de naissance en France ou d'appartenance à l'une des catégories d'entrée et de séjour des enfants de ressortissants de pays tiers, ainsi que des justificatifs correspondants. La résidence et le séjour régulier du bénéficiaire adulte, la charge effective et les conditions de chaque prestation demeurent. Le filtrage migratoire supplémentaire de l'enfant n'est pas nécessaire à la preuve de cette charge ; les règles de police des étrangers et de protection de l'enfant gardent leur objet propre. Aucun formulaire de remplacement n'est créé.",
    "Les sept voies alternatives de l'ancien troisième alinéa et de sa liste ne sont pas fermées : leurs bénéficiaires restent éligibles, et les autres enfants à charge le deviennent sans cette condition. Coordonner D512-2 (lu intégralement) en retirant ses justificatifs d'entrée et de séjour pour les périodes nouvelles ; D512-1 reste applicable à l'adulte. L'ancien renvoi au chapitre IV du titre III du livre III du CESEDA disparaît avec la condition, sans prétendre réécrire ce code extérieur. L512-1, lu en entier, conserve résidence, non-cumul personnel et détachement international. Identité, filiation ou charge peuvent toujours être établies, sans réintroduire le certificat migratoire de l'enfant. Note du 1er mai 2021 historique, sans date nouvelle de promulgation. Le coût des droits supplémentaires n'est pas établi.",
    "Les conditions d'entrée et de séjour propres aux enfants sont effectivement retirées et l'accès aux prestations est élargi. Ce n'est ni une baisse de cotisations ni une simple reprise du droit au réemploi des données.",
    "Le séjour régulier de l'adulte, la résidence, la charge et les conditions propres à chaque prestation restent exigés. La coordination réglementaire D512-2 et l'effet budgétaire restent à réaliser ou mesurer, sans revendiquer une suppression générale des contrôles migratoires.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration substitutive ni nouveau titre, registre ou délai. Les preuves ordinaires de l'identité, de la charge et de la résidence ne sont pas étendues. Le coût public de l'élargissement des droits reste inconnu.",
    proposed=proposal, classification='material_reduction', removed=[
        "Condition d'appartenance de chaque enfant à l'une des sept situations de naissance, d'entrée ou de rattachement migratoire énumérées après le troisième alinéa.",
        "Production des justificatifs propres à la régularité de l'entrée ou du séjour des enfants pour ouvrir le droit aux prestations familiales."],
    effects=[effect('relief_extended', measure,
        "Ouverture des prestations sans filtrage supplémentaire de la situation migratoire des enfants.",
        "Pour les étrangers du deuxième alinéa, chaque enfant devait relever d'une des situations limitativement énumérées ; les autres conditions de prestations s'y ajoutaient.",
        "Aucune condition de lieu de naissance, de nationalité ou d'entrée et de séjour de l'enfant ; conditions de l'adulte, de charge et de résidence conservées.",
        "Étrangers du deuxième alinéa ayant des enfants à charge, y compris les futures familles éligibles.",
        "Prestations dues dès l'entrée en vigueur, situations en cours incluses ; périodes antérieures et recours préservés.",
        "Ces étrangers bénéficient des prestations familiales sous réserve qu'il soit justifié, pour les enfants qui sont à leur charge et au titre desquels les prestations familiales sont demandées, de l'une des situations suivantes :",
        "l'ouverture du droit aux prestations familiales n'est subordonnée à aucune condition tenant au lieu de naissance, à la nationalité ou à la régularité de l'entrée ou du séjour de leurs enfants."),
        effect('obligation_removed', measure,
        "Retrait des justificatifs migratoires propres aux enfants, composante documentaire de la même mesure.",
        "Justificatifs de la situation de chaque enfant imposés par le troisième et le dernier alinéa, détaillés par D512-2.",
        "Ces justificatifs ne peuvent plus être exigés ; les preuves nécessaires à l'identité, à la charge et à la résidence subsistent.",
        "Familles de ressortissants de pays tiers relevant du deuxième alinéa.",
        "Même bascule que l'ouverture du droit élargie, sans remboursement rétroactif général.",
        "Il détermine également la nature des documents exigés pour justifier que les enfants que ces étrangers ont à charge et au titre desquels des prestations familiales sont demandées remplissent les conditions prévues aux alinéas précédents.",
        "Aucun justificatif de ces circonstances n'est exigé pour l'ouverture de ce droit, sans préjudice des éléments nécessaires à l'identification de l'enfant et à la preuve de sa charge et de sa résidence.", unit='legal_duty')])

keep('L512-3',
    "Maintien utile intégral : l'article ouvre les prestations jusqu'à la fin de l'obligation scolaire puis sous conditions d'âge et de rémunération, avec des limites d'âge spéciales et la dispense de condition de rémunération pour l'allocation de décès d'un enfant. Ces critères délimitent des droits sociaux ; il ne crée ni prélèvement accessoire ni dossier autonome à supprimer.",
    "L511-1 lu intégralement : les 3° et 4° désignent bien complément familial et allocation de logement, cette dernière relevant du CCH. Conserver la dérogation L545-1 et les transitions de la loi du 8 juin 2020 figurant en note, dont l'allocation transitoire, sans les prendre pour l'entrée en vigueur d'une réforme nouvelle. L'âge de l'enfant et sa rémunération ne sont pas l'ancienneté du salarié ni l'indemnité ordinaire de rupture.",
    "Aucune réduction supplémentaire démontrée : maintien des conditions générales d'ouverture et de leurs dérogations favorables, sans reformulation stylistique.",
    "Les âges, plafonds et règles spéciales restent à leur champ réglementaire. Aucun élargissement général des prestations et aucun effet fiscal successoral ne sont revendiqués.")

keep('L512-4',
    "Maintien intégral après examen de l'agrément : les deux voies d'adoption ou d'accueil protègent la réalité et la légalité du placement de l'enfant. L'agrément renvoyé au CASF est une garantie de protection des mineurs dans l'adoption internationale, et non un agrément économique redondant créé par la caisse. L'article maintient l'accès aux prestations pour les adoptions françaises et étrangères recevables.",
    "Conserver les deux branches 1° et 2°, l'autorité étrangère compétente, l'autorisation d'entrée à ce titre et les trois références L225-2, L225-3 et L225-17 CASF. Le texte extérieur intégral n'est pas fourni dans le corpus des cinq codes : aucune abrogation de sa procédure ni nouvelle pièce n'est déduite de ce renvoi. L'allègement L512-2 ne supprime pas ces garanties propres à l'adoption. Les futures adoptions recevables restent couvertes.",
    "Le contrôle de la validité de l'adoption est conservé comme protection essentielle de l'enfant ; aucune formalité doublonnée ni taxe autonome retirable n'est démontrée dans ce texte.",
    "Le maintien ne constitue pas une validation de l'ensemble du CASF ou de conventions internationales non jointes. Il ne crée aucun nouveau régime d'agrément ni aucune nouvelle autorisation.")

keep('L512-5',
    "Maintien intégral : la règle évite le double financement de prestations de même objet versées par des régimes français, étrangers ou internationaux, tout en gardant l'allocation différentielle favorable aux familles résidant en France. Ce n'est pas un prélèvement ni une déclaration répétitive ; sa suppression ferait perdre le fondement de coordination et celui du complément différentiel.",
    "Les deux périmètres ne sont pas identiques : le premier alinéa cite aussi les organisations internationales, le second vise les prestations et avantages servis selon les traités ou une législation étrangère de sécurité sociale. Ne pas étendre silencieusement ce second champ. Les règles de priorité de l'Union et des traités doivent garder leur portée supérieure ; aucun texte international non fourni n'est déclaré réécrit. Les familles futures éligibles conservent le différentiel.",
    "Aucun gain matériel nouveau : le non-cumul et le versement différentiel demeurent ensemble, avec leur champ exact et leur habilitation réglementaire.",
    "L'article ne chiffre ni le différentiel ni les priorités internationales applicables à une famille particulière ; aucun allègement des contributions nationales n'est établi.")

keep('L512-6',
    "Maintien nécessaire des droits du conjoint ou concubin vivant en métropole avec les enfants lorsque l'autre membre du couple réside outre-mer. La règle de non-cumul et l'allocation différentielle assurent la coordination sans fermer cet avantage aux futures familles ; aucune obligation documentaire ni autorisation autonome n'est créée ici.",
    "Conserver le champ textuel des départements ou territoires d'outre-mer et le fait que le droit métropolitain s'ouvre du chef du membre résidant en métropole avec les enfants. La dénomination historique des territoires ne vaut pas extension des compétences fiscales ou sociales de collectivités distinctes. Aucun transfert de cotisations vers la capitalisation n'intervient dans cet article.",
    "Maintien du mécanisme territorial favorable et de la prévention du cumul ; aucune simplification matérielle supplémentaire n'est comptée.",
    "Les régimes propres à chaque collectivité et le montant éventuel du différentiel ne sont pas déterminés ici. Aucune nouvelle recette ou économie nationale n'est avancée.")

keep('L513-1',
    "Maintien intégral : rattacher le versement à la personne physique assumant la charge effective et permanente de l'enfant garantit que la prestation finance son entretien. La réserve des règles particulières évite d'effacer partage, placement et dérogations. Aucun prélèvement, délai minimal, agrément ou justificatif supplémentaire n'est imposé par cet article.",
    "Articuler avec L521-2, notamment résidence alternée et aide sociale à l'enfance ; la qualité d'allocataire ne dépend pas d'un contrat de travail ou d'une année d'ancienneté. Les mêmes critères restent ouverts pour toutes futures situations éligibles. Le corps source est conservé sans modification de mots.",
    "La désignation du bénéficiaire demeure nécessaire à l'affectation des prestations ; aucun doublon administratif autonome retirable n'est établi.",
    "Ce maintien ne préjuge pas des conditions particulières à chaque prestation et ne signifie ni nouvelle demande de preuve ni automatisation chiffrée des versements.")

keep('L521-1',
    "Maintien intégral des allocations dès le deuxième enfant, de l'allocation forfaitaire d'un an lors du franchissement de l'âge limite et du complément dégressif. La variation selon ressources et nombre d'enfants organise la prestation ; l'indexation des plafonds et le lissage évitent des pertes de droit. Aucun taux de prélèvement ou dossier redondant n'est institué dans cet article.",
    "Conserver les deux premiers alinéas visés par la modulation, L521-3 pour les majorations, L512-3 2° pour l'âge, l'indice des prix hors tabac et le caractère annuel de la révision. L'allocation forfaitaire ne devient ni illimitée ni réservée aux situations anciennes. Les barèmes et montants sont réglementaires et ne sont pas inventés à partir de ce texte.",
    "Maintien d'avantages familiaux et de leur complément dégressif déjà existant ; aucune amélioration du lissage n'est attribuée à cette lecture seule.",
    "Le calcul individuel des plafonds et montants demeure réglementaire. Le maintien ne prouve aucune baisse de taxes, de cotisations ou du coût global des prestations.")

keep('L521-2',
    "Maintien intégral des règles d'allocataire, de partage par moitié en résidence alternée effective et des garanties pour les enfants confiés à l'aide sociale à l'enfance. La faculté judiciaire de maintien du versement à la famille est un avantage essentiel à conserver, y compris pour les placements futurs. La désignation et le contrôle du placement ont une fonction propre ; aucun agrément économique ou double déclaration n'est établi.",
    "Le renvoi L323-1 appartient expressément au code de la justice pénale des mineurs, non au CSS L323-1 joint par rapprochement de numéro. Les articles civils 373-2-9, 375-3 et 375-5 gardent leur objet distinct. Conserver les quatre cas a) à d), la règle d'ouverture du chef du père ou à défaut de la mère et les conditions du titre I, sans les transformer en ancienneté d'emploi. Les notes d'entrée en vigueur pénale des mineurs de 2021 sont historiques. Aucun renvoi au contrat unique ne figure dans le corps.",
    "Aucune réduction matérielle supplémentaire n'est justifiée au détriment des règles de garde et de placement. Le partage, les voies judiciaires et les exceptions favorables sont maintenus.",
    "Le contenu du CJPM n'est pas remplacé par un article homonyme du CSS. Le maintien n'évalue ni tous les règlements d'allocataire ni l'ensemble du droit de l'autorité parentale.")

keep('L521-3',
    "Maintien intégral des majorations selon l'âge et du bénéfice pour chaque enfant lorsque le nombre d'enfants requis est atteint. Ce sont des avantages sociaux, non des charges à supprimer ; retirer l'exception de l'aîné ou les seuils sans étude créerait une prestation différente plutôt qu'une suppression administrative démontrée.",
    "Conserver l'exception du plus âgé, la dérogation pour les familles du nombre d'enfants déterminé et l'âge minimum réglementaire. Le renvoi du deuxième alinéa au premier reste cohérent. Les montants restent soumis à la modulation L521-1 ; l'avantage est maintenu pour les futures familles éligibles.",
    "Aucun nouveau gain : les deux branches de majoration sont conservées intégralement avec leurs conditions et leur exception favorable.",
    "Aucun montant, âge réglementaire nouveau ou extension de population n'est décidé. Ce maintien n'est pas compté comme réécriture ou baisse de prélèvement.")

keep('L522-1',
    "Maintien intégral du fondement du complément familial sous plafond, selon le nombre et l'âge des enfants. L'article est nécessaire au droit à prestation et ne comporte pas de formalité autonome supprimable. La suppression d'un revenu professionnel minimal pour la majoration de plafond est portée dans les articles qui régissent cette majoration, sans supprimer le complément.",
    "Le premier alinéa de L531-1 vise bien l'âge limite général de la PAJE ; D531-1 et R522-1, lus intégralement, fixent respectivement trois ans et les conditions de trois enfants avec dérogation d'âge jusqu'à vingt et un ans. La note de 2003 conserve ses cohortes nées ou adoptées à compter de 2004 et la naissance présumée. Aucun seuil d'emploi nouveau n'est déduit du contrat unique.",
    "Le droit au complément familial et son articulation d'âge avec la PAJE sont conservés ; aucune formalité ou taxe nouvelle n'est retirée par cet article lui-même.",
    "Les conditions réglementaires de nombre, d'âge et de rémunération restent distinctes de la majoration de ressources réformée dans L522-2 et L522-3. Aucun solde financier global n'est établi.")

# Majoration des plafonds : une seule mesure pour les quatre prestations concernées.
income_measure = 'prestations-familiales-fin-revenu-professionnel-minimal'
income_transition = "La suppression de toute condition de montant minimal du revenu professionnel pour la majoration du plafond s'applique aux prestations dues à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris aux droits en cours et aux futures ouvertures de droit. Les périodes antérieures, leurs créances, régularisations, prescriptions et recours demeurent régis par les dispositions qui leur sont applicables, sans restitution générale ni réduction d'un avantage plus favorable."


def income_effect(number, source_quote, proposed_quote, description, lead=False):
    return effect('relief_extended' if lead else 'coordination', income_measure, description,
        "Majoration pour couples à deux revenus professionnels, subordonnée par R522-2, directement ou par renvoi, à un revenu annuel de chacun au moins égal à 13,6 % du PASS de l'année de référence ; montant et assiette de la prestation inchangés ici.",
        "Majoration maintenue aux mêmes niveaux pour les personnes seules et pour tout couple dont chaque membre a un revenu professionnel, sans montant minimal de celui-ci ; plafond global et autres conditions de la prestation conservés.",
        {'L522-2': 'Ménages à deux revenus professionnels demandant le complément familial.',
         'L522-3': 'Ménages à deux revenus professionnels demandant le montant majoré du complément familial.',
         'L531-2': "Ménages à deux revenus professionnels demandant la prime à la naissance ou à l'adoption.",
         'L531-3': "Ménages à deux revenus professionnels demandant l'allocation de base à taux plein."}[number],
        "Prestations dues dès l'entrée en vigueur, droits en cours et situations futures inclus ; périodes antérieures, personnes seules et avantages plus favorables préservés.",
        source_quote, proposed_quote,
        burdens="Aucune attestation, déclaration ou durée d'activité supplémentaire ; la nature professionnelle du revenu et les autres ressources restent appréciées selon les règles existantes. Dépense publique supplémentaire non chiffrée.")

p = paragraphs('L522-2')
old = "Il est majoré lorsque la charge des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel, soit par une personne seule."
new = "Il est majoré lorsque la charge des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel, sans condition de montant minimal de ce revenu, soit par une personne seule."
p[0] = p[0].replace(old, new)
put('L522-2',
    "Coordination législative de la suppression commune du revenu professionnel minimal, portée comme mesure de fond dans L531-2 : la majoration du plafond du complément familial ne reste pas subordonnée au plancher réglementaire de R522-2. Le texte source législatif ne mentionnait déjà pas de montant minimal ; la précision neutralise cette condition réglementaire sans compter une seconde suppression. Plafond global, nombre et rang des enfants, majoration des personnes seules et complément différentiel restent entiers.",
    "R522-2 lu en entier : son troisième alinéa exige 13,6 % du PASS pour chacun pendant l'année de référence. Coordonner ce seul seuil, en conservant l'assiette des revenus professionnels, l'année de référence, les majorations de 25 % et 30 % selon les enfants et l'indexation. R522-3, lu intégralement, conserve le complément différentiel de douze mensualités et son calcul au douzième ; aucun montant nouveau. R522-4 et R531-1 doivent reprendre la même suppression pour leurs propres plafonds, coordonnée ici à L522-3, L531-2 et L531-3. Une seule mesure dédupliquée ; dépense supplémentaire à évaluer, aucune économie nationale présumée.",
    "Coordination du complément familial avec la même suppression du revenu professionnel minimal que L531-2. La précision empêche le seuil réglementaire de subsister dans ce champ ; elle n'est pas une seconde formalité supprimée ni un allègement fiscal autonome.",
    "Cette mesure ne supprime pas la condition de ressources globale, ne modifie pas les revenus pris en compte et ne revalorise pas les taux de prestation. Les coordinations réglementaires et le coût public restent à établir.",
    "Aucune charge nouvelle n'est identifiée : suppression d'un seuil sans attestation ni démarche de remplacement. La vérification existante de la nature professionnelle des revenus subsiste ; le solde national n'est pas chiffré.",
    proposed=finish_last_paragraph(p, income_transition), classification='coordination_only',
    removed=["Condition de revenu professionnel annuel minimal de chacun des membres du couple pour la majoration du plafond du complément familial, actuellement fixée réglementairement à 13,6 % du PASS."],
    effects=[income_effect('L522-2', old, new,
        "Coordination du plafond du complément familial avec la suppression du revenu professionnel minimal, portée par la même mesure que L531-2.")])

p = paragraphs('L522-3')
old = "Ce plafond est majoré lorsque la charge des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel, soit par une personne seule."
new = "Ce plafond est majoré lorsque la charge des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel, sans condition de montant minimal de ce revenu, soit par une personne seule."
p[0] = p[0].replace(old, new)
put('L522-3',
    "Réforme de fond coordonnée : la suppression du plancher de revenu professionnel vaut également pour la majoration du plafond propre au montant majoré du complément familial. Sans cette coordination, R522-4 pourrait conserver le seuil par renvoi à R522-2. Le plafond inférieur, son adaptation au nombre d'enfants, les personnes seules, l'indexation et les deux taux fixés par décret demeurent intégralement.",
    "R522-4, lu en entier, fixe le plafond à la moitié de celui de R522-2 et renvoie aux deuxième et troisième alinéas pour ses majorations ; conserver cette moitié et les montants de majoration, retirer seulement le seuil de revenu professionnel. D522-1 et D522-2 lus intégralement : 41,65 % et 62,48 % de la base mensuelle restent distincts et inchangés. Aucune nouvelle réduction de taxe ne découle de ce renvoi ; même measure_id que la mesure portée à L531-2 et coordonnée à L522-2. Les prestations supplémentaires possibles sont une dépense non chiffrée.",
    "L'avantage du plafond majoré ne reste pas bloqué par le seuil retiré à L522-2 ; il s'agit du volet coordonné de la même suppression de condition, sans deuxième mesure indépendante.",
    "Le plafond d'accès au montant majoré reste inférieur à celui du complément ordinaire. La réforme ne supprime ni ciblage des ressources ni contrôle de la nature des revenus ; coordination R522-4 nécessaire.",
    "Aucune charge nouvelle n'est identifiée : aucun dossier de majoration distinct, aucun justificatif ou délai supplémentaire. Les données et conditions existantes sont simplement appréciées sans plancher de revenu professionnel.",
    proposed=finish_last_paragraph(p, income_transition), classification='coordination_only',
    removed=["Application au plafond du complément familial majoré d'un montant minimal de revenu professionnel de chacun des deux membres du couple, par le renvoi réglementaire à R522-2."],
    effects=[income_effect('L522-3', old, new,
        "Coordination de la suppression commune du revenu professionnel minimal pour le plafond du complément familial majoré.")])

keep('L523-1',
    "Maintien intégral des quatre causes d'ouverture de l'allocation de soutien familial, du différentiel lorsque la contribution alimentaire est faible, de l'ouverture de plein droit aux bénéficiaires du RSA visés et des cinq formes de titre exécutoire. Les conditions servent à protéger l'enfant et à recouvrer son entretien ; les supprimer affaiblirait le droit à prestation ou sa preuve, sans doublon administratif démontré.",
    "Conserver le II, transmission ciblée de l'adresse et de la solvabilité après contrôle au parent bénéficiaire, sans accès nouveau aux données. Au IV, force exécutoire et cinq voies alternatives évitent un passage judiciaire unique obligatoire ; ne pas remplacer ces dispenses par une autorisation. Le 4° du I prévoit déjà une voie en l'absence de titre, à définir par décret. Les renvois CASF, civil et CPCE gardent leur objet extérieur ; ils ne sont pas déclarés réécrits. Aucun droit sur une succession n'est créé par l'allocation pour enfant orphelin.",
    "Les garanties d'entretien, les voies de preuve alternatives et l'allocation différentielle sont maintenues intégralement ; aucune formalité inutile distincte n'est établie dans le texte assigné.",
    "Le maintien ne vérifie pas tous les titres exécutoires extérieurs ni ne chiffre les contributions alimentaires. Les protections contre la fraude et le recours au juge restent à leur champ propre.")

keep('L523-2',
    "Maintien intégral de la qualité d'allocataire assumant la charge effective et permanente et du ciblage du soutien familial sur le parent sans vie de couple. Cette condition définit la population de la prestation ; elle n'est ni une taxe ni une formalité inutile. L'article ne ferme aucun avantage à une situation future satisfaisant les mêmes critères, notamment celle de la personne autre que les parents visée au premier alinéa.",
    "La cessation au mariage, PACS ou concubinage vise textuellement le père ou la mère titulaire du droit ; ne pas l'étendre à toute personne physique du premier alinéa. Les assimilations d'orphelin restent celles de L523-1, y compris absence de filiation ou défaillance alimentaire. L'article ne doit pas supprimer les dérogations de durée de la PreParE prévues par L531-4, régime distinct. Aucune obligation de déclaration de couple supplémentaire n'est ajoutée.",
    "Maintien d'un critère de population constitutif de la prestation et de son ouverture aux personnes assumant l'enfant ; aucune suppression administrative nouvelle n'est démontrée.",
    "Étendre le soutien à toutes les familles en couple serait une réforme de dépense distincte, non une baisse de prélèvement démontrée. Aucun rendement ni économie ne découle de ce maintien.")

# Corriger un renvoi réellement discordant sans modifier le pouvoir de fixation des taux.
proposal = "<p>Un décret en Conseil d'Etat fixe les taux respectifs de l'allocation dans les deux cas suivants :</p><p>1°) l'enfant est orphelin de père et de mère ou se trouve dans une situation qui y est assimilée, au sens de l'article L. 523-1 ;</p><p>2°) l'enfant est orphelin de père ou de mère ou se trouve dans une situation qui y est assimilée, au sens de l'article L. 523-1.</p>"
put('L523-3',
    "Coordination nécessaire, sans réduction matérielle revendiquée : le texte source attribue la fixation des taux au décret prévu à L584-1 alors que cet article exclut expressément les fixations de taux. L'habilitation autonome à un décret en Conseil d'Etat est conservée ici, avec les deux catégories d'orphelins et assimilés, mais sans le renvoi contradictoire. Aucun taux ni condition d'accès n'est changé.",
    "L584-1 a été lu en entier : il détermine les mesures d'application du livre V autres que les fixations de taux et les mesures du chapitre 2 du titre IV. C'est une incohérence préexistante signalée et corrigée, pas une suppression de contrôle. L523-1 conserve intégralement ses assimilations, ses quatre cas et ses voies exécutoires. La nature de décret en Conseil d'Etat est maintenue pour éviter tout abaissement implicite de garantie ; aucune entrée en vigueur chiffrée nouvelle ni réouverture des droits anciens.",
    "Seul le renvoi à une habilitation excluant les taux est retiré. Le pouvoir réglementaire, les deux catégories et tous les droits sont conservés ; aucune économie ou baisse de charge n'est démontrée.",
    "La correction n'arrête pas les taux réglementaires ni leurs revalorisations et ne vaut pas réécriture des dispositions réglementaires. Les montants de l'allocation ne sont pas modifiés.",
    "Aucune charge nouvelle n'est identifiée : même décret en Conseil d'Etat et mêmes deux cas d'ouverture, sans dépôt, donnée, délai, registre ou condition supplémentaire.",
    proposed=proposal, classification='coordination_only', effects=[effect('coordination', 'asf-habilitation-taux-renvoi-coherent',
        "Remplacement du renvoi discordant à L584-1 par l'habilitation directe du même niveau réglementaire.",
        "Décret en Conseil d'Etat dit prévu à L584-1, lequel exclut les fixations de taux.",
        "Décret en Conseil d'Etat directement habilité par L523-3, mêmes deux catégories et mêmes prestations.",
        "Enfants orphelins ou assimilés et personnes allocataires de l'allocation de soutien familial.",
        "Correction de référence sans modification des montants, des périodes passées ou des droits futurs.",
        "Le décret en Conseil d'Etat prévu à l'article L. 584-1 fixe les taux respectifs de l'allocation dans les deux cas suivants :",
        "Un décret en Conseil d'Etat fixe les taux respectifs de l'allocation dans les deux cas suivants :", unit='regime')])

keep('L531-1',
    "Maintien intégral de l'architecture de la PAJE et de ses quatre prestations. La non-condition de ressources pour la PreParE et le complément de garde lorsque prime ou allocation de base ne sont pas ouvertes est une dérogation favorable, comme le principe de cumul sous les conditions spéciales. Supprimer cette disposition priverait des familles de droits sans retirer une charge essentielle au fonctionnement du système.",
    "Les articles L531-2, L531-3, L531-4, L531-5 à L531-9 restent les régimes particuliers ; le cumul général est à lire avec L531-9, non comme un cumul inconditionnel à taux plein. L531-5 fourni comprend déjà la coordination d'exclusion des indemnités de rupture pour ses plafonds. Cette règle n'impose aucune forme ni ancienneté du contrat au parent ou à la personne gardant l'enfant. La transition de 2014 distingue enfants nés ou adoptés avant et à compter du 1er octobre 2014 ; elle reste conservée par la source et ses notes.",
    "Aucun gain supplémentaire : maintien des quatre composantes, de la dispense favorable de ressources pour deux d'entre elles et du principe de cumul articulé aux règles spéciales.",
    "Ce maintien ne supprime pas les non-cumuls de L531-9 et ne revalorise pas les prestations. Les règles nouvelles du contrat unique ne sont pas artificiellement transposées à l'ouverture des droits familiaux.")

p = paragraphs('L531-2')
old = "Il est majoré lorsque la charge du ou des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel minimal, soit par une personne seule."
new = "Il est majoré lorsque la charge du ou des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel, sans condition de montant minimal de ce revenu, soit par une personne seule."
p[2] = p[2].replace(old, new)
put('L531-2',
    "Réforme de fond : suppression du revenu professionnel minimal pour la majoration du plafond de la prime à la naissance ou à l'adoption, avec coordination de la même mesure dans L522-2, L522-3 et L531-3. La condition de satisfaire et d'établir ce minimum disparaît ; il ne s'agit pas de supprimer la prise en compte des ressources globales. Tous les alinéas de versement sont conservés : prime avant la naissance, adoption majorée et au-delà de l'âge ordinaire, naissances précoces, décès au-delà de la vingtième semaine, ainsi que les plafonds, leurs montants réglementaires et leur indexation.",
    "R531-1 renvoie aux deuxième et troisième alinéas de R522-2 ; ces textes ont été lus en entier et le plancher de 13,6 % du PASS doit cesser dans le nouveau champ, sans retirer l'année de référence ni les montants favorables. D531-2 conserve 229,75 % et 459,5 % de la base mensuelle et le versement d'adoption au plus tard au deuxième mois. Les règles de paiement avant la fin du mois suivant le sixième mois et la vingtième semaine ne sont pas déplacées. Les notes protègent les grossesses commencées dès le 1er octobre 2020 et le paiement transitoire d'avril 2021 ; elles ne datent pas la nouvelle réforme. Même mesure que L522-2, coût de l'extension inconnu.",
    "La condition de satisfaire et d'établir un revenu professionnel minimal est effectivement retirée de la majoration du plafond de prime. L'avantage est élargi sans supprimer la déclaration des ressources globales. Les trois articles de coordination de cette même mesure ne constituent pas trois suppressions supplémentaires.",
    "La condition globale de ressources, les conditions d'adoption et les dates propres aux prestations restent exigées. La coordination de R531-1 est nécessaire ; le surcroît de droits et son coût ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : le revenu reste de nature professionnelle mais aucun montant minimal, certificat de remplacement ou nouveau dépôt ne s'ajoute. Les autres pièces légalement nécessaires ne sont pas étendues.",
    proposed=finish_last_paragraph(p, income_transition), classification='material_reduction',
    removed=["Exigence d'un revenu professionnel minimal de chacun des membres du couple pour obtenir la majoration du plafond de la prime à la naissance ou à l'adoption."],
    benefit="Sont préservés pour les droits en cours et toutes futures situations recevables : prime pour chaque enfant à naître avant sa naissance, prime pour chaque enfant adopté dès l'arrivée au foyer et même au-delà de l'âge ordinaire mais avant la limite L512-3 2°, majoration d'adoption, versement anticipé avant la fin du mois suivant le sixième mois, dérogations pour naissance avant ce mois et décès au-delà de la vingtième semaine. Le plafond selon les enfants nés ou à naître, sa majoration pour personnes seules et couples à deux revenus et son indexation demeurent ; seul le revenu minimal des deux actifs disparaît, ce qui élargit l'avantage. Ni taux ni versement n'est réduit ; les cohortes historiques des notes restent protégées.",
    effects=[income_effect('L531-2', old, new,
        "Suppression du revenu professionnel minimal pour la majoration des plafonds familiaux ; les trois autres articles concernés coordonnent cette même mesure.", lead=True),
        effect('obligation_removed', income_measure,
        "Suppression de l'exigence d'établir un montant professionnel minimal pour chacun des deux membres du couple afin d'obtenir le plafond majoré.",
        "Le demandeur doit satisfaire et établir, pour chacun des deux membres du couple, un revenu professionnel minimal ; R531-1 renvoie au seuil de 13,6 % du PASS de R522-2. Les ressources globales restent par ailleurs prises en compte.",
        "Seule la nature professionnelle du revenu reste nécessaire pour cette majoration : aucun montant minimal à atteindre ou à établir. Les ressources globales et le plafond général restent contrôlés.",
        "Couples à deux revenus professionnels, pour la prime à la naissance ou à l'adoption et, par coordination, les autres plafonds concernés.",
        "Prestations dues à compter de l'entrée en vigueur, droits en cours et futures situations recevables compris ; périodes antérieures préservées.",
        old, new, unit='legal_duty',
        burdens="Aucune déclaration de remplacement ni retrait des données de ressources globales nécessaires. Il s'agit de la condition retirée dans la même mesure, sans seconde suppression de formulaire ni économie chiffrée.")])

p = paragraphs('L531-3')
old = "Elle est versée à taux plein lorsque les ressources ne dépassent pas un plafond qui varie selon le nombre d'enfants nés ou à naître et qui est majoré lorsque la charge du ou des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel minimal, soit par une personne seule."
new = "Elle est versée à taux plein lorsque les ressources ne dépassent pas un plafond qui varie selon le nombre d'enfants nés ou à naître et qui est majoré lorsque la charge du ou des enfants est assumée soit par un couple dont chaque membre dispose d'un revenu professionnel, sans condition de montant minimal de ce revenu, soit par une personne seule."
p[0] = p[0].replace(old, new)
old_duration = "La durée de versement de l'allocation est égale à celle définie au premier alinéa du présent article."
new_duration = "La durée de versement de l'allocation pour chaque enfant adopté ou confié en vue d'adoption est égale à la période comprise entre la naissance et l'âge limite mentionné au premier alinéa de l'article L. 531-1 ; elle est décomptée à compter de l'arrivée de l'enfant au foyer, dans la limite de l'âge mentionné au 2° de l'article L. 512-3."
p[2] = p[2].replace(old_duration, new_duration)
put('L531-3',
    "Réforme de fond coordonnée : suppression du revenu professionnel minimal pour la majoration du plafond de l'allocation de base à taux plein, avec les plafonds et taux partiel ou plein conservés. Coordination distincte d'une incohérence préexistante : le premier alinéa ne fixe aucune durée, alors que le troisième prétend y renvoyer pour l'adoption. La proposition rattache explicitement cette durée à celle de l'allocation de base pour une naissance et à l'arrivée au foyer, sans inventer une nouvelle durée chiffrée. Les limites d'âge et le cumul pour naissances ou adoptions multiples sont maintenus.",
    "R531-1 et R522-2 lus intégralement : retrait coordonné du seuil de 13,6 % du PASS. L'égalité de plafond et de taux avec le complément familial est conservée et coordonnée à L522-2. D531-1 fixe l'âge ordinaire à trois ans et D531-3 les taux à 41,65 % et 20,825 % ; aucun de ces chiffres n'est modifié. Le renvoi interne de durée était matériellement vide : la rédaction retient expressément la durée ordinaire de versement comme règle d'adoption, sans présenter cette résolution comme une économie. Les cohortes jusqu'au 31 mars 2018 et à compter du 1er avril 2018 gardent leurs règles de fixation/revalorisation indiquées dans les notes, sous réserve du nouvel allègement pour les prestations nouvelles. Les durées plus favorables légalement acquises restent protégées.",
    "Le plancher de revenu professionnel est retiré dans le même dispositif de majoration des plafonds. La correction du renvoi de durée n'est pas comptée comme une seconde réduction ni comme une nouvelle prestation chiffrée.",
    "Plafond global, taux, limite d'âge de l'adoption et limitation du cumul demeurent. L'effet individuel de la correction de durée n'est pas chiffré à partir du renvoi source incohérent ; coordinations réglementaires à effectuer.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration ou de preuve supplémentaire, suppression du seul revenu minimal et clarification du point de départ de la durée d'adoption. Aucun solde global des codes n'est établi.",
    proposed=finish_last_paragraph(p, income_transition + " Les durées de versement plus favorables légalement acquises avant cette entrée en vigueur demeurent garanties."), classification='coordination_only',
    removed=["Condition de revenu professionnel minimal de chacun des membres du couple pour la majoration du plafond d'accès à l'allocation de base à taux plein."],
    effects=[income_effect('L531-3', old, new,
        "Coordination de la suppression commune du revenu minimal pour le plafond de l'allocation de base à taux plein."),
        effect('coordination', 'paje-adoption-duree-renvoi-coherent',
        "Résolution explicite d'un renvoi interne qui ne définit pas la durée de versement d'adoption.",
        "Renvoi à une durée prétendument définie au premier alinéa, qui ne traite que des plafonds et taux.",
        "Durée de versement ordinaire pour une naissance, comptée depuis l'arrivée au foyer, sous la limite d'âge L512-3 2° ; durées acquises plus favorables protégées.",
        "Allocataires pour enfants adoptés ou confiés en vue d'adoption.",
        "Règle complète de durée, sans nouvelle durée chiffrée et sans réduction des durées antérieurement acquises.", old_duration, new_duration, unit='regime')])

# PreParE : laisser subsister la durée de taux garanti, ouvrir la hausse anticipée.
p = paragraphs('L531-4')
old_lock = "Il ne peut y avoir révision de ce taux au cours de cette durée qu'en cas de cessation de l'activité ou de la formation."
new_lock = "Au cours de cette durée, le taux est révisé en cas de cessation de l'activité ou de la formation, ainsi que, à la demande du bénéficiaire, lorsqu'une réduction de la quotité de l'activité ou de la formation ouvre droit à un montant plus élevé. Dans ce dernier cas, la révision prend effet le premier jour du mois civil suivant celui du changement. Elle ne réduit pas la durée de droit restant à courir."
p[5] = p[5].replace(old_lock, new_lock)
prepare_transition = "La révision anticipée plus favorable prévue au dernier alinéa du 2 du I s'applique aux changements de quotité intervenant à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris aux droits en cours. Elle n'exige ni nouvelle ouverture de droit ni durée minimale supplémentaire et ne remet pas en cause le maintien du taux antérieurement attribué lorsqu'il demeure plus favorable. Les droits, créances, régularisations, prescriptions et recours relatifs aux périodes antérieures restent soumis aux règles qui leur sont applicables."
put('L531-4',
    "Réforme de fond limitée à une contrainte effective : durant la période minimale au même taux, une baisse de quotité peut désormais ouvrir une prestation à taux partiel plus élevée dès le mois suivant, sans attendre la fin du blocage. La garantie de maintien du taux, la cessation ouvrant le taux plein, les options majorées, les durées étendues et tous les autres I à VI sont maintenus intégralement. Il ne s'agit pas de supprimer les durées minimales de versement favorables ni de remplacer la condition d'activité sociale par l'ancienneté d'un contrat.",
    "R531-3, R531-4 et D531-4 ont été lus intégralement : R531-4 fixe six mensualités au même taux, et D531-4 distingue les quotités au plus égales à 50 % puis supérieures à 50 % et au plus égales à 80 %. Coordonner la révision favorable avec ces textes sans réduire la garantie de taux ni les règles propres à la cessation. Les durées d'adoption de D531-14 (douze mois et cas de trois ans) restent favorables et intactes. Conserver II abrogé, les six subdivisions, la déclaration sur l'honneur des non-salariés et les options définitives du VI. Signaler l'articulation préexistante à contrôler entre le plancher de cumul au taux plein au III et le seul plafond de D531-4 II : aucune correction silencieuse. Les quotités réglementaires fondées sur la durée légale doivent être coordonnées avec la transition 35/40 heures, sans présumer qu'une règle de contrat privé réécrit les autres statuts.",
    "La restriction empêchant une hausse du taux partiel avant l'issue des six mensualités est effectivement levée lorsque l'activité ou la formation diminue. Les autres garanties et options favorables ne sont pas réduites.",
    "Pas de modification des montants, durées totales, anciennetés professionnelles ou règles de non-cumul. La révision est favorable et prospective ; les textes réglementaires de quotité et de mensualité restent à coordonner. Dépense supplémentaire inconnue.",
    "La demande de révision reste facultative pour le bénéficiaire, sans nouvelle attestation ni réouverture de droit. En revanche, l'organisme doit instruire cette nouvelle voie de révision et appliquer le taux supérieur dès le mois suivant le changement : ce traitement obligatoire supplémentaire est recensé, d'où le classement mixed. Son coût et le solde net de complexité ne sont pas établis.",
    proposed='\n'.join(p + ['<p>VII.-' + prepare_transition + '</p>']), classification='mixed',
    removed=["Interdiction de réviser à la hausse la prestation à taux partiel pendant la durée minimale au même taux lorsque la quotité diminue sans cessation totale d'activité ou de formation."],
    benefit="Tous les avantages possibles de l'article restent ouverts aux futures situations recevables : taux plein en cessation ou formation non rémunérée, taux partiel selon quotité et voies adaptées aux non-salariés et élus ; garantie du taux minimalement attribué ; durées selon rang, partage entre parents et prolongations pour parents seuls, y compris après remise en couple ; attente insatisfaite d'une place d'accueil ou scolaire ; assimilations d'activité antérieure ; droits des deux parents avec les garanties de cumul du III. Les durées minimales d'adoption, dérogations d'âge et extensions pour naissances ou adoptions multiples des IV et V restent entières. Le VI conserve cumul temporaire avec revenu de reprise, option majorée, partage, prolongation et maintien après remise en couple, avec leurs conditions et caractères définitifs. Seule l'impossibilité d'obtenir un meilleur taux avant la fin de la période minimale est levée ; aucun de ces avantages n'est réservé aux seuls anciens bénéficiaires.",
    effects=[effect('relief_extended', 'prepare-revision-anticipee-favorable',
        "Ouverture d'une révision plus favorable du taux partiel lorsque la quotité diminue pendant la période minimale.",
        "Même taux pendant la durée minimale fixée par décret à six mensualités ; seule une cessation permettait la révision anticipée.",
        "Taux partiel supérieur accessible sur demande dès le premier jour du mois suivant une réduction de quotité ; garantie du taux plus favorable et durée restante conservées.",
        "Bénéficiaires d'une PreParE à taux partiel dont l'activité ou la formation rémunérée diminue dans les conditions du barème.",
        "Changements de quotité dès l'entrée en vigueur, y compris droits en cours ; aucune révision rétroactive générale.",
        old_lock, "Dans ce dernier cas, la révision prend effet le premier jour du mois civil suivant celui du changement.",
        burdens="Demande facultative de révision favorable et traitement nouveau par l'organisme, sans nouveau justificatif ni réouverture de droit ; aucune période minimale supplémentaire. Coût public non chiffré."),
        effect('obligation_removed', 'prepare-revision-anticipee-favorable',
        "Retrait de l'obligation de maintenir sans révision le taux partiel durant la période minimale lorsqu'une réduction de quotité justifie une hausse.",
        "Obligation de conserver le même taux pendant six mensualités, sauf cessation totale de l'activité ou de la formation.",
        "Cette obligation cesse pour les demandes de hausse liées à une réduction de quotité ; la garantie du taux plus favorable reste intacte dans les autres cas.",
        "Organismes débiteurs et bénéficiaires d'une PreParE à taux partiel dont l'activité ou la formation diminue.",
        "Changements intervenant dès l'entrée en vigueur ; droits en cours compris et périodes antérieures préservées.",
        old_lock, "Au cours de cette durée, le taux est révisé en cas de cessation de l'activité ou de la formation, ainsi que, à la demande du bénéficiaire, lorsqu'une réduction de la quotité de l'activité ou de la formation ouvre droit à un montant plus élevé.",
        unit='legal_duty', burdens="Traitement public de la révision ajouté en contrepartie de cette même levée du blocage ; aucun gain net chiffré."),
        effect('obligation_added', 'prepare-revision-anticipee-favorable',
        "Obligation pour l'organisme de traiter les demandes de révision anticipée favorable et de liquider la hausse au mois suivant le changement.",
        "La révision en cours de période minimale n'était permise que pour une cessation ; aucune révision pour une simple réduction de quotité ne devait être instruite sur ce fondement.",
        "L'organisme examine aussi la réduction de quotité ouvrant un taux supérieur, sur demande, et liquide l'effet au premier jour du mois suivant le changement.",
        "Organismes débiteurs de la PreParE ; demande facultative des bénéficiaires concernés.",
        "Même transition que la levée du blocage, sans réouverture de droit ni prolongation de la durée totale.",
        old_lock, new_lock, unit='legal_duty',
        burdens="Nouvelle voie de liquidation et règle de prise d'effet à mettre en œuvre par l'organisme ; absence de nouvelle pièce prescrite. Coût public et solde net non établis.")])

# Supprimer le suivi/publication sectoriels imposés par la convention de retour à l'emploi.
p = paragraphs('L531-4-1')
old_reporting = plain(p[3])
new_reporting = "L'obligation de prévoir et de réaliser, sur le seul fondement du présent article, un suivi spécifique du dispositif, notamment un taux de bénéficiaires occupant un emploi six mois après la fin de la formation, et une publication du degré de réalisation des objectifs cesse à l'entrée en vigueur de la loi portant la présente rédaction, y compris pour les conventions en cours et les publications non encore effectuées. Les conventions, les actions de formation engagées, le maintien des prestations et les droits des bénéficiaires demeurent valables. Les évaluations volontaires et les contrôles légalement prévus sur un autre fondement restent possibles, sans nouveau rapport de remplacement."
put('L531-4-1',
    "Réforme de fond : suppression du suivi spécifique obligatoire, de l'indicateur d'emploi à six mois et de la publication obligatoirement prévue par la convention. Ce reporting sectoriel ne conditionne pas l'accès à la formation ou le maintien des prestations et sa fonction essentielle distincte n'est pas démontrée. La convention de coopération, la fenêtre de formation de deux ans débutant un an avant la fin des droits, l'information de fin de formation et la participation régionale sont conservées intégralement.",
    "Le renvoi L5312-1 du code du travail désigne l'institution d'emploi, non le CSS L531-2 ni le régime du préavis. L214-13 éducation reste une référence extérieure non intégralement fournie, sans nouveau renvoi. La période de deux ans est celle d'accès aux actions de formation ; elle ne constitue jamais le terme d'un emploi. L'information ponctuelle de fin de formation demeure nécessaire à la continuité de prestation, distincte du reporting supprimé. Transition couvrant aussi conventions en cours et publication pour des formations anciennes non encore effectuée, sans refaire les rapports déposés ni supprimer les contrôles autonomes. Aucun rendement de la suppression n'est chiffré.",
    "Une obligation réelle de suivi et de publication sectoriels est retirée, sans rapport ni indicateur obligatoire de remplacement ; les prestations et l'accès aux formations demeurent.",
    "Les suivis imposés par un fondement autonome et les évaluations librement convenues ne sont pas abolis. Ni les dépenses de formation ni leurs résultats d'emploi ne sont chiffrés à partir de cette coupe.",
    "Aucune charge nouvelle n'est identifiée : absence de rapport, registre, données ou déclaration de remplacement. Les transmissions ponctuelles déjà prévues pour la prestation restent inchangées ; le solde national n'est pas établi.",
    proposed='\n'.join(p[:3] + ['<p>' + new_reporting + '</p>']), classification='material_reduction',
    removed=["Obligation conventionnelle de suivi spécifique mesurant les objectifs du dispositif, avec indicateur du taux d'emploi six mois après la fin de la formation.",
             "Obligation de prévoir et d'effectuer la publication du degré de réalisation des objectifs de ce dispositif particulier de retour à l'emploi."],
    effects=[effect('obligation_removed', 'prepare-retour-emploi-fin-reporting-specifique',
        "Suppression du suivi et de la publication obligatoires de ce dispositif conventionnel.",
        "Toute convention devait prévoir des modalités de suivi, un taux d'emploi à six mois et la publication du degré de réalisation des objectifs.",
        "Aucun suivi spécifique, taux à six mois ou publication n'est exigible sur ce fondement ; convention et accès aux prestations conservés.",
        "Institution d'emploi, organismes de prestations familiales et régions parties aux conventions concernées.",
        "Dès l'entrée en vigueur, conventions en cours et publications non encore effectuées incluses ; droits et formations engagées conservés.",
        old_reporting, "sans nouveau rapport de remplacement.", unit='legal_duty')])

keep('L531-6',
    "Maintien intégral du complément de garde par une association, entreprise ou petite structure d'accueil. L'habilitation vise la sécurité de la garde d'enfants et n'est pas une autorisation économique dont le double emploi serait établi par le texte. Les quatre majorations, la dérogation d'âge et le maintien intégral jusqu'à la rentrée ainsi que l'accès des petites structures sous tarif maximal sont des avantages à conserver pour les opérations futures.",
    "D531-20 à D531-23 et D531-24 ont été lus intégralement : conserver barèmes, dépenses prouvées, plafond de 85 %, majorations 10 % et 30 %, plafonds de ressources et règle tarifaire de 10 euros des petites structures ; ces montants ne sont pas supprimés ou réinterprétés ici. Le 2° renvoie à l'AAH L821-1/L821-2, non au préavis ou à un an d'ancienneté ; le 4° vise l'allocation de l'enfant handicapé L541-1. D531-22 comporte une attestation annuelle sectorielle : la réduction décidée pour les états de protection complémentaire D912-14/15 ne l'abroge pas par homonymie ; son éventuel allègement doit être porté dans ce véritable règlement, non simulé ici. Note de 2022 à coordonner avec l'entrée en vigueur au 1er septembre 2025, sans transformer ce millésime historique en date de loi nouvelle.",
    "Les aides, quatre majorations et dérogations d'âge sont intégralement conservées. Aucun agrément doublonné ni prélèvement accessoire autonome n'est démontré dans cet article.",
    "La sécurité et les tarifs des structures gardent leur régime. Le maintien ne vaut pas réécriture des habilitations du code du travail ou de la santé publique ni validation de tous leurs règlements.",
    benefit="L'aide partielle au coût réel de garde demeure avec le plafond adapté aux ressources, au nombre d'enfants et à la situation de couple. Les quatre majorations sont conservées : horaires spécifiques, allocation aux adultes handicapés de la personne seule ou d'un membre du couple, parent isolé, et enfant à charge ouvrant droit à L541-1. La dérogation au-delà de l'âge ordinaire, le montant réduit dans ce champ et le maintien intégral pour les enfants atteignant l'âge entre le 1er janvier et le 31 août restent ouverts. L'accès dérogatoire par établissement d'accueil de jeunes enfants de capacité limitée sous tarification plafonnée demeure ; il n'est réservé ni aux anciennes structures ni aux anciens bénéficiaires. L'habilitation de garde protège les enfants et n'est pas supprimée ; aucune condition nouvelle d'emploi ou d'ancienneté n'est ajoutée.")

# CMG emploi direct : supprimer l'acte d'adhésion distinct, garder le canal et la déclaration.
p = paragraphs('L531-8')
old_enrolment = plain(p[0])
new_enrolment = "L'attribution du complément mentionné à l'article L. 531-5 emporte, sans démarche d'adhésion distincte de l'employeur, adhésion au dispositif simplifié prévu pour les personnes mentionnées au 4° de l'article L. 133-5-6. L'organisme débiteur des prestations familiales et l'organisme mentionné à l'article L. 133-5-10 mettent en œuvre cette adhésion à partir des informations nécessaires à l'attribution et aux déclarations prévues par l'article L. 133-5-8. Les déclarations nécessaires à l'identification du salarié et des rémunérations demeurent celles de l'article L. 133-5-8 ; aucune répétition de l'adhésion n'est exigée à leur occasion."
p[0] = '<p>' + new_enrolment + '</p>'
old_caisse = "la caisse mentionnée à l'avant-dernier alinéa du présent article dont relève l'allocataire"
new_caisse = "la caisse d'allocations familiales ou la caisse de mutualité sociale agricole dont relève l'allocataire"
p[4] = p[4].replace(old_caisse, new_caisse)
enrolment_transition = "La dispense de démarche d'adhésion distincte s'applique aux attributions du complément et aux adhésions restant à effectuer à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris pour les droits en cours. Les adhésions déjà effectuées restent valables sans renouvellement. Elle ne modifie ni les cotisations et contributions dues, ni les parts de complément et leurs imputations, ni les droits du salarié, les régularisations, les restitutions, les prescriptions et les recours relatifs aux périodes antérieures. La présente rédaction ne reporte pas l'abrogation du présent article déjà prévue au 1er septembre 2027."
put('L531-8',
    "Réforme de fond : l'attribution du complément vaut adhésion au dispositif simplifié ; l'acte d'adhésion distinct imposé au particulier employeur est retiré, sans créer un autre formulaire. Le canal unique, la déclaration mensuelle, le calcul net, le versement du reliquat, les échanges entre organismes et la restitution des indus restent intégralement. Coordination du renvoi ordinal à la caisse subrogée afin que l'ajout de la transition ne le rende pas orphelin.",
    "Les deuxième et troisième alinéas demeurent à leur place, ce qui préserve L531-8-1 et L133-5-12 II 1°. L133-5-6 4° désigne bien les particuliers employant une garde d'enfants ; L133-5-8 garde la déclaration mensuelle, la dispense papier et la substitution de bulletin émis par l'organisme. Les parts a et b renvoient au I de L531-5, y compris ses exclusions d'indemnités ; la déduction L241-10 I bis conserve 2 euros ou 3,70 euros selon le territoire, leurs conditions et non-cumuls. L553-2 conserve garanties de recouvrement et remises pour précarité, sous la dérogation spécifique au présent article. L'automatisation de l'adhésion transfère une opération à l'organisme : coût public net inconnu, classement mixed. La source a valid_until=2027-09-01 et ABROGE_DIFF ; cette proposition ne prolonge pas cette version ni ne prétend écrire sa remplaçante. Les notes relatives aux périodes de garde dès 2019 sont conservées dans leur champ.",
    "La démarche privée d'adhésion est fusionnée avec l'attribution de l'aide, mais la mise en œuvre automatique incombe au service : allègement pour l'employeur, charge de traitement public et solde net inconnus. Aucun taux de cotisations n'est réduit.",
    "L'utilisation du dispositif et la déclaration mensuelle restent nécessaires. La réforme de cette version s'arrête à son champ temporel légal, sans neutraliser une modification déjà programmée au 1er septembre 2027. Les coûts techniques ne sont pas estimés.",
    "Une obligation de traitement automatique de l'adhésion est ajoutée à l'organisme en remplacement de l'acte séparé de l'employeur ; elle est recensée et le classement est mixed. Aucun nouveau formulaire, donnée, compte imposé au-delà du dispositif existant ou délai n'est créé pour la famille. Le coût public et le solde de l'ensemble des codes demeurent inconnus.",
    proposed='\n'.join(p + ['<p>' + enrolment_transition + '</p>']), classification='mixed',
    removed=["Démarche distincte d'adhésion au dispositif simplifié imposée au particulier employeur bénéficiaire du complément de libre choix du mode de garde."],
    benefit="Les aides des deux parts a et b de L531-5 demeurent : cotisations nettes de la déduction I bis de L241-10 et de la part a, puis éventuelle imputation de la part b dans la limite du solde ; versement intégral du reliquat b à l'employeur. Les échanges entre CAF, MSA et organisme de recouvrement restent prévus pour liquider l'aide, sans demande répétée d'adhésion. La restitution de la part a pour le compte de l'employeur et le recouvrement préalable sur les sommes qui lui sont dues restent intacts, comme la subrogation signifiée et les garanties autonomes de L553-2. Les déductions, exonérations et exclusions d'indemnités restent applicables aux futures situations éligibles, y compris contrat unique et anciens contrats dans leur régime transitoire. Aucun salaire ou droit à prestation n'est retiré ; la version à échéance différée n'est pas artificiellement pérennisée.",
    effects=[effect('obligation_merged', 'cmg-adhesion-sans-demarche-distincte',
        "L'attribution du CMG vaut adhésion, sans acte privé séparé.",
        "Employeur bénéficiaire tenu d'adhérer distinctement au dispositif simplifié de garde d'enfants.",
        "Attribution de l'aide valant adhésion ; identification et rémunérations restent déclarées selon L133-5-8.",
        "Particuliers employeurs bénéficiaires du CMG emploi direct, droits en cours et nouveaux droits.",
        "Attributions et adhésions restant à faire dès l'entrée en vigueur ; adhésions existantes maintenues sans renouvellement ; fin de validité légale de cette version conservée.",
        old_enrolment, "L'attribution du complément mentionné à l'article L. 531-5 emporte, sans démarche d'adhésion distincte de l'employeur, adhésion au dispositif simplifié prévu pour les personnes mentionnées au 4° de l'article L. 133-5-6.",
        unit='legal_duty', burdens="Démarche privée supprimée, traitement automatique confié au service ; aucune déclaration d'adhésion substitutive, coût public net inconnu."),
        effect('obligation_added', 'cmg-adhesion-sans-demarche-distincte',
        "Traitement de l'adhésion par l'organisme à partir de l'attribution du complément, contrepartie de la même fusion.",
        "Adhésion accomplie par l'employeur en plus de son attribution de prestation.",
        "Organismes chargés de donner effet à l'adhésion emportée par l'attribution, sans acte distinct de l'employeur.",
        "Organismes de prestations familiales et de recouvrement du dispositif simplifié.",
        "Même champ et même bascule que la dispense privée ; aucun redépôt d'une adhésion existante.",
        old_enrolment, "L'organisme débiteur des prestations familiales et l'organisme mentionné à l'article L. 133-5-10 mettent en œuvre cette adhésion à partir des informations nécessaires à l'attribution et aux déclarations prévues par l'article L. 133-5-8.",
        unit='legal_duty', burdens="Nouveau traitement automatique de service, sans registre nouveau spécifié ; coûts de mise en œuvre et solde net non mesurés."),
        effect('coordination', 'cmg-adhesion-sans-demarche-distincte',
        "Désignation directe de la caisse subrogée afin de préserver le renvoi après ajout d'une transition.",
        "Caisse subrogée désignée par un renvoi à l'avant-dernier alinéa.",
        "CAF ou MSA de l'allocataire directement nommée, même subrogation et même signification.",
        "Allocataires et caisses intervenant dans les restitutions et indus du CMG.",
        "Coordination de référence uniquement, sans nouveau droit de recouvrement.", old_caisse, new_caisse, unit='regime')])

keep('L531-8-1',
    "Maintien intégral d'un avantage de trésorerie existant : le montant de CMG restant dû réduit le prélèvement du service de paiement intermédié, sans diminuer la rémunération effectivement versée au salarié. L'adhésion automatique proposée à L531-8 ne déplace pas son troisième alinéa ; aucune réécriture ni nouvelle baisse n'est donc nécessaire ici.",
    "L133-5-12 I troisième alinéa vise le prélèvement des sommes effectivement dues ; son II 1° tient compte expressément de L531-8 et L531-8-1. Accord écrit préalable du salarié, règles de salaire et de retenue fiscale subsistent. Le troisième alinéa de L531-8 conserve exactement le versement du reliquat de la part b après imputations ; le bénéfice ne peut être compté ou versé deux fois. L'échéance différée de la version de L531-8 au 1er septembre 2027 requiert sa coordination par le texte qui lui succédera ; le présent maintien ne ressuscite pas une version expirée.",
    "La minoration immédiate du prélèvement existe déjà et est préservée ; elle n'est pas présentée comme une nouvelle économie ni comme une diminution de cotisations.",
    "L'avantage ne concerne que le service intermédié et le complément restant dû. Les évolutions légales programmées de L531-8 doivent conserver leur propre articulation temporelle ; aucun double avantage n'est créé.")

keep('L531-9',
    "Maintien intégral des non-cumuls ciblés sur la cessation d'activité et du cumul favorable prévu au VI de L531-4. Ils coordonnent des prestations d'entretien et de garde de même enfant, sans créer de taxe, agrément ou démarche redondante. La réduction propre au complément de garde via une structure en cas de faible quotité reste dans ce champ précis ; elle n'est pas étendue à l'emploi direct ni aux autres enfants.",
    "Les indemnités L331-8-1 et L623-2 jointes ont été lues avec leurs notes : congé supplémentaire de naissance salarié et indemnités de naissance des indépendants sont distincts du préavis et de l'indemnité ordinaire de rupture. Le renvoi agricole L732-12-1-1 est extérieur au corpus des cinq codes, son contenu entier n'est pas fourni et aucune extension n'est inférée. La condition du même enfant concerne le non-cumul avec les indemnités de naissance. La note de la loi du 30 décembre 2025 vise les enfants nés/adoptés dès le 1er janvier 2026 et ceux dont la naissance était présumée à compter de cette date ; cette transition demeure, sans nouvelle date de promulgation. La proposition L331-8-1 supprime sa dégressivité, mais ne change pas l'objet de l'indemnité ni le présent non-cumul.",
    "Les coordinations de prestations sont conservées intégralement avec l'exception VI et leur champ du même enfant. Aucune nouvelle formalité ou baisse de prélèvement n'est démontrée.",
    "Le maintien ne supprime pas les prestations de naissance, ne transforme pas leur durée en terme d'emploi et ne réécrit pas le régime agricole extérieur. Aucun chiffrage national ne peut en être déduit.")

# Les seules cibles obligatoires sont reprises depuis requirements, sans ajout.
CHECKS = {
    'L521-2': {
        'L1234-1': "L521-2 règle l'allocataire, la résidence alternée et les placements ; il ne renvoie pas au préavis de licenciement. Les quinze jours calendaires proposés pour les nouveaux contrats privés, leur notification et les durées anciennes n'affectent ni le partage par moitié ni la décision du juge de maintenir l'allocation à la famille.",
        'L1221-2': "Aucun contrat de garde ou d'emploi n'est une condition de L521-2. Le contrat unique futur et la survie des anciens contrats, y compris CDD, ne changent pas la charge effective de l'enfant, l'ouverture du droit du chef d'un parent ou les exceptions de placement ; aucun CDD spécial n'est créé.",
        'L1234-9': "L'allocataire n'est soumis à aucun seuil d'ancienneté d'emploi par cet article. L'indemnité patronale du contrat unique, nulle avant un an puis de 0,20 mois par année totale avec prorata des mois complets et plafond légal de six mois, ne définit ni la charge ni le versement à l'ASE ; ses transitions restent distinctes.",
        'L323-1': "La cible fournie est le CSS L323-1, qui règle le délai et les durées d'indemnités journalières de maladie. Le corps L521-2 renvoie expressément au L323-1 du code de la justice pénale des mineurs pour une mesure de placement : homonymie, non renvoi à corriger vers la maladie. Cette cible est inapplicable, sans effacer le renvoi pénal des mineurs."},
    'L531-1': {
        'L1234-1': "L531-1 énumère les quatre composantes de la PAJE et ses dispenses de ressources ; aucun préavis de travail n'y est visé. Le préavis futur de quinze jours, la notification et les durées conservées pour anciens contrats n'ajoutent aucune condition aux droits de prime, de base, de PreParE ou de garde.",
        'L1221-2': "Le contrat unique remplace les nouveaux contrats privés à terme, mais L531-1 ne fait dépendre aucune de ses quatre prestations d'un CDD. Les futures situations éligibles et les anciens contrats gardent leurs droits dans les règles propres à chaque composante ; une durée de formation n'est pas une durée d'emploi.",
        'L1234-9': "L531-1 ne définit ni indemnité de rupture ni salaire de garde pris en compte. Le seuil d'un an au terme effectif, préavis inclus, et le calcul de 0,20 mois sur toute l'ancienneté, prorata de mois complets et plafond six mois n'entrent pas dans l'ouverture de la PAJE ; les exclusions éventuelles sont au L531-5.",
        'L531-9': "Le dernier alinéa de L531-1 autorise un cumul de principe entre PreParE et CMG, sous les règles spéciales. L531-9 maintient le non-cumul au taux plein sauf VI de L531-4, le non-cumul avec l'indemnité supplémentaire de naissance du même enfant et la réduction propre à L531-6 au temps partiel ; aucun cumul général inconditionnel n'est affirmé.",
        'L531-5': "La cible ouvre le CMG à l'emploi d'un assistant maternel agréé ou d'une garde à domicile, avec parts a et b, exceptions à l'activité et dérogations d'âge. Son III 6° exclut déjà les indemnités de préavis, de rupture et de congés ; la proposition étend explicitement cette continuité au contrat unique et protège les anciens CDD, sans créer une prime de fin de CDD future."},
    'L531-4-1': {
        'L1234-1': "La période de deux ans d'accès aux formations, qui débute un an avant la fin de PreParE, n'est pas un préavis. La suppression du suivi/publication n'affecte ni les quinze jours calendaires et leur notification pour le nouveau contrat ni les préavis conservés des anciens contrats, ni les protections et procédures collectives distinctes.",
        'L1221-2': "La convention organise des actions de formation limitées dans le temps sans fixer le terme d'un emploi. Tout emploi privé futur demeure à durée indéterminée selon la proposition L1221-2 ; les anciens contrats et leurs droits restent protégés et le retrait du reporting n'autorise aucun nouveau CDD de formation.",
        'L1234-9': "L'accès à la formation et le maintien de la prestation jusqu'à épuisement des droits ne dépendent pas d'une ancienneté d'un an. L'indemnité ordinaire due par l'employeur à partir du seuil effectif, calculée à 0,20 mois par année totale avec plafond six mois, reste étrangère au suivi conventionnel supprimé et aux droits des anciens contrats."},
    'L531-6': {
        'L1234-1': "Les horaires spécifiques justifient une majoration de CMG ; ils ne désignent aucun préavis de licenciement. La durée future de quinze jours calendaires et ses conditions de notification, comme les préavis des anciens contrats, ne modifient ni habilitation de garde ni plafond ou dérogation d'âge de cette prestation.",
        'L1221-2': "Le recours à une association, une entreprise ou un établissement d'accueil ne crée pas un contrat de travail à terme pour le parent ou le personnel. Les aides et quatre majorations restent ouvertes dans les futures situations éligibles sous contrat unique ; les anciens contrats sont distincts et aucun terme de garde ne met automatiquement fin à l'emploi.",
        'L1234-9': "L531-6 couvre le coût de la garde fournie par une structure et ne renvoie pas aux indemnités patronales de rupture. Le seuil d'un an avec préavis inclus, le taux de 0,20 mois sur toute l'ancienneté et le plafond six mois ne peuvent être ajoutés comme conditions de cette aide ou de ses majorations ; aucun droit spécial n'est supprimé.",
        'L821-1': "Le 2° de L531-6 majore le plafond lorsqu'une personne seule ou un membre du couple bénéficie de l'AAH L821-1 ou L821-2. La cible fournie porte incapacité, séjour, subsidiarité et compléments d'AAH, avec sa transition du 23 juillet 2026 ; elle ne fixe aucune ancienneté privée. Le bénéfice de la majoration reste ouvert aux futurs titulaires d'AAH."},
    'L531-8': {
        'L1234-1': "L'adhésion simplifiée et le prélèvement des cotisations ne déterminent pas le préavis de la personne gardant l'enfant. La déclaration et le calcul conservent les droits salariaux réellement dus, y compris un préavis de quinze jours pour les nouveaux contrats dans son champ et les règles anciennes ; aucune procédure collective n'est réputée supprimée.",
        'L1221-2': "L'adhésion désormais emportée par l'attribution du CMG fonctionne pour les emplois nouveaux à durée indéterminée comme pour les anciens contrats valables. Aucune adhésion nouvelle ni fin de période de garde n'autorise un CDD privé ou une fin automatique d'emploi ; les droits et créances des anciens contrats restent réservés.",
        'L1234-9': "Le calcul net et la part b renvoient à L531-5, dont les plafonds excluent les indemnités de rupture. L'absence d'indemnité ordinaire avant un an n'efface ni salaire, congés, préavis ni réparation illégale ; à partir du seuil au terme effectif, le 0,20 mois porte sur toute l'ancienneté, en mois complets proratisés et plafond six mois, sans modifier l'adhésion.",
        'L133-5-8': "Le deuxième alinéa impose la déclaration mensuelle des rémunérations, dont dépend le versement du reliquat de CMG au troisième alinéa de L531-8 : ce renvoi demeure exact et au même rang. La proposition retire seulement l'acte d'adhésion distinct pour les bénéficiaires du CMG ; déclaration, identification, exception papier et bulletin émis par l'organisme restent, sans nouvelle condition de ressources.",
        'L133-5-6': "Le 4° de la cible vise précisément les particuliers employant des salariés de garde d'enfants. L531-8 est la règle spéciale d'adhésion de ces bénéficiaires, désormais automatique avec l'attribution ; elle ne rend pas obligatoires les options des huit autres catégories et ne soumet aucun ancien contrat à une nouvelle autorisation.",
        'L553-2': "Le cinquième alinéa déroge au recouvrement général pour restituer la part a lors d'une correction de cotisations et recouvrer d'abord sur les sommes dues par l'organisme à l'allocataire. Principal, subrogation signifiée et garanties autonomes de L553-2, dont remise pour précarité hors fraude, demeurent ; la caisse est nommée directement pour éviter un renvoi ordinal déplacé.",
        'L241-10': "Seul le I bis est visé au deuxième alinéa : déduction patronale de 2 euros par heure, ou 3,70 euros outre-mer et collectivités indiquées, avec non-cumuls propres, avant les parts CMG. Les exonérations I, II et III ne sont pas importées indistinctement ; le III proposé conserve notamment contrats uniques futurs, anciens CDD et agents publics dans leurs champs. Aucun seuil d'un an ne restreint cette déduction.",
        'L531-5': "Les renvois aux a et b du I restent exacts : prise en charge de cotisations puis aide de rémunération, imputées seulement à concurrence des cotisations restantes avant versement du reliquat. Le III 6° exclut les indemnités prévues, et sa proposition protège celles du contrat unique et des anciens CDD ; ni les deux parts ni les dérogations d'activité, d'âge ou de résidence alternée ne sont supprimées par l'adhésion automatique."},
    'L531-8-1': {
        'L1234-1': "La minoration du prélèvement intermédié est un mode de mobilisation du CMG, sans modification du salaire ni de l'indemnité de préavis. Les quinze jours calendaires et leur notification pour contrats nouveaux, comme les préavis et droits anciens conservés, restent au droit du travail ; ils ne deviennent pas une franchise appliquée au CMG.",
        'L1221-2': "Le service de versement de rémunérations reste accessible dans les mêmes conditions aux futurs contrats privés à durée indéterminée et aux anciens contrats valables. L531-8-1 n'introduit ni terme à l'emploi ni nouvelle possibilité de CDD ; la période de garde et l'opération de prélèvement ne sont pas une durée contractuelle.",
        'L1234-9': "L'aide s'impute sur le prélèvement sans diminuer les sommes effectivement versées au salarié. Le seuil d'un an préavis inclus et le 0,20 mois par année totale avec fractions de mois complets et plafond légal six mois n'ont aucun effet sur ce mécanisme ; salaires, congés, indemnités spéciales et anciens droits ne sont pas retirés par l'absence d'indemnité ordinaire de première année.",
        'L133-5-12': "Le renvoi au troisième alinéa du I désigne bien le prélèvement sur compte de l'employeur des sommes effectivement dues ; le II 1° vise réciproquement L531-8 et L531-8-1. L'accord écrit préalable du salarié, le paiement de toute sa rémunération et le PAS demeurent. La minoration utilise seulement le reliquat de CMG, sans double versement ni nouvelle condition de notification de rupture."},
    'L531-9': {
        'L1234-1': "Le non-cumul vise des prestations pendant la cessation d'activité pour l'enfant, et non le préavis d'une rupture. Les quinze jours calendaires proposés pour les nouveaux contrats et leur notification ne réduisent ni la durée du congé ni les indemnités de naissance ; les règles antérieures et procédures spéciales restent à leur champ.",
        'L1221-2': "Une période de congé ou de prestation n'est pas la durée de l'emploi. L531-9 ne permet aucun nouveau CDD privé ; contrats uniques futurs et anciens contrats valables restent soumis aux mêmes non-cumuls sociaux lorsqu'ils relèvent de leur population, sans fermer les exceptions favorables du VI de L531-4.",
        'L1234-9': "L'indemnité journalière de naissance citée n'est pas l'indemnité ordinaire patronale de rupture. Aucune ancienneté d'un an, aucun 0,20 mois par année ni plafond six mois n'est ajouté au non-cumul ; salaires, congés, réparations illicites, indemnités spéciales et transition des anciens contrats sont distincts.",
        'L331-8-1': "La cible est l'indemnité journalière salariée du congé supplémentaire de naissance, sous cessation du travail et conditions L313-1 I et II. La proposition maintient le montant du premier mois au second, sans changer l'objet ni la population. Le non-cumul avec le CMG pour le même enfant demeure exact, ainsi que la cohorte de naissance/adoption dès 2026 et naissance présumée.",
        'L623-2': "La cible ouvre sur demande des indemnités supplémentaires de naissance aux indépendants qui cessent ou ne reprennent pas leur activité, pour la durée liée à L331-8-1. Il ne s'agit ni d'un contrat privé ni d'une indemnité de licenciement : le renvoi pour le même enfant et la transition des enfants nés/adoptés dès 2026 restent inchangés, sans imposer un préavis salarié aux indépendants."}
}

ANSWER['L522-2']['review_notes'] += " La transition est intégrée au dernier alinéa existant : le renvoi de R522-3 à ce dernier alinéa continue de viser le complément différentiel."
ANSWER['L531-2']['review_notes'] += " La transition complète le dernier alinéa sans en créer un autre : R531-1 continue d'y trouver les montants du plafond et de la majoration."
ANSWER['L531-4']['review_notes'] += " Le VII ajouté porte seulement la transition ; le VI garde ses quatre alinéas, de sorte que son renvoi à l'avant-dernier alinéa continue de viser la prolongation partagée du montant majoré."

# Réserve de protection déjà existante, rendue explicite pour éviter un conflit
# entre la suppression générale des justificatifs migratoires et l'adoption.
ANSWER['L512-2']['reason'] += " La réserve expresse de L512-4 conserve la validité des adoptions et accueils ainsi que l'autorisation d'entrée à ce titre ; elle ne crée pas de nouveau contrôle pour les autres enfants."
ANSWER['L512-2']['review_notes'] += " Le renvoi nouveau à L512-4 vise un article assigné dans ce même lot, lu en entier, et non une cible supplémentaire à ajouter à reference_checks. Sa réserve protège notamment l'autorisation d'entrée liée à une adoption étrangère et l'agrément de protection de l'enfant. L'absence de condition migratoire supplémentaire ne les abroge pas implicitement."
ANSWER['L512-2']['substantive_impact']['scope_limitations'] += " Les conditions spéciales d'adoption ou d'accueil de L512-4, notamment l'autorisation d'entrée à ce titre, sont expressément réservées."
for ef in ANSWER['L512-2']['substantive_impact']['effects']:
    ef['conditions_and_transition'] += " Les conditions propres à l'adoption ou à l'accueil en vue d'adoption de L512-4 demeurent applicables."
    ef['replacement_or_new_burdens'] += " L'adoption garde ses garanties antérieures L512-4 ; cette réserve n'ajoute aucune condition nouvelle."

for number, obj in ANSWER.items():
    src = BY_NUMBER[number]
    key = src['code_id'] + '|' + src['source_id']
    for target_key in REFS['requirements'][key]:
        target = REFS['targets'][target_key]
        obj['reference_checks'].append(dict(
            target_key=target_key, view_sha256=target['view_sha256'],
            assessment=CHECKS[number][target['number']]))

ordered = [ANSWER[src['number']] for src in SOURCES]
(ROOT / 'answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(ordered)} articles')
