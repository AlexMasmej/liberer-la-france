import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answer = []

def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])

def effect(kind, measure, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def retain(number, reason, notes, assessment, limitations):
    a = by_number[number]
    o = {k:a[k] for k in ('code_id','source_id','source_sha256','number')}
    o.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=impact('retained_necessary', assessment, limitations,
                "Aucune charge nouvelle n'est identifiée : le texte source est intégralement maintenu, sans nouvelle donnée, formalité, condition ni échéance."))
    answer.append(o)
    return o

def rewrite(number, xml, reason, notes, assessment, limitations, burdens, effects, removed=None):
    a = by_number[number]
    o = {k:a[k] for k in ('code_id','source_id','source_sha256','number')}
    o.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft',
             substantive_impact=impact('material_reduction' if removed else 'coordination_only',
                                      assessment, limitations, burdens, effects))
    if removed:
        o.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    answer.append(o)
    return o

retain('L382-43',
    "Maintien intégral de l'assimilation des périodes de travail pénitentiaire et de formation pour l'ouverture et le calcul des prestations en espèces. Ce texte ouvre des droits et coordonne les régimes ; il n'institue ni prélèvement accessoire, ni dossier, ni durée minimale d'emploi à supprimer. Retirer cette assimilation pénaliserait les assurés actuels et futurs.",
    "Notes d'entrée en vigueur de l'ordonnance du 19 octobre 2022 lues : le 1er décembre 2024 est une borne historique, non la date de cette réforme. L161-8 et L172-1 à L172-3 conservent respectivement maintien et totalisation/versement interrégimes ; les deux dernières cibles ont aussi été lues dans le corpus public local. Le contrat d'emploi pénitentiaire est distinct du contrat privé. Aucun changement de calcul des indemnités ordinaires de rupture n'en résulte.",
    "La source entière ne comporte qu'une assimilation protectrice et des renvois utiles à la continuité des droits ; aucune baisse de cotisation ou suppression de démarche nouvelle n'est revendiquée.",
    "Les conditions propres à chaque prestation et les règlements de calcul restent applicables ; aucune extension du contrat unique au régime pénitentiaire ni estimation budgétaire n'est établie.")

old = "L'indemnité journalière mentionnée au deuxième alinéa est accordée à l'expiration d'un délai déterminé par décret en Conseil d'Etat à compter du début de l'incapacité temporaire de travail"
new = "L'indemnité journalière mentionnée au deuxième alinéa est accordée dès le premier jour de l'incapacité temporaire de travail, sans délai de carence"
xml = by_number['L382-44']['source_xml'].replace(old, new)
xml += "<p>La suppression du délai de carence s'applique aux journées d'incapacité courant à compter de l'entrée en vigueur de la loi portant cette suppression, y compris lorsque l'incapacité a commencé avant cette date. Le terme réglementaire de la période d'indemnisation n'est ni avancé ni reporté du fait de cette suppression. La règle de non-cumul avec les indemnités journalières de l'assurance maternité demeure applicable. Les prestations afférentes aux journées antérieures, leurs créances, régularisations, prescriptions et recours restent régis par les dispositions antérieures, sans double paiement.</p>"
rewrite('L382-44', xml,
    "Réduction de fond : suppression effective de la carence pour l'indemnité liée aux difficultés médicales de grossesse en détention. La constatation médicale, les conditions de service, le terme réglementaire de l'indemnisation et l'interdiction de cumul maternité demeurent. La carence ne détermine ni le besoin médical ni l'incapacité déjà constatée ; sa suppression ouvre immédiatement la prestation sans agrément ou déclaration de remplacement. L'exclusion générale des autres indemnités maladie en détention n'est pas modifiée par cette mesure ciblée.",
    "R382-136 lu en entier dans le corpus local : son premier alinéa prévoit actuellement un versement à compter du quatrième jour, jusqu'au début de la période du dernier alinéa de L331-5. Coordonner cette première phrase avec le premier jour sans toucher au terme ni au deuxième alinéa, qui retient le plus avantageux des deux calculs (maintien des droits ou activité pénitentiaire). Ce règlement non assigné n'est pas modifié ici. Aucun montant ou taux d'indemnité n'est inventé. L321-1 conserve la constatation médicale ; les propositions de L323-6 ne deviennent pas le droit en vigueur par leur présence dans les cibles. La note de 2022 ne fixe pas l'entrée en vigueur de la présente suppression.",
    "La source entière autorise un délai de carence que R382-136 fixe à trois journées. Le nouveau corps retire cette condition d'attente pour les journées futures couvertes, en conservant la prestation spéciale et toutes ses autres conditions. Il ne s'agit pas d'un simple report de paiement d'une dette inchangée.",
    "Mesure limitée à l'incapacité liée à la grossesse visée au deuxième alinéa ; ni indemnisation générale des maladies en détention ni allongement du terme réglementaire. La dépense de prestations et la coordination de R382-136 restent à évaluer et réaliser.",
    "Aucune charge nouvelle n'est identifiée pour l'assurée : aucun formulaire ni certificat supplémentaire. Les caisses servent plus tôt une prestation selon les mêmes données et contrôles ; le coût public supplémentaire n'est pas chiffré.",
    [effect('deadline_reduced','grossesse-detention-suppression-carence',
        "Suppression de la période initiale non indemnisée de l'incapacité liée à la grossesse en détention.",
        "Carence autorisée par L382-44, de trois jours selon R382-136 : indemnisation à compter du quatrième jour.",
        "Zéro jour de carence : droit dès le premier jour ; montant et terme réglementaires inchangés.",
        'calendar_days',"Personnes détenues empêchées de commencer ou poursuivre un travail pénitentiaire ou un stage pour difficultés médicales liées à leur grossesse.",
        "Journées courant dès l'entrée en vigueur, même pendant une incapacité antérieure ; ancien régime pour les journées antérieures et aucun cumul maternité.",
        "Aucune démarche de remplacement ; même constat médical et mêmes conditions de service ; surcoût de prestations non chiffré.",old,new)],
    ["Suppression du délai initial de carence préalable à l'indemnisation des difficultés médicales de grossesse en détention."])

old = "Les personnes détenues qui remplissent les conditions prévues à l'article L. 313-1 bénéficient du congé et des prestations en espèce de l'assurance maternité dans les conditions prévues aux articles L. 331-3 à L. 331-6."
new = "Les personnes détenues bénéficient du congé et des prestations en espèce de l'assurance maternité dans les conditions prévues aux articles L. 331-3 à L. 331-6. Les conditions prévues à l'article L. 313-1 s'appliquent sous réserve de la dispense expressément prévue à l'article L. 331-6."
rewrite('L382-45', '<p>'+new+'</p>',
    "Coordination nécessaire du renvoi général aux conditions de L313-1 avec la dispense expresse de L331-6 en cas de décès de la mère. Le nouveau corps maintient tout le congé, les prestations et les conditions propres à L331-3 à L331-6 ; il ne subordonne pas le droit transféré au père ou au bénéficiaire subsidiaire à une condition dont la cible les dispense. Il ne crée pas une nouvelle exonération ni une nouvelle réduction d'ancienneté.",
    "Incohérence de lecture préexistante signalée : la source place globalement L313-1 en condition tout en visant L331-6 qui l'écarte expressément. La rédaction rend cette réserve opératoire sans changer les durées de maternité, les reports ou les conditions de cessation du travail. Le renvoi à L313-1 suit sa rédaction applicable ; sa proposition distincte supprimant une durée minimale d'affiliation n'est ni reproduite ni comptée comme une seconde réduction ici. Les transitions historiques des notes de 2006 et 2022 restent à leur objet.",
    "La comparaison avec la source entière révèle une réserve à expliciter pour empêcher que le renvoi général ferme la dispense du droit transféré après décès de la mère. La coordination protège l'avantage existant sans démontrer une nouvelle baisse de prélèvement ou de formalité.",
    "La dispense ne vaut que dans le champ exact de L331-6. Les conditions des autres congés, les durées, les règles de report et les textes réglementaires ne sont pas modifiés par cette coordination.",
    "Aucune charge nouvelle n'est identifiée : la réserve écarte une condition dans le seul cas déjà dispensé et n'ajoute ni demande, justificatif, registre ni délai.",
    [effect('coordination','maternite-detention-dispense-droits-transferes',
        "Explicitation de la priorité de la dispense de L331-6 sur le renvoi général à L313-1.",
        "Condition générale de L313-1 formulée sans réserve, avec renvoi simultané à L331-6.",
        "Même congé et mêmes prestations ; réserve expresse de la dispense déjà inscrite dans L331-6.",'legal_duty',
        "Personnes détenues pouvant relever du transfert de l'indemnisation maternité après décès de la mère.",
        "Clarification du droit préexistant ; aucune fermeture pour les futures situations éligibles, aucun nouveau délai.",
        "Aucun justificatif ni condition de remplacement.",old,new)])

retain('L382-46',
    "Maintien intégral de la base de calcul des indemnités de grossesse et de maternité des personnes détenues. Le renvoi à L323-4 évite un second barème ; il ne constitue ni autorisation ni contribution accessoire. Supprimer cette règle rendrait le montant indéterminé et menacerait les prestations protégées.",
    "L323-4 vise les revenus antérieurs cotisés, leur valeur journalière, une fraction et un plafond réglementaires, sans paramètre chiffré à inventer. La suppression de carence proposée pour L382-44 change l'ouverture temporelle, pas ce calcul. L382-45 conserve ses congés et sa réserve de L331-6. R382-136 maintient le calcul le plus avantageux, lu localement ; il ne doit pas être neutralisé. Note historique de 2022 conservée à son objet.",
    "Le texte entier est une règle commune de calcul, nécessaire pour deux prestations ; aucun double calcul ou prélèvement autonome retirable n'est identifié dans cet article.",
    "Le niveau réglementaire de la fraction et du plafond et le coût de la carence retirée dans un autre article ne sont pas chiffrés ici ; aucune indemnité de rupture du contrat privé n'est concernée.")

retain('L382-47',
    "Maintien intégral des prestations d'invalidité et de décès des détenus et, selon le cas, de leurs ayants droit. Les renvois définissent des droits assurantiels essentiels ; ils ne prélèvent aucun impôt de succession et ne créent aucune procédure redondante dans cet article.",
    "L341-1 et L361-1 lus dans le corpus public local : capacité de travail ou de gain pour l'invalidité ; capital décès au bénéfice des ayants droit, avec les situations d'activité, d'indemnisation ou de maintien des droits prévues. Le capital versé est une prestation, pas le prélèvement sur un capital dénoué par décès que la politique successorale supprime. Ne pas confondre cette prestation avec les droits du CGI. La note d'entrée en vigueur de 2022 demeure historique.",
    "Aucune réduction de charge n'est attribuée à ce maintien : la source complète assure une couverture invalidité-décès et sa disparition supprimerait un avantage essentiel.",
    "Les conditions propres des deux assurances et les droits des ayants droit subsistent ; les droits de mutation, leur abolition et les régimes étrangers ne sont pas réglés par cet article.")

retain('L382-48',
    "Maintien intégral de l'affiliation des travailleurs détenus à la retraite complémentaire, y compris sans régularité de séjour, et de la responsabilité déclarative et contributive de l'Etat. Ces obligations constituent le support des droits à retraite et évitent de les faire porter aux détenus ; leur inutilité n'est pas démontrée et aucun double dépôt n'est prescrit par ce texte.",
    "L921-2-1 et L115-6 lus dans le corpus public local : régime Ircantec et condition de séjour à laquelle l'article déroge expressément. L382-49 conserve la prise en charge des deux parts par l'Etat. Le régime pénitentiaire n'entre pas automatiquement dans la première phase de capitalisation des salariés d'employeurs privés de L241-3 proposé. Note de 2022 : aucune date nouvelle de réforme déduite.",
    "La source entière conserve une dérogation favorable de séjour et l'identification du débiteur des cotisations ; supprimer cette obligation ne prouverait pas une économie sans perte de droits ou transfert de financeur.",
    "Ni taux de retraite complémentaire ni coût des droits ne sont modifiés. Une rationalisation technique des déclarations de l'Etat nécessiterait la preuve d'un doublon extérieur absent de cet article.")

retain('L382-49',
    "Maintien intégral de la prise en charge étatique des cotisations salariales et patronales de retraite complémentaire des détenus. Cette dispense financière pour les personnes affiliées doit rester ouverte aux futures situations ; supprimer le financeur les exposerait à une charge nouvelle ou à une perte de couverture.",
    "Coordination avec L382-48 et son affiliation dérogatoire inchangées. Il s'agit du financement de cotisations existantes, non d'un prélèvement fiscal sur les détenus ni d'une contribution accessoire sans objet. La note de l'ordonnance de 2022 a été lue et reste une transition historique. Aucun transfert vers la capitalisation privée ou compensation budgétaire n'est introduit.",
    "Aucun prélèvement supprimé ou réduit : la source entière met déjà les deux parts à la charge de l'Etat et protège ainsi l'affilié. Son maintien ne compte pas comme un nouvel allègement.",
    "Les taux du régime complémentaire et la dépense de l'Etat demeurent ; aucun solde de financement des retraites ou gain national ne résulte de cet examen.")

retain('L383-1',
    "Maintien intégral de l'habilitation résiduelle déterminant les modalités d'application du livre III, avec décret en Conseil d'Etat sauf disposition contraire. L'article n'impose lui-même ni déclaration, agrément, cotisation, délai d'attente ou justificatif ; son abrogation n'identifierait aucune charge concrètement retirée et fragiliserait les règlements utiles aux prestations.",
    "La formule « en tant que de besoin » n'impose pas un nouveau règlement pour chaque situation. Cette habilitation générale ne permet pas de rétablir une charge expressément supprimée par la loi : les coordinations réglementaires de chaque réforme doivent demeurer ciblées. Pas de note source ni tableau.",
    "La source complète est une habilitation d'exécution, sans charge individuelle autonome à couper. Le maintien est nécessaire à l'application des régimes et ne vaut pas simplification matérielle.",
    "Cet examen ne valide pas toutes les formalités des règlements du livre III ; chacune doit être examinée dans son article propre et aucun gain global n'est établi.")

retain('L411-1',
    "Maintien intégral de la définition protectrice de l'accident du travail, quelle qu'en soit la cause, pour les personnes de L311-2. Aucun prélèvement, délai minimal ou dossier n'est institué. Retirer ou resserrer cette définition supprimerait une protection essentielle, sans allègement de conformité démontré.",
    "Renvoi général aux personnes de L311-2 : aucune condition de CDI, CDD ou d'ancienneté n'y est ajoutée. La note du 14 avril 2023 fixe le 1er septembre 2023 pour sa modification, non une date de la réforme future. L'accident est distinct de la rupture et de son indemnité ordinaire.",
    "Le texte entier définit un risque couvert ; aucune obligation autonome ou cotisation accessoire retirable n'est identifiée et aucune réduction n'est revendiquée.",
    "L'imputabilité, les procédures de reconnaissance et les régimes non visés conservent leur droit ; aucune modification des taux AT-MP ou de la preuve n'est démontrée ici.")

retain('L411-2',
    "Maintien intégral de la couverture des trajets, de l'alternative entre preuve du bénéficiaire et présomptions suffisantes issues de l'enquête, du détour favorable pour covoiturage régulier et des nécessités de la vie courante. La preuve du lien avec le trajet professionnel a une fonction de délimitation du risque ; aucun dossier supplémentaire ni justificatif obligatoire n'est prescrit.",
    "Conserver exactement les deux catégories de trajets : résidence principale, secondaire stable ou lieu familial habituel ; repas pris habituellement hors du travail. L'exception de covoiturage et la qualification des interruptions et détours restent applicables aux situations futures. Il n'est pas exigé de doubler une enquête suffisante par une nouvelle preuve personnelle. Aucun renvoi rendu orphelin par le contrat unique.",
    "La source entière contient déjà une voie probatoire alternative favorable et des exceptions utiles. Les supprimer ou uniformiser tous les trajets ferait perdre la délimitation du risque sans suppression d'une démarche identifiable.",
    "Les critères de trajet et de motif restent contrôlables ; aucun droit nouveau à tous les déplacements privés ni baisse de cotisation n'est établi.")

retain('L412-1',
    "Maintien intégral du champ non agricole des accidents postérieurs au 31 décembre 1946 et des maladies constatées après cette date, sous réserve de L413-12. Cette règle distingue les régimes et protège prévention et réparation ; elle ne crée ni formalité ni prélèvement accessoire à supprimer.",
    "L413-12 est une réserve pour les pensions des ateliers de marine, marins, manufactures d'armes et fonctionnaires ; sa note QPC de 2011 comporte une réserve constitutionnelle qui n'est pas effacée. Le régime agricole et les régimes publics ne deviennent pas ceux du contrat privé. Le 31 décembre 1946 est une frontière historique maintenue.",
    "La source entière délimite une compétence et réserve les régimes distincts ; l'examen ne met en évidence aucune obligation doublonnée et ne revendique aucun allègement.",
    "Aucune harmonisation des pensions publiques, de la protection agricole ou des régimes maritimes n'est opérée ; les réserves constitutionnelles et les règles supérieures ne sont pas écartées.")

retain('L412-2',
    "Maintien intégral de l'accès à la protection AT-MP pour les personnes de L311-3 même hors établissement ou avec leur propre outillage, des conditions particulières des 10° et 17°, et de l'identification de l'employeur par le livre III. Ce texte étend la couverture au-delà d'une forme de contrat et ne contient ni taxe ni second dossier démontré.",
    "L311-3 a été lu dans ses deux versions fournies, notamment ses 10° (garde d'enfants à domicile) et 17° (accueillants familiaux agréés), auxquels seuls s'applique ici la réserve réglementaire. Les options, abattements et statuts assimilés de la cible restent distincts de l'indemnité de licenciement. La note de non-application à Saint-Pierre-et-Miquelon de la loi du 31 décembre 1990 n'est pas supprimée.",
    "La source entière protège un champ d'assurés et définit le débiteur des obligations ; aucune condition nouvelle ni réduction de cotisation ou de procédure n'est attribuée à son maintien.",
    "Les décrets propres aux 10° et 17° et la territorialité restent applicables ; le contrat unique ne convertit pas automatiquement les personnes assimilées en salariés de droit privé.")

retain('L412-3',
    "Maintien intégral de la prise en compte des risques réels chez l'utilisateur pour les ristournes ou cotisations supplémentaires de l'entreprise de travail temporaire, ainsi que des actions réciproques en remboursement. Les ristournes sont favorables et les majorations liées aux risques exceptionnels conservent une fonction essentielle de prévention ; l'article n'instaure ni déclaration périodique ni agrément.",
    "L242-7 distingue ristournes de prévention et cotisations supplémentaires pour risques exceptionnels. Sa proposition supprime seulement le minimum forfaitaire et corrige les recours ; cette mesure n'est pas répliquée ni recomptée ici. Les missions peuvent être limitées dans le temps sans limiter l'emploi nouveau ; les remboursements entre entreprises ne sont pas l'indemnité ordinaire de rupture.",
    "La source entière articule risques, allègements et responsabilité financière entre deux entreprises ; aucune nouvelle suppression matérielle n'est démontrée dans cette disposition de coordination.",
    "Les taux de tarification et cotisations pour risques graves restent à leur champ. Aucun gain du retrait du minimum dans L242-7 n'est compté une deuxième fois ; son adoption n'est pas présumée.")

old = "Sans préjudice des obligations qui lui incombent à l'égard de son employeur en exécution des dispositions de l'article L. 441-1, la victime d'un accident du travail doit en informer ou en faire informer l'utilisateur."
new = "La victime d'un accident du travail informe ou fait informer l'utilisateur dans le délai prévu à l'article L. 441-1, sous les réserves de force majeure, d'impossibilité absolue ou de motifs légitimes prévues au même article. Cette information vaut information de son employeur pour l'application de cet article ; aucune information distincte de l'employeur ne peut être exigée de la victime au titre du même accident."
xml = by_number['L412-4']['source_xml'].replace(old,new)
xml += "<p>La dispense de seconde information s'applique aux accidents survenus à compter de l'entrée en vigueur de la loi portant cette dispense. Elle s'applique également aux informations restant à accomplir à cette date pour un accident antérieur, sans obligation de renouveler une information déjà régulièrement donnée. Elle ne modifie ni la déclaration de l'accident à la caisse par l'employeur, ni les obligations d'information de l'utilisateur prévues au deuxième alinéa. Les droits à réparation, prescriptions et recours sont conservés, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives.</p>"
rewrite('L412-4',xml,
    "Réduction de fond : le signalement effectué à l'utilisateur libère la victime du second signalement à l'entreprise de travail temporaire. L'utilisateur conserve sa transmission à cette entreprise au deuxième alinéa, et celle-ci sa déclaration à la caisse ; aucun signalement ou registre de remplacement n'est créé. Les exceptions légitimes au délai sont explicitées et le lieu de travail comprenant le siège et les lieux de mission est intégralement conservé.",
    "L441-1 et L441-2, R412-1 et R412-2 lus dans le corpus local. Coordonner R412-1 pour rendre la dispense de seconde information effective ; son délai de vingt-quatre heures et les formes du signalement unique ne sont pas réécrits dans ce lot. R412-2 conserve la transmission existante sous vingt-quatre heures à l'entreprise, au service de prévention et à l'inspection : aucune suppression de ces destinataires n'est décidée. Le deuxième alinéa reste exactement à sa place pour L412-5 ; le troisième conserve le trajet de L411-2. L412-9 étend ces règles aux catégories qu'il vise. Ni durée de mission ni signalement d'accident ne constituent un terme de l'emploi nouveau.",
    "La source entière cumule expressément l'information de l'employeur et celle de l'utilisateur par la victime. La nouvelle règle supprime l'exigence de deux signalements pour le même accident en réutilisant la transmission déjà imposée à l'utilisateur ; elle ne réduit pas les cotisations ni les réparations.",
    "Les déclarations de l'employeur à la caisse, les transmissions de sécurité de l'utilisateur et leurs délais restent. L'effet est limité au signalement de la victime ; le règlement R412-1 doit être coordonné, sans prétendre à une baisse nette de coût de tout le système.",
    "Aucune charge nouvelle n'est identifiée : la victime utilise le signalement déjà dû à l'utilisateur, dont la transmission à l'employeur était déjà obligatoire. Aucune donnée, déclaration de remplacement ou registre supplémentaire n'est ajouté.",
    [effect('obligation_merged','accidents-interim-information-unique-victime',
        "Fusion des deux informations initiales dues par la victime ; le signalement à l'utilisateur libère de l'information séparée de l'employeur.",
        "Deux informations distinctes par la victime, à son employeur selon L441-1 et à l'utilisateur selon L412-4, pour le même accident.",
        "Un signalement à l'utilisateur vaut également information de l'employeur ; transmission par l'utilisateur et déclaration à la caisse maintenues.",
        'legal_duty',"Victimes mises à disposition par une entreprise de travail temporaire ; catégories auxquelles L412-9 applique cette règle.",
        "Accidents nouveaux et informations restant dues lors de l'entrée en vigueur ; informations déjà accomplies non renouvelées, droits et recours conservés.",
        "Aucune obligation de remplacement ; la transmission de l'utilisateur existe déjà. Délai et garanties des déclarations de sécurité conservés.",old,new)],
    ["Suppression, pour la victime ayant informé l'utilisateur, de l'information distincte de son employeur au sujet du même accident."])

retain('L412-5',
    "Maintien intégral du recours de la caisse contre l'utilisateur qui omet la transmission à l'entreprise de travail temporaire. Cette responsabilité garantit la déclaration et la protection de la victime ; elle n'est pas un prélèvement automatique ni la répétition d'une information déjà accomplie. Supprimer le recours déresponsabiliserait le détenteur de l'information de sécurité.",
    "Le deuxième alinéa de L412-4 reste l'obligation de l'utilisateur après la fusion du premier signalement de la victime. Le renvoi ordinal est donc conservé exactement. Le deuxième alinéa de L471-1 porte sur le recouvrement des dépenses et la pénalité après défaut des obligations déclaratives, non sur le préavis ou l'ancienneté du salarié. Les sanctions de situations régulières ne sont pas étendues ; la loi répressive plus douce s'applique dans son champ.",
    "La source complète étend un recours existant au responsable réel d'une omission. Aucun nouveau retrait de charge n'est démontré ; la fusion du signalement de la victime est comptée seulement dans L412-4.",
    "Le recours reste limité à la violation du deuxième alinéa de L412-4 ; aucune responsabilité nouvelle de la victime ni suppression des garanties de contestation n'est opérée.")

old = "Ce dernier demeure tenu des obligations prévues audit article sans préjudice de l'action en remboursement qu'il peut exercer contre l'auteur de la faute inexcusable."
new = "Ce dernier demeure tenu des obligations prévues aux articles L. 452-1 à L. 452-4 sans préjudice de l'action en remboursement qu'il peut exercer contre l'auteur de la faute inexcusable."
rewrite('L412-6',by_number['L412-6']['source_xml'].replace(old,new),
    "Coordination du renvoi ambigu « audit article » alors que le début vise quatre articles : les obligations de l'employeur sont explicitement celles de L452-1 à L452-4. La substitution de l'utilisateur dans la direction, la dette envers la victime et le recours contre l'auteur de la faute inexcusable sont intégralement maintenus. Aucune réduction de réparation ou de sanction de sécurité n'est décidée.",
    "Ambiguïté préexistante signalée et levée expressément, sans déplacer d'alinéa. Les cibles fournies L452-2 (majoration), L452-3 (préjudices et versement par la caisse) et L452-4 (accord, juge, assurance et garanties) confirment l'objet pluriel de la règle. Les réserves QPC et les dates d'application des notes ne sont pas supprimées. La dette AT-MP ne relève pas du barème de l'indemnité ordinaire de licenciement.",
    "Le seul changement par rapport à la source complète est l'identification explicite des articles auxquels renvoie la dette de l'employeur. Il ne supprime ni cotisation, ni obligation de sécurité, ni indemnité et ne vaut pas simplification matérielle chiffrée.",
    "Les conséquences de la faute inexcusable et les voies de recours restent à leur champ ; aucune réforme des montants de rente, de l'assurance ou des règles constitutionnelles n'est opérée.",
    "Aucune charge nouvelle n'est identifiée : le renvoi pluriel désigne le même ensemble de règles déjà visé au début de l'article, sans nouvelle procédure, donnée ni délai.",
    [effect('coordination','accidents-interim-faute-inexcusable-renvoi',
        "Correction explicite du singulier dépourvu de cible unique dans le renvoi aux obligations de l'employeur.",
        "Obligations indiquées par « audit article » après une référence à L452-1 à L452-4.",
        "Désignation de L452-1 à L452-4, sans changement de débiteur, de réparation ou de recours.",
        'legal_duty',"Employeurs de travail temporaire, utilisateurs, victimes et ayants droit en cas de faute inexcusable.",
        "Coordination de lecture du même régime ; droits, créances, réserves constitutionnelles et régimes historiques demeurent.",
        "Aucune obligation de remplacement ni formalité nouvelle.",old,new)])

retain('L412-7',
    "Maintien intégral de la substitution de l'utilisateur, de son chef ou de ses préposés en cas de faute intentionnelle. Cette protection permet réparation de droit commun et recours des caisses contre l'auteur réel ; elle est essentielle et ne contient ni autorisation, ni double déclaration, ni prélèvement accessoire retirable.",
    "L452-5 maintient le complément de réparation, les prestations versées par la caisse, son action en remboursement et la constitution des rentes ainsi que la prévention. La réserve QPC de 2010 demeure. Ne pas assimiler une faute intentionnelle à une rupture ordinaire plafonnée à six mois ; aucun seuil d'un an ni préavis privé ne limite ces droits.",
    "La source entière répartit la responsabilité d'un dommage intentionnel ; son maintien ne constitue aucune nouvelle baisse de charge et protège les victimes et le recouvrement contre le responsable.",
    "Les modalités propres à L452-5 et les régimes de faute distincts restent ; aucun changement des rentes, du délai de constitution ou des risques professionnels n'est revendiqué.")

# L412-8 : conserver chaque paragraphe et chaque subdivision hors des renvois corrigés.
xml = by_number['L412-8']['source_xml']
old_c = "c. les personnes effectuant des stages de formation professionnelle continue conformément aux dispositions du livre IX du code du travail, y compris les personnes détenues effectuant de tels stages, pour les accidents survenus par le fait ou à l'occasion de cette formation y compris si cette formation est effectuée par des salariés en partie hors du temps de travail dans les conditions fixées par les articles L6321-2 à L6321-12, L6331-26, L. 6331-69, D6321-4, D6321-5 et D6321-8 et L. 932-2 du code du travail ;"
new_c = "c. les personnes effectuant des stages de formation professionnelle continue au sens de l'article L. 6311-1 du code du travail, y compris les personnes détenues effectuant de tels stages, pour les accidents survenus par le fait ou à l'occasion de cette formation, y compris si cette formation est effectuée par des salariés en partie hors du temps de travail dans les conditions fixées par les articles L. 6321-6 à L. 6321-12 du code du travail. Les accidents survenus à l'occasion de formations relevant, à leur date, des dispositions antérieures du livre IX ou des articles L. 6321-2 à L. 6321-12, L. 6331-26, L. 6331-69, D. 6321-4, D. 6321-5, D. 6321-8 et L. 932-2 du même code demeurent couverts selon les dispositions qui leur sont applicables ;"
assert old_c in xml
xml = xml.replace(old_c,new_c)
old_f = "n'entrant pas dans le cadre de la formation professionnelle continue telle que définie par le livre IX du code du travail"
new_f = "n'entrant pas dans le cadre de la formation professionnelle continue au sens de l'article L. 6311-1 du code du travail"
assert old_f in xml
xml = xml.replace(old_f,new_f)
old_9 = "9° les salariés accomplissant un stage de formation dans les conditions prévues par les articles L4523-10 et L4614-14 à L4614-16, L2325-44 et R2325-8 et L2145-1, et L. 2145-5 à L. 2145-9 du code du travail, pour les accidents survenus par le fait ou à l'occasion de cette formation ;"
new_9 = "9° les salariés accomplissant un stage de formation dans les conditions prévues par les articles L. 4523-10, L. 2315-18, L. 2315-63, L. 2145-1 et L. 2145-5 à L. 2145-9 du code du travail, pour les accidents survenus par le fait ou à l'occasion de cette formation. Les accidents survenus à l'occasion des formations relevant, à leur date, des articles L. 4614-14 à L. 4614-16, L. 2325-44 et R. 2325-8 du même code demeurent couverts selon les dispositions qui leur sont applicables ;"
assert old_9 in xml
xml = xml.replace(old_9,new_9)
old_12 = "Les salariés désignés, dans les conditions définies aux articles L3142-51 à L3142-66 du code du travail, pour siéger dans une instance instituée par une disposition législative ou réglementaire auprès d'une autorité de l'Etat"
new_12 = "Les salariés désignés, dans les conditions définies aux articles L. 3142-60 à L. 3142-66 du code du travail, pour siéger dans une instance instituée par une disposition législative ou réglementaire auprès d'une autorité de l'Etat"
assert old_12 in xml
xml = xml.replace(old_12,new_12)
xml += "<p>Pour les seules activités relevant d'un contrat de travail de droit privé conclu à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, la couverture prévue au présent article reste ouverte dans les conditions propres à chaque catégorie. Une durée de formation, de mission, de mise en situation ou d'accompagnement ne fixe pas le terme de l'emploi. Le présent article n'autorise ni la conclusion ni le renouvellement d'un contrat de travail à durée déterminée après cette entrée en vigueur. Les contrats antérieurs, leur ancienneté et leurs droits acquis conservent leur régime transitoire. Les stages sans contrat de travail, le contrat d'emploi pénitentiaire et les régimes publics demeurent distincts. Les corrections de renvois ne remettent en cause ni la couverture des accidents antérieurs, ni les droits, créances, prescriptions et recours correspondants.</p>"
o = rewrite('L412-8',xml,
    "Coordination nécessaire, sans suppression de couverture : actualiser les références de formation continue, de formation des représentants du personnel et de congé de représentation ; préserver expressément les formations anciennes et l'accès des futures situations éligibles dans le contrat unique. Toutes les catégories 1° à 19°, y compris 14° bis, les exclusions, réserves, bases et répartitions d'obligations sont maintenues. Les stages non salariés et les régimes pénitentiaires ou publics ne deviennent pas artificiellement des emplois privés. Aucun coût de réparation essentiel n'est retranché sous couvert de baisse de charges.",
    "Lecture locale complémentaire des textes officiels L6311-1, L6321-2,3,6 à12, L6331-69, L2315-16,18,63, L3142-60 à66 et L323-3-1. Nouveaux renvois non fournis comme cibles dans reference-targets : L6311-1, L2315-18 et L2315-63 ; ils sont documentés par travail.json du corpus public, sans ajout à reference_checks. Le livre IX et les anciens articles CHSCT/CE ne gouvernent plus les nouvelles formations ; leurs accidents anciens restent couverts. L6331-69 actuel traite d'une contribution de financement de 0,30 %, qui n'est pas supprimée par la correction du renvoi de couverture. L3142-60 à66 règle la représentation ; les dispositions 51 à59 ont d'autres objets : ne pas leur attribuer un emploi déterminé. Le 12° conserve le champ de l'autorité de l'Etat, sans extension implicite à toute instance territoriale. Le cinquième alinéa de L433-1 rend bien L323-3-1 applicable : le renvoi ordinal du 3° reste valable et est donc maintenu, avec les règles d'accord médical et de compatibilité des formations ; la limite d'indemnisation prévue pour certains sinistres de 2027 ne devient pas une durée d'emploi. Incohérence documentaire de la cible L262-1 : celle fournie est le CSS relatif à la prévention, alors que le 10° renvoie au L262-1 du CASF instituant le RSA ; aucune substitution de code. La note source 2025 reste historique. La fiche source de L412-8 porte l'état ABROGE_DIFF et une fin de version au 1er janvier 2029 ; cette métadonnée ne démontre pas l'abolition de toutes les couvertures à cette date. La rédaction future et son acte de coordination ne sont pas fournis dans ce lot : leur concordance, notamment les références pénales, reste à contrôler, sans inventer un texte successeur ni fermer les droits futurs. Les articles extérieurs des codes de la recherche, du sport, du service national, de commerce et du CASF restent à leur champ ; pas de prétention de réécriture de ces codes.",
    "La source complète ouvre une couverture AT-MP à de nombreuses catégories et contient des références obsolètes de formation et de représentation. Les corrections conservent les protections et empêchent un renvoi indirect de rétablir de nouveaux CDD. Aucune seconde suppression d'un régime de contrat ni d'une contribution de financement n'est comptée dans cet article.",
    "Coordination uniquement : pas de baisse de taux ou de base des cotisations, pas de suppression de condition de séjour du 5° ni de l'exclusion L434-1 pour a, b et f. Les décrets de chaque catégorie, le CASF et les textes extérieurs gardent leur champ. La concordance avec la version annoncée au 1er janvier 2029 reste documentairement à établir ; aucun solde global n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les catégories, conditions de couverture et débiteurs des obligations restent ; aucune attestation, autorisation ou déclaration de remplacement n'est ajoutée. L'activité privée relève de la réforme du contrat unique déjà coordonnée ailleurs, sans étendre celle-ci aux stages non salariés ou aux régimes publics.",
    [effect('coordination','accidents-travail-renvois-formation-actualisation',
        "Actualisation du fondement de la formation continue et des formations hors temps de travail, avec maintien des accidents anciens.",
        "Livre IX et liste mêlant textes de formation, anciens règlements et disposition actuelle de financement.",
        "Définition de L6311-1 et conditions pertinentes de L6321-6 à12 ; accidents des anciennes formations préservés.",
        'regime',"Stagiaires de formation continue, y compris personnes détenues et salariés formés hors temps de travail.",
        "Couverture maintenue des formations anciennes et nouvelles ; aucune fin automatique du contrat unique à la fin de la phase pédagogique.",
        "Aucune nouvelle pièce, aucun droit social retiré, aucune suppression du prélèvement autonome de L6331-69.",old_c,new_c),
     effect('coordination','accidents-travail-renvois-formation-actualisation',
        "Actualisation des formations CHSCT/CE vers les formations CSE, sans effacer les accidents des anciennes formations.",
        "Renvois notamment à L4614-14 à16, L2325-44 et R2325-8 pour les anciens organes.",
        "Renvois à L2315-18 et L2315-63 pour les formations actuelles ; anciennes formations expressément protégées.",
        'regime',"Salariés en formation de santé-sécurité, économique ou syndicale, selon les conditions de chaque dispositif.",
        "Aucune rétroactivité défavorable aux formations anciennes ; conditions et durées des formations ne deviennent pas celles de l'emploi.",
        "Aucune formalité ou coût de formation supplémentaire institué par cet article.",old_9,new_9),
     effect('coordination','accidents-travail-renvoi-conge-representation',
        "Rattachement précis du 12° aux dispositions actuelles du congé de représentation.",
        "Plage L3142-51 à66 mêlant plusieurs congés.",
        "Plage L3142-60 à66 correspondant au congé de représentation ; maintien du champ Etat et des autres bénéficiaires du 12°.",
        'regime',"Salariés désignés pour siéger auprès d'une autorité de l'Etat dans les conditions du 12°.",
        "Même objet de mission et droits antérieurs conservés ; les régimes spéciaux et missions syndicales restent distincts.",
        "Aucun agrément, justificatif ni délai nouveau.",old_12,new_12)])
o['benefit_review'] = "Tous les avantages de couverture sont conservés pour les situations futures recevables : 1° délégués mineurs ; 2° a élèves techniques, b autres élèves et étudiants en ateliers/laboratoires ou stages, c formation continue et détenus, d allocations de reclassement, e CSP, f stages non salariés, g doctorants et chercheurs étrangers ; 3° réadaptation, rééducation et actions pendant l'arrêt, assurés L324-1, invalides et stagiaires ONAC ; 4° pupilles ; 5° travail pénitentiaire sous sa réserve de séjour, TIG et travail non rémunéré pénal ; 6° bénévoles d'organismes sociaux ; 7° instances administratives ou paritaires ; 8° marins et faute inexcusable ; 9° formations des représentants et syndicats ; 10° RSA ; 11° actions prescrites de création ou recherche d'emploi ; 12° représentation et missions syndicales ; 13° service civique ; 14° appui à la création/reprise ; 14° bis aide bénévole au repreneur ; 15° volontaires pour l'insertion ; 16° mandats locaux ; 17° entrepreneurs salariés ou associés ; 18° sportifs de haut niveau ; 19° mises en situation handicap. Les qualifications, conditions d'accident, non-cumuls et décrets propres à chaque catégorie restent. Le plafond de champ excluant certains enseignements commerciaux et l'exclusion de l'indemnité en capital L434-1 pour a, b et f ne sont pas des avantages : ils restent des limites du régime, sans extension silencieuse. Les bases spéciales des cotisations et indemnités des personnes sans rémunération normale restent intactes, comme la désignation du débiteur ; aucun taux d'exonération n'est retiré. Les anciens stages restent couverts, et les actions de formation et de reclassement demeurent accessibles dans les futurs contrats uniques sans transformer leur durée pédagogique en terme d'emploi. Les garanties de faute inexcusable et les assimilations de risques sont maintenues."

old_1 = "groupements d'employeurs mentionnés au chapitre VII du titre II du livre premier du code du travail"
new_1 = "groupements d'employeurs mentionnés à l'article L. 1253-1 du code du travail"
old_2 = "associations intermédiaires mentionnées à l'article L. 128 (1) du code du travail"
new_2 = "associations intermédiaires mentionnées à l'article L. 5132-7 du code du travail"
xml = by_number['L412-9']['source_xml'].replace(old_1,new_1).replace(old_2,new_2)
xml += "<p>Ces coordinations de références s'appliquent à compter de l'entrée en vigueur de la loi qui les prévoit, sans remettre en cause les droits, obligations, créances et recours afférents aux accidents et maladies antérieurs. Elles ne modifient ni le champ du régime général et du régime agricole, ni l'application des règles spéciales prévues aux articles L. 412-3 à L. 412-7.</p>"
rewrite('L412-9',xml,
    "Coordination nécessaire de deux références devenues obsolètes : identification actuelle des groupements d'employeurs et associations intermédiaires. Les deux régimes AT-MP, les entreprises membres et les règles spéciales de L412-3 à L412-7 restent intacts, notamment la fusion du signalement de la victime proposée dans L412-4. Aucune seconde réduction de formalité n'est comptée ici.",
    "La note source mentionne expressément l'abrogation de L128 par la loi du 29 juillet 1998 : elle est signalée, non ignorée. Nouveaux renvois L1253-1 et L5132-7 non fournis comme cibles dans reference-targets, lus en entier dans travail.json du corpus public local : mise à disposition par groupements sans but lucratif ; associations intermédiaires conventionnées de l'insertion. Aucun contenu des dispositions de ces cibles n'est inventé ou réécrit. Leurs éventuels renvois anciens au temps partiel sont distincts et ne rétablissent pas le plancher supprimé dans la réforme propre du travail. Les obligations de l'utilisateur et de prévention restent ; le régime agricole n'est pas absorbé par le contrat privé.",
    "La source complète comporte des renvois à une ancienne structure du code du travail et à un article abrogé. Leur actualisation rétablit une identification opératoire des mêmes catégories, sans démontrer une réduction supplémentaire de taxe ou d'obligation.",
    "Les textes réglementaires de tarification et les coordinations du code rural restent hors de ce lot. La fusion du signalement de L412-4 est une seule mesure et n'est pas une seconde obligation supprimée dans L412-9.",
    "Aucune charge nouvelle n'est identifiée : les mêmes acteurs restent soumis aux mêmes règles spéciales ; les références actualisées ne créent ni convention supplémentaire, ni déclaration, ni registre ou délai.",
    [effect('coordination','accidents-travail-groupements-renvois-actualisation',
        "Actualisation des références identifiant groupements d'employeurs et associations intermédiaires.",
        "Chapitre VII du titre II du livre premier et L128 abrogé.",
        "L1253-1 et L5132-7 pour les mêmes catégories ; règles L412-3 à L412-7 et régimes général/agricole conservés.",
        'regime',"Groupements d'employeurs, entreprises membres, associations intermédiaires et leurs salariés.",
        "Coordination prospective sans remise en cause des droits, obligations et créances relatifs aux sinistres antérieurs.",
        "Aucun dépôt ou agrément supplémentaire institué par cette actualisation.",old_2,new_2)])

retain('L413-1',
    "Maintien intégral de la possibilité de bénéficier des règles nouvelles pour les accidents postérieurs au 31 décembre 1946 initialement exclus, avec effet au dépôt de la demande, substitution pour l'avenir et imputation des réparations de droit commun. La demande matérialise l'exercice d'une option qui peut remplacer d'autres prestations ; la supprimer au profit d'une substitution automatique pourrait retirer un avantage sans consentement.",
    "R413-1 lu localement en entier : imprimé, pièces, questionnaire et récépissé ainsi que conversion des réparations et rachats. Ce règlement peut appeler un examen propre des pièces exhaustives et du support imposé, mais une simple reprise du droit CRPA de réemploi ne constitue pas ici une suppression nouvelle. Aucune pièce redondante précise n'est exigée par L413-1 lui-même. Maintenir l'effet à la demande, la substitution future, l'imputation éventuellement revalorisée et les droits des ayants droit ; ne pas prétendre abroger ces mécanismes par une reformulation.",
    "La source entière porte un avantage d'accès aux règles plus favorables et des garde-fous contre le double paiement. Aucune nouvelle suppression de charge n'est établie dans cet article ; le maintien ne vaut pas validation des formalités réglementaires extérieures.",
    "Le champ historique et l'effet au dépôt demeurent. L'examen de R413-1 n'est pas présenté comme sa réécriture ; ni remboursement rétroactif général ni fusion automatique de prestations n'est créé.")

retain('L413-2',
    "Maintien intégral de l'allocation pour les accidents et maladies non agricoles antérieurs au 1er janvier 1947 initialement exclus, y compris les ayants droit, et du seuil d'incapacité pour l'attribution à la victime. La preuve concerne l'éligibilité réelle, sans imposer un support ou une répétition documentaire ; supprimer l'allocation en raison de son ancienneté retirerait des droits encore invocables.",
    "R413-2 et R413-3 lus localement : seuil de 10 %, allocation calculée selon L434-2 et L434-7 sur le salaire minimum de L434-16, effet à la demande. Ces paramètres ne sont pas remplacés par un taux inventé. La note renvoie à L754-4 pour les spécificités DOM ; elle demeure. Le seuil vise l'attribution à la victime et ne doit pas devenir une condition autonome ajoutée aux ayants droit.",
    "La source complète est un dispositif historique de réparation favorable, non un prélèvement ni une autorisation. Ses conditions probatoires et médicales délimitent l'allocation ; aucun doublon concret ne peut être retiré de cet article sans modifier l'éligibilité.",
    "Seuls accidents et maladies antérieurs à 1947 sont couverts ici ; l'absence éventuelle de nouveaux dossiers ne prouve pas l'extinction des droits. Aucune économie ou suppression de prestations n'est revendiquée.")

retain('L413-3',
    "Maintien intégral de la fourniture, de la réparation et du renouvellement des prothèses ou appareils d'orthopédie des titulaires de L413-2. Le besoin lié à l'infirmité est une condition médicale utile ; l'article n'exige ni agrément distinct, justificatif périodique automatique ni paiement accessoire à supprimer.",
    "Conserver les trois droits matériels, sans réduire le renouvellement à la seule fourniture initiale. Le renvoi technique au livre IV n'autorise pas un formulaire ou une autorisation supplémentaire inventés. Le caractère historique de l'allocation support n'éteint pas les besoins futurs d'appareillage des bénéficiaires.",
    "La source entière attribue un avantage en nature essentiel, sans procédure doublonnée identifiable. Son maintien intégral n'est ni une réécriture ni une nouvelle réduction de prélèvement.",
    "Les règles techniques d'appareillage et le droit à l'allocation support restent applicables ; aucune extension à tous les soins ni évaluation de dépense globale n'est opérée.")

retain('L413-4',
    "Maintien intégral du complément portant la rente au taux d'incapacité totale et de la prestation de tierce personne pour les sinistres du 1er juillet 1945 au 31 décembre 1946 aggravés après l'ancien délai de révision. Les trois points de preuve délimitent cet avantage ; le premier dispense déjà de refaire constater une incapacité totale antérieurement reconnue. Supprimer la causalité ou le besoin d'assistance ne serait pas retirer un justificatif redondant, mais changer le risque assuré.",
    "Les deux énumérations 1°/2° puis 1°/2°/3° restent à leur place. Conserver toutes les dates, le dépassement du délai de l'article 19 de la loi du 9 avril 1898 et la dispense de nouvelle constatation du premier point de preuve. L434-2 protège la prestation de tierce personne, ses besoins évalués et sa revalorisation ; aucun gel de pensions du projet retraite ne s'y applique. R413-4 lu localement fixe la prise d'effet à la demande ; pas de rétroactivité créée.",
    "La source entière ouvre deux avantages malgré l'expiration d'un délai ancien et comporte déjà une dispense de preuve pour l'incapacité constatée. Aucune pièce supplémentaire ni prélèvement accessoire ne peut être isolé dans ce texte ; aucun nouvel allègement n'est compté.",
    "Le régime demeure limité aux sinistres de la période indiquée et aux aggravations remplissant ses conditions ; les évaluations médicales et la causalité subsistent. Aucun nouveau barème ni coût national n'est établi.")

retain('L413-5',
    "Maintien intégral de l'allocation du conjoint survivant en cas de décès imputable à un sinistre antérieur à 1947, survenu après le délai ancien. Le lien direct de causalité est essentiel ; sa mention répétée décrit la même condition et ne crée pas deux dépôts distincts à fusionner. Le calcul favorable au salaire minimum et l'accès malgré le délai expiré sont conservés.",
    "L434-8 et L434-16 lus dans le corpus local : les quatre premiers alinéas de L434-8 concernent les conditions de rente, séparation ou divorce, ex-partenaire et concours d'un nouveau conjoint ; le sixième alinéa de complément n'est pas silencieusement ajouté. L413-5 désigne le conjoint survivant, sans extension implicite à toutes les catégories de la cible. Le salaire minimum de L434-16 et les dates pré-1947 demeurent. Une allocation décès est un avantage social, pas un droit de succession supprimé par le CGI.",
    "La source entière protège un survivant malgré l'expiration du délai de la loi de 1898 et fixe une base minimale. L'examen ne révèle ni double démarche exigible ni prélèvement à retirer ; le maintien n'est pas compté comme une réduction nouvelle.",
    "Champ du conjoint et sinistres historiques inchangés ; le renvoi limité aux quatre premiers alinéas et la preuve d'imputabilité demeurent. Aucun impôt au décès, effet budgétaire global ou extension de population n'est réglé ici.")

# Contrôles de cibles : analyses individualisées pour chaque couple article/cible.
contexts = {
 'L382-43':("la totalisation des périodes de travail pénitentiaire et de formation pour les prestations", True),
 'L382-44':("l'indemnité des difficultés médicales de grossesse en détention", True),
 'L382-45':("le congé et les prestations de maternité des personnes détenues", True),
 'L382-46':("le calcul des indemnités journalières de grossesse et de maternité en détention", True),
 'L412-1':("le champ historique non agricole de la prévention et de la réparation AT-MP", False),
 'L412-2':("la couverture AT-MP des personnes assimilées énumérées à L311-3", False),
 'L412-3':("les ristournes et cotisations de risque réparties entre entreprise de travail temporaire et utilisateur", False),
 'L412-4':("le signalement de l'accident par la victime et la transmission par l'utilisateur", False),
 'L412-5':("le recours de la caisse contre l'utilisateur défaillant dans la transmission de l'accident", False),
 'L412-6':("les réparations pour faute inexcusable et le recours contre l'utilisateur auteur de cette faute", False),
 'L412-7':("la réparation et les recours pour faute intentionnelle de l'utilisateur ou de ses préposés", False),
 'L412-8':("les couvertures AT-MP des stagiaires, personnes en reclassement et autres bénéficiaires spéciaux", False),
 'L412-9':("l'application des règles AT-MP aux groupements d'employeurs et associations intermédiaires", False),
 'L413-4':("les compléments de rente et la prestation de tierce personne pour les sinistres de 1945-1946", False),
}
specific = {
 ('L382-43','L172-1'):"L172-1 porte le versement global des indemnités maladie/maternité entre régime général et salariés agricoles et leur compensation. Le renvoi ne change ni débiteur de l'emploi pénitentiaire ni délai de rupture ; aucune ancienneté ou notification de licenciement n'est exigée pour cette totalisation, dont L172-2 et L172-3 gardent les règles propres.",
 ('L382-43','L161-8'):"L161-8 maintient les prestations en espèces après cessation des conditions d'activité, sous résidence/séjour et jusqu'à une nouvelle ouverture de droits, avec prolongation chômage et cas d'indemnités nulles ou faibles. Le renvoi protège les sorties de détention sans importer le préavis privé ni son ancienneté ; la proposition fournie ne réduit pas ces avantages futurs.",
 ('L382-44','L321-1'):"L321-1 vise la constatation de l'incapacité par les professionnels compétents, avec les règles de prescription et l'exception des cures. Ce renvoi de constatation médicale subsiste après retrait de la carence ; la grossesse ne doit pas être subordonnée à une ancienneté ou une notification de rupture du contrat privé. La note d'effet immédiat de 2025 reste distincte de la réforme.",
 ('L382-44','L323-6'):"L323-6 fixe les prescriptions et contrôles de l'arrêt, l'information de reprise et d'adresse, les restitutions volontaires et l'exception des élus locaux. Sa proposition retire les heures de sortie et certaines doubles informations, sans modifier le besoin médical. L382-44 suit sa version applicable sans recréer ces obligations ; aucun préavis ou seuil d'un an ne s'y substitue.",
 ('L382-45','L331-3'):"L331-3 fixe notamment six semaines avant et dix après, les durées de naissances multiples, huit semaines minimales d'arrêt et les protections de prématurité/hospitalisation. L382-45 conserve ce champ entier ; les jours de préavis et le seuil de l'indemnité ordinaire n'altèrent ni congé ni ancienneté d'assurance pertinente. La note spéciale de 2006 reste à son objet.",
 ('L382-45','L331-5'):"L331-5 permet le report après hospitalisation jusqu'à la sixième semaine et prévoit jusqu'à deux semaines supplémentaires sur prescription, avec la réserve de la période de prématurité. Ces avantages demeurent pour les détenues éligibles futures ; la durée du congé n'est pas celle d'un contrat nouveau et aucune notification de rupture ne conditionne ces reports.",
 ('L382-45','L331-6'):"L331-6 transfère après décès de la mère l'indemnisation restante au père qui cesse son travail, sans conditions L313-1, avec report et bénéficiaire subsidiaire. Le nouveau L382-45 réserve expressément cette dispense pour lever l'ambiguïté du renvoi général ; ni ancienneté d'un an ni préavis de rupture ne peut la refermer, et les bénéficiaires futurs restent couverts.",
 ('L382-45','L313-1'):"L313-1 exige rémunérations cotisées ou heures sur une période de référence ; son II officiel ajoute l'affiliation minimale, que sa proposition retire pour les périodes futures avec transition. Le renvoi de L382-45 reste à la rédaction applicable, sous la dispense de L331-6 ; cette affiliation n'est pas l'ancienneté d'emploi d'un an et aucune suppression supplémentaire n'est recomptée ici.",
 ('L382-46','L323-4'):"L323-4 calcule l'indemnité à partir des revenus antérieurs cotisés, de leur valeur journalière, d'une fraction et d'un plafond réglementaires ; la note distingue les arrêts selon juillet 2020 et trente jours. Le renvoi de L382-46 est conservé et ne fixe ni ancienneté de licenciement ni montant de rupture. Il n'est pas neutralisé par le retrait de carence dans L382-44.",
 ('L382-46','L382-44'):"La cible officielle L382-44 ouvre l'indemnité liée à la grossesse avec constatation, conditions L323-6, carence et non-cumul maternité. Le présent lot en retire la seule carence pour les journées futures. L382-46 reste la règle de calcul, sans rétablir l'attente par son renvoi ; le contrat pénitentiaire demeure distinct du CDI privé, de son ancienneté et de sa notification.",
 ('L412-1','L413-12'):"L413-12 réserve les pensions des ateliers de marine, marins, manufactures d'armes et fonctionnaires ; sa note porte une réserve constitutionnelle QPC de 2011. L412-1 conserve cette réserve et sa frontière post-1946, sans attribuer les pensions publiques au contrat privé ou appliquer son seuil d'ancienneté et sa notification. Aucun régime réservé n'est implicitement abrogé.",
 ('L412-2','L311-3'):"L311-3 énumère les affiliés assimilés ; les 10° et 17° réellement visés sont la garde rémunérée d'enfants à domicile et l'accueil familial agréé. La proposition conserve les options et abattements et les ouvre aux contrats uniques recevables, sans transformer tous les assimilés en salariés. La réserve réglementaire de L412-2 subsiste, indépendante d'une ancienneté et notification de rupture.",
 ('L412-3','L242-7'):"L242-7 distingue ristournes de prévention et cotisations pour risques exceptionnels. Sa proposition retire le minimum forfaitaire et actualise le recours ; L412-3 conserve le lien aux risques de l'utilisateur et les actions réciproques sans répéter cette baisse. Ni la durée de mission ni l'ancienneté et notification de licenciement ne déclenchent ces cotisations de risque.",
 ('L412-5','L412-4'):"Le deuxième alinéa de L412-4 impose à l'utilisateur d'informer l'entreprise de travail temporaire ; il est maintenu exactement dans la proposition du lot. La fusion ne vise que les deux informations de la victime du premier alinéa : le recours de L412-5 conserve donc une cible réelle. Aucun seuil d'ancienneté ni notification de rupture ne conditionne cette responsabilité.",
 ('L412-5','L471-1'):"Le deuxième alinéa de L471-1 concerne la récupération des dépenses et la pénalité pour manquement aux déclarations ; le troisième sur séjour irrégulier et travail dissimulé est distinct. Le renvoi de L412-5 ne vise pas indistinctement ces régimes. La transmission de l'utilisateur demeure due ; le défaut déclaratif est sans rapport avec l'ancienneté ou la notification de rupture.",
 ('L412-6','L452-3'):"L452-3 garantit les réparations de préjudices de la faute inexcusable, le forfait à 100 % et les préjudices moraux des ayants droit, versés par la caisse puis récupérés. Sa réserve QPC de 2010 demeure. Le renvoi pluriel clarifié de L412-6 maintient ces droits, sans les plafonner à six mois, ni les soumettre au seuil d'un an ou à la notification de licenciement.",
 ('L412-6','L452-2'):"L452-2 porte la majoration d'indemnité en capital ou de rente, ses plafonds, les réajustements des ayants droit, la revalorisation et la récupération du capital. Sa transition du 1er avril 2013 reste à son objet. L412-6 conserve la dette de l'employeur et le recours contre l'auteur ; cette réparation est distincte de l'ancienneté et notification de rupture ordinaire.",
 ('L412-6','L452-4'):"L452-4 règle accord amiable, juridiction, patrimoine responsable, assurance, prévention et garanties ; son dernier alinéa vise l'appel de l'organisme d'accueil des élèves/stagiaires. L412-6 clarifie seulement la dette de l'employeur en gardant le recours contre l'auteur. Le texte spécial et sa transition de juillet 2026 ne sont ni une indemnité plafonnée de licenciement ni un régime de notification de rupture.",
 ('L412-7','L452-5'):"L452-5 ouvre la réparation de droit commun du préjudice non réparé, impose le service par la caisse et son recours, puis la constitution des rentes sous deux mois et la cotisation de prévention. La substitution de L412-7 désigne les auteurs réels chez l'utilisateur. Faute intentionnelle et réserve QPC restent distinctes de l'ancienneté d'un an et du préavis de quinze jours.",
 ('L412-8','L6321-9'):"Le c du 2° conserve la couverture des formations saisonnières : la source de L6321-9 autorise un CDD de formation, mais sa proposition en fait une phase du contrat unique, avec rémunération et abondement CPF préservés. La durée pédagogique ne termine plus l'emploi nouveau ; anciens contrats et ancienneté restent protégés, sans appliquer le préavis comme condition de couverture AT-MP.",
 ('L412-8','L1233-68'):"Le e du 2° vise l'allocation et les actions de reclassement du CSP, non une durée d'emploi. La proposition de L1233-68 retire les nouvelles périodes d'emploi en CDD et le financement patronal de préavis pour les adhésions nouvelles, mais maintient l'accompagnement et ses droits. L412-8 préserve la couverture future sans recréer un terme, ni supprimer les procédures collectives ou l'ancienneté spéciale du CSP.",
 ('L412-8','L434-1'):"L434-1 attribue un capital sous un seuil d'incapacité, révisable et revalorisé, incessible et insaisissable. L412-8 exclut expressément cette seule prestation pour les a, b et f du 2° ; cette limite est intégralement maintenue, sans supprimer leur autre couverture AT-MP. Le capital de réparation n'est ni un droit de succession ni l'indemnité ordinaire de rupture avec ancienneté et préavis.",
 ('L412-8','L262-1'):"La cible fournie est L262-1 du CSS, relatif à prévention sanitaire et désinsertion professionnelle ; le 10° de L412-8 vise explicitement L262-1 du code de l'action sociale et des familles, relatif au RSA. Ces numéros homonymes ne sont pas substituables : aucune correction vers le CSS n'est faite. La cible fournie ne fonde aucune condition d'ancienneté ou notification et ne remplace pas la vérification CASF extérieure.",
 ('L412-8','L433-1'):"Le cinquième alinéa de la cible fournie rend L323-3-1 applicable ; le renvoi du 3° aux actions de formation et d'accompagnement reste donc opératoire et n'est pas déplacé. L323-3-1 a été lu localement pour la compatibilité médicale des actions. La durée maximale d'IJ prévue pour les sinistres de 2027 ne limite ni la durée d'emploi ni les droits de rupture ; le délai spécial d'inaptitude reste distinct du préavis ordinaire.",
 ('L412-9','L412-3'):"L412-3 tient compte des mesures et risques de l'utilisateur dans la tarification des entreprises de travail temporaire, avec actions réciproques de remboursement. L412-9 maintient l'application de ces règles aux groupements et associations sans relever cotisations ou retirer ristournes. Les contrats antérieurs et la durée de mission ne deviennent pas un seuil d'ancienneté ou un déclencheur de notification AT-MP.",
 ('L412-9','L412-4'):"L412-4 garde la transmission de l'utilisateur à l'entreprise et le lieu de travail comprenant siège et lieux de mission. Sa proposition du présent lot fusionne les deux informations de la victime sans toucher au deuxième alinéa. L412-9 applique la même mesure à ses catégories, sans seconde réduction comptée, ni nouvelle durée d'emploi, ancienneté ou notification de rupture.",
 ('L413-4','L434-2'):"L434-2 détermine l'incapacité, la rente et la prestation de tierce personne selon besoins d'assistance, avec revalorisation et règles d'accidents successifs. L413-4 vise la prestation de son 2° pour les aggravations des sinistres 1945-1946. Le renvoi ne transfère pas tous les autres régimes de la cible et n'importe ni ancienneté d'emploi d'un an ni notification de rupture ; les deux avantages historiques demeurent.",
}

for o in answer:
    number = o['number']
    key = o['code_id']+'|'+o['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        tn = target['number']
        if tn in ('L1234-1','L1221-2','L1234-9'):
            subject, prison = contexts[number]
            if tn == 'L1234-1':
                analysis = (f"Pour {number}, {subject} ne relève pas du préavis de licenciement. "
                    "La cible officielle prévoit les durées selon l'ancienneté ; sa proposition fixe quinze jours calendaires pour les contrats nouveaux et conserve les anciens contrats, procédures collectives et protections. Aucune notification de rupture ni ancienneté de préavis ne conditionne la prestation ou responsabilité AT-MP ici examinée.")
                if prison:
                    analysis += " Le contrat d'emploi pénitentiaire n'est pas un contrat privé auquel importer ce préavis."
            elif tn == 'L1221-2':
                analysis = (f"Pour {number}, {subject} conserve son champ propre. "
                    "La proposition L1221-2 supprime les nouveaux CDD, distingue la durée d'une mission ou formation de celle de l'emploi et protège contrats antérieurs, ancienneté et droits acquis ; ce n'est pas encore le droit officiel. ")
                analysis += ("Le travail pénitentiaire et ses formations ne sont pas convertis en contrats privés ; aucune notification ni ancienneté de rupture n'est importée." if prison else
                    "La couverture ou responsabilité ne dépend pas d'un terme d'emploi ; elle demeure dans les contrats uniques futurs comme pour les anciens contrats, sans ajouter d'ancienneté ni de notification de rupture.")
            else:
                analysis = (f"Pour {number}, {subject} est distinct de l'indemnité ordinaire de rupture. "
                    "La cible proposée retient un an à la fin effective, préavis inclus, puis 0,20 mois par année totale et prorata des mois complets, plafond six mois, employeur seul ; droits anciens et indemnités spéciales demeurent. Ce seuil, cette base et une notification de licenciement ne conditionnent pas les droits de cet article.")
                if prison:
                    analysis += " Le contrat pénitentiaire reste un régime spécial."
        else:
            analysis = specific[(number,tn)]
        checks.append(dict(target_key=target_key,view_sha256=target['view_sha256'],assessment=analysis))
    o['reference_checks'] = checks

assert len(answer)==len(sources)==24
assert [a['number'] for a in answer]==[a['number'] for a in sources]
Path('answer.json').write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
