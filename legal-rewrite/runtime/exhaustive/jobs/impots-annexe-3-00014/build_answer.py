import json
from html import escape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answers = []


def add(index, paragraphs, reason, review):
    source = sources[index]
    text = '\n'.join('<p>' + escape(p.strip(), quote=False).replace('&lt;br /&gt;', '<br />') + '</p>'
                     for p in paragraphs.strip().split('\n') if p.strip())
    answers.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': text,
        'reason': reason,
        'review_notes': review,
        'status': 'rewrite_draft',
    })


add(0, '''
I. – Lorsque les souscripteurs de parts d'un fonds d'investissement de proximité mentionné à l'article L. 214-31 du code monétaire et financier entendent bénéficier de la réduction d'impôt prévue aux VII ou VIII de l'article 199 terdecies-0 A du code général des impôts, la société de gestion du fonds ou le dépositaire de ses actifs agissant pour le compte de cette société doit respecter les obligations définies aux I à III et aux V à VII de l'article 46 AI ter.
II. – À chaque inventaire semestriel, la société de gestion d'un fonds d'investissement de proximité ou le dépositaire de ses actifs agissant pour le compte de cette société vérifie que les sociétés dont les titres ou les avances en compte courant sont retenus pour calculer la proportion mentionnée au I de l'article L. 214-31 du code monétaire et financier remplissent les conditions de l'article L. 214-31. Ces conditions sont appréciées à la date de clôture de leur dernier exercice précédant l'inventaire.
La société de gestion du fonds ou le dépositaire de ses actifs transmet un état de chacun des inventaires semestriels de l'actif du fonds mentionnés à l'alinéa précédent à la direction départementale ou, le cas échéant, régionale des finances publiques dont il relève. Cet état accompagne le bilan et le compte de résultats.
III. – Le contribuable qui entend bénéficier de la réduction d'impôt prévue aux VII ou VIII de l'article 199 terdecies-0 A du code général des impôts au titre de la souscription en numéraire de parts de fonds d'investissement de proximité mentionnés à l'article L. 214-31 du code monétaire et financier est soumis aux dispositions de l'article 46 AI quater.
''',
    "Réécriture à droit constant : la condition d'accès à la réduction précède les obligations du gestionnaire ou du dépositaire ; la date d'appréciation des conditions et l'envoi des inventaires sont formulés dans des phrases distinctes. Aucune réforme de fond ne vise ce régime dans policy.json.",
    "Les I à III et V à VII de l'article 46 AI ter, l'article 46 AI quater, les VII ou VIII de l'article 199 terdecies-0 A et le I de l'article L. 214-31 sont conservés. Les inventaires restent semestriels et les conditions sont appréciées au dernier exercice clos avant chacun d'eux. Le renvoi d'adaptation aux règles des FCPI reste celui de la source ; aucune obligation nouvelle n'est ajoutée.")

add(1, '''
Lorsqu'un contribuable souscrit au capital d'une société dans les conditions prévues aux articles 199 terdecies-0 A bis et 199 terdecies-0 A ter du code général des impôts, l'état individuel prévu au 1 du I de l'article 46 AI bis indique si la société remplit les conditions mentionnées, respectivement, au 1° du I de l'article 199 terdecies-0 A bis ou au II de l'article 199 terdecies-0 A ter.
Pour l'application des articles 199 terdecies-0 A bis et 199 terdecies-0 A ter, la condition relative à la qualité de jeune entreprise innovante est remplie si la société possède cette qualité au titre du dernier exercice clos à la date de la souscription ou au titre de l'exercice au cours duquel la souscription intervient.
''',
    "Réécriture à droit constant : l'état est expressément chargé d'indiquer si la société remplit les conditions, puis les deux exercices alternatifs permettant de satisfaire à la qualification sont énoncés directement. Aucune réforme de fond n'est appliquée.",
    "Les renvois distincts au 1° du I de l'article 199 terdecies-0 A bis et au II de l'article 199 terdecies-0 A ter ainsi que l'alternative entre les deux exercices sont maintenus. Dans le corpus, l'article 199 terdecies-0 A ter comporte aussi un 3° du I relatif aux jeunes entreprises d'innovation à impact : la source réglementaire ne le vise pas expressément ; son articulation avec cette catégorie doit être contrôlée, sans extension ajoutée ici.")

add(2, '''
I. – Lorsqu'un contribuable souscrit des parts de fonds communs de placement dans l'innovation dans les conditions prévues à l'article 199 terdecies-0 A bis du code général des impôts, l'état individuel prévu au V de l'article 46 AI ter indique si la condition mentionnée au deuxième alinéa du 2° du I de l'article 199 terdecies-0 A bis est remplie.<br /><br />II. – Le contribuable qui entend bénéficier de la réduction d'impôt prévue à l'article 199 terdecies-0 A bis du code général des impôts au titre de la souscription en numéraire de parts de fonds communs de placement dans l'innovation est soumis aux dispositions de l'article 46 AI quater.
''',
    "Réécriture à droit constant : la portée de l'état individuel est maintenue et le II désigne directement le contribuable tenu de respecter l'article 46 AI quater. Aucune réforme de fond n'est appliquée aux FCPI.",
    "Les subdivisions I et II et leur séparation par des sauts de ligne sont conservées. Le renvoi au deuxième alinéa du 2° du I de l'article 199 terdecies-0 A bis nécessite un contrôle de concordance : dans le corpus, la disposition concernant les fonds apparaît au dernier alinéa du I, après le 2°. Ce renvoi de la source est conservé sans correction silencieuse.")

add(3, '''
Pour l'application du b du 2° de l'article 199 terdecies-0 AA du code général des impôts, la première vente commerciale est caractérisée par un seuil de chiffre d'affaires de l'entreprise de 250 000 € hors taxe sur la valeur ajoutée. Le chiffre d'affaires retenu est celui constaté à la clôture de l'exercice.<br /><br />La durée de dix ans prévue au même b du 2° commence à la date d'ouverture de l'exercice qui suit celui au titre duquel le chiffre d'affaires de l'entreprise dépasse pour la première fois 250 000 €.
''',
    "Réécriture à droit constant : le chiffre d'affaires à retenir et le point de départ des dix ans sont formulés directement, sans modifier le seuil ni le dépassement qui déclenche le délai. Aucune réforme de fond ne concerne cette définition.",
    "Seuil de 250 000 € hors TVA, constatation à la clôture et départ à l'ouverture de l'exercice suivant le premier dépassement strict conservés. Le renvoi au b du 2° de l'article 199 terdecies-0 AA concorde avec la règle des dix ans du corpus. Aucun taux de réduction d'impôt n'est ajouté.")

add(4, '''
I. – Lorsqu'un contribuable entend bénéficier de la réduction d'impôt prévue à l'article 199 terdecies-0 B du code général des impôts, la société dont il a acquis les titres lui remet un état individuel comportant les mentions suivantes :
a. L'objet de l'état : l'application de l'article 199 terdecies-0 B du code général des impôts ;
b. La raison sociale, l'objet social et le siège social de la société reprise ;
c. L'identité et l'adresse du contribuable ainsi que, le cas échéant, celles des personnes mentionnées au b du I de l'article 199 terdecies-0 B qui participent avec lui à la reprise de la société ;
d. Le nombre de titres acquis par les personnes mentionnées au c, leur date d'acquisition et les pourcentages de droits de vote et de droits dans les bénéfices sociaux de la société reprise que ces titres leur confèrent ;
e. La fonction de direction exercée par le contribuable dans la société et la date à laquelle il a commencé à l'exercer ou, à défaut, l'identité de la ou des personnes qui exercent une fonction de direction dans la société, ainsi que la nature de cette fonction et la date à laquelle elles ont commencé à l'exercer.
Cet état précise que la société remplit les conditions mentionnées aux d, e et f du I de l'article 199 terdecies-0 B du code général des impôts.
II. – Pour bénéficier de la réduction d'impôt sur le revenu prévue à l'article 199 terdecies-0 B, le contribuable joint à sa déclaration de revenus de l'année d'acquisition des titres de la société reprise l'état individuel prévu au I et remis par cette société.
Le contribuable indique également :
a. Le prix d'acquisition des titres de la société reprise ;
b. Le montant, la durée et la date de l'emprunt contracté pour acquérir ces titres, ainsi que le nom et l'adresse de l'organisme prêteur ;
c. Le montant des intérêts dus chaque année au titre de cet emprunt, tel qu'il est prévu dans le contrat initial.
III. – À la demande de l'administration fiscale, le contribuable produit tout document permettant de justifier :
a. Le montant des intérêts retenus chaque année pour calculer la réduction d'impôt sur le revenu prévue à l'article 199 terdecies-0 B ;
b. La durée de détention des titres dont l'acquisition ouvre droit à cette réduction d'impôt sur le revenu.
''',
    "Réécriture à droit constant : les mentions de l'état, les renseignements déclarés par l'acquéreur et les preuves à produire sur demande sont distingués par des formulations directes. L'alternative relative au dirigeant est clarifiée. Aucune réforme de fond n'est appliquée au régime de reprise par emprunt.",
    "I, II, III et toutes les lettres sont maintenus dans leur ordre. Le contrat initial demeure la référence des intérêts déclarés au II ; les justificatifs du III restent exigibles seulement sur demande. Les renvois au b et aux d, e et f du I de l'article 199 terdecies-0 B sont préservés, ainsi que le rattachement à l'année d'acquisition.")

add(5, '''
I. – 1. Lorsqu'un contribuable souscrit au capital d'une société qui remplit les conditions prévues au premier alinéa du a du 1 de l'article 199 terdecies-0 C du code général des impôts, cette société lui remet un état individuel comportant les mentions suivantes :
a) L'objet de l'état ;
b) La raison sociale, l'objet social, le siège social et le régime fiscal de la société ;
c) L'identité et l'adresse du souscripteur ;
d) Le nombre de titres souscrits, ainsi que le montant et la date de leur souscription ;
e) La date et le montant des versements effectués.
Sur cet état, la société atteste qu'elle remplit les conditions mentionnées au premier alinéa du a du 1 et au 5 de l'article 199 terdecies-0 C du code général des impôts.
2. Si la société bénéficiaire de la souscription possède le statut d'entreprise solidaire de presse d'information au sens de l'article 2-1 de la loi n° 86-897 du 1er août 1986 portant réforme du régime juridique de la presse, elle le précise sur l'état mentionné au 1 du présent I.
I bis. – 1. Lorsqu'un contribuable souscrit au capital d'une société mentionnée au premier alinéa du b du 1 de l'article 199 terdecies-0 C du code général des impôts, cette société lui remet un état individuel contenant les informations prévues au 1 du I du présent article.
Sur cet état, la société atteste qu'elle remplit les conditions mentionnées au premier alinéa du b du 1 de l'article 199 terdecies-0 C du même code.
Si son objet statutaire exclusif est de détenir des participations dans des entreprises mentionnées au second alinéa du a du 1 du même article, la société le précise sur cet état.
2. À la clôture de l'exercice au cours duquel le contribuable a souscrit à son capital, la société lui remet une attestation de réinvestissement pour chacun des versements qu'il a effectués. Pour chaque versement que la société a effectué, avant la clôture de cet exercice, au capital de sociétés de presse mentionnées au a du 1 de l'article 199 terdecies-0 C du code général des impôts et qui se rapporte à la souscription correspondant au versement du contribuable, cette attestation comporte les informations suivantes :
a) La raison sociale, l'objet social et le siège social de la ou des sociétés de presse éligibles bénéficiaires de la souscription ;
b) Le nombre de titres souscrits, ainsi que le montant et la date de leur souscription ;
c) La date et le montant des versements effectués par la société au titre de la souscription au capital de la ou des sociétés mentionnées au a du présent 2.
Chaque société de presse au capital de laquelle la société a souscrit délivre un document attestant qu'elle remplit les conditions mentionnées au premier alinéa du a du 1 et au 5 de l'article 199 terdecies-0 C du même code. Ces documents accompagnent l'attestation de réinvestissement.
3. Sur l'attestation mentionnée au 2, la société mentionnée au premier alinéa du b du 1 de l'article 199 terdecies-0 C du code général des impôts s'engage à informer le contribuable si les titres souscrits au capital de sociétés de presse éligibles mentionnées au a du 1 du même article sont cédés avant le 31 décembre de la cinquième année suivant celle de leur souscription.
Si tout ou partie des titres souscrits par la société mentionnée au premier alinéa du b du 1 de l'article 199 terdecies-0 C du même code sont cédés avant le 31 décembre de la cinquième année suivant celle de leur souscription, cette société adresse au contribuable un état individuel. Cet état indique la raison sociale, l'objet social et le siège social de la ou des sociétés de presse dont les titres sont cédés, le nombre de titres cédés, ainsi que le montant et la date de la cession.
II. – À la demande de l'administration fiscale, le contribuable produit l'état mentionné au I et, le cas échéant, les états et l'attestation mentionnés au I bis. Il produit également tout document permettant de justifier la durée de détention des titres dont la souscription, directement ou par l'intermédiaire d'une société mentionnée au b du 1 de l'article 199 terdecies-0 C du code général des impôts, a ouvert droit à la réduction d'impôt sur le revenu prévue à cet article.
''',
    "Réécriture à droit constant : les obligations des sociétés de presse et des sociétés intermédiaires sont exprimées avec des sujets explicites. La longue phrase relative au réinvestissement est scindée en conservant le lien entre chaque versement du contribuable et les investissements correspondants. Aucune réforme de fond n'est appliquée.",
    "Les subdivisions I, I bis et II, leurs numéros et leurs lettres sont maintenus. La clôture de l'exercice, les attestations par versement, l'objet statutaire exclusif et les deux occurrences du terme du 31 décembre de la cinquième année sont préservés. Les premiers et seconds alinéas du a du 1 de l'article 199 terdecies-0 C restent distingués. La loi du 1er août 1986 est un renvoi historique, sans date nouvelle de réforme.")

add(6, '''
La personne morale ou l'entrepreneur individuel qui fournit des prestations de services ouvrant droit à l'aide prévue à l'article 199 sexdecies du code général des impôts remet à chacun de ses clients l'attestation fiscale prévue au premier alinéa de l'article D. 7233-4 du code du travail. Cette attestation contient les informations énumérées à ce même article D. 7233-4.
''',
    "Réécriture à droit constant : le prestataire est placé en tête de phrase et l'obligation de remise est séparée du contenu de l'attestation. Aucune réforme de fond ne modifie ce justificatif.",
    "Les bénéficiaires, les clients destinataires et les deux renvois sont préservés. L'article D. 7233-4 du corpus détaille une attestation annuelle ; le présent article continue d'y renvoyer sans recopier ni déplacer cette liste. Les mesures générales de réemploi des données ne suffisent pas, à elles seules, à supprimer ce justificatif.")

add(7, '''
L'organisme ayant son siège dans un État membre de l'Union européenne ou dans un État partie à l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative destinée à lutter contre la fraude et l'évasion fiscales présente la demande d'agrément mentionnée au 4 bis de l'article 200 du code général des impôts aux services centraux de la direction générale des finances publiques. Il rédige cette demande en français, sur papier libre, selon le modèle fixé par arrêté des ministres chargés de l'économie et du budget.
L'organisme joint à sa demande les pièces justificatives dont la liste est fixée par arrêté des mêmes ministres, ainsi que leur traduction en français. Ces pièces attestent qu'il poursuit des objectifs et présente des caractéristiques similaires à ceux des organismes ayant leur siège en France et remplissant les conditions prévues à l'article 200 du code général des impôts.
Les demandes de renouvellement de l'agrément sont présentées selon ces mêmes modalités.
''',
    "Réécriture à droit constant : l'organisme demandeur et le service destinataire sont identifiés avant les exigences de forme. Les pièces et leur fonction probatoire sont exposées en deux phrases. Aucune réforme de fond n'est appliquée à l'agrément des organismes étrangers.",
    "Le champ UE/EEE, la convention d'assistance requise, le papier libre, le modèle réglementaire, les traductions et les mêmes modalités de renouvellement sont conservés. Le deuxième alinéa demeure celui des pièces, visé par l'article 46 AW quater. La note relative à l'article 59-VIII I de la loi du 28 décembre 2011 est historique et n'est pas transformée en disposition future.")

add(8, '''
I. – Le ministre chargé du budget statue sur la demande d'agrément. Il notifie sa décision à l'organisme et la motive en cas de refus.
II. – Lors d'une première demande, l'agrément couvre la période allant de la date de sa notification au 31 décembre de la troisième année qui suit cette date.
L'organisme présente sa demande de renouvellement au plus tard le 30 juin de la dernière année couverte par l'agrément. Si le renouvellement est accordé, le nouvel agrément couvre une période de trois ans à compter du 1er janvier suivant. Si le renouvellement est refusé, l'agrément en cours continue de produire ses effets jusqu'à son terme.
III. – L'administration fiscale publie sur son site internet la liste des organismes agréés. Elle actualise cette liste à chaque décision d'agrément.
IV. – Le ministre chargé du budget peut retirer l'agrément par une décision motivée s'il est établi que l'organisme, en totalité ou en partie, ne poursuit plus d'objectifs ou ne présente plus de caractéristiques similaires à ceux des organismes ayant leur siège en France et remplissant les conditions prévues à l'article 200 du code général des impôts. La décision est notifiée à l'organisme et la liste mentionnée au III est actualisée.
''',
    "Réécriture à droit constant : les décisions du ministre, la demande de renouvellement et la publication par l'administration sont attribuées explicitement à leurs auteurs. Les conséquences d'un accord ou d'un refus sont exprimées dans des phrases distinctes. Aucune réforme de fond n'est appliquée.",
    "I à IV et les cinq alinéas sont conservés. Le premier agrément expire au 31 décembre de la troisième année suivant la notification, tandis que le renouvellement dure trois ans à compter du 1er janvier suivant. Le 30 juin, le maintien jusqu'au terme en cas de refus et les motifs alternatifs de retrait, total ou partiel, ne sont pas modifiés.")

add(9, '''
I. – Le contribuable indique séparément le montant des dons aux organismes mentionnés au 4 bis de l'article 200 du code général des impôts sur la déclaration de revenus prévue à l'article 170 du même code, au titre de l'année au cours de laquelle les dons sont effectués.
II. – Pour l'application du deuxième alinéa du 4 bis de l'article 200 du code général des impôts, le contribuable fournit les pièces mentionnées au deuxième alinéa de l'article 46 AW bis.
''',
    "Réécriture à droit constant : le contribuable est expressément désigné comme auteur de la déclaration et de la fourniture des pièces. L'année concernée est formulée directement. Aucune réforme de fond n'est appliquée.",
    "Le montant des dons reste déclaré distinctement et les pièces demeurent celles du deuxième alinéa de l'article 46 AW bis. La note historique indiquant que les mots « dans le délai de dépôt de la déclaration » deviennent sans objet n'est pas réintroduite comme délai applicable.")

add(10, '''
Pour l'application de l'article 200 undecies du code général des impôts, l'activité est réputée nécessiter la présence du contribuable sur l'exploitation chaque jour de l'année lorsque l'exploitant exerce une activité d'élevage exigeant quotidiennement des travaux, des soins ou une surveillance.
''',
    "Réécriture à droit constant : la présomption de présence quotidienne est rattachée directement à l'activité d'élevage et ses trois justifications alternatives sont explicites. Aucune réforme de fond ne modifie le crédit d'impôt agricole.",
    "La présomption, la présence chaque jour de l'année et les alternatives travaux, soins ou surveillance sont conservées. Les autres conditions du crédit d'impôt de l'article 200 undecies ne sont ni supprimées ni élargies par cette définition.")

add(11, '''
Une activité agricole autre que celle définie à l'article 46 AZA peut ouvrir droit au crédit d'impôt si l'exploitant joint à la déclaration spéciale mentionnée à l'article 46 AZA quater un calendrier des travaux de ses différentes productions démontrant que celles-ci exigent sa présence tous les jours de l'année.
''',
    "Réécriture à droit constant : la possibilité d'éligibilité et sa preuve par le calendrier sont réunies dans une formulation directe. Aucune réforme de fond n'est appliquée aux activités autres que l'élevage.",
    "Le caractère conditionnel de l'éligibilité, le calendrier couvrant les différentes productions, sa remise avec la déclaration spéciale et l'exigence de présence tous les jours de l'année sont préservés. Les articles 46 AZA et 46 AZA quater gardent leur rôle respectif.")

add(12, '''
Les dépenses de remplacement mentionnées au I de l'article 200 undecies du code général des impôts comprennent les rémunérations, leurs accessoires et les charges sociales. Seules les charges correspondant à des cotisations sociales obligatoires sont prises en compte.
Pour apprécier le plafond du crédit d'impôt prévu au II de l'article 200 undecies, le taux horaire minimum garanti retenu est celui qui est en vigueur au 31 décembre de l'année au titre de laquelle le crédit d'impôt est calculé, en application des articles L. 3231-4 à L. 3231-12 du code du travail.
''',
    "Réécriture à droit constant : la limitation aux cotisations obligatoires fait l'objet d'une phrase propre, dans le même alinéa. La date de référence du minimum garanti est isolée clairement du renvoi au code du travail. Aucune réforme de fond n'est appliquée.",
    "Les rémunérations et leurs accessoires restent inclus, seules les charges sociales obligatoires sont retenues, et la date reste le 31 décembre de l'année du calcul. Le renvoi aux articles L. 3231-4 à L. 3231-12 est maintenu ; le dernier définit bien le minimum garanti dans le corpus. La note de coordination avec l'ordonnance du 12 mars 2007 ne constitue pas une réforme future.")

add(13, '''
Pour l'application de l'article 200 undecies du code général des impôts, les contribuables qui exercent une activité dont les revenus sont imposés dans la catégorie des bénéfices agricoles doivent souscrire une déclaration spéciale conforme au modèle établi par l'administration.
Le contribuable qui exerce une activité professionnelle agricole joint cette déclaration à la déclaration annuelle de résultat qu'il doit déposer en application de l'article 53 A du code général des impôts.
Les exploitants individuels et les associés personnes physiques de sociétés de personnes ou de groupements assimilés, y compris les groupements agricoles d'exploitation en commun, qui ne sont pas tenus de déposer la déclaration annuelle de résultat prévue à l'article 53 A joignent la déclaration spéciale mentionnée au premier alinéa à leur déclaration de revenus de l'année au titre de laquelle ils demandent le crédit d'impôt.
Pour les associés personnes physiques de sociétés de personnes ou de groupements assimilés, y compris les groupements agricoles d'exploitation en commun, la déclaration spéciale précise la quote-part du crédit d'impôt qui revient à chaque associé selon sa participation dans le groupement concerné.
''',
    "Réécriture à droit constant : les deux circuits déclaratifs sont attribués directement au contribuable selon qu'il dépose ou non une déclaration de résultat. La règle propre aux associés est maintenue dans le dernier alinéa. Aucune réforme de fond ne supprime la déclaration spéciale.",
    "Les quatre alinéas sont conservés, notamment le premier auquel renvoie le troisième. L'article 53 A, l'année de demande du crédit, les GAEC et la répartition selon la participation de chaque associé demeurent inchangés quant à leur portée. Seule l'erreur grammaticale « est tenue » de la source est corrigée.")

add(14, '''
Le contribuable joint également à la déclaration spéciale mentionnée à l'article 46 AZA quater une copie de la facture de la prestation de service de remplacement ou une copie du contrat de travail indiquant le coût du salaire horaire du remplaçant et le nombre de jours de remplacement de l'exploitant.
''',
    "Réécriture à droit constant : l'obligation complémentaire est formulée au singulier avec un sujet explicite et les mentions du contrat sont exprimées directement. Aucune réforme de fond n'est appliquée aux justificatifs de remplacement.",
    "L'alternative entre copie de la facture et copie du contrat est maintenue, de même que les deux mentions relatives au salaire horaire et au nombre de jours dans le contrat. La pièce reste jointe à la déclaration spéciale de l'article 46 AZA quater, sans changement de calendrier.")

add(15, '''
Le contribuable qui demande le bénéfice de l'article 200 quaterdecies du code général des impôts au titre des intérêts du ou des prêts immobiliers supportés pour l'acquisition d'un logement mentionné au I de cet article présente les documents suivants à la demande de l'administration fiscale :
1. Si le contribuable ou un membre de son foyer fiscal désigné aux 1 et 3 de l'article 6 du code général des impôts acquiert directement le logement :
1° Une copie de l'acte authentique d'acquisition du logement ;
2° Une déclaration signée indiquant que le logement est affecté à l'habitation principale de l'emprunteur et précisant la date à laquelle cette affectation prend effet, ou, en cas de construction ou d'acquisition en l'état futur d'achèvement, l'engagement d'affecter le logement à cet usage dès son achèvement et au plus tard le 31 décembre de la deuxième année suivant celle de la conclusion du prêt ;
3° L'échéancier de remboursement établi par l'établissement financier prêteur, faisant notamment apparaître les intérêts dus. Si le prêt est souscrit à taux variable, un document établi par cet établissement récapitulant les intérêts effectivement versés par l'emprunteur au cours de l'année ;
4° Le cas échéant, les factures de travaux établies par les entreprises, à l'exclusion des factures d'acompte ;
5° Le cas échéant, lorsque le contribuable fait construire son logement, l'acte authentique d'acquisition du terrain nu, les mémoires des entrepreneurs et architectes chargés des travaux de construction, la déclaration d'ouverture de chantier prévue à l'article R. * 424-16 du code de l'urbanisme accompagnée d'une pièce attestant sa réception en mairie, ainsi qu'une copie des factures des travaux de construction du logement comportant les mentions prévues à l'article 242 nonies A de l'annexe II.
2. Si une société non soumise à l'impôt sur les sociétés acquiert le logement et le met gratuitement à la disposition d'un associé pour son habitation principale, le contribuable présente, outre les documents mentionnés au 1, une attestation sur l'honneur signée conjointement par lui et par la société propriétaire. Cette attestation comporte les déclarations suivantes :
1° La société atteste qu'elle met gratuitement le logement à la disposition de l'associé personne physique. Elle précise ses nom et prénoms et la quote-part correspondant au logement concerné représentative de ses droits dans le capital social ;
2° L'associé atteste qu'il affecte le logement à son habitation principale.
L'attestation précise également l'adresse du logement acquis, la référence du ou des prêts immobiliers souscrits pour le financer, les coordonnées du ou des organismes prêteurs, la date de signature de l'acte authentique d'acquisition et la date à laquelle le logement est affecté à l'habitation principale de l'associé personne physique qui bénéficie de sa mise à disposition gratuite.
Si la société fait construire le logement ou l'acquiert en l'état futur d'achèvement, l'attestation précise que la mise à disposition et l'affectation à l'habitation principale doivent intervenir dès l'achèvement et au plus tard le 31 décembre de la deuxième année suivant celle de la conclusion du prêt.
''',
    "Réécriture à droit constant : les cas d'acquisition directe et par une société sont formulés avec leurs acteurs, et les engagements à terme sont séparés des affectations déjà effectives. La liste complète des documents et des mentions est rédigée en phrases plus lisibles. Aucune réforme de fond n'est étendue à ces prêts anciens.",
    "Les 1 et 2 et leurs 1° à 5° ou 1° à 2° sont maintenus, ainsi que les douze alinéas. Le délai du 31 décembre de la deuxième année suivant la conclusion du prêt figure dans les deux cas, sans prolongation. Les prêts à taux variable, l'exclusion des acomptes, la réception en mairie, les mentions de l'annexe II et la gratuité restent préservés ; aucun droit nouveau à crédit d'impôt n'est ouvert au-delà du champ de l'article 200 quaterdecies.")

add(16, '''
Pour être considérés comme des logements mentionnés au troisième alinéa du III de l'article 200 quaterdecies du code général des impôts, les logements doivent remplir les conditions d'attribution du label « bâtiment basse consommation énergétique, BBC 2005 » mentionné au 5° de l'article 2 de l'arrêté du 3 mai 2007 relatif au contenu et aux conditions d'attribution du label « haute performance énergétique ».
''',
    "Réécriture à droit constant : la définition devient une condition explicite que le logement doit remplir pour entrer dans le champ fiscal visé. Elle reste fondée sur les conditions d'attribution du label, sans exiger une preuve nouvelle. Aucune réforme de fond n'est appliquée.",
    "Le troisième alinéa du III de l'article 200 quaterdecies, le 5° de l'article 2, la date du 3 mai 2007 et la dénomination BBC 2005 sont conservés. La source exige de répondre aux conditions d'attribution, et non expressément de détenir le label : cette distinction avec d'autres articles du lot est maintenue.")

add(17, '''
I. – Pour entrer dans la catégorie des logements mentionnés au troisième alinéa du II de l'article 199 septvicies du code général des impôts, les logements doivent satisfaire aux conditions suivantes :
1° Les logements acquis neufs ou, sous réserve du 2°, acquis en l'état futur d'achèvement ou que le contribuable fait construire doivent bénéficier du label « bâtiment basse consommation énergétique, BBC 2005 » mentionné au 5° de l'article 2 de l'arrêté du 3 mai 2007 relatif au contenu et aux conditions d'attribution du label « haute performance énergétique » ;
2° Les logements qui font ou ont fait l'objet des travaux mentionnés aux b, c et d du 2 du I de l'article 199 septvicies, ainsi que les logements acquis en l'état futur d'achèvement mentionnés au 1 du I du même article lorsqu'ils ne sont pas soumis aux dispositions de l'article L. 171-1 du code de la construction et de l'habitation, doivent remplir l'une des conditions suivantes :
a) Soit bénéficier du label « haute performance énergétique rénovation, HPE rénovation 2009 » ou du label « bâtiment basse consommation énergétique rénovation, BBC rénovation 2009 » mentionnés aux 1° et 2° de l'article 2 de l'arrêté du 29 septembre 2009 relatif au contenu et aux conditions d'attribution du label « haute performance énergétique rénovation » ;
b) Soit respecter les exigences de performance énergétique globale fixées par arrêté du ministre chargé de la construction pour au moins deux des quatre catégories suivantes :
– isolation de la toiture ou des murs donnant sur l'extérieur ;
– fenêtres ;
– système de chauffage ;
– système de production d'eau chaude sanitaire.
II. – Les logements mentionnés au cinquième alinéa du IV de l'article 199 septvicies du code général des impôts doivent bénéficier du label « bâtiment basse consommation énergétique, BBC 2005 » mentionné au 5° de l'article 2 de l'arrêté du 3 mai 2007 relatif au contenu et aux conditions d'attribution du label « haute performance énergétique ».
''',
    "Réécriture à droit constant : les critères définissant les logements sont présentés comme des conditions explicites, avec l'alternative entre labels et performances pour les travaux. Les quatre catégories restent intégrales. Aucune réforme de fond, notamment de rénovation locative, n'est appliquée à ce régime fiscal.",
    "Les I et II, 1° et 2°, a et b, les quatre catégories et leurs alinéas sont conservés. Le minimum de deux catégories sur quatre n'est pas transformé en exigence cumulative ; toiture ou murs demeure une seule catégorie. Les renvois au troisième alinéa du II et au cinquième alinéa du IV de l'article 199 septvicies et à l'article L. 171-1 restent ceux de la source. La note concernant la loi du 28 décembre 2011 reste historique.")

add(18, '''
Pour entrer dans la catégorie des logements mentionnés au II de l'article 199 novovicies du code général des impôts, les logements doivent satisfaire aux conditions suivantes :
1° Les logements acquis neufs ou, sous réserve du 2°, acquis en l'état futur d'achèvement ou que le contribuable fait construire doivent remplir l'une des conditions suivantes :
a) Soit bénéficier du label mentionné au 1° du I de l'article 46 AZA octies ;
b) Soit respecter les caractéristiques thermiques et les conditions mentionnées à l'article R. 172-2 du code de la construction et de l'habitation, selon les prescriptions de l'arrêté prévu à l'article R. 172-3 du même code.
À la demande de l'administration fiscale, le contribuable justifie du respect de la condition de l'alinéa précédent en présentant l'attestation mentionnée à l'article 6 de l'arrêté du 11 octobre 2011 relatif aux attestations de prise en compte de la réglementation thermique et de réalisation d'une étude de faisabilité relative aux approvisionnements en énergie pour les bâtiments neufs ou les parties nouvelles de bâtiments ;
2° Les logements qui font ou ont fait l'objet des travaux mentionnés aux 2°, 3° et 4° du B du I de l'article 199 novovicies du code général des impôts, ainsi que les logements acquis en l'état futur d'achèvement mentionnés au premier alinéa du I du même article lorsqu'ils ne sont pas soumis aux dispositions de l'article L. 171-1 du code de la construction et de l'habitation, doivent remplir l'une des conditions suivantes :
a) Soit bénéficier d'un des labels mentionnés au a du 2° du I de l'article 46 AZA octies ;
b) Soit respecter les exigences de performance énergétique globale dans les mêmes conditions et selon les mêmes modalités que celles définies au b du 2° du I de l'article 46 AZA octies.
3° Les logements qui font ou ont fait l'objet des travaux mentionnés au 5° du B du I de l'article 199 novovicies du code général des impôts doivent remplir l'une des conditions suivantes :<br /><br />a) Soit permettre d'atteindre à la fois une diminution de la consommation conventionnelle d'énergie primaire du bâtiment, définie par un arrêté conjoint des ministres chargés du budget et du logement, et une consommation conventionnelle d'énergie primaire après travaux inférieure au seuil fixé par ce même arrêté ;<br /><br />b) Soit respecter les exigences de performance énergétique fixées par l'arrêté mentionné au a du présent 3° pour au moins deux des cinq catégories suivantes, tout en permettant d'atteindre une consommation conventionnelle d'énergie primaire après travaux inférieure au seuil fixé par ce même arrêté :<br /><br />1. isolation de la toiture ;<br /><br />2. isolation des murs donnant sur l'extérieur ;<br /><br />3. isolation des parois vitrées donnant sur l'extérieur ;<br /><br />4. systèmes de chauffage ;<br /><br />5. système de production d'eau chaude sanitaire.<br /><br />Le même arrêté définit les modalités de justification du respect des exigences prévues aux a et b du présent 3°.
''',
    "Réécriture à droit constant : les trois ensembles de logements et les options techniques sont formulés comme des conditions, en rendant explicite le cumul exigé au sein de chaque option du 3°. Les cinq catégories et la preuve par attestation sont reproduites intégralement. Aucune réforme de fond ne modifie ces exigences fiscales.",
    "Les neuf paragraphes, les 1° à 3°, leurs lettres et les 1 à 5 internes au 3° sont conservés, sans déplacement de l'alinéa visé par la demande d'attestation. Incohérence de renvois à contrôler : les articles R. 172-2 et R. 172-3 du CCH consultés dans le corpus concernent désormais des exigences alternatives pour constructions temporaires et petites constructions ou extensions, alors que la source renvoie à des caractéristiques thermiques et à l'arrêté de 2011. Ils sont conservés sans substitution. Le seuil après travaux reste fixé par arrêté et aucun chiffre n'est inventé.")

add(19, '''
Pour les logements situés outre-mer, la catégorie mentionnée au II de l'article 199 novovicies du code général des impôts comprend les logements qui remplissent les conditions suivantes :
1° En Guyane, en Martinique et à La Réunion, sous réserve du 3°, les logements doivent respecter les prescriptions des articles R. 162-1 et R. 192-2 du code de la construction et de l'habitation ;
2° En Guadeloupe, sous réserve du 3°, les logements doivent respecter les dispositions des délibérations du 19 avril 2011 du conseil régional de la Guadeloupe relevant du domaine du règlement. Ces délibérations portent sur la réglementation thermique et les caractéristiques thermiques de l'enveloppe des bâtiments nouveaux et des parties nouvelles de bâtiments, sur la production d'eau chaude sanitaire par énergie renouvelable ou de récupération dans les bâtiments en Guadeloupe, ainsi que sur les systèmes de refroidissement et la performance énergétique des appareils de climatisation individuels ;
3° En Guadeloupe, en Guyane, en Martinique et à La Réunion, les logements qui font ou ont fait l'objet des travaux mentionnés aux 2°, 3°, 4° et 5° du B du I de l'article 199 novovicies du code général des impôts, ainsi que ceux acquis en l'état futur d'achèvement lorsqu'ils ne sont pas soumis aux prescriptions des articles R. 162-1 et R. 192-2 précités ou aux dispositions des délibérations du 19 avril 2011 du conseil régional de la Guadeloupe précitées, doivent respecter cumulativement :
a. Une exigence thermique, satisfaite par l'intégration au logement de l'un des dispositifs mentionnés au c du 1 du I de l'article 18 quater de l'annexe IV au code général des impôts ;
b. Une exigence énergétique, satisfaite par l'intégration au logement d'au moins un des équipements mentionnés aux 4, 5 et 6 du même I de l'article 18 quater, dans les mêmes conditions.
4° En Nouvelle-Calédonie, en Polynésie française, à Saint-Martin et dans les îles Wallis et Futuna, les logements doivent respecter les exigences prévues aux a et b du 3° ;
5° À Saint-Pierre-et-Miquelon, les logements doivent respecter cumulativement :
a) Une exigence thermique, satisfaite par l'intégration au logement de matériaux d'isolation thermique mentionnés aux 1° et 2° du b du 2 du I de l'article 18 bis de l'annexe IV au code général des impôts ou d'appareils de régulation de chauffage mentionnés au c du même 2 de cet article ;
b) Une exigence énergétique, satisfaite par l'intégration au logement d'au moins un des équipements mentionnés aux 4, 5 et 6 du I de l'article 18 quater de l'annexe IV au code général des impôts, dans les mêmes conditions.
''',
    "Réécriture à droit constant : chaque territoire est associé directement à ses obligations et les deux exigences cumulatives sont formulées de la même manière. La liste complète des territoires, textes et équipements visés demeure présente. Aucune réforme de fond n'étend ni n'allège ce régime outre-mer.",
    "Les cinq cas territoriaux, les réserves du 3°, les lettres et les cumuls sont préservés. Incohérence préexistante : R. 162-1 du CCH concerne l'accessibilité dans le corpus, tandis que R. 192-2 porte sur l'eau chaude sanitaire ; le premier renvoi paraît décalé dans ce contexte énergétique et reste conservé. Les renvois à l'article 18 bis doivent aussi être contrôlés dans la version historiquement applicable : l'article 18 quater consulté vise expressément, pour ses équipements, la version du 31 décembre 2019. La note sur l'arrêté du 13 février 2020 ne fixe aucune date future.")

add(20, '''
Les plafonds par mètre carré de surface habitable mentionnés au premier alinéa du IV de l'article 199 septvicies du code général des impôts sont fixés comme suit selon le lieu où se situe le logement :<br />– zone A : 5 000 € ;<br />– zone B1, ainsi que les départements d'outre-mer, les collectivités d'outre-mer et la Nouvelle-Calédonie mentionnés au XI du même article : 4 000 € ;<br />– zone B2 : 2 100 € ;<br />– zone C : 2 000 €.
Le classement en zones A, B1, B2 et C est celui défini à l'article D. 304-1 du code de la construction et de l'habitation.
La surface habitable retenue est celle définie au troisième alinéa du a de l'article 2 duodecies. Toutefois, pour les départements d'outre-mer, les collectivités d'outre-mer et la Nouvelle-Calédonie mentionnés au XI de l'article 199 septvicies, la surface retenue est celle prévue au III de l'article 46 AG terdecies.
''',
    "Réécriture à droit constant : les montants sont rattachés explicitement à leurs zones et les règles de classement et de surface sont énoncées directement. L'exception de surface outre-mer reste distincte. Aucune réforme de fond ni revalorisation des plafonds n'est appliquée.",
    "Les trois alinéas, les plafonds de 5 000 €, 4 000 €, 2 100 € et 2 000 €, ainsi que les renvois au XI de l'article 199 septvicies, à D. 304-1 et au III de l'article 46 AG terdecies sont conservés. Dans le corpus consulté, le troisième alinéa du a de l'article 2 duodecies définit bien la surface ; sa position doit être préservée lors de toute coordination. La note du décret du 21 août 2019 reste historique.")

add(21, '''
Pour l'application du premier alinéa du A du V de l'article 199 novovicies du code général des impôts, le plafond est de 5 500 € par mètre carré de surface habitable.
En métropole, la surface habitable retenue est celle prévue au dernier alinéa du a de l'article 2 duodecies ; outre-mer, elle est celle prévue au III de l'article 46 AG terdecies.
''',
    "Réécriture à droit constant : le montant est placé à côté de son unité et le choix de la règle de surface est exprimé selon la localisation du logement. Aucune réforme de fond ni modification du plafond n'est appliquée.",
    "Le plafond de 5 500 € et les trois renvois sont maintenus. La surface de métropole et celle d'outre-mer restent distinctes ; aucun changement du champ temporel de l'article 199 novovicies n'est introduit. Le dernier alinéa du a de l'article 2 duodecies demeure la disposition de surface dans le corpus consulté.")

add(22, '''
I. – Pour bénéficier de la réduction d'impôt prévue à l'article 199 sexvicies du code général des impôts, le contribuable joint à sa déclaration de revenus de l'année au titre de laquelle il la demande les pièces suivantes :
1° Une note annexe conforme au modèle fixé par l'administration et comportant les éléments suivants :
a. L'identité et l'adresse du contribuable ;
b. L'adresse du logement concerné ;
c. La date d'achèvement du logement, s'il a été acquis en l'état futur d'achèvement ou s'il est achevé depuis au moins quinze ans ;
d. Le nom et le type de l'établissement ou de la résidence où se situe le logement ;
e. L'engagement de louer le logement meublé à l'exploitant de l'établissement ou de la résidence pendant au moins neuf ans ;
f. Le prix d'acquisition ou de revient du logement retenu pour déterminer la base de la réduction d'impôt ;
2° Une copie du bail conclu avec l'exploitant de l'établissement ou de la résidence. Le bail mentionne la date de prise d'effet de la location et, s'il y a lieu, la durée totale, pour chaque année civile, des périodes pendant lesquelles le propriétaire se réserve l'occupation du logement ;
3° Une copie de l'acte authentique d'acquisition du logement ;
4° Pour un logement achevé depuis au moins quinze ans et ayant fait l'objet de travaux de réhabilitation :
a. Les états descriptifs du logement mentionnés aux 1° et 2° de l'article 2 quindecies C. La personne mentionnée au premier alinéa de cet article qui établit ces états fournit aussi une attestation indiquant que toutes les performances techniques mentionnées au II de l'article 2 quindecies B sont respectées et qu'au moins l'une d'entre elles l'est à la suite des travaux de réhabilitation concernés ;
b. S'ils sont requis, les états prévus aux articles L. 1334-5 et L. 1334-13 du code de la santé publique, fournis par le vendeur lors de la promesse de vente ou annexés à l'acte authentique de vente du logement ;
5° Pour un logement achevé depuis au moins quinze ans et faisant l'objet de travaux de réhabilitation :
a. Les états et l'attestation mentionnés au 4° ;
b. Si l'acquéreur fait réaliser des travaux dans le logement, une copie des factures des entreprises qui les ont réalisés. Ces factures indiquent l'adresse de réalisation des travaux, leur nature et leur montant ;
6° Pour un logement situé dans une résidence de tourisme, une copie de l'arrêté préfectoral portant classement de la résidence ;
7° Pour un logement situé dans une résidence avec services pour personnes âgées ou handicapées, une copie attestant que le gestionnaire des services a obtenu l'agrément prévu à l'article L. 7232-1 du code du travail.
II. – Si l'exploitant change pendant la période couverte par l'engagement de location, le contribuable joint à sa déclaration des revenus de l'année de ce changement une copie du bail conclu avec le nouvel exploitant. Ce bail comporte les mentions prévues au 2° du I.
III. – Pour l'application du dernier alinéa du III de l'article 199 sexvicies du code général des impôts, le conjoint survivant joint une note conforme au modèle fixé par l'administration à la déclaration des revenus qu'il souscrit au titre de l'année du décès de son conjoint pour la période postérieure au décès. Par cette note, il s'engage à louer le logement meublé à l'exploitant de l'établissement ou de la résidence pendant la fraction de la période de neuf ans de l'engagement initial qui reste à courir à la date du décès.
Si l'exploitant de l'établissement ou de la résidence change, les dispositions du II s'appliquent.
''',
    "Réécriture à droit constant : les pièces sont présentées comme les obligations directes du contribuable, les cas de réhabilitation restent séparés et les mentions du bail et de la reprise par le conjoint sont explicitées en phrases plus courtes. Aucune réforme de fond n'est appliquée à cette réduction d'impôt ni aux locations anciennes.",
    "Les I à III, 1° à 7° et toutes les lettres sont conservés dans leurs vingt et un alinéas. Le seuil d'au moins quinze ans, l'engagement d'au moins neuf ans, la distinction entre travaux réalisés et en cours, les états sanitaires seulement lorsqu'ils sont requis et les mentions des factures sont maintenus. Le conjoint ne reprend que la durée restant à courir au décès. Au 7°, la rédaction source « par le gestionnaire des services » est ambiguë : la proposition l'entend comme l'agrément obtenu par le gestionnaire, conformément à L. 7232-1 qui prévoit sa délivrance par l'autorité compétente ; cette articulation appelle contrôle. La note sur la loi du 23 juillet 2010 est historique. Les renvois au code de la santé publique sont préservés ; ce code n'est pas fourni dans le corpus autorisé et leur concordance reste à contrôler.")

add(23, '''
Pour les logements neufs acquis achevés ou en l'état futur d'achèvement, le contribuable justifie du respect de la condition prévue au premier alinéa du II de l'article 199 septvicies du code général des impôts en présentant, à la demande de l'administration fiscale, l'un des documents suivants :
a) La synthèse d'étude thermique mentionnée au 2 de l'article 10 de l'arrêté du 24 mai 2006 relatif aux caractéristiques thermiques des bâtiments nouveaux et des parties nouvelles de bâtiments ;
b) L'attestation mentionnée à l'article 6 de l'arrêté du 11 octobre 2011 relatif aux attestations de prise en compte de la réglementation thermique et de réalisation d'une étude de faisabilité relative aux approvisionnements en énergie pour les bâtiments neufs ou les parties nouvelles de bâtiments ;
c) Le récapitulatif standardisé d'étude thermique mentionné à l'article 9 de l'arrêté du 26 octobre 2010 relatif aux caractéristiques thermiques et aux exigences de performance énergétique des bâtiments nouveaux et des parties nouvelles de bâtiments ;
d) Le certificat délivré par un organisme de certification et mentionnant l'attribution d'un label « haute performance énergétique », selon les critères et dans les conditions fixés par l'arrêté du 3 mai 2007 relatif au contenu et aux conditions d'attribution du label « haute performance énergétique ».
''',
    "Réécriture à droit constant : le champ des logements est placé en tête et le contribuable est désigné directement comme tenu de présenter l'un des quatre justificatifs. La dernière pièce est formulée avec son auteur avant ses conditions. Les intitulés techniques et réglementaires sont conservés, sans réforme de fond.",
    "Les quatre pièces restent alternatives, et exigibles seulement sur demande. Les références au 2 de l'article 10 de l'arrêté du 24 mai 2006, à l'article 6 de celui du 11 octobre 2011, à l'article 9 de celui du 26 octobre 2010 et à l'arrêté du 3 mai 2007 sont intégralement préservées. Aucun label récent n'est substitué aux justificatifs du régime ancien.")

assert len(sources) == len(answers) == 24
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
