import json
import re
import html
from pathlib import Path
from html.parser import HTMLParser

SOURCES = json.loads(Path('source.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'p', 'br', 'div', 'li', 'tr', 'td', 'th'}:
            self.parts.append(' ')

    def handle_endtag(self, tag):
        if tag in {'p', 'div', 'li', 'tr', 'td', 'th'}:
            self.parts.append(' ')

    def handle_data(self, data):
        self.parts.append(data)


def plain(xml):
    parser = TextExtractor()
    parser.feed(xml)
    return re.sub(r'\s+', ' ', ''.join(parser.parts)).strip()


def stripped_plain(xml):
    # Also check the exact text obtained without inserting spaces at tag boundaries.
    # A quotation must not depend on an invented space replacing a <br> tag.
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', xml))).strip()


def paragraphs(*ps):
    return '\n'.join('<p>' + p + '</p>' for p in ps)


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


ANSWERS = {}


def retain(number, reason, notes, assessment, limitations, burdens, benefit=None):
    s = BY_NUMBER[number]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=impact('retained_necessary', assessment, limitations, burdens))
    if benefit:
        a['benefit_review'] = benefit
    ANSWERS[number] = a


def rewrite(number, xml, reason, notes, substantive, removed=None, benefit=None,
            full_repeal=None):
    s = BY_NUMBER[number]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='rewrite_draft', substantive_impact=substantive)
    if full_repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=full_repeal)
    elif removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    ANSWERS[number] = a


retain('R112-3',
       "Maintien intégral, sans réécriture stylistique : les courbes et plages de Lden déterminent l'étendue des servitudes acoustiques. Leur suppression sans étude de l'exposition effacerait la protection contre le bruit, et non une formalité redondante. Les régimes antérieurs au 28 avril 2002, les aérodromes de R. 112-2 et les aérodromes militaires restent tous dans leur champ.",
       "Lecture croisée des sources R. 112-1 et R. 112-2 ainsi que L. 112-7 à L. 112-10. Conserver A : 70 ; B : 70/62, avec limite extérieure 65 à 62 pour les aérodromes antérieurs au 28 avril 2002 ; C ordinaire : 57 à 55 ; C de R. 112-2 : 57 à 52 ; B militaire : 68 à 62 ; C militaire : 64 à 55 ; D : 50. La délimitation facultative de D hors du champ obligatoire de L. 112-7 n'est pas transformée en obligation. Aucun seuil acoustique nouveau ni suppression des dérogations de L. 112-10.",
       "L'article officiel entier est conservé : aucune courbe, plage de modulation ou distinction d'aérodromes n'est supprimée. Aucun allègement fiscal ou administratif n'est revendiqué.",
       "Les effets d'un déplacement des courbes ne sont pas établis par les sources du lot. Les contraintes européennes relatives au bruit ne sont ni écartées ni réputées réécrites.",
       "Aucune charge nouvelle n'est identifiée : les valeurs, catégories, exceptions historiques et documents de référence restent strictement ceux de la source.",
       "Les modulations propres aux aérodromes antérieurs au 28 avril 2002, à ceux de R. 112-2 et aux aérodromes militaires sont intégralement maintenues. Leur effet éventuellement favorable dépend de la courbe retenue ; aucun accès futur à ces régimes n'est fermé.")

retain('R112-4',
       "Maintien intégral : l'échelle commune de 1/25 000, la représentation des quatre zones et l'indication des indices rendent les limites vérifiables par les propriétaires et le public. L'examen des hypothèses de court, moyen et long terme évite une cartographie limitée à une seule situation de trafic. Aucun dossier ou justificatif individuel redondant n'est identifié dans cet article.",
       "Rapprochement avec L. 112-7, R. 112-1 à R. 112-3 et la consultation publique de R. 112-15. La mention de D conserve les mots « le cas échéant » ; elle ne généralise pas cette zone facultative. L'échelle n'est pas remplacée par un format nouveau.",
       "Le contenu cartographique officiel est maintenu en entier, sans ajout d'étude ni modification de l'échelle ou des horizons prévisionnels. Il n'y a pas de réduction démontrée à compter.",
       "Les coûts de production et la pertinence d'une autre échelle ne sont pas documentés ; aucune économie de cartographie n'est affirmée sur cette seule base.",
       "Aucune charge nouvelle n'est identifiée, puisque le texte source est conservé et qu'aucun support, fichier ou actualisation supplémentaire n'est imposé.")

retain('R112-6',
       "Maintien intégral de l'exclusion des seuls éléments protégés par le secret de la défense nationale. Cette dispense ciblée empêche une divulgation illicite dans le rapport public, sans dispenser du rapport lui-même. Elle couvre les affectations exclusive, principale et secondaire ; aucune charge autonome à supprimer n'a été identifiée.",
       "Renvoi à L. 112-7 vérifié dans le corpus. Articuler cette exclusion avec l'enquête de R. 112-15, qui conserve les limites et conditions légales propres à la défense. Aucune donnée secrète n'a été recherchée ni lue.",
       "L'article entier reste inchangé : dispense ciblée de divulgation, et non suppression de l'information publique non protégée. Aucun nouveau gain de simplification n'est compté.",
       "La qualification concrète des éléments classifiés relève de leurs règles propres et n'est pas contrôlée dans ce travail portant sur les seuls textes publics.",
       "Aucune charge nouvelle n'est identifiée : aucun certificat, contrôle ou dossier nouveau n'est ajouté à la dispense existante.",
       "La dispense de faire figurer des éléments protégés dans le rapport reste ouverte pour tout plan futur concernant un aérodrome à affectation exclusive, principale ou secondaire à la défense. Le reste du rapport et la participation du public subsistent.")

retain('R112-7',
       "Maintien intégral de la continuité du plan pendant sa révision. La suppression de cette règle ouvrirait une période sans limites opposables avant la publicité du nouveau plan. Le renvoi à R. 112-17 demeure opérant après le retrait de la presse : cet article conserve notification, accès matériel et affichage des lieux de consultation.",
       "Lecture de L. 112-17 et R. 112-17. La présente conservation ne reconduit pas les deux insertions dans la presse supprimées dans la proposition de R. 112-17 ; elle renvoie aux seules mesures restant requises pour le nouveau champ temporel. Pas de remise à zéro des délais de recours déjà ouverts.",
       "Maintien de l'article officiel en entier et du mécanisme de continuité. La réduction des formalités de publicité est portée par R. 112-17 et n'est pas comptée à nouveau ici.",
       "Aucun allègement autonome du régime d'opposabilité n'est démontré dans cet article ; les décisions anciennes restent soumises à leur régime de publicité.",
       "Aucune charge nouvelle n'est identifiée : le plan précédent demeure applicable jusqu'aux publicités requises, sans confirmation ou nouvelle demande des propriétaires.")

peb_ministere = 'peb-accord-ministeriel-approbation-unique'
xml = paragraphs(
    "La décision d'établir ou de réviser un plan d'exposition au bruit est prise par le préfet. Lorsque l'emprise d'un aérodrome ou les communes concernées ou susceptibles d'être concernées par le plan d'exposition au bruit d'un aérodrome sont situées sur le territoire de plusieurs départements, la décision est prise conjointement par les préfets de ces départements.",
    "La décision d'établir ou de réviser le plan n'est pas subordonnée à un accord ministériel préalable. Les accords exprès requis pour l'approbation du plan dans les cas prévus à l'article R. 112-16 demeurent exigés.",
    "Le deuxième alinéa s'applique aux décisions d'établir ou de réviser un plan prises à compter de l'entrée en vigueur de la loi. Les décisions antérieures et les actes régulièrement accomplis sur leur fondement conservent leurs effets, sans renouvellement des accords déjà recueillis.")
rewrite('R112-8', xml,
        "Réforme de fond : suppression des deux accords ministériels préalables au seul lancement du plan, celui de la défense et celui de l'aviation civile. Le contrôle exprès propre aux aérodromes de défense, d'intérêt national et étrangers subsiste une seule fois à l'approbation par R. 112-16. La compétence préfectorale et la décision conjointe interdépartementale sont maintenues. Correction expresse de la coquille « où » en « ou » dans l'alternative du premier alinéa.",
        "R. 112-16, L. 112-16 et le renvoi de R. 112-9 relus : l'approbation finale, ses accords sectoriels, sa motivation et l'enquête restent applicables. La suppression est limitée au lancement et ne permet pas d'approuver un plan sans les accords finaux. Vérifier les instructions ministérielles d'application hors du corpus ; elles ne doivent pas recréer le visa de lancement. La coquille « aérodrome où les communes » est une anomalie préexistante signalée et corrigée ici, sans changement du champ interdépartemental.",
        impact('material_reduction',
               "Deux accords exprès de lancement sont effectivement retirés pour leurs champs respectifs. Les mêmes autorités conservent leur accord final ; il s'agit d'une réduction du circuit préalable, sans suppression de la protection acoustique ni d'un impôt.",
               "La durée réelle gagnée et les coûts ministériels ne sont pas chiffrés. La réforme ne couvre pas les décisions de lancement antérieures, les accords d'approbation ni les autorisations aéronautiques distinctes.",
               "Aucune charge nouvelle n'est identifiée : aucun avis, déclaration ou délai ne remplace les accords retirés ; l'accord d'approbation était déjà exigé par R. 112-16.",
               [effect('authorization_removed', peb_ministere,
                       "Suppression des accords ministériels de lancement, avec maintien des accords à l'approbation.",
                       "Avant de décider le lancement, accord exprès de la défense pour les aérodromes à affectation exclusive ou principale ; accord exprès de l'aviation civile pour les aérodromes d'intérêt national hors affectation principale défense et les aérodromes étrangers affectant le territoire français.",
                       "La décision préfectorale de lancement ne requiert aucun de ces accords ; les accords exprès sectoriels de R. 112-16 restent requis à l'approbation dans les mêmes cas.",
                       'legal_duty', "Préfets, ministres compétents et collectivités concernées par ces plans.",
                       "Décisions de lancement prises à compter de l'entrée en vigueur de la loi ; décisions et actes antérieurs préservés.",
                       "Aucun circuit de remplacement ; les accords finaux existent déjà.",
                       "Elle est prise avec l'accord exprès du ministre chargé de l'aviation civile, en ce qui concerne les aérodromes classés dans la catégorie des investissements d'intérêt national lorsque le ministère de la défense n'en est pas l'affectataire principal, et pour les aérodromes situés en territoire étranger dont les nuisances de bruit affectent le territoire français.",
                       "La décision d'établir ou de réviser le plan n'est pas subordonnée à un accord ministériel préalable.")]),
        removed=["Accord exprès du ministre chargé de la défense avant la décision préfectorale de lancer l'établissement ou la révision du plan.",
                 "Accord exprès du ministre chargé de l'aviation civile avant le lancement pour les aérodromes d'intérêt national et les aérodromes étrangers du champ source."])

retain('R112-9',
       "Maintien intégral de l'examen au moins quinquennal par la commission existante. Ce contrôle confronte les prévisions au trafic constaté et peut conduire à corriger un plan devenu excessivement restrictif ou insuffisamment protecteur. Il n'impose ni nouvelle commission lorsqu'elle n'existe pas, ni révision systématique, ni rapport distinct à la charge des propriétaires.",
       "Renvoi à R. 112-8 vérifié : le préfet garde son pouvoir de mise en révision même après suppression des accords ministériels de lancement. Le délai reste « tous les cinq ans au moins », sans être transformé en durée minimale de maintien d'une servitude. Articulation avec les données d'activité aérienne, sans collecte privée supplémentaire créée.",
       "La règle officielle entière est maintenue : examen périodique et faculté de proposer la révision. Aucun examen ni déclaration n'est supprimé ; aucun allègement nouveau n'est compté.",
       "Aucun coût net de cet examen ni calendrier réel de révision n'est établi. Les autres dispositifs d'évaluation du bruit ne sont pas présumés équivalents à ce contrôle du plan.",
       "Aucune charge nouvelle n'est identifiée : la périodicité, le rôle de la seule commission existante et la faculté de proposition restent inchangés.")

press = 'urbanisme-suppression-doubles-insertions-presse'
xml = paragraphs(
    "La décision d'établir ou de réviser le plan d'exposition au bruit est notifiée par le préfet, accompagnée d'un projet de plan d'exposition au bruit, aux maires des communes concernées et, s'il y a lieu, aux présidents des établissements publics de coopération intercommunale compétents.",
    "La mention de cette décision dans deux journaux à diffusion régionale ou locale dans le département n'est pas requise. L'affichage prévu à l'article R. 112-12 demeure obligatoire.",
    "Ces dispositions s'appliquent aux décisions prises à compter de l'entrée en vigueur de la loi. Les mesures de publicité relatives aux décisions antérieures restent régies par les dispositions qui leur étaient applicables ; les insertions déjà effectuées n'ont pas à être renouvelées.")
rewrite('R112-10', xml,
        "Réforme de fond : retrait des deux insertions de presse pour la décision de lancement. La notification avec le projet aux élus et l'affichage d'un mois dans toutes les communes et aux sièges intercommunaux concernés restent exigés, ainsi que l'enquête ultérieure. Aucune publication numérique nouvelle n'est imposée en remplacement.",
        "R. 112-12, R. 112-13 et R. 112-15 relus : l'avis des collectivités court toujours de la notification et non d'une insertion. La publicité de lancement demeure assurée par R. 112-12. L. 112-15 peut attacher des effets à la publication de la mise en révision ; l'affichage maintenu ne doit pas être omis. Les publicités de l'enquête prévues hors corpus par l'environnement ne sont pas supprimées. Mesure de presse commune avec R. 112-17 et R. 113-11, sans décompte de taxes distinctes.",
        impact('material_reduction',
               "Les deux insertions de presse obligatoires au lancement sont supprimées, tandis que notifications, projet communiqué et affichage existant subsistent. Aucun taux fiscal n'est modifié.",
               "Les tarifs d'insertion et le solde public ne sont pas connus. Le retrait ne concerne ni les décisions antérieures ni les publicités indépendantes de l'enquête environnementale.",
               "Aucune charge nouvelle n'est identifiée : l'affichage est déjà obligatoire et aucun site, fichier, envoi supplémentaire ou formalité de substitution n'est créé.",
               [effect('obligation_removed', press,
                       "Retrait de la double annonce de presse lors du lancement d'un plan d'exposition au bruit.",
                       "Une mention en caractères apparents dans deux journaux régionaux ou locaux du département, en plus des notifications et de l'affichage.",
                       "Aucune insertion de presse sur ce fondement pour les nouvelles décisions ; notification et affichage de R. 112-12 conservés.",
                       'legal_duty', "Préfets et services chargés de la publicité du lancement des plans.",
                       "Décisions prises à compter de l'entrée en vigueur ; publicité des décisions antérieures régie par le droit antérieur.",
                       "Aucune formalité de remplacement ; affichage préexistant maintenu.",
                       "Mention en est insérée en caractères apparents dans deux journaux à diffusion régionale ou locale dans le département.",
                       "La mention de cette décision dans deux journaux à diffusion régionale ou locale dans le département n'est pas requise.")]),
        removed=["Double insertion obligatoire dans la presse régionale ou locale de la décision d'établir ou de réviser le plan d'exposition au bruit."])

cce = 'peb-commission-environnement-consultation-unique'
xml = paragraphs(
    "Le présent article est abrogé pour les décisions d'établir ou de réviser un plan d'exposition au bruit prises à compter de l'entrée en vigueur de la loi. La consultation distincte de la commission consultative de l'environnement avant ces décisions n'est plus requise.",
    "Les consultations sur le projet de plan prévues à l'article R. 112-14 demeurent applicables. Les décisions de lancement antérieures restent régies par les dispositions qui leur étaient applicables ; les avis régulièrement recueillis conservent leur validité et n'ont pas à être renouvelés du seul fait de la présente abrogation.")
rewrite('R112-11', xml,
        "Abrogation prospective de la consultation séparée avant la décision de lancement. La commission reste consultée sur le projet complet par le circuit de R. 112-14 ; cet article précise désormais que son avis comprend le choix des indices de délimitation. Il y a une seule consultation obligatoire sur le projet, sans effacement des plages de R. 112-3, de l'avis ACNUSA ou de l'enquête publique.",
        "Coordination rédigée dans R. 112-14 pour le même champ temporel et sous la même clé de mesure. L. 112-16 requiert la consultation sur le plan et le recueil préalable de l'avis de la commission par l'ACNUSA dans son champ : ces exigences sont conservées. Aucune nouvelle consultation avant lancement ne doit être rétablie par une instruction. La suppression ne concerne pas les procédures lancées avant la loi, ni les autres missions de la commission.",
        impact('material_reduction',
               "La consultation autonome avant lancement est effectivement supprimée et son objet rejoint l'avis sur le projet déjà obligatoire. Le contrôle des valeurs acoustiques est conservé à ce stade unique ; la coordination de R. 112-14 n'est pas une seconde suppression.",
               "Le délai propre à la consultation initiale n'étant pas fixé dans la source, aucun nombre de jours gagnés n'est avancé. Les procédures antérieures, l'ACNUSA et l'enquête publique ne sont pas supprimées.",
               "Aucune charge nouvelle n'est identifiée : l'avis sur le projet existait déjà et aucun avis, registre ou justificatif supplémentaire ne remplace la consultation séparée.",
               [effect('obligation_merged', cce,
                       "Réunion de l'examen des indices et de l'avis sur le projet dans la consultation existante de R. 112-14.",
                       "Consultation de la commission sur les indices avant la décision de lancement, puis avis de cette commission sur le projet selon R. 112-14.",
                       "Suppression du premier passage obligatoire ; avis sur le projet de R. 112-14 comprenant les indices, avec les délais et garanties de cet article.",
                       'legal_duty', "Préfets, commissions consultatives de l'environnement et autorités chargées du plan.",
                       "Décisions de lancement prises à compter de l'entrée en vigueur ; validité des avis acquis et régime antérieur des anciennes procédures préservés.",
                       "Aucune procédure de remplacement nouvelle ; le second avis existant reprend l'objet utile du premier.",
                       plain(BY_NUMBER['R112-11']['source_xml']),
                       "La consultation distincte de la commission consultative de l'environnement avant ces décisions n'est plus requise.")]),
        full_repeal="Suppression, pour les nouvelles décisions de lancement du plan d'exposition au bruit, de la consultation autonome préalable de la commission sur les indices ; maintien de l'avis sur le projet complet dans R. 112-14.")

retain('R112-12',
       "Maintien intégral de l'affichage d'un mois, seul circuit local de publicité du lancement conservé après retrait des insertions de presse de R. 112-10. Il assure un accès local à l'information sans équipement numérique. Ce mois est une durée d'affichage, non un délai minimal d'attente ajouté à l'instruction ; le réduire dégraderait la publicité utile.",
       "R. 112-10 et L. 112-15 relus. Préserver chaque mairie et, s'il y a lieu, chaque siège intercommunal compétent. Ne pas confondre la durée d'affichage avec le délai de deux mois pour l'avis des collectivités à R. 112-13. La réforme de la presse ne dispense pas de cet affichage.",
       "La source officielle entière est conservée : affichage local d'un mois et mêmes lieux. Aucun délai d'instruction n'est réduit dans cet article.",
       "Le coût de l'affichage n'est pas mesuré et les règles de publicité environnementale distinctes ne sont pas auditées par cette conservation.",
       "Aucune charge nouvelle n'est identifiée : aucun affichage, point d'accès ou délai supplémentaire n'est créé ; l'obligation préexistante est maintenue.")

retain('R112-13',
       "Maintien intégral du délai de deux mois pour l'avis des conseils municipaux et organes intercommunaux, avec avis favorable en cas de silence. Ce délai garantit une délibération effective sur des servitudes affectant les habitants ; il n'impose pas d'attendre l'échéance si les avis sont déjà reçus, comme le confirme R. 112-14. La règle favorable de silence ne doit pas être retirée.",
       "Renvois à R. 112-10 et R. 112-14 relus. Le point de départ reste la notification de la décision avec le projet. Aucun délai n'est relancé à raison du retrait des annonces de presse ou de la consultation initiale. Ne pas transformer les deux mois en durée minimale obligatoire.",
       "Le texte entier reste celui de la source : deux mois au plus pour répondre et silence favorable. Aucun gain nouveau de délai n'est revendiqué.",
       "Aucune donnée ne démontre qu'une réduction du temps laissé aux assemblées préserverait leur participation effective ; les délais d'autres consultations restent distincts.",
       "Aucune charge nouvelle n'est identifiée : les destinataires, la saisine, la durée et l'effet favorable du silence sont conservés sans attestation ou confirmation.",
       "L'avis réputé favorable à l'expiration des deux mois reste applicable aux communes et établissements intercommunaux silencieux dans les procédures futures, sans confirmation supplémentaire. Cette facilité n'est pas transformée en refus tacite.")

xml = BY_NUMBER['R112-14']['source_xml'].strip() + '\n' + paragraphs(
    "Pour les procédures dont la décision d'établir ou de réviser le plan est prise à compter de l'entrée en vigueur de la loi, l'avis de la commission consultative de l'environnement prévu au présent article porte notamment sur les valeurs de l'indice L<sub>den </sub>à prendre en compte pour déterminer la limite extérieure de la zone C et, le cas échéant, celle de la zone B. Aucune consultation distincte de cette commission sur ces valeurs n'est requise avant la décision d'établir ou de réviser le plan. Les procédures engagées par une décision antérieure restent régies par les dispositions qui leur étaient applicables ; les avis régulièrement recueillis n'ont pas à être renouvelés du seul fait de la présente coordination.")
rewrite('R112-14', xml,
        "Coordination nécessaire de l'abrogation prospective de R. 112-11 : l'avis déjà requis sur le projet comprend expressément les valeurs d'indices auparavant examinées séparément avant le lancement. Tout le corps officiel est conservé : circuit ACNUSA/commission selon les aérodromes, avis des communes, délais de deux et quatre mois, dernière saisine interdépartementale et avis favorables tacites. Aucune seconde réduction autonome n'est comptée.",
        "R. 112-3, R. 112-11, R. 112-13 et L. 112-16 relus. La note source d'entrée en vigueur au 1er janvier 2025 concerne le décret n° 2024-610 et ne date pas la réforme proposée. Discordance préexistante à vérifier hors lot : L. 112-16 vise encore 1609 quatervicies A CGI avec une note de concordance CIBS, alors que R. 112-14 vise L. 6360-1 transports. Ne pas présumer ces listes identiques et ne pas modifier ici les champs par inférence. Le préalable de l'avis de la commission à celui de l'ACNUSA est conservé.",
        impact('coordination_only',
               "L'objet de l'avis existant est coordonné avec la suppression du premier passage à R. 112-11 ; tous les circuits et délais du texte officiel de R. 112-14 restent inchangés. Ce n'est pas une nouvelle consultation ni une seconde fusion comptabilisée.",
               "La concordance des champs transports/CGI/CIBS de L. 112-16 requiert un contrôle documentaire hors du lot. Aucun raccourcissement des deux ou quatre mois, ni économie chiffrée, n'est établi ici.",
               "Aucune charge nouvelle n'est identifiée : la commission examine les mêmes indices dans son avis existant sur le projet ; aucun avis supplémentaire, rapport ou donnée nouvelle n'est imposé.",
               [effect('coordination', cce,
                       "Maintien explicite de l'examen des indices dans l'avis existant sur le projet, après retrait de la consultation séparée.",
                       "R. 112-14 organise l'avis sur le projet ; R. 112-11 exige séparément l'avis initial sur les indices avant lancement.",
                       "Même avis sur le projet et mêmes délais ; le texte précise qu'il comprend les indices et qu'aucune consultation distincte avant lancement n'est requise.",
                       'legal_duty', "Commission consultative de l'environnement, préfets et ACNUSA dans leurs champs respectifs.",
                       "Procédures lancées à compter de l'entrée en vigueur de la loi ; anciennes procédures et avis réguliers préservés.",
                       "Aucun nouveau passage obligatoire ; coordination de la mesure portée par R. 112-11.",
                       "La commission consultative de l'environnement dispose d'un délai de deux mois à compter de la date de la saisine, soit par le préfet, soit par l'Autorité de contrôle des nuisances aéroportuaires, pour formuler son avis sur le projet communiqué.",
                       "Aucune consultation distincte de cette commission sur ces valeurs n'est requise avant la décision d'établir ou de réviser le plan.")]),
        benefit="Les avis tacites favorables restent acquis au terme des délais de deux mois pour la commission et de quatre mois pour l'ACNUSA, selon les saisines prévues. La présence éventuelle de la commission, les champs respectifs des aérodromes et les procédures anciennes sont préservés ; aucune nouvelle condition d'accès à un avis favorable n'est ajoutée.")

retain('R112-15',
       "Maintien intégral de l'enquête publique sur le projet éventuellement modifié et de son régime particulier pour les aérodromes de défense. Cette participation est expressément requise par L. 112-16 et protège les riverains soumis au plan ; elle ne constitue pas le doublon de consultation technique supprimé à R. 112-11. Aucun accord ou justificatif privé autonome n'est ajouté par cet article.",
       "L. 112-16 et R. 112-16 relus. Les références R. 571-59 et suivants, L. 123-19-8, L. 123-19-9 et R. 123-46 du code de l'environnement restent intégralement conservées ; leurs textes intégraux ne figurent pas dans le lot ni dans le corpus urbanisme consulté. Leur vérification externe reste identifiée, sans prétendre les avoir réécrits. Les annonces propres à l'enquête ne sont pas retirées par la réforme de R. 112-10/17.",
       "Aucune partie de la source officielle n'est retirée : enquête, adaptation après avis et limites légales de défense subsistent. Aucun allègement fictif de participation publique n'est déclaré.",
       "Les dispositions environnementales citées restent à vérifier dans leur propre corpus ; aucune conformité européenne ni purge de leurs formalités n'est affirmée.",
       "Aucune charge nouvelle n'est identifiée : les mêmes exigences d'enquête et les mêmes réserves de défense restent en vigueur, sans dossier parallèle nouveau.",
       "Les limites et conditions spécifiques à la défense demeurent applicables dans les trois affectations prévues, y compris pour les futurs plans éligibles. La protection des informations légalement secrètes ne s'étend pas par cette conservation aux autres éléments communicables.")

retain('R112-16',
       "Maintien intégral de l'approbation préfectorale, conjointe dans les cas interdépartementaux, des accords exprès sectoriels et de la motivation dans tous les cas. Après suppression de ces accords au lancement dans R. 112-8, ils constituent l'unique contrôle ministériel de ce circuit pour les intérêts de défense, d'aviation nationale et transfrontaliers. L'enquête reste susceptible de conduire à modifier le projet.",
       "R. 112-8, R. 112-15 et L. 112-16 relus. Cet article maintenu ne rétablit pas un accord pour la seule décision de lancement : il ne concerne que l'arrêté d'approbation. Conserver affectations exclusive/principale pour la défense, intérêt national hors défense principale, aérodromes étrangers et motivation environnementale systématique.",
       "La totalité du texte officiel est maintenue sans nouveau visa. La réduction du circuit de lancement est démontrée à R. 112-8 et n'est pas une seconde suppression dans cet article.",
       "Les délais réels d'obtention des accords finaux et les règles aéronautiques hors corpus ne sont pas évalués ; aucun accord d'approbation n'est présenté comme supprimé.",
       "Aucune charge nouvelle n'est identifiée : les accords finaux, la motivation et les autorités d'approbation étaient tous déjà exigés par le texte source.")

xml = paragraphs(
    "Le préfet de département notifie aux maires des communes concernées et, le cas échéant, aux présidents des établissements publics de coopération intercommunale compétents copie de l'arrêté et du plan d'exposition au bruit approuvé.",
    "L'arrêté et le plan d'exposition au bruit sont tenus à la disposition du public à la mairie de chacune des communes concernées, le cas échéant aux sièges des établissements publics de coopération intercommunale compétents, ainsi qu'à la préfecture.",
    "Mention des lieux où les documents peuvent être consultés est affichée dans les mairies et, le cas échéant, aux sièges des établissements publics de coopération intercommunale compétents. L'insertion de cette mention dans deux journaux à diffusion régionale ou locale dans le département n'est pas requise.",
    "Ces dispositions s'appliquent aux arrêtés d'approbation pris à compter de l'entrée en vigueur de la loi. Les arrêtés antérieurs demeurent soumis aux mesures de publicité qui leur étaient applicables. Les publicités régulièrement accomplies conservent leurs effets et aucun délai de recours expiré n'est rouvert par cette modification.")
rewrite('R112-17', xml,
        "Réforme de fond limitée à la suppression des deux annonces de presse après approbation. La copie intégrale aux élus, la consultation dans chaque mairie, aux sièges intercommunaux et à la préfecture et l'affichage des lieux demeurent. Aucun transfert vers une publicité électronique obligatoire n'est ajouté. Les actes antérieurs et leurs délais restent protégés.",
        "Renvoi de R. 112-7 vérifié : la fin de vigueur de l'ancien plan dépend toujours des publicités requises par le présent article dans son champ temporel ; pas d'entrée en vigueur automatique avant leur accomplissement. L. 112-16 impose que le plan soit à disposition du public, ce qui demeure assuré. Les publicités des enquêtes environnementales restent distinctes. Même mesure que les doubles annonces retirées à R. 112-10 et R. 113-11, sans addition de prétendues taxes supprimées.",
        impact('material_reduction',
               "Deux insertions de presse sont effectivement retirées à l'approbation, avec maintien intégral des notifications, des lieux de consultation et de l'affichage. La réforme ne supprime pas la publicité ni l'accès au plan.",
               "Les coûts d'annonces et le solde public restent inconnus. Les anciennes approbations, les formalités d'enquête et les délais de recours déjà expirés ne sont pas affectés.",
               "Aucune charge nouvelle n'est identifiée : les services continuent les seules notifications, mises à disposition et affichages déjà requis, sans nouvelle plateforme ou publication de substitution.",
               [effect('obligation_removed', press,
                       "Retrait de la double annonce de presse des lieux de consultation du plan approuvé.",
                       "Mention des lieux de consultation dans deux journaux régionaux ou locaux, en plus de l'affichage et de la disponibilité du plan.",
                       "Affichage existant, consultation physique et notification conservés ; aucune insertion de presse sur ce fondement pour les nouvelles approbations.",
                       'legal_duty', "Préfets et services assurant la publicité des plans d'exposition au bruit approuvés.",
                       "Arrêtés d'approbation pris à compter de l'entrée en vigueur de la loi ; publicités antérieures et délais expirés préservés.",
                       "Aucun nouveau support imposé ; les moyens d'accès locaux existent déjà.",
                       "Mention des lieux où les documents peuvent être consultés est insérée dans deux journaux à diffusion régionale ou locale dans le département et affichée dans les mairies et, le cas échéant, aux sièges des établissements publics de coopération intercommunale compétents.",
                       "L'insertion de cette mention dans deux journaux à diffusion régionale ou locale dans le département n'est pas requise.")]),
        removed=["Double insertion obligatoire dans deux journaux régionaux ou locaux de la mention des lieux de consultation du plan d'exposition au bruit approuvé."])

retain('R113-1',
       "Maintien intégral de l'information du Centre national de la propriété forestière sur la prescription des documents d'urbanisme et les classements boisés. Cette information ciblée assure l'intervention de l'organisme forestier compétent ; elle ne prescrit pas un agrément ou une déclaration aux propriétaires. La lecture des dispositifs généraux de notification ne démontre pas que le Centre reçoit nécessairement les mêmes décisions par un autre circuit.",
       "L. 113-1, L. 132-7/9/10/13, L. 153-11 et L. 153-16/17 relus : le Centre ne figure pas dans les listes de personnes publiques associées de L. 132-7 et L. 132-9. Ne pas prétendre à un doublon établi sur la seule présence de consultations forestières dans d'autres cas. Conserver le rôle du maire ou président intercommunal et les documents tenant lieu de PLU. La coquille L.L. 153-8 dans L. 153-11 est signalée par sa propre note source et ne modifie pas cette analyse.",
       "L'article officiel reste intégralement maintenu après examen du circuit d'information. Aucune notification redondante démontrée n'est supprimée et aucun gain nouveau n'est annoncé.",
       "Les systèmes locaux d'échange peuvent déjà éviter des copies, mais leur fonctionnement n'est pas documenté. Il n'est pas établi qu'une suppression de l'information laisserait le Centre informé de chaque classement.",
       "Aucune charge nouvelle n'est identifiée : le même envoi ciblé est maintenu, sans périodicité, registre, format ou pièce supplémentaire.")

retain('R113-2',
       "Maintien intégral du pouvoir de rétablir un boisement détruit illicitement et de l'exécution subsidiaire aux frais du propriétaire défaillant. Il s'agit de réparation d'un dommage et non d'un prélèvement général à supprimer. Le délai de trois ans, ses deux points de départ et le préalable de non-exécution de la plantation ou du semis encadrent le pouvoir administratif ; les retirer élargirait la charge ou rendrait la protection inopérante.",
       "Lecture de L. 113-1 et L. 113-2. Conserver le délai courant après l'année des déboisements ou travaux illicites, puis celui courant de la fin de l'année prévue pour les travaux prescrits. Le recouvrement comme en matière de contributions directes n'est pas un impôt nouveau. Les garanties générales de procédure, responsabilité et recours restent dans leurs textes propres.",
       "Le texte officiel complet demeure : réparation ciblée, défaillance préalable et récupération du coût réel selon le régime source. Aucun montant de taxe ou délai n'est modifié.",
       "Le coût des remises en état et la situation de chaque propriétaire ne sont pas évalués. La réforme de formalités du présent lot n'amnistie pas les déboisements illicites.",
       "Aucune charge nouvelle n'est identifiée : ni l'assiette des frais ni le délai d'intervention ni les hypothèses de réparation ne sont étendus.")

xml = paragraphs(
    "L'autorisation de construire sur une partie du terrain classé prévue au 2° de l'article L. 113-3 est demandée au préfet.",
    "La demande est accompagnée d'un plan de situation du terrain classé, d'un plan parcellaire de la propriété dans laquelle ce terrain est compris et d'un état des plantations ainsi que de l'étude d'impact définie à l'article R. 122-5 du code de l'environnement.",
    "Le demandeur n'est tenu de joindre ni une pièce justifiant de sa qualité de propriétaire ni une attestation s'y substituant. Cette dispense ne modifie pas la condition de propriété prévue à l'article L. 113-3, les droits des tiers ni les règles applicables à la fraude.",
    "Ces dispositions s'appliquent aux demandes déposées à compter de l'entrée en vigueur de la loi et aux demandes en cours à cette date, sans nouveau dépôt ni reprise des délais. Les pièces déjà fournies demeurent utilisables et n'ont pas à être refaites du seul fait de la présente modification. Les autorisations régulièrement accordées avant cette date conservent leurs effets.")
rewrite('R113-3', xml,
        "Réduction de fond du dossier de la dérogation boisée : retrait de la pièce de propriété obligatoirement jointe, sans attestation de remplacement. La qualité de propriétaire reste une condition de L. 113-3. Les plans de situation et parcellaire, l'état des plantations, l'étude d'impact, la saisine du préfet et le dispositif compensatoire sont maintenus. Les dossiers en cours profitent de la dispense sans refaire les pièces. Cette suppression dépasse le seul réemploi d'un justificatif déjà légalement disponible : aucune pièce de propriété n'est exigée au dépôt sur ce fondement.",
        "L. 113-3/4, R. 113-4 à R. 113-10 et R. 113-12 relus : conserver la limite du dixième, le délai d'acquisition de cinq ans, le plafond de valeur, la cession, l'accord communal et le décret dans leurs textes propres. La dispense de pièce jointe n'est ni transfert de propriété ni droit de construire pour un non-propriétaire. Elle ne préjuge pas des pièces authentiques nécessaires à la cession elle-même. R. 122-5 environnement reste le fondement de l'étude conservée, sans réécriture ni contrôle de ses rubriques hors corpus. La source n'impose pas expressément deux supports matériels pour les deux plans ; aucun gain de fusion de supports n'est donc revendiqué et aucune exigence de supports distincts n'est créée.",
        impact('material_reduction',
               "Comparée à la source entière, la proposition supprime le justificatif de propriété à joindre au dépôt. Les deux plans, l'étude d'impact et l'état des plantations sont conservés ; aucune autorisation n'est prétendue supprimée. La dispense ne se limite pas au réemploi d'une pièce déjà détenue par l'administration.",
               "La propriété doit toujours exister et les formalités civiles de cession restent distinctes. Le coût de la pièce retirée et le solde global de complexité ne sont pas chiffrés. La source n'impose pas expressément des supports graphiques séparés : aucun gain sur ce point n'est établi.",
               "Aucune charge nouvelle n'est identifiée : aucune attestation ne remplace la pièce retirée, les informations graphiques restent identiques et aucun demandeur ne doit refaire son dossier ni recommencer les délais.",
               [effect('obligation_removed', 'espaces-boises-dispense-piece-propriete-depot',
                       "Suppression de la pièce de propriété à joindre à la demande, sans attestation équivalente.",
                       "Le demandeur propriétaire joint obligatoirement des pièces prouvant cette qualité au dossier de l'autorisation de L. 113-3, 2°.",
                       "Aucune pièce ni attestation de propriété n'est jointe sur ce fondement ; la condition légale de propriété et la cession restent requises.",
                       'legal_duty', "Propriétaires demandant la dérogation de construction compensatoire sur terrain boisé classé.",
                       "Nouvelles demandes et demandes en cours à l'entrée en vigueur ; autorisations antérieures et droits des tiers préservés.",
                       "Aucun justificatif de remplacement ; les actes civils de la cession restent distincts.",
                       plain(BY_NUMBER['R113-3']['source_xml']).split('préfet. ', 1)[1],
                       "Le demandeur n'est tenu de joindre ni une pièce justifiant de sa qualité de propriétaire ni une attestation s'y substituant.")]),
        removed=["Obligation de joindre à la demande les pièces justifiant de la qualité de propriétaire, sans attestation nouvelle en remplacement."],
        benefit="La possibilité favorable de construire à titre de compensation de la cession du surplus reste ouverte aux propriétaires futurs remplissant L. 113-3 et L. 113-4. Le dossier allégé ne supprime ni cette dérogation ni ses deux voies de compensation, et ne restreint pas les autorisations déjà accordées.")

retain('R113-4',
       "Maintien intégral de l'instruction préfectorale, de l'avis financier et du rapport sur le terrain, les constructions et le défrichement. Ces éléments permettent de contrôler le plafond de compensation de L. 113-3 et de préparer le décret dérogatoire sans méconnaître les conséquences forestières. La source n'établit pas que les évaluations de R. 113-5 imposent une seconde consultation distincte : aucun doublon financier fictif n'est compté.",
       "L. 113-3/4 et R. 113-5/7/8 relus. Conserver les alternatives départementale/régionale de la direction des finances publiques et tous les objets du rapport. L. 341-5 forestier est une référence de fond conservée, non une dispense de protection ; son texte n'est pas joint au présent corpus et reste à vérifier dans le code concerné.",
       "L'article officiel entier est maintenu : les justifications de la dérogation, de la valeur de cession et de l'examen forestier demeurent. Aucun second avis supprimé n'est inventé à partir du seul renvoi aux évaluations.",
       "La pratique de réunion de l'avis et des évaluations financières n'est pas documentée. Aucune réduction de temps ou de coût de ce circuit ne peut être démontrée dans le seul lot.",
       "Aucune charge nouvelle n'est identifiée : l'instruction, le rapport et la consultation sont maintenus dans leurs champs, sans pièce privée supplémentaire.",
       "L'instruction garantit l'examen de la demande favorable de construction compensatoire sans fermer son accès futur. La consultation financière et l'analyse du terrain soutiennent la dérogation et son plafond de valeur, sans introduire une taxe ni un critère d'exclusion nouveau.")

retain('R113-5',
       "Maintien intégral des trois évaluations : terrain à bâtir offert, terrain classé cédé gratuitement et surcroît de valeur de la partie conservée. Elles rendent possible une compensation dans la limite de L. 113-3 et protègent à la fois le propriétaire et la collectivité. Les supprimer sans méthode alternative retirerait le mécanisme favorable ou son encadrement financier ; aucune taxe autonome ne figure dans ce texte.",
       "L. 113-3, R. 113-4 et R. 113-9/10 relus. Préserver les deux modalités départementale ou régionale de l'évaluation et la prise en compte des possibilités de construction dans le seul dernier terme. Ne pas assimiler valeur de compensation et assiette d'un prélèvement.",
       "Les évaluations officielles sont maintenues en entier, sans nouveau plafond ni modification de leur assiette patrimoniale. Aucune baisse de taxe ou de dépense nationale n'est revendiquée.",
       "Les valeurs concrètes et les coûts d'expertise ne sont pas connus. Les actes de cession et leur fiscalité distincte ne sont pas modifiés par ce maintien.",
       "Aucune charge nouvelle n'est identifiée : mêmes trois objets de valeur, même autorité d'évaluation et mêmes éléments de construction, sans nouvelle expertise privée imposée.",
       "La compensation en terrain à bâtir ou en autorisation de construire demeure accessible aux futurs propriétaires éligibles selon L. 113-3. Les évaluations qui rendent ces avantages calculables sont conservées intégralement, sans diminution du plafond favorable ni nouveau délai.")

xml = paragraphs(
    "Sauf s'il apparaît que la demande ne peut être accueillie, le préfet saisit du dossier le maire de chacune des communes intéressées en vue de la délibération du conseil municipal sur l'accord prévu au troisième alinéa de l'article L. 113-4. Si le conseil municipal ne s'est pas prononcé dans les quatre mois de cette saisine, l'accord est réputé donné.",
    "L'accord réputé donné ne vaut ni autorisation de construire ni décret de déclassement ; les autres conditions prévues aux articles L. 113-3 et L. 113-4 demeurent applicables.",
    "La règle d'accord tacite s'applique aux saisines des communes effectuées à compter de l'entrée en vigueur de la loi. Les saisines antérieures restent régies par les dispositions qui leur étaient applicables ; les accords, refus et autorisations antérieurs ne sont pas remis en cause par cette modification.")
rewrite('R113-6', xml,
        "Réforme de fond favorable : à quatre mois, le silence du conseil municipal vaut accord au lieu de refus. La saisine de chacune des communes, la délibération possible, le délai et l'exception des demandes manifestement irrecevables sont conservés. Il n'y a ni suppression de l'accord exigé par L. 113-4 ni autorisation automatique de construire ; le décret et les conditions compensatoires restent nécessaires.",
        "L. 113-3/4, R. 113-7/8/9/10 relus. L. 113-4 exige l'accord communal sans exiger expressément une délibération positive ; le règlement proposé précise son acquisition tacite. Le désaccord exprès reste un obstacle à la transmission de R. 113-7. Le silence étatique de R. 113-8 reste un refus après deux mois : ne pas étendre à ce décret le silence favorable communal. Les anciens refus tacites ne sont pas annulés ou rouverts automatiquement.",
        impact('mixed',
               "La source impose un refus tacite après quatre mois ; la proposition en fait un accord tacite, ce qui enlève le veto résultant de la seule inertie communale. Pour refuser, la commune doit désormais se prononcer expressément dans ce délai. Le gain pour le demandeur s'accompagne de cette exigence d'intervention pour la commune ; le solde net n'est pas établi.",
               "Aucun raccourcissement du délai de quatre mois ni droit automatique au décret n'est établi. Les anciennes saisines et le refus tacite étatique restent hors de cet allègement ; le coût de vigilance et de délibération des communes n'est pas chiffré.",
               "La commune qui veut refuser ne peut plus compter sur son silence : elle doit délibérer dans les quatre mois existants. Cette exigence conditionnelle est nouvelle. Aucune charge nouvelle n'est identifiée pour le demandeur : mêmes dossier et saisine, sans confirmation, certificat ou délai supplémentaire.",
               [effect('relief_extended', 'espaces-boises-accord-communal-tacite-favorable',
                       "Substitution de l'accord tacite communal au refus tacite après quatre mois.",
                       "Sans délibération du conseil municipal dans les quatre mois de la saisine, l'accord nécessaire à la dérogation est réputé refusé.",
                       "Sans délibération dans les mêmes quatre mois, l'accord est réputé donné ; une décision de décret demeure nécessaire selon les autres textes.",
                       'legal_duty', "Propriétaires sollicitant l'autorisation compensatoire et communes dont l'accord est demandé.",
                       "Saisines communales effectuées à compter de l'entrée en vigueur de la loi ; anciennes saisines et décisions préservées.",
                       "Pas de confirmation à la charge du demandeur ; le décret existant subsiste. La commune doit exprimer son refus dans les quatre mois si elle entend s'opposer.",
                       "Si le conseil municipal ne s'est pas prononcé dans les quatre mois de cette saisine, l'accord est réputé refusé.",
                       "Si le conseil municipal ne s'est pas prononcé dans les quatre mois de cette saisine, l'accord est réputé donné."),
                effect('obligation_added', 'espaces-boises-accord-communal-tacite-favorable',
                       "Nécessité d'une prise de position expresse dans les quatre mois pour la commune qui veut refuser l'accord.",
                       "La commune peut laisser naître un refus tacite en ne se prononçant pas pendant quatre mois.",
                       "Le silence produit l'accord ; pour s'opposer la commune doit se prononcer dans les quatre mois, sans obligation générale de refuser ou de délibérer lorsqu'elle accepte.",
                       'legal_duty', "Conseils municipaux des communes saisies qui entendent refuser l'accord.",
                       "Saisines communales effectuées à compter de l'entrée en vigueur ; anciennes saisines régies par leur droit antérieur.",
                       "Vigilance et délibération nécessaires en cas d'opposition, dans le délai préexistant ; coût non chiffré. Aucun dossier nouveau pour le propriétaire.",
                       plain(BY_NUMBER['R113-6']['source_xml']),
                       "Sauf s'il apparaît que la demande ne peut être accueillie, le préfet saisit du dossier le maire de chacune des communes intéressées en vue de la délibération du conseil municipal sur l'accord prévu au troisième alinéa de l'article L. 113-4. Si le conseil municipal ne s'est pas prononcé dans les quatre mois de cette saisine, l'accord est réputé donné.")]),
        removed=["Effet de refus automatique attaché au seul silence du conseil municipal pendant quatre mois sur l'accord de construction compensatoire."],
        benefit="La dérogation compensatoire de L. 113-3 reste accessible aux nouvelles situations éligibles. Le silence communal devient favorable après quatre mois sans modifier les autres conditions ; les accords exprès et autorisations acquis demeurent protégés et aucune ancienne compensation n'est retirée.")

retain('R113-7',
       "Maintien intégral de la transmission préfectorale au ministre avec avis et propositions, sauf désaccord communal. Ce circuit est nécessaire au décret exigé par L. 113-4 et précisé à R. 113-8 ; sa suppression réglementaire isolée bloquerait l'avantage compensatoire. La formule « désaccord » vise toujours une opposition, et ne transforme pas en opposition l'accord tacite favorable désormais prévu à R. 113-6.",
       "L. 113-4 et R. 113-6/8 relus. Conserver la transmission, qui n'est pas un nouveau dossier déposé par le propriétaire. La rédaction source « Sauf, en cas » présente une ponctuation maladroite sans incohérence normative nécessitant une réécriture. Aucun ministère ou visa supplémentaire n'est ajouté.",
       "Le texte source complet est conservé pour rendre opérante l'autorisation par décret. L'amélioration du silence communal est portée par R. 113-6 et n'est pas recomptée comme transmission supprimée.",
       "La suppression du décret nécessiterait une décision législative sur L. 113-4 et une coordination de R. 113-8/9/10/12, qui ne sont pas réalisées par cet article maintenu.",
       "Aucune charge nouvelle n'est identifiée : mêmes transmission et avis internes, sans seconde demande, nouvelle pièce ou délai supplémentaire imposé au propriétaire.",
       "La transmission permet aux propriétaires futurs éligibles de bénéficier de la construction compensatoire ; elle reste ouverte en l'absence de désaccord communal, y compris lorsque l'accord est acquis tacitement selon le nouveau R. 113-6. Aucun avantage acquis n'est fermé.")

retain('R113-9',
       "Maintien intégral de la désignation du bénéficiaire public, de la protection et de l'entretien du terrain cédé, du périmètre constructible et du déclassement. La substitution du décret à l'autorisation de défrichement est un avantage qui évite un titre distinct ; elle reste applicable aux futures opérations, sans être limitée aux droits acquis. Ces éléments rendent le mécanisme compensatoire opérant et assurent sa contrepartie environnementale.",
       "L. 113-3/4/5, R. 113-8/10/12 relus. La dispense de titre forestier séparé vise seulement la partie déclassée. L. 341-3 du code forestier n'est pas reproduit dans le lot ; la vérification de son régime propre reste extérieure, sans prétendre supprimer les autres autorisations forestières. Le décret ne dispense pas des autres règles de construction, comme le confirme R. 113-10.",
       "L'article officiel entier demeure, notamment le titre unique valant autorisation de défrichement pour la seule partie déclassée. Ce bénéfice préexistant est conservé et n'est pas présenté comme une nouvelle fusion.",
       "Les autorisations forestières hors partie déclassée, les règles environnementales et la délivrance des permis distincts ne sont pas supprimées ; leurs coûts ne sont pas évalués.",
       "Aucune charge nouvelle n'est identifiée : mêmes effets du décret et mêmes engagements publics, sans rétablissement d'une seconde demande de défrichement dans le champ dispensé.",
       "Le décret continue à tenir lieu de l'autorisation de défrichement de L. 341-3 pour la partie déclassée. Cet avantage et la faculté de construction compensatoire demeurent pour toute future opération remplissant les conditions légales, sans pièce ou titre de remplacement ajouté.")

retain('R113-10',
       "Maintien intégral de la fixation par le décret des possibilités de construction offertes à titre compensatoire. Il s'agit du contenu utile de l'avantage de L. 113-3, 2°, et non d'une autorisation supplémentaire. La réserve des autres règles de construction empêche de confondre déclassement dérogatoire et permis général ; aucune formalité autonome superflue n'est identifiée.",
       "L. 113-3/4 et R. 113-8/9/12 relus. Conserver le renvoi au 2° sans étendre le décret à la compensation par terrain à bâtir du 1°. Les allègements de dossier et d'accord communal restent portés par R. 113-3 et R. 113-6 ; aucun double effet de suppression n'est enregistré ici.",
       "La source officielle entière est conservée afin que le décret définisse les droits à construire compensatoires. Aucun régime supplémentaire n'est fusionné et aucun permis distinct n'est supprimé.",
       "La constructibilité concrète reste subordonnée aux règles propres et aux conditions légales de cession ; aucun volume de logements, économie ou délivrance automatique n'est démontré.",
       "Aucune charge nouvelle n'est identifiée : mêmes contenu du décret et réserve des règles existantes, sans nouvelle condition, pièce ou délai.",
       "Le décret continue à accorder les possibilités de construction de L. 113-3, 2°, pour les futurs propriétaires et terrains éligibles. L'avantage n'est ni abrogé ni réservé au stock ancien ; les conditions de valeur, de cession et les droits acquis demeurent dans leur champ.")

xml = paragraphs(
    "Le décret fait l'objet d'une mention au Journal officiel de la République française.",
    "Aucune insertion de cette mention dans des journaux régionaux ou locaux n'est exigée aux frais du pétitionnaire.",
    "Ces dispositions s'appliquent aux décrets pris à compter de l'entrée en vigueur de la loi. Les décrets antérieurs restent soumis aux mesures de publicité qui leur étaient applicables et les frais légalement engagés pour ces mesures demeurent régis par les dispositions antérieures. Aucune restitution générale des frais antérieurs n'est instituée ; les droits à remboursement d'un paiement indu et les recours restent préservés.")
rewrite('R113-11', xml,
        "Réforme de fond : retrait de la double annonce de presse aux frais du pétitionnaire, qui s'ajoute à la mention au Journal officiel. Cette dernière reste exigée. L'allègement porte sur une dépense et une formalité de publicité imposées, non sur une taxe. La dérogation de construction compensatoire et ses effets restent intacts ; aucun autre support payant ou dépôt ne remplace les annonces supprimées.",
        "R. 113-8 à R. 113-12 relus : conserver le décret, la mention au Journal officiel et le délai de transfert de deux ans courant de la publication du décret. Les règles de notification, d'accès aux actes et de recours sur leurs fondements autonomes ne sont pas supprimées. Même mesure de retrait des doubles annonces que R. 112-10/17, avec population et stade propres ; ne pas ajouter une prétendue taxe ni chiffrer une économie nationale à partir de tarifs inconnus.",
        impact('material_reduction',
               "La source met deux annonces locales à la charge du pétitionnaire ; la proposition retire cette obligation et sa dépense pour les nouveaux décrets tout en conservant la mention au Journal officiel. Aucune valeur de taxe ou compensation foncière n'est modifiée.",
               "L'économie individuelle dépend du prix des annonces, non fourni ; les frais des anciens décrets et les autres formalités de publicité légalement autonomes ne sont pas abolis.",
               "Aucune charge nouvelle n'est identifiée : la mention au Journal officiel était déjà requise et aucun envoi, registre ou publication de remplacement n'est créé.",
               [effect('obligation_removed', press,
                       "Suppression de la double annonce locale du décret financée par le pétitionnaire.",
                       "Le préfet fait insérer la mention du décret dans deux journaux régionaux ou locaux aux frais du pétitionnaire, outre le Journal officiel.",
                       "Aucune insertion de presse ni frais correspondants sur ce fondement pour les nouveaux décrets ; mention au Journal officiel maintenue.",
                       'legal_duty', "Pétitionnaires bénéficiant du décret de construction compensatoire et préfets chargés de sa publicité.",
                       "Décrets pris à compter de l'entrée en vigueur ; anciens frais légaux préservés, avec recours et remboursement des indus.",
                       "Aucun report de la dépense d'insertion vers un autre financeur ; la formalité disparaît sans remplacement.",
                       "Le préfet fait en outre insérer cette mention, aux frais du pétitionnaire, dans deux journaux régionaux ou locaux diffusés dans le département.",
                       "Aucune insertion de cette mention dans des journaux régionaux ou locaux n'est exigée aux frais du pétitionnaire.")]),
        removed=["Obligation préfectorale de publier la mention du décret dans deux journaux régionaux ou locaux et prise en charge obligatoire de ces deux annonces par le pétitionnaire."],
        benefit="La construction compensatoire et le décret qui tient lieu de défrichement demeurent accessibles aux futures opérations éligibles. La suppression des frais de presse ne réduit aucun de ces avantages ; elle laisse subsister la publicité au Journal officiel et protège les recours ou remboursements d'indus antérieurs.")


def validate():
    assert len(SOURCES) == len(ANSWERS) == 24
    assert set(ANSWERS) == set(BY_NUMBER)
    allowed_kinds = {'tax_removed', 'tax_reduced', 'obligation_removed', 'obligation_merged',
                     'authorization_removed', 'regime_merged', 'deadline_reduced',
                     'compliance_cost_reduced', 'tax_increased', 'obligation_added',
                     'deadline_increased', 'complexity_added', 'financing_transfer',
                     'payment_deferred', 'relief_extended', 'relief_preserved', 'coordination'}
    allowed_tags = {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em',
                    'u','sup','sub','ul','ol','li','div','span','blockquote'}

    class MarkupCheck(HTMLParser):
        def handle_starttag(self, tag, attrs):
            assert tag in allowed_tags, tag
            for name, value in attrs:
                assert name in {'rowspan', 'colspan'} and value.isdigit(), (name, value)

    for s in SOURCES:
        a = ANSWERS[s['number']]
        for k in ['code_id','source_id','source_sha256','number']:
            assert a[k] == s[k]
        im = a['substantive_impact']
        assert im['version'] == 1
        for k in ['assessment','scope_limitations','new_burdens_review']:
            assert isinstance(im[k], str) and len(im[k]) >= 40, (a['number'], k)
        if s.get('benefit_check_required'):
            assert len(a['benefit_review']) >= 100
        if a['status'] == 'retained_unchanged':
            assert a['proposed_xml'] is None
            assert a['classification'] == im['classification'] == 'retained_necessary'
            assert im['effects'] == []
        else:
            MarkupCheck().feed(a['proposed_xml'])
            assert a['proposed_xml']
        if a.get('change_type') == 'full_repeal':
            assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé'))
            assert len(a['repeal_scope']) >= 30
        if a.get('change_type') == 'normative_reduction':
            assert a['removed_provisions'] and all(len(x) >= 30 for x in a['removed_provisions'])
        seen = set()
        for e in im['effects']:
            key = e['measure_id'], e['kind']
            assert key not in seen, ('Duplicate measure and effect in one article', a['number'], key)
            seen.add(key)
            assert e['kind'] in allowed_kinds
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
            assert 6 <= len(e['measure_id']) <= 96
            assert len(e['source_quote']) >= 12 and len(e['proposed_quote']) >= 12
            assert e['source_quote'] in plain(s['source_xml']), (a['number'],'source_quote',e['source_quote'])
            assert e['proposed_quote'] in plain(a['proposed_xml']), (a['number'],'proposed_quote',e['proposed_quote'])
            assert e['source_quote'] in stripped_plain(s['source_xml']), (a['number'],'source_quote_without_inserted_spaces',e['source_quote'])
            assert e['proposed_quote'] in stripped_plain(a['proposed_xml']), (a['number'],'proposed_quote_without_inserted_spaces',e['proposed_quote'])
            assert e['unit'] in {'percent','euro','legal_duty','regime','calendar_days','working_days','financing','other'}


validate()
ordered = [ANSWERS[s['number']] for s in SOURCES]
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'article_count': len(ordered),
                  'rewritten': sum(a['status'] == 'rewrite_draft' for a in ordered),
                  'retained': sum(a['status'] == 'retained_unchanged' for a in ordered),
                  'effects': sum(len(a['substantive_impact']['effects']) for a in ordered),
                  'unique_measures': len({e['measure_id'] for a in ordered for e in a['substantive_impact']['effects']})}, ensure_ascii=False))
