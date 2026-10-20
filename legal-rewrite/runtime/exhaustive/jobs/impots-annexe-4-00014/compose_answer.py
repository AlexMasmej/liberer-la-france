import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}

def put(number, paragraphs, reason, notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }

put('51 F', [
    "Le directeur régional des douanes et droits indirects statue sur la demande après son instruction. Au cours de cette instruction, le requérant peut être entendu.",
    "La décision est notifiée au requérant dans un délai maximal de quatre mois à compter de la réception de la demande.",
], "À droit constant : distinguer l'instruction, pendant laquelle le requérant peut être entendu, de la décision du directeur et de sa notification. Aucune réforme de fond prévue par policy.json ne concerne cette procédure de rachat.",
    "Le délai maximal de quatre mois court à compter de la réception de la demande, et non de la fin de l'instruction. Les deux alinéas et le caractère facultatif de l'audition sont conservés.")

put('51 G', [
    "Si l'administration refuse le rachat, le requérant doit attendre un an à compter de la notification de cette décision avant de déposer une nouvelle demande.",
], "À droit constant : exprimer directement le délai d'attente imposé au requérant après un refus de rachat et préciser son point de départ. Aucune réforme de fond n'est applicable à cet article.",
    "Le délai d'un an reste attaché à la notification du refus de l'administration. Il se distingue du délai prévu à l'article 51 H, qui court à compter du refus du requérant.")

put('51 H', [
    "Si l'administration accepte le rachat, sa décision indique expressément :",
    "Le prix proposé au requérant. Ce prix ne peut, en aucun cas, être inférieur à la valeur de récupération des matières composant les organes principaux des appareils ;",
    "Les conditions de paiement ;",
    "Les conditions de livraison ou de gardiennage du ou des appareils.",
    "À compter de la date de notification de la décision, le requérant dispose d'un mois pour accepter ou refuser le bénéfice du rachat au prix fixé.",
    "S'il donne son accord, le requérant doit livrer le ou les appareils, ou en conserver la garde, dans les conditions qui lui ont été notifiées.",
    "S'il refuse, le requérant doit attendre un an à compter de la date de son refus avant de déposer une nouvelle demande de rachat.",
], "À droit constant : séparer le contenu obligatoire de la décision, le choix du requérant et les conséquences de son accord ou de son refus. Le prix plancher et les modalités de garde sont explicités sans réforme de fond.",
    "Les sept alinéas sont maintenus. Le mois de réponse court à compter de la notification ; l'année d'attente court à compter du refus du requérant. Aucune conséquence nouvelle n'est ajoutée en cas de silence. Le prix plancher porte sur les matières des organes principaux, sans extension à la valeur totale de l'appareil.")

put('51 bis', [
    "Pour obtenir l'autorisation d'exercer la profession de loueur d'alambic ambulant, le requérant adresse une demande écrite à chaque direction régionale des douanes et droits indirects dans le ressort de laquelle se trouve un lieu d'utilisation de son ou de ses appareils.",
], "À droit constant : identifier le demandeur, la forme écrite de sa demande et chacune des directions régionales destinataires selon le lieu d'utilisation des appareils. Aucune réforme de fond n'est introduite.",
    "La demande reste nécessaire auprès de chaque direction régionale territorialement concernée ; elle n'est pas remplacée par une demande unique. Articulation maintenue avec le contenu du dossier fixé à l'article 51 ter.")

put('51 ter', [
    "La demande d'autorisation comporte les renseignements suivants :",
    "a. Les nom et prénoms du requérant, ou sa raison sociale, ainsi que l'adresse de son domicile ;",
    "b. Le nombre d'alambics à employer, leur nature, leur capacité et leur débit ;",
    "c. Le cas échéant, la date et la nature des autorisations que le requérant a obtenues dans d'autres départements.",
], "À droit constant : préciser l'objet de la demande et rendre les renseignements techniques plus lisibles, en conservant les rubriques a, b et c. Aucune réforme de fond ne concerne ce dossier.",
    "Les quatre caractéristiques des alambics sont maintenues. La mention des autorisations obtenues dans d'autres départements reste conditionnelle ; aucune pièce ni autorisation nouvelle n'est exigée.")

put('51 quater', [
    "Le directeur régional des douanes et droits indirects instruit les demandes qui lui sont soumises.",
    "S'il estime insuffisantes les garanties offertes par le requérant, il rejette la demande.",
    "S'il estime ces garanties suffisantes, il propose au préfet d'accorder l'autorisation demandée.",
], "À droit constant : présenter séparément l'examen de la demande et les deux suites possibles selon l'appréciation des garanties par le directeur régional. Aucune réforme de fond n'est introduite.",
    "Les trois alinéas et le pouvoir d'appréciation du directeur sont conservés. Des garanties jugées suffisantes conduisent à une proposition au préfet, et non à une autorisation automatique ; voir l'article 51 quinquies.")

put('51 quinquies', [
    "Le préfet examine les propositions du directeur régional des douanes et droits indirects, puis accorde l'autorisation par arrêté ou prend une décision de rejet.",
], "À droit constant : donner au préfet un rôle explicite dans la phrase et préciser les deux décisions possibles après examen des propositions. Aucune réforme de fond ne modifie cette compétence.",
    "L'arrêté reste la forme de l'octroi de l'autorisation. Le texte n'impose pas cette forme à la décision de rejet. La répartition des compétences des articles 51 quater et 51 quinquies est maintenue.")

put('51 sexies', [
    "Si le titulaire d'une autorisation commet une infraction aux articles 303 à 520 du code général des impôts ou aux textes pris pour leur application, le préfet peut retirer cette autorisation par arrêté, sur proposition du directeur régional des douanes et droits indirects. La période de retrait ne peut dépasser la campagne au cours de laquelle l'infraction a été commise et les deux campagnes suivantes.",
    "Le préfet est tenu de prononcer le retrait lorsque l'infraction relevée est passible de l'une des sanctions prévues aux articles 1746, 1810 et 1815 du code général des impôts. Il en est également tenu lorsqu'il est établi que le titulaire de l'autorisation a facilité la fraude commise par ses clients ou leur a sciemment procuré les moyens de la commettre.",
    "Dans le cas visé au deuxième alinéa où l'infraction est punie des sanctions prévues à l'article 1810 du code général des impôts, la durée du retrait est d'au moins trois campagnes, y compris celle au cours de laquelle l'infraction a été commise, et de six campagnes au plus. Toutefois, le retrait de l'autorisation d'exercer la profession de loueur d'alambic ambulant est définitif en cas d'infractions punies des sanctions prévues aux articles 1746 et 1815 du même code. Il est également définitif lorsqu'une nouvelle infraction passible des sanctions prévues à l'article 1810 de ce code est relevée à la charge du contrevenant, avant ou après la date de l'arrêté préfectoral prononçant le retrait.",
], "À droit constant : distinguer le retrait facultatif, les cas de retrait obligatoire et les durées particulières ou définitives. Le dernier alinéa est découpé en phrases tout en restant à sa place. Aucune réforme de fond des sanctions n'est prévue par policy.json.",
    "Les trois alinéas et le renvoi au deuxième alinéa sont maintenus. Le plafond ordinaire est la campagne de l'infraction et les deux suivantes ; le cas de l'article 1810 prévoit trois à six campagnes, campagne de l'infraction incluse. Le caractère définitif reste limité aux hypothèses énoncées pour les loueurs d'alambic ambulant. Les articles 1810 et 1815 sont absents du corpus CGI fourni : leur portée actuelle ne peut y être vérifiée. L'article 1746 y figure avec une abrogation différée au 1er janvier 2029. Ces renvois anciens et la plage 303 à 520 sont conservés, sans substitution inventée ; une coordination des bases de sanction demeure à établir séparément.")

put('51 septies', [
    "L'exploitant attribue un numéro distinctif à chaque appareil, cuve, bac, foudre ou réservoir fixe destiné à contenir des matières et des alcools. Sur chacun de ces récipients, il peint ce numéro et l'indication de la contenance en caractères d'au moins cinq centimètres de haut. Il reporte ces indications sur les plans remis à l'administration à l'appui de la déclaration générale d'exploitation prévue à l'article 58 de l'annexe I au code général des impôts.",
    "Les tuyaux où circule l'alcool doivent être parfaitement identifiables et rester visibles sur l'ensemble de leur parcours.",
], "À droit constant : attribuer explicitement à l'exploitant la numérotation, le marquage et leur report sur les plans, puis isoler l'exigence de visibilité des tuyaux. Aucune réforme de fond n'est introduite.",
    "Le minimum de cinq centimètres concerne la hauteur des caractères du numéro et de la contenance. Le renvoi à l'article 58 de l'annexe I a été vérifié dans le corpus : il porte sur la déclaration et les plans. Les deux alinéas sont conservés.")

put('51 septies A', [
    "L'exploitant maintient en bon état d'usage les marques, jauges et tubes de niveau réglementaires.",
    "L'accès aux points des installations où les agents du service des douanes et droits indirects doivent normalement intervenir pour leurs opérations de contrôle et de reconnaissance doit respecter les conditions de sécurité et d'éclairage prévues par la réglementation en vigueur.",
], "À droit constant : formuler directement l'obligation d'entretien de l'exploitant et préciser les exigences applicables à l'accès des agents. Aucune réforme de fond n'est applicable.",
    "Les deux alinéas, les trois catégories d'équipements et les opérations tant de contrôle que de reconnaissance sont maintenus. Aucun standard technique nouveau de sécurité ou d'éclairage n'est ajouté.")

put('51 septies B', [
    "Dans la distillerie, l'exploitant réserve aux agents du service des douanes et droits indirects un emplacement convenable qui doit être agréé par l'administration.",
], "À droit constant : placer l'obligation à la charge de l'exploitant dans une phrase directe et distinguer le caractère convenable de l'emplacement de son agrément. Aucune réforme de fond n'est introduite.",
    "L'emplacement demeure situé dans la distillerie et soumis à l'agrément de l'administration. La formulation n'ajoute aucune exigence de local séparé ou de surface minimale.")

put('51 septies D', [
    "L'exploitant maintient propre l'intérieur des bacs ou récipients de stockage. Les agents du service des douanes et droits indirects peuvent exiger l'enlèvement des dépôts qui se trouvent au fond de ces bacs ou récipients et sont susceptibles de fausser l'échelle des contenances, sans entraver l'activité de la distillerie.",
], "À droit constant : identifier l'exploitant comme responsable de la propreté et préciser les dépôts dont les agents peuvent demander l'enlèvement. Aucune réforme de fond n'est introduite.",
    "L'alinéa unique est conservé. Le pouvoir des agents reste limité aux dépôts susceptibles de fausser l'échelle des contenances et doit s'exercer sans entraver l'activité. Le présent article vise le stockage ; le coulage figure dans le régime spécial de l'article 51 octies A.")

put('51 septies E', [
    "L'exploitant déclare immédiatement aux agents habilités par l'administration des douanes et droits indirects tout incident ou toute anomalie de fonctionnement d'un compteur qu'il constate. Il consigne sur le registre prévu à cet effet :",
    "La nature de l'incident ou de l'anomalie ;",
    "La date et l'heure auxquelles il l'a constaté ;",
    "Les index du compteur au moment de cette constatation ;",
    "Le moyen par lequel il a avisé les agents habilités par l'administration des douanes et droits indirects.",
    "Si l'incident perturbe l'écoulement normal de l'alcool, l'exploitant utilise le circuit de secours et les bacs de réserve.",
    "Les agents habilités par l'administration des douanes et droits indirects remettent l'installation en ordre dans les meilleurs délais. Ils inscrivent leur intervention sur le registre mentionné au premier alinéa.",
], "À droit constant : distinguer la déclaration immédiate, les quatre renseignements à enregistrer, le recours au circuit de secours et l'intervention des agents. Aucune réforme de fond n'est introduite.",
    "Les sept alinéas sont conservés, notamment le premier auquel renvoie le dernier. Les index sont ceux du moment de la constatation. Le recours au circuit de secours et aux bacs de réserve reste conditionné à l'effet de l'incident sur l'écoulement normal de l'alcool ; aucun délai chiffré de remise en ordre n'est créé.")

put('51 septies F', [
    "Les agents habilités par l'administration des douanes et droits indirects effectuent périodiquement les relevés des compteurs. La fréquence de ces relevés est fixée selon le modèle de l'appareil installé et les circonstances particulières à la distillerie. L'exploitant doit assister aux relevés ou s'y faire représenter.",
    "Ces agents inscrivent les résultats des relevés sur un registre spécial déposé à la distillerie.",
], "À droit constant : identifier les agents chargés des relevés et séparer la fréquence, la présence de l'exploitant et l'enregistrement des résultats. Aucune réforme de fond n'est introduite.",
    "Les deux critères de fréquence sont maintenus, sans désigner une autorité de fixation que la source ne nomme pas. L'exploitant conserve la possibilité d'être représenté ; le registre spécial reste déposé à la distillerie.")

put('51 septies H', [
    "Les huiles essentielles ou de fusel font l'objet d'un suivi dans un compte d'ordre.",
    "Lorsqu'elles sont expédiées à destination d'une distillerie, ces huiles doivent circuler sous le couvert d'un titre de mouvement indiquant leur volume et l'alcool qu'elles renferment, correspondant au degré apparent.",
], "À droit constant : préciser le suivi comptable des huiles et formuler directement l'obligation documentaire applicable à leur expédition vers une distillerie. Aucune réforme de fond n'est introduite.",
    "Le compte demeure un compte d'ordre. Le titre de mouvement reste exigé pour la destination expressément visée, avec le volume et l'alcool correspondant au degré apparent ; aucune formule de conversion ni autre destination n'est ajoutée.")

put('51 septies I', [
    "Le bilan de fabrication prévu à l'article 73 de l'annexe I au code général des impôts comporte les inscriptions suivantes :",
    "En charges, les quantités d'alcool :",
    "Présentes dans les appareils à rectifier ou à déshydrater et dans leurs circuits de fabrication lors de la reprise des comptes de la campagne ;",
    "Produites sur place ;",
    "Présentes en magasin lors de la reprise des comptes de la campagne ;",
    "Introduites dans la distillerie pendant la campagne sous le couvert de titres de mouvement et inscrites aux charges du compte de magasin ;",
    "Constatées en excédent lors des inventaires de magasin effectués en cours de campagne.",
    "En décharges, les quantités d'alcool :",
    "Expédiées de la distillerie pendant la campagne sous le couvert de titres de mouvement et inscrites aux décharges du compte de magasin ;",
    "Ayant fait l'objet d'une perte accidentelle ou d'une destruction régulièrement constatée ;",
    "Dénaturées en présence du service.",
    "En restes, les quantités d'alcool :",
    "Constatées en magasin lors de l'inventaire général de clôture de la campagne ;",
    "Présentes dans les appareils à rectifier ou à déshydrater et dans leurs circuits de fabrication lors de l'inventaire général de clôture de la campagne.",
], "À droit constant : rendre plus explicite la fonction du bilan et harmoniser la rédaction des inscriptions sans modifier la répartition entre charges, décharges et restes. Aucune réforme de fond n'est introduite.",
    "Les quatorze alinéas et l'ordre des cinq charges, trois décharges et deux restes sont conservés. L'inscription au compte de magasin reste requise pour les entrées et sorties concernées. L'article 73 de l'annexe I, vérifié dans le corpus, prévoit le bilan de fin de campagne et le calcul du manquant ; sa formule n'est pas modifiée ici.")

put('51 septies J', [
    "Le registre mis à la disposition de l'exploitant pour enregistrer les déclarations prévues à l'article 75 de l'annexe I au code général des impôts mentionne les renseignements suivants au fur et à mesure du déroulement des mises en distillation de matières à traiter suivies en compte, des repassages de produits imparfaits, des rectifications de flegmes ou de produits défectueux et des déshydratations d'alcool achevé :",
    "La nature de l'opération ;",
    "La nature des matières à traiter ;",
    "Le récipient dont ces matières sont extraites ;",
    "La date et l'heure de début de l'opération ;",
    "La date et l'heure de fin de l'opération ;",
    "Le volume des matières et, pour les produits à repasser, à rectifier ou à déshydrater, leur titre alcoolique et la quantité d'alcool pur qu'ils renferment.",
    "Lorsque l'opération est continue, les deux dernières indications peuvent n'être inscrites qu'en fin de journée. L'heure de cette inscription est convenue entre l'exploitant et les agents du service des douanes et droits indirects ou, à défaut d'accord, fixée par ces agents.",
], "À droit constant : ponctuer l'énumération des opérations, préciser les données à enregistrer et séparer l'exception de fin de journée de la fixation de son heure. Aucune réforme de fond n'est introduite.",
    "Les huit alinéas et les six renseignements restent dans le même ordre : les deux dernières indications sont donc toujours la fin de l'opération et les données de volume, titre et alcool pur. L'article 75 de l'annexe I, vérifié dans le corpus, vise aussi les mises en macération de fruits, que le présent article ne mentionne pas : cette différence préexistante de champ est signalée sans ajout silencieux. La source de 2025 et la formule « matières à traiter suivies en compte » sont conservées dans leur portée.")

put('51 octies', [
    "Les distilleries relevant du régime spécial prévu à l'article 57 de l'annexe I au code général des impôts sont soumises de plein droit aux articles 51 septies, 51 septies A et 51 septies B ainsi qu'aux dispositions particulières ci-après.",
], "À droit constant : formuler directement l'application de plein droit des règles communes aux distilleries du régime spécial, en maintenant les dispositions particulières. Aucune réforme de fond n'est introduite.",
    "L'article 57 de l'annexe I, vérifié dans le corpus, distingue les régimes général et spécial. Les trois articles rendus applicables sont limitativement maintenus ; les autres règles du régime général ne sont pas étendues par cette réécriture.")

put('51 octies A', [
    "L'exploitant assure la propreté de l'intérieur des bacs ou récipients de coulage et de stockage.",
    "Les agents du service des douanes et droits indirects peuvent exiger l'enlèvement des dépôts qui se trouvent au fond des bacs ou récipients et sont susceptibles de fausser l'échelle des contenances, sans entraver la marche de la distillerie.",
], "À droit constant : attribuer explicitement l'entretien à l'exploitant et préciser l'objet du pouvoir de contrôle des agents. Aucune réforme de fond n'est introduite.",
    "Les deux alinéas sont conservés. À la différence de l'article 51 septies D, le présent article du régime spécial vise à la fois le coulage et le stockage. Le pouvoir d'exiger le nettoyage reste subordonné au risque de fausser l'échelle et à l'absence d'entrave à la marche de la distillerie.")

put('51 octies B', [
    "Les registres mis à la disposition de l'exploitant pour enregistrer les déclarations prévues aux articles 82 et 85 de l'annexe I au code général des impôts mentionnent les renseignements suivants, au fur et à mesure du déroulement des opérations :",
    "a. Pour la fabrication ou la préparation de matières susceptibles de produire de l'alcool :",
    "La nature de l'opération ;",
    "La date et l'heure auxquelles l'opération commence et se termine ;",
    "L'espèce des matières mises en œuvre et leur poids ou leur volume ;",
    "Le numéro des bacs ou récipients qui recueillent les produits obtenus ;",
    "Le volume ou le poids de ces produits et, le cas échéant, la quantité d'alcool pur qu'ils renferment.",
    "b. Pour les mises en fermentation destinées à produire des boissons ou à obtenir des matières susceptibles d'être mises en distillation :",
    "La nature de l'opération ;",
    "La date et l'heure auxquelles l'opération commence ;",
    "Le numéro des bacs ou récipients où l'opération est effectuée ;",
    "L'espèce et la quantité des moûts, jus ou matières mis en œuvre ;",
    "La date et l'heure auxquelles l'opération se termine ;",
    "Le volume ou le poids des matières fermentées et, pour les boissons et dilutions alcooliques, la quantité d'alcool pur qu'elles renferment.",
    "c. Pour les mises en distillation :",
    "La nature de l'opération ;",
    "La date et l'heure auxquelles le chargement de l'appareil commence et se termine ;",
    "Le numéro de l'appareil ;",
    "La nature des matières mises en œuvre ;",
    "Le volume ou le poids de ces matières, leur titre alcoolique et la quantité d'alcool pur qu'elles renferment ;",
    "Le numéro des bacs ou récipients dont ces matières sont extraites ;",
    "Le volume, le degré et la quantité d'alcool pur des alcools achevés ou imparfaits soumis à repasse, seuls ou ajoutés à des matières fermentées et, dans ce dernier cas, la quantité totale d'alcool mise en distillation ;",
    "Le volume, le degré et la quantité d'alcool pur des produits effectivement obtenus, en distinguant les produits achevés des produits imparfaits ;",
    "Le numéro des bacs ou récipients qui recueillent ces produits.",
], "À droit constant : clarifier le contenu des registres par des phrases plus explicites tout en maintenant les subdivisions a, b et c et chaque renseignement à sa place. Aucune réforme de fond n'est introduite.",
    "Les vingt-quatre alinéas sont maintenus : cinq renseignements sous a, six sous b et neuf sous c. L'horaire du c concerne le chargement de l'appareil, non la durée globale de distillation. La quantité totale d'alcool n'est exigée dans l'alinéa de repasse que lorsque les alcools sont ajoutés aux matières fermentées. Les articles 82 et 85 de l'annexe I ont été vérifiés : ils concernent respectivement les inscriptions de fabrication/fermentation et l'information avant et après la distillation.")

put('52', [
    "Une richesse alcoolique inférieure à 50 % vol. est admise pour les produits de parfumerie et de toilette visés à l'article 349 du code général des impôts qui relèvent de l'une des dénominations génériques suivantes :",
    "Lotions au pétrole ;",
    "Lotions détersives ;",
    "Lotions toniques pour les soins du visage et du corps ;",
    "Teintures ;",
    "Fixateurs pour les cheveux ;",
    "Brillantines deux corps ;",
    "Shampooings ;",
    "Produits de beauté (crèmes, laits, etc., pour les soins de l'épiderme) ;",
    "Vernis ;",
    "Rouges liquides ;",
    "Dépilatoires ;",
    "Fards ;",
    "Eaux dentifrices ;",
    "Produits de permanente pour cheveux ;",
    "Produits pour l'entretien de la chevelure (l'hygiène et les soins de la chevelure).",
], "À droit constant : formuler la permission de présenter une richesse alcoolique inférieure au seuil et améliorer la ponctuation de la liste. Les quinze dénominations techniques sont conservées intégralement ; aucune réforme de fond n'est introduite.",
    "Le seuil reste strictement inférieur à 50 % vol., sans changement de mesure ni de champ. L'article 349 est absent du corpus CGI fourni : la base de ce renvoi ancien reste à vérifier et à coordonner séparément. La réécriture ne présume ni son remplacement ni l'abrogation de la liste.")

put('52 ter', [
    "À compter du 1er janvier 2026, le contingent annuel d'exportation de 153 000 hectolitres d'alcool pur fixé par l'article 362 du code général des impôts est réparti conformément au tableau ci-après. Cette répartition distingue le rhum traditionnel agricole du rhum traditionnel de sucrerie et attribue les contingents entre les départements d'outre-mer et entre les distilleries.",
], "À droit constant : séparer la date d'application et la règle de répartition de la présentation des deux catégories de rhum et de leurs bénéficiaires. Le tableau chiffré est reproduit intégralement, avec seulement une normalisation de son balisage ; ses dénominations et valeurs ne sont pas présentées comme réécrites. Aucune réforme de fond n'est introduite.",
    "L'article 362 du CGI, vérifié dans le corpus, fixe le contingent à 153 000 hectolitres d'alcool pur. Le tableau conserve ses trente lignes, ses quatre colonnes logiques, toutes ses cellules vides, les noms et les quatre décimales des montants. Les sous-totaux départementaux correspondent aux sommes des distilleries. Leur total atteint toutefois 152 999,9999 hectolitres d'alcool pur, soit 0,0001 de moins que le contingent annoncé : écart préexistant conservé et signalé, sans correction silencieuse. La note source vise l'article 3 de l'arrêté du 16 juin 2025 (NOR : ECOD2514688A) et confirme l'application au 1er janvier 2026 ; cette date historique n'est pas utilisée comme date d'une réforme future.")
# Préserver exactement les textes de toutes les cellules et les fusions du tableau.
a = next(a for a in sources if a['number'] == '52 ter')
table = ET.fromstring('<div>' + a['source_xml'] + '</div>').find('table')
for node in table.iter():
    for attr in list(node.attrib):
        if attr not in {'rowspan', 'colspan'}:
            del node.attrib[attr]
for cell in list(table.iter('td')) + list(table.iter('th')):
    content = ' '.join(''.join(cell.itertext()).split())
    for child in list(cell):
        cell.remove(child)
    cell.text = content
    cell.tail = '\n'
drafts['52 ter']['proposed_xml'] += '\n' + ET.tostring(table, encoding='unicode', short_empty_elements=False).strip()

put('52 quater', [
    "I. - Les personnes qui expédient des rhums traditionnels des départements d'outre-mer depuis la France métropolitaine vers l'étranger doivent obtenir un certificat pour bénéficier du régime de l'exportation préalable prévu à l'article 144 bis de l'annexe III au code général des impôts. Ce certificat est délivré par le bureau de la direction générale des douanes et droits indirects qui a constaté la sortie du territoire national. Il précise la quantité, la qualité et l'origine du ou des rhums concernés ainsi que le volume d'alcool pur correspondant.",
    "II. - Un certificat d'exportation préalable ne peut être délivré que pour une expédition accompagnée de titres de mouvement attestant qu'il s'agit de rhums traditionnels des départements d'outre-mer. Le cas échéant, il est émis autant de certificats que de qualités et d'origines de rhums mentionnées sur la déclaration mensuelle d'assemblage du mois correspondant aux expéditions.",
    "Chaque certificat d'exportation préalable est extrait d'un carnet à souches et n'est pas cessible. Il est valable six mois à compter du jour de sa délivrance. Dans ce délai, il doit être imputé en charge, selon les qualités qu'il indique, sur les contingents des opérateurs du département d'origine du rhum. À défaut d'imputation dans ce délai, le certificat devient caduc.",
], "À droit constant : rendre explicites la demande de certificat, le bureau compétent, les mentions requises et les conditions d'imputation, sans modifier les subdivisions I et II. Aucune réforme de fond n'est introduite.",
    "Les trois alinéas sont conservés. La durée de six mois court du jour de délivrance ; le certificat reste incessible et devient caduc faute d'imputation dans ce délai. L'article 144 bis de l'annexe III, vérifié dans le corpus, distingue notamment les anciens certificats sous le décret du 8 octobre 1948 (III) et l'abondement lié aux réexportations ou réexpéditions (II). L'articulation de ce régime ancien avec les certificats du présent article mérite une coordination expresse ; aucune extension aux certificats ou opérations d'un autre régime n'est opérée ici.")

put('54-0 A', [
    "Les règles de l'article 444 du code général des impôts relatives à l'apposition de capsules représentatives des droits indirects sur les récipients s'appliquent aux vins, aux cidres et aux spiritueux, dans les conditions fixées aux articles 54-0 B à 54-0 BX.",
    "L'apposition de ces capsules tient lieu du document prévu au II de l'article 302 M du même code.",
], "À droit constant : rendre directe la règle d'application aux trois catégories de boissons et préciser l'effet documentaire de l'apposition des capsules. Aucune réforme de fond n'est introduite.",
    "Les deux alinéas, les trois catégories de boissons et la plage 54-0 B à 54-0 BX sont maintenus. Les articles 54-0 B et 54-0 BX ont été vérifiés dans le corpus de l'annexe IV. En revanche, les articles 444 et 302 M sont absents du corpus CGI fourni : incohérence documentaire préexistante à coordonner avec les bases légales de circulation applicables, sans inventer de renvoi de remplacement ni supprimer silencieusement l'effet substitutif.")

assert len(sources) == len(drafts) == 24
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles ;', Path('answer.json').stat().st_size, 'octets')
