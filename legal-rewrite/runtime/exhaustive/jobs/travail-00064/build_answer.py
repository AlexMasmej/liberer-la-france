import json
import re
from html import unescape
from pathlib import Path


SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml))


def paragraphs(*items):
    return ''.join('<p>' + item + '</p>' for item in items)


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


ANSWERS = []


def add(number, reason, review, assessment, limitations, burdens,
        proposed=None, impact_class='retained_necessary', effects=None,
        removed=None):
    s = BY_NUMBER[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=review,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    a['substantive_impact'] = dict(
        version=1, classification=impact_class, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects or [])
    a['reference_checks'] = []
    ANSWERS.append(a)
    return a


add('L2344-2',
    "Maintien intégral après examen des deux alinéas : la désignation syndicale à partir des dernières élections réutilise une représentation déjà élue, sans imposer un second scrutin en présence de syndicats. Les deux hypothèses, instance constituée en France et représentation française dans une instance constituée dans un autre Etat, doivent rester couvertes. Aucun prélèvement, agrément, rapport périodique ni justificatif redondant n'est institué ici ; retirer le mécanisme priverait les salariés d'une désignation représentative.",
    "Articuler cet article avec L2344-3 pour les collèges et le plus fort reste, et avec L2344-5 et L2344-6 pour l'absence de syndicat. Les résultats sont ceux des dernières élections, sans ancienneté individuelle supplémentaire. Cadre européen identifié : désignation nationale du groupe spécial de négociation et du comité européen, directive 2009/38/CE ; son texte consolidé n'est pas joint et sa conformité exhaustive n'est pas certifiée. Aucune nouvelle durée d'emploi ou restriction aux futurs contrats uniques n'est déduite de la durée des mandats.",
    "La source entière reste applicable : les organisations syndicales désignent parmi leurs élus ou représentants, sur les derniers résultats, dans les deux configurations territoriales. Aucune réduction nouvelle n'est revendiquée pour cette réutilisation déjà prévue.",
    "Le maintien concerne la désignation des représentants français ; il ne règle ni les sièges d'autres Etats ni une réforme européenne. Aucun solde global de coût des instances n'est établi.",
    "Aucune charge nouvelle n'est identifiée : maintien des mêmes candidats possibles, résultats électoraux et destinataires, sans nouveau scrutin, fichier ou dépôt.")

add('L2344-3',
    "Maintien intégral des deux répartitions distinctes. Le poids numérique des collèges protège la représentation des catégories de salariés ; le nombre d'élus et le plus fort reste déterminent ensuite la part de chaque syndicat. Ces calculs ne sont ni deux déclarations identiques ni deux autorisations : ils répondent à deux objets de représentativité. La suppression d'une étape modifierait les droits électoraux sans allègement administratif autonome démontré.",
    "Ne pas remplacer le nombre d'élus par le nombre de voix et ne pas appliquer le plus fort reste à une autre assiette. L2344-2 fixe les personnes désignables ; la source ne prévoit ici aucune transmission ni périodicité à retirer. R2344-1, lu dans le corpus, règle séparément les sièges par Etat, non le présent partage entre collèges et syndicats français.",
    "Les deux assiettes et le plus fort reste sont conservés exactement. Il s'agit d'une garantie de répartition des sièges, sans baisse de cotisation ou formalité supprimée par ce maintien.",
    "Aucun changement du nombre de sièges européens ou du coût des élections nationales n'est démontré ; seules les règles françaises de répartition sont examinées ici.",
    "Aucune charge nouvelle n'est identifiée : mêmes calculs sur les effectifs et les élus existants, sans attestation, registre ni transmission supplémentaire.")

add('L2344-4',
    "Maintien intégral : les représentants des établissements situés dans les autres Etats sont élus ou désignés selon les règles ou usages de ces Etats. Cette règle de conflit évite de cumuler une procédure française avec la procédure nationale et protège leur représentation. Aucun dossier français, agrément ou délai minimal autonome n'est ici imposé à ces établissements.",
    "L2341-1, lu en entier, délimite les Etats de la Communauté européenne ou de l'Espace économique européen ; L2343-1, lu en entier, vise le comité institué en l'absence d'accord, notamment après les délais de six mois et de trois ans. Conserver ce champ et ne pas imposer aux représentants étrangers le contrat unique français ou le préavis individuel de quinze jours.",
    "La source entière est maintenue : priorité aux règles nationales de l'Etat d'implantation pour les élections ou désignations visées. L'absence de procédure française cumulée existe déjà et n'est pas un gain nouveau.",
    "Les règles et usages de chacun des Etats ne sont pas fournis ; leur contenu n'est ni réécrit ni réputé vérifié. Le champ subsidiaire du renvoi L2343-1 demeure.",
    "Aucune charge nouvelle n'est identifiée : aucun double scrutin, contrôle français additionnel ou collecte de données étrangère n'est ajouté.")

source = BY_NUMBER['L2344-5']
p23445 = paragraphs(
    "Pour l'entreprise ou le groupe d'entreprises de dimension communautaire dont le siège social ou celui de l'entreprise dominante est implanté en France, lorsqu'il n'existe pas d'organisation syndicale, les représentants du personnel au groupe spécial de négociation ou au comité d'entreprise européen sont élus directement, selon les règles applicables au comité social et économique.")
add('L2344-5',
    "Coordination nécessaire de la dénomination de l'instance : le « comité social et économique européen » de la source est remplacé par le comité d'entreprise européen du titre IV. L'élection directe en l'absence de syndicat, l'implantation du siège et le recours aux règles électorales du CSE sont entièrement conservés. Cette correction d'une incohérence préexistante ne supprime aucune obligation et n'est pas une simplification matérielle comptée.",
    "L2344-2 à L2344-4 et L2344-6 distinguent le comité d'entreprise européen du CSE national ; la source de L2344-5 mêle leurs dénominations. Le renvoi de L2344-6 à la présente élection garde son objet, y compris son seuil propre de cinquante salariés. La correction ne crée pas une nouvelle institution. Les élections et mandats régulièrement constitués avant l'entrée en vigueur restent identifiés comme ceux de l'instance européenne ; aucune réélection ne résulte de la seule dénomination corrigée.",
    "Seule la dénomination incohérente de l'organe européen est rectifiée par rapport à la source officielle entière. Le scrutin direct et ses conditions ne sont ni supprimés ni renouvelés par cette coordination.",
    "Aucune réduction d'obligation ou de coût n'est démontrée. Les règles électorales du CSE demeurent applicables sans prétendre réviser tous leurs règlements dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : la correction ne crée ni second comité ni nouveau scrutin ni condition de mandat ; elle identifie l'instance déjà visée.",
    proposed=p23445, impact_class='coordination_only', effects=[effect(
        'coordination', 'comite-europeen-denomination',
        "Correction de la dénomination de l'instance européenne sans changement du mode de représentation.",
        "La source désigne un comité social et économique européen tout en renvoyant aux règles du CSE national.",
        "La représentation concerne le comité d'entreprise européen ; les règles du CSE restent le référentiel électoral.",
        'other', "Représentants des salariés des entreprises ou groupes dont le siège pertinent est en France, sans syndicat.",
        "Même champ et mêmes mandats ; aucune reprise des élections du seul fait de la correction.",
        "Aucune obligation remplacée ou ajoutée ; correction de nom seulement.",
        'comité social et économique européen', "comité d'entreprise européen")])

add('L2344-6',
    "Maintien intégral du droit d'élire directement les représentants français en l'absence de syndicat lorsque l'instance européenne doit être constituée dans un autre Etat. Le seuil propre d'au moins cinquante salariés limite la charge électorale ; le retirer ou le réduire pourrait créer une obligation nouvelle pour les petits établissements. L'élection reste une garantie de représentation, sans agrément ou déclaration indépendante à supprimer.",
    "L2341-1 et L2344-5 ont été lus. Le premier fixe le champ des Etats, le second l'élection directe selon les règles du CSE. La proposition de L2344-5 corrige uniquement le nom du comité européen ; elle n'altère donc pas ce renvoi. Les cinquante salariés concernent l'établissement ou l'entreprise implanté en France, non l'effectif mondial ni une condition d'ancienneté du salarié.",
    "La source entière et son seuil favorable de cinquante salariés sont conservés. Aucune suppression d'obligation n'est comptée : la procédure donne une représentation aux salariés français dans l'instance établie à l'étranger.",
    "Aucune obligation française n'est étendue aux autres établissements étrangers. Les droits nationaux d'accueil et le cadre européen ne sont pas intégralement joints.",
    "Aucune charge nouvelle n'est identifiée : maintien du seuil, du défaut de syndicat et de la même élection directe, sans document supplémentaire.")

add('L2344-7',
    "Maintien intégral de l'accès au juge judiciaire pour contester les désignations françaises au groupe spécial de négociation ou au comité européen. Il ne s'agit ni d'une autorisation préalable ni d'un recours obligatoire à exercer pour que la désignation produise effet. Supprimer cette compétence rendrait le contrôle de la représentation incertain, sans retirer une formalité imposée aux employeurs.",
    "R2344-3, lu avec ses notes, désigne le tribunal judiciaire du siège de l'entreprise ou de la filiale française dominante ; la note du 1er janvier 2020 est historique et ne date pas la réforme proposée. La compétence ne doit pas être étendue aux désignations relevant exclusivement d'un autre Etat. Aucun délai de préavis de quinze jours ni seuil d'un an d'ancienneté n'est applicable à ce droit de recours.",
    "Le recours judiciaire prévu par toute la source est préservé. Aucun contrôle préalable, nouvelle sanction ou démarche de routine n'est supprimé par ce maintien nécessaire.",
    "La source ne fixe ni délai contentieux ni frais ; aucun raccourcissement ou gain chiffré ne peut être déduit de ce texte de compétence.",
    "Aucune charge nouvelle n'est identifiée : le juge reste le même, sans saisine systématique ou préalable obligatoire ni nouvel envoi.")

add('L2344-8',
    "Maintien intégral des deux obligations précisément délimitées : secret sur les procédés de fabrication, discrétion sur les informations objectivement confidentielles présentées comme telles. Ces garanties protègent les secrets économiques nécessaires à une information effective des représentants, sans instaurer une confidentialité générale de tous les travaux. Aucun agrément d'expert, dépôt annuel ou justificatif administratif n'est prescrit par cet article.",
    "L2343-1 a été lu : le renvoi réserve la règle aux membres du comité institué selon le régime subsidiaire, outre le groupe spécial et les experts. La comparaison avec L2315-3, lu en entier, confirme la distinction entre secret des procédés et discrétion conditionnelle. Le seul marquage de l'employeur ne dispense pas de la condition objective de confidentialité. Cadre européen de confidentialité identifié, directive 2009/38/CE ; texte consolidé non joint, aucune interdiction implicite des divulgations légalement protégées n'est ajoutée.",
    "Les seuls secrets et informations désignés par les 1° et 2° restent protégés. La source entière est conservée pour éviter de supprimer les garanties de confidentialité qui permettent la communication des données économiques.",
    "Les exceptions légales autonomes, la protection des alertes et les recours conservent leur champ ; cet article ne les inventorie pas et leur suppression n'est pas présumée.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvelle catégorie de secret, de classement général, d'autorisation de communiquer ou de registre.")

add('L2344-9',
    "Maintien intégral du droit aux formations nécessaires au mandat, sans perte de salaire. La nécessité de la formation en limite déjà le champ ; la rémunération est un avantage à conserver, également pour les futurs membres. Il ne s'agit pas d'un état annuel obligatoire ou d'une formation nouvelle imposée à tout salarié. La supprimer ferait disparaître une garantie essentielle sans simplification administrative propre démontrée.",
    "Conserver les deux groupes de bénéficiaires et le caractère subsidiaire du comité institué en l'absence d'accord. Le droit ne doit être ni subordonné à un an d'ancienneté ni plafonné par les six mois de l'indemnité ordinaire. La durée de formation n'est pas un terme d'emploi. Le cadre européen de formation des représentants est identifié ; aucune prise en charge nouvelle de frais autres que ceux effectivement prévus par les textes applicables n'est inventée.",
    "Toute la source est maintenue, notamment le salaire pendant les formations nécessaires et l'accès des futurs titulaires éligibles. Aucun allègement nouveau n'est revendiqué.",
    "Le texte ne précise ni nombre d'heures ni tarif de formation ; aucun montant, financement additionnel ou économie ne peut en être déduit.",
    "Aucune charge nouvelle n'est identifiée : mêmes bénéficiaires, nécessité liée au mandat et maintien de salaire, sans attestation périodique ou nouvel agrément.")

p23451 = paragraphs(
    "Lorsque, du fait d'une baisse des effectifs, l'entreprise ou le groupe d'entreprises de dimension communautaire ne remplit plus les conditions de seuils mentionnées à l'article L. 2341-1, le comité d'entreprise européen, qu'il ait été institué ou non par accord, peut être supprimé par accord.",
    "A défaut d'accord, l'employeur peut décider la suppression du comité en cas de réduction importante et durable du personnel ramenant l'effectif au-dessous de ces seuils. Aucune autorisation administrative préalable, déclaration ou demande de visa n'est requise à ce titre. Les stipulations conventionnelles plus favorables organisant le maintien du comité restent applicables. La réalité des conditions de suppression demeure soumise au contrôle du juge.",
    "Ces dispositions s'appliquent aux suppressions décidées à compter de l'entrée en vigueur de la loi. Les demandes d'autorisation encore en cours à cette date n'ont plus à être poursuivies ; elles ne valent pas, par elles-mêmes, décision de suppression. Les décisions antérieures et les recours qui les concernent restent régis par les dispositions antérieurement applicables. La suppression ne porte atteinte ni aux créances nées du fonctionnement du comité avant sa disparition, ni aux droits de recours, ni aux autres institutions de représentation du personnel.")
add('L2345-1',
    "Réforme de fond : suppression de l'autorisation administrative préalable de suppression du comité en cas de réduction importante et durable des effectifs sous les seuils. L'employeur peut décider sous ces conditions objectives, sans déclaration ni visa de remplacement et sous contrôle du juge. La voie d'accord du premier alinéa est conservée, ainsi que les garanties conventionnelles plus favorables, les créances et les recours antérieurs. La disparition d'un seuil ne devient pas une faculté générale de supprimer les représentations encore obligatoires.",
    "L2341-1 et L2341-2, lus dans le corpus, conservent les seuils d'au moins mille salariés et la présence d'au moins cent cinquante salariés dans au moins deux Etats selon leurs champs respectifs. R2345-1, lu intégralement avec toutes ses notes territoriales de 2009 et 2010, doit perdre sa compétence d'autorisation pour les décisions nouvelles : coordination réglementaire à effectuer hors de ce lot, non déclarée achevée. Le contrôle préalable est remplacé par le contrôle juridictionnel des conditions, pas par une déclaration. Le maintien des stipulations plus favorables limite la faculté patronale afin de préserver les avantages conventionnels. Le cadre européen des comités et le respect des accords doivent être confrontés à la version applicable de la directive 2009/38/CE, non jointe ; aucune conformité européenne définitive n'est affirmée. Ni dissolution automatique à la baisse des effectifs, ni effet sur les autorisations de licenciement protégé, procédures collectives ou préavis individuel.",
    "Par rapport aux deux alinéas de la source, une autorisation préalable disparaît réellement pour les décisions futures sans accord, sous la même condition de réduction importante et durable sous les seuils. L'accord et les protections conventionnelles demeurent. Il ne s'agit ni d'une taxe supprimée ni d'une disparition générale des comités.",
    "La mesure ne concerne que la suppression du comité européen sous les seuils ; le règlement R2345-1 reste à coordonner et le texte européen consolidé n'est pas fourni. L'effet net sur les coûts publics et contentieux n'est pas établi.",
    "Aucune charge nouvelle de déclaration, registre, données ou délai n'est identifiée : aucun dossier ne remplace l'autorisation. Le contrôle juridictionnel conserve l'exigence de prouver la réduction durable ; les clauses de maintien plus favorables sont réservées. Un contentieux éventuel et son coût restent possibles sans solde global chiffré.",
    proposed=p23451, impact_class='material_reduction', removed=[
        "Autorisation administrative préalable de suppression du comité d'entreprise européen en l'absence d'accord après une réduction importante et durable sous les seuils légaux."
    ], effects=[effect(
        'authorization_removed', 'comite-europeen-suppression-sans-autorisation',
        "Retrait du contrôle administratif préalable pour la suppression d'un comité européen devenu hors seuils, avec contrôle juridictionnel et garanties conventionnelles préservés.",
        "En l'absence d'accord, la suppression pour réduction importante et durable sous les seuils de L2341-1 est subordonnée à une autorisation que l'autorité administrative peut accorder.",
        "En l'absence d'accord, l'employeur décide sous la même condition de réduction importante et durable, sans autorisation, déclaration ni visa ; les clauses plus favorables et le juge demeurent.",
        'legal_duty', "Entreprises et groupes dotés d'un comité européen dont les effectifs baissent de façon importante et durable sous les seuils légaux.",
        "Décisions de suppression à compter de l'entrée en vigueur ; demandes pendantes non poursuivies sans suppression automatique ; décisions et recours antérieurs, créances et autres représentants préservés.",
        "Aucune déclaration de remplacement ; contrôle des conditions par le juge et respect des clauses conventionnelles de maintien, avec coût contentieux éventuel non chiffré.",
        "A défaut d'accord, l'autorité administrative peut autoriser la suppression du comité en cas de réduction importante et durable du personnel ramenant l'effectif au-dessous de ces seuils.",
        "Aucune autorisation administrative préalable, déclaration ou demande de visa n'est requise à ce titre.")])

add('L2345-2',
    "Maintien intégral d'une faculté existante de fusion fonctionnelle : un accord peut supprimer le comité de groupe après vote favorable de celui-ci et transférer ses compétences au comité européen. Cette disposition évite déjà un cumul d'instances sans retirer l'information, la consultation et l'expertise correspondantes. Le vote protège le consentement effectif de l'instance supprimée ; il n'est pas une autorisation administrative redondante à éliminer.",
    "L2342-2, L2332-1, L2332-2 et L2334-4 ont été lus en entier, propositions disponibles comprises. Les renvois transfèrent les informations économiques et d'emploi, le régime d'OPA et l'expertise-comptable rémunérée par l'entreprise dominante. L2332-1 et L2332-2 contiennent dans leurs sources des renvois anciens à L2323 ; leurs propositions du corpus les coordonnent vers les dispositions du CSE, sans être le droit en vigueur. Ces corrections des articles cibles doivent être adoptées avec le dispositif ; elles ne sont pas rédigées à nouveau ici. Le renvoi direct de cet article à leurs compétences reste pertinent. Ne pas compter une seconde fusion nouvelle et ne pas assimiler ce vote au préavis individuel de rupture.",
    "La source entière préserve une fusion déjà possible et le transfert des droits vers le comité européen, sous accord et vote favorable. Aucune nouvelle obligation fusionnée ou supprimée n'est comptée par ce maintien.",
    "L'effet suppose un accord et un vote effectif ; aucun comité n'est supprimé automatiquement. Les renvois internes anciens des articles cibles exigent leur propre coordination, identifiée dans le corpus.",
    "Aucune charge nouvelle n'est identifiée : ni second rapport ni second expert n'est imposé par ce maintien ; les garanties et le vote de la source restent ceux du mécanisme existant.")

add('L2346-1',
    "Maintien intégral des deux infractions : entrave à la constitution ou à la libre désignation, et entrave au fonctionnement. Les peines protègent l'effectivité des droits collectifs et du recours des salariés ; elles ne constituent pas une taxe de production ou une cotisation à supprimer. Le second alinéa ne prévoit déjà pas d'emprisonnement. Aucune déclaration de conformité, autorisation ou sanction administrative doublonnée n'est instituée ici.",
    "L2342-1 à L2342-7 et L2343-1 ont été lus en entier : constitution, initiative, réunions, moyens et régime subsidiaire sont bien les obligations protégées. Conserver l'an d'emprisonnement et les deux mentions de 7 500 euros dans leurs champs distincts, sans les additionner comme une peine automatique pour les mêmes faits. Le cadre européen exige une protection effective de l'information et de la consultation ; aucune obligation de peine d'emprisonnement issue du seul droit de l'Union n'est affirmée. La suppression d'autorisation de L2345-1 ne décriminalise pas l'entrave aux instances restant légalement en place.",
    "Toute la source pénale est maintenue pour rendre effectifs la constitution, le libre choix des représentants et leur fonctionnement. Aucune recette fiscale supprimée ni baisse de prélèvement n'est revendiquée.",
    "L'application des peines et les principes de non-cumul relèvent des règles pénales autonomes ; aucun quantum nouveau ou contrôle de constitutionnalité indépendant n'est présenté comme effectué.",
    "Aucune charge nouvelle n'est identifiée : maintien des mêmes infractions et peines, sans attestation de conformité, contrôle préalable ou registre nouveau.")

add('L2351-1',
    "Maintien intégral des trois rattachements : SE française constituée selon le règlement cité, sociétés françaises participantes, et filiales ou établissements français d'une SE située dans un autre Etat membre ou de l'EEE. Ce champ évite de priver les salariés de représentation lors d'une constitution transfrontière et n'impose à lui seul ni déclaration ni agrément supplémentaire. Sa suppression serait une suppression du régime de représentation, non une simple formalité retirée.",
    "Conserver la date du règlement (CE) n° 2157/2001 du 8 octobre 2001 et les trois catégories, sans prendre cette date pour l'entrée en vigueur d'une réforme future. Le règlement et la directive 2001/86/CE relatifs à la SE sont des contraintes européennes à coordonner ; leurs textes intégraux ne sont pas joints et aucune conformité consolidée indépendante n'est affirmée. Le champ couvre les salariés des entités françaises sans réformer implicitement les régimes d'agents publics ou les droits des autres Etats.",
    "La source entière délimitant les personnes concernées reste applicable. Aucun agrément ou dépôt distinct n'a été identifié dans cet article de champ et aucune économie n'est déduite de son maintien.",
    "Le règlement européen cité n'est pas fourni intégralement. L'examen porte sur les trois rattachements nationaux, sans réécriture des règles d'immatriculation du code de commerce.",
    "Aucune charge nouvelle n'est identifiée : mêmes sociétés, participantes et implantations françaises, sans extension territoriale ni nouvelle demande administrative.")

p23512 = paragraphs(
    "Lorsqu'une société européenne mentionnée à l'article L. 2351-1 est une entreprise de dimension communautaire ou un groupe d'entreprises de dimension communautaire au sens, respectivement, des articles L. 2341-1 et L. 2341-2, les dispositions du titre IV relatif au comité d'entreprise européen ou à la procédure d'information et de consultation dans les entreprises de dimension communautaire ne sont applicables ni à la société européenne ni à ses filiales.")
add('L2351-2',
    "Coordination du renvoi de définition : L2341-2 définit le groupe, tandis que L2341-1 définit l'entreprise ; les deux cibles sont désormais distinguées expressément. L'exclusion du cumul du titre IV avec le régime de la SE reste intégralement conservée pour la société et ses filiales, y compris les futures situations éligibles. Aucun nouveau gain de suppression d'instance n'est attribué à une exclusion déjà présente dans la source.",
    "L2351-1, L2341-1 et L2341-2 ont été lus intégralement. Nouveau renvoi exprès à L2341-1 : cible absente des quatre vues de reference-targets.json, mais texte officiel fourni dans le corpus public et lu ; il définit l'entreprise de mille salariés avec établissements de cent cinquante dans au moins deux Etats. L2341-2 garde son propre champ de groupe. L2352-13 et le chapitre III ont également été lus : la décision qualifiée de ne pas négocier a un régime particulier. L'articulation de l'exclusion avec cette décision et les exceptions européennes doit être confrontée à la directive 2001/86/CE, notamment son article 13, non jointe ; ce point est signalé, sans inventer une exception ni affirmer la conformité de l'exclusion générale source. La présente correction ne modifie pas ce régime préexistant.",
    "La source exclut déjà l'application du titre IV aux SE et à leurs filiales. La proposition rectifie seulement la cible de définition entreprise/groupe et conserve cette absence de cumul ; elle ne supprime pas une seconde institution nouvelle.",
    "Aucune réduction matérielle nouvelle n'est démontrée. L'articulation européenne de l'exclusion, notamment en cas de décision de ne pas négocier, demeure un point de confrontation documentaire identifié et non réputé résolu.",
    "Aucune charge nouvelle n'est identifiée : les deux définitions délimitent le même régime d'exclusion, sans nouveau dossier, seuil, contrôle ou élection ajouté.",
    proposed=p23512, impact_class='coordination_only', effects=[effect(
        'coordination', 'societe-europeenne-exclusion-double-instance',
        "Distinction expresse des définitions de l'entreprise et du groupe dans le renvoi qui délimite l'exclusion existante.",
        "Un renvoi au seul L2341-2, définissant le groupe, accompagne les deux notions d'entreprise et de groupe communautaires.",
        "Renvois respectifs à L2341-1 pour l'entreprise et L2341-2 pour le groupe ; même exclusion du titre IV pour la SE et ses filiales.",
        'regime', "Sociétés européennes de L2351-1 et leurs filiales entrant dans le champ communautaire concerné.",
        "Coordination de définition sans suppression de droits antérieurs ni nouvelle procédure ; les cas de non-négociation gardent leur régime propre à confronter au cadre européen.",
        "Aucun dispositif de représentation supplémentaire ; aucune formalité remplacée ou ajoutée.",
        "au sens de l'article L. 2341-2",
        "au sens, respectivement, des articles L. 2341-1 et L. 2341-2")])

add('L2351-3',
    "Maintien intégral de l'information, de la consultation et, le cas échéant, de la participation, organisées prioritairement par accord. Le chapitre III est un régime subsidiaire, pas un second circuit cumulé avec l'accord. Supprimer le fondement de l'accord ou le dispositif de secours affaiblirait l'implication effective des salariés ; aucune autorisation, déclaration ou prélèvement autonome ne figure dans les trois alinéas.",
    "Le chapitre III a été lu intégralement, L2353-1 à L2353-32, y compris L2353-27-1 : L2353-1 réserve l'absence d'accord et l'absence de décision de L2352-13. Ce renvoi ne signifie donc pas application automatique du chapitre dans tous les échecs de négociation. Les cibles du chapitre comportent des renvois préexistants à L2325-5 et L2325-44, ainsi que des renvois réglementaires anciens à coordonner dans leurs articles propres, hors lot ; le maintien du renvoi au chapitre n'en valide pas la concordance. Cadre de la directive 2001/86/CE identifié, texte intégral non joint.",
    "La source entière conserve une voie d'accord et un régime subsidiaire distinct, avec participation seulement lorsqu'elle s'applique. Aucun double régime supplémentaire n'est supprimé par ce maintien.",
    "Le chapitre de référence reste à coordonner dans ses propres articles pour ses références anciennes ; il n'est pas déclaré réécrit ici. Le coût global de la représentation n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : ni participation universelle, ni second accord, ni dépôt ou calendrier nouveau n'est ajouté aux trois alinéas.")

add('L2351-4',
    "Maintien intégral de la définition de l'information transnationale et de sa finalité : permettre l'évaluation des incidences puis, le cas échéant, la préparation d'une consultation. Les deux branches territoriales et le dépassement des pouvoirs nationaux limitent le champ ; cet article ne crée pas un rapport périodique ou une collecte générale à retirer. La définition est nécessaire pour éviter une information sans utilité pour les représentants.",
    "Ne pas remplacer la société européenne elle-même et toute filiale ou établissement situé dans un autre Etat par la totalité indifférenciée des questions locales. L2353-3, lu dans le chapitre III, reprend la délimitation transnationale ; L2351-5 distingue l'avis issu de la consultation. L'article ne fixe aucun délai de quinze jours ni procédure de licenciement. Cadre européen de définition identifié : directive 2001/86/CE ; consolidation intégrale non fournie.",
    "Les deux alinéas de la source sont conservés, avec leur périmètre transnational et leur finalité d'évaluation. Aucune transmission doublonnée déterminée n'est identifiée dans cette définition.",
    "Les supports et périodicités relèvent d'autres dispositions ou accords ; aucun délai, volume de données ou gain de coût n'est déduit du seul présent article.",
    "Aucune charge nouvelle n'est identifiée : aucun rapport récurrent, rubrique de données, destinataire ni justificatif de plus n'est créé.")

add('L2351-5',
    "Maintien intégral de la consultation comme dialogue permettant un avis à partir des informations fournies. La possibilité de prise en considération de l'avis n'est ni un agrément des représentants ni un droit de veto général. Supprimer cette définition ne retire pas un dossier inutile : cela compromettrait l'effectivité de la consultation et sa distinction avec une simple transmission d'information.",
    "L2351-4 fournit le cadre de l'information et L2351-6 définit séparément la participation aux organes sociaux. Conserver le caractère d'avis et le verbe « peut » du second alinéa, sans créer une obligation générale d'obtenir un accord avant toute décision. Les consultations et protections collectives restent distinctes du préavis individuel de quinze jours ; aucune réduction de leur calendrier n'est impliquée.",
    "La totalité de la source reste applicable : dialogue et échange de vues en vue d'un avis, sans droit d'autorisation générale. Aucun allègement nouveau n'est revendiqué.",
    "La définition ne fixe ni délai ni procédure sectorielle et ne chiffre aucun coût. Les obligations d'une opération déterminée restent celles de leurs textes propres.",
    "Aucune charge nouvelle n'est identifiée : aucun avis conforme, accord obligatoire, formulaire ou suspension automatique de décision n'est ajouté.")

add('L2351-6',
    "Maintien intégral des deux formes de participation des salariés aux affaires sociales : élire ou désigner des membres, ou recommander leur désignation ou s'y opposer. Il s'agit de droits de gouvernance, non d'une cotisation ou d'une participation financière à transférer. La définition doit rester disponible pour protéger les droits de participation existants et déterminer les régimes applicables aux futures SE.",
    "Les deux formes sont alternatives et ne deviennent pas cumulatives. L2352-13, L2352-17 à L2352-19 et L2353-28 à L2353-32, lus dans le corpus, distinguent les majorités, les systèmes antérieurs et les modes de constitution ; cet article n'impose pas la participation à toutes les sociétés. Aucun changement de financeur des retraites ou de taux fiscal n'est attaché au mot « participation ».",
    "Les deux branches de la source sont conservées pour identifier les droits aux organes de surveillance ou d'administration. Aucun régime financier n'est fusionné ou prélèvement réduit par ce maintien.",
    "Les proportions de sièges et les droits nationaux sous-jacents sont fixés ailleurs ; aucun nouveau quantum ou droit universel d'opposition n'est inventé.",
    "Aucune charge nouvelle n'est identifiée : aucune participation additionnelle, catégorie de données, élection ou autorisation n'est imposée par la définition maintenue.")

a23517 = add('L2351-7',
    "Maintien intégral du renvoi au calcul général des effectifs de L1111-2 pour les seules implantations françaises. Réemployer ce calcul évite de créer une assiette ou un registre parallèle pour la SE. La cible proposée préserve la proratisation des affectations temporaires et l'exclusion des remplaçants sous contrat unique, ainsi que les anciens CDD ; le renvoi lui-même reste cohérent et n'exige pas un nouveau corps normatif.",
    "Les quatre cibles exigées dans reference-targets.json ont été lues en entier, sources, notes et propositions comprises. Seul L1111-2 est un renvoi opératoire du présent article. Sa proposition distingue le CDI à temps plein, les affectations temporaires réelles, l'exclusion pendant le remplacement, les douze mois, le temps partiel et le décompte des intérimaires chez l'utilisateur ; son adoption coordonnée préserve ces modalités pour les futurs contrats uniques sans compter deux fois le salarié. Les propositions ne sont pas le droit en vigueur. Aucun renvoi nouveau à une règle de rupture n'est introduit et aucun agent public ou salarié d'une implantation étrangère n'est assimilé à un contrat privé français.",
    "Toute la source est maintenue : une seule règle générale de calcul pour les effectifs en France. Les avantages de décompte de la cible doivent suivre les futures affectations éligibles ; aucune nouvelle suppression d'obligation distincte n'est comptée ici.",
    "La cohérence future dépend de l'adoption coordonnée de L1111-2 proposé ; aucun calcul d'effectif étranger n'est réformé. Les seuils et votes des autres articles ne sont pas remplacés par un délai de rupture.",
    "Aucune charge nouvelle n'est identifiée : pas de registre autonome, attestation, nouveau calcul d'indemnité ou notification imposé par le maintien de ce renvoi.")

CHECK_TEXTS = {
    'L1234-1': "Cette cible règle le préavis individuel de licenciement, non le décompte des effectifs de la SE. Le projet prévoit quinze jours calendaires pour les nouveaux contrats, sans exemption pour faute grave ; il préserve pour les anciens contrats le régime inférieur à six mois, le mois de préavis entre six mois et moins de deux ans et les deux mois à partir de deux ans, sous règles plus favorables. Aucun de ces délais ou conditions d'ancienneté n'est importé dans L2351-7, qui n'y renvoie pas. Les protections et procédures collectives restent autonomes.",
    'L1221-2': "Cette cible règle la forme du contrat : le projet impose l'emploi nouveau à durée indéterminée, sans terme automatique de mission, formation ou affectation et sans nouveau renouvellement de CDD. L2351-7 ne crée aucune exception à cette règle ; son renvoi au décompte L1111-2 conserve les situations anciennes et les modalités temporaires éligibles sans transformer une durée de mandat en durée d'emploi.",
    'L1111-2': "Renvoi opératoire vérifié : CDI à temps plein intégrés, catégories proratisées sur douze mois, temps partiel selon les horaires et exclusion des remplacements. Pour la mise à disposition extérieure visée, la présence dans les locaux de l'utilisateur et le travail depuis au moins un an restent distincts du seuil d'indemnité de rupture. Le projet préserve les affectations temporaires éligibles sous contrat unique, l'exclusion pendant le remplacement, les anciens CDD et le régime des intérimaires chez l'utilisateur. Le maintien de L2351-7 suppose cette coordination, sans effectif étranger ajouté ni double compte.",
    'L1234-9': "Cette cible porte l'indemnité ordinaire, sans renvoi depuis L2351-7. Le projet retient un an à la fin effective, préavis inclus, puis 0,20 mois sur toute l'ancienneté et les mois complets, plafond de six mois, rupture patronale seulement, avec exception de faute grave et droits spéciaux distincts. Pour les anciens contrats, il conserve l'ouverture à huit mois, la composante des services antérieurs et les minima correspondants sans double compte. Ni ces seuils ni la notification de rupture ne conditionnent le décompte des salariés de la SE."
}
key23517 = a23517['code_id'] + '|' + a23517['source_id']
for target_key in REFS['requirements'][key23517]:
    t = REFS['targets'][target_key]
    a23517['reference_checks'].append(dict(
        target_key=target_key, view_sha256=t['view_sha256'],
        assessment=CHECK_TEXTS[t['number']]))

add('L2352-1',
    "Maintien intégral de la constitution rapide du groupe spécial de négociation après le projet pertinent et de sa personnalité juridique. Ce groupe temporaire permet un accord autonome avant la création de la SE ; il n'est pas une instance permanente à cumuler avec le comité définitif. Sa personnalité lui donne la capacité d'exercer et défendre ses droits sans introduire ici un agrément, une immatriculation ou un dossier séparé.",
    "Conserver les déclencheurs distincts : publication du projet de fusion ou de holding ; adoption du projet de filiale ou de transformation. « Dès que possible » n'est pas un délai minimal incompressible. L2352-9 et D2352-14, lus en entier, règlent séparément le début et la durée des négociations ; aucune disparition de leurs délais ne résulte de ce maintien. La durée d'existence du groupe ne termine aucun contrat de travail. Cadre européen de négociation identifié, directive 2001/86/CE, texte intégral non fourni.",
    "Les deux alinéas sont conservés : groupe constitué rapidement et doté de personnalité juridique pour la négociation. Aucun délai d'attente ou dépôt administratif distinct n'est identifié à supprimer dans cet article.",
    "Les procédures du projet de société et les règlements de convocation ne sont pas réécrits ici. Aucune économie globale de structure n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvelle personnalité à immatriculer séparément, de registre ni de rapport ajouté par rapport à la source.")

add('L2352-2',
    "Maintien intégral de l'accord écrit entre le groupe et les dirigeants ou leurs représentants. L'écrit est la preuve du consentement et du contenu des droits d'information, de consultation et, selon le cas, de participation ; il ne double pas un agrément administratif. Le retirer fragiliserait la protection collective et les modalités librement négociées sans supprimer un dépôt ou justificatif redondant déterminé.",
    "L2351-3, dans le lot, définit les trois composantes et la voie d'accord ; L2352-13, lu dans le corpus, fixe les majorités selon la décision, et non une simple signature individuelle. L'accord ne crée pas un CDD ni une durée maximale d'emploi. Aucun formulaire obligatoire, transmission CPPNI ou délai supprimé par la section negociation_collective n'est réintroduit : il s'agit d'un régime distinct d'implication dans la SE.",
    "La source entière est maintenue : accord écrit sur l'implication, conclu avec l'organe représentatif compétent. Aucune formalité supplémentaire à l'écrit utile n'est identifiée ni supprimée.",
    "Les clauses et majorités sont précisées dans d'autres articles ; aucun raccourcissement de délai, diminution de salaire ou gain budgétaire n'est établi ici.",
    "Aucune charge nouvelle n'est identifiée : mêmes parties et même écrit, sans formulaire, dépôt, certification ou autorisation additionnels.")

add('L2352-3',
    "Maintien intégral de la répartition des sièges entre Etats selon leurs effectifs et de la détermination des salariés représentés par chaque membre. Les deux opérations ne sont pas un doublon : l'une répartit les mandats, l'autre permet de vérifier les majorités de membres et de salariés. En supprimer une compromettrait le consentement collectif et pourrait modifier les droits de participation.",
    "R2352-5 et D2352-16 ont été lus intégralement : dix tranches de sièges selon l'effectif par Etat, puis représentation par membre et règles propres aux sièges supplémentaires. L2352-13, lu intégralement, exige une majorité absolue des membres représentant la majorité absolue des salariés et prévoit des décisions qualifiées aux deux tiers, ainsi que des seuils de 25 % et 50 % pour la réduction de participation. Le présent article ne change aucune de ces assiettes. Le décret en Conseil d'Etat fixe un nombre, ce n'est pas une demande d'autorisation adressée par l'entreprise.",
    "Les deux alinéas restent applicables : proportion d'effectifs par Etat et pondération des votes. Aucun calcul ou régime superflu supprimé n'est démontré au regard de leur fonction distincte.",
    "Les formules réglementaires et majorités restent inchangées et ne sont pas réécrites dans ce lot. Aucun effet financier global ne découle du maintien.",
    "Aucune charge nouvelle n'est identifiée : mêmes effectifs et pondérations, sans déclaration administrative, registre parallèle ou nouvelle condition de majorité.")

add('L2352-4',
    "Maintien intégral des sièges supplémentaires protégeant les salariés d'une société absorbée non directement représentée. Le plafond de 20 %, l'ordre décroissant des effectifs et la correction entre Etats évitent une représentation déséquilibrée. Le calcul final des salariés représentés empêche le double compte et n'est pas une production administrative doublonnée. Retirer ces garanties priverait certains salariés de voix lors de la fusion.",
    "Conserver les trois alinéas et les conditions cumulatives : fusion, disparition de la personnalité de la participante et défaut de représentation directe. Les 20 % sont rapportés au nombre de membres déterminé par L2352-3, non à l'effectif salarié ni à un taux fiscal. D2352-3, D2352-12 et D2352-16, lus en entier, règlent les sièges additionnels, leur attribution et la déduction de l'effectif déjà représenté. La règle d'alternance vise deux sociétés successives du même Etat et le siège suivant dans un Etat différent, sans quota national nouveau.",
    "La source entière conserve le correctif de représentation et son plafond de 20 %, ainsi que le contrôle du double compte. Aucun siège ou obligation réellement superflu n'est supprimé par ce maintien.",
    "Ce correctif ne s'étend pas aux autres modes de constitution de la SE. Les droits nationaux de participation et le coût des sièges ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : mêmes conditions, plafond, ordre d'attribution et calculs, sans nouveau formulaire ni justification de remplacement.")

source23525 = BY_NUMBER['L2352-5']
first4 = [s.strip() for s in source23525['source_xml'].split('<br />') if s.strip()][:4]
assert len(first4) == 4
p23525 = paragraphs(*first4,
    "La désignation de ces membres est notifiée par l'organisation syndicale à l'employeur par tout moyen donnant date certaine à sa réception. La lettre recommandée avec avis de réception n'est pas obligatoire et aucun envoi de confirmation n'est exigé. Cette liberté de moyen ne dispense pas de la notification ni de la preuve de sa réception ; un simple envoi électronique ne vaut pas, à lui seul, réception certaine.",
    "Ces modalités s'appliquent aux notifications effectuées à compter de l'entrée en vigueur de la loi, y compris pour une désignation antérieure. Les notifications déjà régulièrement effectuées n'ont pas à être renouvelées. Les points de départ, durées et conditions des recours restent applicables selon leur régime ; aucun délai expiré n'est rouvert.")
add('L2352-5',
    "Réduction normative ciblée du dernier alinéa : la notification reste obligatoire, mais sa forme réglementaire exclusive cède devant tout moyen prouvant la réception et sa date, sans recommandé ni confirmation imposés. D2352-7, lu dans le corpus, impose actuellement le recommandé avec avis de réception : la liberté de support retire effectivement cette contrainte dans une relation entre syndicat et employeur, distincte des échanges administratifs du CRPA. Les quatre premiers alinéas sont intégralement conservés, notamment les personnes désignables, les collèges, le plus fort reste et les droits des autres Etats.",
    "D2352-6 à D2352-13 et R2352-18 ont été lus en entier. D2352-7 doit être coordonné pour retirer l'exclusivité du recommandé, sans nouvelle confirmation ; sa réécriture n'est pas prétendue achevée par ce lot. D2352-13 conserve ses destinataires propres et l'information des salariés ; aucune suppression de ces informations n'est déduite du changement de support. R2352-18 conserve les quinze jours à compter de la notification pour la désignation et l'information des salariés pour leur recours ; ses renvois préexistants à R2324-24 et R2324-25 nécessitent une coordination dans ce règlement hors lot, sans les présenter comme une cible actuelle vérifiée. Les notifications nouvelles bénéficient du choix même si la désignation est ancienne ; les notifications accomplies et délais expirés ne sont pas repris. L2353-9 et D2353-2 renvoient au mécanisme de désignation pour le comité de la SE : cette conséquence de coordination est identifiée, sans compter une seconde mesure ni supprimer les voies d'information propres. Le délai contentieux de quinze jours n'est pas le préavis individuel de L1234-1.",
    "La source officielle entière est conservée sauf l'imposition d'une forme réglementaire exclusive à la notification : le nouveau texte rend inopposable le recommandé obligatoire de D2352-7. La réduction porte sur le support et ses frais, non sur la désignation, la notification ou les garanties électorales.",
    "Une seule mesure de liberté de notification est comptée ; le coût net et la fréquence des envois ne sont pas connus. D2352-7 et les anciens renvois contentieux de R2352-18 restent à coordonner dans leurs propres textes.",
    "Aucune charge nouvelle n'est identifiée : la réception datée était déjà prouvée par le recommandé et reste nécessaire aux recours. Aucun nouveau registre, déclaration ou second envoi n'est créé ; les garanties légales de réception électronique restent applicables.",
    proposed=p23525, impact_class='material_reduction', removed=[
        "Exclusivité de la forme réglementaire de notification de la désignation, actuellement la lettre recommandée avec avis de réception prévue par D2352-7, sans suppression de l'information de l'employeur."
    ], effects=[effect(
        'compliance_cost_reduced', 'societe-europeenne-designation-notification-libre',
        "Choix du moyen de notification des désignations au lieu du recommandé obligatoire, avec preuve de réception datée conservée.",
        "L2352-5 impose les conditions réglementaires de notification ; D2352-7 exige une lettre recommandée avec avis de réception pour le syndicat notifiant à l'employeur.",
        "Tout moyen donnant date certaine à la réception peut être utilisé ; recommandé et envoi de confirmation ne sont pas obligatoires ; la notification subsiste.",
        'legal_duty', "Organisations syndicales notifiant à l'employeur les désignations des représentants français relevant de L2352-5.",
        "Notifications à compter de l'entrée en vigueur, même pour désignations anciennes ; aucun renouvellement des notifications régulières ni réouverture des délais expirés.",
        "Preuve de réception et date, déjà assurées par l'avis de réception, maintenues sans registre ou nouveau document imposé ; coût du moyen choisi non chiffré.",
        "La désignation de ces membres est notifiée par l'organisation syndicale à l'employeur dans des conditions déterminées par voie réglementaire.",
        "La lettre recommandée avec avis de réception n'est pas obligatoire et aucun envoi de confirmation n'est exigé.")])

add('L2352-6',
    "Maintien intégral de l'élection directe en l'absence d'organisation syndicale, dans la SE dont le siège est en France comme dans l'implantation française d'une SE. Cette voie protège l'accès à la représentation lorsque la désignation syndicale n'est pas possible. Elle ne crée pas un scrutin supplémentaire à cumuler systématiquement avec celle-ci, et aucun agrément ou rapport périodique autonome n'est identifié à retirer.",
    "L2352-5 et D2352-6 à D2352-12, lus en entier, organisent les voies de désignation ou d'élection selon la présence d'élus et les effectifs ; D2352-10 règle les situations mixtes et D2352-11 le scrutin commun. Les renvois anciens de D2352-11 à R2324-18 et suivants sont une incohérence réglementaire à coordonner hors lot, non une raison de supprimer le scrutin ou ses garanties. Le renvoi du présent article aux règles du CSE demeure pertinent. Ne pas transposer la suppression des transmissions CPPNI ou des délais de négociation L2232 à ce régime de SE, ni attribuer à la durée du mandat un terme d'emploi.",
    "Les deux alinéas de la source restent applicables afin que les futurs salariés éligibles disposent d'une élection directe en l'absence de syndicat. Aucun gain nouveau de fusion de scrutin n'est revendiqué.",
    "Les dispositions réglementaires du scrutin comportent des références historiques à coordonner dans leurs textes propres ; leur correction complète n'est pas réalisée dans ce lot législatif.",
    "Aucune charge nouvelle n'est identifiée : même élection de substitution, sans scrutin additionnel, déclaration, délai d'attente ou condition d'ancienneté créé.")


assert len(ANSWERS) == len(SOURCES) == 24
assert [a['number'] for a in ANSWERS] == [s['number'] for s in SOURCES]
Path('answer.json').write_text(json.dumps(ANSWERS, ensure_ascii=False, indent=2) + '\n')
