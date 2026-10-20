import json
import re
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent
sources = json.loads((ROOT / 'source.json').read_text())
refs = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def p(text):
    return '<p>' + escape(text, quote=False) + '</p>'


def body(*paragraphs):
    return '\n'.join(p(t) for t in paragraphs)


def paragraphs(number):
    return [unescape(re.sub('<[^>]+>', '', t)) for t in re.findall(r'<p(?:\s[^>]*)?>(.*?)</p>', by_number[number]['source_xml'], re.S)]


def entry(number, reason, notes, assessment, limits, burdens, proposed=None,
          category='retained_necessary', effects=None, removed=None, repeal=None):
    src = by_number[number]
    a = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        a['classification'] = 'retained_necessary'
    a['substantive_impact'] = dict(version=1, classification=category,
        assessment=assessment, scope_limitations=limits,
        new_burdens_review=burdens, effects=effects or [])
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal)
    a['reference_checks'] = []
    answers[number] = a
    return a


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
        before=before, after=after, unit=unit, affected_population=population,
        conditions_and_transition=transition,
        replacement_or_new_burdens=burdens,
        source_quote=source_quote, proposed_quote=proposed_quote)


entry('L2261-14-3',
    "Maintien intégral de la faculté de négocier par anticipation un accord de substitution et de révision lors d'une restructuration. Elle évite une succession de négociations après le transfert, sans imposer de dossier, de prélèvement, d'autorisation ni de négociation supplémentaire. L'entrée en vigueur liée à la réalisation de l'opération protège la continuité conventionnelle. Aucun changement de fond ni simple réécriture stylistique n'est proposé.",
    "L'article porte sur la mise en cause des accords, non sur la rupture des contrats. L2261-14-4 fixe les périmètres de majorité ; L2232-12 et L2232-13 ont été lus dans le corpus. L1224-1 y confirme la poursuite des contrats : le transfert ne déclenche ni préavis, ni indemnité ordinaire, ni nouvel essai. Le contrat antérieur conserve son régime et son ancienneté ; l'accord collectif ne peut créer un nouveau CDD. Voir les trois vérifications ciblées jointes.",
    "La source entière offre une négociation anticipée facultative ; aucune obligation supprimable distincte ou baisse de prélèvement n'y est démontrée. Le maintien conserve cet outil de continuité des droits collectifs.",
    "Aucun gain nouveau n'est compté ; l'article ne règle ni la validité de l'opération de transfert, ni les licenciements éventuellement décidés séparément, ni le régime public.",
    "Aucune charge nouvelle n'est identifiée : maintien du texte officiel entier, sans registre, déclaration, agrément ou délai ajouté.")

entry('L2261-14-4',
    "Maintien des règles de majorité et des périmètres de consultation propres aux deux voies de substitution anticipée. La distinction entre entreprise transférante et chaque entreprise concernée empêche qu'un accord soit validé sur un corps électoral inadéquat. Il ne s'agit pas d'une transmission supplémentaire à la CPPNI ; supprimer ces règles atteindrait le consentement collectif. Aucun nouveau corps n'est nécessaire.",
    "Lecture de L2261-14-2 : accord transitoire d'au plus trois ans ; L2261-14-3 : accord de substitution et de révision. L2232-12 conserve plus de 50 %, la voie de plus de 30 % et la consultation, et L2232-13 le collège catégoriel. Les taux ne sont ni des conditions d'ancienneté, ni des délais de préavis ; ils s'apprécient dans les périmètres des 1° et 2°. Les trois cibles imposées sont examinées sans leur attribuer de renvoi textuel absent.",
    "La source complète organise la légitimité des accords anticipés ; son maintien ne supprime aucune obligation mais protège l'assiette des majorités et la consultation dans chaque périmètre pertinent.",
    "Aucun raccourcissement des délais de consultation ni modification des seuils de validité n'est revendiqué. Les règles individuelles de rupture sont extérieures à cet article.",
    "Aucune charge nouvelle n'est identifiée : les mêmes majorités et consultations restent applicables, sans nouvelle pièce ou transmission.")

entry('L2261-15',
    "Maintien de l'extension par arrêté après avis motivé : rendre un accord obligatoire à des non-signataires exige un contrôle de légalité et une délibération représentative. La règle de durée et de conditions évite d'étendre indéfiniment un accord éteint. Ce n'est pas un agrément d'embauche ; sa suppression retirerait aussi l'accès des salariés et entreprises non adhérents aux garanties et dérogations conventionnelles futures. L'allègement du doublon préalable est porté par L2261-24.",
    "Sous-section 2 et procédure de la sous-section 3 examinées dans le lot. L2261-24 proposé retire l'avis avant le simple engagement, sans retirer l'avis avant l'arrêté exigé ici. Les arrêtés antérieurs et les extensions futures restent possibles pour leur durée conventionnelle. La note de 2020 fixe l'entrée en vigueur historique au 1er juin 2021 ; elle n'est pas la date de la réforme proposée.",
    "La source entière est conservée : le contrôle de l'extension et l'accès à ses effets ne constituent pas une charge privée redondante dont la suppression serait démontrée. Le seul doublon est traité à son article propre.",
    "Aucune autorisation ni taxe n'est supprimée ici ; l'allègement de L2261-24 ne doit pas être compté une seconde fois dans cet article.",
    "Aucune charge nouvelle n'est identifiée, puisque l'arrêté, l'avis motivé et la durée conventionnelle sont maintenus sans circuit supplémentaire.")

entry('L2261-16',
    "Maintien de la faculté d'étendre avenants et annexes. Elle permet aux bénéficiaires non signataires d'accéder aux améliorations et dérogations nouvelles sans renégocier la convention entière. Le champ de référence assorti de la possibilité d'un champ expressément différent est une souplesse conservée. Aucun dossier autonome, taxe ou délai minimal n'est créé par cet article.",
    "Le renvoi à la sous-section 3 reste opérant malgré ses allègements dans le présent lot. Le champ différent doit toujours résulter de dispositions expresses ; ne pas étendre un avenant au-delà de ce champ par une simple référence à la convention principale. Les annexes conventionnelles ne sont pas les annexes du CGI et la règle ne fixe aucune durée du contrat de travail.",
    "La disposition entière est une faculté nécessaire d'actualisation et de modulation du champ des accords étendus. Son maintien ne produit aucune réduction normative nouvelle.",
    "Les formalités de la procédure d'extension restent à leur champ ; aucun effet sur les taux fiscaux ou sur la durée de l'emploi n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : maintien de la faculté existante et de son champ, sans déclaration ou autorisation de remplacement.")

entry('L2261-17',
    "Maintien du remède à l'impossibilité persistante de négocier : l'élargissement donne accès à une couverture conventionnelle existante et à ses avantages. Les trois voies, l'analogie des emplois pour les 1° et 2°, l'opposition majoritaire écrite et motivée et les avenants ultérieurs sont conservés. Les supprimer indistinctement fermerait des garanties et dérogations pour les secteurs futurs non couverts ; la fonction de protection n'est pas doublonnée par une simple négociation d'entreprise.",
    "Les 1° et 2° exigent un accord déjà étendu et des emplois analogues ; le 3° concerne un accord interprofessionnel étendu. Ne pas assimiler cet élargissement pour carence persistante à une fusion forcée de branches, retirée du I de L2261-32. L2261-29 et L2261-30 continuent de régler la caducité. La note d'entrée en vigueur de 2021 est historique. Aucun quota SRU ni régime public n'est concerné.",
    "Aucune suppression n'est retenue après examen complet : la couverture en cas de carence, ses conditions ciblées et le veto majoritaire sont nécessaires pour étendre légitimement les droits aux secteurs dépourvus d'accord.",
    "Le maintien n'affirme ni disparition de l'arrêté d'élargissement ni baisse des charges conventionnelles. La fusion administrative de L2261-32 est une mesure distincte.",
    "Aucune charge nouvelle n'est identifiée : les conditions, voies d'élargissement et garanties d'opposition restent celles de la source.")

entry('L2261-18',
    "Maintien de la faculté d'assimilation à une carence après cinq ans d'inactivité conventionnelle. Ce délai est un seuil d'ouverture d'un remède, non une obligation de produire périodiquement un accord, ni un délai d'attente général pour toute négociation. L'abroger fermerait cette possibilité de couverture pour les branches futures éligibles ; l'existence d'un autre cas de carence à L2261-17 ne suffit pas à rendre identiques leurs conditions.",
    "Les deux situations sont conservées : absence d'avenant ou annexe à une convention existante, ou absence d'accord à défaut de convention, chacune depuis au moins cinq ans. L2261-17 demeure en vigueur et garde ses conditions d'analogie et d'opposition. Le délai n'est ni celui de l'harmonisation des conventions après regroupement de L2261-33, ni un préavis individuel.",
    "Le texte entier maintient une voie facultative d'accès à une couverture conventionnelle. Aucune formalité annuelle ni obligation autonome à supprimer n'a été relevée dans la source.",
    "Le seuil de cinq ans n'est pas réduit, car cela élargirait le pouvoir d'imposer des normes à d'autres branches. Aucun allègement nouveau n'est comptabilisé.",
    "Aucune charge nouvelle n'est identifiée : ni attestation périodique, ni registre, ni nouvelle déclaration ne s'ajoutent au dispositif conservé.")

entry('L2261-19',
    "Maintien de la négociation paritaire représentative et de l'opposition patronale majoritaire à l'extension. Le mois de publicité, l'écrit motivé, la notification et le dépôt permettent d'identifier la contestation et son opposabilité avant d'imposer l'accord à des tiers. Aucun doublon concret de ce dépôt n'est établi par la source ; la suppression des transmissions CPPNI décidée ailleurs ne porte pas sur cette opposition. Aucun allègement artificiel n'est revendiqué.",
    "Conserver exactement plus de 50 % des salariés des seules entreprises adhérant aux organisations patronales représentatives, non 50 % des entreprises ni de tous les salariés de la branche. Le renvoi à L2232-9 vise la commission, non le rapport annuel ou le minimum de trois réunions supprimés par sa proposition. L2231-5 et L2231-6 ont été lus : notification et dépôt demeurent des fonctions distinctes. La réserve de l'article 5 de l'ordonnance 2017-1388 pour les accords conclus avant le 1er janvier 2018 reste applicable.",
    "La comparaison à la source entière ne démontre aucune suppression possible sans affaiblir la légitimité de l'extension ou la preuve de l'opposition. Maintien sans reformulation.",
    "Aucun gain propre n'est attribué aux allègements déjà proposés pour L2232-9 ou L2231-6. L'ancien régime d'extension des accords antérieurs à 2018 reste distinct.",
    "Aucune charge nouvelle n'est identifiée : le mois, l'assiette majoritaire, la notification et le dépôt existants sont conservés sans pièce supplémentaire.")

entry('L2261-20',
    "Maintien de la faculté de provoquer une commission mixte et de sa convocation obligatoire lorsque deux organisations représentatives la demandent. Cette obligation pèse sur l'autorité administrative et garantit l'accès au dialogue lorsqu'une seule initiative ne suffit pas. Elle ne fixe aucun minimum annuel de réunions et ne rétablit pas celui retiré de L2232-9. Sa suppression retirerait une garantie procédurale sans retirer de démarche privée imposée.",
    "Conserver la distinction entre demande d'une organisation, initiative de l'autorité et demande de deux organisations. L2261-21 et R2261-10, lu dans le corpus, traitent du litige sur l'importance des délégations. Cette commission mixte n'est pas une autorisation de rompre un contrat, ni une procédure collective de licenciement.",
    "La source complète organise un recours à la négociation paritaire et une obligation administrative de convocation protectrice. Aucun prélèvement ni doublon privé n'y est supprimé.",
    "La réunion est liée à une demande, sans périodicité annuelle générale. Aucun délai d'achèvement de la négociation ou effet économique national n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : les deux voies de convocation restent intégralement inchangées.")

entry('L2261-21',
    "Maintien du cadre réglementaire de convocation en cas de litige sur la taille des délégations. La règle ne crée aucune autorisation de négocier et évite qu'un désaccord de représentation bloque la commission. Le contrôle par décret en Conseil d'Etat assure un cadre commun ; aucun doublon d'état déclaratif ni de justificatif ne ressort de la source.",
    "R2261-10 a été lu : le ministre peut fixer dans les convocations un maximum de représentants par organisation. La présente règle ne délègue pas la suppression de la représentativité ou des droits syndicaux ; L2261-20 demeure son contexte. Aucun renvoi au contrat unique, à une ancienneté ou à un préavis n'y figure.",
    "Maintien de la totalité de la disposition nécessaire au règlement d'un blocage de composition de la commission ; aucune réduction de charge n'est démontrée par un changement de vocabulaire.",
    "Le contenu du décret n'est pas réécrit dans ce lot et aucune baisse de frais de délégation ne peut être inférée de ce seul article.",
    "Aucune charge nouvelle n'est identifiée : le seul renvoi réglementaire existant est conservé sans nouveau contrôle préalable.")

# L2261-22 : l'intégralité des rubriques est conservée ; quatre cessent d'être
# des conditions de l'extension. Les paragraphes ajoutés coordonnent le contrat.
t22 = paragraphs('L2261-22')
assert len(t22) == 28, len(t22)
t22[4] = ("II.-Elle contient en outre des clauses portant sur les thèmes ci-après. "
          "Toutefois, les clauses prévues aux 5°, 6°, 7° et 15° sont facultatives et leur absence ne fait pas obstacle à l'extension :")
t22 += [
    "La seule absence de clauses sur les thèmes des 5°, 6°, 7° et 15° n'appelle aucune justification particulière. Les droits légaux et réglementaires relatifs à ces thèmes demeurent directement applicables. Les stipulations conventionnelles existantes conservent leurs effets selon leurs règles de durée, de révision et de dénonciation. Des garanties et des modalités conventionnelles peuvent être négociées à l'avenir sur chacun de ces thèmes, dans les limites fixées par la loi.",
    "Pour les contrats conclus à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, les clauses relatives au recrutement et à la rupture respectent la durée indéterminée prévue à l'article L. 1221-2. La durée d'une mission, d'une affectation, d'une formation, d'une convention ou d'une aide ne fixe pas le terme du contrat. Aucun nouveau contrat à durée déterminée ni renouvellement d'un tel contrat ne peut être institué par la convention. Les contrats conclus avant cette entrée en vigueur et les droits qui en sont issus conservent leur régime transitoire ; une conversion convenue conserve l'ancienneté et les créances acquises.",
    "Pour ces contrats uniques nouveaux, les clauses du 7° ne peuvent rétablir une durée conventionnelle de préavis individuel différente des quinze jours calendaires applicables à l'employeur comme au salarié. Le délai court à partir du lendemain de la présentation ou de la réception de la notification écrite. Les dispenses favorables de préavis à l'initiative du salarié demeurent applicables. Les motifs de rupture, les droits de la défense, les procédures collectives, les autorisations requises pour les salariés protégés et les protections contre la discrimination ou liées à la santé, à la maternité et à la représentation ainsi que le recours au juge restent à leur champ propre ; le préavis ne se substitue pas à ces procédures ou autorisations.",
    "Pour ces contrats uniques nouveaux, l'indemnité ordinaire légale de rupture mentionnée à l'article L. 1234-9 n'est due que lorsque l'employeur rompt le contrat et que le salarié atteint un an d'ancienneté à la fin effective du contrat. Le préavis, exécuté ou non, entre dans cette ancienneté, sous réserve des règles propres à la fin de l'essai. Avant ce seuil, aucune indemnité ordinaire légale n'est due ; une fois ce seuil atteint, toute l'ancienneté reconnue entre dans le calcul, à raison de 0,20 mois de salaire brut de référence par année, au prorata des mois complets pour une année incomplète et dans la limite de six mois de ce salaire. L'exception de faute grave reste celle de l'article L. 1234-9. La rupture à l'initiative du salarié n'ouvre pas cette indemnité. Les indemnités conventionnelles ou contractuelles plus favorables, les salaires, les congés acquis, les indemnités de préavis, les dommages réparant une illégalité et les indemnités spéciales, notamment d'inaptitude professionnelle, ne sont pas supprimés ni plafonnés par cette règle. Pour les contrats antérieurs, les conditions d'ouverture et les composantes d'indemnité conservées par l'article L. 1234-9 demeurent applicables, sans double compte d'une période d'ancienneté.",
    "Les garanties des 12° b et e et du 14° demeurent ouvertes aux situations futures éligibles dans le contrat unique. Le caractère temporaire de l'activité ou d'une affectation ne met pas fin à l'emploi et ne supprime pas, à lui seul, une aide, une exonération, une dispense ou une garantie applicable à cette situation. Le renvoi du 14° au II de l'article L. 911-7 du code de la sécurité sociale conserve son champ : les prestations minimales de couverture complémentaire. Il ne supprime ni le financement patronal ni les dispenses d'affiliation prévus par les autres subdivisions de cet article.",
    "La dispense de clauses obligatoires prévue au II s'applique aux procédures d'extension engagées ou en cours à compter de l'entrée en vigueur de la présente rédaction, sans nouveau dépôt du seul fait de cette dispense. Elle ne remet pas en cause les arrêtés déjà pris et ne rouvre aucun délai de recours expiré."
]
x22 = body(*t22)
a22 = entry('L2261-22',
    "Réforme de fond : quatre thèmes cessent d'être des clauses obligatoires conditionnant l'extension nationale : congés payés, recrutement, rupture et mise en œuvre de l'intéressement, de la participation et de l'épargne salariale. Leurs règles légales continuent de s'appliquer sans recopie conventionnelle ; aucune justification de l'absence de clauses n'est exigée. Toutes les rubriques restent à leur numéro, les autres clauses obligatoires et garanties sont maintenues. Coordination nécessaire, et non nouvelle réduction comptée : les clauses de recrutement et de rupture respectent le contrat unique, son préavis et son indemnité ; les droits spéciaux et les avantages futurs sont explicitement réservés.",
    "Les I 1° à 3°, II 1° à 16° et a à g du 12° sont reproduits sans omission ; seule l'introduction du II rend quatre rubriques facultatives. Le renvoi à L1234-9 vise l'article entier, avec ses transitions et ses garanties plus favorables. L1234-1, L1221-2 et L1234-9 sont les propositions fournies, non le droit en vigueur. Le point de départ du préavis est repris de la décision travail ; sa coordination avec L1234-3 et l'essai avec L1221-25 est nécessaire hors de ce lot et ces cibles ne sont pas fournies dans reference-targets.json. Le renvoi littéral à L1234-3 n'est pas ajouté. L911-7 II conserve ses trois catégories de dépenses ; son III reste distinct. R2261-1 lu dans le corpus porte sur les 4°, 9° et 10°, tous maintenus. L2261-23 et L2261-27 2° gardent des renvois cohérents aux clauses encore obligatoires. Aucun relèvement implicite à quarante heures des régimes annuels ni suppression d'un minimum spécial n'est opéré.",
    "Par rapport à la source officielle entière, quatre thèmes ne bloquent plus l'extension et ne nécessitent plus de justification d'absence. Les règles légales et les garanties négociées restent applicables. Les coordinations du contrat unique transmettent aussi ses contraintes nouvelles pour les futurs recrutements, notamment la fin du recours au CDD ; elles ne sont pas des réductions supplémentaires et le solde net n'est pas établi.",
    "Le gain concerne la condition d'extension, pas une suppression des congés, indemnités, garanties de santé ou mécanismes d'épargne. Les textes réglementaires du contrat unique et les transitions des articles de rupture restent à coordonner hors du lot. Aucun solde économique ou national de complexité n'est établi.",
    "Aucune pièce, déclaration, autorisation ou justification nouvelle ne remplace les quatre clauses facultatives. Toutefois, par rapport au droit officiel entier, la coordination du contrat unique interdit les nouveaux CDD, impose le préavis individuel écrit de quinze jours des deux côtés et écarte les durées conventionnelles différentes hors dispenses conservées. Ces contraintes proviennent des mesures générales coordonnées, sans être comptées comme des obligations autonomes une seconde fois ; elles peuvent renchérir certaines ruptures auparavant dispensées ou plus courtes. Les règles d'ancienneté et de seuil créent aussi une distinction entre contrats anciens et nouveaux. Le solde net de charge n'est pas établi : classement mixed.",
    proposed=x22, category='mixed',
    removed=["Condition d'extension imposant une clause sur les congés payés, même lorsque les droits légaux suffisent.",
             "Condition d'extension imposant une clause sur le recrutement des salariés et sa justification en cas d'absence.",
             "Condition d'extension imposant une clause sur la rupture du contrat, indépendamment des règles légales applicables.",
             "Condition d'extension imposant des modalités conventionnelles de mise en œuvre de l'intéressement, de la participation et de l'épargne salariale."],
    effects=[effect('obligation_removed', 'extension-clauses-legales-facultatives',
        "Quatre thèmes cessent d'être imposés comme contenu préalable à l'extension d'une convention nationale.",
        "Le II impose des clauses sur chacun des thèmes 5°, 6°, 7° et 15° pour l'extension d'une convention nationale, sous réserve des dérogations légales existantes.",
        "Ces quatre thèmes deviennent facultatifs sans justification d'absence ; les droits légaux et les clauses conventionnelles subsistent.",
        'legal_duty', "Négociateurs et bénéficiaires des conventions de branche nationales soumises à extension ; adaptation territoriale par L2261-23.",
        "Procédures nouvelles et en cours à l'entrée en vigueur ; pas de nouveau dépôt, de remise en cause des arrêtés ou de réouverture d'un recours expiré.",
        "Aucune obligation de remplacement ; les autres thèmes et garanties essentielles restent requis.",
        '5° Les congés payés ;',
        "Toutefois, les clauses prévues aux 5°, 6°, 7° et 15° sont facultatives et leur absence ne fait pas obstacle à l'extension :"),
        effect('coordination', 'contrat-unique-duree-indeterminee',
        "Les thèmes recrutement et salariés temporaires ne peuvent ouvrir de nouveaux contrats à terme.",
        "Le 6° vise les conditions de recrutement et le 12° e vise les salariés temporaires, sans distinction nouvelle de durée de l'emploi.",
        "Les situations temporaires restent couvertes, mais ne terminent pas les nouveaux contrats uniques ; les anciens contrats gardent leur transition.",
        'regime', "Salariés privés recrutés après la réforme et salariés déjà employés concernés par les garanties conventionnelles.",
        "Nouveaux contrats à compter de la réforme ; contrats antérieurs et conversion convenue protégés.",
        "Pas de déclaration nouvelle ; restriction substantielle du recours aux CDD admis par L1221-2 officiel, héritée de la réforme coordonnée et non comptée une seconde fois comme obligation autonome.",
        "6° Les conditions de recrutement des salariés ;",
        "La durée d'une mission, d'une affectation, d'une formation, d'une convention ou d'une aide ne fixe pas le terme du contrat."),
        effect('coordination', 'contrat-unique-preavis-quinze-jours',
        "Le thème conventionnel rupture ne rétablit pas une durée de préavis individuel différente.",
        "Le 7° impose des clauses sur les conditions de rupture, sans durée individuelle fixée par cet article.",
        "Pour les nouveaux contrats, préavis individuel de quinze jours calendaires des deux côtés ; protections et procédures distinctes conservées.",
        'calendar_days', "Employeurs et salariés des nouveaux contrats uniques soumis à des conventions de branche.",
        "Point de départ au lendemain de la présentation ou réception écrite ; anciennes règles des contrats antérieurs et dispenses favorables du salarié conservées.",
        "La notification écrite et les quinze jours sont des contraintes de la réforme générale, pouvant allonger certaines ruptures ou écarter des durées plus favorables ; pas de formalité additionnelle propre à cette coordination et aucune autorisation spéciale supprimée.",
        "7° Les conditions de la rupture du contrat de travail ;",
        "Pour ces contrats uniques nouveaux, les clauses du 7° ne peuvent rétablir une durée conventionnelle de préavis individuel différente des quinze jours calendaires applicables à l'employeur comme au salarié."),
        effect('coordination', 'contrat-unique-indemnite-ordinaire',
        "Le thème rupture respecte le seuil et le calcul de l'indemnité ordinaire, sans absorber les indemnités spéciales.",
        "Le 7° vise les conditions de rupture et ne fixe ni seuil ni montant de l'indemnité.",
        "Employeur seul ; seuil d'un an à la fin effective, préavis compris ; 0,20 mois par année totale, prorata des mois complets et plafond légal de six mois, sous l'exception de faute grave de L1234-9.",
        'other', "Salariés des nouveaux contrats uniques ; composantes antérieures et avantages conventionnels plus favorables réservés.",
        "Les anciens contrats gardent les conditions et parts d'indemnité de L1234-9 ; pas de soustraction de la première année ni de double compte.",
        "Aucune formalité nouvelle ; salaires, congés, préavis, réparations et indemnités spéciales demeurent.",
        "7° Les conditions de la rupture du contrat de travail ;",
        "Avant ce seuil, aucune indemnité ordinaire légale n'est due ; une fois ce seuil atteint, toute l'ancienneté reconnue entre dans le calcul, à raison de 0,20 mois de salaire brut de référence par année, au prorata des mois complets pour une année incomplète et dans la limite de six mois de ce salaire.")])
a22['benefit_review'] = "Les congés payés, garanties de rupture plus favorables, épargne salariale, formation, égalité, droits des personnes handicapées, des femmes enceintes, jeunes, temps partiels, travailleurs à domicile, salariés à l'étranger, temporaires, inventeurs et salariés déplacés outre-mer restent à leur champ. Seule leur présence obligatoire dans la convention est retirée pour quatre thèmes : les droits légaux s'appliquent directement et les clauses favorables peuvent être maintenues et négociées pour de futures situations. Le II de L911-7 conserve la couverture minimale ; son III, le financement patronal et les dispenses, notamment pour les périodes temporaires éligibles au sein du contrat unique, ne sont pas fermés. Aucun impôt ou avantage fiscal n'est supprimé par ce texte."

entry('L2261-23',
    "Maintien du renvoi adaptable aux conventions territoriales lorsqu'il n'existe pas de convention nationale. L'exception d'adaptation aux conditions du secteur est une souplesse favorable à conserver pour les futures conventions. Le renvoi à L2261-22 demeure exact : il applique ses conditions telles qu'allégées, sans imposer à nouveau les quatre thèmes devenus facultatifs. Aucun nouveau corps n'est nécessaire.",
    "Le champ est subsidiaire : défaut de convention au niveau national, conventions de branche conclues à d'autres niveaux territoriaux. Il n'autorise pas un CDD territorial et n'écarte pas le contrat unique pour les nouveaux recrutements. Les allègements de L2261-22 s'appliquent par le renvoi existant ; ils ne sont pas une seconde suppression. Les droits légaux et adaptations favorables subsistent.",
    "Le maintien intégral conserve l'adaptation territoriale utile et transmet les conditions d'extension de L2261-22 sans incohérence. Aucune réduction autonome n'est comptée pour ce renvoi.",
    "Aucun nouvel effet fiscal ou gain distinct de celui de L2261-22 n'est démontré. Les adaptations restent bornées par les conditions du secteur et le droit applicable.",
    "Aucune charge nouvelle n'est identifiée : aucun dossier, preuve d'absence de convention nationale ou délai supplémentaire n'est ajouté au texte officiel.")

x231 = body(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.",
    "L'extension d'une convention de branche ou d'un accord professionnel n'est plus subordonnée à la présence de stipulations spécifiques pour les entreprises de moins de cinquante salariés ni à une justification de leur absence. Cette suppression s'applique également aux demandes d'extension en cours, sans nouveau dépôt de la convention ou de l'accord.",
    "Les stipulations spécifiques déjà applicables et les droits qui en résultent sont conservés selon les règles qui leur sont propres. La faculté de négocier de telles stipulations et d'appliquer un accord type dans les conditions de l'article L. 2232-10-1 demeure ouverte, y compris pour les situations futures éligibles.",
    "Les arrêtés d'extension déjà pris ne sont pas remis en cause. Aucun délai de recours expiré n'est rouvert par cette abrogation.")
a231 = entry('L2261-23-1',
    "Abrogation de la condition autonome d'extension imposant des stipulations pour les entreprises de moins de cinquante salariés, sauf justification. La possibilité d'un accord type, son application et les clauses déjà négociées restent sur leur fondement autonome L2232-10-1 ; l'allègement ne les réserve pas au stock ancien. La condition et la justification disparaissent sans déclaration de remplacement et sans modifier les garanties substantielles des salariés.",
    "L2232-10-1 a été lu intégralement dans le corpus public : faculté de clauses spécifiques sur l'ensemble des négociations, accord type, choix unilatéral dans ses options et information du CSE et des salariés. Son maintien permet les futures situations éligibles. Aucune condition de validité d'un accord ni majorité de L2232-6 n'est retirée. Les procédures en cours bénéficient de l'abrogation ; les arrêtés acquis et délais expirés sont conservés. Le renvoi à L2232-10-1 existe déjà dans la source, il n'est pas une nouvelle cible de reference-targets.json.",
    "La source entière n'impose que cette condition et sa justification alternative. Leur suppression retire effectivement une charge préalable à l'extension, tout en conservant la faculté autonome de clauses adaptées aux petites entreprises.",
    "L'effet porte sur l'accès à l'extension, sans démontrer de réduction des coûts de rédaction de toutes les conventions ni autoriser le retrait de garanties existantes. Aucun solde national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration, ni attestation de non-besoin, ni nouvelle pièce ne remplace les stipulations et la justification supprimées. Les règles propres à l'accord type restent existantes.",
    proposed=x231, category='material_reduction',
    repeal="Suppression pour les extensions futures et en cours de la condition de clauses spécifiques aux entreprises de moins de cinquante salariés et de la justification alternative de leur absence.",
    effects=[effect('obligation_removed', 'extension-fin-condition-clauses-petites-entreprises',
        "Suppression de la condition de clauses spécifiques ou de justification pour étendre l'accord.",
        "Convention de branche ou accord professionnel : stipulations spécifiques pour les entreprises de moins de cinquante salariés obligatoires sauf justification.",
        "Ni stipulation spécifique obligatoire, ni justification de son absence pour l'extension ; facultés L2232-10-1 maintenues.",
        'legal_duty', "Négociateurs de branche et entreprises concernées par l'extension, notamment entreprises de moins de cinquante salariés.",
        "Demandes nouvelles ou en cours à l'entrée en vigueur ; droits et arrêtés antérieurs protégés, pas de recours expiré rouvert.",
        "Aucune condition ou déclaration de remplacement ; les clauses favorables restent disponibles pour les situations futures.",
        "Pour pouvoir être étendus, la convention de branche ou l'accord professionnel doivent, sauf justifications, comporter, pour les entreprises de moins de cinquante salariés, les stipulations spécifiques mentionnées à l'article L. 2232-10-1",
        "L'extension d'une convention de branche ou d'un accord professionnel n'est plus subordonnée à la présence de stipulations spécifiques pour les entreprises de moins de cinquante salariés ni à une justification de leur absence.")])
a231['benefit_review'] = "Les clauses adaptées aux entreprises de moins de cinquante salariés et l'option d'accord type peuvent être des assouplissements favorables : elles restent négociables et applicables sous L2232-10-1 aux entreprises futures éligibles. Les clauses existantes conservent leurs effets. Seule l'obligation d'en insérer ou de justifier leur absence comme condition d'extension est abrogée ; aucune exonération fiscale ou dispense sociale n'est supprimée."

t24 = paragraphs('L2261-24')
t24[0] = t24[0].replace(", après avis motivé de la Commission nationale de la négociation collective, de l'emploi et de la formation professionnelle", '')
t24.append("La présente rédaction s'applique aux procédures d'extension engagées ou en cours à compter de son entrée en vigueur. L'avis préalable au seul engagement de la procédure n'est plus requis ; l'avis exigé avant l'arrêté d'extension par l'article L. 2261-15 demeure applicable. Les actes régulièrement accomplis sont conservés et aucun nouveau dépôt n'est exigé du seul fait de cette suppression.")
x24 = body(*t24)
entry('L2261-24',
    "Réforme de fond : suppression de l'avis motivé exigé avant le simple engagement de la procédure, qui doublonne la consultation préalable à l'arrêté d'extension maintenue par L2261-15. L'initiative ministérielle, la demande d'une organisation représentative et l'engagement sans délai restent intacts. Aucun avis ou dépôt de remplacement n'est créé ; la procédure se poursuit aussi pour les dossiers en cours.",
    "La seule suppression concerne le membre de phrase final du premier alinéa ; le second alinéa sur l'engagement sans délai est reproduit. Les contrôles de L2261-19, l'avis final de L2261-15, les droits des tiers et les oppositions ne sont pas abrégés. R2261-4-7 lu dans le corpus conserve une règle de rejet implicite après six mois ; aucune modification de cette durée n'est prétendue ici. La note d'entrée en vigueur de 2021 ne fixe pas la date de la réforme.",
    "La source entière contient une consultation avant l'engagement, en plus de celle avant l'arrêté. Seule la première est retirée : un circuit administratif redondant disparaît sans retrait du contrôle final.",
    "Aucun nombre de jours gagnés ni coût national n'est établi ; le droit d'opposition et l'avis sur le fond peuvent toujours prendre du temps. L'obligation d'engager sans délai existait déjà.",
    "Aucune charge nouvelle n'est identifiée : aucun rapport ou saisine de remplacement, aucun nouveau dépôt pour les dossiers en cours et aucune modification des conditions substantielles d'extension.",
    proposed=x24, category='material_reduction',
    removed=["Avis motivé de la commission nationale préalablement au seul engagement de la procédure d'extension, distinct de l'avis avant arrêté."],
    effects=[effect('obligation_removed', 'extension-avis-prealable-engagement-suppression',
        "Retrait de l'avis nécessaire pour commencer la procédure ; l'avis avant la décision d'extension reste requis.",
        "Avis motivé de la commission nationale requis pour engager la procédure, en plus de la consultation avant l'arrêté de L2261-15.",
        "Engagement sans cet avis préalable ; consultation motivée avant l'arrêté maintenue.",
        'legal_duty', "Ministère, commission nationale et organisations demandant l'extension d'une convention ou d'un accord.",
        "Procédures nouvelles et en cours ; actes déjà accomplis maintenus sans nouveau dépôt.",
        "Aucun contrôle ou rapport de remplacement ; aucune réduction annoncée du délai d'opposition.",
        "La procédure d'extension d'une convention de branche ou d'un accord professionnel ou interprofessionnel est engagée à la demande d'une des organisations d'employeurs ou de salariés représentatives mentionnées à l'article L. 2261-19 ou à l'initiative du ministre chargé du travail, après avis motivé de la Commission nationale de la négociation collective, de l'emploi et de la formation professionnelle.",
        "L'avis préalable au seul engagement de la procédure n'est plus requis ; l'avis exigé avant l'arrêté d'extension par l'article L. 2261-15 demeure applicable.")])

entry('L2261-25',
    "Maintien du filtre de légalité et d'intérêt général avant d'imposer des clauses à des non-signataires. Les exclusions divisibles et les réserves d'application permettent d'étendre le reste de l'accord sans exiger sa renégociation entière. La faculté d'extension de clauses à compléter par accord d'entreprise conserve sa souplesse sous les limites législatives. Supprimer ces instruments fermerait des dérogations favorables ou permettrait une extension contraire aux protections essentielles.",
    "Conserver distinctement clauses illégales, motifs d'intérêt général dont concurrence et emploi, clauses divisibles inadaptées, clauses incomplètes et clauses nécessitant un complément d'entreprise. La formule ancienne du nom de la commission dans la source vise le même organe ; aucune création d'organe n'est nécessaire. L2261-19 source_notes réserve l'ancien droit aux accords conclus avant le 1er janvier 2018. Les règles nouvelles du contrat unique s'imposent à l'extension dans leur seul champ temporel.",
    "La lecture entière montre un contrôle et plusieurs voies de souplesse permettant de ne pas bloquer l'accord complet. Aucun doublon supprimable n'est démontré au-delà des circuits spécifiques retirés dans les articles voisins.",
    "Le maintien ne supprime pas la faculté de refus pour un intérêt général établi. Il ne crée pas une extension automatique ni un droit à déroger au contrat unique.",
    "Aucune charge nouvelle n'est identifiée : les avis, réserves et compléments d'entreprise restent à leurs conditions existantes, sans agrément ou justificatif ajouté.")

entry('L2261-26',
    "Maintien de l'examen accéléré des seuls avenants salariaux, du plafond favorable de deux mois lorsque le SMIC a augmenté au moins deux fois dans les douze mois et de la voie agricole régionale ou départementale. Le texte est déjà une dérogation de délai favorable pour les avenants futurs éligibles ; aucun raccourcissement supplémentaire fondé ni doublon d'obligation n'est identifié. Les droits des tiers restent expressément préservés.",
    "Les références SMIC sont conservées : L3231-5, L3231-6 à L3231-9 et L3231-10. Les douze mois se mesurent avant la conclusion de l'avenant. R2261-5 et R2261-6 ont été lus dans le corpus : quinze jours de demande d'examen et, dans le cas spécial, décision ministérielle sous deux mois avec rejet implicite. Ces quinze jours ne sont pas le préavis individuel. Aucun relèvement du seuil des heures supplémentaires ne résulte de cet article.",
    "Le texte officiel entier maintient un calendrier déjà accéléré et une voie spéciale agricole. Ce maintien préserve un allègement existant sans le compter comme une nouvelle réduction.",
    "Le plafond de deux mois n'est pas étendu aux autres accords et aucun temps réel gagné n'est chiffré. Les dispositions réglementaires ne sont pas réputées réécrites.",
    "Aucune charge nouvelle n'est identifiée : la consultation, les garanties des tiers, les seuils et délais spéciaux sont conservés sans nouveau justificatif.")

t27 = paragraphs('L2261-27')
t27[0] = "Après avis motivé de la Commission nationale de la négociation collective, de l'emploi et de la formation professionnelle, le ministre chargé du travail peut étendre par arrêté une convention ou un accord ou leurs avenants ou annexes dans les cas suivants :"
t27[4] = "En l'absence d'opposition écrite et motivée soit de deux organisations d'employeurs, soit de deux organisations de salariés représentées à cette commission, l'extension prévue au présent article requiert un avis favorable de la commission."
t27[5] = "En cas d'opposition dans les conditions prévues à l'alinéa précédent, les oppositions sont examinées avec la demande d'extension au cours de la même consultation. Elles n'imposent ni une seconde consultation ni un rapport distinct sur la portée des dispositions et les conséquences de l'extension. Le ministre peut décider l'extension au vu de l'avis motivé recueilli ; cette décision est motivée. Le présent article ne déroge ni aux conditions de validité de la convention ou de l'accord, ni à l'opposition majoritaire à l'extension prévue à l'article L. 2261-19."
t27.append("La présente rédaction s'applique aux décisions d'extension prises à compter de son entrée en vigueur, y compris dans une procédure en cours. Les oppositions et avis déjà recueillis sont conservés ; aucune nouvelle consultation n'est exigée pour le seul motif qu'une opposition de deux organisations d'employeurs ou de deux organisations de salariés a été exprimée. Si l'avis requis n'a pas été recueilli, la consultation nécessaire demeure obligatoire. Les arrêtés antérieurs et les délais de recours restent régis par les règles qui leur sont applicables.")
x27 = body(*t27)
entry('L2261-27',
    "Réforme de fond : un seul examen par la commission, avec les oppositions, remplace la voie de seconde consultation accompagnée d'un rapport distinct lorsque deux organisations d'un même collège s'opposent. Les trois situations dérogatoires d'extension et la motivation du ministre en cas d'opposition restent. L'avis favorable demeure exigé en l'absence de cette opposition ; dans la voie avec opposition, aucun nouveau veto de la commission n'est créé, la source permettant une décision au vu de son nouvel avis sans exiger qu'il soit favorable. L'opposition patronale majoritaire de L2261-19 et les majorités de validité restent impératives.",
    "1° absence de signature de toutes les organisations, 2° clauses obligatoires manquantes et 3° couverture partielle des catégories sont conservés à leur numéro et sans modification. Un avis motivé effectif demeure requis ; la suppression de la seconde saisine ne vaut pas avis favorable automatique. La voie avec opposition conserve la décision ministérielle motivée au vu de l'avis, sans lui ajouter une condition de nouvel avis favorable que la source ne prévoyait pas. Les clauses devenues facultatives dans L2261-22 ne sont plus des clauses manquantes obligatoires au sens du 2°. La note d'entrée en vigueur de 2021 reste historique.",
    "Par rapport à la source entière, la procédure spéciale en cas d'opposition de deux organisations ne nécessite plus une nouvelle saisine ni un rapport séparé. La décision repose toujours sur un avis motivé et les oppositions reçues ; l'avis doit être favorable dans la voie sans opposition de deux organisations. Les droits de veto majoritaire et de recours ne sont pas retirés.",
    "La seconde consultation était une faculté permettant de dépasser l'opposition : elle devient inutile comme circuit spécial. Aucun délai précis ou gain de coût n'est démontré. Une consultation demeure nécessaire si aucun avis n'a été recueilli ; la condition d'avis favorable de la voie sans opposition est conservée.",
    "Aucune charge nouvelle n'est identifiée : les oppositions existantes sont examinées dans la consultation utile, sans nouvelle pièce ni renonciation. La motivation déjà imposée en cas d'opposition reste ; aucun avis favorable fictif n'est ajouté.",
    proposed=x27, category='material_reduction',
    removed=["Circuit spécial de nouvelle consultation de la commission après opposition de deux organisations du même collège, avec rapport distinct sur la portée et les conséquences de l'extension."],
    effects=[effect('obligation_merged', 'extension-oppositions-examen-consultation-unique',
        "Intégration des oppositions dans l'examen utile ; retrait du circuit de nouvelle saisine et du rapport distinct permettant de passer outre.",
        "En cas d'opposition de deux organisations patronales ou de deux organisations de salariés à la commission, voie de nouvelle consultation sur un rapport avant extension au vu du nouvel avis.",
        "Les oppositions sont examinées dans la même consultation ; ni second examen exigé du seul fait de l'opposition, ni rapport distinct ; avis motivé effectif et décision ministérielle motivée, sans nouveau veto de la commission.",
        'legal_duty', "Ministre et commission instruisant les extensions dérogatoires des 1° à 3° ; organisations représentées à la commission.",
        "Décisions nouvelles, y compris procédures en cours ; avis et oppositions déjà acquis conservés, arrêtés antérieurs et recours protégés.",
        "Aucun dépôt ni protocole nouveau ; motivation ministérielle existante et conditions de validité inchangées.",
        "En cas d'opposition dans les conditions prévues au premier alinéa, le ministre chargé du travail peut consulter à nouveau la commission sur la base d'un rapport précisant la portée des dispositions en cause ainsi que les conséquences d'une éventuelle extension.",
        "Elles n'imposent ni une seconde consultation ni un rapport distinct sur la portée des dispositions et les conséquences de l'extension.")])

x271 = body(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.",
    "Aucune saisine du groupe d'experts ni aucun rapport de ce groupe ne peut être exigé sur ce fondement pour une procédure d'extension nouvelle ou en cours. Les saisines déjà intervenues n'imposent pas la remise d'un rapport après cette entrée en vigueur et ne retardent pas la poursuite de la procédure d'extension.",
    "Les avis et rapports déjà remis restent utilisables dans l'instruction et le contrôle de la légalité des décisions. Les droits à rémunération ou à indemnisation légalement acquis au titre des mandats ou des prestations accomplis avant cette entrée en vigueur sont conservés. Les obligations de secret, de confidentialité et de protection des données applicables aux informations déjà recueillies demeurent.",
    "Cette abrogation ne supprime ni la consultation de la commission nationale requise pour l'extension, ni les observations et oppositions légalement ouvertes aux organisations intéressées, ni le contrôle du juge. Aucun rapport, dépôt ou visa particulier ne remplace la saisine supprimée.")
entry('L2261-27-1',
    "Abrogation du circuit spécial de saisine d'un groupe d'experts distinct et du rapport associé, doublonnant l'instruction économique et sociale préalable à l'extension et l'avis de la commission nationale. Les organisations gardent leurs observations, oppositions et recours ; les documents d'expertise déjà remis demeurent utilisables. Il ne s'agit pas de supprimer l'examen de la concurrence ou de l'emploi de L2261-25, mais d'enlever une étape institutionnelle sans rapport de remplacement.",
    "D2261-4-1 à D2261-4-6 ont été lus intégralement : cinq membres, mandats de quatre ans, demande sous un mois, rapport sous deux mois, indépendance, secret et conflits d'intérêts. Ils nécessitent une abrogation ou coordination expresse hors des articles assignés, avec préservation des droits acquis aux mandats, du secret et des prestations déjà accomplies. La présente norme législative retire néanmoins toute exigence future de saisine et de rapport, y compris dans les dossiers en cours. Les délais réglementaires ne sont pas comptés comme du temps automatiquement gagné. La note sur les accords antérieurs à 2018 vise L2261-19 et L2261-25, non un nouveau report de cette abrogation.",
    "Suppression effective, par rapport à la source entière, de la saisine institutionnelle spéciale et de la production d'un rapport d'experts sur ce seul fondement. Le contrôle final, les oppositions et les analyses déjà disponibles subsistent.",
    "Le coût public du groupe et le délai réel de chaque extension ne sont pas chiffrés. Les textes réglementaires cités restent à coordonner ; cette abrogation ne vaut pas achèvement de leur réécriture ni retrait des contrôles autonomes.",
    "Aucune charge nouvelle n'est identifiée : aucun expert, visa, déclaration ou rapport alternatif imposé. La conservation des droits acquis et du secret ne crée pas un reporting de remplacement.",
    proposed=x271, category='material_reduction',
    repeal="Suppression de la saisine spéciale du groupe d'experts sur les effets économiques et sociaux d'une extension et de son rapport, pour toutes procédures nouvelles ou en cours à l'entrée en vigueur.",
    effects=[effect('obligation_removed', 'extension-groupe-experts-saisine-rapport-suppression',
        "Retrait de la saisine spéciale d'experts et du rapport qui en résulte.",
        "Le ministre saisit le groupe d'experts de sa propre initiative ou à la demande écrite et motivée d'une organisation représentative ; expertise spéciale des effets de l'extension.",
        "Aucune saisine ou rapport de ce groupe requis pour une extension nouvelle ou en cours ; analyses et contrôles autonomes conservés.",
        'legal_duty', "Ministère, groupe d'experts et organisations représentatives intéressées à l'extension.",
        "À l'entrée en vigueur, y compris saisines en cours ; avis remis et droits acquis préservés, secret maintenu.",
        "Aucun dépôt, avis ou rapport spécifique de remplacement ; avis de la commission nationale toujours exigé dans son champ.",
        "Le ministre chargé du travail, de sa propre initiative ou à la demande écrite et motivée d'une organisation d'employeurs ou d'une organisation de salariés représentative dans le champ d'application d'une convention, d'un accord ou de leurs avenants, saisit un groupe d'experts chargé d'apprécier les effets économiques et sociaux susceptibles de résulter de leur extension.",
        "Aucune saisine du groupe d'experts ni aucun rapport de ce groupe ne peut être exigé sur ce fondement pour une procédure d'extension nouvelle ou en cours.")])

entry('L2261-28',
    "Maintien intégral de la caducité automatique de l'arrêté quand l'accord cesse de produire effet. Cette borne empêche la survie d'une obligation conventionnelle sans support et dispense d'une demande d'abrogation pour ce seul événement. La remplacer par une démarche imposée créerait une charge ; l'abroger pourrait prolonger les effets d'un accord éteint. Aucun nouveau corps utile n'est nécessaire.",
    "La cessation des effets de l'accord, et non sa seule dénonciation ou l'annonce de son remplacement, est le point de départ. Les effets de survie légalement applicables ne sont pas supprimés par cette règle. L2261-29 coordonne l'élargissement et L2261-30 un autre cas de caducité. Aucun rapport ou accusé de réception n'est exigé par la source.",
    "La source entière est déjà une limitation automatique des contraintes de l'extension. Elle est maintenue sans lui attribuer une nouvelle suppression d'obligation.",
    "Aucune modification des règles de durée, de dénonciation ou de survie conventionnelle n'est proposée, et aucune économie chiffrée n'est établie.",
    "Aucune charge nouvelle n'est identifiée : la caducité demeure automatique et aucune déclaration de cessation n'est ajoutée.")

entry('L2261-29',
    "Maintien du lien de caducité entre élargissement et extinction de l'extension de référence. Il évite qu'un secteur demeure soumis à un texte dont le fondement d'extension a disparu et n'impose aucune nouvelle démarche. La suppression de cette borne serait plus contraignante ; sa reformulation n'apporterait aucun allègement réel.",
    "Le jour retenu est celui où l'arrêté d'extension cesse de produire effet ; ne pas substituer la simple date d'un avenant ou le début d'une fusion de branches. L2261-17 et L2261-18 restent opérants et L2261-30 garde ses deux autres règles de sortie. La disposition ne supprime ni les créances déjà nées ni les droits propres résultant d'un autre fondement.",
    "Maintien intégral d'une extinction automatique nécessaire des contraintes sans base d'extension. Aucune mesure nouvelle de baisse de taxe ou de formalité n'est démontrée.",
    "Les autres causes de cessation de l'élargissement et les droits nés avant sa caducité restent à leur régime ; aucun gain indépendant n'est compté.",
    "Aucune charge nouvelle n'est identifiée : ni demande de caducité ni preuve ou registre supplémentaire ne remplace l'effet automatique conservé.")

entry('L2261-30',
    "Maintien des deux sorties de l'élargissement : caducité pour les employeurs liés par un accord ultérieur du secteur, puis abrogation dans le champ où cet accord est étendu. Ces mécanismes évitent une superposition de normes et conservent la liberté de négocier un accord propre. Aucune obligation privée redondante ne peut être retirée de ce texte déjà dérogatoire.",
    "Le premier alinéa ne concerne que les employeurs liés par la convention ou l'accord ultérieur ; le second dépend d'un arrêté d'extension et de son champ exact. Les deux effets ne se confondent pas et aucun silence ne vaut extension. La suppression des fusions imposées de L2261-32 ne ferme pas ces voies autonomes d'accord et d'extension.",
    "La lecture complète montre deux mécanismes existants de substitution sans cumul des effets d'élargissement. Ils sont maintenus sans changement de fond et sans nouveau gain attribué.",
    "Aucun élargissement automatique du champ de l'accord nouveau n'est proposé. Les obligations et garanties des autres textes ne sont pas réputées éteintes.",
    "Aucune charge nouvelle n'est identifiée : les caducité et abrogation restent liées aux actes déjà prévus, sans formalité additionnelle des employeurs.")

entry('L2261-31',
    "Maintien intégral des deux exclusions de la procédure commune : accords d'assurance chômage et accords de gestion de droits issus de la participation. Ces régimes disposent de leur logique propre ; l'abrogation de l'exclusion les assujettirait potentiellement à une procédure additionnelle. Aucun prélèvement, déclaration ni autorisation n'est imposé par l'article et la distinction des régimes favorables doit rester ouverte aux accords futurs.",
    "Le 1° vise les seuls accords de L5422-20 ; le 2° ne vise pas toute convention de participation mais les accords conclus dans son cadre qui fixent la nature et la gestion des droits reconnus. Ne pas transformer l'exclusion procédurale en suppression de l'assurance chômage, de droits d'épargne ou des règles autonomes de financement. Aucun renvoi nouveau n'est ajouté.",
    "Le texte complet porte des dispenses de procédure nécessaires à la séparation des régimes. Leur maintien n'est pas une nouvelle simplification et ne supprime aucun droit social.",
    "Les règles propres de ces régimes ne sont pas auditées intégralement dans ce lot ; leur exclusion ne prouve aucune baisse de cotisation ou de fiscalité.",
    "Aucune charge nouvelle n'est identifiée : les dispenses restent entières pour les accords actuels et futurs, sans justification ou agrément ajouté.")

t32 = paragraphs('L2261-32')
assert len(t32) == 18, len(t32)
t32new = [
    "I.-Abrogé.",
    *t32[11:15],
    "III.-Abrogé.",
    "IV.-Abrogé.",
    t32[17],
    "L'abrogation des I, III et IV s'applique à compter de l'entrée en vigueur de la loi qui la prévoit. Aucune nouvelle fusion de champs conventionnels ne peut être engagée ou prononcée sur le fondement du I, y compris dans une procédure engagée avant cette entrée en vigueur et non achevée à cette date. Aucun refus d'extension ni aucune décision de ne pas arrêter les listes d'organisations représentatives ne peut être pris sur les seuls fondements des III et IV.",
    "Les décisions antérieures fondées sur les seuls III ou IV ne peuvent être opposées à l'examen des demandes et à l'établissement des listes effectués à compter de cette entrée en vigueur. Cette règle ne prononce par elle-même aucune extension et ne dispense d'aucune condition légale de représentativité ou de validité des accords.",
    "Les fusions déjà prononcées avant cette entrée en vigueur conservent leurs effets, ainsi que les conventions et accords légalement conclus, les droits et créances déjà constitués et les recours ouverts. Les articles L. 2261-33 et L. 2261-34 leur demeurent applicables dans leur champ transitoire. Le regroupement volontaire par accord collectif reste possible selon ses règles de validité, sans recours aux pouvoirs supprimés. Le II demeure applicable aux secteurs non couverts, y compris pour les opérations futures éligibles. L'élargissement prévu au II ne constitue pas une fusion de branches et ne peut être utilisé pour rétablir les pouvoirs supprimés par les I, III et IV."
]
x32 = body(*t32new)
entry('L2261-32',
    "Réforme de fond : suppression des pouvoirs de fusion administrative forcée, de refus d'extension motivé par la seule restructuration et de gel des listes de représentativité attaché aux mêmes critères. Les six critères du I ne servent donc plus de déclencheurs à ces contraintes. Le II, voie autonome de couverture d'un secteur non couvert avec publicité, observations et consultation, est intégralement conservé pour l'avenir. Les fusions déjà prononcées et les accords volontaires ne sont pas défaits.",
    "Les subdivisions I, II, III, IV et V sont maintenues ; le II et ses quatre alinéas restent complets. Le V conserve le décret en Conseil d'Etat. Le I supprimé comprenait notamment moins de 5 000 salariés, moins de 5 % d'entreprises adhérentes, faiblesse conventionnelle, champ régional/local, défaut de CPPNI et capacité formation/apprentissage ; aucune de ces données n'est demandée dans un registre de remplacement. R2261-15, lu intégralement dans le corpus, doit être abrogé pour l'avenir, sans maintenir un nouveau déclencheur. D2261-14 et D2261-15 ont également été lus en entier : retirer leurs renvois respectifs aux huitième et dixième alinéas du I abrogé, mais conserver les renvois au deuxième et au troisième alinéas du II. Les quinze jours d'observations, les quinze jours pour une proposition alternative et le mois minimal avant seconde consultation demeurent dans le seul champ du II maintenu. Ces coordinations réglementaires sont identifiées, non rédigées dans ce lot ; les autres règlements de listes restent à vérifier. L2261-33 et L2261-34 sont effectivement coordonnés ci-après. Le II ne peut servir à recréer une fusion : son objet demeure seulement la couverture d'un secteur non couvert.",
    "La source entière autorise une restructuration imposée et deux leviers administratifs associés ; ces pouvoirs disparaissent pour l'avenir et pour les procédures non achevées. La couverture favorable des secteurs non couverts demeure sous le II et les situations antérieures restent protégées.",
    "Le coût net des regroupements évités n'est pas chiffré. Les décisions de fusion déjà prises ne sont pas annulées, les critères de représentativité demeurent et aucune extension automatique n'est accordée. Les règlements hors lot restent à coordonner.",
    "Aucune charge nouvelle n'est identifiée : pas d'accord, déclaration, registre, autorisation ou indicateur substitué à la fusion forcée. Les consultations et observations du II sont préexistantes ; les regroupements volontaires gardent leurs règles de validité.",
    proposed=x32, category='material_reduction',
    removed=["Pouvoir de fusion imposée du champ des conventions collectives sur les six critères du I, avec publicité et consultations propres à cette procédure.",
             "Pouvoir du III de refuser l'extension d'une convention, d'un avenant ou d'une annexe pour le seul intérêt général de restructuration des branches visées au I.",
             "Pouvoir du IV de ne pas arrêter les listes d'organisations représentatives d'employeurs et de salariés pour les seules finalités de restructuration des branches visées au I."],
    effects=[effect('obligation_removed', 'branches-fin-restructuration-administrative-forcee',
        "Suppression de la fusion administrative imposée et des leviers propres de refus d'extension ou de gel de représentativité servant cette restructuration.",
        "Fusion possible par le ministre pour branches de moins de 5 000 salariés, faiblesse conventionnelle, champ local/régional, adhésion patronale inférieure à 5 %, défaut de CPPNI ou capacité insuffisante de formation ; pouvoirs des III et IV sur ces branches.",
        "Plus de nouvelle fusion imposée ni de refus d'extension ou gel des listes sur ces seuls fondements ; regroupements volontaires et couverture des secteurs non couverts par le II maintenus.",
        'legal_duty', "Branches professionnelles, organisations patronales et syndicales, salariés et employeurs relevant de leurs conventions.",
        "Dès l'entrée en vigueur, y compris procédures non achevées ; fusions déjà prononcées, accords et créances protégés ; anciennes décisions III/IV inopposables aux examens futurs sur leurs seuls fondements.",
        "Aucune procédure de regroupement obligatoire de remplacement ; exigences légales ordinaires et II inchangés.",
        "I.-Le ministre chargé du travail peut, eu égard à l'intérêt général attaché à la restructuration des branches professionnelles, engager une procédure de fusion du champ d'application des conventions collectives d'une branche avec celui d'une branche de rattachement présentant des conditions sociales et économiques analogues :",
        "Aucune nouvelle fusion de champs conventionnels ne peut être engagée ou prononcée sur le fondement du I, y compris dans une procédure engagée avant cette entrée en vigueur et non achevée à cette date.")])

t33 = paragraphs('L2261-33')[0].split('\n')
# Les alinéas d'origine sont séparés par deux br dans un même p.
orig33 = [unescape(re.sub('<[^>]+>', '', t)).strip() for t in re.split(r'<br\s*/?>\s*<br\s*/?>', re.search(r'<p[^>]*>(.*?)</p>', by_number['L2261-33']['source_xml'], re.S).group(1))]
assert len(orig33) == 3
orig33[0] = ("Pour les fusions prononcées en application du I de l'article L. 2261-32 avant l'entrée en vigueur de la loi supprimant ce pouvoir de fusion et pour les accords de regroupement conclus avant cette entrée en vigueur, les stipulations conventionnelles" + orig33[0].split(', les stipulations conventionnelles', 1)[1])
orig33[2] += " Toutefois, cette application ne met pas fin de plein droit aux stipulations de la convention de la branche rattachée qui régissent des situations spécifiques à cette branche."
x33 = body(*orig33,
    "Pour les accords de regroupement conclus à compter de cette entrée en vigueur, l'adoption de stipulations communes est facultative et n'est soumise à aucun délai légal d'harmonisation. Plusieurs conventions collectives peuvent continuer à s'appliquer dans leurs champs respectifs. À défaut de stipulations communes valablement conclues, les stipulations antérieures demeurent applicables dans leur champ selon leurs règles de durée, de révision, de dénonciation et de cessation des effets. Aucune convention de rattachement ne s'y substitue automatiquement du seul fait du regroupement ou de l'écoulement d'un délai de cinq ans.",
    "Pour ces regroupements nouveaux, les différences temporaires de traitement entre salariés résultant du regroupement ne peuvent être utilement invoquées pendant cinq ans à compter de sa date d'effet. Cette dérogation n'écarte ni les interdictions de discrimination ni les autres protections d'ordre public. À l'issue de ces cinq ans, les différences de traitement restent soumises au droit commun. Les stipulations régissant des situations spécifiques à une branche et les garanties et dérogations favorables demeurent applicables selon leurs règles propres, y compris aux situations futures éligibles. Les accords de regroupement ne peuvent déroger aux règles légales du contrat de travail unique dans leur champ temporel.")
a33 = entry('L2261-33',
    "Réforme de fond pour les regroupements volontaires futurs : suppression de l'obligation de remplacer les stipulations relatives à des situations équivalentes par un corpus commun sous cinq ans et de la substitution automatique par la convention de rattachement à défaut d'accord. La coexistence des conventions reste possible. La dérogation favorable de cinq ans pour les différences temporaires résultant du regroupement demeure ouverte aux futurs regroupements, sans être rendue indéfinie. Les trois alinéas anciens restent dans le champ transitoire des fusions déjà prononcées et regroupements déjà convenus. La réserve constitutionnelle sur les situations spécifiques est rendue explicite, afin de ne pas faire disparaître des droits autonomes.",
    "L2261-32 I est abrogé pour les fusions nouvelles ; son renvoi historique est conservé seulement pour les décisions déjà prononcées. Le délai ancien de cinq ans part toujours de la date d'effet de la fusion ou du regroupement antérieur ; il n'est ni relancé ni raccourci. Pour les regroupements futurs, la durée de la dérogation relative aux différences temporaires est autonomisée à cinq ans depuis leur date d'effet, puisque l'harmonisation n'a plus d'échéance obligatoire. La note source renvoie à la décision 2019-816 QPC du 29 novembre 2019 : la substitution au troisième alinéa ne peut effacer les situations spécifiques. Le régime de durée, révision et dénonciation des conventions subsiste : maintenir leur champ ne les rend pas perpétuelles. Aucun délai supplémentaire de dérogation ni restriction de ses bénéficiaires futurs n'est créé.",
    "La comparaison à l'article officiel entier montre, pour les seuls regroupements futurs, la disparition de l'échéance obligatoire de cinq ans et du remplacement automatique par une convention de rattachement. Les situations antérieures gardent leurs transitions ; les protections propres à une branche ne s'éteignent pas par défaut d'accord.",
    "La suppression ne s'applique pas rétroactivement à toutes les anciennes harmonisations et ne chiffre pas le coût des négociations évitées. La dérogation de cinq ans n'est pas une immunité générale contre les discriminations ; après elle, le droit commun s'applique. Aucune baisse de salaire ou de prélèvement n'est déduite.",
    "Aucune charge nouvelle n'est identifiée : aucun plan, dépôt périodique, accord obligatoire ou justification ne remplace l'harmonisation sous cinq ans. La dérogation favorable temporaire est conservée pour les regroupements futurs sur la même durée ; le contrôle de droit commun après cinq ans et la réserve constitutionnelle ne sont pas des obligations nouvelles.",
    proposed=x33, category='material_reduction',
    removed=["Pour les accords de regroupement futurs, obligation de remplacer les stipulations relatives à des situations équivalentes par des stipulations communes dans les cinq ans.",
             "Pour les accords de regroupement futurs, application automatique de la convention de la branche de rattachement en l'absence d'accord d'harmonisation au terme des cinq ans."],
    effects=[effect('obligation_removed', 'branches-regroupement-harmonisation-facultative',
        "Retrait de l'harmonisation obligatoire sous cinq ans et de sa substitution automatique pour les nouveaux regroupements volontaires.",
        "Après fusion ou regroupement, stipulations des situations équivalentes remplacées sous cinq ans ; à défaut d'accord, application de la convention de rattachement, sous la réserve des situations spécifiques.",
        "Pour les nouveaux accords de regroupement, harmonisation facultative sans échéance légale ; coexistence dans les champs respectifs sans substitution automatique ; dérogation favorable sur les différences temporaires maintenue pendant cinq ans puis droit commun.",
        'legal_duty', "Organisations négociatrices, employeurs et salariés des branches volontairement regroupées après la réforme.",
        "Accords conclus à compter de la réforme ; fusions prononcées et regroupements convenus antérieurement gardent le délai et les effets anciens sous la réserve constitutionnelle.",
        "Aucun calendrier, plan ou rapport de remplacement ; pas d'immunité générale nouvelle contre les recours.",
        "A défaut d'accord conclu dans ce délai, les stipulations de la convention collective de la branche de rattachement s'appliquent.",
        "Pour les accords de regroupement conclus à compter de cette entrée en vigueur, l'adoption de stipulations communes est facultative et n'est soumise à aucun délai légal d'harmonisation.")])
a33['benefit_review'] = "Les stipulations spécifiques de chaque branche, y compris garanties et dérogations favorables, ne disparaissent plus automatiquement dans les regroupements futurs et restent ouvertes aux situations futures éligibles. La dérogation favorable de cinq ans pour les différences temporaires résultant du regroupement est expressément conservée pour les futurs accords, depuis leur date d'effet, malgré le retrait de l'échéance d'harmonisation. Pour les fusions et regroupements antérieurs, le régime de cinq ans et les effets acquis demeurent, avec la réserve constitutionnelle protégeant les situations spécifiques. Aucun avantage fiscal ni exonération sociale n'est retiré."

orig34 = [unescape(re.sub('<[^>]+>', '', t)).strip() for t in re.split(r'<br\s*/?>\s*<br\s*/?>', re.search(r'<p[^>]*>(.*?)</p>', by_number['L2261-34']['source_xml'], re.S).group(1))]
assert len(orig34) == 3
source34_first = orig34[0]
orig34[0] = "Jusqu'à la mesure de la représentativité des organisations professionnelles d'employeurs qui suit une fusion de champs conventionnels prononcée avant l'entrée en vigueur de la loi supprimant ce pouvoir, en application du I de l'article L. 2261-32 dans sa rédaction alors applicable, ou qui suit la conclusion d'un accord collectif regroupant le champ de plusieurs conventions préexistantes, sont admises à négocier les organisations professionnelles d'employeurs représentatives dans le champ d'au moins une branche préexistant à la fusion ou au regroupement."
x34 = body(*orig34,
    "Les dispositions relatives aux accords collectifs de regroupement demeurent applicables aux accords conclus après cette entrée en vigueur. Elles ne permettent ni une nouvelle fusion administrative sur le fondement abrogé ni une dérogation aux majorités et conditions de validité des accords.",
    "Après la mesure de l'audience suivant une fusion administrative antérieure à cette entrée en vigueur, les organisations d'employeurs et de salariés qui ont perdu leur caractère représentatif à l'échelle de la branche issue de la fusion peuvent continuer à participer aux discussions relatives à l'accord de remplacement. Cette participation ne leur permet ni de signer cet accord, ni de s'y opposer, ni de s'opposer à son éventuelle extension.")
entry('L2261-34',
    "Coordination nécessaire avec l'abrogation prospective du pouvoir de fusion : le renvoi au I de L2261-32 devient expressément historique, tandis que la représentation transitoire des regroupements volontaires reste ouverte aux accords futurs. Les trois alinéas d'origine et l'assiette des taux sont conservés. La participation aux discussions des anciennes organisations devenues non représentatives après une fusion est explicitée conformément à la réserve constitutionnelle, sans leur donner de droit de signature ou de veto.",
    "Le dernier alinéa de L2261-19 conserve plus de 50 % des salariés des entreprises adhérant aux organisations patronales représentatives ; L2232-6, lu dans le corpus, exige au moins 30 % des suffrages des organisations représentatives et absence d'opposition syndicale majoritaire, avec quinze jours d'opposition. Ces taux s'apprécient au niveau de la branche issue du regroupement, non dans chaque ancienne branche. La construction source « qui suit la fusion ... ou de la conclusion » est rectifiée en deux compléments de « qui suit », sans modifier les événements visés. La note source de L2261-34 cite « 2020-816 QPC du 29 novembre 2019 » ; incohérence préexistante signalée : la note de L2261-33 porte le numéro 2019-816 pour cette date. La réserve décrite dans la note est reprise sans prétendre avoir effectué une consultation externe du Conseil constitutionnel. La garantie ajoutée sur les discussions vise les fusions antérieures, non tous les accords volontaires par extension implicite.",
    "Aucune réduction autonome de charge : la modification borne un renvoi à des fusions anciennes et conserve la représentation de transition ainsi que la réserve constitutionnelle. La suppression de la fusion forcée est comptée seulement à L2261-32.",
    "Ni les seuils de représentativité ni les majorités ne sont réduits. La concordance du numéro de la décision constitutionnelle reste signalée ; aucun audit externe de jurisprudence n'est revendiqué.",
    "Aucune charge nouvelle n'est identifiée : aucune mesure d'audience supplémentaire ni formalité nouvelle ; le droit de participer aux discussions décrit par la note source n'est pas transformé en signature ou opposition nouvelle.",
    proposed=x34, category='coordination_only',
    effects=[effect('coordination', 'branches-fin-restructuration-administrative-forcee',
        "Borne historique du renvoi aux anciennes fusions sans fermeture des regroupements volontaires futurs.",
        "Admission transitoire des organisations d'au moins une branche préexistante après fusion administrative ou accord de regroupement jusqu'à la mesure de représentativité suivante.",
        "Même admission pour les fusions déjà prononcées et pour les regroupements volontaires actuels ou futurs ; aucune nouvelle fusion sur le fondement abrogé.",
        'regime', "Organisations patronales et syndicales des branches fusionnées avant la réforme ou volontairement regroupées.",
        "Fusions administratives limitées aux décisions antérieures à l'entrée en vigueur ; taux au niveau de la nouvelle branche ; réserve de participation aux discussions maintenue.",
        "Aucun dépôt ou scrutin supplémentaire ; pas de nouveau droit de signature ou de veto pour les organisations non représentatives.",
        source34_first,
        orig34[0])])


# Les contrôles ciblés couvrent exactement requirements, y compris les cibles
# contextuelles qui ne correspondent pas à un renvoi littéral de l'article.
checks = {
    'L2261-14-3': {
        'L1234-1': "Aucun renvoi littéral à L1234-1 : L2261-14-3 autorise un accord collectif anticipé, sans rompre les contrats transférés. Il ne déclenche donc ni l'ancien préavis gradué par ancienneté, ni les quinze jours des nouveaux contrats prévus par la proposition. La notification d'une rupture distincte et ses protections demeurent nécessaires ; le transfert seul ne transforme pas un contrat antérieur en contrat nouveau.",
        'L1221-2': "La substitution concerne les conventions collectives, non la durée ou la naissance des contrats individuels. La proposition de L1221-2 interdit un terme aux nouveaux recrutements, y compris à la fin d'une mission ou d'une formation ; un transfert n'est pas une nouvelle embauche. L2261-14-3 maintenu n'ouvre aucun nouveau CDD ni renouvellement contournant cette règle et ne remet à zéro ni ancienneté ni créance des contrats antérieurs.",
        'L1234-9': "L'accord anticipé n'est pas une rupture patronale et n'ouvre par lui-même aucune indemnité de L1234-9. Si une rupture distincte intervient, la proposition réserve aux nouveaux contrats le seuil d'un an à la fin effective, préavis compris, puis 0,20 mois par année totale et mois complets, plafond légal six mois. Les anciens contrats gardent leur condition de huit mois et leurs composantes ; L2261-14-3 n'efface ni ces droits ni les indemnités spéciales ou conventionnelles plus favorables."
    },
    'L2261-14-4': {
        'L1234-1': "Les 1° et 2° de L2261-14-4 fixent le périmètre des majorités de l'accord de substitution, pas les 1° à 3° du préavis légal de L1234-1. Les taux s'apprécient selon le transfert ou chaque entreprise concernée ; ils n'imposent aucune ancienneté individuelle. Le préavis proposé de quinze jours exige une rupture distincte notifiée selon ses règles, et ne remplace ni la consultation collective ni les protections spéciales.",
        'L1221-2': "La validité de l'accord anticipé s'apprécie dans les périmètres propres aux deux voies, pour les contrats transférés quelle que soit leur date. Elle n'autorise pas un terme au nouveau contrat unique de L1221-2. La durée de l'accord transitoire de L2261-14-2, au plus trois ans selon la cible de contexte lue, ne fixe pas celle de l'emploi. Les anciens contrats restent des contrats antérieurs et ne perdent pas leur ancienneté du fait du vote.",
        'L1234-9': "Les taux et consultations de L2261-14-4 ne sont pas le seuil d'ancienneté de l'indemnité et leur notification d'accord n'est pas une notification de rupture. L1234-9 proposé reste seul applicable à une rupture patronale distincte : un an mesuré au terme effectif pour les nouveaux contrats, toute l'ancienneté ensuite, mois complets et plafond légal de six mois, sans effacer le régime des anciens contrats ni les réparations et indemnités spéciales."
    },
    'L2261-22': {
        'L1234-1': "Le II 7° porte sur la rupture mais ne renvoyait pas textuellement à L1234-1 ; il ne peut servir à rétablir les anciens préavis conventionnels pour les contrats nouveaux. La proposition coordonnée fixe quinze jours calendaires des deux côtés, à compter du lendemain de la présentation ou réception écrite, sans condition d'ancienneté ; les dispenses favorables du salarié sont gardées. Les anciens contrats conservent leurs règles graduées ou plus favorables, et les procédures collectives ou autorisations spéciales restent distinctes du préavis.",
        'L1221-2': "Le renvoi ajouté pour les clauses de recrutement et de rupture vise la durée indéterminée des nouveaux contrats de L1221-2 proposé, non une interdiction des missions temporaires. L'alinéa initial de la cible exclut le terme automatique ; son deuxième autorise la durée limitée d'une formation ou affectation sans fin de l'emploi ; son troisième préserve l'ancien stock sans nouveau renouvellement contournant la réforme. Les garanties du II 12° e restent ainsi ouvertes sans recréer un CDD.",
        'L1234-9': "Le renvoi ajouté à l'article entier applique l'indemnité ordinaire patronale des nouveaux contrats : zéro avant un an au terme effectif avec préavis inclus, puis 0,20 mois de salaire par année totale, mois complets au prorata et plafond légal six mois, sous l'exception de faute grave de la proposition. La première année n'est pas soustraite ; la démission ordinaire n'ouvre pas cette indemnité. Le texte réserve les anciens huit mois d'ouverture, les deux composantes sans double compte, les droits plus favorables, salaires, congés, dommages et indemnités spéciales.",
        'L911-7': "Le II 14° renvoie précisément au II de L911-7 : participation de l'assuré, forfait journalier et frais dentaires ou dispositifs médicaux, avec contrats responsables ; ce renvoi est conservé. Il n'absorbe pas le III, qui prévoit au moins la moitié du financement par l'employeur et des dispenses, ni le IV relatif au régime local. La proposition fournie étend les dispenses temporaires aux affectations éligibles dans le contrat unique sans terme d'emploi ; ces facultés restent accessibles aux situations futures et les anciens contrats gardent leurs droits."
    },
    'L2261-33': {
        'L1234-1': "L2261-33 ne renvoie pas littéralement à L1234-1 : ses cinq ans concernent l'harmonisation et les différences temporaires de traitement entre branches, non un préavis individuel. La source officielle de L1234-1 prévoit des durées graduées selon l'ancienneté et des règles plus favorables ; sa proposition les conserve pour les contrats antérieurs et fixe quinze jours calendaires pour les nouveaux contrats, sans condition d'ancienneté, y compris en cas de faute grave avec paiement si le maintien au travail est impossible. La coexistence conventionnelle permise par L2261-33 ne rétablit pas pour ces nouveaux contrats une durée incompatible avec cette proposition et la décision travail. Une rupture distincte nécessite sa notification écrite, avec départ le lendemain de sa présentation ou réception selon la coordination retenue ; ni le regroupement ni l'expiration des cinq ans ne valent notification. Les dispenses favorables à l'initiative du salarié et les procédures collectives et autorisations spéciales restent distinctes.",
        'L1221-2': "Le regroupement de champs conventionnels de L2261-33 ne conclut ni ne renouvelle par lui-même les contrats de travail. La source officielle de L1221-2 admet encore certains contrats à terme ; la proposition fournie les exclut pour les nouvelles embauches et reconductions postérieures à la réforme. La phrase finale proposée de L2261-33 soumet expressément les accords de regroupement à ces règles légales dans leur champ temporel : durée de l'accord, phase d'harmonisation de cinq ans, mission ou formation ne fixent pas de terme au nouvel emploi. La coexistence des conventions ne constitue pas une voie spéciale de CDD. Les contrats antérieurs et leurs litiges de terme conservent leur transition, sans remise à zéro d'ancienneté et sans disparition des garanties ou dérogations applicables aux futures situations éligibles.",
        'L1234-9': "L2261-33 règle la survie et le remplacement des stipulations collectives ; il ne crée ni rupture patronale ni indemnité par le seul regroupement. La source officielle de L1234-9 ouvre l'indemnité légale à huit mois sauf faute grave ; la proposition réserve aux nouveaux contrats le seuil d'un an mesuré à la fin effective, préavis inclus sous la réserve de fin d'essai. Une fois ce seuil atteint : 0,20 mois de salaire brut de référence par année totale, fractions au prorata des mois complets et plafond légal de six mois ; la première année est comptée, la démission ordinaire n'ouvre pas ce droit et l'exception de faute grave reste propre à la cible proposée. Le maintien des conventions par L2261-33 conserve les indemnités conventionnelles plus favorables pour leurs futurs bénéficiaires : il ne les soumet pas au plafond légal. Pour les contrats antérieurs, condition de huit mois et deux composantes préservées s'appliquent sans double compte ; salaires, congés, réparations d'illégalité et indemnités spéciales restent distincts."
    }
}
for number, a in answers.items():
    key = a['code_id'] + '|' + a['source_id']
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        a['reference_checks'].append(dict(target_key=target_key,
            view_sha256=target['view_sha256'],
            assessment=checks[number][target['number']]))


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)


def plain(xml):
    parser = Text()
    parser.feed(xml or '')
    return ''.join(parser.parts)


class Allowed(HTMLParser):
    tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
    def handle_starttag(self, tag, attrs):
        assert tag in self.tags, tag
        for k, v in attrs:
            assert k in ('rowspan', 'colspan') and re.fullmatch(r'[0-9]+', v), (k, v)


def validate():
    assert len(answers) == len(sources) == 24
    assert set(answers) == set(by_number)
    for src in sources:
        a = answers[src['number']]
        for k in ('code_id', 'source_id', 'source_sha256', 'number'):
            assert a[k] == src[k]
        key = a['code_id'] + '|' + a['source_id']
        assert [c['target_key'] for c in a['reference_checks']] == refs['requirements'][key]
        for check in a['reference_checks']:
            assert check['view_sha256'] == refs['targets'][check['target_key']]['view_sha256']
            assert len(check['assessment']) >= 80
        impact = a['substantive_impact']
        assert impact['version'] == 1
        for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(impact[k]) >= 40
        if a['status'] == 'retained_unchanged':
            assert a['proposed_xml'] is None and a['classification'] == 'retained_necessary'
            assert impact['classification'] == 'retained_necessary' and impact['effects'] == []
        else:
            assert a['proposed_xml'] and a['status'] == 'rewrite_draft'
            Allowed().feed(a['proposed_xml'])
            # Le corps, sans racine supplémentaire dans le fichier, doit pouvoir
            # être lu comme un fragment XML équilibré.
            import xml.etree.ElementTree as ET
            ET.fromstring('<root>' + a['proposed_xml'] + '</root>')
        if src.get('benefit_check_required'):
            assert len(a['benefit_review']) >= 100
        if a.get('change_type') == 'full_repeal':
            assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
            assert len(a['repeal_scope']) >= 30
        if a.get('change_type') == 'normative_reduction':
            assert all(len(x) >= 30 for x in a['removed_provisions'])
        for e in impact['effects']:
            assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)+', e['measure_id'])
            assert 6 <= len(e['measure_id']) <= 96
            assert e['kind'] in {'tax_removed','tax_reduced','obligation_removed','obligation_merged','authorization_removed','regime_merged','deadline_reduced','compliance_cost_reduced','tax_increased','obligation_added','deadline_increased','complexity_added','financing_transfer','payment_deferred','relief_extended','relief_preserved','coordination'}
            assert e['unit'] in {'percent','euro','legal_duty','regime','calendar_days','working_days','financing','other'}
            for quote, xml in [(e['source_quote'],src['source_xml']), (e['proposed_quote'],a['proposed_xml'])]:
                assert len(quote) >= 12
                assert quote in plain(xml), (a['number'], 'citation non exacte', quote)
    # Contrôle de l'intégralité des énumérations conservées.
    proposed22 = paragraphs('L2261-22')
    for i, para in enumerate(proposed22):
        if i != 4:
            assert para in plain(answers['L2261-22']['proposed_xml'])
    for para in paragraphs('L2261-32')[11:15] + paragraphs('L2261-32')[17:18]:
        assert para in plain(answers['L2261-32']['proposed_xml'])
    for para in paragraphs('L2261-27')[1:4]:
        assert para in plain(answers['L2261-27']['proposed_xml'])
    return [answers[src['number']] for src in sources]


if __name__ == '__main__':
    result = validate()
    (ROOT / 'answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'articles': len(result), 'rewrite_draft': sum(a['status']=='rewrite_draft' for a in result),
        'retained_unchanged': sum(a['status']=='retained_unchanged' for a in result),
        'reference_checks': sum(len(a['reference_checks']) for a in result),
        'effects': sum(len(a['substantive_impact']['effects']) for a in result)}, ensure_ascii=False))
