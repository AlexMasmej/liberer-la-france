import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
references = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens, source_quote=source_quote,
                proposed_quote=proposed_quote)


answers = {}


def retained(number, reason, notes, assessment, limitations, burdens, benefit=None):
    src = by_number[number]
    out = {k: src[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    out.update(proposed_xml=None, reason=reason, review_notes=notes,
               status='retained_unchanged', classification='retained_necessary',
               substantive_impact=impact('retained_necessary', assessment, limitations, burdens))
    if benefit:
        out['benefit_review'] = benefit
    answers[number] = out


retained('L532-1',
    "Maintien intégral après examen : cette règle empêche le cumul de deux prestations d'entretien familial, sans créer de prélèvement, de dossier ou d'autorisation. Le complément familial et l'allocation de base gardent chacun leur fondement et leurs bénéficiaires futurs ; supprimer ici le seul non-cumul créerait une dépense de cumul, et non une réduction démontrée de formalités. Aucune réécriture stylistique n'est proposée.",
    "L522-1 et L531-3 ont été lus dans le corpus public : le premier définit le complément familial ; le second conserve les taux plein et partiel de l'allocation de base et ses règles propres. L522-1 exige en principe des enfants au-delà de l'âge de la PAJE, mais les situations particulières, notamment d'adoption, ne permettent pas de tenir le non-cumul pour un doublon sans objet. Le renvoi n'est ni un quota SRU ni une restriction au contrat unique.",
    "La source entière est maintenue : aucun cumul supplémentaire, aucune prestation supprimée et aucune baisse de prélèvement ne sont revendiqués.",
    "Les montants et les modalités de choix relèvent des textes propres aux deux prestations ; le coût d'un cumul éventuel n'est pas établi.",
    "Aucune charge nouvelle n'est identifiée : la règle de non-cumul est conservée sans déclaration, justificatif ou délai supplémentaire.")

retained('L532-2',
    "Maintien intégral des cinq subdivisions : les exclusions de cumul organisent l'articulation entre la PreParE, les autres revenus de remplacement et le complément familial. Les exceptions favorables des III, IV et V et la reprise des droits au chômage sont conservées pour les futures situations éligibles. La source n'impose pas un agrément ou une déclaration autonome à supprimer ; retirer indistinctement ces règles fermerait aussi des droits de cumul.",
    "Conserver exactement les listes des 1° à 5° du II, les cumuls en cours de droit du III, le mois d'ouverture du IV et le mois de fin d'indemnisation du V. L531-4 a été lu : le deuxième alinéa de son VI vise bien l'option majorée à taux plein, distincte de la reprise d'activité du premier alinéa. Les notes de la loi 2025-1403 préservent le champ des enfants nés ou adoptés dès le 1er janvier 2026 et des naissances prévues à compter de cette date ; il ne s'agit pas de la date de la réforme proposée. Les régimes agricoles, maritimes et publics ne deviennent pas des contrats privés.",
    "Les interdictions et exceptions de cumul, la conservation du reliquat de chômage et les cinq subdivisions sont laissées intactes ; aucun allègement nouveau n'est compté.",
    "Aucun changement des prestations maternité, paternité, maladie, vieillesse ou des régimes agricoles et maritimes n'est opéré par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : aucun contrôle, formulaire ou minimum d'activité ne s'ajoute à l'articulation existante des prestations.")

retained('L541-1',
    "Maintien intégral du fondement de l'AEEH, de son complément et de la voie d'accès pour une incapacité inférieure au taux principal. Les dépenses et l'aide humaine sont les critères du complément, non des taxes ou formalités autonomes. L'exclusion de l'internat entièrement financé conserve son exception favorable pour les congés ou suspensions de prise en charge. Les supprimer ensemble réduirait la protection des familles ; aucun doublon d'autorisation n'est démontré dans cet article.",
    "Préserver les quatre alinéas et les renvois au CASF L312-1 I 2° et 12°, à L146-9 et au code de l'éducation L351-1. R541-1 à R541-4 ont été lus : les seuils réglementaires sont 80 % et 50 %, avec six catégories de complément ; ils ne sont pas remplacés par un taux inventé. R541-4 maintient notamment des attributions sans terme fixe dans son champ et les avances liées au réexamen du complément. La réduction distincte proposée dans L541-2 ne supprime ni ces conditions matérielles ni la compétence d'appréciation du handicap. L351-1 du CSS, cible contextuelle sur la retraite, ne doit pas être confondu avec L351-1 du code de l'éducation effectivement cité.",
    "Le droit à l'AEEH et au complément, l'accès dérogatoire et les périodes indemnisables hors internat sont intégralement conservés ; aucun taux ou montant n'est réduit.",
    "Les réexamens et justificatifs des articles réglementaires, lus pour le contexte, ne sont pas réécrits dans ce maintien ; aucun gain de formalités ne leur est imputé.",
    "Aucune charge nouvelle n'est identifiée : les conditions légales d'incapacité, d'accompagnement et de dépenses sont reproduites depuis la source sans ajout.")

retained('L541-3',
    "Maintien intégral du renvoi d'attribution à L521-2 : il permet de déterminer le destinataire de l'AEEH à partir de la charge effective de l'enfant et de protéger les situations familiales particulières. Il n'institue ni prélèvement ni agrément supplémentaire. Recréer ces règles ici doublerait leur rédaction sans retirer une obligation.",
    "L521-2 a été lu en entier, notes comprises : charge effective et permanente, résidence alternée, ouverture du chef des parents et enfant confié à l'ASE avec faculté de maintien judiciaire à la famille. Le renvoi reste à son champ d'application ; il n'est pas transformé en répartition nouvelle de l'AEEH ni en suppression de l'exception judiciaire. Ne pas confondre la présente prestation avec les seuls calculs d'allocations familiales visés par certaines phrases de la cible.",
    "Le rattachement aux règles existantes de bénéficiaire est maintenu, sans fusion de prestations ni nouvelle réduction matérielle.",
    "L'application aux configurations de résidence et de placement reste celle du droit existant ; aucune nouvelle méthode de partage n'est décidée.",
    "Aucune charge nouvelle n'est identifiée : le renvoi réemploie la règle existante et n'impose aucun second dossier de désignation d'allocataire.")

retained('L541-4',
    "Maintien intégral de la majoration spécifique pour le parent isolé assumant seul un enfant handicapé nécessitant une tierce personne. Les deux voies, AEEH avec complément ou AEEH avec prestation de compensation, demeurent ouvertes aux situations futures. Le texte crée un avantage social utile, sans taxe ni autorisation distincte dont la suppression serait justifiée.",
    "Conserver le renvoi à L541-1 et celui à L245-1 du CASF : le second vise la prestation de compensation, et non un financement retraite. Le décret règle les modalités de versement ; la présente disposition n'ajoute pas d'attestation périodique d'isolement. La réforme de L541-2 ne retire pas la majoration lorsque ses conditions propres restent remplies.",
    "La majoration de parent isolé et ses deux combinaisons favorables sont conservées ; aucun avantage n'est réservé au seul stock des anciens bénéficiaires.",
    "Le montant réglementaire et le contrôle des conditions d'isolement ne sont ni modifiés ni chiffrés dans cet article.",
    "Aucune charge nouvelle n'est identifiée : aucune condition, pièce ou procédure ne s'ajoute aux éléments existants de l'avantage.")

retained('L541-5',
    "Maintien intégral de la répartition des responsabilités : les organismes débiteurs versent et contrôlent l'AEEH pour le compte de la CNSA, qui les rembourse. Retirer cette règle de financement ne réduirait aucune cotisation et pourrait priver la prestation de son circuit de paiement. Aucun rapport ou double dossier n'est imposé à la famille par cet article.",
    "Le 1er janvier 2021 figurant en note est la date historique d'entrée en vigueur de cette organisation, non celle d'une nouvelle réforme. Le contrôle conservé porte sur les conditions de la prestation : il ne doit pas rétablir le motif de sanction retiré par la proposition de L541-2. Le remboursement CNSA/organismes reste un flux interne, sans recette de compensation inventée.",
    "Le paiement, le contrôle et le remboursement entre organismes sont conservés ; aucun transfert nouveau de financement ni économie nationale n'est affirmé.",
    "Les coûts de gestion et les autres compétences des organismes ne sont pas évalués ; ce maintien n'approuve pas leurs éventuels doublons réglementaires.",
    "Aucune charge nouvelle n'est identifiée : le circuit existant est maintenu sans nouvel état financier ni information supplémentaire des familles.")

retained('L542-9',
    "Maintien intégral de deux facultés favorables de prêt : amélioration de l'habitat des allocataires et amélioration des lieux d'accueil des assistants maternels, à domicile ou en maison d'assistants maternels. Le texte n'impose ni emprunt ni procédure autonome d'agrément. Son abrogation fermerait une aide aux opérations futures, en contradiction avec la conservation des avantages.",
    "Préserver les 1° et 2° et les deux renvois au CASF L421-1 et L424-1. Les conditions et limites des prêts sont réglementaires ; la qualification professionnelle d'assistant maternel ne doit pas être assimilée ici à un agrément financier supplémentaire. Aucun quota SRU, permis ou nouvelle recette ne résulte de ces prêts.",
    "Les deux possibilités de prêt restent ouvertes, y compris pour les futurs travaux recevables ; aucune dette de prêt existante n'est effacée.",
    "Les taux, plafonds et pièces réglementaires ne figurent pas dans cet article et ne sont pas réputés simplifiés par son maintien.",
    "Aucune charge nouvelle n'est identifiée : les prêts restent facultatifs, sans nouvelle demande de garantie ou déclaration instituée ici.")

retained('L543-1',
    "Maintien intégral de l'allocation de rentrée scolaire, de ses deux voies d'accès et de l'indexation du plafond. L'apprentissage reste une situation pédagogique éligible et non un contrat d'emploi que cet article limiterait dans le temps. Le plafond de ressources et le plafond de rémunération ciblent la prestation ; aucun prélèvement ou dossier redondant n'est créé par les quatre alinéas.",
    "L512-3 a été lu : son 2° vise le plafond de rémunération des enfants après l'obligation scolaire ; ce renvoi reste pertinent pour les études et l'apprentissage. Conserver la modulation selon l'âge et l'indexation hors tabac, avec décret en Conseil d'Etat puis arrêté conjoint sécurité sociale/budget/agriculture. Aucun nouveau CDD d'apprentissage n'est autorisé ; la phase de formation future en contrat unique conserve l'accès à l'aide selon les mêmes âges et ressources.",
    "La prestation, l'apprentissage éligible, les plafonds et leur indexation sont intégralement maintenus ; aucune réduction de taux ou formalité n'est comptée.",
    "Les âges et montants réglementaires ne sont pas fixés à nouveau ; le changement de durée du contrat de travail n'abolit pas les limites d'âge de l'aide.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation de type de contrat ou durée minimale d'emploi n'est ajoutée à l'éligibilité.")

retained('L543-2',
    "Maintien intégral de l'allocation différentielle : elle évite la perte intégrale de l'allocation de rentrée scolaire lors d'un dépassement limité du plafond. Supprimer cette disposition favorable augmenterait l'effet de seuil. Elle ne comporte ni prélèvement ni circuit d'autorisation redondant.",
    "L543-1 est maintenu intégralement dans ce lot et dans la vue officielle fournie ; le renvoi à son plafond reste opérant. Le décret en Conseil d'Etat définit le dépassement et le calcul ; aucun montant ou seuil nouveau n'est introduit. Les élèves et apprentis futurs conservent cette voie d'accès dans le champ de L543-1.",
    "La prestation différentielle et son mécanisme de dépassement limité sont conservés sans prétendre créer un lissage supplémentaire.",
    "La formule réglementaire n'est pas réécrite et son coût n'est pas chiffré ; ce maintien ne concerne pas le barème de l'impôt sur le revenu.",
    "Aucune charge nouvelle n'est identifiée : le maintien de ce droit ne crée ni formulaire, ni condition d'emploi, ni délai nouveau.")

retained('L543-3',
    "Maintien intégral : la consignation de l'allocation protège un pécule appartenant à l'enfant placé, la dérogation laisse le versement à la famille qui le garde effectivement, et le calcul des ressources continue d'inclure tous les enfants. La gestion par la Caisse des dépôts et la restitution des seuls indus ont une fonction patrimoniale précise ; les supprimer ne constituerait pas une baisse de taxe.",
    "Conserver les quatre alinéas, les 3° et 5° de 375-3 et 375-5 du code civil, la majorité ou l'émancipation comme échéance du pécule et le destinataire familial de la dérogation. L543-1 et L543-2 sont maintenus dans le lot. Les textes civils extérieurs au corpus n'ont pas été réécrits ; aucune décision de placement n'est réputée disparaître du fait du contrat unique.",
    "Le pécule de l'enfant, la dérogation familiale, le calcul favorable des charges et la restitution des indus sont intégralement préservés.",
    "Le rendement et le coût de la gestion du pécule ne sont pas évalués ; aucune réforme générale du placement ou des décisions judiciaires n'est faite.",
    "Aucune charge nouvelle n'est identifiée : le circuit existant protège l'enfant sans nouveau registre ni justification annuelle ajoutée par cet article.",
    "Les avantages examinés sont le pécule acquis à l'enfant et versé à sa majorité ou émancipation, le versement direct à la famille lorsque l'enfant y reste effectivement à charge, ainsi que la prise en compte des enfants placés dans le calcul des ressources. Ils restent tous applicables aux placements et droits futurs éligibles, avec l'allocation différentielle ; la restitution ne vise que les sommes indûment versées à la Caisse des dépôts.")

retained('L544-1',
    "Maintien intégral du droit à l'allocation journalière de présence parentale pour l'enfant gravement malade, handicapé ou accidenté. Le renvoi au congé de présence parentale n'introduit ni CDD ni ancienneté minimale de rupture. L'extension expresse aux agents publics doit demeurer ; aucune autorisation distincte ou prélèvement accessoire n'est institué dans cet article.",
    "L1225-62 du travail a été lu en entier, source et proposition : certificat, 310 jours ouvrés de congé, temps partiel/fractionnement avec accord patronal, renouvellement exceptionnel et réouvertures sont à leur champ propre. Sa durée de congé n'est pas la durée de l'emploi ; l'accord sur la modalité de congé n'est pas un avis médical préalable au paiement. L544-2 et L544-3 sont réduits dans ce lot sans fermer ce droit. Écart préexistant lu : L1225-63 exige dix jours d'information initiale, R1225-14 mentionne encore quinze jours ; leur coordination hors lot reste nécessaire. La borne de version 2027-12-12 de la source ne devient pas une extinction normative de la prestation.",
    "Le droit de base à l'AJPP et son application aux agents publics restent entiers ; les coupes médicales sont portées par L544-2 et L544-3 et ne sont pas recomptées ici.",
    "Ce maintien ne réduit ni le délai d'information de l'employeur ni les limites de congé ; la mise en cohérence du règlement du travail reste hors lot.",
    "Aucune charge nouvelle n'est identifiée : aucun préavis de rupture, seuil d'ancienneté ou condition de contrat unique n'est ajouté à la prestation.",
    "L'avantage est l'indemnisation journalière de la présence auprès de l'enfant dans les trois situations de gravité, pour les salariés et expressément pour les agents publics. Les congés futurs recevables restent indemnisables ; la réforme des avis médicaux dans L544-2 et L544-3 ne réserve pas le droit aux anciens contrats et n'abolit aucune protection statutaire publique.")

retained('L544-4',
    "Maintien intégral du plafond mensuel commun d'allocations pour un même enfant : il règle l'utilisation des jours par l'un ou les deux parents et ne limite pas la durée du contrat de travail. Il n'impose aucune autorisation ni pièce périodique. Sa suppression modifierait l'intensité financière de la prestation plutôt que retirer un doublon administratif démontré.",
    "D544-4 a été lu : le plafond réglementaire est de 22 allocations par mois civil, commun aux deux membres du couple. Ne pas le confondre avec les 310 allocations de L544-3 ou les jours ouvrés de congé de L1225-62. La note de 2005 conserve le régime antérieur pour les bénéficiaires de l'ancienne allocation jusqu'à son terme et fixe le 1er mai 2006 pour les nouvelles demandes ; ces dates historiques ne sont pas une nouvelle bascule.",
    "La règle mensuelle commune est conservée sans diminution du plafond ni prétendue suppression d'une déclaration.",
    "Aucune évaluation du coût d'une augmentation du plafond mensuel n'est fournie ; les droits des deux parents restent ceux du texte officiel.",
    "Aucune charge nouvelle n'est identifiée : aucun relevé mensuel supplémentaire ou nouveau mode de décompte n'est institué ici.")

retained('L544-6',
    "Maintien intégral du montant fixé par décret, de sa revalorisation annuelle au 1er janvier sur le SMIC net et des adaptations au fractionnement ou au temps partiel. Ces dispositions protègent la valeur et les modalités de l'allocation, sans constituer une taxe sur les salaires. L'accord requis pour une modalité de congé conserve son champ distinct de l'avis médical préalable supprimé ailleurs.",
    "D544-6 a été lu en entier : formule A = (7 * shn)/(1-a), arrondi au centième, demi-journée égale à la moitié et exceptions des demandeurs d'emploi. Aucun nouveau montant ni taux social n'est déduit de cette formule. Le renvoi à L3231-2 concerne le SMIC ; celui à L1225-62, lu, concerne le fractionnement/temps partiel. Les agents publics restent régis par leurs propres règles. Ni les quarante heures ni les quinze jours de rupture ne remplacent ces références.",
    "L'indexation au SMIC net et les modalités de paiement à temps partiel restent inchangées ; aucun taux de cotisation n'est abaissé dans cet article.",
    "L'évolution future du montant dépend du SMIC et des prélèvements applicables à sa référence ; aucun gain forfaitaire ou économie publique n'est calculé.",
    "Aucune charge nouvelle n'est identifiée : le règlement existant de calcul est conservé sans nouvelle déclaration de salaire ou de temps de travail.")

retained('L544-7',
    "Maintien intégral du complément forfaitaire pour frais, avec son plafond de ressources variable selon les enfants et ses majorations pour la double activité ou le parent seul. Le seuil de dépenses cible une aide distincte du remplacement de revenu. Supprimer cet avantage, ses majorations ou son accès futur irait à l'encontre de la préservation demandée.",
    "Le premier alinéa de L544-1 désigne la maladie, le handicap ou l'accident grave : le renvoi demeure intact. La note historique du 1er mai 2006 préserve aussi le régime des anciennes allocations jusqu'à leur terme. Aucun seuil de dépenses ou de ressources nouveau n'est inventé ; le complément conserve sa périodicité mensuelle et son caractère forfaitaire, sans justificatif périodique ajouté par le présent maintien.",
    "Le complément mensuel et ses plafonds majorés sont maintenus pour les familles présentes et futures éligibles ; aucune réduction matérielle nouvelle n'est déclarée.",
    "Les montants et justificatifs réglementaires ne sont pas modifiés ; aucune condition d'ancienneté dans l'emploi ne s'en déduit.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation de dépenses ou d'activité additionnelle ne remplace les conditions existantes.")

retained('L544-8',
    "Maintien intégral de l'ouverture de l'AJPP aux professions et situations expressément énumérées, du versement mensuel pour les demandeurs d'emploi ou la formation rémunérée et de la reprise du reliquat d'indemnisation chômage. Les suspendre ou les fondre dans le seul salariat privé fermerait des avantages. L'article ne crée aucune nouvelle déclaration ou autorisation à retirer.",
    "Les cibles du travail L7221-1, L7311-3 et L5421-1 ont été lues en entier : elles visent respectivement particuliers employeurs, VRP et revenu de remplacement des personnes aptes recherchant un emploi. Les indépendants, conjoints et non-salariés agricoles gardent leurs renvois propres L611-1, L661-1, L321-5 et L722-9. L'observation grammaticale « celle mentionnées » ne justifie pas un nouveau corps à droit constant. La note d'entrée en vigueur au 1er janvier 2026 reste historique ; aucune durée de formation ne devient le terme de l'emploi.",
    "Toutes les catégories légales, le paiement mensuel spécifique et la reprise du chômage jusqu'à son terme sont conservés, sans faux transfert vers le contrat unique.",
    "Les modalités réglementaires des cessations d'activité et les statuts agricoles restent distincts ; aucune réforme de leur financement n'est réalisée.",
    "Aucune charge nouvelle n'est identifiée : aucune notification de rupture ou condition d'ancienneté n'est ajoutée au bénéfice des catégories énumérées.")

retained('L544-9',
    "Maintien intégral des neuf cas de non-cumul et de l'exception pour maladie ou accident du travail pendant l'activité à temps partiel. Ces règles articulent des revenus de remplacement, l'aide humaine et les autres allocations ; elles ne sont pas des prélèvements à supprimer. L'exception favorable demeure pour toutes les situations futures recevables, et l'AEEH de base n'est pas ajoutée aux exclusions.",
    "Préserver notamment « pour un même bénéficiaire », « pour le même enfant » au 7°, le seul élément du 1° de L245-3 au 9° et le cumul en cours de droit lorsque tous les jours de L544-4 ne sont pas servis. L544-4 reste maintenu. Les notes de 2025-1403 et leurs enfants nés/adoptés ou attendus dès le 1er janvier 2026 restent applicables dans leur champ. Les prestations des conjoints collaborateurs et indépendants ne sont pas des indemnités ordinaires de rupture ; aucune suppression d'avis médical en L544-2 ne modifie ces règles de cumul.",
    "Les neuf exclusions et la dérogation partielle sont conservées sans extension aux prestations de base ou aux autres membres de la famille.",
    "Aucune unification des prestations de compensation ou de remplacement n'est décidée ; les coûts d'un cumul élargi ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : aucun contrôle ou formulaire de cumul supplémentaire n'est institué par le maintien du texte entier.")

retained('L544-10',
    "Maintien intégral de l'information due sur l'AEEH et la prestation de compensation du handicap. Cette obligation du payeur facilite un choix effectif entre droits dont les règles de cumul diffèrent ; elle protège l'accès aux prestations plutôt qu'elle n'impose une charge à la famille. Aucun rapport périodique distinct ou document promotionnel n'est prescrit.",
    "L'obligation vise aussi bien le demandeur que le bénéficiaire de l'AJPP, les critères, conditions et modalités de demande des deux autres aides. Elle ne vaut ni nouvel examen ni demande forcée de prestation. Ne pas la confondre avec les états annuels de protection complémentaire supprimés par reporting_social.",
    "L'information individuelle nécessaire à l'exercice des droits est conservée, sans la transformer en nouveau rapport ou en prétendue simplification.",
    "Le support de l'information et son coût ne sont pas évalués ; aucun automatisme d'attribution ou de transfert des données médicales n'est créé.",
    "Aucune charge nouvelle n'est identifiée : le payeur garde son obligation existante et la famille n'a pas à produire de preuve de réception nouvelle.")

retained('L545-1',
    "Maintien intégral de l'allocation forfaitaire en cas de décès d'un enfant, de la modulation des ressources et de la protection contre les retenues d'autres indus. Il s'agit d'une prestation de soutien, non d'un droit français de succession ni d'un prélèvement sur un capital décès. Le non-cumul avec les capitaux sociaux énumérés est conservé sans supprimer ces capitaux ou créer un remboursement fiscal.",
    "Préserver les plafonds selon le nombre d'enfants, l'indexation hors tabac, le versement réglementaire et la dernière dérogation à L553-2, dont la source et les notes ont été lues en entier dans reference-targets. L512-3, lu dans le corpus, dispense cette allocation de la condition de rémunération de l'enfant. Les références transport et invalidité-décès demeurent à leur champ social ; leurs textes extérieurs non fournis ne sont pas réécrits. La note relative aux IV et V de l'article 5 de la loi 2020-692 protège la transition historique et ne constitue pas une date de réforme nouvelle. Les successions et les donations n'interviennent pas dans le fait générateur de cette aide.",
    "L'aide au décès, son indexation et l'interdiction de retenir d'autres indus sur son versement sont intégralement maintenues ; aucun impôt aboli n'est compté ici.",
    "Le coût de l'allocation et des capitaux décès, leurs montants et la coordination documentaire hors corpus ne sont pas chiffrés ou déclarés achevés.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration successorale, preuve fiscale ou certificat de non-imposition n'est ajouté à l'aide.",
    "Les avantages possibles sont l'allocation forfaitaire pour chaque décès éligible, son barème de ressources avec plafonds familiaux indexés, ainsi que l'interdiction de retenir sur elle les autres prestations indûment versées. Tous demeurent ouverts aux décès futurs recevables et aux droits antérieurs. Le non-cumul vise seulement les capitaux sociaux énumérés : ces versements ne sont pas une taxe de succession, et la récupération des seuls indus de cette allocation reste assortie des règles protectrices de L553-2.")

retained('L551-1',
    "Maintien intégral de la base mensuelle et de sa revalorisation au 1er avril, avec les exceptions du CMG et de l'AJPP. Cette règle maintient la valeur des aides familiales et leur coordination ; la supprimer réduirait un avantage sans supprimer de taxe. Le gel envisagé pour une seule fraction de certaines pensions ne s'étend pas aux prestations familiales.",
    "L161-25 a été lu avec sa proposition : coefficient d'inflation hors tabac et plancher égal à un conservés. L531-5 fourni dans reference-targets contient ses propres renvois à la date de L551-1 malgré l'exception à sa base de calcul ; ne pas supprimer ces renvois ni les exclusions d'indemnités de rupture au III 6°. L544-1 est maintenu et L544-6 garde son indexation SMIC au 1er janvier. La note renvoie aux VI et VII de l'article 86 de la loi 2022-1616 ; ces modalités historiques ne sont pas une date nouvelle de promulgation.",
    "La revalorisation des bases et les deux régimes de calcul distincts sont conservés sans économie de désindexation ni réduction de cotisation revendiquée.",
    "Aucun montant futur d'inflation n'est prédit ; le financement et le gel transitoire de certaines pensions demeurent en dehors de cet article.",
    "Aucune charge nouvelle n'est identifiée : la revalorisation reste une opération des organismes, sans démarche annuelle supplémentaire des familles.")

retained('L552-1',
    "Maintien intégral de la règle d'effet des changements de situation et de sa réserve de continuité des prestations. Elle protège les droits lors des changements de nature de l'aide, sans instituer de nouveau formulaire, délai minimal ou autorisation. Son abrogation ferait disparaître une protection générale sans simplification démontrée.",
    "L531-4, lu en entier dans le corpus, prévoit au I 3 et au dernier alinéa du VI des dérogations expresses à L552-1 maintenant la durée étendue de PreParE lors d'une mise en couple ; elles demeurent opérantes. La règle présente n'impose pas à elle seule une nouvelle déclaration de changement et n'écarte aucune transition propre à une prestation.",
    "La continuité des prestations et les règles d'effet des changements sont conservées ; aucune nouvelle obligation supprimée n'est comptabilisée.",
    "Les dates propres à chaque prestation et les dérogations existantes restent applicables ; aucune date de versement uniforme n'est créée.",
    "Aucune charge nouvelle n'est identifiée : aucun registre de changements, attestation ou nouvelle périodicité déclarative n'est ajouté.")


# Les nouveaux corps portent exclusivement des suppressions de fond identifiées.
prime = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>"
    "<p>À compter de cette date, le versement de la prime à la naissance ne peut être subordonné à la réalisation du premier examen prénatal médical obligatoire ni à la production de sa justification. Cette règle s'applique aux primes dont le droit s'ouvre à compter de cette date ainsi qu'aux demandes non définitivement tranchées à cette date, y compris lorsque la grossesse a commencé antérieurement. Les justificatifs de grossesse exigés pour l'attribution de la prime ne peuvent imposer la réalisation de cet examen.</p>"
    "<p>Pour les prestations dues à compter de cette date, le seul défaut de réalisation ou de justification de cet examen ne peut davantage fonder une suspension de la prestation d'accueil du jeune enfant. Les autres conditions d'attribution et de versement des prestations ainsi que les obligations médicales prévues à l'article L. 2122-1 du code de la santé publique demeurent applicables.</p>"
    "<p>Les prestations afférentes aux périodes antérieures conservent leur régime, à l'exception des primes visées au deuxième alinéa. Les décisions devenues définitives avant cette date ne sont pas remises en cause. Les créances, restitutions, prescriptions et recours relatifs aux prestations demeurant régies par le droit antérieur sont préservés, sous réserve de l'application des dispositions répressives plus douces lorsqu'elle est légalement requise. Aucune restitution générale des sommes légalement dues n'est créée.</p>"
)

aeeh = (
    "<p>L'allocation et son complément éventuel sont attribués au vu de la décision de la commission mentionnée à l'article L. 146-9 du code de l'action sociale et des familles appréciant si l'état de l'enfant ou de l'adolescent justifie cette attribution.</p>"
    "<p>L'allocation et son complément ne peuvent être suspendus ni supprimés au seul motif que la personne ayant la charge de l'enfant ne donne pas suite aux mesures préconisées par la commission. Les conditions d'attribution prévues à l'article L. 541-1, les contrôles de leur respect, les garanties de procédure et les voies de recours demeurent applicables.</p>"
    "<p>Le deuxième alinéa s'applique aux prestations dues à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsqu'une décision d'attribution, de suspension ou de suppression a été prise antérieurement. Les effets futurs d'une suspension ou d'une suppression fondée exclusivement sur ce motif cessent à cette date, si les autres conditions du droit demeurent remplies. Les créances, restitutions, prescriptions et recours relatifs aux périodes antérieures conservent leur régime, sous réserve de l'application des dispositions répressives plus douces lorsqu'elle est légalement requise.</p>"
)

ajpp2 = (
    "<p>La particulière gravité de la maladie, du handicap ou de l'accident visés au premier alinéa de l'article L. 544-1 ainsi que le caractère indispensable d'une présence soutenue et de soins contraignants sont attestés par un certificat médical détaillé, établi par le médecin qui suit l'enfant au titre de la maladie, du handicap ou de l'accident susmentionnés. Le certificat médical précise la durée prévisible du traitement. Le droit à la prestation est ouvert au vu de ce certificat, sans être subordonné à un avis favorable préalable du service du contrôle médical prévu à l'article L. 315-1 ou du régime spécial de sécurité sociale. Le service compétent conserve le contrôle des conditions médicales du droit à la prestation, dans le respect du secret médical et des voies de recours applicables ; ce contrôle ne constitue pas une autorisation préalable de son ouverture, de son renouvellement ou de son versement.</p>"
    "<p>Le droit est ouvert pour une période égale à la durée prévisible du traitement de l'enfant visée au premier alinéa. Lorsque le médecin le prévoit, la durée fait l'objet d'un réexamen à l'échéance qu'il a fixée et qui ne peut être inférieure à six mois. Le seul écoulement de quatorze mois n'impose ni réexamen ni production d'un nouveau certificat médical.</p>"
    "<p>Les dispositions du présent article s'appliquent aux journées indemnisables à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris au titre des droits déjà ouverts et des demandes en cours, sans nouveau dépôt de demande ni production d'un certificat encore valable déjà remis. Les autres conditions d'attribution et les limites de durée et de nombre d'allocations demeurent applicables. Les prestations dues au titre de journées antérieures, les créances, les restitutions, les prescriptions et les recours correspondants conservent leur régime.</p>"
)

ajpp3 = (
    "<p>L'allocation est versée dans la limite d'une durée maximum fixée par décret pour un même enfant et par maladie, handicap ou accident. Le nombre maximum d'allocations journalières versées au cours de cette période est égal à trois cent dix. Le versement de l'allocation n'est pas subordonné à un avis préalable du service du contrôle médical.</p>"
    "<p>A titre exceptionnel et par dérogation au premier alinéa, lorsque le nombre maximal d'allocations journalières est atteint au cours de la période mentionnée au même premier alinéa et qu'un nouveau certificat médical établi par le médecin qui suit l'enfant atteste le caractère indispensable, au regard du traitement de la pathologie ou du besoin d'accompagnement de l'enfant, de la poursuite des soins contraignants et d'une présence soutenue, la durée maximale mentionnée au premier alinéa du présent article peut être renouvelée une fois au titre de la même maladie, du même handicap ou du fait de l'accident dont l'enfant a été victime, et ce avant la fin du terme initialement fixé. Ce renouvellement n'est pas subordonné à un accord du service du contrôle médical prévu à l'article L. 315-1 ou du régime spécial de sécurité sociale.</p>"
    "<p>Au-delà de la durée maximale prévue au premier alinéa, le droit à l'allocation journalière de présence parentale peut être ouvert de nouveau, dès lors que les conditions mentionnées aux articles L. 544-1 et L. 544-2 sont réunies, dans les situations qui suivent :</p>"
    "<p>1° En cas de rechute ou de récidive de la pathologie de l'enfant au titre de laquelle le droit à l'allocation journalière de présence parentale avait été ouvert ;</p>"
    "<p>2° Lorsque la gravité de la pathologie de l'enfant au titre de laquelle le droit à l'allocation journalière de présence parentale avait été ouvert nécessite toujours une présence soutenue et des soins contraignants.</p>"
    "<p>La suppression de l'avis ou de l'accord médical préalable s'applique aux journées indemnisables à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris au titre des droits déjà ouverts et des demandes de renouvellement en cours. Aucun nouveau dépôt ni certificat encore valable déjà remis n'est exigé du seul fait de cette suppression. Les avances déjà accordées sont imputées une seule fois sur les allocations dues ; la seule absence de l'avis ou de l'accord supprimé ne constitue pas un motif de récupération. Les autres conditions d'attribution et les contrôles maintenus par l'article L. 544-2 demeurent applicables. Les prestations afférentes aux journées antérieures, les créances, restitutions, prescriptions et recours correspondants conservent leur régime.</p>"
)


def draft(number, xml, reason, notes, changes, imp, benefit=None, repeal=False):
    src = by_number[number]
    out = {k: src[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    out.update(proposed_xml=xml, reason=reason, review_notes=notes,
               status='rewrite_draft', substantive_impact=imp)
    if repeal:
        out.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=changes)
    else:
        out.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=changes)
    if benefit:
        out['benefit_review'] = benefit
    answers[number] = out


draft('L533-1', prime,
    "Réforme de fond : abrogation de la condition financière de réalisation et de justification du premier examen prénatal, et de l'habilitation à imposer cette preuve pour payer la prime. La sanction de suspension de PAJE fondée sur ce seul examen est écartée pour les prestations futures. La grossesse et les autres conditions de la prime restent à établir selon leur droit propre ; l'examen médical obligatoire conserve son fondement sanitaire. Une aide à l'accueil de l'enfant n'a pas à servir de sanction supplémentaire d'un suivi médical dont la protection sanitaire demeure organisée séparément.",
    "D532-1 et D532-2 ont été lus en entier : coordonner le document de grossesse attestant l'examen au deuxième alinéa de D532-1 et abroger pour les prestations nouvelles la suspension fondée sur le renvoi à L533-1 dans D532-2. La proposition interdit directement que ces dispositions réglementaires rétablissent la condition supprimée ; aucune déclaration équivalente n'est instituée. Les données nécessaires à la réalité et à la datation de la grossesse restent distinctes. CSP L2122-1, cité dès la source, n'est pas fourni dans le corpus des cinq codes : sa règle sanitaire n'est pas abrogée ni réputée réécrite. L531-2, lu, conserve l'aide avant naissance, ses délais, cas de naissance précoce/décès et majoration d'adoption. D545-8 6°, lu, concerne une preuve dans le régime distinct de l'allocation décès et n'est pas supprimé par analogie. Aucun impôt ni rendement budgétaire n'est inventé.",
    "Condition et justification de réalisation du premier examen prénatal pour le versement de la prime à la naissance, avec fin de la suspension de PAJE fondée sur ce seul défaut pour les prestations futures ; obligations sanitaires distinctes maintenues.",
    impact('material_reduction',
        "La source entière ne comporte que le prérequis d'examen et sa justification réglementaire : ils sont effectivement retirés du paiement de la prime, sans attestation de remplacement ni diminution de l'aide.",
        "L'obligation sanitaire d'examen n'est pas supprimée. Les déclarations de grossesse utiles à d'autres droits, les critères de ressources et les décisions antérieures définitives restent à leur champ ; le coût public net n'est pas chiffré.",
        "Aucune charge nouvelle n'est identifiée : aucun document supplémentaire ne remplace la preuve supprimée et les justificatifs de grossesse existants ne peuvent exiger cet examen. Le suivi sanitaire et les autres conditions de la prime demeurent.",
        [effect('obligation_removed', 'prime-naissance-fin-condition-examen-prenatal',
            "Suppression du prérequis financier et de la justification de l'examen prénatal pour la prime à la naissance ; une seule mesure avec ses coordinations d'exécution.",
            "Prime à la naissance conditionnée à la justification du premier examen prénatal obligatoire de la mère ; aucun taux de taxe n'est en cause.",
            "Aucune réalisation ou preuve de cet examen exigible pour payer la prime ; les autres conditions d'attribution subsistent et l'obligation sanitaire n'est pas abolie.",
            'legal_duty', "Ménages et personnes éligibles à la prime à la naissance, y compris grossesses et demandes déjà en cours.",
            "Effet dès l'entrée en vigueur, prestations futures et dossiers en cours ; décisions antérieures définitives et droits relatifs aux périodes antérieures conservés selon le texte transitoire.",
            "Aucune déclaration, autorisation ou taxe de remplacement ; les preuves utiles de grossesse demeurent dans leur champ sans imposer l'examen.",
            "Le versement de la prime à la naissance est subordonné à la justification de la passation du premier examen prénatal médical obligatoire de la mère prévu en application de l'article L. 2122-1 du code de la santé publique.",
            "À compter de cette date, le versement de la prime à la naissance ne peut être subordonné à la réalisation du premier examen prénatal médical obligatoire ni à la production de sa justification.")]),
    "La prime à la naissance reste attribuable aux futures grossesses éligibles, sans perdre son plafond familial, ses cas favorables de naissance précoce ou de décès et ses autres garanties de L531-2. La preuve d'examen retirée est une condition restrictive, non un avantage. La prime d'adoption et sa majoration ne sont pas réduites. Le maintien du suivi sanitaire ne rétablit pas une sanction financière sur la PAJE.",
    repeal=True)

draft('L541-2', aeeh,
    "Réforme de fond limitée au second alinéa : suppression de la possibilité de suspendre ou supprimer l'AEEH et son complément pour le seul défaut de suite aux préconisations de la commission. L'appréciation initiale du handicap par la commission reste intégralement au premier alinéa. Les contrôles du handicap, des dépenses et de l'aide humaine restent suffisants pour vérifier l'affectation légale ; l'aide à l'enfant n'a pas à être une sanction autonome des choix d'accompagnement de sa famille.",
    "L541-1 reste entier, notamment sa voie d'éligibilité à taux inférieur liée à l'établissement, au dispositif adapté ou aux soins : la suppression d'une sanction ne supprime pas une condition matérielle du droit. R541-3 et R541-4, lus en entier, conservent le dossier, le réexamen en cas de changement et le contrôle de l'effectivité de l'aide humaine, avec avances. R541-5, lu, impose encore un réexamen sous deux ans après préconisations ; sa coordination doit distinguer vérification du handicap et rétablissement interdit de la sanction retirée, sans déclarer ce règlement réécrit. L'audition sur demande liée au motif supprimé ne devient pas une suppression des garanties procédurales des décisions prises sur d'autres fondements. Aucune compétence sanitaire ou de protection de l'enfance extérieure n'est abrogée. Le renvoi à L541-1 est intra-lot et n'est pas une cible supplémentaire dans reference_checks.",
    ["Possibilité de suspendre ou de supprimer l'AEEH et son complément au seul motif du défaut de suite aux mesures préconisées par la commission, y compris ses effets sur les prestations futures."],
    impact('material_reduction',
        "Le motif autonome de suspension ou suppression figurant au second alinéa de la source est retiré ; la décision d'éligibilité, le handicap requis et les contrôles des conditions subsistent.",
        "La proposition ne garantit pas une allocation lorsque les conditions matérielles cessent d'être remplies ; les périodes anciennes gardent leur régime et les textes réglementaires hors lot restent à coordonner.",
        "Aucune charge nouvelle n'est identifiée : aucune déclaration d'observance, attestation alternative ou autorisation ne remplace le motif supprimé. Les contrôles conservés portent sur les conditions déjà existantes de L541-1.",
        [effect('obligation_removed', 'aeeh-fin-sanction-non-suivi-preconisations',
            "Retrait de la sanction financière autonome de non-suivi des préconisations, sans retrait des conditions de handicap ni des protections de l'enfant.",
            "La personne ne donnant pas suite aux mesures préconisées peut voir l'AEEH suspendue ou supprimée, avec audition sur sa demande.",
            "Aucune suspension ou suppression fondée sur ce seul comportement ; le handicap, les frais et l'aide humaine demeurent contrôlables.",
            'legal_duty', "Personnes assumant la charge d'un enfant ou adolescent handicapé bénéficiaire de l'AEEH et, le cas échéant, de son complément.",
            "Prestations dues dès l'entrée en vigueur, y compris effets futurs des décisions antérieures ; autres conditions du droit maintenues, sans remboursement rétroactif général.",
            "Aucune formalité de remplacement ; décision d'éligibilité et contrôles existants maintenus, sans nouvelle obligation d'observance.",
            "Lorsque la personne ayant la charge de l'enfant handicapé ne donne pas suite aux mesures préconisées par la commission, l'allocation peut être suspendue ou supprimée dans les mêmes conditions et après audition de cette personne sur sa demande.",
            "L'allocation et son complément ne peuvent être suspendus ni supprimés au seul motif que la personne ayant la charge de l'enfant ne donne pas suite aux mesures préconisées par la commission.")]),
    "L'AEEH et son complément restent attribués par la commission pour tous les enfants futurs remplissant L541-1 ; la voie d'accès à taux d'incapacité inférieur demeure soumise à ses propres conditions. La majoration pour parent isolé et les autres droits connexes ne sont pas supprimés. L'allègement retire uniquement une cause de sanction financière, sans fermer l'accès aux soins, à l'éducation adaptée ou aux aides humaines.")

draft('L544-2', ajpp2,
    "Deux suppressions de fond : l'avis médical favorable préalable, doublonnant le certificat détaillé du médecin suivant l'enfant, cesse de conditionner l'AJPP ; le réexamen automatique à quatorze mois et le plafond de quatorze mois de l'échéance médicale sont supprimés. Le médecin conserve la détermination de la durée et la faculté de prévoir un réexamen, avec le plancher favorable de six mois. Le contrôle médical demeure possible sans autorisation préalable ; ni la gravité ni les soins contraignants ne sont supprimés des conditions d'accès.",
    "Coordination opérée avec L544-3 dans le lot : fin de l'accord supplémentaire de renouvellement et paiement sans attente d'avis, avec protection des avances. L1225-62 du travail, lu intégralement, vise bien le deuxième alinéa de L544-2 pour le réexamen ; ce rang est conservé, la transition étant ajoutée au troisième alinéa. R544-1 et R544-2, lus, doivent conserver le certificat secret et le service compétent pour le contrôle, sans second visa préalable. R544-3 premier alinéa doit perdre sa procédure d'avis tacite, mais son deuxième alinéa favorable sur le silence du payeur ne doit pas être abrogé. D544-2, lu, mentionne encore une année alors que la source législative du 14 juin 2026 dit quatorze mois : incohérence préexistante signalée, puis périodicité obligatoire à retirer conformément au nouveau deuxième alinéa. Ces règlements ne sont pas déclarés réécrits. Le contrôle conservé ne crée aucun accès supplémentaire aux données de santé ; aucune décision de distribution d'IS, retraite ou contrat unique n'étend son champ.",
    ["Avis favorable préalable du service du contrôle médical ou du régime spécial comme condition d'ouverture du droit à l'allocation journalière de présence parentale.",
     "Réexamen systématique du traitement au plus tard à quatorze mois, plafond de cette échéance et renouvellement du certificat imposé par ce seul écoulement de durée."],
    impact('material_reduction',
        "Par rapport aux deux alinéas officiels entiers, la proposition retire une autorisation médicale préalable et une répétition périodique obligatoire du contrôle, tout en gardant le certificat clinique, le contrôle du droit et le plancher de six mois.",
        "Les 310 allocations, limites de durée globale, conditions de congé et contrôles ciblés subsistent. Les coordinations réglementaires identifiées ne sont pas exécutées dans ce lot ; aucun coût net global ou rendement n'est établi.",
        "Aucune charge nouvelle n'est identifiée : le certificat détaillé et sa durée sont déjà requis, aucune déclaration ne remplace l'avis et aucun registre de suivi n'est créé. Le contrôle des conditions est maintenu, sans droit d'accès nouveau aux données.",
        [effect('authorization_removed', 'ajpp-fin-accord-medical-prealable',
            "Suppression de l'avis favorable préalable à l'ouverture et au service de l'AJPP, certificat du médecin suivant l'enfant conservé.",
            "Certificat médical détaillé et avis favorable du service du contrôle médical ou du régime spécial exigés pour le droit à l'AJPP.",
            "Certificat détaillé suffisant pour l'élément médical du droit ; aucun avis favorable préalable, autres conditions et contrôle médical maintenus.",
            'legal_duty', "Demandeurs et bénéficiaires de l'AJPP du régime général et des régimes spéciaux, dans le champ de L544-1 et L544-8.",
            "Journées indemnisables à compter de l'entrée en vigueur, droits ouverts et demandes en cours compris ; pas de nouveau dépôt pour ces dossiers.",
            "Pas d'avis ou de déclaration de remplacement ; certificat clinique existant, secret médical et voies de recours conservés.",
            "Le droit à la prestation est soumis à un avis favorable du service du contrôle médical prévu à l'article L. 315-1 ou du régime spécial de sécurité sociale.",
            "Le droit à la prestation est ouvert au vu de ce certificat, sans être subordonné à un avis favorable préalable du service du contrôle médical prévu à l'article L. 315-1 ou du régime spécial de sécurité sociale."),
         effect('obligation_removed', 'ajpp-fin-reexamen-periodique-quatorze-mois',
            "Suppression du réexamen obligatoire tous les quatorze mois du seul fait de la durée du traitement et de la borne haute correspondante.",
            "Échéance médicale entre six et quatorze mois ; nouvel examen obligatoire à quatorze mois si le traitement prévisible excède cette durée.",
            "Durée médicale prévisible et réexamen prévu par le médecin, jamais avant six mois ; aucun réexamen ni certificat nouveau exigible du seul écoulement de quatorze mois.",
            'legal_duty', "Enfants nécessitant un traitement prolongé et parents bénéficiaires de l'AJPP, sans modification du plafond global de jours.",
            "Journées futures dès l'entrée en vigueur, y compris droits déjà ouverts ; expiration réelle du certificat, changement médical et renouvellement exceptionnel demeurent distincts.",
            "Aucune attestation annuelle de remplacement ; contrôles médicaux existants conservés sans périodicité obligatoire de substitution.",
            "Dans tous les cas, lorsque la durée prévisible excède quatorze mois, elle fait l'objet d'un nouvel examen à cette échéance.",
            "Le seul écoulement de quatorze mois n'impose ni réexamen ni production d'un nouveau certificat médical.")]),
    "Le droit à l'AJPP est conservé sur le certificat du médecin suivant l'enfant, avec la même gravité, présence et soins requis. La durée prévisible, le réexamen choisi par le médecin et la protection d'une échéance non inférieure à six mois restent applicables aux futurs dossiers et aux droits en cours. Supprimer la seconde autorisation et le réexamen automatique n'écarte ni l'accès aux soins ni les renouvellements favorables de L544-3 ; les certificats valables déjà remis ne sont pas à refaire.")

draft('L544-3', ajpp3,
    "Réforme de fond coordonnée à L544-2 : l'accord du contrôle médical confirmant le certificat de renouvellement exceptionnel est retiré, sans nouveau visa. La simple possibilité d'avance dans l'attente d'un avis est remplacée par l'absence de condition d'avis au versement ; les avances déjà consenties restent protégées contre une récupération fondée sur cette seule absence. Le plafond de 310 allocations, le renouvellement anticipé une fois et les deux voies ultérieures de réouverture sont intégralement conservés.",
    "Les cinq premiers alinéas gardent leurs rangs, y compris les 1° et 2° ; la transition est ajoutée après eux. L1225-62 du travail, lu en entier, permet déjà le renouvellement exceptionnel du congé sur le nouveau certificat, sans accord du service médical : la proposition n'ajoute pas une durée déterminée d'emploi. D544-1, D544-3 et D544-5, lus, conservent respectivement la période de trois ans, les renouvellements et la nouvelle pathologie ; R544-1 garde le certificat spécifique, R544-3 doit être coordonné sans supprimer la décision tacite favorable du payeur. Le contrôle médical L315-1 ne doit pas faire renaître un accord préalable pour ce renouvellement. Une seule famille de mesure ajpp-fin-accord-medical-prealable, sans compter chaque renvoi comme une seconde suppression générale.",
    ["Accord du service du contrôle médical ou du régime spécial confirmant le nouveau certificat pour le renouvellement exceptionnel anticipé de la période d'AJPP après épuisement du nombre maximal de journées.",
     "Attente d'un avis médical comme fondement du régime d'avance, remplacée par un versement non soumis à cet avis et sans retrait des avances antérieurement accordées."],
    impact('material_reduction',
        "La confirmation médicale administrative du renouvellement exceptionnel est effectivement supprimée ; le paiement est coordonné sans attente d'avis. Aucune limitation de 310 jours, faculté de renouvellement ou réouverture des deux derniers cas n'est perdue.",
        "Le certificat de renouvellement, le plafond global et les conditions matérielles subsistent ; le paiement n'est pas promis avant vérification des autres conditions du droit. Aucun solde national de coûts n'est établi.",
        "Aucune charge nouvelle n'est identifiée : le nouveau certificat est celui déjà exigé par la source pour le renouvellement exceptionnel ; aucun formulaire, visa ou contrôle périodique de remplacement n'est créé. L'imputation des avances évite un double paiement sans nouvelle démarche.",
        [effect('authorization_removed', 'ajpp-fin-accord-medical-prealable',
            "Retrait, dans le volet de renouvellement exceptionnel, de la confirmation par le contrôle médical ; même mesure que L544-2, et non deuxième suppression générale d'AJPP.",
            "Après épuisement des 310 allocations avant le terme, nouveau certificat médical confirmé par accord du contrôle médical pour renouveler la période une fois.",
            "Même épuisement, même nouveau certificat attestant soins et présence indispensables, même renouvellement une fois avant terme, sans accord du contrôle médical.",
            'legal_duty', "Parents atteignant le maximum d'allocations avant la fin de la période pour la même maladie, le même handicap ou le même accident de l'enfant.",
            "Journées indemnisables après l'entrée en vigueur et demandes de renouvellement en cours ; droits antérieurs et avances préservés selon la transition.",
            "Aucun agrément ou déclaration de remplacement ; certificat spécifique existant et autres contrôles de L544-2 conservés.",
            "A titre exceptionnel et par dérogation au premier alinéa, lorsque le nombre maximal d'allocations journalières est atteint au cours de la période mentionnée au même premier alinéa et qu'un nouveau certificat médical établi par le médecin qui suit l'enfant et attestant le caractère indispensable, au regard du traitement de la pathologie ou du besoin d'accompagnement de l'enfant, de la poursuite des soins contraignants et d'une présence soutenue est confirmé par un accord du service du contrôle médical prévu à l'article L. 315-1 ou du régime spécial de sécurité sociale, la durée maximale mentionnée au premier alinéa du présent article peut être renouvelée une fois au titre de la même maladie, du même handicap ou du fait de l'accident dont l'enfant a été victime, et ce avant la fin du terme initialement fixé.",
            "Ce renouvellement n'est pas subordonné à un accord du service du contrôle médical prévu à l'article L. 315-1 ou du régime spécial de sécurité sociale."),
         effect('coordination', 'ajpp-fin-accord-medical-prealable',
            "Coordination de l'ancienne avance en attente d'avis avec la disparition de cet avis, sans compter un report de paiement comme une baisse de prélèvement.",
            "Avance possible dans l'attente de l'avis préalable de L544-2.",
            "Versement non conditionné à cet avis ; avances déjà consenties imputées une seule fois et non récupérées pour la seule absence de cet avis.",
            'other', "Bénéficiaires de l'AJPP dont le versement ou une avance dépendait de l'avis préalable supprimé.",
            "Paiements des journées nouvelles et avances antérieurement accordées ; toutes autres conditions d'ouverture et recours conservés.",
            "Aucune nouvelle demande d'avance ni nouvelle autorisation de paiement n'est créée ; les conditions générales de paiement demeurent.",
            "L'allocation peut faire l'objet d'une avance dans l'attente de l'avis mentionné à la dernière phrase du premier alinéa de l'article L. 544-2.",
            "Le versement de l'allocation n'est pas subordonné à un avis préalable du service du contrôle médical.")]),
    "Les avantages conservés sont les 310 allocations par période, le renouvellement anticipé exceptionnel une fois pour la même affection ou le même accident, puis les réouvertures pour rechute/récidive ou persistance de gravité. Ils restent accessibles aux futures situations éligibles, sans accord médical administratif supplémentaire. L'avance n'est pas supprimée au détriment du bénéficiaire : l'attente d'avis disparaît et les avances acquises sont imputées sans double compte, sans récupération pour le seul défaut de cet avis.")


# Analyses des cibles requises : aucune cible contextuelle n'est ajoutée.
contexts = {
    'L532-2': "L532-2 règle les cumuls de la PreParE et la reprise des indemnités de chômage",
    'L541-1': "L541-1 ouvre l'AEEH selon le handicap, les dépenses et l'aide nécessaire à l'enfant",
    'L543-1': "L543-1 ouvre l'allocation de rentrée scolaire aux élèves et apprentis selon l'âge, les ressources et la rémunération",
    'L543-2': "L543-2 maintient l'allocation différentielle en cas de dépassement limité des ressources de rentrée scolaire",
    'L543-3': "L543-3 protège l'allocation de rentrée scolaire de l'enfant placé, son pécule et la dérogation familiale",
    'L544-1': "L544-1 indemnise les jours de présence parentale et vise séparément les agents publics",
    'L544-2': "L544-2 fixe le certificat et la durée médicale de l'AJPP, avec suppression du second avis et du réexamen automatique",
    'L544-3': "L544-3 règle les 310 allocations, leur renouvellement exceptionnel et les réouvertures de l'AJPP",
    'L544-6': "L544-6 règle le montant de l'AJPP, son indexation et le fractionnement du congé ou le temps partiel",
    'L544-7': "L544-7 attribue un complément mensuel pour frais avec plafonds majorés pour les familles concernées",
    'L544-8': "L544-8 ouvre l'AJPP à plusieurs professions et aux demandeurs d'emploi, puis rétablit leur reliquat de chômage",
    'L544-9': "L544-9 articule les non-cumuls de l'AJPP et le cumul partiel favorable de maladie ou d'accident du travail",
    'L545-1': "L545-1 institue une aide au décès d'un enfant et la protège des retenues d'autres indus",
    'L551-1': "L551-1 indexe les bases de prestations familiales avec règles distinctes pour le CMG et l'AJPP",
}


def labor_assessment(number, target):
    context = contexts[number]
    if target == 'L1234-1':
        return (context + ". Aucun renvoi au préavis de licenciement ne figure dans cet article. La proposition cible distingue quinze jours calendaires pour les nouveaux contrats et les anciens délais liés à l'ancienneté pour les contrats antérieurs ; ces règles de notification de rupture ne deviennent pas une condition d'accès à cette prestation. Les délais de congé ou de traitement médical gardent leur objet propre.")
    if target == 'L1221-2':
        extra = {
            'L543-1': " L'apprentissage demeure une phase pédagogique éligible dans un emploi nouveau à durée indéterminée, sans transformer sa durée de formation en terme de l'emploi.",
            'L543-2': " Le maintien du différentiel vaut aussi pour les futurs apprentis éligibles à L543-1, sans nouveau CDD spécial.",
            'L543-3': " La mesure de placement et le pécule ne dépendent pas du type de contrat des parents ou de l'apprenti ; les droits futurs restent ouverts.",
            'L544-1': " Les salariés en contrat unique gardent le congé et l'AJPP ; les agents publics restent au régime expressément visé au deuxième alinéa.",
            'L544-2': " La durée du certificat n'est pas un terme d'emploi ; le renvoi de L1225-62 au deuxième alinéa médical demeure à son rang.",
            'L544-3': " Le terme de la période d'AJPP et le renouvellement exceptionnel ne mettent pas fin à l'emploi ni ne créent un nouveau contrat.",
            'L544-6': " Le fractionnement ou le temps partiel du congé ne devient ni mission à terme ni nouveau contrat d'emploi ; les règles publiques restent distinctes.",
            'L544-8': " Une formation rémunérée peut être limitée sans borner l'emploi ; les indépendants et régimes agricoles ne deviennent pas des salariés privés.",
        }.get(number, " Les droits sociaux des futurs bénéficiaires éligibles demeurent ouverts ; aucune durée d'aide ne devient une durée d'emploi.")
        return (context + ". Aucun nouveau CDD n'est autorisé par cette règle sociale. La proposition de L1221-2 impose le contrat unique à durée indéterminée aux nouvelles embauches et préserve les contrats antérieurs, sans renouvellement contournant la réforme." + extra)
    if target == 'L1234-9':
        return (context + ". Il ne s'agit pas de l'indemnité ordinaire de rupture et aucun renvoi à L1234-9 ne fixe le droit ici. La cible propose zéro avant un an atteint au terme effectif préavis inclus, puis 0,20 mois par année totale, fractions par mois complets et plafond légal de six mois à charge de l'employeur ; anciens droits et indemnités spéciales restent distincts. Ni ce seuil ni la notification de rupture ne sont importés dans la prestation.")
    raise ValueError(target)


special_checks = {
    ('L532-2', 'L663-1'): "Le II 2° vise les allocations de repos et indemnités de remplacement des conjoints collaborateurs définies par L663-1, non une indemnité de licenciement. La revalorisation par renvoi au SMIC et les durées propres restent intactes ; le III conserve le cumul en cours de droit pour l'activité partielle et le IV le mois d'ouverture prévu. Aucune ancienneté ni notification du contrat unique n'est ajoutée aux conjoints collaborateurs.",
    ('L532-2', 'L623-1'): "Le II 2° vise la maternité/paternité des indépendants et leurs prestations de cessation d'activité, distinctes de la rupture d'emploi. La source cible comprend aussi le deuil de quinze jours et la faculté favorable des élus locaux au III ter : le renvoi de non-cumul ne les abroge pas. La réserve QPC du 8 août 2025 sur la reconnaissance conjointe est conservée dans le contexte légal ; aucune exclusion de ces bénéficiaires ni seuil d'ancienneté privé n'est créé.",
    ('L532-2', 'L623-2'): "Le II 2° vise expressément les indemnités supplémentaires de naissance, avec cessation ou non-reprise après les durées minimales de L623-1. Leur revalorisation et le champ des enfants nés, adoptés ou attendus à compter du 1er janvier 2026 restent distincts du préavis de rupture. Les cumuls favorables III à V de L532-2 demeurent dans leur champ, sans transformer l'arrêt d'activité en fin de contrat.",
    ('L541-1', 'L351-1'): "La source de L541-1 renvoie à L351-1 du code de l'éducation pour le dispositif adapté, et non à cette cible homonyme du CSS sur la pension de vieillesse. La proposition de retraite préserve droits constitués et solidarité et conditionne le transfert aux règles de financement. Elle ne modifie donc pas l'incapacité de l'enfant, le complément ni l'accès futur à l'AEEH ; aucun renvoi vieillesse artificiel n'est ajouté.",
    ('L543-2', 'L543-1'): "Le renvoi vise exactement le plafond de ressources variable avec les enfants à charge de L543-1, non son plafond de rémunération de l'enfant. La cible officielle sans proposition conserve élèves et apprentis, indexation hors tabac et modulation d'âge. Le différentiel reste ouvert en cas de dépassement limité sans nouvelle ancienneté ou notification d'emploi, y compris pour les apprentis futurs en contrat unique.",
    ('L543-3', 'L543-1'): "Le premier et le deuxième alinéas renvoient à l'allocation de rentrée scolaire de L543-1 ; L543-2 demeure la voie différentielle parallèle. La cible officielle couvre élèves et apprentis selon âge et ressources. Le placement modifie le destinataire et crée le pécule, non le champ d'emploi : majorité/émancipation et dérogation familiale restent, sans ancienneté ni notification du contrat unique.",
    ('L544-2', 'L544-1'): "Le premier alinéa vise exactement la gravité de la maladie, du handicap ou de l'accident et la nécessité de présence et soins du premier alinéa de L544-1. Le certificat détaillé et ces critères restent ; seuls avis préalable et réexamen automatique sont supprimés. L'ouverture aux agents publics du deuxième alinéa de la cible est conservée, sans importation d'une ancienneté ou notification de rupture privée.",
    ('L544-2', 'L315-1'): "Le renvoi source désigne le service compétent pour l'avis favorable, non une règle d'ancienneté ou de préavis. La proposition retire cet avis comme préalable et conserve le contrôle des critères médicaux, sans élargir l'accès aux données protégé par le V. La proposition cible retire seulement le contrôle systématique lié aux statistiques de prescription au II ; elle ne dispense pas du certificat AJPP et ne rétablit pas une seconde autorisation au titre de cette allocation familiale.",
    ('L544-3', 'L544-1'): "Les réouvertures au troisième alinéa demeurent subordonnées aux conditions de gravité, présence soutenue et soins de L544-1, puis déclinées aux 1° et 2°. Le plafond de 310 allocations et le renouvellement exceptionnel une fois restent ; la suppression d'accord médical n'efface pas ces critères. Le champ public de la cible subsiste et la période d'indemnisation n'est pas un terme de contrat d'emploi.",
    ('L544-3', 'L315-1'): "Le deuxième alinéa source exigeait la confirmation du nouveau certificat par ce service. La proposition retire exactement cet accord et coordonne l'ancienne avance du premier alinéa, tout en conservant le service pour les contrôles de L544-2. L315-1 V et ses garanties de secret restent applicables ; son projet sur les prescriptions statistiquement élevées ne crée aucun avis favorable supplémentaire de renouvellement AJPP.",
    ('L544-7', 'L544-1'): "Le renvoi au premier alinéa de L544-1 identifie les trois causes graves ouvrant droit au complément pour frais ; il n'étend pas le montant forfaitaire à tout congé. Les plafonds familiaux et leurs majorations restent ouverts aux futurs bénéficiaires remplissant ces critères, salariés comme agents publics dans leur champ propre, sans condition d'ancienneté ou de notification de rupture.",
    ('L544-9', 'L663-1'): "Le 2° conserve le non-cumul de l'AJPP avec les prestations maternité/paternité des conjoints collaborateurs définies par L663-1. Les allocations, indemnités de remplacement et leur indexation SMIC subsistent ; le texte ne les transforme pas en indemnités de rupture ni n'y ajoute le seuil d'un an. Le cumul favorable final de L544-9 reste limité aux indemnités du 3° pendant l'activité à temps partiel.",
    ('L544-9', 'L623-1'): "Le 2° vise les prestations d'interruption et de remplacement de maternité/paternité du régime indépendant. L623-1 comprend aussi des droits de deuil et la dérogation des élus au III ter ; le renvoi dans cette énumération ne les abroge ni ne les assimile au contrat privé. La réserve QPC sur la filiation par reconnaissance conjointe demeure. La dernière exception de L544-9 vise seulement son 3°, pas une nouvelle exclusion générale de ces bénéficiaires.",
    ('L544-9', 'L623-2'): "Le 2° inclut les indemnités journalières supplémentaires de naissance créées dans ce régime de cessation d'activité. Leur durée renvoie à L331-8-1, non aux quinze jours de rupture du contrat unique. Le champ temporel de la loi 2025-1403 pour naissances/adoptions 2026 ou attendues dès cette date reste conservé ; aucune condition privée d'ancienneté ou taxe ne remplace la prestation.",
    ('L545-1', 'L553-2'): "Le dernier alinéa applique L553-2 aux seuls indus de cette allocation, mais interdit de retenir sur elle les autres prestations indûment versées. La cible conserve composition familiale, ressources, charges de logement et possibilité de remise pour précarité hors fraude ; cette protection n'est pas effacée par les règles de récupération croisée. Ni capital décès ni allocation de deuil ne devient un prélèvement de succession ou une indemnité ordinaire de licenciement.",
    ('L551-1', 'L544-1'): "L544-1 est expressément exclu de la base mensuelle commune de L551-1 : le montant de son AJPP suit L544-6 et le SMIC au 1er janvier. La cible conserve salariés et agents publics ; les suppressions d'avis de L544-2/L544-3 ne modifient pas cette exception de calcul. Ni préavis de quinze jours ni ancienneté d'un an ne conditionnent cette indexation.",
    ('L551-1', 'L531-5'): "L'exception au calcul par base mensuelle n'efface pas les renvois de L531-5 à la date du 1er avril : plafond du II et barème du III demeurent revalorisés. Le III 6° de la proposition cible exclut aussi les indemnités du contrat unique et protège les anciennes indemnités CDD pour vérifier les plafonds de rémunération ; L551-1 ne rétablit donc ni CDD futur ni inclusion défavorable de ces indemnités. Les dispenses d'activité du I restent intégrales.",
}

for src in sources:
    number = src['number']
    required = references['requirements'][src['code_id'] + '|' + src['source_id']]
    checks = []
    for key in required:
        target = references['targets'][key]
        if target['code_id'] == 'LEGITEXT000006072050':
            assessment = labor_assessment(number, target['number'])
        else:
            assessment = special_checks[(number, target['number'])]
        checks.append(dict(target_key=key, view_sha256=target['view_sha256'], assessment=assessment))
    answers[number]['reference_checks'] = checks

result = [answers[a['number']] for a in sources]
(ROOT / 'answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json: {len(result)} articles; {sum(a["status"] == "rewrite_draft" for a in result)} nouveaux corps; {sum(len(a["reference_checks"]) for a in result)} vérifications de cibles.')
