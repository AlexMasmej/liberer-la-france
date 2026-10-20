import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))


def effect(number, kind, measure_id, description, before, after, unit,
           population, transition, replacement, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in plain(by_number[number]['source_xml']), (number, source_quote)
    assert len(proposed_quote) >= 12 and proposed_quote in plain(answers[number]['proposed_xml']), (number, proposed_quote)
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


def make(number, reason, review, assessment, limitations, burdens,
         xml=None, impact='retained_necessary', removed=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    out.update(proposed_xml=xml, reason=reason, review_notes=review,
               status='retained_unchanged' if xml is None else 'rewrite_draft',
               substantive_impact=dict(version=1, classification=impact,
                                       assessment=assessment,
                                       scope_limitations=limitations,
                                       new_burdens_review=burdens, effects=[]),
               reference_checks=[])
    if xml is None:
        out['classification'] = 'retained_necessary'
    if removed:
        out.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    answers[number] = out
    return out


make('L413-6',
     "Maintien intégral : l'article désigne le débiteur des prestations anciennes et permet la subrogation contre le tiers responsable. L'imputation de la réparation déjà reçue évite une double indemnisation du même dommage ; ce n'est ni un prélèvement accessoire autonome ni une démarche périodique à supprimer.",
     "Conserver les deux alinéas, la revalorisation éventuelle de la rente imputée et la répartition Etat/caisses. Les articles L. 413-2 à L. 413-5 ont été lus dans le corpus ; leurs allocations, appareillage et droits du conjoint survivant subsistent. La note de 2016 concerne l'entrée en vigueur de la source en 2018, sans fixer celle du projet. La nouvelle procédure de première attribution proposée en L. 413-8 ne change pas le débiteur désigné ici.",
     "Aucune réduction matérielle revendiquée : financement des réparations AT-MP et recours subrogatoire sont conservés, sans création de taxe ou restriction de prestation.",
     "Ce maintien ne modifie ni les conditions médicales des articles L. 413-2 à L. 413-5 ni les règles réglementaires de conversion en rente de la réparation en capital, notamment R. 413-13.",
     "Aucune charge nouvelle identifiée : le texte source seul est conservé, sans nouveau justificatif, registre, délai ou transfert de financement.")

make('L413-7',
     "Maintien intégral de la revalorisation des allocations et prestations historiques : supprimer cette règle retirerait un avantage aux victimes. Elle n'exige aucune déclaration nouvelle et n'institue aucun prélèvement.",
     "L. 434-17 et L. 161-25 lus : revalorisation au 1er avril et coefficient d'évolution des prix hors tabac, ramené à un s'il lui est inférieur. R. 413-18 applique cette revalorisation sans demande du bénéficiaire. Le gel partiel envisagé pour les pensions de retraite ne vise pas ces prestations AT-MP.",
     "La protection contre l'érosion monétaire reste intégralement applicable aux prestations éligibles ; aucune simplification ni économie n'est comptée.",
     "Les dates anciennes des accidents restent dans leur champ propre ; le maintien n'élargit pas ces dispositifs à tous les accidents et ne transfère aucune cotisation à la capitalisation.",
     "Aucune charge nouvelle identifiée : l'indexation demeure de plein droit, avec ses règles existantes et sans nouvelle demande.")

xml = """<p>Pour les demandes de première attribution présentées à compter de l'entrée en vigueur de la loi supprimant la constatation judiciaire préalable, le droit aux prestations prévues aux articles L. 413-2 à L. 413-5 est constaté par le service ou l'organisme chargé de leur liquidation. Aucune ordonnance préalable du président du tribunal judiciaire n'est exigée.</p>
<p>Ce service ou cet organisme vérifie les conditions légales et réglementaires d'attribution dans le cadre de la demande de prestations et notifie sa décision à l'intéressé. La constatation du droit ne donne lieu ni à une demande distincte de la demande de liquidation, ni à la production d'une expédition d'ordonnance. Les règles relatives à la preuve, au calcul et au point de départ des prestations demeurent applicables. Les décisions peuvent faire l'objet des recours préalables et juridictionnels applicables à leur auteur et à la matière.</p>
<p>Les demandes présentées avant cette entrée en vigueur et les révisions de droits constatés selon les dispositions antérieures restent soumises à ces dispositions : le droit est constaté par une ordonnance, non susceptible d'appel, rendue par le président du tribunal judiciaire. Les ordonnances déjà rendues conservent leurs effets. La présente réforme ne modifie ni les droits ainsi constatés ni les garanties applicables à leur révision et ne rouvre aucun délai expiré.</p>"""
a = make('L413-8',
     "Réforme de fond : retrait, pour les nouvelles premières demandes, de l'ordonnance judiciaire obligatoire avant liquidation des prestations L. 413-2 à L. 413-5. Le service liquidateur constate directement les conditions de fond dans la même demande ; le juge reste accessible pour un litige. Les demandes déjà déposées, ordonnances et révisions de droits anciens gardent leur régime pour ne pas modifier leurs garanties.",
     "R. 413-6 à R. 413-18 lus en entier. Coordonner R. 413-6 à R. 413-9 (constatations initiales), R. 413-11 1° (expédition d'ordonnance), R. 413-12 (liquidation) et R. 413-15 (frais) dans le nouveau champ ; R. 413-16 étend la procédure à L. 413-9. R. 413-10 reste applicable aux révisions anciennes, notamment son contradictoire et l'effet différé des réductions au trimestre suivant la signification. Le liquidateur est aujourd'hui le service compétent de l'Etat employeur ou, dans les autres cas, la Caisse des dépôts, selon R. 413-12 : ne pas lui substituer automatiquement la CPAM qui supporte la charge. L. 142-1 et L. 142-4 ont été lus pour les recours sociaux ; la compétence dépend de l'auteur et de la matière, notamment pour l'Etat. Aucun nouvel article de procédure contentieuse n'est inventé. Les seuils d'incapacité, appareillage, tierce personne, droits du conjoint et dates d'effet R. 413-3 à R. 413-5 restent entiers. La fusion normative ici dépasse le seul réemploi de données déjà garanti par le CRPA.",
     "La source impose une ordonnance préalable pour constater le droit. Le projet retire cette étape aux nouvelles premières demandes et réunit constatation et liquidation ; il confie aussi une décision supplémentaire au liquidateur. Le classement est mixed car la démarche privée diminue et la responsabilité administrative augmente.",
     "Les demandes antérieures, les révisions des droits déjà constatés et leurs voies de recours restent au régime antérieur. Les règlements cités doivent être coordonnés ; aucun coût net public, délai global de paiement ni économie nationale n'est établi.",
     "Pas de formulaire ou de justificatif de remplacement imposé au demandeur. Le liquidateur doit constater les conditions et notifier la décision dans la demande existante : cette responsabilité remplace le constat du juge et son coût public net reste inconnu.",
     xml=xml, impact='mixed', removed=["Saisine judiciaire et ordonnance préalables obligatoires à toute première attribution nouvelle des prestations des articles L. 413-2 à L. 413-5."])
a['substantive_impact']['effects'] = [
    effect('L413-8', 'obligation_removed', 'at-mp-anciennes-prestations-sans-ordonnance',
           "Suppression du passage judiciaire obligatoire avant la première attribution nouvelle.",
           "Une ordonnance non susceptible d'appel est nécessaire pour constater les droits L. 413-2 à L. 413-5, indépendamment de l'existence d'un litige.",
           "Le service liquidateur constate le droit dans la demande de prestations, sans ordonnance ni demande distincte de constatation.",
           'legal_duty', "Victimes et ayants droit demandant les prestations historiques L. 413-2 à L. 413-5, y compris le champ de L. 413-9 par son renvoi.",
           "Premières demandes présentées dès l'entrée en vigueur ; demandes et révisions anciennes conservées ; conditions de fond et points de départ inchangés.",
           "Constatation administrative à la place du constat préalable judiciaire ; recours maintenus et coût net non établi.",
           "Le droit aux prestations prévues aux articles L. 413-2 à L. 413-5 est constaté par une ordonnance, non susceptible d'appel,",
           "Aucune ordonnance préalable du président du tribunal judiciaire n'est exigée."),
    effect('L413-8', 'obligation_added', 'at-mp-anciennes-prestations-sans-ordonnance',
           "Responsabilité de constatation initiale confiée au liquidateur, en remplacement du juge obligatoire.",
           "Le constat du droit appartient au président du tribunal judiciaire ; le service liquidateur n'en est pas l'auteur dans cet article.",
           "Le service ou organisme liquidateur vérifie les conditions et notifie sa décision dans le dossier de prestations existant.",
           'legal_duty', "Services liquidateurs des prestations historiques AT-MP, dont le service de l'Etat employeur et la Caisse des dépôts dans leurs champs réglementaires.",
           "Uniquement les nouvelles premières demandes ; aucune réouverture ou nouvelle instruction imposée aux droits déjà constatés.",
           "Travail de décision transféré du juge vers le liquidateur ; aucune économie nette présumée.",
           "Le droit aux prestations prévues aux articles L. 413-2 à L. 413-5 est constaté par une ordonnance, non susceptible d'appel,",
           "Ce service ou cet organisme vérifie les conditions légales et réglementaires d'attribution dans le cadre de la demande de prestations et notifie sa décision à l'intéressé.")]

make('L413-9',
     "Maintien intégral de l'extension favorable aux accidents et maladies liés à une activité en Algérie avant le 1er juillet 1962, y compris les catégories étrangères admises. La preuve du fait générateur et du champ personnel reste utile ; aucune obligation déclarative périodique ou taxe n'est instituée par cet article.",
     "Le renvoi à L. 413-2 à L. 413-8 inclut la suppression proposée du préalable judiciaire pour les nouvelles premières demandes. R. 413-16 lu confirme l'application des règlements de cette procédure aux bénéficiaires de L. 413-9 ; leur coordination est nécessaire mais aucun changement de montant ou de catégorie n'en découle. L. 482-5 lu est une habilitation réglementaire, pas une règle de contrat de travail. Les décrets concernant les catégories étrangères ne sont pas tous joints : aucune fermeture ni extension personnelle non documentée.",
     "Le droit d'accès au dispositif historique reste ouvert aux nouvelles demandes remplissant ses conditions. Ce maintien n'est pas compté comme une nouvelle réduction ; l'allègement procédural est porté par L. 413-8.",
     "Le champ reste lié à l'Algérie et aux événements antérieurs au 1er juillet 1962. La résidence, la nationalité et les catégories réglementaires sont conservées, sous réserve des normes supérieures applicables.",
     "Aucune charge nouvelle identifiée : la preuve d'éligibilité préexistante subsiste et aucun dépôt, agrément ou délai supplémentaire n'est ajouté.")

make('L413-10',
     "Maintien intégral de l'allocation différentielle et du service de substitution en cas de non-versement des avantages anciens en Algérie. Supprimer ces dispositions diminuerait les droits des victimes ; les quatre alinéas fixent les bénéficiaires, le complément et les débiteurs sans formalité autonome superflue.",
     "Préserver les dates du 1er juillet et du 30 juin 1962, les articles 13, 14 et 26 de la loi de 1954 et la double fonction d'allocation différentielle et de service des avantages non payés. R. 413-19 à R. 413-22 lus : justification des conditions, prise d'effet, prestations substituées et extension aux étrangers admis. L. 482-1 fourni concerne notamment les rentes d'orphelin et l'apprentissage, pas une indemnité de licenciement ; le renvoi à ses articles suivants demeure collectif. L. 723-2 rural reste à son champ de caisses agricoles ; son texte n'est pas fourni ici et n'est pas reconstruit.",
     "Les compléments et paiements de substitution sont conservés sans baisse, fermeture aux nouvelles demandes éligibles ou changement de financeur. Aucune réduction de prélèvement n'est revendiquée.",
     "Ce maintien ne couvre pas des accidents nouveaux ni tous les pays anciennement sous souveraineté française ; le champ agricole et les droits historiques restent distincts du nouveau contrat privé.",
     "Aucune charge nouvelle identifiée : aucune nouvelle attestation ni déclaration n'est ajoutée aux conditions existantes d'accès aux allocations.")

make('L413-11',
     "Maintien de la règle favorable qui apprécie la résidence en France au jour de la demande pour L. 413-10. Elle fixe une date unique et n'impose pas le maintien perpétuel de la résidence ni une déclaration récurrente.",
     "Ne pas importer la suspension pour départ de France de l'ancien L. 413-11-3, qui vise un dispositif distinct. Le présent article reste le fondement temporel de la condition de L. 413-10 pour les demandes futures aussi. Aucun âge, délai de séjour ou justificatif nouveau n'est décidé.",
     "Aucune modification : l'appréciation ponctuelle de la résidence et l'accès futur aux droits historiques sont préservés. Il ne s'agit pas d'un allègement nouvellement créé.",
     "La disposition porte seulement sur la résidence de L. 413-10 et ne supprime ni les conditions de nationalité applicables ni la preuve du droit à rente ou allocation historique.",
     "Aucune charge nouvelle identifiée : maintien de la seule date d'appréciation déjà fixée, sans contrôle périodique supplémentaire.")

make('L413-11-1',
     "Maintien intégral de l'allocation différentielle pour les accidents et maladies dans les autres anciens territoires concernés. Son seuil de 10 %, son articulation avec les rentes et majorations locales et le niveau des avantages français servent le calcul du droit ; aucune taxe ou autorisation nouvelle n'est établie.",
     "L. 413-11-3 détermine spécialement la date d'appréciation de la résidence prévue ici ; sa proposition supprime seulement la cessation de versement après un départ ultérieur de France, sans modifier la condition initiale. Conserver les trois alinéas, la date d'indépendance propre à chaque pays et le rattachement de la comparaison à la date de l'accident ou de la première constatation médicale. Aucune nouvelle assimilation de taux ou nationalité.",
     "Maintien des conditions et du calcul de l'allocation, sans réduction de prestation. L'ouverture après départ de France relève uniquement de L. 413-11-3 et n'est pas comptée deux fois.",
     "Les accidents d'Algérie sont traités ailleurs ; cette disposition reste limitée aux événements antérieurs à l'indépendance du pays considéré et aux personnes entrant dans son champ.",
     "Aucune charge nouvelle identifiée : pas de justificatif périodique, nouveau taux ou obligation professionnelle ajouté aux conditions existantes.")

make('L413-11-2',
     "Maintien intégral : le financement de l'allocation est attribué aux caisses et la subrogation est limitée à son montant. Cette limite protège le bénéficiaire contre une récupération au-delà de ce qu'il a reçu ; le recours contre un autre débiteur n'est pas une cotisation nouvelle.",
     "Conserver le plafond correspondant au montant de l'allocation et les débiteurs de majorations ou d'avantages de même nature. La suppression de la condition de résidence continue proposée à L. 413-11-3 ne change ni les caisses débitrices ni les limites de subrogation. Note de source : modification applicable depuis le 1er janvier 2018, sans date de réforme future.",
     "Financement et plafond de subrogation restent inchangés ; aucun transfert de cotisation, baisse de taux ou formalité supprimée n'est revendiqué.",
     "Le maintien ne préjuge pas du recouvrement effectif sur les débiteurs étrangers et ne crée pas une créance supplémentaire contre le bénéficiaire.",
     "Aucune charge nouvelle identifiée : la règle préexistante de subrogation bornée est conservée sans déclaration, registre ou donnée supplémentaire.")

xml = """<p>La condition de résidence en France prévue à l'article L. 413-11-1 s'apprécie à la date à laquelle les intéressés demandent le bénéfice des articles L. 413-11-1 à L. 413-11-4. La cessation ultérieure de cette résidence n'interrompt pas le versement de l'allocation.</p>
<p>Cette règle s'applique aux allocations dues pour les périodes courant à compter de l'entrée en vigueur de la loi supprimant la condition de résidence continue. Pour ces périodes, le service d'une allocation précédemment suspendue pour ce seul motif reprend dès lors que les autres conditions d'attribution demeurent remplies. Les périodes antérieures, leurs créances, prescriptions et recours conservent leur régime ; aucune restitution générale ni aucun rappel pour ces périodes n'est créé par la présente disposition.</p>"""
a = make('L413-11-3',
     "Réforme de fond favorable : suppression de l'interruption de l'allocation pour le seul départ de France après l'ouverture du droit. La résidence reste appréciée à la demande initiale comme en L. 413-11, sans résidence continue imposée. Les allocations suspendues pour ce seul motif reprennent pour les nouvelles périodes ; aucune rétroactivité générale n'est instituée.",
     "Coordination expresse de la résidence mentionnée au premier alinéa de L. 413-11-1, sans changer nationalité, taux minimal de 10 %, fait générateur historique ou formule différentielle. L. 413-11-4 maintient la liquidation et le paiement par la Caisse des dépôts. Vérifier les actes d'application et les conventions internationales avant toute évaluation du nombre de bénéficiaires : certaines situations peuvent déjà bénéficier d'une règle d'exportation supérieure. Aucun rappel ancien systématique, déclaration de départ ou certificat de résidence récurrent de remplacement.",
     "Le texte source cesse le versement lorsque la résidence en France prend fin. Cette cause de cessation est retirée pour les périodes nouvelles, ce qui étend effectivement le maintien de l'allocation après un départ sans supprimer une autre condition de fond.",
     "La résidence initiale, la nationalité et l'ensemble des conditions de L. 413-11-1 subsistent. Les droits internationaux déjà ouverts et le coût de l'extension ne sont pas quantifiés ; les périodes anciennes restent à leur régime.",
     "Aucune charge administrative nouvelle identifiée : la condition continue est retirée sans déclaration ou preuve de remplacement. Le paiement reste assuré par le liquidateur existant ; l'extension de dépense n'est pas chiffrée.",
     xml=xml, impact='material_reduction', removed=["Cessation obligatoire du versement de l'allocation différentielle lorsque son bénéficiaire cesse de résider en France après l'ouverture du droit."])
a['substantive_impact']['effects'] = [effect(
    'L413-11-3', 'relief_extended', 'allocation-anciens-territoires-residence-initiale',
    "Maintien de l'allocation après cessation de la résidence en France.",
    "Allocation L. 413-11-1 non versée dès que cesse la résidence en France, sous réserve des normes supérieures déjà applicables.",
    "Résidence vérifiée à l'ouverture ; un départ ultérieur ne supprime plus l'allocation, toutes les autres conditions demeurant remplies.",
    'other', "Bénéficiaires de l'allocation L. 413-11-1 pour les anciens territoires autres que l'Algérie, puis établis hors de France.",
    "Périodes dès l'entrée en vigueur, y compris reprise des allocations suspendues pour ce seul motif ; pas de rappel général pour les périodes anciennes.",
    "Aucun remplacement déclaratif ; financement et organisme payeur inchangés, dépense supplémentaire non évaluée.",
    "L'allocation n'est plus versée dès que cette condition cesse d'être remplie.",
    "La cessation ultérieure de cette résidence n'interrompt pas le versement de l'allocation.")]

make('L413-11-4',
     "Maintien intégral de la désignation de la Caisse des dépôts et consignations comme liquidateur et payeur. Supprimer cet article laisserait indéterminé le service des allocations ; aucun double dépôt ou agrément à la charge du bénéficiaire n'y figure.",
     "Distinguer le payeur chargé de la liquidation des caisses qui supportent la charge selon L. 413-11-2. La reprise pour les nouvelles périodes des allocations suspendues pour résidence relève du même payeur après la réforme de L. 413-11-3, sans créer un second guichet.",
     "Organisation du paiement maintenue, sans transfert de financeur ni baisse de prélèvement. L'article assure la continuité des droits du dispositif.",
     "Cette désignation ne réforme pas les frais de gestion ou l'organisation interne de la Caisse des dépôts, dont aucun coût de doublon n'est démontré par la source.",
     "Aucune charge nouvelle identifiée : même liquidateur, même payeur et aucun formulaire ou calendrier nouveau.")

make('L413-12',
     "Maintien intégral des quatre réserves de régimes de pensions : ateliers de la marine, marins visés au décret de 1938, manufactures d'armes de la défense et fonctionnaires de l'Etat ou territoriaux. Ce sont des garanties de coexistence des droits, pas des autorisations d'embauche ni un prélèvement accessoire.",
     "La note source signale la décision 2011-127 QPC du 6 mai 2011 et sa réserve au considérant 9 pour le 2° ; cette réserve ne peut être neutralisée par la règle de non-dérogation. Son texte intégral n'est pas joint : ne pas inventer sa teneur. Conserver l'article 2 du décret du 17 juin 1938, ses personnes visées et les quatre numéros. Le contrat unique privé ne supprime aucun régime public ni régime maritime autonome.",
     "Les clauses protégeant les régimes spéciaux sont intégralement conservées, avec leur portée constitutionnelle applicable ; aucune nouvelle réduction n'est attribuée à ce maintien.",
     "Les prestations exactes de chaque régime et l'articulation de la réserve QPC requièrent leurs textes propres ; aucune fusion des pensions ou assimilation aux indemnités de rupture n'est décidée.",
     "Aucune charge nouvelle identifiée : la non-dérogation existante subsiste, sans nouvelle condition d'ancienneté, attestation ou procédure.")
answers['L413-12']['benefit_review'] = "Les avantages possibles sont le maintien des pensions propres aux ouvriers, apprentis et journaliers des ateliers de la marine (1°), aux marins visés par l'article 2 du décret du 17 juin 1938 (2°), aux ouvriers immatriculés des manufactures d'armes de la défense (3°) et aux fonctionnaires de l'Etat et des collectivités territoriales (4°). Chaque réserve est conservée intégralement, pour les situations futures éligibles autant que les droits antérieurs ; aucun régime n'est limité aux seuls bénéficiaires déjà servis. La réserve constitutionnelle signalée dans la note au sujet du 2° demeure applicable et ne peut être transformée en exclusion générale de droits. Aucun prélèvement correspondant n'est aboli ici et aucun avantage n'est déclaré sans objet."

make('L413-13',
     "Maintien intégral des autorisations anciennes permettant le service direct de la réparation AT-MP. Les supprimer retirerait une dérogation favorable sans baisse démontrée de cotisation. L'article ne crée pas d'autorisation nouvelle : il protège celles données avant le 13 mai 1960 et habilite le contrôle de la continuité des prestations.",
     "D. 413-1 à D. 413-11 lus : caution, fonds de réserve, paiement de secours, faculté de renonciation et retrait pour défaillance justifient un contrôle, distinct d'un nouvel agrément. Les autorisations et les bénéficiaires demeurent dans leur périmètre historique ; aucune ouverture de nouvelles autorisations n'est inventée. Les intitulés anciens de représentation du personnel figurent dans ces règlements hors lot et nécessitent leur coordination propre.",
     "La dérogation de service direct et les garanties de paiement sont maintenues sans réduction fictive. Aucun coût administratif redondant n'est supprimé dans cet article.",
     "Seules les autorisations antérieures au 13 mai 1960 sont visées. Le maintien ne prouve pas que chaque obligation réglementaire d'exécution soit nécessaire ni qu'elle ait été réécrite ici.",
     "Aucune charge nouvelle identifiée : pas de renouvellement ajouté, pas de demande d'agrément nouvelle et pas de transfert de cotisations.")

make('L413-14',
     "Maintien du paiement direct des prestations par les employeurs publics et régimes visés, avec affiliation obligatoire des petits établissements publics au régime général. Ce dernier mécanisme garantit la couverture du risque ; sa suppression pourrait laisser les agents sans débiteur organisé plutôt que réduire une contrainte inutile.",
     "Conserver l'exclusion des EPIC au premier alinéa et la limitation aux prestations en espèces pour les industries électriques et gazières. Les désignations SNCF, SNCF Mobilités et SNCF Réseau sont celles de la source ; leur application aux personnes morales ayant succédé aux entités nommées nécessite la confrontation avec les textes d'organisation ferroviaire hors corpus. Cette ancienneté de nomenclature est signalée, sans transfert implicite de dette ni correction inventée. D. 413-12 lu confirme les ministres compétents pour le seuil d'affiliation, dont aucun nombre nouveau n'est fixé.",
     "Aucune réforme de financement ou réduction démontrée : l'article conserve le service direct et la couverture des agents des petits établissements.",
     "La succession des entités ferroviaires n'est pas reconstituée à partir de la seule source. Aucun régime public n'est converti au contrat unique privé ou à la capitalisation des salariés privés.",
     "Aucune charge nouvelle identifiée : maintien des responsabilités de paiement et d'affiliation existantes, sans nouveau seuil ou justificatif.")

make('L421-1',
     "Maintien intégral du cadre commun de prévention AT-MP. Le rattachement des missions des caisses à la politique de l'Etat coordonne la protection de la santé ; il n'institue ni dossier à déposer ni autorisation préalable pour l'entreprise.",
     "R. 421-1 lu : politique définie par les ministres chargés du travail et de la sécurité sociale. Les renvois au 2° de L. 221-1 et à L. 215-1 désignent les missions institutionnelles, pas une formalité pour percevoir une exonération. Aucune mesure de financement ou de contrat unique n'est importée.",
     "Cadre institutionnel nécessaire conservé ; aucune baisse de taxe, fusion d'obligation ou diminution de délai n'est démontrée par ce maintien.",
     "L'article ne permet pas de chiffrer les frais des organismes ni de supprimer leurs missions de prévention ou les contrôles de sécurité.",
     "Aucune charge nouvelle identifiée : le maintien ne crée aucune donnée à transmettre, registre ou échéance supplémentaire.")

make('L421-2',
     "Maintien intégral de la faculté de délégation et, en son absence, de la consultation des comités techniques. L. 215-4 lu établit leur composition paritaire travailleurs/employeurs : cette participation à la prévention des risques graves justifie la consultation et ne constitue pas un double agrément individuel des entreprises.",
     "Préserver les deux voies alternatives : délégation totale ou partielle, ou consultation lorsque le conseil ne délègue pas. Il ne s'agit pas de deux consultations cumulatives obligatoires. La composition et la mission d'assistance des comités prévues par L. 215-4 restent dans leur champ.",
     "Aucun gain matériel revendiqué : les deux modalités alternatives de gouvernance et la participation paritaire à la prévention demeurent.",
     "Le nombre et le coût des consultations ne sont pas documentés. Aucune obligation faite aux employeurs de déposer un dossier auprès du comité n'est créée par cet article.",
     "Aucune charge nouvelle identifiée : maintien des compétences existantes, sans nouveau rapport, registre ou réunion minimale.")

xml = by_number['L422-1']['source_xml'].replace("l'article L. 611-1 du code du travail", "l'article L. 8112-1 du code du travail")
a = make('L422-1',
     "Coordination nécessaire du renvoi de contrôle : remplacement de l'ancien L. 611-1 du code du travail par L. 8112-1, dont le texte officiel du corpus confie aux inspecteurs le contrôle de la législation du travail. Les cinq alinéas utiles sont maintenus ; l'arrêté d'extension des règles de sécurité n'est pas supprimé comme un agrément individuel inutile.",
     "Nouveau renvoi non compris dans les cibles imposées : L. 8112-1, LEGIARTI000033025397, lu intégralement dans travail.json du corpus public. L. 243-11 lu confirme les agents des caisses ; L. 422-3 conserve au deuxième alinéa le serment et le secret des ingénieurs-conseils. R. 422-2 lu maintient les compétences ministérielles. L'intitulé ancien des directeurs régionaux désigne dans la source l'autorité régionale du travail ; ses textes d'organisation et leurs intitulés réglementaires doivent être coordonnés séparément sans déplacer la compétence au juge ou au service des ruptures. Aucun préavis de quinze jours ne remplace les délais d'exécution de prévention.",
     "Seul le renvoi obsolète vers les missions de l'inspection est coordonné ; aucune suppression d'obligation de sécurité, d'autorisation ou de cotisation n'en résulte.",
     "Extension nationale, fixation des délais, études, secret et rémunération demeurent. La coordination des intitulés administratifs hors lot n'est pas présentée comme achevée.",
     "Aucune charge nouvelle identifiée : le renvoi désigne les missions de contrôle déjà attribuées aux inspecteurs par le droit en vigueur, sans nouveau pouvoir ou dépôt.",
     xml=xml, impact='coordination_only')
a['substantive_impact']['effects'] = [effect(
    'L422-1', 'coordination', 'prevention-inspection-renvois-recodifies',
    "Actualisation de la référence légale des missions de l'inspection du travail.",
    "Constat de l'inobservation des dispositions étendues par renvoi à l'ancien L. 611-1 du code du travail.",
    "Même constat et mêmes règles de prévention, avec référence à L. 8112-1 du code du travail.",
    'other', "Inspecteurs du travail, agents de prévention des caisses et employeurs soumis aux dispositions étendues.",
    "Coordination à l'entrée en vigueur, sans réouverture des décisions antérieures et sans modification des délais de sécurité.",
    "Aucun nouveau contrôle, document ou régime d'autorisation.",
    "les inspecteurs du travail en application de l'article L. 611-1 du code du travail",
    "les inspecteurs du travail en application de l'article L. 8112-1 du code du travail")]

xml = by_number['L422-2']['source_xml'].replace(
    "communiqués aux comités d'hygiène, de sécurité et des conditions de travail.",
    "communiqués aux instances de représentation du personnel exerçant les attributions en matière de santé, de sécurité et de conditions de travail, dans le champ de leurs compétences.")
a = make('L422-2',
     "Coordination des destinataires des études avec les instances exerçant aujourd'hui les attributions de santé et sécurité. Le maintien du seul intitulé CHSCT laisserait sans mention leur successeur dans les entreprises. Les statistiques de causes, fréquence, effets et incapacités, leur centralisation et la communication annuelle à l'Etat demeurent : elles servent directement la connaissance des risques, sans rapport d'entreprise distinct dans cet article.",
     "L. 2312-5, L. 2312-8 et L. 2312-9 du code du travail lus dans le corpus établissent les attributions de santé et sécurité du CSE ; aucun renvoi numérique nouveau à ces textes n'est inséré. La désignation fonctionnelle couvre les instances réellement compétentes sans imposer une communication supplémentaire à une commission distincte. Demande de l'instance toujours requise, pas de transmission annuelle nouvelle. R. 422-3 lu conserve les destinataires ministériels des statistiques et le niveau régional pour les études ; ses intitulés administratifs anciens ne sont pas modifiés dans ce lot.",
     "Même production statistique et même accès sur demande aux études ; la coordination remplace le seul intitulé ancien des représentants compétents. Aucun rapport ni prélèvement n'est supprimé.",
     "Les règles d'organisation des instances publiques ne sont pas intégralement jointes ; leur compétence reste celle de leurs textes propres. Aucune publication de données individuelles n'est ouverte.",
     "Aucune charge nouvelle identifiée : pas de destinataire cumulatif, de registre ou de calendrier ajouté ; l'accès sur demande reste celui des instances compétentes.",
     xml=xml, impact='coordination_only')
a['substantive_impact']['effects'] = [effect(
    'L422-2', 'coordination', 'prevention-instances-personnel-successeurs',
    "Identification des représentants compétents à la place de l'intitulé exclusif CHSCT.",
    "Résultats des études communiqués sur demande aux CHSCT nommément désignés.",
    "Même communication sur demande aux instances exerçant les attributions correspondantes dans leur champ de compétence.",
    'other', "Instances de représentation du personnel compétentes en santé, sécurité et conditions de travail et caisses régionales.",
    "Accès futur des instances compétentes, sans remise en cause des communications antérieures et sans nouvelle périodicité.",
    "Aucun envoi supplémentaire distinct à une commission interne ou accès élargi aux données personnelles.",
    "sur leur demande, communiqués aux comités d'hygiène, de sécurité et des conditions de travail.",
    "sur leur demande, communiqués aux instances de représentation du personnel exerçant les attributions en matière de santé, de sécurité et de conditions de travail, dans le champ de leurs compétences.")]

make('L422-3',
     "Maintien intégral des enquêtes de sécurité, de l'accès aux documents nécessaires et des vérifications antifraude, avec serment, secret de fabrication, preuve contraire et contradictoire. Ces fonctions protègent la santé et la correcte attribution des ristournes, subventions et prestations ; les supprimer ne constituerait pas un retrait de formalité sans fonction essentielle.",
     "Source du 27 juin 2026 lue en entier : six alinéas, dont le deuxième reste la cible du secret visé en L. 422-1. L. 243-11 lu fonde l'accueil des agents régulièrement accrédités. Aucun nouveau régime général de transmission ne découle de cet article : les échanges gardent leur finalité et leurs procédures. Les intitulés anciens des directeurs départementaux du travail et de l'emploi sont signalés comme une nomenclature administrative à rapprocher des services successeurs dans les textes d'organisation hors lot ; aucune compétence nouvelle n'est attribuée silencieusement. Les aides et ristournes restent ouvertes aux futures situations éligibles.",
     "Aucune réduction revendiquée : les pouvoirs utiles de prévention et de vérification restent accompagnés de leurs garanties de confidentialité, preuve contraire et défense.",
     "L'article ne justifie pas la nécessité de chaque pièce demandée dans un dossier particulier : seuls les documents nécessaires à la mission entrent dans l'obligation. Aucun solde global de conformité n'est établi.",
     "Aucune charge nouvelle identifiée : maintien des obligations et échanges existants, sans nouvelle collecte générale, nouveau registre ou justificatif d'accès aux aides.")

xml = by_number['L422-4']['source_xml'].replace("l'article L. 611-10 du code du travail", "l'article L. 8113-7 du code du travail")
a = make('L422-4',
     "Coordination du renvoi obsolète de constatation des infractions avec L. 8113-7 du code du travail, déjà visé par L. 242-7. Les mesures de prévention justifiées, homologation des dispositions générales, recours et exceptions précises à l'injonction préalable restent nécessaires face aux risques graves ou répétés. Aucun supplément de cotisation n'est nouvellement supprimé dans cet article.",
     "Nouveau renvoi non fourni comme cible obligatoire : L. 8113-7, LEGIARTI000032376386, lu intégralement dans travail.json ; il traite des procès-verbaux et de l'information préalable de la personne visée. L. 242-7 fourni distingue ristournes, cotisations supplémentaires et affectations : sa proposition retire déjà le montant forfaitaire minimal, que le présent texte ne réintroduit pas. L. 422-1 reste le vrai fondement des dispositions étendues ; ni son renvoi ni le 1° bis ne sont renumérotés. R. 422-5 lu fixe notamment un délai de trois ans pour la récidive du 2° ; il ne s'agit pas du préavis individuel de rupture.",
     "La seule différence est une référence recodifiée pour le constat d'infraction. Le mécanisme de prévention et les garanties antérieures subsistent, sans nouvelle baisse de cotisation comptée.",
     "La suppression du minimum forfaitaire proposée à L. 242-7 n'est pas une seconde mesure de cet article. Les arrêtés sur les risques exceptionnels et les délais spécifiques conservent leur champ.",
     "Aucune charge nouvelle identifiée : aucun nouveau motif de supplément, contrôle, registre ou délai ; le renvoi reprend la procédure actuelle de constatation.",
     xml=xml, impact='coordination_only')
a['substantive_impact']['effects'] = [effect(
    'L422-4', 'coordination', 'prevention-inspection-renvois-recodifies',
    "Concordance du renvoi de constatation d'infraction avec le code du travail actuel.",
    "Exception à l'injonction préalable en cas d'infraction constatée par renvoi à L. 611-10.",
    "Même exception avec référence à L. 8113-7, sans modification des cas de supplément ou de récidive.",
    'other', "Caisses régionales et employeurs soumis aux mesures de prévention et aux cotisations supplémentaires AT-MP.",
    "Coordination sans réouverture des décisions ni nouvelle durée ; régimes anciens et garanties de recours demeurent.",
    "Aucune charge de remplacement et aucune seconde suppression du minimum de L. 242-7.",
    "d'infraction constatée en application de l'article L. 611-10 du code du travail",
    "d'infraction constatée en application de l'article L. 8113-7 du code du travail")]

xml = """<p>Dans une limite fixée par voie réglementaire, des avances peuvent être accordées par la caisse régionale aux entreprises qui souscrivent aux conditions de la convention d'objectifs fixant un programme d'actions de prévention spécifique à leurs branches d'activité. Ces avances pourront être acquises aux entreprises dans les conditions prévues par la convention.</p>
<p>La caisse mentionnée au premier alinéa peut également accorder, dans des conditions définies par arrêté, des subventions aux entreprises éligibles aux programmes de prévention définis par la Caisse nationale de l'assurance maladie ou par la caisse mentionnée au premier alinéa après avis des comités techniques mentionnés respectivement aux articles L. 422-1 et L. 215-4. Ces programmes précisent les risques et les catégories d'entreprises éligibles ainsi que les montants financiers susceptibles d'être alloués. Une subvention ne peut être accordée à une entreprise que si son comité social et économique ou l'instance de représentation du personnel qui exerce, selon le régime applicable à l'entreprise, les attributions correspondantes en matière de santé, de sécurité et de conditions de travail a été informé des mesures de prévention préalablement à leur mise en œuvre. L'absence d'instance ne fait pas obstacle à l'aide lorsqu'elle est conforme aux règles applicables de représentation du personnel.</p>
<p>Pour les conventions d'objectifs conclues à compter de l'entrée en vigueur de la loi supprimant leur approbation préalable, aucune approbation de la Caisse nationale de l'assurance maladie n'est requise. Aucune déclaration de remplacement n'est exigée. Les demandes en cours bénéficient de cette suppression sans nouveau dépôt. Les conventions valablement conclues auparavant, les avances, les droits à leur acquisition, les subventions et les engagements financiers antérieurs conservent leurs effets selon leurs conditions. Les règles antérieures d'information des représentants du personnel demeurent applicables aux décisions d'aide prises avant cette entrée en vigueur. Les limites de financement, les conditions de prévention et les contrôles légalement applicables restent en vigueur.</p>"""
a = make('L422-5',
     "Réforme de fond : suppression de l'approbation préalable par la caisse nationale de chaque convention d'objectifs, sans déclaration équivalente. Le plafond réglementaire, la spécialité de branche, les conditions d'acquisition des avances, les programmes, avis techniques, montants d'aides et contrôles sont conservés. Coordination nécessaire de l'information des représentants avec les instances actuelles ; l'absence régulière de représentant n'exclut pas les petites entreprises éligibles.",
     "Les deux premiers alinéas gardent leurs fonctions et le dernier alinéa porte la transition. L. 215-4 et L. 422-1 lus : l'avis des comités techniques sur les programmes est distinct de l'approbation nationale supprimée. R. 422-8 lu organise les avances remboursables, subventions et transformation des avances pour des mesures expérimentales ; aucune de ces catégories n'est retirée. R. 422-6 vise l'autorisation de création d'institutions ou services : régime distinct, non supprimé par ce texte. L. 2312-5, L. 2312-8 et L. 2312-9 lus pour le CSE, sans insertion d'un nouveau renvoi numérique. Les actes réglementaires et conventions types qui imposeraient le visa national doivent être coordonnés ; leurs conditions financières autonomes demeurent. Aucun financement supplémentaire, enveloppe ou droit automatique à subvention n'est inventé.",
     "La source subordonne la convention d'objectifs à une approbation préalable nationale ; ce verrou est retiré pour les conventions nouvelles et demandes en cours. Les aides et conditions de prévention subsistent ; la mise à jour des représentants est une coordination sans gain distinct compté.",
     "La suppression ne porte ni sur les plafonds de financement, ni sur les avis techniques relatifs aux programmes, ni sur les autres autorisations de création de services. Le coût budgétaire et le gain de délai ne sont pas quantifiés.",
     "Aucune charge nouvelle identifiée : pas de déclaration de remplacement, pas de demande à refaire et pas d'attestation sur l'absence d'instance. L'information préalable existante passe à l'instance compétente, sans double information imposée.",
     xml=xml, impact='material_reduction', removed=["Approbation préalable obligatoire par la Caisse nationale de l'assurance maladie des conventions d'objectifs ouvrant accès aux avances de prévention."])
a['substantive_impact']['effects'] = [
    effect('L422-5', 'authorization_removed', 'prevention-conventions-objectifs-sans-approbation',
           "Retrait de l'approbation nationale préalable des conventions d'objectifs.",
           "Avances accordables seulement au titre d'une convention d'objectifs préalablement approuvée par la CNAM, sous limite réglementaire.",
           "Même dispositif d'avances, de programmes et de limite réglementaire, sans approbation nationale préalable de la convention.",
           'legal_duty', "Caisses régionales et entreprises éligibles aux avances de prévention par branche.",
           "Conventions conclues dès l'entrée en vigueur et demandes en cours sans redépôt ; engagements et aides antérieurs préservés.",
           "Aucune déclaration, autorisation locale supplémentaire ou recette de remplacement ; conditions financières et contrôles conservés.",
           "la convention d'objectifs, préalablement approuvée par la caisse nationale de l'assurance maladie",
           "aucune approbation de la Caisse nationale de l'assurance maladie n'est requise."),
    effect('L422-5', 'coordination', 'prevention-instances-personnel-successeurs',
           "Maintien de l'information préalable sur les mesures de prévention auprès de l'instance compétente actuelle.",
           "Condition d'information du CHSCT ou, à défaut, des délégués du personnel avant mise en œuvre des mesures subventionnées.",
           "Même information préalable au CSE ou à l'instance correspondante ; absence régulière d'instance ne fermant pas l'aide.",
           'other', "Entreprises candidates aux subventions et leurs représentants du personnel compétents.",
           "Nouvelles décisions d'aide ; décisions antérieures et règles d'information antérieures conservées.",
           "Aucun second destinataire cumulatif, registre ou justificatif nouveau ; aucun allègement supplémentaire chiffré.",
           "le comité d'hygiène, de sécurité et des conditions de travail ou, à défaut, les délégués du personnel ont été informés des mesures de prévention préalablement à leur mise en œuvre.",
           "son comité social et économique ou l'instance de représentation du personnel qui exerce, selon le régime applicable à l'entreprise, les attributions correspondantes en matière de santé, de sécurité et de conditions de travail a été informé des mesures de prévention préalablement à leur mise en œuvre.")]

xml = """<p>Des conventions sont conclues entre les organismes de sécurité sociale compétents et les services de prévention et de santé au travail mentionnés à l'article L. 4622-7 du code du travail. Elles fixent les modalités des actions conjointes ou complémentaires conduites par les services de prévention et de santé au travail et les services de prévention des risques professionnels des caisses de sécurité sociale dans le respect de leurs missions respectives. A cet effet, ces services échangent toutes informations utiles au succès de ces actions de prévention, à l'exclusion des informations personnelles relatives aux salariés, venues à la connaissance des médecins du travail.</p>
<p>Les conventions conclues à compter de l'entrée en vigueur de la loi supprimant l'avis administratif préalable ne sont soumises à aucun avis préalable de l'autorité administrative sur le fondement du présent article. Aucune déclaration de remplacement n'est exigée. Cette suppression s'applique aux projets de convention en cours sans nouveau dépôt. Les conventions antérieurement conclues et les engagements qui en résultent conservent leurs effets. Les missions, contrôles et règles de protection des données applicables aux services demeurent en vigueur.</p>"""
a = make('L422-6',
     "Réforme de fond : suppression de l'avis administratif préalable pour les conventions de coopération en prévention, sans notification de remplacement. La convention, les missions distinctes des services, la finalité de l'échange et l'exclusion des informations personnelles connues des médecins du travail sont conservées intégralement.",
     "L'avis de la source n'est pas un agrément ni une autorisation : l'effet est classé obligation_removed. L. 4622-7, LEGIARTI000043893852, lu dans le corpus public, vise le service assuré par un groupement ou organisme distinct de l'employeur et les obligations de ses responsables ; il ne règle ni préavis ni indemnité de licenciement. La note source du 2 août 2021 renvoie aux conditions transitoires de son article 40 II : elles ne sont pas abrogées implicitement. Coordonner seulement les actes ou modèles exigeant cet avis pour les projets nouveaux et en cours ; les contrôles autonomes et les engagements antérieurs subsistent.",
     "Une étape préalable imposée à chaque convention est effectivement retirée. Le contenu de coopération et le secret médical restent entiers ; aucune baisse de cotisation ou suppression de contrôle de santé n'est déduite de cet allègement.",
     "Les autres avis ou agréments prévus par des fondements autonomes ne sont pas supprimés. Les délais gagnés et les coûts publics nets de la suppression ne sont pas chiffrés.",
     "Aucune charge nouvelle identifiée : aucune déclaration, copie ou autorisation ne remplace l'avis supprimé ; le cadre conventionnel et les échanges déjà autorisés gardent leur champ.",
     xml=xml, impact='material_reduction', removed=["Saisine préalable obligatoire de l'autorité administrative pour avis sur les conventions de coopération entre organismes sociaux et services de prévention et de santé au travail."])
a['substantive_impact']['effects'] = [effect(
    'L422-6', 'obligation_removed', 'prevention-cooperation-sans-avis-administratif',
    "Suppression de la consultation administrative préalable des conventions de coopération.",
    "Conventions entre organismes de sécurité sociale et services L. 4622-7 soumises à l'avis préalable de l'autorité administrative.",
    "Mêmes conventions et garanties de confidentialité, sans avis administratif préalable sur ce fondement.",
    'legal_duty', "Organismes sociaux et services de prévention et de santé au travail concluant les conventions visées.",
    "Conventions nouvelles et projets en cours dès l'entrée en vigueur ; engagements antérieurs et autres contrôles préservés.",
    "Aucune déclaration ou saisine équivalente de remplacement ; pas d'élargissement de l'accès aux informations médicales.",
    "Des conventions soumises à l'avis préalable de l'autorité administrative sont conclues",
    "ne sont soumises à aucun avis préalable de l'autorité administrative sur le fondement du présent article.")]

make('L431-1',
     "Maintien intégral du socle de prestations : soins et transports même sans interruption de travail, indemnités journalières, prestations de décès, capital ou rentes d'incapacité et rentes d'ayants droit. Ce sont des réparations du risque professionnel ; ni la suppression des droits de succession ni le zéro d'indemnité ordinaire avant un an ne justifie de les supprimer.",
     "Conserver les quatre numéros, la restriction et la réserve réglementaire concernant les pupilles de l'éducation surveillée, les produits L. 165-1 et les prothèses L. 162-1-7. L. 432-12 fourni confirme le complément de reconversion par abondement CPF : aucune durée de formation ne termine le contrat unique et la suppression de la contribution CPF-CDD n'abolit pas cet abondement. La version assignée prend fin le 1er novembre 2026 ; la version suivante n'est pas fournie dans les cibles et doit être confrontée lors de la consolidation temporelle, sans inventer son contenu. La note d'entrée en vigueur de 2017/2019 n'est pas la date du projet.",
     "Le droit aux réparations AT-MP reste entier pour les bénéficiaires éligibles ; aucun gain nouveau, taux réduit ou transfert de financement n'est revendiqué.",
     "Le maintien porte sur la version assignée, valable jusqu'au 1er novembre 2026, et ne vaut pas examen d'une rédaction ultérieure non jointe. Les conditions de chaque prestation demeurent dans leurs dispositions propres.",
     "Aucune charge nouvelle identifiée : mêmes prestations, mêmes caisses débitrices et aucune nouvelle ancienneté minimale, attestation ou durée d'emploi.")

make('L431-2',
     "Maintien intégral des prescriptions biennales, points de départ, recours et causes d'interruption. Elles protègent à la fois l'exercice des droits des victimes et la stabilité des paiements, et limitent la répétition des indus hors fraude. Aucun délai minimal d'attente ou formalité redondante n'est institué à retirer dans cet article.",
     "Conserver tous les points de départ 1° à 4°, les deux ans pour les professionnels et pour la récupération d'indus sauf fraude ou fausse déclaration, ainsi que l'interruption par action pénale ou reconnaissance professionnelle en matière de faute inexcusable. L'expression source « trois alinéas précédents » a une portée à vérifier dans l'articulation des blocs de prescription malgré le découpage XML : aucune correction silencieuse n'en est faite. La note de 2019 vise les recours introduits selon son calendrier au plus tard le 1er janvier 2022 ; ce n'est pas une transition de la réforme. L. 431-1 est maintenu dans sa version assignée ; sa fin de validité au 1er novembre 2026 exige confrontation de la version suivante lors de la consolidation. Les délais sociaux ne sont ni un préavis de rupture ni une condition d'ancienneté.",
     "Pas de modification : prescription des demandes, des factures et des indus avec leurs exceptions et interruptions conservée. Aucune réduction de délai ou de dette indue n'est annoncée.",
     "Les faits interruptifs, la faute inexcusable et les droits de recours demeurent à leur régime propre. La portée du renvoi ordinal ancien et la version future de L. 431-1 restent des points de consolidation explicitement signalés.",
     "Aucune charge nouvelle identifiée : aucun nouveau recours préalable, délai de forclusion ou document n'est ajouté ; l'article source est intégralement conservé.")

make('L431-3',
     "Maintien intégral de la faculté de stipuler des avantages complémentaires pour les victimes et ayants droit. Supprimer cette faculté retirerait une amélioration de protection sans alléger une obligation générale, car le présent article n'impose ni montant ni souscription obligatoire.",
     "L'employeur et les institutions de prévoyance du titre III du livre IX restent les opérateurs de service dans leur champ. Les états annuels de protection complémentaire supprimés dans d'autres articles ne conditionnent pas cette faculté et ne sont pas recréés ici. La note source renvoie seulement à la date d'application de la loi du 8 août 1994 ; elle ne définit pas l'entrée en vigueur d'une réforme nouvelle.",
     "Maintien d'une faculté favorable pour les stipulations futures et les engagements antérieurs, sans nouvelle cotisation ou obligation de reporting.",
     "Les conditions de chaque stipulation et le régime propre des institutions de prévoyance ne sont pas réécrits ; aucun financement nouveau n'est garanti.",
     "Aucune charge nouvelle identifiée : la faculté contractuelle et les opérateurs existants subsistent, sans minimum, adhésion ou déclaration supplémentaire.")


# Analyses propres à chaque article, pour les seules cibles imposées.
labor_context = {
    'L413-10': "L'allocation différentielle et le service des avantages historiques d'Algérie relèvent des accidents antérieurs au 1er juillet 1962 et des caisses ou de l'Etat, pas de la rupture d'un contrat actuel.",
    'L413-12': "La non-dérogation aux quatre régimes de pensions, notamment des marins et agents publics, ne règle aucune rupture individuelle de contrat privé.",
    'L422-1': "Le renvoi de cet article concerne les missions de l'inspection et les délais d'exécution des mesures de prévention étendues, pas les conditions de fin du contrat.",
    'L422-4': "Les injonctions, homologations et suppléments AT-MP liés au risque exceptionnel sont distincts de la rupture individuelle ; le renvoi de constatation est coordonné vers L. 8113-7.",
    'L422-5': "Les avances et subventions financent la prévention de risques de branche ; leur convention d'objectifs n'est pas un contrat de travail et sa durée ne fixe pas la durée d'emploi.",
    'L422-6': "La convention unit des organismes sociaux et des services de prévention L. 4622-7 : ce n'est pas une relation employeur-salarié et la suppression de son avis ne supprime aucune procédure de rupture.",
    'L431-1': "Soins, indemnités journalières, capital, rentes et prestations de décès réparent le risque AT-MP ; ils ne sont pas l'indemnité de licenciement ni un impôt de succession.",
    'L431-2': "Les deux ans de prescription des réparations AT-MP, factures et indus et leurs interruptions ne sont pas les délais de notification ou de rupture du contrat de travail."
}

labor_explanation = {
    'L1234-1': "La source prévoit des préavis selon l'ancienneté, avec minima plus favorables ; la proposition fournie, distincte du droit en vigueur, retient quinze jours calendaires pour les nouveaux contrats et préserve l'ancien régime des contrats antérieurs. Cette durée ne s'applique pas aux décisions sociales ou de prévention de l'article examiné ; elle n'abolit aucune autorisation collective ou protection spéciale.",
    'L1221-2': "La proposition fournie impose la durée indéterminée aux nouvelles embauches privées et conserve la transition des contrats antérieurs, contrairement à la source qui admet encore les CDD. Aucun CDD ni terme d'emploi ne résulte du présent dispositif ; les prestations et aides restent ouvertes aux futures situations éligibles sans requalification artificielle des agents publics.",
    'L1234-9': "La source ouvre l'indemnité de licenciement à huit mois ; la proposition fournie distingue les nouveaux contrats : seuil d'un an à la fin effective, préavis inclus, puis 0,20 mois par année totale et prorata des mois complets, plafond de six mois, employeur seul, avec son exception de faute grave. Ce régime ordinaire et la transition des droits anciens ne conditionnent aucune prestation, rente ou aide examinée ici, ni les indemnités spéciales et réparations d'illégalité."
}

special = {
    ('L413-10', 'L482-1'): "Le renvoi vise L. 482-1 et suivants pour les avantages historiques : le texte fourni relève les limites d'âge des rentes d'orphelin en apprentissage, études ou incapacité permanente. Une durée de formation y est une condition de protection de l'orphelin, pas un terme d'emploi ; aucune condition d'un an d'ancienneté ni notification de rupture n'y est insérée.",
    ('L422-4', 'L422-1'): "Le 1° de dispense d'injonction vise les dispositions générales effectivement étendues nationalement par arrêté selon L. 422-1 ; sa faculté de prévoir autrement est conservée. La cible fournie est la source officielle, sans proposition ; le présent lot coordonne seulement son renvoi d'inspection. Ni le préavis de quinze jours ni les règles d'ancienneté de rupture ne remplacent l'arrêté ou ses délais d'exécution.",
    ('L422-4', 'L242-7'): "La source autorise ristournes et suppléments de risque exceptionnel et prévoit un minimum forfaitaire ; la proposition fournie retire ce minimum pour les périodes nouvelles, y compris les décisions anciennes, tout en préservant les ristournes futures et recours. L. 422-4 n'impose aucun minimum et ne le rétablit pas ; les exemptions d'injonction ne créent pas une seconde réduction de cotisation et n'ont aucun rapport avec l'ancienneté de rupture.",
    ('L422-5', 'L422-1'): "Le second alinéa vise les comités techniques nationaux et leurs programmes de prévention, non un avis individuel sur chaque aide ou chaque embauche. La procédure d'extension nationale de L. 422-1 reste distincte de l'approbation des conventions d'objectifs supprimée ici ; avis paritaires, bénéficiaires futurs et montants éligibles sont préservés sans ancienneté d'un an ni délai de rupture.",
    ('L431-1', 'L432-12'): "La cible officielle, sans proposition fournie, permet un abondement CPF de reconversion après incapacité permanente atteignant le taux réglementaire. L. 431-1 en conserve le champ de reconversion ; supprimer la contribution CPF-CDD ne retire pas cet abondement aux futures situations éligibles. Une formation ne fixe pas le terme de l'emploi et aucune ancienneté d'un an ou notification de licenciement n'est exigée pour ce droit.",
    ('L431-2', 'L431-1'): "La prescription de l'action des praticiens et fournisseurs vise bien les prestations de L. 431-1 ; les droits de la victime couvrent le livre IV et ne sont pas réduits aux seules créances de soins. La cible fournie est la source officielle, maintenue dans ce lot, valable jusqu'au 1er novembre 2026 ; ses prestations ne sont pas subordonnées à un an d'ancienneté. Les quatre points de départ, l'exception de fraude et l'interruption pour faute inexcusable subsistent, sans substitution du préavis individuel."
}

for a in sources:
    out = answers[a['number']]
    key = a['code_id'] + '|' + a['source_id']
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        number = target['number']
        if number in labor_explanation:
            assessment = labor_context[a['number']] + ' ' + labor_explanation[number]
        else:
            assessment = special[(a['number'], number)]
        assert len(assessment) >= 80
        out['reference_checks'].append(dict(target_key=target_key,
                                            view_sha256=target['view_sha256'],
                                            assessment=assessment))
    if a.get('benefit_check_required'):
        assert len(out.get('benefit_review', '')) >= 100

# Retenir des phrases ou alinéas complets comme preuves, sans ellipses.
def paragraph(xml, index):
    return plain(re.findall(r'<p>(.*?)</p>', xml, re.S)[index]).strip()


for e in answers['L413-8']['substantive_impact']['effects']:
    e['source_quote'] = plain(by_number['L413-8']['source_xml']).strip()

e = answers['L422-1']['substantive_impact']['effects'][0]
e['source_quote'] = paragraph(by_number['L422-1']['source_xml'], 1)
e['proposed_quote'] = paragraph(answers['L422-1']['proposed_xml'], 1)

e = answers['L422-2']['substantive_impact']['effects'][0]
e['source_quote'] = paragraph(by_number['L422-2']['source_xml'], 1)
e['proposed_quote'] = paragraph(answers['L422-2']['proposed_xml'], 1)

e = answers['L422-4']['substantive_impact']['effects'][0]
e['source_quote'] = paragraph(by_number['L422-4']['source_xml'], 5)
e['proposed_quote'] = paragraph(answers['L422-4']['proposed_xml'], 5)

e = answers['L422-5']['substantive_impact']['effects'][0]
e['source_quote'] = paragraph(by_number['L422-5']['source_xml'], 0)
e['proposed_quote'] = "Pour les conventions d'objectifs conclues à compter de l'entrée en vigueur de la loi supprimant leur approbation préalable, aucune approbation de la Caisse nationale de l'assurance maladie n'est requise."

e = answers['L422-5']['substantive_impact']['effects'][1]
e['source_quote'] = "Une subvention ne peut être accordée à une entreprise que si " + e['source_quote']
e['proposed_quote'] = "Une subvention ne peut être accordée à une entreprise que si " + e['proposed_quote']

e = answers['L422-6']['substantive_impact']['effects'][0]
e['source_quote'] = "Des conventions soumises à l'avis préalable de l'autorité administrative sont conclues entre les organismes de sécurité sociale compétents et les services de prévention et de santé au travail mentionnés à l'article L. 4622-7 du code du travail."
e['proposed_quote'] = "Les conventions conclues à compter de l'entrée en vigueur de la loi supprimant l'avis administratif préalable ne sont soumises à aucun avis préalable de l'autorité administrative sur le fondement du présent article."

for number, out in answers.items():
    for e in out['substantive_impact']['effects']:
        assert e['source_quote'] in plain(by_number[number]['source_xml'])
        assert e['proposed_quote'] in plain(out['proposed_xml'])

result = [answers[a['number']] for a in sources]
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'articles': len(result),
                  'statuts': {s: sum(a['status'] == s for a in result) for s in {'rewrite_draft', 'retained_unchanged'}},
                  'impacts': {s: sum(a['substantive_impact']['classification'] == s for a in result) for s in {a['substantive_impact']['classification'] for a in result}}}, ensure_ascii=False))
