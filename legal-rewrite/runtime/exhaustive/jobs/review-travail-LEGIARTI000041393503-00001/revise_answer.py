import copy
import hashlib
import json

with open('source.json') as f:
    sources = json.load(f)
with open('previous-answer.json') as f:
    previous = json.load(f)
with open('reference-targets.json') as f:
    refs = json.load(f)

answer = copy.deepcopy(previous)
by_number = {a['number']: a for a in answer}

# Reprise des corps complets du précédent essai après confrontation aux sources.
# Les contrôles de renvois sont tous reconstruits depuis les vues actuelles.
for a in answer:
    a.pop('reference_checks', None)

contexts = {
    'R6323-10': (
        "Les prévenances de demande de congé supprimées sont des délais de formation ; elles ne règlent pas le licenciement.",
        "Le congé s'adresse à l'employeur actuel, même si l'affectation temporaire change ; il ne fixe aucun terme d'emploi.",
        "L'ancienneté vérifiée pour le congé n'est pas la condition d'ouverture de l'indemnité de rupture."
    ),
    'R6323-11-1': (
        "Le dépôt financier avant réponse sur le congé n'est pas une notification de rupture et n'ouvre aucun préavis.",
        "La demande pendant l'emploi est ouverte au contrat unique futur et aux contrats antérieurs, sans CDD nouveau requis.",
        "L'accès au financement pendant le contrat n'est pas subordonné à un an d'ancienneté au titre d'une indemnité de rupture."
    ),
    'R6323-11-2': (
        "Les quatre et six mois retirés concernaient le calendrier postérieur à l'emploi, non la durée du préavis de rupture.",
        "La fin d'une mission peut ouvrir la demande de formation alors que le contrat unique continue ; elle n'en devient pas le terme.",
        "La suppression des échéances de formation ne modifie ni le débiteur ni le calcul d'une indemnité de rupture."
    ),
    'R6323-14-1': (
        "La fin effective du contrat sépare les modalités de financement avant et après emploi ; la décision de financement ne rompt pas le contrat.",
        "Le maintien du régime social après emploi ne peut rester réservé au CDD supprimé pour les nouvelles embauches.",
        "La rémunération de stagiaire et les garanties sociales ne sont pas l'indemnité ordinaire de licenciement."
    ),
    'R6323-14-3': (
        "Le II compare la décision de rupture à l'accord de prise en charge, sans confondre cette décision avec la fin du préavis.",
        "Le maintien du projet après rupture reste ouvert dans les emplois futurs à durée indéterminée ; aucune formation ne termine ces emplois.",
        "La démission n'ouvre pas l'indemnité ordinaire, mais elle peut conserver le financement de formation selon le II proposé."
    ),
    'D6323-18-2': (
        "Le paiement direct par la commission suit la fin effective de l'emploi, et non la réception de la seule notification de rupture.",
        "Le payeur après cessation d'emploi reste déterminé pour les futurs contrats uniques comme pour les CDD antérieurs.",
        "Le paiement de rémunération par la commission après emploi est distinct d'une indemnité due par l'employeur à la rupture."
    ),
    'R6323-18-2-1': (
        "La lettre de mission de formation organise une affectation, sans être une notification de rupture ni déclencher son préavis.",
        "Le II remplace le nouveau contrat de mission de formation par une lettre dans l'emploi à durée indéterminée, sans nouvel essai.",
        "Les avances, remboursements et cotisations de formation ne sont pas plafonnés par le barème d'indemnité ordinaire de rupture."
    ),
    'D6323-18-3': (
        "Les douze et quatre mois constituent des références de salaire de formation, sans régler le préavis individuel.",
        "Le calcul favorable de quatre mois ne doit pas exiger un CDD nouveau ; l'emploi demeure à durée indéterminée après la bascule.",
        "Le salaire moyen de formation ne reprend pas le salaire de référence ni le seuil d'ouverture d'une indemnité de licenciement."
    ),
    'R6323-18-3-1': (
        "Les 600 heures servent à la moyenne salariale intérimaire, sans fixer un préavis ni une date de rupture du contrat.",
        "Le calcul subsidiaire sert les intérimaires en contrat unique sans leur imposer la fin de leur mission ou de leur emploi.",
        "Les allocations et congés spectacles inclus dans la moyenne relèvent de la rémunération de formation, non de l'indemnité ordinaire."
    ),
    'R6324-1': (
        "La fenêtre de dépôt supprimée et les vingt jours d'instruction conservés ne sont pas le préavis de rupture de l'emploi.",
        "Le contrat avec l'entreprise d'accueil doit être à durée indéterminée ; la reconversion et la suspension du contrat d'origine ont une durée propre.",
        "L'accord de suspension et le dossier de reconversion ne conditionnent pas la formation au paiement d'une indemnité de rupture."
    ),
    'R6324-4': (
        "L'abrogation vise une transmission au ministre, sans modifier la notification du refus aux parties ni les notifications de rupture.",
        "L'abrogation du dépôt central ne remet pas en cause l'emploi d'accueil à durée indéterminée ni les accords de suspension.",
        "La suppression du circuit ministériel n'affecte aucun seuil d'ancienneté ou paiement de l'indemnité ordinaire de rupture."
    ),
    'D6325-12': (
        "La convention spéciale entreprise-prestataire abrogée porte sur la pédagogie, sans durée de préavis individuel de l'emploi.",
        "La phase de professionnalisation, sa convention et son financement ne fixent pas le terme du contrat unique futur.",
        "L'abrogation de la signature spéciale ne concerne ni les indemnités patronales de rupture ni les créances salariales du salarié."
    ),
}

core = {
    'L1234-1': "La source prévoit les préavis patronaux selon l'ancienneté : règles professionnelles avant six mois, un mois de six mois à moins de deux ans, deux mois ensuite, avec minima plus favorables. La vue proposée les conserve pour les contrats antérieurs et fixe quinze jours calendaires pour les nouveaux contrats, y compris paiement sans exécution si la faute grave empêche le maintien au travail. Ce préavis individuel reste distinct des procédures collectives et autorisations spéciales. Le départ après notification écrite et le préavis du salarié sont coordonnés par la section travail ; le présent article de formation n'y déroge pas.",
    'L1221-2': "Le texte officiel autorise encore les emplois à terme du titre IV. La vue proposée, qui est un projet et non le droit en vigueur, impose le contrat unique à durée indéterminée pour les embauches nouvelles et interdit une fin automatique à l'achèvement d'une mission, d'une formation ou d'un chantier, ainsi que les renouvellements à terme après la bascule. Les contrats antérieurs et leur ancienneté restent protégés. La présente coordination conserve les avantages futurs de formation dans ce champ privé et n'étend pas le régime aux agents publics.",
    'L1234-9': "La source ouvre le droit après huit mois hors faute grave. Pour le contrat unique nouveau, la vue proposée retient un an à la fin effective, préavis inclus sous sa réserve de fin d'essai, puis 0,20 mois de salaire brut par année totale, fractions en mois complets au prorata, plafond légal de six mois et initiative de l'employeur seule ; elle conserve une exception de faute grave. La première année compte entière après ouverture. Les contrats anciens gardent le seuil antérieur et une composante acquise sans double compte ; droits plus favorables, congés, réparations d'illégalité et indemnités spéciales restent distincts. Aucun de ces seuils n'est importé dans le présent droit de formation.",
}

specific = {
    ('R6323-10', 'L1251-2'):
        "Le renvoi du dernier alinéa identifie l'entreprise de travail temporaire qui recrute et rémunère le salarié : c'est elle qui reçoit la demande de congé, et non l'entreprise utilisatrice. La vue proposée conserve cette définition et impose le contrat unique aux recrutements nouveaux avec garanties de rémunération et d'intermission. Le destinataire reste donc cohérent sans exiger un nouveau contrat de mission ; les anciens contrats et leurs droits ne sont pas exclus.",
    ('R6323-11-1', 'R6323-10'):
        "Le renvoi porte sur l'autorisation de l'absence effective pendant le temps de travail. La source prévoit 120/60 jours, réponse écrite sous trente jours, accord tacite et refus motivé ; la vue fournie supprime les deux prévenances. Le texte complet du présent lot retire aussi les mentions distinctes d'examen. Le dépôt financier peut précéder la réponse sans autoriser l'absence par lui-même. L'autorisation expresse ou tacite suffit, sans second accord sur le financement ni confusion avec le préavis de rupture.",
    ('R6323-11-1', 'D6323-9'):
        "La source distingue 24 mois dont douze dans l'entreprise et 24 mois sur cinq ans dont quatre de CDD sur douze, avec exclusions au II. La proposition fournie fusionne l'accès au 1° en 24 mois globaux, abroge le 2°, retire l'ancienneté locale et réintègre les cinq catégories de périodes ; elle conserve dispenses et appréciation au départ au III. Le présent texte ne reprend donc plus l'ancien 2° ni ses exclusions, à la différence de previous_draft. La conversion convenue conserve l'ancienneté ; aucun nouveau CDD n'est nécessaire.",
    ('R6323-11-2', 'R6323-9-1'):
        "Le renvoi vise les voies spéciales spectacle du I et intérim du II ; le III apprécie l'ancienneté au départ. La source impose en outre 220 jours/cachets et 600 heures dans l'entreprise ou le groupe. La proposition retire ces deux verrous, mais conserve les alternatives professionnelles 130/65, 88/44 et 60/30, ainsi que 1 600 heures de branche sur dix-huit mois et les intermissions pour le CDI. La suppression ici des quatre et six mois postérieurs à l'emploi ne rétablit aucun verrou supprimé et n'efface pas les périodes de référence maintenues. La fin de mission ne rompt pas le contrat unique.",
    ('R6323-14-1', 'R6323-11-1'):
        "Le I renvoie à la demande présentée pendant l'exécution du contrat. La source de la cible réserve cette faculté au CDD ; sa vue l'étend au contrat unique mais son troisième paragraphe conserve encore les quatre mois et exclusions de D. 6323-9. La nouvelle rédaction de ce même lot corrige ce point pour suivre la fusion actuelle des voies d'ancienneté. Le financement après fin effective et les garanties du II restent ainsi ouverts aux futurs contrats uniques ; l'autorisation de congé ne concerne que le temps de travail effectivement occupé.",
    ('R6323-14-3', 'R6323-10'):
        "La référence sert uniquement lorsqu'un nouvel emploi est effectivement repris et que la formation empiète sur son temps de travail. Le nouvel employeur autorise alors le congé expressément ou par silence de trente jours, selon la cible. La suppression de 120/60 jours dans la vue est conservée, et le présent lot retire également les mentions séparées d'examen. Le maintien du financement n'exige plus de retrouver un emploi, ni un mois entre contrats ; ce mois n'est pas un préavis et sa suppression ne dispense pas d'une rupture régulière.",
    ('D6323-18-2', 'R6323-14-1'):
        "Le renvoi ouvre le paiement direct pour le projet après cessation effective. La cible officielle limite le début à six mois après le CDD et garantit statut de stagiaire, rémunération, sécurité sociale, chômage et retraite complémentaire. Sa vue élargit au contrat unique mais conserve six mois. La rédaction complète retenue dans ce lot supprime ce verrou en coordination avec R. 6323-11-2, sans retirer les garanties. Le versement ne débute pas du seul fait d'une notification ou d'une fin de mission lorsque l'emploi continue.",
    ('D6323-18-2', 'R6323-18-2-1'):
        "La cible distingue le paiement mensuel direct aux intermittents au I du paiement patronal remboursé pour l'intérim aux II à IV. Le renvoi pendant emploi maintient ce partage, avec remboursement sous un mois et avances des moins de cinquante salariés plafonnées à 90 %. Le texte de ce lot supprime en plus la facture distincte de première avance, sans changer ses trente jours. Il ne fait pas supporter à un ancien employeur la rémunération relevant du paiement direct après emploi, et une lettre de mission ne crée pas une rupture.",
    ('R6323-18-2-1', 'L1251-58-1'):
        "La source prévoit déjà contrat de mise à disposition avec l'utilisateur et lettre de mission dans le CDI intérimaire. La vue proposée généralise le contrat unique pour les recrutements nouveaux, préserve l'ancienneté et interdit que la fin de mission rompe l'emploi. Le II retient donc la lettre pour l'affectation de formation, sans nouveau CDD ni essai. Le contrat commercial du 1° conserve son champ lorsqu'un utilisateur existe ; le congé ne crée pas artificiellement un utilisateur. Les anciens contrats de mission demeurent protégés jusqu'à leur terme, sans renouvellement nouveau après la réforme.",
    ('R6323-18-2-1', 'L1251-57'):
        "Les 1° et 2° assimilent à des missions les stages, bilans, VAE, congés de transition et formations professionnelles conventionnelles. L'assimilation permet de formaliser l'affectation de formation par lettre ; elle n'impose pas un contrat de travail à terme. La vue proposée conserve les initiatives de l'employeur ou du salarié et les conditions conventionnelles, puis les rend applicables au contrat unique sans terme automatique. Les avantages et anciennes créances de formation subsistent ; la fin de la phase n'est pas une notification de rupture.",
    ('R6323-18-2-1', 'R6323-9-1'):
        "La référence source au III pour les conditions intérimaires est corrigée : le II fixe les heures et les intermissions, le III seulement leur appréciation au départ. La vue actuelle retire les 600 heures dans l'entreprise/groupe mais garde 1 600 heures de branche sur dix-huit mois ; au I, elle retire les 220 jours supplémentaires sans effacer les alternatives des 1° à 3°. Le présent article ne remet ces seuils supprimés ni au financement ni au paiement. La correction de L. 125158-1 en L. 1251-58-1 est distincte de cette rectification de subdivision.",
    ('D6323-18-3', 'R6323-11-1'):
        "La vue de la cible conserve encore une assimilation à quatre mois de CDD et les exclusions de l'ancien II de D. 6323-9. Ces éléments sont retirés dans la version complète du présent lot car la cible actuelle D. 6323-9 fusionne ses voies et réintègre ces périodes. La référence salariale favorable est désormais définie directement au III de D. 6323-18-3, sans demander une nouvelle période de CDD ni l'accord patronal préalable au dépôt. Le congé sur temps de travail reste autorisé, sans importer les conditions d'indemnité de rupture.",
    ('D6323-18-3', 'D6323-9'):
        "La source fait dépendre la moyenne de douze mois du 1° et celle de quatre mois de CDD du 2°. La proposition actuelle de D. 6323-9 abroge ce 2°, supprime les douze mois dans l'entreprise et les exclusions du II ; elle maintient 24 mois globaux, dispenses et appréciation au départ. Le calcul est donc coordonné directement : douze mois de référence, ou quatre derniers mois d'activité plus favorables si quatre mois existent sur douze. Ces quatre mois sont un critère de calcul seulement, sans recréer une condition d'ouverture ni exclure les contrats uniques futurs.",
    ('R6323-18-3-1', 'D6323-18-3'):
        "Cette cible ajoutée a été lue en entier, source et proposition. La source sépare douze mois au II et quatre mois de CDD au III ; la vue fournie continue de rattacher ce III au 2° du I de D. 6323-9, pourtant abrogé dans la vue actuelle de ce dernier. La nouvelle rédaction de D. 6323-18-3 dans le présent lot corrige ce renvoi et conserve quatre mois d'activité sur douze si plus favorables, sans exclusion de contrats. Le nouveau renvoi au III de cet article sert uniquement au calcul subsidiaire quand aucune heure de mission n'est utilisable ; il n'étend pas la voie générale à tous les calculs spéciaux et n'ajoute aucune ancienneté à l'intérimaire.",
    ('R6323-18-3-1', 'R6323-9-1'):
        "Le I détermine les périodes du spectacle et le II l'ancienneté intérimaire ; le III apprécie au départ. La proposition fournie retire les 220 jours supplémentaires et les 600 heures d'entreprise ou de groupe mais maintient les alternatives professionnelles, 1 600 heures de branche sur dix-huit mois et les intermissions. Les 600 heures de la formule salariale locale ne doivent donc pas devenir un seuil d'accès : le calcul de branche intervient à défaut, puis les rémunérations réelles en l'absence de mission utilisable. Les intermissions restent de l'ancienneté sans devenir des heures fictives de mission ; allocations et congés spectacles conservent leur traitement distinct au I.",
    ('R6323-18-3-1', 'D6323-9'):
        "Cette seconde cible ajoutée est distincte du calcul spécial d'intérim. Son texte officiel prévoit deux voies d'ancienneté et des exclusions ; sa proposition fusionne au 1° les 24 mois globaux, abroge le 2° et rend comptables les périodes du II, avec dispenses et appréciation au départ. Le renvoi nouveau apparaît ici seulement pour écarter une condition générale supplémentaire lors du recours au calcul de D. 6323-18-3. Il ne soumet pas un intérimaire admis par R. 6323-9-1 à 24 mois en plus de ses heures, ni à douze mois dans l'entreprise ou quatre mois de CDD. Les contrats anciens, les dispenses et les futures périodes en contrat unique restent recevables dans leurs champs.",
    ('R6324-1', 'L6324-3'):
        "Les pièces du 1° correspondent à l'accord interne du I et à l'accord de suspension du II ; le 3° identifie le contrat d'accueil. La source législative admet un CDD d'au moins six mois et impose un essai ; sa vue proposée remplace l'embauche nouvelle par le contrat unique, rend l'essai facultatif et protège le retour anticipé. Le dossier ne rétablit donc ni CDD, ni essai obligatoire, ni terme de l'emploi par la reconversion. Les notes préservent l'ancienne rédaction pour les avenants antérieurs au 1er janvier 2026 : cette date historique est distincte de l'entrée en vigueur future de la réforme.",
    ('R6324-4', 'L6324-3'):
        "L'accord écrit protège l'organisation interne avec rémunération maintenue au I et la suspension avec retour possible au II. La vue proposée impose un emploi nouveau à durée indéterminée et un essai seulement facultatif ; elle conserve les anciens contrats et leur ancienneté. L'abrogation porte sur la transmission au ministre, pas sur ces accords, leur financement ou les avantages futurs. Le régime de fond des avenants antérieurs au 1er janvier 2026 subsiste ; seules leurs transmissions encore à effectuer sur le fondement abrogé sont supprimées expressément, sans nouveau dépôt.",
    ('D6325-12', 'L6325-13'):
        "La source organise les actions par un organisme ou le service de formation de l'entreprise et prévoit 15 % à 25 %, au moins 150 heures. La vue proposée rapporte ces proportions à la durée de l'action au début du contrat unique et conserve les anciens droits, sans terme d'emploi. L'abrogation de la convention spéciale ne retire ni ces durées, ni la formation effective, ni ses aides futures. L'annexe pédagogique conserve un fondement propre dans D. 6325-11 lu dans le corpus ; le contrat prestataire-acheteur conserve celui de L. 6353-1. Ces références facultatives sont distinguées des cibles requises.",
}

for a in answer:
    n = a['number']
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        number = target['number']
        content = target['proposed_xml'] if target['view_kind'] == 'proposal' else target['source_xml']
        assert hashlib.sha256(content.encode()).hexdigest() == target['view_sha256']
        if number in core:
            index = {'L1234-1': 0, 'L1221-2': 1, 'L1234-9': 2}[number]
            assessment = contexts[n][index] + ' ' + core[number]
        else:
            assessment = specific[(n, number)]
        checks.append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': assessment,
        })
    a['reference_checks'] = checks

a = by_number['R6323-18-3-1']
a['review_notes'] = (
    "La source distingue déjà l'ancienneté dans l'entreprise OU le groupe (R. 6323-9-1) et une référence salariale dans la seule entreprise : l'éventuelle insuffisance d'heures dans cette entreprise est une difficulté préexistante, désormais traitée explicitement. La vue proposée retire l'obligation locale de 600 heures ; elle ne retire ni les 1 600 heures de branche sur dix-huit mois ni les intermissions d'ancienneté. La nouvelle moyenne n'intègre pas les intermissions comme heures rémunérées de mission et ne diminue pas la garantie mensuelle du CDI intérimaire. En l'absence totale de mission utilisable, le calcul utilise les rémunérations réellement versées, notamment la garantie d'intermission, sur douze mois avec la possibilité favorable de quatre mois. "
    "Les deux nouveaux renvois à D. 6323-18-3 et D. 6323-9 disposent désormais de leurs cibles complètes dans reference-targets.json ; ils sont couverts par les analyses requises et leurs empreintes actuelles. La vue de D. 6323-18-3 conserve encore l'ancien 2° du I de D. 6323-9 : la rédaction complète de D. 6323-18-3 dans ce lot le remplace par le calcul favorable directement défini au III. Le présent renvoi vise ce III coordonné, jamais une condition de quatre mois de CDD ou les anciennes exclusions. Le renvoi à D. 6323-9 est seulement une exclusion d'ancienneté supplémentaire, pas une deuxième voie d'éligibilité obligatoire. "
    "L'utilisation de rémunérations de plusieurs entreprises pour le seul calcul de secours élargit les données utiles : accès légal à respecter, coût de traitement non chiffré. Les droits déjà ouverts sont protégés. Le calcul de secours ne permet pas de remettre en cause une base salariale déjà établie sous le régime antérieur ; aucun effet individuel favorable universel ni solde net de complexité n'est démontré."
)
a['reason'] += (
    " La confrontation aux deux cibles complètes ajoutées confirme que le renvoi au III de D. 6323-18-3 doit suivre sa rédaction coordonnée dans ce lot ; il ne peut conserver la voie d'accès au 2° du I de D. 6323-9 supprimée dans sa proposition actuelle. Le corps complet du précédent essai est conservé sur ce point, les anciennes analyses de renvois étant remplacées."
)

# Les renvois facultatifs ne sont jamais ajoutés à reference_checks.
by_number['D6325-12']['review_notes'] += (
    " Les renvois ajoutés à L. 6353-1, D. 6353-1 et D. 6325-11 ne figurent pas parmi les cibles requises de reference-targets.json ; ils sont vérifiés en lecture seule dans travail.json du corpus fourni, sans ajout à reference_checks. D. 6353-1 II ouvre déjà les bons de commande ou devis approuvés, et son III prévoit le cas CPF : ces dispenses ne sont pas supprimées. La note de son décret 2025-586 concerne l'application aux contrats d'apprentissage conclus depuis le 1er juillet 2025, sans fixer la date de la présente réforme."
)
by_number['R6323-11-1']['review_notes'] += (
    " Le renvoi dérogatoire à R. 6323-11, absent des cibles requises, a été vérifié dans son texte intégral du corpus fourni : l'accord est bien préalable au dépôt dans la source. La dérogation supprime ce seul ordre obligatoire, en conservant compétence territoriale et interdiction des demandes simultanées."
)

source_by_key = {(s['code_id'], s['source_id']): s for s in sources}
for a in answer:
    s = source_by_key[(a['code_id'], a['source_id'])]
    for field in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert a[field] == s[field]

with open('answer.json', 'w') as f:
    json.dump(answer, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(f"answer.json : {len(answer)} articles, {sum(len(a['reference_checks']) for a in answer)} analyses de renvoi actuelles")
