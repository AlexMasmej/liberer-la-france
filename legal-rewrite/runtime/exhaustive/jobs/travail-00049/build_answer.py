import json
import re
from html import unescape
from html.parser import HTMLParser


sources = json.load(open('source.json', encoding='utf-8'))
by_number = {s['number']: s for s in sources}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml or ''))


def base(number):
    source = by_number[number]
    return {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


def retain(number, reason, notes, assessment, limitations, burdens):
    a = base(number)
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary')
    a['substantive_impact'] = {
        'version': 1, 'classification': 'retained_necessary',
        'assessment': assessment, 'scope_limitations': limitations,
        'new_burdens_review': burdens, 'effects': []}
    answers[number] = a


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


retain('L2262-1',
       "Maintien intégral après examen : la force obligatoire des conventions pour leurs signataires et les membres des organisations signataires garantit les engagements librement souscrits et les droits conventionnels des salariés. Ce n'est ni un agrément, ni une déclaration, ni une contribution accessoire retirable. Aucune reformulation à droit constant n'est produite.",
       "La réserve relative à l'extension et à l'élargissement reste entière. Lecture croisée de L2262-2 à L2262-4 et des actions L2262-9 à L2262-12 : aucune de ces règles ne remplace la détermination des personnes liées. Ce maintien ne rétablit pas la liste annuelle supprimée de L2262-6 ni une transmission CPPNI. Les stipulations incompatibles avec une disposition impérative de la réforme restent soumises à cette disposition et à sa transition, sans réécriture implicite des contrats antérieurs.",
       "Aucun allègement nouveau : l'obligation d'appliquer les engagements conventionnels est maintenue pour protéger leur effectivité, y compris les avantages futurs ouverts par ces engagements.",
       "La validité de chaque stipulation et les effets propres des arrêtés d'extension ne sont pas audités par cet article ; aucun gain global de coût n'est établi.",
       "Aucune charge nouvelle identifiée : le maintien n'ajoute ni dépôt, ni registre, ni condition d'adhésion aux obligations conventionnelles existantes.")

retain('L2262-2',
       "Maintien intégral : rattacher l'adhésion à l'organisation signataire à la convention évite une seconde adhésion de même objet. La réserve de L2261-3 empêche une extension irrégulière du champ conventionnel. Aucun doublon déclaratif supplémentaire n'est créé par cet article et aucun changement stylistique n'est utile.",
       "L2261-3, L2261-5 et L2261-6 ont été lus intégralement : organisations syndicales représentatives de salariés, organisations ou associations d'employeurs et employeurs individuels ; adhésion hors champ soumise à l'accord collectif ou à l'agrément syndical applicable. La source de L2261-3 exige notification et dépôt ; sa proposition déjà présente dans le corpus retire le dépôt administratif distinct pour les adhésions nouvelles tout en conservant notification et règles de champ. Le renvoi conservé ici s'applique à L2261-3 ainsi coordonné et ne rétablit pas le dépôt supprimé. Aucun nouvel allègement n'est compté dans L2262-2.",
       "L'effet juridique de l'adhésion demeure inchangé ; l'absence de seconde adhésion autonome à la convention est déjà contenue dans la source et n'est pas comptée comme une fusion nouvelle.",
       "Les procédures de L2261-5 et L2261-6 ne sont pas réécrites dans ce lot ; le maintien ne démontre aucune suppression de leurs formalités.",
       "Aucune charge nouvelle identifiée : mêmes personnes liées, même réserve d'adhésion et aucune attestation ou validation de remplacement.")

retain('L2262-3',
       "Maintien intégral de la persistance des engagements après la démission patronale de l'organisation signataire. La supprimer permettrait de faire disparaître des droits conventionnels par une simple sortie de l'organisation ; ce n'est pas un doublon administratif. L'examen ne révèle ni prélèvement ni justificatif à retirer.",
       "Distinguer la démission de l'organisation et la dénonciation régulière de l'accord. L2262-7, lu dans le corpus, traite seulement l'information immédiate de cette démission ; sa coordination prévue dans travail doit conserver des destinataires explicites après suppression de L2262-6. Le maintien du lien conventionnel n'exige aucun nouvel état annuel.",
       "Aucune réduction revendiquée : maintien de la protection contre la sortie unilatérale des obligations conventionnelles par démission de l'organisation.",
       "Les procédures et effets d'une véritable dénonciation d'accord restent hors de cet article ; aucune durée nouvelle de survie n'est instituée.",
       "Aucune charge nouvelle identifiée : seule subsiste la force des engagements déjà applicables, sans notification ni contrôle supplémentaires dans cet article.")

retain('L2262-4',
       "Maintien intégral : l'exécution loyale est une garantie réciproque des conventions. La seconde phrase limite la garantie des organisations à ce que prévoit le texte négocié ; ce tempérament favorable ne doit pas disparaître. L'article n'impose ni rapport, ni document, ni contrôle préalable à supprimer.",
       "Conserver tous les sujets : organisations de salariés, organisations ou groupements d'employeurs et employeurs individuels liés. L2262-11 et L2262-12 conservent les actions en exécution et réparation ; ils ne transforment pas la garantie limitée ici en responsabilité générale de résultat.",
       "Aucun changement matériel : maintien de la loyauté et de la limitation conventionnelle de garantie, utiles à l'équilibre des engagements collectifs.",
       "Les clauses de responsabilité de chaque accord ne sont pas examinées individuellement ; aucune baisse chiffrée de contentieux ou de coût n'est démontrée.",
       "Aucune charge nouvelle identifiée : pas de garantie illimitée, de registre d'exécution ou de compte rendu périodique ajouté.")

retain('L2262-8',
       "Maintien intégral : la communication et la copie des accords déposés assurent l'accès au droit applicable. Cette faculté d'accès ne se confond ni avec le dépôt, ni avec une double transmission imposée aux entreprises. Aucune autorisation nouvelle n'est instaurée et aucune reformulation n'est nécessaire.",
       "Le décret en Conseil d'Etat reste habilité à définir les conditions de communication ; cet article ne fixe ni délai minimal d'attente, ni tarif, ni obligation de créer une plateforme. L2231-5-1 a été lu : publicité nationale, anonymisation, occultations et exclusions de publication demeurent distinctes de l'accès légal aux textes. La dispense proposée ailleurs de seconde version publiable n'est pas remise en cause.",
       "Aucun gain nouveau : conservation du fondement d'accès aux textes conventionnels déposés, nécessaire à leur connaissance et aux recours.",
       "Le régime réglementaire de délivrance des copies n'est pas modifié ici ; aucune gratuité nouvelle ou suppression de frais n'est démontrée.",
       "Aucune charge nouvelle identifiée : pas de dépôt supplémentaire ni de nouvelle pièce exigée du déposant pour exercer ce droit d'accès existant.")

retain('L2262-9',
       "Maintien intégral de l'action des organisations en faveur de leurs membres sans mandat. L'avertissement et l'absence d'opposition protègent la liberté du membre ; son intervention à l'instance reste ouverte. Exiger moins de garanties porterait atteinte au consentement ; supprimer l'action réduirait l'accès au juge.",
       "Les deux alinéas restent applicables, aux organisations ou groupements ayant capacité d'agir et dont les membres sont liés. Aucun écrit de mandat ni délai nouveau n'est requis. Distinguer cette action pour les membres des actions propres et interventions de L2262-10 à L2262-12. Le préavis individuel de quinze jours ne concerne pas cette procédure.",
       "La dispense de mandat est déjà acquise dans la source ; elle reste disponible pour les litiges futurs et n'est pas présentée comme un allègement nouveau.",
       "Les règles procédurales de notification de l'avertissement et de recevabilité hors de cet article restent applicables ; aucun nouveau délai de recours n'est proposé.",
       "Aucune charge nouvelle identifiée : avertissement, droit d'opposition et intervention personnelle restent exactement ceux de la source, sans mandat ajouté.")

retain('L2262-10',
       "Maintien intégral du droit d'intervention des organisations en raison de l'intérêt collectif du litige. La capacité d'agir et le lien de leurs membres avec la convention délimitent ce droit sans agrément administratif. L'action initiale et l'intervention ne sont pas des doublons de déclaration à fusionner.",
       "Conserver la faculté d'intervenir lorsque l'action initiale émane d'une personne comme d'une organisation ou d'un groupement. L'intérêt collectif reste exigé ; aucune preuve de mandat individuel n'est ajoutée. L2262-9 et L2262-11 répondent à des objets distincts et sont maintenus.",
       "Aucune simplification nouvelle revendiquée : l'intervention protège la représentation de l'intérêt collectif sans supprimer l'action individuelle.",
       "Les conditions générales de l'intervention devant chaque juridiction ne sont pas réécrites ; aucune économie de procédure n'est mesurée.",
       "Aucune charge nouvelle identifiée : la faculté d'intervenir reste optionnelle et n'est assortie d'aucune déclaration, adhésion ou autorisation supplémentaire.")

retain('L2262-11',
       "Maintien intégral : l'action en nom propre permet l'exécution des engagements et la réparation de leur violation. Le champ des défendeurs, incluant les propres membres de l'organisation, est utile à l'effectivité de la convention. Aucun circuit administratif ni prélèvement accessoire n'est imposé par le texte.",
       "Maintenir capacité d'agir, lien conventionnel, exécution et dommages-intérêts éventuels contre les autres organisations ou groupements, les propres membres et toute personne liée. L2262-4 limite toujours la garantie à ce que détermine la convention. Le régime de rupture individuelle ne plafonne pas ces réparations conventionnelles.",
       "Aucun changement normatif : le recours contractuel propre des organisations est conservé, distinct des actions en faveur des membres et des actions individuelles.",
       "Aucune responsabilité automatique ni montant de réparation n'est ajouté ; le fond de chaque demande reste soumis au juge et aux autres règles applicables.",
       "Aucune charge nouvelle identifiée : pas de conciliation administrative, d'agrément ou de justificatif préalable ajouté à l'action existante.")

retain('L2262-12',
       "Maintien intégral du droit de toute personne liée d'obtenir l'exécution et, le cas échéant, des dommages-intérêts pour les engagements violés à son égard. Ce recours individuel demeure nécessaire même lorsque l'organisation peut agir. Le supprimer comme doublon affaiblirait l'accès au juge.",
       "Conserver le caractère éventuel des dommages-intérêts et le lien des défendeurs à la convention ou à l'accord. L2262-9 n'écarte ni cette action ni l'intervention personnelle. Aucune indemnité ordinaire de rupture du contrat unique ne se substitue à la réparation de l'inexécution ou d'une illégalité.",
       "Aucune réduction nouvelle : maintien du recours individuel permettant de rendre effectifs les salaires et autres avantages conventionnels.",
       "Les prescriptions et les compétences juridictionnelles particulières ne sont pas modifiées ; aucun montant de réparation n'est présumé.",
       "Aucune charge nouvelle identifiée : absence de nouveau mandat, registre, rapport ou voie préalable obligatoire pour obtenir l'exécution des engagements.")

retain('L2262-13',
       "Maintien intégral de la charge de démontrer l'illégalité pour celui qui la conteste. Cette règle ordonne le débat judiciaire et sécurise les accords ; elle n'exige aucun dossier annuel de conformité. L'abroger sans régime probatoire précis déplacerait la preuve sans allègement établi et pourrait fragiliser les droits négociés.",
       "Ne pas lire la règle comme une interdiction de recours ou une dispense de respecter les conditions légales de validité. Elle n'écarte pas les règles probatoires spéciales applicables à des objets distincts, notamment la discrimination. L2262-14 reste relatif à l'action en nullité, non à la définition de toute preuve dans tout contentieux du travail.",
       "Aucun changement réel revendiqué : le principe probatoire existant demeure, sans créer de certification préventive à la charge des signataires.",
       "Les aménagements de preuve issus d'autres dispositions et leur application jurisprudentielle ne sont pas épuisés par cette lecture du corpus.",
       "Aucune charge nouvelle identifiée : ni dossier de conformité permanent, ni attestation, ni procédure préalable de contestation n'est créé.")

retain('L2262-14',
       "Maintien intégral : le délai d'action en nullité de deux mois assure la stabilité des accords sans être un délai minimal avant de saisir le juge. Les deux points de départ et les régimes contentieux réservés évitent une prescription indifférenciée. Les notes historiques et la réserve constitutionnelle ont été lues ; aucune réécriture stylistique n'est utile.",
       "L2231-5 et L2231-5-1 ont été lus : notification aux organisations concernées et publication sont distinctes. La réserve du paragraphe 35 de la décision 2018-761 DC impose, pour les parties non publiées, une connaissance valable avant le départ du délai à l'encontre des autres personnes ; le maintien ne neutralise pas cette réserve. La note de l'ordonnance 2017-1385, article 15, protège les instances antérieures, y compris appel et cassation, et règle les accords anciens sans instance. L1233-24, L1235-7-1 et L1237-19-8 ont été lus intégralement : leurs objets, délais spéciaux et compétences restent réservés. Ni la dispense de seconde version publiable ni le préavis individuel ne déclenchent à eux seuls ce délai.",
       "Aucun délai nouveau ni réduction revendiquée : maintien du délai de nullité avec ses garanties de connaissance du texte et ses exceptions contentieuses.",
       "L'action en exécution et les moyens d'inopposabilité ne sont pas assimilés ici à l'action en nullité ; leur régime propre n'est pas réécrit. Aucune date future n'est tirée des notes de 2017 ou 2018.",
       "Aucune charge nouvelle identifiée : mêmes notifications, publication et points de départ, sans attestation de connaissance ou nouveau dépôt ajouté.")

retain('L2262-14-1',
       "Maintien intégral du délai de six mois donné au juge pour statuer sur l'action en nullité. Il s'agit d'une garantie de célérité pour tous les intéressés, non d'une attente minimale imposée avant le jugement. Sa suppression ne démontrerait aucun allègement utile pour les parties.",
       "Le renvoi à L2262-14 demeure cohérent et vise son action en nullité. Ne pas convertir les six mois en extinction de l'instance, rejet tacite ou délai de recours. L'article ne fixe pas de sanction automatique en cas de dépassement ; aucune n'est inventée.",
       "Aucun changement : les six mois demeurent une exigence de célérité juridictionnelle, sans réduction du droit au recours ni nouvelle formalité des parties.",
       "Les moyens des juridictions et les effets procéduraux d'un dépassement ne sont pas évalués ; aucune économie ni durée effective de jugement n'est chiffrée.",
       "Aucune charge nouvelle identifiée : le maintien n'ajoute aux parties ni relance obligatoire, ni requête distincte, ni pièce justificative.")

retain('L2262-15',
       "Maintien intégral de la faculté judiciaire de moduler les effets de l'annulation. Les conséquences manifestement excessives, l'intérêt général et la protection des actions déjà engagées encadrent cette souplesse favorable à la sécurité des situations constituées. Aucun visa ou rapport administratif n'est à retirer.",
       "Conserver les deux branches de modulation : effet pour l'avenir ou modulation dans le temps, ainsi que tous les critères et la réserve des actions engagées à la date de décision sur le même fondement. Cette faculté ne valide pas un accord illégal et n'efface pas automatiquement les créances des salariés.",
       "Aucun gain nouveau : la modulation protectrice des situations et des recours déjà engagés reste entièrement disponible au juge.",
       "L'application aux circonstances de chaque annulation demeure juridictionnelle ; aucun maintien automatique d'effets ni durée nouvelle n'est fixé.",
       "Aucune charge nouvelle identifiée : pas de demande administrative ni de procédure de régularisation obligatoire ajoutée pour bénéficier de la modulation.")

retain('L2263-1',
       "Maintien intégral : lorsque la loi autorise une dérogation par accord étendu dans une matière déterminée, le respect des stipulations de substitution demeure sanctionné comme celui de la loi remplacée. La règle sécurise la faculté de dérogation sans en faire un moyen d'impunité. Il n'y a ni amende autonome chiffrée, ni prélèvement accessoire, ni déclaration supprimable dans cet article.",
       "Conditions cumulatives préservées : disposition législative expresse, matière déterminée, convention ou accord étendu et véritable dérogation aux règles légales. Aucun régime pénal n'est étendu aux simples accords non étendus ni à toutes les clauses d'un accord. L'extension reste un mécanisme distinct dont les avis relèvent du 3° de L2271-1, maintenu. Les dérogations ouvertes aux situations futures demeurent possibles selon leur loi d'habilitation.",
       "Aucune réduction de sanction ni taxe supprimée : maintien du mécanisme de substitution pénale qui accompagne les dérogations légales autorisées.",
       "Les sanctions concrètes et les lois autorisant chaque dérogation dépendent des matières concernées ; aucun inventaire exhaustif de ces infractions n'est revendiqué.",
       "Aucune charge nouvelle identifiée : mêmes conditions de déclenchement et mêmes sanctions de référence, sans nouvelle infraction ni justification préalable.")
answers['L2263-1']['benefit_review'] = (
    "L'avantage possible est la faculté de déroger, par convention ou accord collectif étendu, à une disposition légale lorsque la loi l'autorise expressément dans une matière déterminée. Cette faculté demeure intégralement ouverte, y compris aux futurs accords et aux futures situations éligibles. Le présent article n'institue ni exonération fiscale, ni dispense de sanction : il applique aux stipulations dérogatoires les sanctions de la règle légale correspondante. Le maintien de cette équivalence ne retire aucun allègement autorisé et n'ajoute aucune condition à la dérogation.")

retain('L2272-1',
       "Maintien intégral de la représentation de l'Etat, du Conseil d'Etat et des partenaires sociaux, et des compositions élargies adaptées aux objets de consultation. Cette participation n'est pas un agrément d'entreprise ni un doublon de déclaration. La suppression ciblée des examens annuels de L2271-1 n'exige pas de retirer les représentants des consultations maintenues.",
       "Trois alinéas conservés. Le renvoi au 10° de L2271-1 reste exact : assurance chômage et plans de formation ; l'abrogation du seul 7° ne le décale pas. R2272-1 a été lu pour les formations spécialisées et leurs compositions. La note historique de l'article 148 II de la loi 2020-1525 explique le 1er juin 2021 ; elle n'est pas une transition de la présente réforme.",
       "Aucun allègement nouveau : les formations de représentation sont conservées pour les missions substantielles qui restent à la commission.",
       "Les nominations et moyens de fonctionnement ne sont pas réorganisés ; aucune économie de siège ou de réunion ne peut être attribuée à cet article maintenu.",
       "Aucune charge nouvelle identifiée : mêmes collèges et mêmes cas d'élargissement, sans expert, registre ou représentant obligatoire supplémentaire.")

retain('L2272-2',
       "Maintien intégral de l'habilitation au décret en Conseil d'Etat pour organiser la commission. Elle assure un cadre de fonctionnement commun pour les consultations maintenues ; elle n'impose par elle-même ni autorisation, ni périodicité, ni déclaration aux entreprises. Sa suppression créerait une lacune de compétence sans réduction démontrée.",
       "Le pouvoir réglementaire demeure subordonné à L2271-1 révisé : il ne peut rétablir sur ce seul fondement les examens annuels supprimés. R2271-1 et le dernier alinéa de R2272-13, lus intégralement, sont les cibles précises à coordonner ; ils ne sont pas réécrits dans ce lot. Les missions et sous-commissions utiles de R2272-10 demeurent distinctes.",
       "Aucun gain propre : l'habilitation réglementaire demeure nécessaire, sans être comptée comme une seconde simplification des missions annuelles.",
       "La coordination réglementaire de R2271-1 et R2272-13 reste nécessaire ; conserver l'habilitation ne signifie pas que ces dispositions ont déjà été réécrites.",
       "Aucune charge nouvelle identifiée : aucun décret supplémentaire déterminé ni circuit d'approbation nouveau n'est exigé par ce maintien.")

retain('L2281-1',
       "Maintien intégral du droit d'expression directe et collective sur le contenu, les conditions et l'organisation du travail. Le recours au numérique est une faculté existante et reste encadré par les droits et obligations des salariés. Il n'y a ni plateforme imposée ni déclaration à abolir.",
       "Les deux alinéas restent entiers. Les suppressions de périodicité dans L2281-6 et de délais d'attente dans L2281-7 concernent la négociation des modalités ; elles n'abolissent pas le droit lui-même. L2281-3 et L2281-4 conservent la protection contre les sanctions et la rémunération du temps consacré.",
       "Aucun changement réel : protection du droit collectif et maintien de la faculté numérique, déjà prévue dans la source et non comptée comme un nouveau gain.",
       "Les règles de protection des données et les modalités conventionnelles des outils restent à leur champ propre ; aucun coût numérique évité n'est établi.",
       "Aucune charge nouvelle identifiée : ni équipement, ni compte, ni abonnement, ni registre d'expression n'est rendu obligatoire.")

retain('L2281-2',
       "Maintien intégral de l'objet du droit d'expression : améliorer les conditions de travail, l'organisation de l'activité et la qualité de la production. Cet objet délimite une liberté existante et n'impose pas de plan d'action, de résultat chiffré ou de rapport. Il n'y a aucune charge autonome à supprimer dans cette phrase.",
       "Conserver les deux échelles, unité de travail et entreprise, ainsi que les trois finalités cumulativement mentionnées. L2281-1 définit le droit et L2281-5 ses modalités négociées ; aucune de ces fonctions n'est remplacée par le présent article.",
       "Aucune réduction nouvelle : la définition de l'objet du droit demeure nécessaire à son exercice et à la délimitation de sa protection.",
       "L'article n'établit pas à lui seul les modalités de réunion ou de suivi ; aucune obligation d'amélioration mesurable ni économie n'en est déduite.",
       "Aucune charge nouvelle identifiée : maintien d'une finalité juridique sans nouvelle procédure, nouvelle donnée à collecter ou nouveau compte rendu.")

retain('L2281-3',
       "Maintien intégral de l'interdiction de sanctionner ou licencier un salarié pour les opinions émises dans l'exercice du droit d'expression. La protection de toutes les places dans la hiérarchie est essentielle à l'effectivité de cette liberté. Aucun formalisme redondant ni prélèvement n'est présent.",
       "Le contrat unique, l'essai et le préavis individuel de quinze jours ne neutralisent pas cette protection. Les réparations d'une rupture illégale demeurent distinctes de l'indemnité ordinaire, même avant un an d'ancienneté. Le texte protège les opinions dans l'exercice du droit ; aucune immunité générale pour tout comportement étranger à cet exercice n'est ajoutée.",
       "Aucun gain nouveau : maintien de la protection contre les représailles, pour les salariés présents comme pour les futurs salariés éligibles.",
       "Les règles de nullité et de réparation des sanctions ou ruptures restent dans leurs textes propres ; aucun montant ni barème de dommage n'est créé.",
       "Aucune charge nouvelle identifiée : pas de déclaration préalable d'opinion ni de procédure d'autorisation pour bénéficier de la protection existante.")

retain('L2281-4',
       "Maintien intégral : exercice sur les lieux et pendant le temps de travail, avec rémunération de ce temps comme travail. Supprimer ces garanties déplacerait le coût sur les salariés et réduirait un droit essentiel ; ce ne serait pas une économie démontrée de prélèvements. Aucun justificatif spécifique n'est exigé par cet article.",
       "Les deux alinéas sont conservés, sans plafond nouveau ni exclusion des outils numériques autorisés par L2281-1. La suppression de la réunion patronale triennale de L2281-6 ne concerne pas les réunions d'expression elles-mêmes ni les temps déjà accomplis. L2281-10 et le régime distinct L2282-2 ne sont pas abrogés.",
       "Aucun allègement revendiqué : maintien du salaire et de l'accessibilité matérielle du droit, sans transfert de son exercice sur le temps personnel.",
       "Les modalités concrètes de durée restent conventionnelles ou régies par leurs textes particuliers ; aucune baisse de masse salariale n'est imputée à ce maintien.",
       "Aucune charge nouvelle identifiée : la rémunération est celle déjà due et aucun suivi distinct du temps, attestation ou équipement supplémentaire n'est créé.")

retain('L2281-5',
       "Maintien intégral de l'intégration des modalités d'expression à la négociation sur l'égalité professionnelle et la qualité de vie et des conditions de travail. Cette intégration évite déjà un thème autonome imposé hors du cadre collectif ; elle garantit en même temps que le droit puisse être exercé. Aucune fusion supplémentaire n'est inventée.",
       "L2242-1 a été lu : cadre des négociations et périodicité maximale de quatre ans dans son champ. L2242-17, 6°, confirme le thème d'expression dans la négociation supplétive annuelle ; L2242-11 et L2281-10 ont aussi été lus. La suppression de la seule réunion triennale L2281-6 ne supprime pas ces négociations ni les règles de majorité. Note historique de la loi 2021-1018, article 40 I/II : entrée au 31 mars 2022 et conditions propres à cette réforme, aucune nouvelle date de promulgation déduite.",
       "Aucun gain nouveau : la négociation intégrée demeure celle de la source, avec son objet et le même renvoi à L2242-1.",
       "Les échéances autonomes des négociations obligatoires et les engagements conventionnels demeurent ; aucune suppression générale des réunions de dialogue social n'est démontrée.",
       "Aucune charge nouvelle identifiée : aucun thème supplémentaire, second accord obligatoire, registre ou transmission supplémentaire n'est institué.")


# Nouveau corps complet : seules les trois obligations identifiées sont retirées.
s = by_number['L2271-1']['source_xml']
old7 = "<p>7° D'examiner le bilan annuel de la négociation collective ; </p>"
assert old7 in s
p = s.replace(old7, '<p>7° Abrogé ; </p>')
assert p.count('De suivre annuellement') == 2
p = p.replace('De suivre annuellement', 'De suivre')
p += ("<p>La suppression de l'examen obligatoire du bilan annuel au 7° et de la périodicité annuelle des suivis aux 8° et 9° s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux examens et travaux préparatoires non encore accomplis à cette date. Aucun examen annuel, bilan distinct ou rapport préparatoire ne peut être exigé sur le seul fondement des obligations ainsi supprimées. Les suivis prévus aux 8° et 9° demeurent obligatoires, sans périodicité annuelle imposée par le présent article. Les rapports et examens déjà réalisés conservent leurs effets ; ils n'ont pas à être renouvelés. Le rapport du groupe d'experts et l'avis prévus au 5° demeurent soumis à leurs règles propres.</p>")
a = base('L2271-1')
a.update(
    proposed_xml=p, status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "L'examen obligatoire par la commission du bilan annuel de la négociation collective, prévu au 7°, et les travaux préparatoires exclusivement fondés sur cet examen.",
        "La périodicité annuelle imposée au suivi des principes d'égalité et des mesures favorisant le droit au travail des personnes handicapées, sans suppression de cette mission de suivi.",
        "La périodicité annuelle imposée au suivi du taux d'activité des personnes de plus de cinquante ans, sans suppression des propositions en faveur de leur emploi."],
    reason="Réforme de fond ciblée : suppression de l'examen obligatoire distinct du bilan annuel au 7° et des deux cadences annuelles aux 8° et 9°. La commission conserve toutes ses autres missions, ainsi que le suivi substantiel de l'égalité, du handicap et de l'emploi des plus de cinquante ans. Ces fonctions peuvent être exercées sans imposer chaque année ces trois opérations. Les consultations sur les projets de textes, l'extension, les interprétations, le SMIC, l'assurance chômage et la formation ne sont pas supprimées. Aucun changement stylistique n'est apporté aux dispositions maintenues.",
    review_notes="Le 7° garde son emplacement abrogé ; les 8°, 9° et 10°, les lettres a), b), c), les renvois L3231-6, L3231-10, L5422-20 et L6122-1 et le seuil d'au moins la moitié au 4° sont conservés. R2271-1, lu en entier, rattache un bilan d'égalité à l'examen annuel du 8° : coordonner son calendrier sans supprimer le suivi des écarts. Le dernier alinéa de R2272-13, lu en entier, impose un comité et un rapport pour le bilan annuel du 7° : retirer cette obligation devenue sans objet ; les nominations et autres règles restent autonomes. L2, L2272-1 et R2272-10 ont été lus : leurs consultations, compositions et compétences ne sont pas abolies. La transition écarte les travaux non accomplis exclusivement fondés sur les obligations retirées, pas les droits acquis, les contrôles d'égalité ni les obligations européennes ou internationales autonomes. Le rapport annuel des experts du SMIC au 5° est expressément conservé ; ne pas annoncer la disparition de tout rapport national. Les textes réglementaires signalés ne sont pas déclarés réécrits. La date du 1er janvier 2024 des notes source est historique. Aucun rendement budgétaire ni solde net national n'est établi.")
a['substantive_impact'] = dict(
    version=1, classification='material_reduction',
    assessment="La comparaison avec toute la source démontre le retrait d'un examen annuel obligatoire et de deux cadences annuelles, sans retirer les missions substantielles des 8° et 9°. Ce ne sont ni trois taxes supprimées ni la suppression générale des rapports sociaux. L'allègement porte sur les opérations institutionnelles obligatoires ; son coût net n'est pas chiffré.",
    scope_limitations="L'effet vise la commission et ses préparations exclusivement liées aux obligations retirées. R2271-1 et le dernier alinéa de R2272-13 restent à coordonner matériellement. Les rapports du SMIC, les négociations obligatoires, les statistiques et contrôles ayant un fondement autonome restent hors de la suppression ; aucune baisse globale de complexité n'est démontrée.",
    new_burdens_review="Aucune charge nouvelle identifiée : pas de rapport regroupé, de collecte, de registre, de déclaration ni de nouvelle échéance en remplacement. Le suivi de l'égalité et de l'emploi des seniors demeure une mission déjà existante. La réserve expresse du rapport des experts du SMIC n'ajoute rien à la source.",
    effects=[
        effect('obligation_removed', 'cnnc-examens-annuels-allegement',
               "Mesure unique regroupant le retrait de l'examen obligatoire du bilan annuel au 7° et des cadences annuelles des suivis aux 8° et 9° ; les trois retraits restent détaillés dans removed_provisions.",
               "La commission examine obligatoirement le bilan annuel de la négociation collective, suit annuellement les principes d'égalité et les mesures en faveur du travail des personnes handicapées, et suit annuellement le taux d'activité des personnes de plus de cinquante ans. Aucun taux ni assiette fiscale n'est en cause.",
               "Le 7° est abrogé ; les suivis et propositions des 8° et 9° restent obligatoires avec leurs champs complets, sans cadence annuelle imposée. Les examens et préparations non accomplis exclusivement fondés sur les obligations supprimées ne sont plus exigibles ; le rapport des experts du SMIC et les obligations autonomes demeurent.",
               'legal_duty', "Commission nationale et services préparant ces travaux ; suivi de l'égalité, du handicap et de l'emploi des personnes de plus de cinquante ans maintenu.",
               "Dès l'entrée en vigueur de la loi pour les examens et travaux non encore accomplis ; rapports et examens réalisés, droits acquis et obligations autonomes préservés. R2271-1 et le dernier alinéa de R2272-13 restent à coordonner.",
               "Aucun examen périodique, rapport, dépôt, collecte ou fréquence de remplacement ajouté ; aucun retrait de protection individuelle ou collective. Le coût net de cet allègement institutionnel n'est pas chiffré.",
               "7° D'examiner le bilan annuel de la négociation collective ;",
               "Aucun examen annuel, bilan distinct ou rapport préparatoire ne peut être exigé sur le seul fondement des obligations ainsi supprimées.")])
answers[a['number']] = a


p6 = (
    "<p>Lorsqu'un accord sur le droit d'expression existe, l'employeur engage sa renégociation à la demande d'une organisation syndicale représentative. Aucune réunion périodique distincte destinée à examiner les résultats de cet accord n'est imposée par le présent article.</p>"
    "<p>La suppression de la réunion obligatoire au moins une fois tous les trois ans s'applique, à compter de l'entrée en vigueur de la loi portant la présente réforme, aux réunions non encore tenues à cette date. Elle ne remet en cause ni les salaires et autres droits acquis au titre des réunions déjà tenues, ni les engagements conventionnels autonomes. Le droit d'expression, la rémunération du temps consacré à son exercice et les négociations prévues à l'article L. 2281-5 demeurent applicables. Les demandes de négociation et de renégociation sont régies par l'article L. 2281-7.</p>")
a = base('L2281-6')
a.update(
    proposed_xml=p6, status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=["L'obligation pour l'employeur de provoquer au moins tous les trois ans une réunion distincte avec les organisations syndicales représentatives pour examiner les résultats de l'accord sur le droit d'expression."],
    reason="Réforme de fond : retrait de la réunion automatique triennale distincte d'examen d'un accord sur le droit d'expression. L2281-5 rattache déjà les modalités de ce droit à la négociation sur l'égalité et les conditions de travail ; une réunion séparée imposée par calendrier n'est pas nécessaire pour conserver cette négociation. Le droit des organisations représentatives de demander la renégociation demeure. Le texte ne supprime ni les réunions où les salariés exercent leur droit, ni leur rémunération, ni les engagements conventionnels autonomes.",
    review_notes="Coordination complète avec le nouveau L2281-7 : réponse dans les quinze jours et transmission aux autres organisations dans les huit jours conservées ; la suppression des délais d'attente légaux est analysée dans cet autre article, sans la compter ici une seconde fois. L2281-5, L2242-1, L2242-11 et L2242-17, 6°, lus en entier, gardent leurs calendriers propres ; la seule réunion triennale d'examen est retirée. L2281-10 et L2282-2, lus, demeurent distincts : contenu des accords et réunions d'atelier du secteur public ne sont pas supprimés. Source L2281-6/L2281-7 : le droit de renégociation à la demande n'était pas expressément soumis à un an dans L2281-6, tandis que L2281-7 mentionnait un an en cas d'accord ; cette articulation préexistante est rendue explicite, sans présenter toute demande avant un an comme un droit nouveau. Réunions déjà tenues, créances salariales et engagements autonomes préservés ; aucun rapport de remplacement n'est créé. Aucun préavis individuel de rupture n'est modifié.")
a['substantive_impact'] = dict(
    version=1, classification='material_reduction',
    assessment="L'obligation automatique d'initiative patronale pour une réunion distincte au moins tous les trois ans disparaît réellement par rapport à la source entière. La négociation sur demande et la négociation intégrée restent. L'économie de réunions dépend des demandes et des obligations conventionnelles ; aucun solde financier global n'est démontré.",
    scope_limitations="Sont seuls visés les accords existants sur le droit d'expression et leur réunion légale d'examen non encore tenue. Les réunions d'expression, les accords autonomes, la négociation égalité et les règles spéciales du secteur public demeurent ; l'ouverture de la demande sans attente est évaluée dans L2281-7.",
    new_burdens_review="Aucune charge nouvelle propre à cet article : la renégociation demandée par une organisation était déjà obligatoire et aucun bilan, registre, formulaire ou réunion de substitution n'est ajouté. L'extension des demandes avant trois ans en l'absence d'accord est expressément recensée dans L2281-7, sans présumer le solde des deux articles.",
    effects=[effect('obligation_removed', 'expression-salaries-reexamen-sur-demande',
                    "Suppression de l'initiative patronale automatique pour le réexamen triennal distinct de l'accord.",
                    "Lorsqu'un accord existe, réunion provoquée par l'employeur au moins tous les trois ans avec les organisations représentatives, plus renégociation sur demande.",
                    "Pas de réunion périodique distincte imposée par cet article ; renégociation sur demande et négociations autonomes maintenues.",
                    'legal_duty', "Employeurs et organisations syndicales représentatives dans les entreprises couvertes par un accord sur le droit d'expression.",
                    "Réunions non tenues à l'entrée en vigueur ; salaires, droits acquis et engagements conventionnels autonomes maintenus.",
                    "Aucun rapport ou réunion de remplacement ; voir séparément l'élargissement des demandes prévu à L2281-7.",
                    "l'employeur provoque une réunion, au moins une fois tous les trois ans, avec les organisations syndicales représentatives en vue d'examiner les résultats de cet accord",
                    "Aucune réunion périodique distincte destinée à examiner les résultats de cet accord n'est imposée par le présent article.")])
answers[a['number']] = a


p7 = (
    "<p>A la demande d'une organisation syndicale représentative, la négociation sur les modalités d'exercice du droit d'expression ou la renégociation de l'accord existant s'engage obligatoirement dans les quinze jours suivant la présentation de cette demande.</p>"
    "<p>Cette demande est transmise aux autres organisations syndicales représentatives par l'employeur dans les huit jours.</p>"
    "<p>L'exercice de ce droit n'est subordonné ni à l'absence d'initiative de l'employeur, ni à l'écoulement d'un délai d'un an ou de trois ans depuis l'ouverture de la négociation précédente. Une demande portant sur une négociation de même objet déjà en cours ne contraint pas à ouvrir une seconde procédure parallèle ; les droits de participation de toutes les organisations syndicales représentatives à la négociation en cours demeurent applicables.</p>"
    "<p>Ces dispositions s'appliquent aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente réforme. Les demandes antérieures recevables conservent leurs effets et les délais déjà commencés ne sont pas recommencés ; aucune nouvelle demande n'est exigée. Les accords valablement conclus, les droits acquis et les obligations de négociation ayant un fondement autonome demeurent applicables.</p>")
a = base('L2281-7')
a.update(
    proposed_xml=p7, status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "La condition d'absence d'initiative patronale pendant un an en présence d'un accord ou trois ans en l'absence d'accord avant de rendre obligatoire l'ouverture de la négociation sur demande syndicale.",
        "Le point de départ à l'ouverture de la négociation précédente pour les délais d'attente d'un an ou de trois ans ainsi retirés."],
    reason="Réforme de fond et coordination : après suppression de la réunion patronale triennale distincte dans L2281-6, la demande syndicale peut déclencher la négociation sans attendre l'absence d'initiative pendant un ou trois ans. Les délais protecteurs de quinze jours pour l'ouverture et de huit jours pour informer les autres organisations sont intégralement conservés. Une négociation de même objet déjà en cours ne doit pas être dupliquée, sans exclure aucun participant habilité. Cette ouverture allège l'attente syndicale mais étend la disponibilité obligatoire de l'employeur, notamment avant trois ans lorsqu'aucun accord n'existe : l'impact est mixte et non une baisse nette de contraintes démontrée.",
    review_notes="L2281-6 source permettait déjà la renégociation à la demande en présence d'un accord, sans délai minimal explicite, alors que L2281-7 mentionnait un an en cas d'accord et trois ans sans accord. Cette articulation préexistante est signalée ; le gain nouveau certain porte surtout sur l'absence d'accord et les trois ans. Aucun de ces délais n'est un préavis de rupture. Les délais de quinze jours et huit jours sont inchangés et ne deviennent pas calendaires par assimilation au préavis individuel ; leurs règles ordinaires de computation demeurent. L2281-5, L2242-1, L2242-11, L2242-17, L2281-8 à L2281-10 et L2232-16 ont été lus : cadre de négociation, participants et dépôt restent autonomes. L2283-1, lu intégralement, sanctionne le refus d'engager la négociation prévue à L2281-5 ; l'ouverture anticipée doit être coordonnée avec son champ pénal selon les principes de légalité et d'application dans le temps, sans prétendre cet article pénal réécrit ni créer une sanction nouvelle ici. La transition ne rouvre pas automatiquement des demandes anciennes irrecevables. Aucune obligation de conclure un accord, de transmettre à la CPPNI, de voter sans garanties, ou de déposer un rapport nouveau n'est instituée. Le solde de charge dépend de l'usage du droit de demande et reste inconnu.")
a['substantive_impact'] = dict(
    version=1, classification='mixed',
    assessment="La source subordonnait le déclenchement obligatoire prévu ici à un an sans initiative en cas d'accord ou trois ans sans accord. Ces attentes sont retirées et la voie sur demande est coordonnée au retrait de la réunion triennale. L'employeur peut devoir négocier plus tôt en l'absence d'accord : le texte ne démontre pas une réduction nette de toutes les obligations. Le droit déjà formulé à L2281-6 ne devient pas artificiellement une seconde extension.",
    scope_limitations="Le nouveau régime vise les demandes futures d'organisations syndicales représentatives ; les demandes antérieures recevables et leurs délais sont préservés. La portée du refus pénal L2283-1 appelle une coordination propre. Ni les calendriers de négociation autonomes, ni les salaires, ni les majorités ne sont supprimés ; le coût net n'est pas mesuré.",
    new_burdens_review="Charge élargie identifiée : ouverture obligatoire de la négociation dans les quinze jours même avant trois ans sans accord, et transmission sous huit jours pour ces demandes désormais recevables. Aucune nouvelle forme, donnée, attestation ou registre n'est exigé. L'absence de procédure parallèle de même objet préserve les droits de participation et ne supprime pas la négociation en cours. Aucun solde global des codes n'est chiffré.",
    effects=[
        effect('coordination', 'expression-salaries-reexamen-sur-demande',
               "Articulation de la négociation sur demande avec la fin de la réunion triennale automatique, sans compter une seconde réunion supprimée.",
               "L'article combine l'absence d'initiative pendant un ou trois ans et l'ouverture dans les quinze jours ; L2281-6 impose séparément un réexamen triennal.",
               "Une voie de négociation sur demande après suppression, dans L2281-6, du seul réexamen périodique distinct ; quinze jours et huit jours conservés.",
               'legal_duty', "Employeurs et organisations syndicales représentatives concernés par le droit d'expression.",
               "Demandes futures ; effets des demandes antérieures recevables et délais déjà commencés maintenus.",
               "Le réexamen n'est pas remplacé par un rapport ; l'élargissement temporel des demandes est décrit séparément sous la mesure correspondante.",
               "la négociation s'engage obligatoirement à la demande d'une organisation syndicale représentative dans les quinze jours suivant la présentation de cette demande.",
               "A la demande d'une organisation syndicale représentative, la négociation sur les modalités d'exercice du droit d'expression ou la renégociation de l'accord existant s'engage obligatoirement dans les quinze jours suivant la présentation de cette demande."),
        effect('deadline_reduced', 'expression-salaries-demande-sans-attente',
               "Suppression de l'attente légale avant la demande entraînant l'ouverture obligatoire, notamment des trois ans sans accord.",
               "Sans accord, absence d'initiative de l'employeur pendant trois ans depuis l'ouverture de la négociation précédente ; avec accord, un an dans cet article sous réserve du droit déjà ouvert par L2281-6.",
               "Aucune attente d'un an ou de trois ans ni condition d'inertie patronale ; délai de quinze jours après demande et transmission sous huit jours inchangés.",
               'other', "Organisations syndicales représentatives demandant une négociation sur l'expression des salariés.",
               "Demandes à compter de l'entrée en vigueur ; demandes antérieures recevables protégées. Les années ne sont pas converties artificiellement en jours fixes.",
               "L'employeur doit répondre aux demandes plus précoces ; aucune baisse nette des charges de toutes les parties n'est affirmée.",
               "A défaut d'initiative de l'employeur dans le délai d'un an en cas d'accord, ou de trois ans en l'absence d'accord,",
               "L'exercice de ce droit n'est subordonné ni à l'absence d'initiative de l'employeur, ni à l'écoulement d'un délai d'un an ou de trois ans depuis l'ouverture de la négociation précédente."),
        effect('obligation_added', 'expression-salaries-demande-sans-attente',
               "Extension dans le temps de l'obligation patronale d'ouvrir la négociation et d'en informer les autres organisations.",
               "En l'absence d'accord, le déclenchement imposé par cet article suppose trois ans sans initiative ; les délais d'ouverture et de transmission sont quinze et huit jours.",
               "Même en l'absence d'accord avant trois ans, l'employeur ouvre la négociation sous quinze jours sur demande représentative et transmet celle-ci aux autres organisations sous huit jours.",
               'legal_duty', "Employeurs recevant une demande représentative avant l'ancien terme, notamment en l'absence d'accord.",
               "Demandes nouvelles uniquement ; pas de seconde procédure parallèle de même objet ; droits des participants et demandes antérieures recevables préservés.",
               "Obligation de négocier, sans obligation de conclure ; pas de déclaration ou de document nouveau, mais davantage de demandes peuvent devenir recevables et engendrer la transmission existante.",
               "A défaut d'initiative de l'employeur dans le délai d'un an en cas d'accord, ou de trois ans en l'absence d'accord, la négociation s'engage obligatoirement à la demande d'une organisation syndicale représentative dans les quinze jours suivant la présentation de cette demande.",
               "A la demande d'une organisation syndicale représentative, la négociation sur les modalités d'exercice du droit d'expression ou la renégociation de l'accord existant s'engage obligatoirement dans les quinze jours suivant la présentation de cette demande.")])
answers[a['number']] = a


# Les preuves retiennent des alinéas entiers, sans coupure de phrase.
def paragraph(xml, needle):
    for part in re.findall(r'<p>(.*?)</p>', xml, flags=re.S):
        text = plain(part).strip()
        if needle in text:
            return text
    raise AssertionError(needle)


def paragraphs_range(xml, start, end):
    text = plain(xml)
    first = text.index(start)
    last = text.index(end, first)
    return text[first:last].rstrip()


# Une seule preuve continue couvre les trois retraits de la même mesure.
proof = answers['L2271-1']['substantive_impact']['effects'][0]
proof['source_quote'] = paragraphs_range(by_number['L2271-1']['source_xml'],
                                         '7° ', '10° ')
proof['proposed_quote'] = paragraphs_range(answers['L2271-1']['proposed_xml'],
                                           '7° ', '10° ')
answers['L2281-6']['substantive_impact']['effects'][0]['source_quote'] = plain(by_number['L2281-6']['source_xml']).strip()
for proof in answers['L2281-7']['substantive_impact']['effects']:
    proof['source_quote'] = plain(by_number['L2281-7']['source_xml']).strip().split('\n')[0]


allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())


class Tags(HTMLParser):
    def handle_starttag(self, tag, attrs):
        assert tag in allowed, tag
        for key, value in attrs:
            assert key in ('rowspan', 'colspan') and value.isdigit(), (key, value)


result = [answers[s['number']] for s in sources]
assert len(result) == len(sources) == 24
for source, a in zip(sources, result):
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[key] == a[key]
    impact = a['substantive_impact']
    assert impact['version'] == 1
    for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(impact[key]) >= 40
    if source.get('benefit_check_required'):
        assert len(a['benefit_review']) >= 100
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert impact['effects'] == []
    else:
        Tags().feed(a['proposed_xml'])
        assert all(len(x) >= 30 for x in a.get('removed_provisions', []))
    effect_keys = [(e['measure_id'], e['kind']) for e in impact['effects']]
    assert len(effect_keys) == len(set(effect_keys)), (a['number'], 'duplicate measure and effect')
    for e in impact['effects']:
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12 and len(e['proposed_quote']) >= 12
        assert e['source_quote'] in plain(source['source_xml']), (a['number'], 'source', e['source_quote'])
        assert e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], 'proposed', e['proposed_quote'])

with open('answer.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'article_count': len(result),
                  'rewritten': sum(a['status'] == 'rewrite_draft' for a in result),
                  'retained': sum(a['status'] == 'retained_unchanged' for a in result)}, ensure_ascii=False))
