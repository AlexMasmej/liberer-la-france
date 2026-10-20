import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes, *, removed=None, repeal=None):
    item = {
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }
    if removed:
        item.update(change_type='normative_reduction',
                    reform_policy_id='editorial_direction_2026_10_19',
                    removed_provisions=removed)
    if repeal:
        item.update(change_type='full_repeal',
                    repeal_policy_id='editorial_direction_2026_10_19',
                    repeal_scope=repeal)
    assert number not in drafts
    drafts[number] = item


add('L2222-3-1', '''
<p>Une convention ou un accord collectif peut fixer une méthode de négociation destinée à assurer la loyauté des échanges et la confiance mutuelle entre les parties.</p>
<p>Les parties déterminent librement le contenu de cette convention ou de cet accord. Elles peuvent préciser les informations partagées entre les négociateurs, notamment, dans l'entreprise, à partir de la base de données prévue à l'article L. 2312-18, et les principales étapes des négociations. Elles peuvent également prévoir des moyens supplémentaires ou spécifiques, notamment des crédits d'heures pour les représentants syndicaux ou le recours à l'expertise, pour le bon déroulement d'une ou de plusieurs négociations. Les informations exactes et à jour déjà accessibles aux négociateurs dans cette base n'ont pas à leur être remises une seconde fois ; leur mise à disposition doit leur permettre de les consulter effectivement pour la négociation. Cette dispense de remise en double ne réduit ni les droits d'accès ni les obligations légales d'information des négociateurs.</p>
<p>Sauf stipulation contraire de cette convention ou de cet accord, le non-respect de ses stipulations n'entraîne pas la nullité des accords conclus si les parties ont respecté le principe de loyauté.</p>
<p>La liberté de définir le contenu de l'accord de méthode s'applique aux conventions et accords conclus à compter de l'entrée en vigueur de la loi. Les stipulations des conventions et accords antérieurs restent applicables selon leurs propres conditions. La dispense de remise en double s'applique aux communications restant à effectuer à cette date, sans remettre en cause les obligations déjà exigibles ni les droits et recours nés antérieurement.</p>
''',
    "Réforme de fond : les accords de méthode ne sont plus tenus de contenir une liste d'informations et un déroulement type ; une dispense de remise en double des informations déjà effectivement accessibles est instaurée. La méthode demeure facultative. À droit constant sont conservés la loyauté, la confiance mutuelle, la possibilité de moyens syndicaux supplémentaires et d'expertise, ainsi que le régime de nullité et sa réserve conventionnelle.",
    "Le renvoi source à L. 2323-8 est obsolète : aucun article de ce numéro ne figure dans le corpus en vigueur. Coordination expressément proposée avec L. 2312-18, lu dans le corpus, qui institue la base de données économiques, sociales et environnementales. La dispense ne crée pas un droit d'accès indifférencié à la base et ne remplace pas les informations nécessaires à une négociation loyale. L. 2222-3 et les obligations de négociation du titre IV restent distincts ; leur calendrier légal n'est pas supprimé. Les accords antérieurs ne sont pas libérés rétroactivement de leurs engagements.",
    removed=[
        "Obligation d'insérer dans tout accord de méthode la nature des informations partagées entre les négociateurs.",
        "Obligation d'insérer dans tout accord de méthode les principales étapes du déroulement des négociations."
    ])

add('L2222-3-2', '''
<p>Un accord de branche définit la méthode de négociation applicable dans l'entreprise. Il s'applique aux entreprises qui n'ont pas conclu de convention ou d'accord sur le fondement de l'article L. 2222-3-1. Lorsqu'une telle convention ou un tel accord est conclu, ses stipulations remplacent celles de l'accord de branche.</p>
<p>Sauf stipulation contraire de l'accord de branche mentionné au premier alinéa, le non-respect de ses stipulations n'entraîne pas la nullité des accords conclus dans l'entreprise si les parties ont respecté le principe de loyauté.</p>
''',
    "Réécriture à droit constant : identification directe de la méthode de branche, de son application supplétive et de la substitution de l'accord d'entreprise. Le régime de nullité est formulé avec un sujet explicite. La priorité de la méthode négociée dans l'entreprise sert déjà l'orientation de décentralisation ; elle est maintenue.",
    "Renvoi à L. 2222-3-1 conservé et coordonné avec l'allègement de son contenu obligatoire. Le texte n'impose pas ici de conclure un accord de branche ou d'entreprise. La réserve permettant à l'accord de branche de prévoir une conséquence différente en cas de méconnaissance est conservée ; la loyauté reste requise. Aucun changement des conditions de représentativité ou de validité des accords collectifs.")

add('L2222-3-3', '''
<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Les conventions et accords conclus à compter de cette date ne sont plus soumis à l'obligation légale de comporter un préambule.</p>
<p>Les préambules des conventions et accords antérieurs conservent leur portée. L'absence de préambule dans ces textes ne peut entraîner leur nullité. L'abrogation ne remet pas en cause les droits et les effets produits avant son entrée en vigueur.</p>
''',
    "Abrogation de fond : suppression de l'obligation de rédiger un préambule présentant les objectifs et le contenu, formalité qui ne conditionnait déjà pas la validité du texte. Les parties peuvent toujours choisir de rédiger un préambule ; les préambules existants et la protection des accords qui en sont dépourvus sont préservés.",
    "Aucun renvoi à cet article relevé dans les textes du corpus travail consultés. Les règles de consentement, de négociation loyale, d'écrit et de publicité ne sont pas affectées. La date d'entrée en vigueur dépend de la loi proposée et ne reprend pas la date historique du 10 août 2016.",
    repeal="Obligation légale d'inclure dans chaque convention ou accord collectif un préambule exposant succinctement ses objectifs et son contenu, supprimée pour les textes nouveaux.")

add('L2222-4', '''
<p>Une convention ou un accord peut être conclu pour une durée déterminée ou pour une durée indéterminée.</p>
<p>Si la convention ou l'accord ne fixe pas sa durée, il est conclu pour cinq ans.</p>
<p>La convention ou l'accord conclu pour une durée déterminée cesse de produire ses effets à son expiration.</p>
''',
    "Réécriture à droit constant : la liberté de durée, la durée supplétive de cinq ans et la cessation des effets à l'échéance sont exprimées séparément. La règle supplétive évite aux parties une clause obligatoire et garantit une échéance identifiable ; sa suppression créerait une incertitude sur les accords silencieux.",
    "Durée de cinq ans intégralement conservée. Les paragraphes purement vides et les sauts de ligne de présentation sont retirés sans déplacement d'un alinéa normatif. Aucune reconduction tacite ni transformation des accords antérieurs n'est introduite. L'expiration d'un accord à durée déterminée reste distincte de la dénonciation régie par L. 2261-9 et suivants.")

add('L2222-5', '''
<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Les conventions et accords conclus à compter de cette date ne sont plus tenus de fixer les formes et le délai de leur renouvellement ou de leur révision. L'absence de ces clauses ne peut faire obstacle à leur extension au titre du 2° du I de l'article L. 2261-22.</p>
<p>Les clauses des conventions et accords antérieurs relatives au renouvellement ou à la révision restent applicables selon leurs conditions. Les règles légales de durée, de renouvellement et de révision, notamment celles des articles L. 2222-4, L. 2261-7, L. 2261-7-1 et L. 2261-8, demeurent applicables. Les droits, obligations et recours nés avant l'entrée en vigueur de l'abrogation sont préservés.</p>
''',
    "Abrogation de fond : suppression de la clause obligatoire de procédure et de délai de renouvellement ou de révision, sans supprimer la faculté de négocier ces modalités. Les règles légales de validité et de révision suffisent à encadrer les opérations futures. La condition d'extension qui réintroduirait la même charge est expressément neutralisée pour ce seul objet.",
    "L. 2261-22, lu intégralement, renvoie à L. 2222-5 au 2° de son I : sa coordination formelle doit retirer ce renvoi, sans toucher aux autres conditions d'extension. L. 2261-7, L. 2261-7-1 et L. 2261-8 ont été vérifiés ; les habilitations, majorités, substitution des avenants et dépôt demeurent. Les clauses antérieures ne sont pas réputées non écrites. Aucun renouvellement automatique n'est créé à l'échéance de cinq ans.",
    repeal="Obligation d'insérer dans chaque convention ou accord les formes et le délai de renouvellement ou de révision, ainsi que son exigence redondante comme condition d'extension pour les textes nouveaux.")

add('L2222-5-1', '''
<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Les conventions et accords conclus à compter de cette date ne sont plus tenus de définir des conditions de suivi ni de comporter des clauses de rendez-vous.</p>
<p>Les conditions de suivi et les clauses de rendez-vous déjà stipulées restent applicables selon leurs conditions. Pour les conventions et accords conclus avant cette date, leur absence ou leur méconnaissance ne peut, à elle seule, entraîner la nullité de la convention ou de l'accord. Les droits et recours nés avant cette date sont préservés.</p>
''',
    "Abrogation de fond : suppression de l'obligation générale de clauses de suivi et de rendez-vous, sans obligation de les remplacer par un dispositif équivalent. Leur contenu peut être librement négocié lorsque le suivi présente une utilité. Les engagements existants et l'absence de nullité pour les anciens accords sont conservés.",
    "La suppression ne porte que sur le suivi général prescrit par cet article ; les obligations sectorielles de suivi, de négociation périodique et d'information résultant d'autres dispositions demeurent. Aucun renvoi à L. 2222-5-1 relevé dans le corpus travail consulté. Le régime des clauses librement souscrites dans les textes futurs relève de leurs stipulations et des règles générales, sans extinction des créances antérieures.",
    repeal="Obligation légale générale de définir le suivi de toute convention ou de tout accord collectif et d'y insérer des clauses de rendez-vous, supprimée pour les textes nouveaux.")

add('L2222-6', '''
<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Les conventions et accords conclus à compter de cette date ne sont plus tenus de comporter des clauses fixant les conditions de leur dénonciation et la durée du préavis. L'absence de ces clauses ne peut faire obstacle à leur extension au titre du 2° du I de l'article L. 2261-22.</p>
<p>Les clauses de dénonciation des conventions et accords antérieurs restent applicables selon leurs conditions. Les règles légales de dénonciation des articles L. 2261-9 à L. 2261-13 demeurent applicables, notamment le préavis de trois mois à défaut de stipulation expresse, la notification, le dépôt et les garanties attachées aux effets de la dénonciation. Les dénonciations intervenues avant l'entrée en vigueur de l'abrogation, leurs effets et les droits et recours qui s'y rattachent conservent leur régime.</p>
''',
    "Abrogation de fond : suppression de la clause obligatoire de dénonciation et de préavis qui répétait un mécanisme déjà organisé par la loi. Le préavis supplétif de trois mois et les garanties de survie et de rémunération ne sont pas supprimés. La condition d'extension redondante est écartée pour les conventions nouvelles, sans annuler les clauses existantes.",
    "Coordination formelle nécessaire au 2° du I de L. 2261-22 pour supprimer le renvoi à L. 2222-6 ; ses autres conditions subsistent. L. 2261-9 à L. 2261-13 ont été lus : préavis de trois mois, périodes de survie d'un an et garantie de rémunération restent dans leurs champs respectifs. Aucun droit de dénoncer un accord à durée déterminée n'est ajouté et aucune procédure déjà engagée n'est recommencée.",
    repeal="Obligation d'insérer dans chaque convention ou accord les conditions de dénonciation et la durée du préavis, y compris comme condition d'extension pour les textes nouveaux ; maintien des garanties légales et des clauses antérieures.")

add('L2231-1', '''
<p>Une convention ou un accord est conclu entre :</p>
<p>- du côté des salariés, une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord ;</p>
<p>- du côté des employeurs, une ou plusieurs organisations syndicales d'employeurs, toute autre association d'employeurs ou un ou plusieurs employeurs agissant individuellement.</p>
<p>Les associations d'employeurs constituées conformément à la loi du 1er juillet 1901 relative au contrat d'association et compétentes pour négocier des conventions et accords sont assimilées aux organisations syndicales pour l'exercice des attributions que le présent titre confère à celles-ci.</p>
''',
    "Réécriture à droit constant : les deux côtés de la négociation sont nommés directement et l'assimilation des associations d'employeurs est formulée avec ses deux conditions cumulatives. La représentativité et la capacité des signataires garantissent la légitimité des normes collectives ; elles ne constituent pas des formalités redondantes à supprimer.",
    "Maintien des organisations multiples, des employeurs pris individuellement et des associations régies par la loi du 1er juillet 1901. L'assimilation demeure limitée aux attributions du présent titre. Les règles particulières de négociation d'entreprise sans délégué syndical et les autres conditions de représentativité restent dans leur champ propre.")

add('L2231-2', '''
<p>Les représentants des organisations mentionnées à l'article L. 2231-1 peuvent engager l'organisation qu'ils représentent lorsqu'ils sont habilités par l'un des moyens suivants :</p>
<p>1° Une stipulation des statuts de l'organisation ;</p>
<p>2° Une délibération spéciale de l'organisation ;</p>
<p>3° Des mandats spéciaux écrits que tous les adhérents de l'organisation leur donnent individuellement.</p>
<p>Les associations d'employeurs fixent elles-mêmes leurs modalités de délibération.</p>
''',
    "Réécriture à droit constant : les trois sources alternatives d'habilitation sont présentées sans répétition de « soit ». Les mandats individuels de tous les adhérents demeurent une possibilité, et non une obligation ajoutée aux statuts ou à une délibération. L'habilitation protège le consentement collectif et prévient les engagements sans pouvoir.",
    "Numéros 1°, 2° et 3° conservés. Le caractère spécial et écrit des mandats du 3° et leur attribution individuelle par tous les adhérents sont maintenus. Les modes statutaires ou délibératifs restent des alternatives moins lourdes ; aucune légalisation, certification ni procédure administrative supplémentaire n'est introduite.")

add('L2231-3', '''
<p>La validité d'une convention ou d'un accord est subordonnée à son établissement par écrit.</p>
''',
    "Réécriture à droit constant de l'exigence d'écrit et de sa sanction de nullité : la condition de validité est énoncée directement. Le support écrit est essentiel à la preuve et à la connaissance des droits collectifs, ce qui justifie son maintien.",
    "La condition de validité conserve la portée de l'expression source « à peine de nullité ». Aucune exigence de support papier, de dépôt supplémentaire ou de certification n'est ajoutée. La brièveté de la norme ne justifie pas une extension artificielle du texte.")

add('L2231-4', '''
<p>Les conventions et accords, y compris les conventions d'entreprise ou d'établissement, sont rédigés en français.</p>
<p>Une clause rédigée dans une langue étrangère ne peut être opposée à un salarié lorsque son application lui ferait grief.</p>
''',
    "Réécriture à droit constant : le champ comprend expressément l'entreprise et l'établissement ; la sanction est rattachée au salarié auquel la clause fait grief. L'accès intelligible à la norme collective est une protection utile, conservée sans nouvelle formalité de traduction certifiée.",
    "Maintien de l'inopposabilité au salarié lésé, distincte d'une nullité générale de la convention. Aucun droit d'invoquer une version étrangère au détriment du salarié ni obligation d'une traduction dans toutes les langues n'est créé.")

add('L2231-5', '''
<p>À l'issue de la procédure de signature d'une convention ou d'un accord, l'organisation signataire qui agit la première en notifie le texte à toutes les organisations représentatives.</p>
''',
    "Réécriture à droit constant : le moment de la notification, son auteur et tous ses destinataires sont explicités. Une seule organisation signataire agit pour la notification ; aucune notification cumulative par chaque signataire n'est requise. Cette information ouvre les droits d'opposition et doit être conservée.",
    "La formule « qui agit la première » explicite la partie la plus diligente sans désigner un employeur non visé comme auteur exclusif. Le texte complet est notifié à toutes les organisations représentatives, y compris non signataires. L. 2232-2 maintient le délai de quinze jours à compter de la notification ; la publication publique et le dépôt ne s'y substituent pas. L. 2261-19 renvoie également à cet article pour l'opposition patronale à l'extension, dans son propre champ.")

add('L2231-5-1', '''
<p>Les conventions et accords de branche, de groupe, interentreprises, d'entreprise et d'établissement sont rendus publics dans une base de données nationale. Son contenu est publié en ligne dans un standard ouvert permettant une réutilisation aisée. La version publiée ne comporte ni les noms ni les prénoms des négociateurs et des signataires.</p>
<p>Après la conclusion d'une convention ou d'un accord de groupe, interentreprises, d'entreprise ou d'établissement, les parties peuvent décider qu'une partie du texte ne sera pas publiée au titre du premier alinéa. Elles consignent cette décision dans un acte joint à la version intégrale lors du dépôt prévu à l'article L. 2231-6. L'employeur peut également occulter les éléments dont la publication porterait atteinte aux intérêts stratégiques de l'entreprise. Le déposant identifie les passages exclus de la publication. À partir du texte intégral déposé et de ces indications, le service dépositaire établit la version destinée à la publication ; il ne peut exiger du déposant une seconde version du texte. Seule la version respectant les exclusions de publication et l'omission des noms et prénoms prévue au premier alinéa est rendue publique.</p>
<p>Un décret en Conseil d'État fixe les conditions d'application du présent article.</p>
<p>Ne sont pas soumis à la publication prévue au présent article les accords d'intéressement et de participation, les plans d'épargne d'entreprise et interentreprises, les plans d'épargne pour la retraite collectifs, les plans d'épargne retraite d'entreprise collectifs ainsi que les accords mentionnés aux articles L. 1233-24-1 et L. 2254-2.</p>
<p>La dispense de fournir une version distincte destinée à la publication s'applique aux dépôts effectués à compter de l'entrée en vigueur de la loi, y compris pour les conventions et accords conclus antérieurement. Les dépôts déjà accomplis ne sont pas renouvelés. Les actes de non-publication et les occultations valablement effectués avant cette date restent applicables.</p>
''',
    "Réforme de fond : suppression du dépôt d'une seconde version publiable, en plus du texte intégral signé. Le service dépositaire effectue les occultations à partir des indications du déposant. À droit constant sont maintenus la publicité nationale réutilisable, l'anonymisation, l'acte des parties, la protection des intérêts stratégiques, le décret en Conseil d'État et toutes les catégories exclues de la publication.",
    "Coordonner D. 2231-7, 2° a, et R. 2231-1-1 avec l'établissement de la version publiable par le service. Le corpus présente deux discordances préexistantes : R. 2231-1-1 vise aussi des accords de branche pour l'acte de non-publication alors que le deuxième alinéa législatif ne les vise pas ; son II conserve une anonymisation sur demande alors que le premier alinéa législatif l'impose. La proposition conserve le champ législatif et impose le respect de l'anonymisation sans demande. Ne pas étendre les occultations à la notification intégrale aux organisations ni à l'accès juridictionnel. Note historique lue : application de l'ordonnance n° 2019-766, article 9 I, au plus tard le 1er janvier 2020, effectivement fixée au 1er octobre 2019 par le décret n° 2019-807, article 9 II ; ces dates ne sont pas celles de la réforme proposée. Aucune de ces anciennes catégories de plans n'est retirée au motif qu'elle serait historique.",
    removed=[
        "Obligation pour le déposant de préparer et déposer une version distincte de la convention ou de l'accord destinée à la publication, en plus de la version intégrale."
    ])

add('L2231-6', '''
<p>Les conventions et accords sont déposés une seule fois auprès du service compétent. Un exemplaire intégral signé suffit ; aucun exemplaire supplémentaire sur papier ni dépôt distinct au greffe du conseil de prud'hommes ne peut être exigé du déposant. Le service dépositaire assure la conservation du texte et sa transmission au greffe compétent.</p>
<p>Les pièces nécessaires au dépôt ne peuvent être demandées une seconde fois lorsqu'elles sont déjà légalement accessibles au service dépositaire, exactes et à jour. Le déposant indique les références permettant de les retrouver. Les éléments nouveaux ou modifiés et ceux que le service ne peut légalement obtenir restent à fournir. Cette dispense ne supprime ni la preuve de la signature, ni celle de la notification, ni les actes et indications nécessaires à la protection des informations exclues de la publication.</p>
<p>Les modalités du dépôt et de délivrance du récépissé sont fixées par voie réglementaire, sans rétablir les remises en double supprimées par le présent article. Le dépôt auprès du service compétent produit ses effets sans attendre la transmission au greffe.</p>
<p>Ces règles s'appliquent aux dépôts effectués à compter de l'entrée en vigueur de la loi, même lorsque la convention ou l'accord a été conclu antérieurement. Les dépôts déjà accomplis et leur date d'effet sont conservés ; aucun nouveau dépôt n'est requis pour ce seul motif et aucun délai expiré n'est rouvert.</p>
''',
    "Réforme de fond : le dépôt devient unique ; sont supprimés le double exemplaire papier et électronique, le dépôt séparé au greffe et la remise répétée de pièces légalement disponibles. Le service transmet au greffe. Le dépôt, la version signée, la preuve de notification et le récépissé demeurent afin de garantir la preuve et l'application des accords. L'unicité est opposable au règlement.",
    "Coordinations réglementaires précises : D. 2231-2 I pour le double support, D. 2231-2 III pour le dépôt au greffe, D. 2231-4 pour la plateforme et D. 2231-6 et D. 2231-7 pour les pièces et le récépissé. La version publiable distincte est supprimée par la proposition de L. 2231-5-1. L. 2261-1, lu dans le corpus, conserve sauf stipulation contraire l'application le lendemain du dépôt auprès du service compétent ; la transmission au greffe ne devient pas un nouveau fait déclencheur. L. 2261-8 renvoie à ce dépôt pour les avenants ; la notification de dénonciation et son dépôt prévus par L. 2261-9 et D. 2231-8 restent des actes distincts, sans redépôt du texte initial. Le droit de consultation et de copie de R. 2231-9 subsiste. Les modes de dépôt restent déterminés par le règlement : pas d'obligation numérique exclusive créée ici.",
    removed=[
        "Obligation réglementaire de déposer simultanément une version papier signée et une version électronique du même texte collectif.",
        "Obligation pour le déposant de remettre séparément un exemplaire de chaque convention ou accord au greffe du conseil de prud'hommes.",
        "Obligation de fournir à nouveau les pièces nécessaires au dépôt déjà légalement accessibles au service, exactes et à jour, sous réserve de leur identification."
    ])

add('L2231-8', '''
<p>L'opposition à l'entrée en vigueur d'une convention ou d'un accord est formulée par écrit. Elle expose ses motifs et précise les points de désaccord.</p>
<p>L'auteur de l'opposition la notifie aux signataires.</p>
''',
    "Réécriture à droit constant : les exigences de forme, de motivation et d'identification des désaccords sont séparées de la notification, dont l'auteur devient explicite. Elles rendent l'opposition vérifiable et permettent le contradictoire ; leur suppression fragiliserait les droits des parties.",
    "Les deux alinéas normatifs sont conservés. Aucun délai n'est ajouté : celui de quinze jours pour les accords interprofessionnels reste fixé à L. 2232-2. Le présent article ne transforme pas toute opposition en opposition majoritaire ; les seuils demeurent régis par les dispositions propres au niveau de négociation.")

add('L2231-9', '''
<p>Sont réputés non écrits, dans les conditions du chapitre II, les conventions et accords qui font l'objet d'une opposition majoritaire ainsi que ceux qui n'ont pas été approuvés par la majorité des salariés.</p>
''',
    "Réécriture à droit constant : les deux causes qui privent le texte d'effet sont réunies autour d'un sujet clairement identifié et la qualification de texte réputé non écrit est conservée. Le contrôle majoritaire garantit la légitimité de la norme collective et justifie le maintien de cette règle.",
    "Renvoi au chapitre II conservé pour les champs, procédures et majorités respectifs. Aucune consultation de salariés n'est rendue obligatoire hors des cas prévus par ce chapitre, et une simple opposition minoritaire n'entraîne pas l'effet prévu ici.")

add('L2232-1', '''
<p>Un accord interprofessionnel peut couvrir le territoire national ou avoir un champ d'application défini à l'échelle régionale ou locale.</p>
''',
    "Réécriture à droit constant : les trois échelles territoriales sont exprimées comme des champs possibles de l'accord. Cette liberté ne crée ni autorisation ni charge de dossier et est maintenue.",
    "Les niveaux national, régional et local sont tous conservés. Le périmètre départemental n'est pas ajouté comme catégorie autonome. La nationalité du champ des branches prévue par L. 2232-5-2 n'est pas transposée aux accords interprofessionnels.")

add('L2232-2', '''
<p>Pour être valide, un accord interprofessionnel doit être signé par une ou plusieurs organisations syndicales de salariés représentatives ayant obtenu au moins 30 % des suffrages exprimés en faveur des organisations reconnues représentatives au niveau considéré, aux élections retenues pour mesurer l'audience prévue au 3° de l'article L. 2122-9, quel que soit le nombre de votants. Il ne doit pas faire l'objet de l'opposition d'une ou de plusieurs organisations syndicales de salariés représentatives ayant obtenu la majorité des suffrages exprimés en faveur des mêmes organisations, aux mêmes élections et quel que soit le nombre de votants.</p>
<p>Le délai pour formuler l'opposition est de quinze jours à compter de la date de notification de l'accord. L'opposition respecte les conditions prévues à l'article L. 2231-8.</p>
''',
    "Réécriture à droit constant : la signature à 30 % et l'absence d'opposition majoritaire sont expliquées en deux phrases dans le même alinéa. Les suffrages de référence et l'indifférence au nombre de votants sont conservés dans les deux conditions. Le délai d'opposition reste dans le deuxième alinéa. Ces garanties de représentativité ne sont pas des doublons administratifs.",
    "Contrôle des paramètres : au moins 30 %, majorité calculée parmi les suffrages en faveur des organisations reconnues représentatives, mêmes élections, indépendamment du nombre de votants ; quinze jours à compter de la notification et renvois au 3° de L. 2122-9 et à L. 2231-8 conservés. La note source a été lue intégralement : le I de l'article 12 de la loi n° 2008-789 du 20 août 2008 maintient, jusqu'à la détermination des organisations représentatives dans les branches et au niveau interprofessionnel, les anciennes rédactions de L. 2232-2, L. 2232-6 et L. 2232-7, avec suffrages pris en compte quel que soit le nombre de votants. Cette règle législative extérieure n'est ni abrogée ni réactivée ; elle demeure la référence pour l'appréciation des accords relevant de sa période historique.")

add('L2232-2-1', '''
<p>Une organisation syndicale catégorielle affiliée à une confédération syndicale catégorielle et reconnue représentative des salariés qu'elle a statutairement vocation à représenter peut négocier toute disposition applicable à cette catégorie de salariés.</p>
<p>Lorsqu'un accord interprofessionnel concerne uniquement une catégorie professionnelle déterminée relevant d'un collège électoral, sa validité exige la signature d'une ou de plusieurs organisations syndicales de salariés représentatives ayant obtenu au moins 30 % des suffrages exprimés dans ce collège en faveur des organisations reconnues représentatives à ce niveau, aux élections retenues pour mesurer l'audience prévue au 3° de l'article L. 2122-9, quel que soit le nombre de votants. Il ne doit pas faire l'objet de l'opposition d'une ou de plusieurs organisations syndicales de salariés représentatives ayant obtenu, dans ce collège, la majorité des suffrages exprimés en faveur des mêmes organisations, aux mêmes élections et quel que soit le nombre de votants.</p>
''',
    "Réécriture à droit constant : le droit de négocier de l'organisation catégorielle et les conditions de validité de l'accord limité à une catégorie sont distingués selon la séparation déjà présente dans la source. Les deux conditions de validité sont exprimées en phrases distinctes, sans changer les collèges ni les suffrages de référence. Les garanties de représentation catégorielle sont maintenues.",
    "Maintien cumulatif de l'affiliation à une confédération catégorielle, de la représentativité et de la vocation statutaire. Le second alinéa conserve l'exclusivité de la catégorie visée, son rattachement à un collège électoral, au moins 30 %, la majorité d'opposition dans ce même collège et l'indifférence au nombre de votants dans les deux calculs. Renvoi au 3° de L. 2122-9 conservé. Le saut de ligne interne de la source matérialisant les deux règles est rendu par deux paragraphes, sans déplacement de leur ordre.")

add('L2232-3', '''
<p>Les accords interprofessionnels précisent les garanties accordées aux salariés des entreprises pour leur participation aux négociations ou aux réunions des instances paritaires instituées par ces accords : les modalités d'exercice du droit de s'absenter, la compensation des pertes de salaire ou le maintien du salaire, ainsi que l'indemnisation des frais de déplacement.</p>
''',
    "Réécriture à droit constant : le bénéficiaire et les deux situations de participation sont clarifiés. Les trois catégories de garanties sont conservées. Ces garanties rendent l'exercice de la négociation possible et empêchent qu'il soit financé personnellement par les salariés participants ; elles justifient de maintenir l'obligation conventionnelle.",
    "Maintien des modalités d'absence, de l'alternative compensation des pertes de salaire ou maintien de celui-ci, et du remboursement des déplacements, sans plafond ni tarif inventé. L'abrogation proposée de L. 2232-4 ne retire pas ces droits aux salariés participant à une instance paritaire maintenue ou créée volontairement. Le renvoi du 3° du I de L. 2261-22 à L. 2232-3 reste distinct de la suppression des clauses formelles du 2°.")

add('L2232-4', '''
<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Les accords interprofessionnels conclus à compter de cette date ne sont plus tenus d'instituer une commission paritaire d'interprétation.</p>
<p>Les commissions instituées par des accords antérieurs continuent d'exercer leurs missions dans les conditions prévues par ces accords, jusqu'à leur modification ou leur cessation régulière. Les droits, obligations et recours nés avant l'entrée en vigueur de l'abrogation sont préservés. L'abrogation ne limite ni le recours au juge ni les obligations distinctes relatives aux commissions prévues à l'article L. 2232-9.</p>
''',
    "Abrogation de fond : suppression de la création obligatoire d'une commission d'interprétation pour chaque accord interprofessionnel. Les parties peuvent conserver une commission commune ou créer un organe adapté sans obligation légale nouvelle. Les instances conventionnelles existantes, le juge et les commissions légales distinctes restent compétents dans leur champ.",
    "L. 2232-9 a été vérifié : la commission paritaire permanente de négociation et d'interprétation de branche et ses missions ne sont pas supprimées. L. 2261-19, qui exige une négociation dans la commission qu'il vise pour l'extension, demeure applicable. Aucun renvoi direct à L. 2232-4 relevé dans le corpus travail consulté. L. 2232-3 continue de protéger les participants aux instances paritaires effectivement instituées. La réforme ne met pas fin de plein droit aux commissions antérieures ni aux dossiers dont elles sont saisies.",
    repeal="Obligation pour tout accord interprofessionnel d'instituer une commission paritaire d'interprétation, supprimée pour les accords nouveaux sans dissolution des commissions déjà convenues ni restriction du recours au juge.")

add('L2232-5', '''
<p>Les conventions de branche et les accords professionnels peuvent avoir un champ d'application territorial national, régional ou local.</p>
<p>Sauf disposition contraire, l'expression « convention de branche » comprend la convention collective, les accords de branche, les accords professionnels et les accords interbranches.</p>
''',
    "Réécriture à droit constant : la portée territoriale et la définition conventionnelle de l'expression sont formulées directement. Aucune autorisation supplémentaire n'est imposée et aucune des catégories incluses dans la définition n'est retranchée.",
    "Tension préexistante à conserver visible : cet article permet les niveaux national, régional ou local, tandis que le premier alinéa de L. 2232-5-2 énonce un champ national des branches assorti d'adaptations locales. La proposition n'efface pas cette articulation par une suppression implicite. L. 2261-32 I, 3°, prévoit en outre un motif de restructuration lié au champ uniquement régional ou local ; aucun de ses effets n'est modifié ici. La réserve « sauf disposition contraire » et les accords interbranches sont conservés.")

add('L2232-5-1', '''
<p>La branche exerce les missions suivantes :</p>
<p>1° Définir les conditions d'emploi et de travail des salariés ainsi que les garanties qui leur sont applicables dans les matières mentionnées aux articles L. 2253-1 et L. 2253-2, selon les conditions prévues par ces articles ;</p>
<p>2° Réguler la concurrence entre les entreprises comprises dans son champ d'application.</p>
''',
    "Réécriture à droit constant : les deux missions sont présentées avec des verbes directs. La définition des garanties de branche demeure limitée aux matières et conditions des articles visés. Ces missions ne prescrivent pas de déclaration ou de prélèvement identifiable à retirer dans cet article ; les protections collectives et leur articulation sont maintenues.",
    "Numéros 1° et 2° conservés. L. 2253-1 et L. 2253-2 ont été lus : les matières réservées, l'équivalence des garanties et les conditions du verrouillage de branche ne sont pas remplacées ici par une priorité générale de l'entreprise. La priorité d'entreprise de L. 2253-3 demeure dans son champ. Coordination de fond à assurer dans le véritable article L. 2253-1, notamment son 10° sur le renouvellement de l'essai et son 6° renvoyant au temps partiel, avec les transitions de coordination.json ; le présent article de mission ne doit pas rétablir le renouvellement pour les nouveaux CDI ni le plancher général légal supprimé, ni supprimer les minima conventionnels plus favorables. Aucun changement automatique des contrats antérieurs ou des autres régimes.")

add('L2232-5-2', '''
<p>Le champ d'application des branches est national. Toutefois, certaines stipulations de leurs conventions et accords peuvent être définies, adaptées ou complétées au niveau local.</p>
<p>Les organisations d'employeurs constituées conformément à l'article L. 2131-2 et affiliées ou adhérentes aux organisations d'employeurs reconnues représentatives dans la branche peuvent négocier, dans le périmètre de cette branche, des accords collectifs régionaux, départementaux ou locaux et en demander l'extension.</p>
''',
    "Réécriture à droit constant : la règle nationale et sa faculté d'adaptation locale sont distinguées de l'habilitation des organisations d'employeurs. Les critères d'habilitation et la faculté de demander l'extension sont conservés. L'article permet déjà une négociation décentralisée sans créer de dépôt ou d'autorisation supplémentaire propre à supprimer.",
    "Maintien des niveaux régional, départemental et local, de l'alternative affiliation ou adhésion, du périmètre de branche et du renvoi à L. 2131-2. L'extension reste une demande soumise à ses conditions légales, jamais un effet automatique de l'habilitation. La coexistence avec les champs régional ou local de L. 2232-5 constitue une difficulté d'articulation préexistante, signalée sans correction silencieuse. L. 2261-32 I, 3°, et les garanties de branche ne sont pas abrogés par cette rédaction.")


assert len(sources) == 24
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'{len(answer)} articles écrits dans answer.json')
