import json
import re
from html import unescape

with open('source.json') as f:
    sources = json.load(f)
with open('reference-targets.json') as f:
    references = json.load(f)

by_number = {a['number']: a for a in sources}
answers = {}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()


def clean(xml):
    return xml.replace(' align="left"', '')


def replace_once(xml, before, after):
    assert xml.count(before) == 1, (before, xml.count(before))
    return xml.replace(before, after, 1)


def impact(classification, assessment, scope, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=scope, new_burdens_review=burdens,
                effects=effects or [])


def effect(number, kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    assert source_quote in plain(by_number[number]['source_xml']), (number, source_quote)
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def base(number, proposal, reason, notes, substantive):
    s = by_number[number]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=proposal, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposal is None else 'rewrite_draft',
             substantive_impact=substantive, reference_checks=[])
    if proposal is None:
        a['classification'] = 'retained_necessary'
    answers[number] = a
    return a


def retain(number, reason, notes, assessment, scope, burdens):
    return base(number, None, reason, notes,
                impact('retained_necessary', assessment, scope, burdens))


def reduce(number, proposal, reason, notes, removed, substantive):
    a = base(number, proposal, reason, notes, substantive)
    a.update(change_type='normative_reduction',
             reform_policy_id='editorial_direction_2026_10_19',
             removed_provisions=removed)
    return a


retain('R113-12',
       "Maintien intégral après examen : l'attache du cadre et d'au moins une roue et la stabilité donnent un contenu effectif au stationnement sécurisé imposé par les articles L. 113-18 à L. 113-20. La localisation préférentielle n'est pas une interdiction des autres niveaux. Supprimer ces garanties laisserait une obligation d'équipement sans protection minimale contre la chute ou le vol ; aucune déclaration ni autorisation distincte n'est imposée ici.",
       "Les trois articles législatifs L. 113-18 à L. 113-20 ont été lus dans le corpus public : l'obligation de stationnement subsiste et L. 113-19 permet déjà une autre partie du bâtiment ou son extérieur sur la même unité foncière. R. 113-16 est coordonné dans ce lot pour supprimer la seule couverture obligatoire ; son renvoi reste opérant. Les notes du décret du 25 juin 2022 concernent l'entrée en vigueur passée, non la date de la réforme proposée.",
       "Aucune réduction supplémentaire : maintien du dispositif d'attache et de la localisation sur l'unité foncière, avec préférence non impérative de niveau. La coupe de couverture est portée uniquement par R. 113-16.",
       "Le nombre de places, les coûts d'installation et les éventuelles exigences autonomes restent hors de cette disposition ; aucun gain national ou nouveau gain de renvoi n'est établi.",
       "Aucune charge nouvelle n'est identifiée : le texte demeure intégralement celui de la source, sans nouveau justificatif, registre, autorisation ou échéance.")

retain('R113-13',
       "Maintien utile des limites de l'obligation lors de travaux : au moins 10 places et rapport travaux/valeur du bâtiment atteignant un seuil réglementaire qui ne peut être inférieur à 2 %. Leur retrait, alors que L. 113-19 subsiste, pourrait étendre l'obligation aux petits parcs et aux travaux mineurs. La méthode de valeur permet d'appliquer ce filtre sans expertise immobilière individuelle imposée par cet article.",
       "L. 113-19 et R. 173-2 ont été lus dans le corpus. Le renvoi à R. 173-2 vise le coût de construction, pas son seuil propre de 25 % ni sa surface hors œuvre nette : la surface à utiliser ici reste celle de L. 111-14 du code de l'urbanisme. Aucun taux d'arrêté n'est inventé ; le plancher de 2 % et les 10 places sont conservés. L'arrêté conjoint n'est pas dans les sources assignées et n'est pas présenté comme réécrit.",
       "Aucune coupe n'est comptée : l'article borne favorablement le champ de l'équipement obligatoire ; le calcul légal de valeur et les deux seuils restent applicables aux futurs travaux.",
       "Le montant du seuil effectivement fixé par arrêté et le coût du calcul ne sont pas évalués ici. Le maintien ne vaut pas examen exhaustif de l'arrêté ni baisse de prélèvement.",
       "Aucune charge nouvelle n'est identifiée : maintien des conditions actuelles, sans expertise nouvelle, dossier de dérogation ni déclaration de remplacement.")

retain('R113-14',
       "Maintien intégral des deux seuils de 10 places destinées aux travailleurs, pour le propriétaire et pour le copropriétaire dont les lots comportent ces places privatives. Ils limitent le champ de L. 113-20 et évitent d'assujettir des petits parcs par la seule disparition de leur texte d'application. Aucune procédure d'emploi, cotisation ou autorisation n'est instituée par la référence aux travailleurs.",
       "L. 113-20, lu dans le corpus, vise les bâtiments existants tertiaires principalement professionnels. Le présent seuil ne l'étend pas aux autres bâtiments. Les I et II et la qualification de places privatives sont conservés, sans additionner artificiellement les places de lots de propriétaires différents. Note d'entrée en vigueur de 2022 conservée comme historique.",
       "Pas de réduction nouvelle démontrée : conservation du filtre favorable des 10 places et du champ respectif du propriétaire et du copropriétaire.",
       "La mesure ne supprime pas l'obligation législative d'équipement des bâtiments concernés ; aucune incidence chiffrée sur les entreprises ou la copropriété n'est calculée.",
       "Aucune charge nouvelle n'est identifiée : ni déclaration d'effectifs, ni autorisation, ni pièce supplémentaire n'est ajoutée au texte maintenu.")

retain('R113-15',
       "Maintien intégral : l'attente de l'échéance du bail de stationnement est la protection d'un droit contractuel existant, avec une voie immédiate déjà ouverte par l'accord du locataire. Retirer cette réserve permettrait la privation unilatérale d'une place louée ; il ne s'agit pas d'un délai administratif sans fonction. La règle reste applicable aux futurs baux et transformations.",
       "Le contrat visé est la location d'une place automobile, non un contrat de travail. L'accord du locataire permet déjà l'installation avant l'échéance ; aucune forme nouvelle d'accord ni indemnité forfaitaire n'est créée. L'allègement de R. 113-16 ne supprime ni les baux en cours ni cette faculté d'accord.",
       "Aucun allègement nouveau : l'article conserve la jouissance promise au locataire et la possibilité d'une transformation anticipée librement acceptée.",
       "Les règles autonomes du bail, les modifications contractuelles et les recours civils ne sont pas réécrits par cet article ; aucun coût national n'est établi.",
       "Aucune charge nouvelle n'est identifiée : la réserve du bail et son exception consensuelle sont maintenues sans autorisation ou justificatif supplémentaire.")

xml = by_number['R113-16']['source_xml']
xml = replace_once(xml, 'ces infrastructures sont couvertes, éclairées et closes.',
                   'ces infrastructures sont éclairées et closes.')
xml = replace_once(xml, 'ces infrastructures sont couvertes et éclairées.',
                   'ces infrastructures sont éclairées.')
xml += "<p>La suppression de l'obligation de couverture s'applique à compter de l'entrée en vigueur de la loi de réforme, y compris aux infrastructures existantes. Elle n'impose ni la dépose des couvertures existantes ni la modification des contrats valablement conclus et ne remet pas en cause les droits et recours relatifs aux faits antérieurs. Les prescriptions fondées sur une autre disposition demeurent applicables.</p>"
reduce('R113-16', xml,
       "Réforme de fond : suppression, dans les I et II, de la couverture systématique des infrastructures extérieures. La protection contre les intempéries ne justifie pas une obligation constructive générale au titre de la sécurisation antivol. Les portes sécurisées, la clôture du I, l'éclairage, l'alternative de surveillance du II, ses modalités et toutes les catégories de destinataires restent intégralement maintenus. Aucun agrément ni attestation ne remplace la couverture supprimée.",
       "Le renvoi de R. 113-12 reste utile. L. 113-18 à L. 113-20 ont été lus : le stationnement sécurisé reste obligatoire dans leur champ. Le texte ne supprime que la couverture exigée par R. 113-16 et non une protection distincte de sécurité, d'urbanisme ou un engagement contractuel. Vérifier l'arrêté conjoint pris en application de R. 113-18 et coordonner ses prescriptions si elles réitèrent cette couverture ; cet arrêté extérieur au lot n'a pas été réécrit. Aucun gain ne résulte de la suppression d'un abri déjà amorti ; coûts évités non chiffrés.",
       ["Obligation de couvrir systématiquement les stationnements extérieurs du I et du II, indépendamment du maintien des dispositifs antivol, de l'éclairage et de la clôture exigée au I."],
       impact('material_reduction',
              "La source entière exige une couverture extérieure dans les deux catégories d'usagers. La proposition retire cette dépense constructive obligatoire, sans supprimer l'éclairage ni le dispositif de sécurisation approprié de chacun des I et II.",
              "L'effet porte sur la seule obligation de couverture de cet article ; les obligations législatives, prescriptions autonomes et contrats subsistent. Aucun montant d'économie ou solde global de complexité n'est démontré.",
              "Aucune charge nouvelle n'est identifiée : aucune déclaration, justification d'équivalence, caméra ou assurance nouvelle ne remplace le toit supprimé ; les solutions de sécurité existantes restent les mêmes.",
              [effect('R113-16', 'obligation_removed', 'stationnement-velos-fin-couverture-obligatoire',
                      "Suppression de la couverture imposée aux infrastructures de stationnement extérieures, dans les deux régimes de sécurisation.",
                      "Couverture obligatoire des infrastructures extérieures du I et du II ; le I exige aussi clôture et éclairage, le II éclairage et surveillance ou fermeture sécurisée.",
                      "Aucune couverture imposée sur ce fondement ; clôture et éclairage du I, éclairage et dispositifs de sécurité propres aux deux régimes conservés.",
                      'legal_duty', "Propriétaires et constructeurs d'infrastructures extérieures de stationnement des vélos relevant des I et II.",
                      "Effet dès l'entrée en vigueur de la loi de réforme, installations existantes comprises ; aucune dépose imposée, contrats et recours antérieurs préservés.",
                      "Aucune procédure, attestation ou dépense obligatoire de remplacement ; prescriptions autonomes maintenues.",
                      "ces infrastructures sont couvertes, éclairées et closes.",
                      "ces infrastructures sont éclairées et closes.")]))

a = retain('R113-17',
       "Maintien intégral des trois allègements : dispense en l'absence d'espace accessible sans adaptation raisonnable et sûre, dispense lorsque la perte de places empêcherait de respecter le minimum du PLU, et absence de seconde mise en conformité lors de travaux si l'obligation de L. 113-20 est déjà satisfaite. Leur suppression aggraverait les obligations d'équipement conservées par la loi ; aucune procédure distincte d'agrément n'est ajoutée.",
       "L. 113-19 et L. 113-20 ont été lus intégralement dans le corpus. Les deux dérogations du I et le non-cumul du II restent ouverts aux situations futures éligibles ; leur maintien ne recrée ni quota SRU ni déclaration. La condition de sécurité d'une adaptation raisonnable n'est pas effacée. L'allègement de couverture de R. 113-16 n'exige pas de refaire une infrastructure déjà conforme.",
       "Aucune nouvelle réduction : maintien des dispenses d'impossibilité d'accès, de conflit avec les minima de stationnement du PLU et de double équipement après conformité à L. 113-20.",
       "Les obligations générales d'équipement subsistent ; l'article ne dispense pas d'une adaptation accessible et sûre lorsqu'elle est raisonnablement réalisable. Aucun bilan de coûts ni bénéfice fiscal n'est avancé.",
       "Aucune charge nouvelle n'est identifiée : pas de nouvelle demande, attestation, collecte ou autorisation pour conserver les dispenses et le non-cumul existants.")
a['benefit_review'] = "Le premier avantage est la dérogation lorsque aucun espace disponible n'est accessible au cycliste, sous la réserve existante d'une adaptation raisonnable et sûre. Le deuxième protège le respect du minimum de places automobiles fixé par le PLU. Le troisième écarte l'obligation de L. 113-19 lorsque celle de L. 113-20 est déjà satisfaite. Les trois restent intégralement applicables aux futures opérations et situations éligibles aussi bien qu'aux situations antérieures, sans agrément, justificatif ou délai nouveau. L'obligation générale subsistant, aucun de ces avantages n'est déclaré sans objet."

retain('R113-18',
       "Maintien utile de l'habilitation de dimensionnement, nécessaire à l'exécution du nombre minimal de places prévu par L. 113-18. Les quatre critères distinguent logements, travailleurs, agents ou usagers et capacité des parcs commerciaux ou cinématographiques. L'article ne comporte lui-même ni déclaration, rapport, autorisation ni taux à supprimer ; enlever l'habilitation sans fixer un régime complet laisserait l'obligation législative indéterminée.",
       "L. 113-18 à L. 113-20 ont été lus. Les renvois à R. 113-12 à R. 113-14 et R. 113-17 demeurent cohérents, ces textes et leurs dérogations étant conservés. L'arrêté d'application n'est pas fourni dans ce lot : aucun nouveau ratio ou surface minimale n'est inventé et son examen exhaustif n'est pas affirmé. La suppression de couverture est autonome et portée par R. 113-16.",
       "Aucune coupe comptée : maintien des critères de dimensionnement des infrastructures dans les quatre catégories, sans nouvelle exigence de surface ou de nombre.",
       "Le contenu chiffré de l'arrêté extérieur n'est pas audité ici ; la couverture du présent article ne vaut ni réécriture de cet arrêté ni démonstration d'une baisse de coût.",
       "Aucune charge nouvelle n'est identifiée : le texte d'habilitation demeure identique, sans déclaration périodique d'effectifs ni autorisation supplémentaire.")

xml = by_number['R113-19']['source_xml']
xml = replace_once(xml,
                   "est faite par lettre recommandée avec accusé de réception ou par acte d'huissier de justice et comporte les éléments suivants :",
                   "est faite par lettre recommandée avec accusé de réception, par acte de commissaire de justice ou par tout autre moyen légal donnant date certaine à sa réception. Elle comporte les éléments suivants :")
xml = replace_once(xml, "Les noms, prénoms, adresses postales et électroniques et coordonnées téléphoniques du ou des propriétaires",
                   "Les noms, prénoms et adresses postales du ou des propriétaires")
xml = replace_once(xml, "5° Le projet d'acte authentique prévu au I de l'article L. 113-5-1 ;",
                   "5° Abrogé pour les notifications régies par la présente rédaction ;")
xml = replace_once(xml, "6° Le projet de la convention prévue au II de l'article L. 113-5-1 ;",
                   "6° Abrogé pour les notifications régies par la présente rédaction ;")
xml += "<p>Les présentes dispositions s'appliquent aux notifications adressées à compter de l'entrée en vigueur de la loi de réforme. La validité des notifications antérieures et les délais qu'elles ont fait courir restent régis par les dispositions alors applicables, sans nouvel envoi ni reprise du délai d'opposition. La suppression des projets mentionnés aux anciens 5° et 6° ne modifie ni les conditions d'exercice des droits prévus aux I et II de l'article L. 113-5-1, par accord des propriétaires ou sur le fondement d'une décision de justice, ni l'obligation d'acquitter les indemnités avant les travaux.</p>"
reduce('R113-19', xml,
       "Réforme de fond du dossier initial de surplomb : retrait des coordonnées électroniques et téléphoniques obligatoires et des deux projets d'acte authentique et de convention, prématurés avant l'accord sur le surplomb. Ouverture de la notification à tout moyen légal donnant date certaine à la réception, avec maintien des canaux antérieurs. Le descriptif et les plans, la justification de la nécessité, les propositions indemnitaires, la reproduction de la loi et l'information sur les six mois d'opposition sont conservés. Les actes définitifs restent requis avant travaux.",
       "Les 5° et 6° restent à leur emplacement comme subdivisions abrogées ; les 1° à 4° et 7° ne sont pas renumérotés. L. 113-5-1 I/II/III a été confronté à sa source et à sa proposition dans reference-targets.json : ni ses 35 centimètres, ses deux mètres, ses six mois ni les indemnités préalables ne sont modifiés. R. 113-20 à R. 113-23 restent applicables. Le remplacement terminologique de l'huissier par le commissaire de justice ne compte pas comme un gain. L'ouverture d'un moyen de notification est ici expresse dans un rapport privé et ne repose pas sur une extension du CRPA ; un courriel ordinaire n'acquiert aucune présomption de réception. Les cibles travail imposées au contrôle sont étrangères à ce délai civil.",
       ["Obligation de fournir les adresses électroniques et coordonnées téléphoniques de tous les propriétaires et de leurs représentants dès la notification initiale.",
        "Obligation de joindre dès la notification le projet d'acte authentique du I et le projet de convention du II, sans retrait des actes définitifs avant travaux.",
        "Exclusivité de la lettre recommandée et de l'acte d'huissier pour la notification initiale, remplacée par un libre choix de moyens légalement recevables donnant date certaine à réception."],
       impact('material_reduction',
              "Le dossier entier reste substantiel mais deux projets juridiques et les contacts numériques obligatoires disparaissent réellement. Les autres pièces et la connaissance du droit d'opposition sont maintenues ; les actes définitifs ne sont pas transformés en une formalité nouvelle.",
              "Le délai légal d'opposition de six mois reste inchangé. Les économies de rédaction et de notification ne sont pas chiffrées ; aucun effet sur les droits de rupture d'un contrat de travail n'est produit.",
              "Aucune charge nouvelle n'est identifiée : le choix de moyens donnant date certaine est facultatif, le dossier restant et les actes définitifs existaient déjà. Aucun visa, déclaration ou nouvelle confirmation ne remplace les projets supprimés.",
              [effect('R113-19', 'compliance_cost_reduced', 'isolation-surplomb-notification-allegee',
                      "Retrait des deux projets juridiques obligatoires au stade de la notification initiale, avant accord sur les modalités définitives.",
                      "Le propriétaire devait joindre un projet d'acte authentique de surplomb et un projet de convention d'accès, même avant accord du voisin.",
                      "Les 5° et 6° sont abrogés pour les nouvelles notifications ; actes définitifs et protection indemnitaire avant travaux restent exigés.",
                      'legal_duty', "Propriétaires procédant à l'isolation extérieure par surplomb et leurs représentants.",
                      "Notifications nouvelles dès l'entrée en vigueur ; notifications antérieures et délai déjà engagé préservés, sans renvoi.",
                      "Aucun dossier alternatif ni déclaration de remplacement ; pièces techniques et indemnitaires des 2° à 4° conservées.",
                      "5° Le projet d'acte authentique prévu au I de l'article L. 113-5-1 ;",
                      "5° Abrogé pour les notifications régies par la présente rédaction ;"),
               effect('R113-19', 'obligation_removed', 'isolation-surplomb-notification-allegee',
                      "Fin de la collecte obligatoire des adresses électroniques et numéros de téléphone lors de la notification initiale.",
                      "Noms, prénoms, adresses postales et électroniques et coordonnées téléphoniques obligatoires pour les propriétaires et leurs représentants.",
                      "Noms, prénoms et adresses postales seuls restent obligatoires dans le 1°, avec le même champ de propriétaires et de représentants.",
                      'legal_duty', "Propriétaires du bâtiment à isoler et représentants concernés par le 1°.",
                      "Applicable aux notifications adressées après l'entrée en vigueur de la réforme ; les anciennes ne sont pas à refaire.",
                      "Aucune donnée ni registre de remplacement ; la remise volontaire de contacts n'est pas imposée.",
                      "Les noms, prénoms, adresses postales et électroniques et coordonnées téléphoniques du ou des propriétaires",
                      "Les noms, prénoms et adresses postales du ou des propriétaires"),
               effect('R113-19', 'compliance_cost_reduced', 'isolation-surplomb-notification-allegee',
                      "Ouverture de moyens légaux de notification autres que les deux supports exclusivement énumérés par la source.",
                      "Notification par lettre recommandée avec accusé de réception ou acte d'huissier seulement.",
                      "Ces deux voies demeurent ; tout autre moyen légal donnant date certaine à réception est également admis.",
                      'legal_duty', "Propriétaire notifiant le projet de surplomb au propriétaire voisin.",
                      "Voies ouvertes pour les notifications futures uniquement, sans modification du délai de six mois ni présomption nouvelle de réception.",
                      "Le support supplémentaire est facultatif et doit être légalement recevable ; aucun outil ou abonnement imposé.",
                      "est faite par lettre recommandée avec accusé de réception ou par acte d'huissier de justice",
                      "par tout autre moyen légal donnant date certaine à sa réception.")]))

retain('R113-20',
       "Maintien intégral des quatre éléments de la convention d'accès : périmètre et durée, installations provisoires et protection du fonds, indemnité, remise en état éventuelle. Ils limitent l'atteinte temporaire à la propriété du voisin et rendent son consentement effectif. Le retrait du projet de convention dans R. 113-19 ne supprime pas la convention définitive exigée par L. 113-5-1 II.",
       "Le renvoi vise le II de L. 113-5-1 et non une convention d'emploi. La durée à prévoir concerne exclusivement l'accès au fonds, sans fin automatique d'un contrat de travail. Les quatre rubriques sont conservées, notamment la remise en état seulement le cas échéant. Le texte n'impose ni dépôt administratif ni accord de tiers supplémentaire.",
       "Aucune réduction nouvelle : la convention reste la garantie concrète d'une occupation temporaire proportionnée du fonds d'autrui et de son indemnisation.",
       "L'allègement du stade initial est porté uniquement par R. 113-19. Aucun montant d'indemnité, délai d'emploi ou coût de travaux n'est déterminé ici.",
       "Aucune charge nouvelle n'est identifiée : maintien des quatre rubriques existantes, sans contrat supplémentaire ni extension des personnes ou installations concernées.")

retain('R113-21',
       "Maintien intégral de la voie judiciaire accélérée ouverte au propriétaire voisin faute d'accord, tant pour l'opposition que pour l'indemnité. Le délai de six mois est celui fixé par L. 113-5-1 III et n'est pas un délai réglementaire autonome supprimable ici. Retirer la compétence du juge ou son accès affaiblirait une protection essentielle de propriété et de recours.",
       "Le tribunal compétent demeure celui du lieu de l'immeuble surplombé, et le président statue selon la procédure accélérée au fond. Les droits visés restent ceux des I et II de L. 113-5-1 ; la nouvelle notification allégée de R. 113-19 continue de déclencher les six mois. Aucun délai de préavis du travail ne remplace ce délai de saisine civil.",
       "Aucun allègement compté : conservation d'une compétence juridictionnelle et d'un recours permettant de discuter une atteinte au fonds ou l'indemnisation.",
       "L'article n'écourte pas la procédure judiciaire, n'en chiffre pas les frais et ne modifie ni les motifs légaux d'opposition ni le délai législatif.",
       "Aucune charge nouvelle n'est identifiée : mêmes parties, même juge, même procédure et même délai, sans préalable amiable ou justificatif nouveau.")

retain('R113-22',
       "Maintien intégral : la motivation de l'opposition, les deux questions soumises à l'assemblée, les pièces jointes à la convocation et sa tenue à temps garantissent une décision collective informée sans perdre le recours de six mois. Les questions d'opposition et d'indemnisation ne sont pas nécessairement identiques ; les fusionner obligatoirement pourrait priver les copropriétaires d'un choix distinct.",
       "Les I et II de L. 113-5-1 fondent les deux droits ; son III fonde les six mois. Le dossier joint est celui effectivement notifié selon R. 113-19 révisé : il ne comprend donc plus les projets supprimés, sans nouvelle copie à constituer ni seconde réduction autonome comptée ici. Aucun renvoi au droit du travail ni mandat d'emploi n'est créé par la décision du syndicat.",
       "Pas de réduction nouvelle : maintien du consentement collectif éclairé et de l'accès au juge, avec application du dossier initial allégé sans réintroduction de ses pièces supprimées.",
       "Les majorités et modalités générales de copropriété restent soumises à leurs règles propres ; la réforme ne promet pas un vote ou une procédure complète en quinze jours.",
       "Aucune charge nouvelle n'est identifiée : l'information de l'assemblée et ses questions existaient déjà ; aucun document retiré de R. 113-19 n'est exigé à nouveau.")

retain('R113-23',
       "Maintien intégral : la signature des actes ou la décision de justice définitive et le paiement préalable des deux indemnités protègent la propriété avant des travaux qui l'affectent matériellement. Ces préalables ne constituent pas un agrément administratif redondant. L'allègement des projets au stade de notification ne peut supprimer le titre définitif, la convention ou l'indemnisation.",
       "L. 113-5-1 I et II sont visés pour le titre de surplomb, l'accès et les deux indemnités. L'alternative judiciaire reste distincte de la voie amiable ; la qualité de décision devenue définitive est maintenue, sans présumer l'exécution provisoire ni supprimer un recours. Ces indemnités foncières sont étrangères au barème d'indemnité de rupture du travail.",
       "Aucune réduction nouvelle démontrée : les conditions d'accès à des travaux affectant le fonds voisin et l'indemnisation préalable restent inchangées.",
       "La réforme ne supprime pas le délai nécessaire à une décision définitive et ne chiffre ni les indemnités ni les frais d'acte ; les droits de recours restent distincts.",
       "Aucune charge nouvelle n'est identifiée : mêmes titres et indemnités préalables, sans certification, assurance ou notification ajoutée.")

xml = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi de réforme. Aucune notification complémentaire de l'identité et des coordonnées des intervenants, de leur numéro d'inscription au répertoire des entreprises et de leurs établissements ou des numéros de police d'assurance n'est exigée sur son seul fondement après cette date, y compris pour une opération dont la notification initiale est antérieure.</p><p>Les notifications déjà effectuées demeurent valables et ne sont pas renouvelées. La suppression de ces envois ne modifie pas le point de départ ni la durée du délai d'opposition fixé par l'article L. 113-5-1 et rappelé par l'article R. 113-19. Les droits, responsabilités et recours relatifs aux faits antérieurs demeurent régis par les dispositions qui leur sont applicables.</p><p>Cette abrogation ne supprime ni les obligations d'assurance prévues aux articles L. 241-1 et L. 242-1 du code des assurances, ni les obligations résultant du titre de surplomb et de la convention d'accès, ni les droits à indemnisation du propriétaire voisin.</p>"
a = base('R113-24', xml,
         "Abrogation de fond de la seconde série obligatoire de notifications au voisin : les contacts des intervenants, identifiants d'entreprise et numéros d'assurance ne doivent plus être envoyés systématiquement ni par recommandé sur le seul fondement de cet article. La notification technique initiale, le titre définitif, la convention d'accès, l'assurance obligatoire et les droits indemnitaires ont des fondements distincts conservés. Aucun envoi, déclaration ou agrément de remplacement n'est créé.",
         "Portée bornée à R. 113-24 : il ne s'agit pas d'une suppression des assurances construction ni des obligations contractuelles d'information convenues. Les deux références au code des assurances sont reprises de la source, sans modification de leur contenu non fourni. L. 113-5-1 est fourni comme cible de contexte des articles précédents ; son renvoi de sauvegarde est ajouté ici et signalé, sans cible supplémentaire dans reference_checks, dont la liste requise pour cet article porte sur R. 113-19 et les trois articles du travail. R. 113-19 révisé conserve la notification initiale et ses six mois ; l'abrogation n'en reprend pas le délai. Pas de restitution générale de frais de recommandés ni d'extinction des responsabilités antérieures.",
         impact('material_reduction',
                "La source entière n'impose que des notifications complémentaires et leur mode d'envoi. Elles sont supprimées pour tous les envois futurs, y compris pour les projets déjà engagés ; les assurances et la protection réelle du voisin demeurent distinctes.",
                "Les devoirs d'assurance, les responsabilités, la convention d'accès et toute obligation autonome d'information subsistent. Le coût des envois supprimés n'est pas chiffré ; aucune baisse de prime d'assurance n'est affirmée.",
                "Aucune charge nouvelle n'est identifiée : pas de registre, de dossier d'assurance ou de notification alternative à déposer auprès du voisin ou d'une administration.",
                [effect('R113-24', 'obligation_removed', 'isolation-surplomb-fin-notifications-complementaires',
                        "Suppression complète du circuit de notifications complémentaires des intervenants et des polices d'assurance.",
                        "Notification des noms, contacts, identifiants d'entreprise et polices dès le choix des intervenants ou la souscription d'assurance, avec envoi complémentaire en recommandé.",
                        "Aucun de ces envois n'est dû sur R. 113-24 ; notification initiale, assurances obligatoires et protection indemnitaire demeurent.",
                        'legal_duty', "Propriétaires faisant isoler un bâtiment en surplomb d'un fonds voisin, y compris pour les opérations déjà notifiées.",
                        "Fin des envois sur ce fondement dès l'entrée en vigueur, sans renvoi des documents déjà transmis ni reprise du délai d'opposition ; responsabilités et recours anciens maintenus.",
                        "Aucune formalité de remplacement ; obligations autonomes d'assurance et engagements de la convention demeurent à leur champ propre.",
                        "Ces notifications complémentaires sont valablement faites par lettre recommandée avec demande d'avis de réception",
                        "Aucune notification complémentaire de l'identité et des coordonnées des intervenants, de leur numéro d'inscription au répertoire des entreprises et de leurs établissements ou des numéros de police d'assurance n'est exigée sur son seul fondement après cette date")]))
a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
         repeal_scope="Suppression pour tous les envois futurs des notifications complémentaires imposées par R. 113-24 sur les intervenants et leurs assurances, sans retrait des assurances, du titre de surplomb, de l'accès conventionnel ni des recours antérieurs.")

xml = clean(by_number['R114-1']['source_xml'])
xml = replace_once(xml, 'Ils remettent aux ministres un rapport annuel d\'activité.',
                   "Aucun rapport annuel d'activité distinct n'est exigé sur le seul fondement du présent article.")
xml += "<p>La suppression de ce rapport s'applique aux transmissions à effectuer à compter de l'entrée en vigueur de la loi de réforme, y compris lorsqu'elles portent sur une période antérieure. Elle ne dispense pas des informations et communications directement requises par les règlements de l'Union européenne mentionnés au I, ni des contrôles exercés sur leur fondement. Les rapports déjà remis ne sont pas à refaire.</p>"
reduce('R114-1', xml,
       "Réforme de fond limitée au rapport annuel d'activité distinct imposé par le II : sa remise systématique est supprimée sans rapport de remplacement. L'autorité notifiante de l'Etat, la désignation et les modifications par arrêté conjoint, les missions respectives au titre des deux règlements, le contradictoire de trois mois et le plafond d'un an de suspension restent intégralement maintenus. La notification et les contrôles de compétence des organismes ne sont pas des agréments inutiles : ils concourent à la fiabilité des produits de construction et résultent d'un cadre européen.",
       "Les I à IV restent numérotés et complets. La coupe concerne seulement la remise nationale distincte au ministre, jamais les informations et communications directement dues au titre des règlements 305/2011 et 2024/3110. Les articles européens 40, 43 et 53 sont identifiés par la source ; leur texte intégral n'est pas joint aux documents locaux, et aucune conformité européenne exhaustive ni économie portant sur leurs obligations n'est affirmée. Coordonner toute disposition nationale d'application qui reproduirait exclusivement ce rapport annuel ; les arrêtés de désignation ne sont pas présentés comme réécrits. Les trois mois de contradictoire et l'articulation des mesures urgentes de l'article 53 restent un point de contrôle européen, sans suppression implicite de ce dernier.",
       ["Obligation nationale de remettre systématiquement aux ministres un rapport annuel d'activité distinct, sans retrait des informations et contrôles directement imposés par les règlements européens."],
       impact('material_reduction',
              "La proposition retire la remise annuelle distincte de la source entière, y compris pour les transmissions futures relatives à un exercice passé. La désignation, le suivi et les garanties contradictoires des organismes notifiés restent en place.",
              "L'effet ne couvre pas les communications européennes directement obligatoires, dont les textes intégraux ne sont pas fournis ; le volume effectivement évité peut donc être limité. Aucun coût national ni conformité exhaustive n'est établi.",
              "Aucune charge nouvelle n'est identifiée : le rapport national n'est remplacé ni par une déclaration annuelle ni par un visa ; la réserve des obligations européennes conserve seulement leurs fondements propres.",
              [effect('R114-1', 'obligation_removed', 'produits-construction-fin-rapport-annuel-national',
                      "Suppression de la remise annuelle d'un rapport d'activité distinct sur le seul fondement national de R. 114-1 II.",
                      "Tous les organismes notifiés désignés par arrêté conjoint remettent un rapport annuel d'activité aux ministres.",
                      "Aucun rapport annuel distinct n'est dû sur cet article ; les informations directement requises par les règlements européens restent dues dans leur champ.",
                      'legal_duty', "Organismes notifiés du chapitre IV pour les produits de construction.",
                      "Suppression des transmissions nationales futures dès l'entrée en vigueur, même sur périodes antérieures ; rapports déposés non refaits.",
                      "Aucune transmission nationale équivalente de remplacement ; seules les exigences européennes autonomes et contrôles subsistent.",
                      "Ils remettent aux ministres un rapport annuel d'activité.",
                      "Aucun rapport annuel d'activité distinct n'est exigé sur le seul fondement du présent article.")]))

retain('R*114-2',
       "Maintien intégral de la demande écrite de notification : elle est rattachée aux articles 47 ou 50 des deux règlements européens, non à une autorisation nationale sans objet. Le délai de trois mois est un maximum de traitement et de refus motivé, pas une attente minimale imposée au demandeur. Un silence favorable ne saurait tenir lieu de la notification européenne effective d'un organisme chargé de vérifier des produits de construction.",
       "La demande demeure adressable à l'un ou l'autre ministre compétent. Les références européennes et le refus motivé dans le même délai sont conservés ; aucun dépôt double auprès des deux ministres n'est ajouté. La source ne comporte pas de point II : l'erreur du renvoi figurant à R. 114-4 est corrigée dans ce lot vers R. 114-3. Les textes intégraux des règlements ne sont pas fournis ; aucune dispense européenne ni validation de leur application transitoire n'est inventée.",
       "Pas de réduction comptée : le régime de notification, son délai maximal de trois mois et la décision motivée sont maintenus pour sécuriser la reconnaissance des organismes au niveau européen.",
       "Les modalités détaillées de dépôt et délais propres de la procédure européenne ne sont pas audités ici ; le maintien ne vaut ni rejet de simplifications futures ni conformité européenne certifiée.",
       "Aucune charge nouvelle n'est identifiée : même demande écrite, même choix initial de ministre et aucun nouveau certificat, taux, renouvellement ou délai minimal.")

xml = clean(by_number['R114-3']['source_xml'])
xml = replace_once(xml,
                   "sur demande motivée présentée par l'organisme au plus tard un mois avant son expiration",
                   "sur demande motivée présentée par l'organisme avant son expiration")
xml += "<p>La suppression de l'anticipation minimale d'un mois s'applique dès l'entrée en vigueur de la loi de réforme, y compris aux délais d'un an en cours à cette date. Les prorogations déjà accordées restent valables. Elle ne rouvre pas un délai déjà expiré, ne remet pas en cause un retrait définitivement intervenu et n'autorise aucune prorogation au-delà des six mois prévus au deuxième alinéa.</p>"
reduce('R114-3', xml,
       "Réforme de fond ciblée : suppression du dépôt de la demande de prorogation au moins un mois avant l'expiration du délai d'accréditation. Le dossier étant déjà suivi par le COFRAC et les ministres, cette anticipation uniforme n'est pas nécessaire au contrôle de compétence ; la demande motivée reste à présenter avant l'expiration. Les exigences d'accréditation, les tâches et annexes européennes, la recevabilité préalable, le délai d'un an, le retrait à défaut et les six mois de prorogation restent intacts.",
       "Le délai d'un an court toujours de la décision de recevabilité du COFRAC, non de la notification. Les six mois restent une prorogation facultative, non un droit automatique ni une suspension du délai par simple demande. L'assouplissement bénéficie aussi aux délais d'un an en cours, sans réouverture des délais expirés. L'habilitation provisoire favorable est conservée pour les futurs organismes éligibles. Les articles 46 et annexes V/IX européens ne sont pas modifiés ; leur texte intégral absent n'est pas reconstitué par inférence.",
       ["Obligation de présenter la demande motivée de prorogation au moins un mois avant la fin du délai d'un an, alors que la demande demeure requise avant son expiration."],
       impact('material_reduction',
              "L'anticipation minimale d'un mois disparaît réellement ; les demandes de prorogation peuvent être présentées pendant le dernier mois du délai initial. Le contrôle de compétence et la limite de six mois supplémentaires sont maintenus.",
              "L'article ne garantit ni l'accord de prorogation ni une décision avant l'expiration pour toute demande tardive. Un mois civil n'est pas converti fictivement en trente jours ; aucun allègement des exigences européennes n'est revendiqué.",
              "Aucune charge nouvelle n'est identifiée : la demande reste motivée comme auparavant, sans pièce, déclaration périodique ou frais nouveau ; seule sa date limite est assouplie.",
              [effect('R114-3', 'deadline_reduced', 'produits-construction-fin-anticipation-prorogation',
                      "Suppression du mois minimal d'anticipation pour demander la prorogation du délai d'accréditation.",
                      "Demande motivée au plus tard un mois avant l'expiration du délai d'un an courant de la recevabilité ; prorogation possible de six mois.",
                      "Demande motivée possible jusqu'avant l'expiration de ce même délai d'un an ; prorogation maximale inchangée de six mois.",
                      'other', "Organismes provisoirement notifiés dont la demande d'accréditation est recevable mais l'accréditation pas encore obtenue.",
                      "Applicable aux délais d'un an nouveaux ou encore en cours à la réforme, sans réouverture ni nouvelle prorogation après les six mois.",
                      "Aucune procédure de remplacement ; la motivation et la décision discrétionnaire de prorogation existaient déjà.",
                      "sur demande motivée présentée par l'organisme au plus tard un mois avant son expiration",
                      "sur demande motivée présentée par l'organisme avant son expiration")]))

xml = clean(by_number['R114-4']['source_xml'])
xml = replace_once(xml, "l'accréditation mentionnée au point II de l'article R. 114-2",
                   "l'accréditation mentionnée à l'article R. 114-3")
base('R114-4', xml,
     "Coordination nécessaire, sans allègement revendiqué : le renvoi au point II de R. 114-2 est incohérent, cet article n'ayant pas de II et réglant la demande de notification. R. 114-3 porte effectivement l'accréditation du COFRAC. Le corps entier est conservé avec ce seul remplacement de renvoi ; la faculté de définir les compétences minimales du personnel pour la vérification de la durabilité environnementale reste inchangée.",
     "Incohérence préexistante expressément signalée, et non corrigée silencieusement. R*114-2 et R. 114-3 ont été lus dans les sources assignées. Le nouveau renvoi à R. 114-3 n'est pas une cible fournie dans reference-targets.json ; il est fondé sur sa source intégrale présente dans ce lot et est signalé ici sans cible supplémentaire dans reference_checks. Le point 1.4 bis de l'annexe V et le point 4 de l'annexe IX sont conservés ; aucune concordance européenne complète ni obligation d'emploi à durée déterminée n'est déduite de la référence au personnel.",
     impact('coordination_only',
            "Seul le renvoi d'accréditation est rectifié vers son véritable siège réglementaire ; aucune compétence minimale, autorisation ou formalité n'est supprimée par cette correction.",
            "La validité et le contenu de l'arrêté éventuel de compétences, ainsi que le détail des annexes européennes non fournies, ne sont pas audités. Aucun gain financier ou de complexité n'est établi.",
            "Aucune charge nouvelle n'est identifiée : même faculté réglementaire, mêmes personnels et mêmes tâches ; le renvoi corrigé ne crée pas une nouvelle accréditation.",
            [effect('R114-4', 'coordination', 'produits-construction-renvoi-accreditation',
                    "Correction du renvoi inexistant au point II de R. 114-2 vers l'accréditation prévue à R. 114-3.",
                    "Renvoi à un point II absent de R. 114-2, dont le corps concerne la demande de notification.",
                    "Renvoi à R. 114-3 qui fixe les conditions d'accréditation et la notification provisoire.",
                    'other', "Organismes sollicitant l'accréditation pour vérifier l'évaluation de la durabilité environnementale et leurs personnels.",
                    "Coordination de référence sans changement du champ, des annexes visées ni des droits antérieurs.",
                    "Aucun agrément ou justificatif supplémentaire ; pas de seconde accréditation.",
                    "l'accréditation mentionnée au point II de l'article R. 114-2",
                    "l'accréditation mentionnée à l'article R. 114-3")]))

retain('R114-5',
       "Maintien intégral de la désignation et du contrôle des organismes d'évaluation technique au titre de l'article 39 du règlement 2024/3110. La compétence ministérielle assure la reconnaissance et le suivi d'une fonction technique européenne. Le retrait motivé après trois mois d'observations protège l'organisme ; ce délai favorable ne peut être supprimé comme une contrainte pesant sur lui. Aucun rapport périodique distinct n'est prescrit par cet article.",
       "Les organismes d'évaluation technique de cette section sont distincts des organismes notifiés de R. 114-1 : la suppression du rapport national de ces derniers ne retire pas la désignation ou les contrôles du présent article. Les I et II, les compétences respectives des ministres et les trois mois sont conservés. Le contenu intégral de l'article 39 européen n'est pas fourni ; son articulation avec d'éventuelles mesures immédiates reste à contrôler, sans l'effacer implicitement.",
       "Aucune réduction nouvelle : maintien du cadre de désignation et d'évaluation technique ainsi que de la motivation et du contradictoire protégeant l'organisme en cas de retrait.",
       "Le régime européen détaillé et les arrêtés individuels ne sont pas réécrits. Aucun délai global de commercialisation ni coût national n'est déduit du seul délai de trois mois.",
       "Aucune charge nouvelle n'est identifiée : aucun nouveau contrôle périodique, rapport, demande ou condition de recrutement n'est ajouté à la source maintenue.")

retain('R121-1',
       "Maintien intégral des missions de recherche, d'appui aux politiques publiques, de diffusion des connaissances et de coopération du CSTB. Les avis techniques sont justifiés par la nouveauté d'un procédé et l'expertise collective ; les prestations aux tiers du II sont réalisées à leur sollicitation. L'article n'oblige pas un constructeur à acheter une certification et ne crée ni prélèvement ni agrément obligatoire à supprimer. La mission publique de recherche répond notamment aux risques sanitaires et à la performance du bâti.",
       "L. 121-1 a été lu dans le corpus public : il fonde les recherches et l'appui aux politiques de construction et d'habitat. R. 121-7, R. 121-8 et R. 121-9 ont aussi été lus pour distinguer les compétences du conseil, la consultation scientifique et les ressources. Le présent maintien ne rend obligatoire aucun avis ou certificat facultatif et ne valide pas les tarifs de prestations. Aucune filiation SRU ou mission géotechnique particulière ne résulte de cet article.",
       "Aucune réduction comptée : maintien de missions scientifiques d'intérêt général et de services sollicités, qui ne sont pas par eux-mêmes des autorisations obligatoires imposées aux constructeurs.",
       "Le financement et les tarifs du CSTB, les textes extérieurs d'avis techniques et les exigences d'autres régimes de construction ne sont pas audités ici ; aucune économie budgétaire n'est annoncée.",
       "Aucune charge nouvelle n'est identifiée : aucune prestation, certification, donnée de chantier ou contribution n'est rendue obligatoire par le maintien du texte.")

retain('R121-2',
       "Maintien intégral de la composition pluraliste du conseil du CSTB : 27 membres répartis entre Parlement, Etat, collectivités, personnalités qualifiées et salariés. La réduction arbitraire du nombre de sièges pourrait altérer la représentation des salariés et les équilibres légaux du secteur public ; elle ne prouverait pas une économie, les fonctions étant en principe gratuites selon R. 121-3. Les modalités de désignation et d'élection sont nécessaires au fonctionnement de l'établissement.",
       "Contrôle arithmétique : 2 parlementaires + 6 représentants de l'Etat + 4 représentants des collectivités + 6 personnalités qualifiées + 9 salariés = 27. Les quatre associations et les six ministères restent nommés comme dans la source. La loi du 26 juillet 1983 est un fondement extérieur distinct, non réécrit dans ce lot ; aucune suppression de ses exigences de représentation ou d'élection n'est supposée. L'allègement du nombre minimal de séances relève de R. 121-6, non de la composition.",
       "Aucune coupe comptée : préservation des sièges et procédures de représentation, sans prétendre qu'un nombre de membres plus faible produirait une baisse démontrée de prélèvement ou de dépense.",
       "Le coût réel de gouvernance et les prescriptions intégrales de la loi de 1983 ne sont pas chiffrés ou réécrits. Le maintien porte sur la composition, non sur un objectif de rendement de l'établissement.",
       "Aucune charge nouvelle n'est identifiée : mêmes 27 sièges et mêmes voies de désignation ou d'élection, sans nouvelle commission ni nouvelle rémunération.")

xml = by_number['R121-3']['source_xml']
xml = replace_once(xml,
                   "Chaque année, le commissaire du Gouvernement vérifie auprès des membres du conseil d'administration qu'ils lui ont signalé les modifications intervenues dans les éléments figurant dans sa déclaration.",
                   "Le commissaire du Gouvernement peut vérifier auprès des membres du conseil d'administration qu'ils lui ont signalé les modifications intervenues dans les éléments figurant dans leur déclaration, sans périodicité annuelle obligatoire.")
xml += "<p>La suppression de la vérification annuelle obligatoire s'applique à compter de l'entrée en vigueur de la loi de réforme, sans confirmation annuelle ni rattrapage exigé sur ce seul fondement. Les déclarations et modifications déjà communiquées restent valables et confidentielles. Les contrôles en cours peuvent être poursuivis dans le cadre de la faculté de vérification maintenue par le présent article.</p>"
reduce('R121-3', xml,
       "Réforme de fond limitée au contrôle annuel systématique des mises à jour de déclarations : il devient facultatif, sans périodicité imposée et sans confirmation à néant. Le contrôle initial des conflits d'intérêts et les vérifications utiles subsistent. Tous les autres éléments sont maintenus, notamment cinq ans et trois mandats, remplacement, quatre absences, quinze heures mensuelles, gratuité et remboursement de frais, mandat de représentation unique, déclaration sous quinze jours, seuil d'un vingtième, interdiction de siéger en défaut, confidentialité, abstention et discrétion.",
       "La modification conserve le signalement des changements déjà présupposé par la source et la possibilité de le vérifier ; elle n'introduit pas une déclaration sur événement, de nouvelles rubriques ou un nouveau délai. Les destinataires et la communication au contrôleur économique et financier restent identiques. La déclaration initiale et le contrôle des intérêts personnels ont une fonction essentielle de prévention de la fraude et des conflits. Le délai de quinze jours porte sur la nomination ou la désignation d'un administrateur, non sur une rupture d'emploi. L'accord du représentant conserve sa forme écrite et un seul pouvoir peut être détenu.",
       ["Obligation pour le commissaire du Gouvernement de vérifier chaque année systématiquement les mises à jour des déclarations de tous les administrateurs ; pouvoir de vérification ciblée conservé sans confirmation annuelle à néant."],
       impact('material_reduction',
              "La source entière exigeait une vérification annuelle auprès des administrateurs. Ce passage devient une faculté de contrôle sans cadence annuelle imposée ; les déclarations initiales, mises à jour pertinentes et garanties d'intégrité demeurent.",
              "Il s'agit du retrait d'une tâche annuelle obligatoire du dispositif public, pas de la suppression de toutes les déclarations d'intérêts ni d'un gain fiscal. Les vérifications restent possibles, et leur volume ou coût net n'est pas estimé.",
              "Aucune charge nouvelle n'est identifiée : mêmes informations, seuils, personnes et destinataires. Les mises à jour restent celles déjà visées par la source ; aucun délai nouveau ou confirmation à néant n'est institué.",
              [effect('R121-3', 'obligation_removed', 'cstb-fin-verification-annuelle-systematique',
                      "Suppression de la cadence annuelle obligatoire de vérification des modifications des déclarations d'intérêts.",
                      "Le commissaire du Gouvernement vérifie chaque année auprès des membres si les modifications ont été signalées.",
                      "Le commissaire peut effectuer cette même vérification, sans cadence annuelle ni confirmation systématique à néant.",
                      'legal_duty', "Commissaire du Gouvernement auprès du CSTB et administrateurs interrogés dans ce cadre.",
                      "Suppression dès l'entrée en vigueur, sans rattrapage annuel ; déclarations existantes conservées et contrôles en cours possibles.",
                      "Aucun registre, champ de déclaration ou échéance de mise à jour supplémentaire ; le signalement des modifications et les contrôles utiles demeurent.",
                      "Chaque année, le commissaire du Gouvernement vérifie auprès des membres du conseil d'administration",
                      "sans périodicité annuelle obligatoire.")]))

retain('R121-4',
       "Maintien intégral de la désignation, des compétences et des suppléances de la présidence du CSTB. Les consultations du conseil préservent son rôle collégial, la représentation en justice et la qualité d'ordonnateur identifient le responsable, et les délégations permettent déjà une gestion souple. La durée de cinq ans est celle du mandat institutionnel, non celle d'un contrat de travail. Aucune procédure particulière de licenciement ni indemnité ordinaire n'est créée.",
       "Les I à V sont conservés : nomination et consultations, politique et représentation, direction et personnel, délégations et adjoints, intérim en cas de vacance. R. 121-7 lu dans le corpus précise les compétences et délégations du conseil ; aucun nouveau circuit d'autorisation n'est ajouté. Le III ne dispense le président employeur ni du droit du travail applicable aux personnels privés, ni des règles propres aux agents de statut public. Les trois cibles de reference-targets.json sont examinées sans les transformer en renvois normatifs du présent article.",
       "Aucune réduction nouvelle : conservation des responsabilités institutionnelles et possibilités de délégation, sans assimiler le mandat de cinq ans à un emploi à durée déterminée.",
       "L'article ne réécrit pas les contrats ou statuts du personnel et ne fixe ni procédure de rupture ni indemnité. Aucun effet chiffré de gouvernance ou d'emploi n'est démontré.",
       "Aucune charge nouvelle n'est identifiée : mêmes consultations, pouvoirs, délégations et intérim, sans formalité supplémentaire pour les salariés ou les membres du conseil.")

xml = "<p>Le ministre chargé de la construction nomme auprès du Centre scientifique et technique du bâtiment un fonctionnaire de son département pour y remplir les fonctions de commissaire du Gouvernement.</p><p>Le commissaire du Gouvernement est tenu régulièrement informé des projets et activités du centre et reçoit communication des documents nécessaires à cet effet.</p><p>Il assiste aux séances du conseil d'administration sans toutefois prendre part au vote.</p><p>Le commissaire du Gouvernement ne peut suspendre l'exécution d'une délibération du conseil d'administration sur le seul fondement du présent article.</p><p>Les contrôles et approbations imposés sur un fondement distinct, notamment les règles particulières d'exécution du budget et du compte financier, demeurent applicables.</p><p>À compter de l'entrée en vigueur de la loi de réforme, les suspensions fondées exclusivement sur le présent article cessent de produire effet, y compris lorsqu'elles ont été décidées auparavant. Les décisions ministérielles déjà prises, les contrats conclus, les actes exécutés et les recours demeurent régis par les règles qui leur sont applicables. Aucun nouveau délai d'attente n'est exigé sur ce seul fondement.</p>"
reduce('R121-5', xml,
       "Réforme de fond : suppression du pouvoir général d'opposition suspensive du commissaire du Gouvernement, du passage obligatoire au ministre lorsqu'il l'exerce et de l'attente associée pouvant durer un mois. L'information du commissaire, son accès aux séances sans voix délibérative et les contrôles autonomes, notamment budgétaires et comptables, subsistent. Le contrôle de toute délibération n'a pas à doubler systématiquement les compétences du conseil et ces contrôles spécialisés ; aucun visa de remplacement n'est institué.",
       "R. 121-6 est coordonné dans le même lot pour retirer la fenêtre d'opposition de dix jours et la transmission procédurale au ministre. Les conditions particulières du budget et du compte financier demeurent celles de R. 121-7, lu intégralement, et du décret du 7 novembre 2012 qu'il vise, non réécrit ici. Le commissaire conserve les documents, le contrôle des intérêts de R. 121-3 et les séances ; la suppression ne supprime ni responsabilité, fraude, contrôle financier ni recours. Les suspensions encore en cours sur ce seul fondement cessent ; une décision ministérielle déjà prise n'est pas annulée automatiquement. Ce mécanisme était une opposition éventuelle, pas un agrément préalable universel.",
       ["Pouvoir général du commissaire du Gouvernement de suspendre toute délibération jusqu'à décision ministérielle et mécanisme d'attente pouvant durer un mois, hors contrôles et approbations fondés sur des dispositions autonomes."],
       impact('material_reduction',
              "La possibilité de bloquer toutes les délibérations sur ce seul fondement disparaît et les suspensions correspondantes en cours cessent. L'information et les contrôles spécialisés demeurent ; il n'est pas prétendu que chaque délibération subissait auparavant un mois d'attente.",
              "Les effets sont limités à l'opposition générale de R. 121-5 et à sa procédure de R. 121-6 ; budgets, comptes, contrôles autonomes et décisions ministérielles déjà prises gardent leur régime. Les délais effectivement évités et le solde de coût public sont inconnus.",
              "Aucune charge nouvelle n'est identifiée : aucune déclaration ni autorisation équivalente ne remplace l'opposition. Les informations et contrôles explicitement conservés existaient déjà.",
              [effect('R121-5', 'obligation_removed', 'cstb-fin-opposition-suspensive-generale',
                      "Suppression de la soumission des délibérations à une opposition suspensive générale suivie d'une décision du ministre.",
                      "Le commissaire peut suspendre l'exécution ; le ministre doit décider dans le mois de la réception, à défaut de quoi la délibération devient exécutoire.",
                      "Aucune suspension sur R. 121-5 ; fin des suspensions encore fondées exclusivement sur lui ; règles particulières des budgets et comptes conservées.",
                      'legal_duty', "CSTB, son conseil et sa direction ; commissaire du Gouvernement et ministre dans cette procédure générale.",
                      "Dès l'entrée en vigueur, y compris suspensions en cours, sans annulation des décisions déjà prises, contrats exécutés ou recours antérieurs.",
                      "Aucun visa ou envoi de remplacement ; les contrôles autonomes et l'information existante demeurent.",
                      "Il peut suspendre l'exécution des délibérations du conseil jusqu'à décision du ministre chargé de la construction.",
                      "Le commissaire du Gouvernement ne peut suspendre l'exécution d'une délibération du conseil d'administration sur le seul fondement du présent article.")]))

xml = by_number['R121-6']['source_xml']
xml = replace_once(xml, "se réunit sur la convocation de son président au moins trois fois par an.",
                   "se réunit sur la convocation de son président, sans nombre minimal annuel de séances imposé par le présent article.")
xml = replace_once(xml,
                   "Le commissaire du Gouvernement dispose d'un délai de dix jours après notification du procès-verbal de la séance pour informer éventuellement le président de son opposition à la délibération du conseil d'administration et transmettre cette dernière au ministre chargé de la construction.",
                   "La notification du procès-verbal au commissaire du Gouvernement n'ouvre aucun délai d'opposition suspensive sur le fondement du présent article. Les règles particulières d'exécution du budget et du compte financier demeurent applicables.")
xml += "<p>La suppression du nombre minimal annuel de séances et du délai d'opposition s'applique dès l'entrée en vigueur de la loi de réforme, sans séance de rattrapage ni nouvelle notification des procès-verbaux antérieurs. Les convocations régulièrement adressées demeurent valables. Les obligations de délibérer résultant des autres dispositions et la convocation à la requête de trois membres ou du commissaire du Gouvernement restent applicables.</p>"
reduce('R121-6', xml,
       "Réforme de fond : retrait du minimum uniforme de trois séances annuelles, sans supprimer les séances nécessaires aux décisions obligatoires ni la convocation exigible par trois membres ou le commissaire. Coordination de la fin de l'opposition suspensive de R. 121-5 par suppression de sa fenêtre de dix jours et du circuit de transmission au ministre. L'ordre du jour et ses pièces dix jours à l'avance, le contrôle consultatif, le quorum, la reconvocation sous quinze jours, la majorité, la voix prépondérante et le procès-verbal signé sont maintenus.",
       "Les sept alinéas initiaux gardent leur place ; le quatrième demeure celui du quorum et le renvoi du cinquième à ce quatrième alinéa est conservé. Les dix jours d'information avant séance ne sont pas les dix jours d'opposition supprimés. R. 121-7 lu dans le corpus conserve les délibérations budgétaires, comptables et autres obligatoires ; elles ne peuvent être évitées faute de minimum général de réunions. La suppression d'opposition est une seule mesure avec R. 121-5, dont le présent article est l'exécution coordonnée, sans seconde opposition ou taxe supprimée comptée. Les convocations existantes sont valables et aucune séance de rattrapage n'est créée.",
       ["Minimum uniforme de trois réunions annuelles du conseil d'administration, sans retrait des réunions requises pour les décisions obligatoires ou à la demande des personnes habilitées.",
        "Délai de dix jours d'opposition du commissaire après notification du procès-verbal et transmission au ministre propres au pouvoir général de suspension supprimé à R. 121-5."],
       impact('material_reduction',
              "Le nombre minimal de trois séances est retiré ; les membres peuvent encore provoquer une réunion et les décisions obligatoires doivent être prises. La fenêtre d'opposition est supprimée par coordination de la même mesure que R. 121-5, sans la compter comme une seconde réduction indépendante.",
              "Les dix jours d'information avant séance, le quorum, le délai maximal de quinze jours de reconvocation et les décisions obligatoires restent inchangés. Le nombre réel de séances évitables et le solde de coût public ne sont pas établis.",
              "Aucune charge nouvelle n'est identifiée : pas de rapport, consentement unanime ou procédure écrite de remplacement ; mêmes garanties de participation et contrôles financiers autonomes.",
              [effect('R121-6', 'obligation_removed', 'cstb-fin-minimum-trois-reunions',
                      "Suppression du nombre minimal uniforme de trois séances du conseil par an.",
                      "Conseil convoqué au moins trois fois par an, en plus des réunions exigibles à la requête de trois membres ou du commissaire.",
                      "Aucun minimum annuel sur cet article ; convocation à la requête maintenue et délibérations obligatoires d'autres textes toujours requises.",
                      'legal_duty', "Président et membres du conseil d'administration du CSTB et services préparant les séances.",
                      "Suppression immédiate du minimum, sans rattrapage pour l'année en cours ni invalidation des convocations existantes.",
                      "Aucune consultation ou transmission supplémentaire ; maintien des réunions utiles et légalement obligatoires.",
                      "Le conseil d'administration se réunit sur la convocation de son président au moins trois fois par an.",
                      "Le conseil d'administration se réunit sur la convocation de son président, sans nombre minimal annuel de séances imposé par le présent article."),
               effect('R121-6', 'coordination', 'cstb-fin-opposition-suspensive-generale',
                      "Retrait de la fenêtre procédurale de dix jours donnant effet au pouvoir d'opposition déjà supprimé à R. 121-5.",
                      "Dix jours après le procès-verbal pour informer de l'opposition et transmettre la délibération au ministre.",
                      "Aucun délai d'opposition suspensive sur cet article ; les contrôles budgétaires et comptables autonomes demeurent.",
                      'legal_duty', "Commissaire du Gouvernement, président du CSTB et ministre chargé de la construction.",
                      "Même entrée en vigueur que la fin du pouvoir général ; pas de nouvelle notification des procès-verbaux antérieurs.",
                      "Aucun circuit de visa ou rapport de remplacement, et pas de seconde réduction autonome comptée.",
                      "Le commissaire du Gouvernement dispose d'un délai de dix jours après notification du procès-verbal de la séance",
                      "La notification du procès-verbal au commissaire du Gouvernement n'ouvre aucun délai d'opposition suspensive sur le fondement du présent article.")]))


work_preavis = 'LEGITEXT000006072050|LEGIARTI000006901112'
work_contract = 'LEGITEXT000006072050|LEGIARTI000019071087'
work_indemnity = 'LEGITEXT000006072050|LEGIARTI000035644154'
surplomb_law = 'LEGITEXT000006074096|LEGIARTI000043966798'
surplomb_notice = 'LEGITEXT000006074096|LEGIARTI000045960527'

checks = {
    'R113-19': {
        work_preavis: "L. 1234-1 concerne le préavis de licenciement, avec six mois/deux ans d'ancienneté dans la source et quinze jours pour les nouveaux contrats dans la proposition. R. 113-19 déclenche une opposition foncière de six mois après notification au voisin : ce n'est ni un préavis d'emploi ni un renvoi au code du travail. Aucune substitution de quinze jours n'est opérée.",
        work_contract: "L. 1221-2 porte sur la durée des contrats de travail privés, sa proposition supprimant les nouveaux CDD. Ici, la notification vise une isolation et les propriétaires du fonds voisin ; les projets de titre réel et de convention d'accès supprimés du dossier initial n'étaient pas des contrats de travail. Les droits des anciens salariés et des futurs contrats uniques ne sont pas affectés.",
        work_indemnity: "L. 1234-9 distingue l'indemnité de licenciement de la source, ouverte à huit mois, et l'indemnité proposée au seuil d'un an au terme effectif, préavis inclus. Le 4° de R. 113-19 vise au contraire les indemnités foncières préalables des I et II de L. 113-5-1 : elles restent proposées sans appliquer zéro, 0,20 mois ou plafond de six mois.",
        surplomb_law: "La source et la proposition de L. 113-5-1 maintiennent en I le droit de surplomb de 35 cm au plus, la hauteur minimale de deux mètres sauf accord et le titre authentique ou judiciaire ; le II exige la convention d'accès et l'indemnité. Le III impose la notification et six mois d'opposition. R. 113-19 retire seulement deux projets précoces et des contacts ; il conserve les justificatifs du 3°, l'indemnisation du 4° et l'information du 7°. Les actes définitifs restent requis avant travaux."
    },
    'R113-20': {
        work_preavis: "L. 1234-1 vise une durée de préavis de licenciement et une ancienneté d'emploi. La durée prévue au 1° de R. 113-20 est celle de l'accès temporaire au fonds voisin, à convenir pour les travaux. Elle reste proportionnée à cet accès, sans reprise du préavis de quinze jours proposé ni des seuils de six mois et deux ans.",
        work_contract: "La convention du II de L. 113-5-1 précise l'occupation du fonds, les installations et sa remise en état ; elle ne recrute aucun salarié. L. 1221-2, dont la proposition impose l'emploi nouveau à durée indéterminée, n'interdit donc pas de prévoir une durée limitée d'accès ou de chantier dans cette convention. Aucune fin de contrat d'emploi n'en découle.",
        work_indemnity: "Le 3° de R. 113-20 fixe l'indemnité due au propriétaire voisin en contrepartie de l'accès et des installations, sans condition d'ancienneté. L. 1234-9 porte sur la rupture d'emploi : ni le seuil ancien de huit mois ni le seuil proposé d'un an, ni le taux de 0,20 mois et le plafond de six mois ne sont applicables à cette indemnisation foncière.",
        surplomb_law: "Le renvoi unique vise expressément le II de L. 113-5-1 : accès temporaire, installations strictement nécessaires, indemnité et convention. Les quatre rubriques de R. 113-20 en précisent l'exercice sans étendre le droit de surplomb du I. La suppression du projet en amont dans R. 113-19 laisse la convention définitive obligatoire et les avantages du droit de surplomb ouverts aux opérations futures éligibles."
    },
    'R113-21': {
        work_preavis: "La saisine du président du tribunal judiciaire dans les six mois de notification est un délai civil d'opposition au surplomb ou de fixation d'indemnité. L. 1234-1 régit le préavis de licenciement, non ce recours réel ; ses seuils d'ancienneté et le préavis proposé de quinze jours sont inapplicables. Le délai et la procédure accélérée de R. 113-21 restent inchangés.",
        work_contract: "L. 1221-2 traite du contrat de travail et de ses termes possibles dans la source, supprimés pour les nouveaux emplois par la proposition. R. 113-21 détermine un juge et un délai de recours entre propriétaires, sans contrat d'emploi ni terme de mission. Le contrat unique n'a donc pas à modifier ce recours ni les six mois de saisine.",
        work_indemnity: "L. 1234-9 et son seuil proposé d'un an au terme effectif concernent l'indemnité ordinaire de rupture patronale. Le juge de R. 113-21 fixe les indemnités foncières des I et II de L. 113-5-1 à défaut d'accord. Leur ouverture n'est pas subordonnée à l'ancienneté et leur montant n'est pas calculé en mois de salaire ; aucun plafond de six mois n'y est importé.",
        surplomb_law: "Les I et II de L. 113-5-1 définissent les droits auxquels le voisin peut s'opposer dans le champ du III ; ce III donne six mois à compter de la notification et permet aussi de faire fixer l'indemnité préalable. La source et la proposition cible conservent cette structure. R. 113-21 maintient le juge du lieu du fonds, la procédure accélérée au fond et ce même délai, sans l'allonger ni le rendre orphelin."
    },
    'R113-22': {
        work_preavis: "La réunion de copropriété doit préserver la saisine dans les six mois de L. 113-5-1 III. Ce n'est pas une consultation d'un employeur avant licenciement. L. 1234-1 et son préavis proposé de quinze jours ne remplacent ni le délai civil ni l'information des copropriétaires ; aucune ancienneté de travail n'est exigée du syndicat ou du syndic.",
        work_contract: "Le mandat du syndic et la décision du syndicat concernent l'exercice d'un droit sur un immeuble, non une embauche relevant de L. 1221-2. Le contrat unique et la fin des nouveaux CDD n'interdisent pas une assemblée ou un accès de chantier de durée limitée. R. 113-22 ne crée aucun emploi à terme ni exception spéciale au futur contrat unique.",
        work_indemnity: "La seconde question d'assemblée porte sur la saisine du juge pour les indemnités de surplomb et d'accès de L. 113-5-1. Elle reste distincte de l'opposition au projet. L. 1234-9 et son indemnité de rupture, ancienne à huit mois et proposée à un an avec préavis inclus, sont étrangers à cette réparation foncière ; aucune règle de zéro ou de plafond n'y est transposée.",
        surplomb_law: "R. 113-22 renvoie aux droits des I et II de L. 113-5-1 et au délai de six mois du III. La décision motivée du syndicat et l'assemblée en temps utile rendent le recours effectif. Le dossier remis à l'assemblée reste celui effectivement notifié, allégé par R. 113-19 sans reconstitution des projets supprimés ; les motifs légaux d'opposition et les indemnités ne sont pas réduits."
    },
    'R113-23': {
        work_preavis: "Le préalable d'acte ou de jugement définitif de R. 113-23 est un titre d'intervention sur le fonds voisin, non un préavis de licenciement. La source de L. 1234-1 et sa proposition de quinze jours restent au champ de l'emploi. Elles ne permettent pas de commencer les travaux quinze jours après notification ni d'écarter l'indemnité préalable ou la convention d'accès.",
        work_contract: "L. 1221-2 vise la relation de travail ; l'acte authentique et la convention mentionnés ici mettent en œuvre un surplomb et un accès immobilier. La future interdiction des nouveaux CDD ne supprime pas ces actes ni ne transforme leur durée d'accès en durée d'emploi. R. 113-23 ne crée ni terme automatique d'emploi ni dérogation au contrat unique.",
        work_indemnity: "Les indemnités préalablement acquittées dans tous les cas sont celles du propriétaire voisin prévues par L. 113-5-1 I et II. Elles ne sont pas l'indemnité de L. 1234-9 : le seuil de huit mois de la source ou d'un an proposé, le taux de 0,20 mois et le plafond de six mois sont sans application. Leur paiement avant travaux est entièrement conservé.",
        surplomb_law: "Le I de L. 113-5-1 exige un titre authentique ou judiciaire publié et l'indemnité de surplomb ; le II prévoit la convention d'accès et son indemnité. R. 113-23 maintient ces protections et l'alternative d'une décision de justice devenue définitive. La suppression des seuls projets dans R. 113-19 ne dispense pas des actes définitifs et ne ferme pas le droit de surplomb pour les nouvelles opérations."
    },
    'R113-24': {
        work_preavis: "Les notifications complémentaires de R. 113-24 portent sur les intervenants de chantier et leurs assurances, jamais sur une rupture d'emploi. L. 1234-1 et sa proposition de préavis individuel de quinze jours sont donc hors champ. L'abrogation ne modifie pas le délai foncier de six mois, son point de départ, les règles de notification d'un licenciement ou les garanties des anciens contrats.",
        work_contract: "Le choix d'une entreprise et la durée d'un chantier ne sont pas le contrat de travail des intervenants. L. 1221-2, dont la proposition supprime les nouveaux CDD, ne justifie ni le maintien de ces notifications immobilières ni une exception d'emploi à terme. L'abrogation enlève le seul circuit informatif au voisin sans fixer la durée des emplois ni supprimer leurs droits.",
        work_indemnity: "L. 1234-9 traite de l'indemnité patronale de rupture et de son ancienneté : huit mois dans la source, un an au terme effectif dans la proposition. Aucun de ces paramètres n'est visé par l'envoi de polices d'assurance de R. 113-24. Son abrogation ne réduit ni les indemnités foncières du voisin ni les droits des salariés, anciens ou futurs, ni leurs réparations spéciales.",
        surplomb_notice: "La cible fournie R. 113-19 est uniquement sa source officielle, sans proposition dans la vue. Elle définit la notification initiale et rappelle le point de départ des six mois d'opposition. La proposition du présent lot y supprime seulement des pièces initiales ; l'abrogation de R. 113-24 retire le circuit complémentaire sans supprimer cette notification initiale, remettre le délai à zéro ou imposer un nouvel envoi pour les projets antérieurs."
    },
    'R121-4': {
        work_preavis: "Le III de R. 121-4 attribue au président la gestion du personnel mais ne règle aucun préavis et ne déroge pas au droit applicable. L. 1234-1 conserve les anciens contrats selon sa transition et propose quinze jours pour les contrats nouveaux privés. Ce préavis individuel n'efface ni procédures collectives ni autorisations protectrices ; le mandat institutionnel de cinq ans ne devient pas un préavis ou une durée d'emploi.",
        work_contract: "La nomination pour cinq ans au I est un mandat de présidence, pas un CDD de salarié. L. 1221-2 vise l'emploi privé et sa proposition impose les nouveaux contrats à durée indéterminée ; la compétence de gestion du III n'autorise donc aucun nouveau CDD. Les statuts publics éventuels restent distincts et le texte institutionnel n'est pas transformé en réforme implicite de ces agents.",
        work_indemnity: "R. 121-4 ne fixe aucune indemnité de rupture du personnel ou du président. L. 1234-9, source et proposition distinguées, reste au champ de l'emploi privé : seuil proposé d'un an au terme effectif avec préavis, puis 0,20 mois par année totale et plafond de six mois, sans atteinte aux droits antérieurs et spéciaux. La fin d'un mandat de cinq ans ne déclenche pas artificiellement ce barème."
    }
}

for s in sources:
    number = s['number']
    a = answers[number]
    required = references['requirements'][s['code_id'] + '|' + s['source_id']]
    assert set(checks.get(number, {})) == set(required), number
    a['reference_checks'] = [
        dict(target_key=key, view_sha256=references['targets'][key]['view_sha256'],
             assessment=checks[number][key])
        for key in required
    ]

ordered = [answers[s['number']] for s in sources]
assert len(ordered) == 24
with open('answer.json', 'w') as f:
    json.dump(ordered, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('answer.json :', len(ordered), 'articles')
