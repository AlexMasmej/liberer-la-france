import json
import re
from html import unescape
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFERENCES = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWERS = {}


def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml))


def base(number, reason, review, classification, assessment, limitations, burdens, proposed=None):
    source = BY_NUMBER[number]
    answer = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    answer.update(proposed_xml=proposed, reason=reason, review_notes=review,
                  status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        answer['classification'] = 'retained_necessary'
    answer['substantive_impact'] = {
        'version': 1, 'classification': classification, 'assessment': assessment,
        'scope_limitations': limitations, 'new_burdens_review': burdens, 'effects': []}
    answer['reference_checks'] = []
    ANSWERS[number] = answer
    return answer


def reduction(answer, provisions):
    answer.update(change_type='normative_reduction',
                  reform_policy_id='editorial_direction_2026_10_19', removed_provisions=provisions)


def effect(answer, kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in plain(BY_NUMBER[answer['number']]['source_xml'])
    assert len(proposed_quote) >= 12 and proposed_quote in plain(answer['proposed_xml'])
    answer['substantive_impact']['effects'].append({
        'kind': kind, 'measure_id': measure, 'description': description,
        'before': before, 'after': after, 'unit': unit, 'affected_population': population,
        'conditions_and_transition': transition, 'replacement_or_new_burdens': replacement,
        'source_quote': source_quote, 'proposed_quote': proposed_quote})


# L351-17 : le rachat reste facultatif et contributif ; seule la forclusion d'âge est retirée.
p = replace_once(BY_NUMBER['L351-17']['source_xml'],
    "1° L'âge jusqu'auquel l'assuré peut présenter une demande, qui ne peut être inférieur à vingt-cinq ans ;",
    "1° Les modalités de présentation de la demande, qui ne peut être soumise à une limite d'âge ;")
p = replace_once(p, "Les étudiants peuvent demander", "Les étudiants et anciens étudiants peuvent demander")
p += "<p>La suppression de la limite d'âge s'applique aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente rédaction et à celles en cours à cette date, y compris pour les stages antérieurs entrant dans le champ du premier alinéa. Un refus antérieur fondé sur cette seule limite ne fait pas obstacle à une nouvelle demande, sans révision à ce titre des arrérages de pension dus pour des périodes antérieures à cette entrée en vigueur. Les versements antérieurs, les échelonnements accordés et les trimestres déjà pris en compte conservent leur régime, y compris les droits à remboursement des versements indus ou surnuméraires. Une même période ne peut être validée deux fois.</p>"
a = base('L351-17',
    "Réforme de fond : suppression de l'âge maximal de demande de validation des stages, sans supprimer la faculté avantageuse de rachat. La mention des anciens étudiants empêche que la fin des études rétablisse la restriction d'accès supprimée. Le versement reste volontaire, dans la limite de deux trimestres, et son imputation sur les trimestres du rachat à tarif réduit demeure intégrale. Il ne s'agit ni d'une baisse de cotisation obligatoire ni d'un transfert vers la capitalisation.",
    "D351-16, D351-17 et D351-18 lus intégralement : retirer la date limite du 31 décembre de l'année du trentième anniversaire dans D351-16 ; conserver les conditions des stages, les règles de preuve, le montant de 12 % du plafond mensuel par trimestre, le seul effet sur la minoration, les quatre trimestres par an, les remboursements et les échéanciers d'un ou deux ans. Ces règlements ne sont pas modifiés dans ce lot. L351-14-1 II reste le rachat distinct à montant abaissé ; le plafond total et la déduction des trimestres ne sont pas supprimés. Les articles du code de l'éducation déjà cités ne sont pas fournis intégralement dans le corpus autorisé : aucune modification de leur contenu n'est présumée. Note de 2023 maintenue pour son champ historique, sans la transformer en date de réforme. L'effet financier de demandes plus tardives reste à évaluer.",
    'material_reduction',
    "La source autorise une limite d'âge opposable aux demandes. La proposition interdit cette limite et rouvre la possibilité de déposer une demande après un refus pour ce seul motif ; elle ne rend pas les trimestres gratuits.",
    "Seuls les stages déjà éligibles et deux trimestres au maximum sont concernés. Ni les effets de ce rachat sur une pension donnée ni le coût pour la branche ne sont chiffrés ; la coordination de D351-16 reste nécessaire.",
    "Aucune charge nouvelle identifiée : même demande facultative, mêmes cotisations et même contrôle de l'éligibilité, sans déclaration, registre ou justificatif de remplacement de l'âge supprimé. Le volume de demandes peut augmenter, sans solde global chiffré.", p)
reduction(a, ["La limite supérieure d'âge à laquelle l'assuré peut demander la validation de ses périodes de stage est supprimée."])
effect(a, 'relief_extended', 'stages-retraite-fin-limite-age',
    "Ouverture du rachat des stages sans forclusion tenant à l'âge du demandeur.",
    "Demande soumise à un âge maximal fixé par décret, au moins vingt-cinq ans ; D351-16 fixe actuellement la fin de l'année des trente ans.",
    "Aucun âge maximal ; versement volontaire et plafond de deux trimestres maintenus.", 'legal_duty',
    "Assurés du régime général ayant accompli des stages entrant dans L351-17, y compris ceux dépassant l'âge limite antérieur.",
    "Demandes nouvelles et en cours à l'entrée en vigueur ; stages antérieurs éligibles inclus, sans révision des arrérages antérieurs pour ce seul motif.",
    "Aucune condition d'investissement, attestation d'âge ou déclaration de remplacement ; coût des droits supplémentaires non établi.",
    "1° L'âge jusqu'auquel l'assuré peut présenter une demande, qui ne peut être inférieur à vingt-cinq ans ;",
    "1° Les modalités de présentation de la demande, qui ne peut être soumise à une limite d'âge ;")


# L353-1 : supprimer l'exception au minimum, sans toucher à la pension de réversion.
p = replace_once(BY_NUMBER['L353-1']['source_xml'],
    " Toutefois, ce minimum n'est pas applicable aux pensions de réversion issues d'une pension dont le montant est inférieur au minimum prévu à l'article L. 351-9.", "")
p += "<p>L'exclusion du montant minimum en raison du faible montant de la pension dont est issue la pension de réversion ne s'applique plus aux arrérages dus pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsque la pension de réversion a déjà été liquidée. Cette suppression ne modifie ni la durée d'assurance servant au calcul du minimum ni les règles de ressources et de réduction prévues au présent article. Elle ne donne pas lieu à restitution ou à révision générale des arrérages dus pour des périodes antérieures.</p>"
a = base('L353-1',
    "Réforme de fond favorable : retrait de l'exception qui prive de minimum les pensions de réversion issues d'une très petite pension. Le minimum reste modulé selon la durée d'assurance et la pension reste soumise au plafond de ressources. Les droits dérivés de la seconde pension de cumul emploi-retraite et la majoration pour enfants sont conservés. La réversion est une prestation, non un impôt successoral à abroger.",
    "Le renvoi source à L351-9 est absent du corpus actif consultable ; son ancien seuil n'est ni reconstitué ni remplacé par un chiffre supposé. La proposition retire expressément toute cette exclusion, plutôt que de maintenir un renvoi dont la teneur n'est pas vérifiable localement. D353-1 et R353-1/2/6/7 lus : conserver le pourcentage de réversion, le minimum proratisé, les exclusions favorables de ressources, l'abattement d'activité et les dates d'effet. Le nouvel alinéa est ajouté après les quatre alinéas existants, sans déplacer les renvois au deuxième ou au quatrième. L161-22-1 et ses notes de 2027 lus : la réversion de la nouvelle pension garde les cohortes et exceptions applicables, sans généralisation rétroactive. Perte de la minoration d'aide et coût des compléments à chiffrer ; aucune taxe de remplacement.",
    'material_reduction',
    "La source écarte entièrement le minimum lorsque la pension initiale est sous le seuil visé. La proposition retire cette exclusion et permet le minimum proratisé aux bénéficiaires concernés, tout en conservant le plafond de ressources et son écrêtement.",
    "Ce n'est pas un minimum uniforme sans condition de durée ou de ressources. Le nombre de bénéficiaires de l'exception ancienne et le montant des compléments ne sont pas établis ; la teneur historique de L351-9 reste documentairement manquante.",
    "Aucune charge nouvelle identifiée pour le conjoint : aucun dossier ou justificatif supplémentaire, aucun nouvel âge ou plafond. Les caisses appliquent le minimum dans les liquidations et paiements concernés ; leur charge et la dépense supplémentaire ne sont pas chiffrées.", p)
reduction(a, ["L'exclusion du minimum de réversion pour les pensions issues d'une pension de faible montant, assortie du renvoi à L351-9, est supprimée."])
effect(a, 'relief_extended', 'reversion-minimum-fin-exclusion-petite-pension',
    "Suppression de l'exclusion du minimum de réversion liée au faible montant de la pension initiale.",
    "Minimum non applicable aux pensions de réversion issues d'une pension sous le minimum visé à L351-9 ; taux de réversion et ressources distincts.",
    "Minimum applicable aussi à ces pensions, calculé selon la durée d'assurance et toujours soumis à l'écrêtement de ressources ; aucun taux nouveau.", 'euro',
    "Conjoints survivants et bénéficiaires auxquels L353-1 est applicable, dont la pension de réversion subissait cette exclusion.",
    "Arrérages relatifs aux périodes à compter de l'entrée en vigueur, y compris pensions déjà liquidées ; pas de révision générale des périodes antérieures.",
    "Aucun prélèvement ni justificatif de remplacement ; dépense supplémentaire non chiffrée.",
    "Toutefois, ce minimum n'est pas applicable aux pensions de réversion issues d'une pension dont le montant est inférieur au minimum prévu à l'article L. 351-9.",
    "L'exclusion du montant minimum en raison du faible montant de la pension dont est issue la pension de réversion ne s'applique plus aux arrérages dus pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsque la pension de réversion a déjà été liquidée.")


base('L353-2',
    "Maintien intégral utile : la liquidation provisoire après disparition protège le conjoint sans attendre une preuve de décès ou un jugement d'absence définitif. Les deux situations, assuré déjà pensionné sans réclamation d'arrérages et assuré non pensionné, conservent leurs conditions propres. Le délai d'un an sert à caractériser la disparition prolongée et ne constitue pas une autorisation administrative d'emploi ou un impôt.",
    "R353-8 et R353-7 lus : le point de départ varie selon l'existence d'une pension, les pièces de disparition et les conséquences d'une réapparition gardent leur régime, avec la protection de L355-3. Pas de réduction improvisée du délai susceptible d'engendrer des restitutions au conjoint. La note citant L643-10 ne concorde pas avec l'article actuel lu, qui porte sur l'organisation des professions libérales ; L811-12 n'est pas présent au corpus actif. Ces mentions historiques ne sont pas transformées en renvois normatifs nouveaux ni présentées comme vérifiées dans leur ancien champ.",
    'retained_necessary',
    "La source entière est conservée : droit provisoire, deux hypothèses de disparition et transformation en droit définitif. Aucun prélèvement accessoire, agrément ou double déclaration n'est imposé par cet article.",
    "Le maintien n'établit pas que toutes les démarches de R353-8 sont optimales. La filiation des deux références historiques de la note reste incertaine ; elle ne ferme pas le droit principal au conjoint.",
    "Aucune charge nouvelle identifiée : aucun texte nouveau, aucun justificatif, registre ou délai ajouté ; la source demeure intégrale avec ses garanties et ses conditions existantes.")

base('L353-3',
    "Maintien intégral : l'assimilation du conjoint divorcé, le partage selon chaque durée de mariage, la majoration familiale et l'accroissement au décès d'un bénéficiaire sont des droits favorables et des règles nécessaires entre titulaires concurrents. Les supprimer au motif du décès retirerait une prestation au lieu de supprimer un droit de succession.",
    "Les quatre alinéas sont conservés à leur place ; le partage intervient à la première liquidation demandée. Les notes de la loi de 2003 conservent expressément l'allocation de veuvage antérieure, la réserve de ressources pour les pensions déjà servies, les dispositions d'âge et la charge de l'assurance vieillesse. Renvois à L353-1 et L351-12 examinés ; la réforme du minimum de L353-1 ne justifie ni un nouveau partage ni la fermeture des droits futurs des divorcés.",
    'retained_necessary',
    "Aucune modification de la source : les droits des conjoints et divorcés, les proportions et les majorations restent ouverts selon leurs conditions, sans création d'une nouvelle démarche distincte.",
    "Ce maintien ne supprime pas les justificatifs nécessaires au mariage et à sa durée. Aucun montant de pension ou coût national n'est déduit de l'existence du partage.",
    "Aucune charge nouvelle identifiée : aucun dossier supplémentaire ni condition de parenté, résidence ou notification ajouté aux règles de partage déjà applicables.")

base('L353-4',
    "Maintien intégral de l'avance de réversion : elle atténue l'attente de paiement dans la limite des droits établis. Son financement par l'action sanitaire et sociale et son remboursement par les fonds de prestations légales évitent de supprimer une aide de trésorerie au conjoint. L'article n'impose ni taxe ni autorisation au bénéficiaire.",
    "Ne pas assimiler le remboursement entre fonds à une dette nouvelle du conjoint. L'avance reste possible pour les futures demandes aussi ; aucun plafond chiffré, délai de paiement garanti ou avance automatique non décidé n'est créé. La limite des droits établis protège l'allocation des fonds et les autres assurés.",
    'retained_necessary',
    "La faculté d'avance existante demeure exactement. Il n'y a ici ni nouvelle baisse de prélèvement ni nouveau report de dette à comptabiliser : l'avantage de calendrier est déjà dans la source.",
    "Les critères de gestion de l'action sociale et les délais effectivement pratiqués ne sont pas établis par ce seul article ; aucune accélération chiffrée n'est revendiquée.",
    "Aucune charge nouvelle identifiée : la faculté existante et son financement sont conservés, sans obligation de registre, de rapport ou de pièces nouvelles.")

base('L353-5',
    "Maintien intégral de la majoration forfaitaire par enfant à charge. Les conditions d'âge, l'absence d'avantage personnel de vieillesse et le non-cumul avec une prestation de même objet définissent cette protection ciblée ; la réserve selon laquelle le dépassement de l'âge du titulaire ne supprime pas le droit est favorable et conservée. Ni le montant ni l'accès futur ne sont fermés.",
    "L161-1 et R353-9/10/11 lus : conserver enfants à charge, dates d'effet, information de changement familial, montant réglementaire et revalorisation. L161-23-1 lu avec sa proposition : distinguer la règle ordinaire et le dispositif temporaire visant seulement les pensions ; ne pas appliquer le gel à des prestations étrangères à son champ. L'extension explicite aux conjoints des L353-2 et L353-3 reste entière. Le non-cumul concerne la charge d'enfant du chef du même décès, non l'indemnité ordinaire de rupture.",
    'retained_necessary',
    "La majoration, sa revalorisation et ses extensions sont maintenues dans leur entier. L'examen ne révèle pas dans cet article un agrément ou une déclaration redondante à retirer sans redéfinir le financement d'une prestation.",
    "Ce maintien ne chiffre pas la majoration ni son incidence sur les prestations sous condition de ressources. Les règles réglementaires de notification restent distinctes du présent lot.",
    "Aucune charge nouvelle identifiée : aucun âge nouveau, aucun cumul défavorable supplémentaire et aucun justificatif de remplacement n'est introduit.")


# L353-6 : fin de l'obligation de liquider tous les droits pour obtenir la majoration.
p = replace_once(BY_NUMBER['L353-6']['source_xml'],
    "Le conjoint survivant ne peut bénéficier des dispositions du présent article que s'il a fait valoir les avantages personnels de retraite et de réversion auxquels il peut prétendre auprès des régimes légaux ou rendus légalement obligatoires, de base et complémentaires, français et étrangers, ainsi qu'auprès des organisations internationales.",
    "Le bénéfice de cette majoration n'est pas subordonné à la liquidation de l'ensemble des avantages personnels de retraite et de réversion auxquels le conjoint survivant peut prétendre. La seule absence de liquidation de l'un de ces avantages ne peut justifier le refus ou la suspension de la majoration, ni une demande de preuve de l'impossibilité de le liquider. Les avantages effectivement servis restent pris en compte dans les conditions du premier alinéa.")
p += "<p>La suppression de cette condition s'applique aux majorations dues pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsque la pension de réversion a été liquidée avant cette date. Elle ne remet pas en cause les garanties limitant la révision d'une majoration déjà attribuée. Les périodes antérieures, leurs créances, restitutions et recours conservent leur régime ; aucune restitution générale n'est instituée.</p>"
a = base('L353-6',
    "Réforme de fond : retirer la liquidation préalable obligatoire de tous les avantages français, étrangers et internationaux, ainsi que la preuve de l'impossibilité de liquider prévue en exécution. Une majoration de faible réversion ne doit pas contraindre son bénéficiaire à demander prématurément une autre pension. L'âge, le plafond, le pourcentage et l'écrêtement sur les avantages servis demeurent ; aucun taux nouveau n'est créé.",
    "R353-12/13/14, D353-4 et R173-17-1 lus intégralement. R353-14 doit perdre l'exigence de date d'entrée en jouissance de toutes les pensions et la preuve d'impossibilité, sans déclaration de remplacement. Conserver l'appréciation des montants servis, le plafond revalorisé et le taux de 11,1 %, la coordination entre régimes et les garanties de non-révision de R353-13 ; aucune donnée nouvelle ni nouveau répertoire n'est institué. L161-17-1-1, L173-1-1, L342-6 et L357-10-2 lus : la priorité entre majorations et les extensions de la majoration subsistent. Leur application ne doit pas rétablir l'exigence supprimée. Les règlements et le code rural restent à coordonner dans leurs champs propres ; coût de l'ouverture élargie non chiffré.",
    'material_reduction',
    "La source impose de faire valoir toutes les retraites avant la majoration. Cette obligation et son prolongement probatoire sont retirés ; l'avantage existant est accessible sans liquidation exhaustive, avec le même contrôle des avantages réellement servis.",
    "Le plafond et le montant de la majoration ne sont pas relevés. Les liquidations imposées pour d'autres prestations ne sont pas supprimées ; la dépense supplémentaire et l'adaptation réglementaire restent à établir.",
    "Aucune charge nouvelle identifiée : ni pension fictive à calculer, ni nouvelle attestation, ni déclaration annuelle de remplacement ; le contrôle des montants servis conserve son régime existant et les garanties de non-révision sont préservées.", p)
reduction(a, ["L'obligation de liquider l'ensemble des avantages de retraite et de réversion pour accéder à la majoration est supprimée.",
              "La preuve de l'impossibilité de liquider un avantage, exigée en exécution de cette condition, ne peut plus être demandée pour obtenir la majoration."])
effect(a, 'obligation_removed', 'reversion-majoration-fin-liquidation-exhaustive',
    "Retrait de la liquidation préalable de toutes les pensions pour l'accès à la majoration de réversion.",
    "Conjoint tenu d'avoir fait valoir ses avantages de tous régimes, de base et complémentaires, français, étrangers et internationaux.",
    "Absence de condition de liquidation exhaustive ; mêmes âge, plafond, pourcentage et réduction selon les avantages effectivement servis.", 'legal_duty',
    "Conjoints survivants éligibles à la majoration de L353-6 et bénéficiaires de ses extensions légales.",
    "Périodes à compter de l'entrée en vigueur, y compris pensions déjà liquidées ; garanties de non-révision et droits des périodes antérieures conservés.",
    "Aucune déclaration équivalente, pension théorique imputée ou preuve d'impossibilité de liquidation ne remplace la condition retirée.",
    "Le conjoint survivant ne peut bénéficier des dispositions du présent article que s'il a fait valoir les avantages personnels de retraite et de réversion auxquels il peut prétendre auprès des régimes légaux ou rendus légalement obligatoires, de base et complémentaires, français et étrangers, ainsi qu'auprès des organisations internationales.",
    "Le bénéfice de cette majoration n'est pas subordonné à la liquidation de l'ensemble des avantages personnels de retraite et de réversion auxquels le conjoint survivant peut prétendre.")

base('L355-1',
    "Maintien intégral de la majoration pour l'aide constante d'une tierce personne. Les conditions médicales du 3° de L341-4 et les deux voies d'accès des pensionnés d'invalidité ou de vieillesse pour inaptitude garantissent une aide essentielle à l'autonomie ; aucun prélèvement accessoire ou agrément d'activité n'est institué ici.",
    "L341-4 lu : le 3° vise l'impossibilité d'exercer une profession et le recours à une tierce personne pour les actes ordinaires de la vie. Les deux alinéas gardent leurs bornes d'âge et la possibilité de remplir ultérieurement les conditions. Supprimer ces conditions sans coordonner les autres aides d'autonomie modifierait l'articulation des prestations, ce qui n'est pas une économie démontrée. L357-7 conserve son extension propre aux pensions anciennes. Le gel temporaire des seules pensions de retraite ne doit pas être appliqué par analogie à la prestation d'invalidité.",
    'retained_necessary',
    "La majoration d'aide humaine et ses ouvertures futures sont intégralement préservées. La source ne comporte ni double formalité explicite ni cotisation indépendante dont la suppression serait démontrée.",
    "Les interactions avec les autres aides d'autonomie et les paramètres réglementaires d'âge ne sont pas recalibrés ; aucune baisse de coût ou extension de population non décidée n'est annoncée.",
    "Aucune charge nouvelle identifiée : les conditions médicales existantes restent les mêmes, sans dossier, donnée, registre ou délai nouveau.")


# L355-2 : suppression du privilège de saisie hospitalière, maintien des autres alinéas.
p = replace_once(BY_NUMBER['L355-2']['source_xml'],
    " Toutefois, elles le sont dans la limite de 90 % au profit des établissements hospitaliers et des caisses de sécurité sociale pour le paiement des frais d'hospitalisation.", "")
p += "<p>À compter de l'entrée en vigueur de la loi portant la présente rédaction, les cessions et saisies destinées au paiement de frais d'hospitalisation sont soumises aux conditions et limites applicables aux salaires, y compris pour les sommes non encore prélevées au titre d'une cession ou d'une saisie antérieure. La dérogation du quatrième alinéa demeure applicable dans son champ propre. Les dettes d'hospitalisation demeurent dues et peuvent être recouvrées dans ces limites. Les sommes régulièrement prélevées avant cette entrée en vigueur ne sont pas restituées de ce seul fait ; les droits à restitution des sommes indues et les recours sont préservés.</p>"
a = base('L355-2',
    "Réforme de fond : supprimer la dérogation permettant de saisir jusqu'à 90 % de la pension pour frais d'hospitalisation. La dette n'est pas effacée, mais son recouvrement rejoint le barème protecteur des salaires. Les garanties sur rappels et pension d'invalidité, ainsi que la réparation des victimes de crimes contre l'humanité et son minimum réservé, sont conservées intégralement.",
    "Les quatre alinéas initiaux restent en place, seule la deuxième phrase du premier étant retirée ; la transition s'ajoute après eux. Le renvoi au premier alinéa de L351-10 vise le minimum de pension, non son addition de majorations ni un salaire de rupture. La source a une fin de validité au 1er janvier 2029 ; l'acte et l'éventuel régime successeur de cette échéance ne sont pas fournis ici. La proposition n'affirme pas abroger cette échéance ni avoir réécrit le régime de 2029 : une coordination de la loi portant cette abrogation différée est à vérifier, sans rétablissement de la saisie à 90 %. Le barème des saisies de rémunérations et l'article 375 du CPP ne sont pas réécrits dans ce lot ; aucun pourcentage de saisie ordinaire n'est inventé.",
    'material_reduction',
    "Le pouvoir de prélever jusqu'à 90 % pour hospitalisation est retiré au profit des limites ordinaires. C'est un allègement de l'emprise du recouvrement sur les ressources du pensionné, sans réduction de la dette hospitalière ou d'un taux fiscal.",
    "Le montant effectivement laissé au débiteur dépend du barème ordinaire et de sa situation ; aucun gain uniforme n'est calculé. Le régime postérieur au 1er janvier 2029 n'est pas établi dans les sources fournies.",
    "Aucune charge nouvelle identifiée : ni demande d'autorisation ni déclaration remplaçante ; les créanciers appliquent les limites de saisie ordinaires déjà existantes, sous les garanties conservées.", p)
a['benefit_review'] = "Les limites de saisie assimilées aux salaires, le calcul par échéance des rappels, le plancher trimestriel d'invalidité égal au quart du minimum de L341-5 et la somme réservée égale au tiers du minimum de L351-10 sont intégralement conservés, pour les situations futures aussi. Le pouvoir de saisie à 90 % est un privilège de recouvrement des créanciers hospitaliers, non une exonération ou une dérogation allégeant une charge du pensionné ; sa suppression renforce sa protection sans éteindre la dette. La dérogation destinée à réparer les victimes de crimes contre l'humanité, avec son minimum protégé, demeure entière. Aucun avantage fiscal n'est fermé et aucun prélèvement de remplacement n'est créé."
reduction(a, ["Le pouvoir dérogatoire de céder ou saisir jusqu'à 90 % des pensions et rentes pour le paiement de frais d'hospitalisation est supprimé."])
effect(a, 'relief_extended', 'pensions-fin-saisie-hospitaliere-90-pourcent',
    "Extension des limites ordinaires de saisie aux créances d'hospitalisation.",
    "Pensions et rentes saisissables jusqu'à 90 % pour frais d'hospitalisation au profit des établissements hospitaliers et caisses de sécurité sociale.",
    "Même dette recouvrable dans les conditions et limites des salaires, sous les garanties particulières conservées ; aucun taux de dette réduit.", 'legal_duty',
    "Titulaires de pensions et rentes des titres et chapitres visés faisant l'objet d'une cession ou saisie pour frais d'hospitalisation.",
    "Sommes à prélever à compter de l'entrée en vigueur, y compris mesures en cours ; anciens prélèvements réguliers non remboursés de ce seul fait.",
    "Pas de formalité nouvelle ; maintien du principal de la dette, des recours et des autres pouvoirs de recouvrement légaux.",
    "Toutefois, elles le sont dans la limite de 90 % au profit des établissements hospitaliers et des caisses de sécurité sociale pour le paiement des frais d'hospitalisation.",
    "À compter de l'entrée en vigueur de la loi portant la présente rédaction, les cessions et saisies destinées au paiement de frais d'hospitalisation sont soumises aux conditions et limites applicables aux salaires, y compris pour les sommes non encore prélevées au titre d'une cession ou d'une saisie antérieure.")


# L355-3 : correction explicite du libellé d'un renvoi, sans couper la lutte contre la fraude.
p = replace_once(BY_NUMBER['L355-3']['source_xml'],
                 "à l'article aux articles L. 168-8 et L. 511-1", "aux articles L. 168-8 et L. 511-1")
a = base('L355-3',
    "Coordination nécessaire du renvoi matériellement corrompu « à l'article aux articles » vers L168-8 et L511-1, sans modification du champ des prestations saisies ni des conditions. Maintien intégral de la prescription biennale, des dispenses et remises favorables en cas d'erreur de caisse, du choix de remboursement, du contradictoire et des recours. L'indemnité de 10 % est ciblée sur une fraude du bénéficiaire : sa suppression, sans examen du dispositif antifraude, n'est pas retenue comme coupe d'une charge sans fonction essentielle.",
    "L133-4-1 entier, source et proposition, lus : ses quatrième à neuvième alinéas portent sur la rectification et la mise en recouvrement ; le renvoi final des quatrième à dernier alinéas maintient aussi l'encadrement réglementaire des notifications. Les six alinéas de L355-3 ne sont pas déplacés. Les douze mois sont un maximum laissé au décret pour l'option de versements, pas une année de préavis ni une prescription. Le L821-1 cité ici relève du CCH (aides personnelles au logement, texte lu), pas du CSS (AAH, cible fournie distincte). Ne pas déplacer ce renvoi de code. La référence ancienne au plafond AVTS sert une protection favorable ; elle n'est pas remplacée par un seuil supposé. Aucun nouveau renvoi n'est introduit.",
    'coordination_only',
    "Le seul changement est la rectification de la formulation du renvoi à deux articles déterminés. Le principal, la prescription, l'indemnité antifraude, les dispenses de remboursement et les voies de recouvrement sont identiques à la source entière.",
    "Aucune réduction de dette ni de démarche n'est démontrée. Le calcul des plafonds historiques AVTS et les modalités des autres codes restent à leur régime propre ; aucune cohérence générale de tous les dispositifs d'indus n'est prétendue.",
    "Aucune charge nouvelle identifiée : le renvoi ne crée ni prestation supplémentaire saisissable, ni délai, registre, donnée ou condition de remboursement nouvelle.", p)
effect(a, 'coordination', 'indus-vieillesse-renvoi-prestations-correction',
    "Correction du libellé du renvoi aux prestations de proche aidant et familiales.",
    "Renvoi source rédigé « à l'article aux articles L. 168-8 et L. 511-1 », sans ambiguïté sur les deux numéros mais grammaticalement corrompu.",
    "Renvoi explicite « aux articles L. 168-8 et L. 511-1 », sous les mêmes conditions de recouvrement et de recours.", 'other',
    "Bénéficiaires d'indus de vieillesse ou invalidité soumis aux retenues croisées prévues par L355-3.",
    "Coordination sans changement de créance, de période recouvrable ou d'option ; toutes les garanties existantes demeurent.",
    "Aucune obligation ou baisse supplémentaire comptée ; aucune donnée nouvelle demandée.",
    "à l'article aux articles L. 168-8 et L. 511-1", "aux articles L. 168-8 et L. 511-1")


# L356-1 : suppression du délai de forclusion et correction du maintien de qualité d'assuré.
p = replace_once(BY_NUMBER['L356-1']['source_xml'],
    "ou qui bénéficiait, en application de l'article L. 311-5, des prestations en nature de l'assurance maladie du régime général",
    "ou qui conservait, en application de l'article L. 311-5, la qualité d'assuré du régime général")
p = replace_once(p, "décret.L'allocation", "décret. L'allocation")
p = replace_once(p,
    "Ce décret détermine aussi le délai dans lequel le conjoint survivant demande l'attribution de cette prestation postérieurement à la date du décès de l'assuré.",
    "Aucun délai de forclusion à compter du décès ne peut être opposé à la demande d'attribution de cette prestation. La demande demeure soumise aux prescriptions applicables aux arrérages ; elle ne prolonge pas la période pendant laquelle l'allocation est due.")
p += "<p>La suppression du délai de forclusion s'applique aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente rédaction et aux demandes en cours à cette date, y compris pour un décès antérieur. Un refus fondé sur ce seul délai ne fait pas obstacle à une nouvelle demande pour les arrérages non prescrits ; les décisions juridictionnelles passées en force de chose jugée sont préservées. Les conditions de ressources et leurs exclusions, les conditions d'âge et de résidence, les règles de séjour, les dates d'effet et les durées de service, y compris les prolongations favorables, restent applicables. Aucune nouvelle période de versement ne commence du seul fait du dépôt tardif de la demande.</p>"
a = base('L356-1',
    "Réforme de fond : suppression de la forclusion de la demande d'allocation veuvage, distincte de la durée temporaire de service et de la prescription des arrérages. Les ressources, exclusions de revenus professionnels et de formation, ouvertures hors de France pour l'assurance volontaire et droit des conjoints d'allocataires handicapés restent entiers. Coordination du renvoi à L311-5 : la source parle encore de prestations en nature, alors que la cible actuelle maintient la qualité d'assuré et des droits en espèces ; le droit de veuvage est rattaché à cette qualité pour ne pas devenir inopérant.",
    "D356-1 à D356-13 lus intégralement : retirer le dernier alinéa de D356-2 sur la recevabilité dans la période maximale de D356-5, et coordonner la réserve finale de D356-12 ; préserver les deux ans de service, la prolongation de cinquante à cinquante-cinq ans, les dates d'effet de D356-6 et les exonérations de ressources de D356-3, notamment les abattements 100 % puis 50 % et le dispositif créateurs/repreneurs. Ces articles réglementaires ne sont pas réécrits ici. Le présent texte n'invente aucun délai de prescription : l'identification de tous les fondements applicables aux arrérages et des effets d'un jugement demeure à coordonner avec les textes civils et procéduraux extérieurs au lot. Aucun titre de séjour supplémentaire n'est créé ; les données déjà légalement détenues ne doivent pas être redemandées selon le droit existant, sans gain CRPA nouveau compté. Le renvoi L311-5 n'assimile ni chômage, ni formation, ni emploi public à un nouveau CDD.",
    'material_reduction',
    "La source habilite un décret à enfermer la demande dans un délai après le décès ; la proposition interdit cette forclusion tout en laissant la période indemnisable et les prescriptions à leur régime propre. Une coordination supplémentaire évite de faire dépendre le droit d'un maintien de prestations en nature qui n'est plus celui de L311-5 actuel.",
    "Ce n'est ni une allocation perpétuelle ni une suppression des ressources ou des conditions d'affiliation. Le droit aux arrérages dépend encore de leurs prescriptions ; le coût des demandes recevables supplémentaires et l'effet exact sur les cohortes de maintien d'assurance ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : la demande demeure celle d'allocation veuvage, sans déclaration de remplacement de la forclusion ni nouveau justificatif de chômage. Le traitement de demandes tardives peut accroître l'activité des caisses, dont le coût n'est pas établi.", p)
reduction(a, ["Le délai de forclusion après le décès qui conditionne la recevabilité de la demande d'allocation de veuvage est supprimé."])
effect(a, 'obligation_removed', 'veuvage-fin-forclusion-demande',
    "Suppression de l'obligation de demander l'allocation dans un délai maximal après le décès.",
    "Délai postérieur au décès fixé par décret ; D356-2 lie la recevabilité à la période maximale de versement.",
    "Aucun délai de forclusion propre à la demande ; prescription des arrérages, dates d'effet et durée maximale de service conservées.", 'legal_duty',
    "Conjoints survivants remplissant les autres conditions de l'allocation veuvage, y compris les demandes tardives.",
    "Demandes nouvelles ou pendantes à l'entrée en vigueur, même pour décès antérieur ; arrérages prescrits et décisions juridictionnelles définitives non rouverts.",
    "Aucun délai ou titre de remplacement ; aucune nouvelle période indemnisable créée par une demande tardive.",
    "Ce décret détermine aussi le délai dans lequel le conjoint survivant demande l'attribution de cette prestation postérieurement à la date du décès de l'assuré.",
    "Aucun délai de forclusion à compter du décès ne peut être opposé à la demande d'attribution de cette prestation.")
effect(a, 'coordination', 'veuvage-maintien-qualite-assure',
    "Coordination de l'ouverture du veuvage avec le maintien de qualité d'assuré de L311-5.",
    "L356-1 vise des prestations en nature attribuées en application de L311-5, qui vise désormais le maintien de qualité d'assuré et des droits en espèces.",
    "L356-1 vise la qualité d'assuré conservée en application de L311-5, sans inventer une condition de durée d'emploi ou de rupture.", 'other',
    "Conjoints survivants des assurés relevant du maintien prévu à L311-5.",
    "Les règles de maintien et les périodes particulières propres à L311-5 ne sont pas changées ; aucune nouvelle liquidation de contrat n'est exigée.",
    "Aucune nouvelle preuve, déclaration ou modification des procédures collectives ; incidence de la coordination non chiffrée.",
    "ou qui bénéficiait, en application de l'article L. 311-5, des prestations en nature de l'assurance maladie du régime général",
    "ou qui conservait, en application de l'article L. 311-5, la qualité d'assuré du régime général")

base('L356-2',
    "Maintien intégral : le caractère temporaire, le montant unique revalorisé et les modalités plus favorables liées à l'âge au décès organisent l'allocation veuvage. Retirer l'allocation pour réduire son coût contredirait la préservation des avantages ; supprimer son caractère temporaire redéfinirait une prestation distincte de la réversion, sans financement établi.",
    "D356-5 et D356-7 lus avec L161-23-1 et L161-25. Les deux ans et la prolongation jusqu'à cinquante-cinq ans sous condition d'âge au décès restent des règles de durée de prestation, sans durée d'emploi. La proposition de L161-23-1 II exclut expressément les prestations autres que pensions de vieillesse et réversion : le renvoi de revalorisation de l'allocation ne la soumet donc pas au gel temporaire des pensions. La suppression de la forclusion de L356-1 ne prolonge pas ce service.",
    'retained_necessary',
    "La protection temporaire et son régime plus favorable selon l'âge demeurent inchangés. Le renvoi assure sa revalorisation sans créer un nouveau gain matériel dans cet article.",
    "Aucun nouveau montant ou durée de versement n'est proposé et aucun gain de prestations n'est chiffré ; les interactions avec la réversion continuent de relever de leurs conditions propres.",
    "Aucune charge nouvelle identifiée : le maintien ne crée ni délai, ni justificatif, ni condition d'emploi ni reporting supplémentaire.")


# L356-3 : fin de l'exclusion liée à une nouvelle union, sans nouveau test de ménage.
p = replace_once(BY_NUMBER['L356-3']['source_xml'],
    "1° Se remarie, conclut un pacte civil de solidarité ou vit en concubinage ;",
    "1° Abrogé ;")
p += "<p>Le remariage, la conclusion d'un pacte civil de solidarité ou le concubinage ne peuvent, à eux seuls, faire obstacle à l'attribution, au maintien ou au rétablissement de l'allocation de veuvage. Cette règle s'applique aux périodes courant à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsque le décès ou la nouvelle union est antérieur. Le rétablissement n'ouvre pas une nouvelle période de service et ne prolonge pas la durée pendant laquelle l'allocation est due. Les conditions de l'article L. 356-1, les exclusions et abattements favorables de ressources et les prescriptions applicables restent inchangés. Les périodes antérieures et les décisions juridictionnelles passées en force de chose jugée conservent leur régime.</p>"
a = base('L356-3',
    "Réforme de fond favorable : retrait de l'exclusion automatique pour remariage, PACS ou concubinage. L'âge, les ressources personnelles et la durée temporaire restent des conditions suffisantes pour cibler cette aide de transition ; une nouvelle union ne doit pas à elle seule l'éteindre. Le 1° est laissé à sa place comme abrogé et le 2° maintient le renvoi aux autres conditions, sans remplacer l'exclusion par un nouveau test des ressources du couple.",
    "Coordonner D356-2 4°, D356-11 2° et D356-12 2°, tous lus, pour que l'exclusion de vie en couple et ses effets ne soient pas rétablis par règlement. Conserver les conditions et les autres causes d'interruption, ainsi que la période maximale de D356-5 et les abattements de D356-3. La transition couvre l'avenir des décès et unions antérieurs sans prolonger la période de service ni créer de remboursement des périodes antérieures. Les règles d'information de changement ne peuvent exiger sur ce seul fondement la preuve négative de l'absence d'une union désormais indifférente ; les changements de ressources dus demeurent déclarés. Dépense supplémentaire et articulation avec les autres prestations à évaluer, sans recette de compensation inventée.",
    'material_reduction',
    "Le 1° de la source ferme le droit dès une nouvelle union, indépendamment des ressources. Cette exclusion est supprimée ; le droit devient accessible ou maintenu pendant la période restant à courir, sous les autres conditions existantes.",
    "Le montant, les plafonds de ressources personnelles et la durée maximale ne sont pas relevés. L'effet budgétaire et les interactions avec les autres aides ne sont pas établis ; les règlements visés restent à coordonner.",
    "Aucune charge nouvelle identifiée : aucun agrément, déclaration d'union ou examen des ressources du nouveau partenaire n'est créé en remplacement ; les changements de ressources personnelles continuent de relever des règles existantes.", p)
reduction(a, ["La condition d'absence de remariage, de pacte civil de solidarité ou de concubinage pour l'attribution et le maintien de l'allocation de veuvage est supprimée."])
effect(a, 'relief_extended', 'veuvage-fin-exclusion-nouvelle-union',
    "Ouverture et maintien de l'allocation veuvage malgré une nouvelle union.",
    "Droit refusé ou éteint en cas de remariage, PACS ou concubinage, même si les autres conditions demeurent remplies.",
    "Nouvelle union sans effet d'exclusion à elle seule ; conditions de ressources personnelles, âge et période de service inchangées.", 'legal_duty',
    "Conjoints survivants éligibles à l'allocation veuvage ayant formé ou formant une nouvelle union.",
    "Périodes à compter de l'entrée en vigueur, même pour unions et décès antérieurs, sans nouvelle période de service ni rétroactivité générale.",
    "Aucun nouveau test des revenus du ménage ou justificatif d'absence de vie de couple ; conséquences budgétaires non chiffrées.",
    "1° Se remarie, conclut un pacte civil de solidarité ou vit en concubinage ;",
    "Le remariage, la conclusion d'un pacte civil de solidarité ou le concubinage ne peuvent, à eux seuls, faire obstacle à l'attribution, au maintien ou au rétablissement de l'allocation de veuvage.")


# L356-4 : la succession institutionnelle est rendue explicite, sans nouvel accès aux données.
p = replace_once(BY_NUMBER['L356-4']['source_xml'],
    "les associations pour l'emploi dans l'industrie et le commerce", "l'opérateur France Travail")
a = base('L356-4',
    "Coordination institutionnelle du circuit de ressources : le détenteur actuel France Travail remplace la désignation historique des associations pour l'emploi dans l'industrie et le commerce. L'accès reste limité aux ressources et prestations des bénéficiaires, sur demande de la caisse, avec le secret professionnel. Aucun nouveau registre, échange systématique ou demande de justificatif au bénéficiaire n'est instauré.",
    "L5312-1 du code du travail lu intégralement dans le corpus autorisé, avec ses notes : l'opérateur France Travail assure notamment le service des allocations pour l'assurance chômage et l'État. Aucun nouveau renvoi numéroté à cet article n'est ajouté au texte. La modification ne donne pas accès à des données supplémentaires détenues pour d'autres missions et ne modifie pas les bases légales de transmission ou les garanties de protection des données. La réutilisation d'informations déjà légalement disponibles est déjà encadrée par le droit existant ; aucun gain nouveau CRPA n'est compté. Les anciennes informations régulièrement obtenues et leurs obligations de secret restent protégées.",
    'coordination_only',
    "Seule la dénomination du détenteur des données est actualisée. La source autorise déjà la communication ciblée et impose le secret ; aucune seconde collecte ou formalité supprimée n'est démontrée.",
    "L'efficacité réelle des échanges, leur fréquence et les coûts ne sont pas mesurés. La coordination ne constitue pas une habilitation générale à croiser les fichiers de France Travail.",
    "Aucune charge nouvelle identifiée : ni donnée supplémentaire, ni destinataire nouveau quant à la fonction visée, ni registre, rapport ou condition d'allocation nouvelle ; l'obligation fonctionnelle de communication existait déjà.", p)
effect(a, 'coordination', 'veuvage-ressources-detention-france-travail',
    "Actualisation de la désignation du détenteur des données d'indemnisation chômage.",
    "Communication des informations de ressources détenues par les anciennes associations pour l'emploi dans l'industrie et le commerce.",
    "Même communication ciblée par France Travail pour les données qu'il détient, sans extension à ses autres données ou missions.", 'other',
    "Organisme débiteur de l'allocation veuvage et bénéficiaires dont les ressources sont vérifiées.",
    "Actualisation des communications futures ; secret et légalité des données antérieures préservés, sans nouveau dépôt.",
    "Aucune simplification matérielle nouvelle comptée ; aucune collecte ou transmission périodique générale ajoutée.",
    "les associations pour l'emploi dans l'industrie et le commerce", "l'opérateur France Travail")

base('L356-5',
    "Maintien intégral de l'habilitation réglementaire nécessaire au service de l'assurance veuvage. Cet article ne crée aucune demande, autorisation ou prélèvement autonome ; l'abroger fragiliserait les règles qui rendent l'allocation et ses avantages effectifs.",
    "L'habilitation est subordonnée aux règles législatives nouvelles de L356-1 et L356-3 : aucun décret ne peut rétablir leur forclusion ou l'exclusion liée à une union. D356-1 à D356-13 ont été lus ; les modifications nécessaires sont identifiées dans les notes de ces deux articles, sans prétendre que ce maintien les réalise. Le renvoi porte sur tout le chapitre, non sur un contrat de travail.",
    'retained_necessary',
    "L'habilitation demeure exactement. Elle est un support d'exécution des droits et non une obligation supplémentaire individuelle qu'on pourrait supprimer isolément.",
    "Ce maintien ne valide pas globalement toutes les obligations réglementaires ; la coordination détaillée des articles D356 signalés reste à effectuer hors du lot assigné.",
    "Aucune charge nouvelle identifiée : aucun nouveau décret imposé, registre, donnée, délai ou condition ajouté par le maintien de cette phrase.")

base('L357-1',
    "Maintien intégral de la faculté de calcul des pensions locales anciennes selon L357-2, L357-5 et L357-9. L'ancienneté des lois de 1911 et la date du 1er juillet 1946 n'établissent pas l'extinction des créances, des révisions ou des droits dérivés ; supprimer le texte pourrait retirer une option favorable.",
    "Les trois articles de calcul sont dans le présent lot et examinés. Les pensions de vieillesse, invalidité, veufs et veuves et les trois départements restent expressément couverts. Aucun rattachement automatique du régime local à la nouvelle capitalisation des salariés privés n'est créé par cette faculté. Les sources locales de 1911 ne figurent pas intégralement dans le corpus ; leur contenu non reproduit n'est pas reconstitué.",
    'retained_necessary',
    "La faculté de calcul favorable et ses trois renvois cohérents sont intégralement maintenus. La source ne prévoit ni taxe accessoire ni autorisation ou déclaration distincte.",
    "Les effectifs encore concernés et les montants différentiels entre les régimes ne sont pas connus. Le maintien n'affirme pas avoir relu les lois locales de 1911 absentes du corpus.",
    "Aucune charge nouvelle identifiée : aucun changement de caisse, financement, dossier ou condition de calcul n'est imposé aux titulaires.")

base('L357-2',
    "Maintien intégral du calcul de la pension locale, somme de base et majorations contributives, avec sa minoration entre les âges réglementaires. Ce calcul ouvre un droit et n'impose pas une nouvelle cotisation. La suppression isolée de la minoration reviendrait à changer les paramètres de départ du régime local sans décision de coordination des retraites ; les dispenses favorables sont conservées.",
    "D357-8 lu intégralement : maintien de la non-application de la réduction aux mères réunissant les conditions précises de trente années d'assurance, trois enfants et travail manuel ouvrier. Ne pas généraliser cette dispense à tous ni la fermer aux situations futures qui entrent encore dans le champ légal. Aucun âge, coefficient ou salaire de référence n'est inventé ; les renvois à cet article depuis L357-5 et L357-10 restent opérants.",
    'retained_necessary',
    "Le montant de base, les majorations et les conditions de minoration sont inchangés, ainsi que la possibilité de dispense réglementaire signalée en note. Aucune baisse de prélèvement n'est revendiquée pour ce calcul de pension.",
    "Les coefficients et âges réglementaires complets ne sont pas réécrits. Ni le coût actuariel d'une suppression de décote ni une réforme autonome d'âge de ce régime n'est établi.",
    "Aucune charge nouvelle identifiée : aucune cotisation, attestation, déclaration ou durée minimale nouvelle n'est ajoutée à la source.")

base('L357-3',
    "Maintien intégral du renvoi favorable aux majorations pour enfants et pour conjoint à charge des pensions locales. Il ne s'agit ni d'un doublon administratif ni d'une taxe ; la brièveté du renvoi ne justifie pas de supprimer l'accès aux avantages qu'il étend.",
    "L351-12, L351-13 et L357-15 lus intégralement. Le renvoi est limité au premier alinéa de L351-13 ; ne pas y substituer tout cet article et importer implicitement la fermeture du troisième alinéa de 2011 dans un champ local sans examen. La réserve de L357-15 sur la pension la plus élevée demeure, sans perte de la seconde pension. Les majorations familiales et les protections liées aux décisions pénales de L351-12 gardent leur champ, sans droit nouveau arbitraire ni fermeture pour les futures situations localement éligibles.",
    'retained_necessary',
    "Les deux extensions de majoration restent intégrales et dans les subdivisions exactes visées. Aucun nouveau gain de prestation n'est compté, puisque le fondement favorable existe déjà dans la source.",
    "L'articulation historique précise de la majoration locale pour conjoint à charge avec la fermeture de droit commun de 2011 n'est pas tranchée au-delà du renvoi source limité ; aucune nouvelle restriction n'est posée.",
    "Aucune charge nouvelle identifiée : aucun nouveau dossier familial, justificatif annuel ou cumul défavorable supplémentaire n'est institué.")

base('L357-4',
    "Maintien intégral des extensions au régime local : règles générales de pension, majorations de solidarité, taux plein, retraite progressive et cumul emploi-retraite. Elles assurent l'accès à des droits et leurs adaptations ; les fusionner dans une reformulation n'enlèverait aucune charge et risquerait de fermer des dérogations favorables.",
    "Les quatre alinéas et la borne des pensions prenant effet après le 31 août 2003 restent en place. L351-4-1, L351-6, L351-7-1, L351-8 et L161-22-1-6 à -8 lus en plus des cibles fournies. Le renvoi à L351-5 conserve le congé parental privé actuel et l'ancienne référence publique ; celui à L351-1 n'étend le transfert de cotisations qu'au champ privé expressément défini, sous financement préalable. L161-22 comporte une transition 2027 et une exception de première pension antérieure : ce renvoi ne les avance pas. L'indemnité de départ à la retraite visée par la retraite progressive est distincte de L1234-9. Aucun préavis privé de quinze jours n'est imposé aux fonctionnaires par cet article.",
    'retained_necessary',
    "La source reste entière avec ses renvois de droits et leurs conditions propres. Aucun prélèvement ou formalité nouvelle n'est supprimé par la seule application de ces droits aux assurés du régime local.",
    "Les adaptations réglementaires et les codes publics ou agricoles extérieurs au lot ne sont pas réécrits. Le maintien n'évalue pas le financement du raccordement à la capitalisation et ne présume pas les conditions remplies.",
    "Aucune charge nouvelle identifiée : pas de nouvelle catégorie assujettie, de durée d'emploi, de notification ou de déclaration créée ; les champs privés et publics restent distincts.")

base('L357-5',
    "Maintien intégral de la pension locale d'invalidité et de sa substitution par la pension de vieillesse à l'âge applicable. Il s'agit d'une continuité de protection, non d'une obligation accessoire de travail ou d'une double cotisation ; supprimer l'article retirerait le fondement du paiement.",
    "Le renvoi porte sur la pension du premier alinéa de L357-2 et sur l'âge fixé en application de ce même article ; aucune substitution par l'âge du contrat unique ou un taux supposé n'est effectuée. Le minimum distinct de L357-8 et l'extension de tierce personne de L357-7 restent disponibles. Pas de prétendue extinction des pensions anciennes faute d'effectifs connus.",
    'retained_necessary',
    "La fraction de pension d'invalidité et le passage au droit vieillesse sont inchangés. Aucun gain de prélèvement ni suppression de démarche ne peut être attribué à ce maintien.",
    "Le montant réglementaire de la fraction et les droits individuels ne sont pas recalculés ; la continuité maintenue n'est pas une validation actuarielle du régime.",
    "Aucune charge nouvelle identifiée : aucune demande de substitution, donnée ou condition d'âge supplémentaire n'est créée.")

base('L357-7',
    "Maintien intégral de l'extension de la majoration pour tierce personne aux pensions locales d'invalidité liquidées sous le régime antérieur au 1er juillet 1946. L'ancienneté du champ n'autorise pas à éteindre un droit d'aide humaine susceptible d'être exercé lorsque les conditions médicales sont remplies.",
    "L355-1 et le 3° de L341-4 lus : le besoin d'assistance dans les actes ordinaires de la vie reste la condition matérielle ; aucune autorisation d'emploi ou condition de contrat privé ne s'y ajoute. Le maintien vaut pour les demandes futures dans la cohorte légalement définie et pour les droits antérieurs, sans prétendre ouvrir de nouvelles affiliations au régime ancien.",
    'retained_necessary',
    "L'extension favorable est conservée mot pour mot et ne fait pas l'objet d'une fausse réécriture. Aucun prélèvement ni formalité administrative distincte n'apparaît dans la source.",
    "L'effectif des titulaires historiques n'est pas établi. Aucun montant d'économie ou coût de la tierce personne n'est extrapolé de leur ancienneté.",
    "Aucune charge nouvelle identifiée : le droit médical existant est maintenu sans justificatif périodique, registre ou procédure supplémentaire.")

base('L357-8',
    "Maintien intégral du plancher de pension d'invalidité locale pour les titulaires non couverts par L357-19. La réserve d'incapacité pour les pensions de la loi de 1911 reste une condition de fond de ce droit ; aucune formalité redondante n'est identifiée dans la phrase. Supprimer le minimum serait contraire à la conservation des avantages.",
    "L341-5 et L357-19 lus : le minimum d'invalidité est fixé par décret et le régime de L357-19 couvre une autre articulation avec les droits vieillesse. Le texte ne donne pas la valeur du taux d'incapacité : elle n'est pas remplacée par un chiffre inventé. L'article 1255 du code local n'est pas fourni intégralement dans le corpus autorisé ; son mode d'appréciation n'est pas reconstitué, et le renvoi est maintenu sans prétendre sa vérification historique complète.",
    'retained_necessary',
    "Le minimum annuel et son champ subsidiaire restent entiers. La source ne prévoit pas de cotisation nouvelle à supprimer et le renvoi à un taux ne permet pas de revendiquer une baisse chiffrée.",
    "La formule locale et l'article 1255 extérieur au corpus ne sont pas audités. Les populations encore couvertes et le coût de ce plancher ne sont pas établis.",
    "Aucune charge nouvelle identifiée : aucun seuil, examen médical, document ou renouvellement nouveau n'est introduit par le maintien.")

base('L357-9',
    "Maintien intégral des pensions de veuves et veufs locales, de leur assiette sur la pension du défunt et du pourcentage plus élevé dans le code local que dans la loi de 1911. La période de stage mentionnée est une condition d'assurance, non une formation ou un terme d'emploi qu'il faudrait convertir en contrat unique.",
    "Les deux alinéas conservent la différence entre une pension déjà perçue et celle dont le défunt aurait bénéficié, avec le stage exigé dans ce dernier cas. Aucun pourcentage non donné dans la source n'est inventé. L357-1 et L357-10 restent cohérents pour le calcul, le minimum et les majorations. Les lois locales de 1911 non fournies intégralement ne sont pas déclarées réécrites ; l'abolition des droits fiscaux au décès ne retire aucune de ces pensions.",
    'retained_necessary',
    "Le droit dérivé et le pourcentage local favorable restent intégralement maintenus. Ni la cotisation du défunt ni un impôt successoral ne sont modifiés par cet article de prestation.",
    "Les fractions réglementaires et les périodes de stage ne sont pas quantifiées dans cette source. Aucun effet financier total ou suppression de condition contributive n'est affirmé.",
    "Aucune charge nouvelle identifiée : aucun terme d'emploi, âge, durée d'affiliation, déclaration ou justificatif nouveau n'est ajouté.")

base('L357-10',
    "Maintien intégral du minimum des pensions de veufs et veuves et de la majoration familiale, calculée si nécessaire sur la pension portée au minimum. La réserve pour les pensions attribuées sans justification d'invalidité et leur accès ultérieur selon l'âge ou l'inaptitude restent dans leur champ propre ; aucun droit favorable n'est fermé pour l'avenir.",
    "Les trois alinéas et leurs renvois sont maintenus : L353-1 deuxième alinéa définit toujours le minimum, y compris après le retrait de sa seule exception relative aux petites pensions ; L351-12 garde la majoration familiale ; L357-2 garde l'âge local. Le présent minimum local était déjà formulé de façon autonome et n'est pas compté comme une seconde extension de la mesure portant sur L353-1. Les pensions sans justification d'invalidité conservent leur droit différé et l'exception plus favorable pour inaptitude, sans importation des seuils d'ancienneté du licenciement.",
    'retained_necessary',
    "Le minimum, sa majoration et l'accès différé favorable restent intégraux dans le texte source. Le renvoi de montant demeure au même alinéa, sans nouvelle diminution ou extension comptée ici.",
    "Le nombre de pensions concernées et leurs dates individuelles d'ouverture ne sont pas connus. Les âges et montants réglementaires ne sont pas recalibrés dans ce lot.",
    "Aucune charge nouvelle identifiée : aucun certificat, renouvellement, nouveau seuil d'invalidité ou démarche annuelle n'est créé.")


# Analyses spécifiques des seules cibles requises par reference-targets.json.
CHECKS = {
 'L351-17': {
  'L1234-1': "L351-17 traite du rachat de stages d'étudiants, non d'un licenciement : il ne renvoie pas à L1234-1. Les quinze jours calendaires des nouveaux contrats, leur notification et les anciens préavis restent sans effet sur la durée de stage validable ou sur la demande de rachat.",
  'L1221-2': "Le stage visé relève du code de l'éducation, avec gratification et deux trimestres au plus ; il n'est pas transformé par cet article en emploi à terme. Le contrat unique de la cible vise les nouvelles relations de travail privées et préserve les anciens contrats ; la fin du stage ne peut servir à rétablir un CDD.",
  'L1234-9': "La cotisation facultative de validation et le décompte des trimestres ne sont pas l'indemnité ordinaire de rupture. Le seuil d'un an au terme effectif préavis inclus, les 0,20 mois par année totale avec mois complets et le plafond de six mois ne s'appliquent donc pas à ce rachat.",
  'L351-14-1': "Le dernier alinéa de L351-17 déduit les trimestres versés du contingent ouvrant le montant abaissé au II de L351-14-1. Ce II, son champ de formation initiale et sa borne d'âge distincte restent inchangés ; la suppression de l'âge de demande des stages n'ajoute ni double validation ni nouveau plafond de rachat. La proposition de la cible retire seulement la catégorie d'établissement par arrêté."
 },
 'L355-2': {
  'L1234-1': "L'assimilation des pensions aux salaires concerne ici la cession et la saisie, pas la durée du préavis de licenciement. La cible propose quinze jours calendaires pour les nouveaux contrats en conservant l'ancien régime ; aucune durée d'ancienneté ou de notification n'est importée dans le calcul des quotités de saisie.",
  'L1221-2': "Le mot salaires ne renvoie pas à la forme du contrat de travail. Le contrat unique de la cible et la préservation des anciens CDD n'altèrent ni les pensions du titre IV ni celles des chapitres 1 à 4 du titre V ; aucune cessation automatique d'emploi n'est créée pour les pensionnés.",
  'L1234-9': "La pension saisie et ses rappels ne sont pas l'indemnité ordinaire de licenciement de L1234-9. Le seuil d'un an mesuré préavis inclus, le calcul sur toute l'ancienneté et le plafond de six mois sont inapplicables aux minima insaisissables ; les indemnités spéciales gardent leur propre régime.",
  'L351-10': "Le dernier alinéa réserve un tiers du minimum visé au premier alinéa de L351-10 pour la saisie liée aux crimes contre l'humanité. Ce premier alinéa contient le minimum et son minimum majoré, distincts des accessoires des alinéas suivants : le texte source ne choisit pas expressément entre ces deux montants. Cette précision de liquidation reste à contrôler, sans modifier le renvoi ni la somme réservée lors de la suppression du privilège hospitalier."
 },
 'L355-3': {
  'L1234-1': "Les délais de cet article concernent la prescription et le choix de remboursement d'indus, non la notification d'une rupture. La durée de quinze jours de L1234-1 proposée pour les nouveaux contrats, et les anciens préavis selon ancienneté, ne réduisent ni la prescription biennale ni le délai maximal de douze mois visé ici.",
  'L1221-2': "Le recouvrement porte sur des prestations de vieillesse et invalidité, quelle que soit la forme d'un ancien emploi. La proposition de contrat unique ne supprime pas leurs conditions de ressources ou de bonne foi et ne fait pas d'un remboursement échelonné une relation de travail à durée déterminée.",
  'L1234-9': "Les sommes réclamées sont des indus et, seulement en cas de fraude, une indemnité de 10 % pour frais ; elles ne relèvent pas du barème de rupture de L1234-9. Aucun seuil d'un an, préavis inclus, ni plafond de six mois de salaire ne peut limiter les dispenses ou le recouvrement ici prévus.",
  'L168-8': "Le cinquième alinéa vise réellement l'allocation journalière du proche aidant de L168-8, ouverte aux salariés, aux personnes de L544-8 et aux agents publics. La correction du libellé ne retire ni accord de l'organisme ni absence d'indu concurrent ni garanties de L133-4-1 ; elle n'assimile pas les agents publics à un contrat privé.",
  'L133-4-1': "Les quatrième à neuvième alinéas, tant dans la source que dans la proposition de la cible, organisent rectification, observations et bornes de recouvrement. Le renvoi final aux quatrième à dernier alinéas comprend aussi les mentions réglementaires de notification. L'accord de l'organisme, le choix de versements dans le délai fixé et l'absence d'indu sur la prestation retenue sont conservés.",
  'L821-1': "La cible fournie est L821-1 du CSS sur l'AAH, mais le renvoi écrit dans L355-3 est L821-1 du code de la construction et de l'habitation, sur les aides personnelles au logement. La cible CSS n'est donc pas substituable : son droit au complément d'AAH et ses exceptions européennes ne sont ni supprimés ni transformés en règle de contrat privé. Le texte CCH a été lu séparément dans le corpus."
 },
 'L356-1': {
  'L1234-1': "L'allocation veuvage dépend du décès et de conditions d'assurance, âge et ressources, non d'un préavis de rupture. Les quinze jours calendaires et la notification écrite du contrat unique restent étrangers au délai de demande de l'allocation supprimé ici ; les droits des anciens contrats ne sont pas modifiés.",
  'L1221-2': "Les rémunérations d'activité et de stage de formation peuvent rester exclues des ressources sans condition de CDD. La cible impose un emploi privé nouveau à durée indéterminée, même pendant une formation limitée ; l'allocation et ses abattements restent ouverts aux futures situations éligibles et ne recréent pas de contrat à terme.",
  'L1234-9': "Le droit au veuvage n'est pas une indemnité ordinaire patronale. Ni l'absence d'indemnité avant un an, ni les 0,20 mois par année totale au terme préavis inclus, ni le plafond de six mois ne définissent ici l'affiliation ou les ressources ; les prestations et indemnités spéciales conservent leurs règles propres.",
  'L311-5': "La source de L356-1 parle des prestations en nature alors que L311-5 actuel conserve la qualité d'assuré et les droits en espèces pour les bénéficiaires d'allocations, les reprises insuffisantes et les autres situations précisées. Le premier alinéa est donc coordonné à cette qualité d'assuré, sans retirer les cohortes et droits maintenus de la cible ni restreindre les avantages aux anciens emplois."
 },
 'L357-4': {
  'L1234-1': "Le renvoi de L357-4 aux règles de retraite et de cumul n'est pas un renvoi au préavis individuel. Les quinze jours proposés pour le nouveau contrat privé ne s'étendent pas aux agents publics relevant de textes distincts et ne remplacent ni autorisations de rupture protégée ni procédures collectives ; les anciens préavis gardent leur transition.",
  'L1221-2': "Les assurés du régime local peuvent relever de situations privées ou publiques : leur régime de pension ne les transforme pas en salariés du contrat unique. Pour une nouvelle relation privée la cible exclut le CDD, mais une phase à temps partiel ou une retraite progressive ne fixe aucun terme d'emploi ; les contrats anciens gardent leurs droits.",
  'L1234-9': "La retraite progressive mentionnée via L161-22-1-5 peut viser l'indemnité de départ à la retraite de L1237-9, distincte de l'indemnité ordinaire de L1234-9. Le seuil d'un an au terme effectif préavis inclus, les 0,20 mois par année totale et les six mois de plafond ne doivent donc pas être importés dans les prestations du régime local ou ses droits spéciaux.",
  'L351-5': "Le renvoi étend la majoration pour la durée effective du congé parental, si elle est plus favorable que L351-4. La proposition de la cible corrige l'ancien L122-28-1 privé en L1225-47 1° et L1225-48 tout en préservant les congés anciens et la référence publique de la loi de 1978 ; L357-4 peut garder ce renvoi sans importer un régime privé aux agents publics.",
  'L351-1': "La cible conserve le calcul, les indemnités maternité dans le salaire de base et la garantie historique, puis limite le transfert de cotisations aux salariés du régime général d'un employeur privé. Le renvoi local n'efface pas ces limites ni les conditions préalables de L241-3 : aucune capitalisation automatique pour tous les titulaires locaux, aucune double réduction des droits.",
  'L161-22-1-5': "La retraite progressive est un service fractionné de pension soumis à âge, durée d'assurance, activité réduite et exceptions du II. Sa proposition conserve les majorations et l'exclusion liée au dernier alinéa de L1237-9 ; L357-4 ne doit ni les fermer ni y substituer le barème de licenciement de L1234-9 ou un terme de quinze jours.",
  'L161-22': "Le second alinéa de L357-4 étend les règles de cessation et cumul avec leurs exceptions salariées, agricoles, publiques et de retraite progressive. Les notes de la cible bornent le nouveau régime à la première pension de base dès le 1er janvier 2027, sauf autre pension antérieure et exceptions indiquées ; le renvoi ne supprime pas cette transition ni les dérogations favorables."
 }
}

for number, answer in ANSWERS.items():
    key = answer['code_id'] + '|' + answer['source_id']
    required = REFERENCES['requirements'][key]
    descriptions = CHECKS.get(number, {})
    for target_key in required:
        target = REFERENCES['targets'][target_key]
        assessment = descriptions[target['number']]
        assert len(assessment) >= 80
        answer['reference_checks'].append({'target_key': target_key,
            'view_sha256': target['view_sha256'], 'assessment': assessment})
    assert len(descriptions) == len(required)

ordered = [ANSWERS[a['number']] for a in SOURCES]
assert len(ordered) == 24
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(ordered), 'articles')
