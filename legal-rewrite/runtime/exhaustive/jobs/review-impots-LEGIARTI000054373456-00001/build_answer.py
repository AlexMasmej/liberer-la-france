import html
import json
import re
from pathlib import Path


source = json.loads(Path('source.json').read_text())[0]
references = json.loads(Path('reference-targets.json').read_text())
paragraphs = re.findall(r'<p>.*?</p>', source['source_xml'], re.S)
assert len(paragraphs) == 58
original = paragraphs.copy()

# Les alinéas sans réforme restent dans leur rédaction officielle, à leur place.
paragraphs[11] = "<p>Cette exonération est applicable aux opérations effectuées par les coopératives de céréales et leurs unions avec l'Etablissement national des produits de l'agriculture et de la mer (FranceAgriMer) relativement à l'achat, la vente, la transformation ou le transport de céréales ; il en est de même pour les opérations effectuées par des coopératives de céréales avec d'autres coopératives de céréales, sans condition de programme élaboré par l'établissement ni d'autorisation de celui-ci.</p>"
paragraphs[12] = "<p>Le respect, par les sociétés coopératives agricoles et leurs unions, des dispositions législatives et réglementaires relatives au statut juridique de la coopération agricole est vérifié dans le cadre des contrôles fiscaux de droit commun. Le présent article n'impose aucune production spéciale de comptabilité ou de justificatifs en sus des obligations de droit commun ;</p>"
paragraphs[14] = "<p>4° Les organismes d'habitations à loyer modéré mentionnés à l'article L. 411-2 du code de la construction et de l'habitation, les sociétés d'économie mixte visées à l'article L. 481-1 du même code et les sociétés anonymes dont le bénéfice du présent 4° est maintenu par le troisième alinéa du V de l'article 81 de la loi n° 2018-1021 du 23 novembre 2018, pour :</p>"
paragraphs[18] = "<p>La fraction du bénéfice provenant d'activités autres que celles visées aux alinéas précédents ne bénéficie pas de l'exonération du présent 4°. Lorsqu'elle relève de l'impôt sur les sociétés ordinaire, elle est imposée dans les conditions prévues au 4 du présent article.</p>"
paragraphs[19] = "<p>Pour l'application des dispositions du premier alinéa de l'article 221 bis, la deuxième condition mentionnée à cet alinéa n'est pas exigée des sociétés qui cessent totalement ou partiellement d'être soumises au taux prévu au deuxième alinéa du I de l'article 219 du fait des dispositions du présent 4°. Les dispositions de l'article 111 bis ne s'appliquent pas à ces mêmes sociétés. La même dispense et la même exclusion s'appliquent lorsque le présent 4° exonère des bénéfices qui relevaient du régime ordinaire d'imposition à la distribution.</p>"
paragraphs[28] = "<p>5° Les bénéfices réalisés par des associations sans but lucratif régies par la loi du 1er juillet 1901 organisant des foires, expositions, réunions sportives et autres manifestations publiques, correspondant à l'objet défini par leurs statuts et présentant, du point de vue économique, un intérêt certain pour la commune ou la région. Le concours d'une commune ou d'un département n'est pas exigé pour bénéficier de cette exonération ;</p>"
paragraphs[29] = "<p>5° bis. Les organismes sans but lucratif mentionnés au 1° du 7 de l'article 261, pour les opérations à raison desquelles ils sont exonérés de la taxe sur la valeur ajoutée. En cas d'abrogation ou de recodification de ces dispositions, l'exonération d'impôt sur les sociétés reste applicable aux organismes et aux opérations qui remplissent les conditions qu'elles prévoyaient dans leur rédaction en vigueur le 1er juillet 2026, ainsi qu'aux organismes sans but lucratif et aux opérations exonérées de taxe sur la valeur ajoutée en application des dispositions qui leur succèdent. Elle reste ouverte aux opérations nouvelles remplissant ces conditions ;</p>"

new_paragraphs = [
    "<p>4. Pour les exercices relevant du 12 de l'article 206, les exonérations du présent article sont maintenues, y compris pour les activités et opérations nouvelles qui remplissent leurs conditions. Une fraction de bénéfice exonérée ne devient pas imposable à l'impôt sur les sociétés ordinaire du seul fait de sa mise en réserve, de son report, de sa conservation en trésorerie ou de sa distribution. Aucun investissement ni délai de réinvestissement n'est exigé à ce titre.</p>",
    "<p>Les fractions non exonérées qui relèvent du régime ordinaire ne sont imposables qu'à la distribution, dans les conditions des XI à XIII de l'article 209 et des V et VI de l'article 219. La détermination des résultats et des fractions visées aux 1 bis à 1 quater n'entraîne aucune imposition annuelle des bénéfices conservés. Les régimes distincts mentionnés au 12 de l'article 206 et l'impôt minimum international prévu aux articles 223 VJ et suivants conservent leur champ propre.</p>",
    "<p>Les bénéfices sont suivis dans la comptabilité existante selon leur fraction exonérée ou imposable et les conditions attachées à cette qualification, conformément au XI de l'article 209. Aucun registre, état déclaratif ou certificat distinct n'est exigé au titre du présent article. Les exonérations définitivement acquises et les réserves déjà imposées sont protégées selon le même XI ; les dividendes entre sociétés, déficits et crédits relèvent de leurs dispositions propres, sans double inscription ni double utilisation. La distribution ne renouvelle ni une exonération consommée ni un avantage historique expiré. Les conditions de fond des exonérations et la fiscalité propre des associés demeurent applicables.</p>",
    "<p>Le 4 et l'adaptation au régime de distribution prévue au 4° du 1 s'appliquent aux exercices ouverts à compter de l'entrée en vigueur de la présente loi. La suppression, au 3° du 1, de la condition de programme ou d'autorisation pour les opérations entre coopératives de céréales et, au 5° du même 1, de la condition de concours d'une commune ou d'un département s'applique aux opérations réalisées à compter de cette entrée en vigueur, y compris au cours d'un exercice ouvert antérieurement. La suppression de la production documentaire spéciale prévue au 3° du 1 s'applique à toute demande adressée à compter de cette entrée en vigueur ; les pièces déjà régulièrement détenues restent utilisables pour les contrôles de droit commun. Aucune production n'est exigée après cette date sur le seul fondement de l'obligation spéciale supprimée. Sous réserve de ces allègements, les exercices ouverts antérieurement, les dettes, créances, contrôles, restitutions et recours qui s'y rattachent restent régis par les dispositions qui leur étaient applicables. La continuité de l'exonération prévue au 5° bis du 1 s'applique, en cas d'abrogation ou de recodification des dispositions auxquelles il renvoie, aux opérations réalisées à compter de cette abrogation ou recodification ; les droits afférents aux opérations antérieures sont préservés.</p>",
]
proposed = '\n'.join(paragraphs + new_paragraphs)


def plain(value):
    return html.unescape(re.sub(r'<[^>]*>', '', value))


def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           replacement_or_new_burdens, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in plain(source['source_xml'])
    assert len(proposed_quote) >= 12 and proposed_quote in plain(proposed)
    return dict(
        kind=kind, measure_id=measure_id, description=description,
        before=before, after=after, unit=unit,
        affected_population=affected_population,
        conditions_and_transition=conditions_and_transition,
        replacement_or_new_burdens=replacement_or_new_burdens,
        source_quote=source_quote, proposed_quote=proposed_quote,
    )


effects = [
    effect(
        'obligation_removed', 'cooperatives-agricoles-fin-requisition-speciale',
        "Suppression de la production spéciale de comptabilité et de justifications sur le seul fondement du 3° du 1 ; réforme déjà acquise dans le brouillon, conservée après réexamen.",
        "Les coopératives agricoles et leurs unions doivent produire leur comptabilité et les justifications de leur conformité statutaire à toute réquisition de l'administration, en plus du cadre fiscal commun.",
        "Aucune production spéciale fondée sur cet article ; les obligations et pouvoirs de contrôle de droit commun restent applicables.",
        'legal_duty', 'Sociétés coopératives agricoles et leurs unions.',
        "Demandes adressées à compter de l'entrée en vigueur, même pour un exercice ancien ; les pièces déjà détenues restent utilisables et les contrôles autonomes subsistent.",
        "Aucune déclaration, attestation ou autorisation de remplacement ; maintien du contrôle de la conformité au statut coopératif par les voies fiscales communes.",
        plain(original[12]), plain(paragraphs[12]),
    ),
    effect(
        'relief_extended', 'is-cereales-exoneration-sans-programme-ni-autorisation',
        "Extension de l'exonération aux opérations entre coopératives de céréales sans programme FranceAgriMer ni autorisation de cet établissement comme préalable fiscal ; coupe supplémentaire par rapport au brouillon.",
        "Pour ces opérations entre coopératives de céréales, l'exonération est subordonnée à un programme élaboré par l'établissement ou à son autorisation ; le texte ne fixe pas de taux propre.",
        "Même exonération totale d'IS sur ces opérations, sans ces deux voies préalables ; les conditions de fonctionnement coopératif et les limites des 1 bis à 1 quater subsistent.",
        'regime', "Coopératives de céréales effectuant des opérations avec d'autres coopératives de céréales ; aucune extension indistincte aux opérations avec tous tiers.",
        "Opérations réalisées dès l'entrée en vigueur, y compris dans un exercice en cours ; les opérations anciennes conservent leur régime.",
        "Pas de déclaration de remplacement. La suppression vise la condition fiscale du 3°, non les obligations agricoles autonomes ou celles résultant du droit de l'Union.",
        "il en est de même pour les opérations effectuées par des coopératives de céréales avec d'autres coopératives de céréales dans le cadre de programmes élaborés par l'établissement ou avec son autorisation.",
        "il en est de même pour les opérations effectuées par des coopératives de céréales avec d'autres coopératives de céréales, sans condition de programme élaboré par l'établissement ni d'autorisation de celui-ci.",
    ),
    effect(
        'relief_extended', 'is-manifestations-associatives-sans-concours-local',
        "Retrait du concours obligatoire d'une commune ou d'un département comme condition d'exonération des bénéfices des manifestations associatives ; coupe supplémentaire par rapport au brouillon.",
        "Exonération des bénéfices des manifestations du 5° seulement si elles sont organisées avec le concours des communes ou des départements et remplissent les autres conditions de ce 5°.",
        "Même exonération des mêmes bénéfices sans concours local imposé ; association non lucrative régie par la loi de 1901, objet statutaire et intérêt économique certain pour la commune ou la région maintenus.",
        'regime', "Associations sans but lucratif organisant les foires, expositions, réunions sportives ou autres manifestations publiques du 5°.",
        "Opérations réalisées dès l'entrée en vigueur, y compris dans un exercice déjà ouvert ; pas de restitution générale pour les opérations anciennes.",
        "Aucun agrément, partenariat ou document supplémentaire remplaçant ce concours. Les conditions substantielles déjà présentes demeurent.",
        plain(original[28]), plain(paragraphs[28]),
    ),
    effect(
        'coordination', 'is-distribution',
        "Coordination de l'IS à la distribution : le 4° et les calculs des fractions coopératives ne rétablissent pas l'IS ordinaire annuel sur les bénéfices conservés. Ce renvoi n'est pas une deuxième abolition d'IS.",
        "L'article 207 exonère certaines personnes et fractions ; il soumet expressément la fraction des autres activités HLM à l'IS et renvoie au résultat de l'article 209, sans régime de distribution dans ce corps officiel.",
        "Les fractions non exonérées relevant du régime ordinaire suivent les XI à XIII de 209 et les V et VI de 219, avec exigibilité à la distribution ; les fractions exonérées le restent. L'article 207 ne fixe aucun taux nouveau.",
        'regime', "Personnes et fractions relevant du régime ordinaire du 12 proposé de l'article 206 ; les régimes distincts et le minimum international ne sont pas absorbés.",
        "Exercices ouverts à compter de l'entrée en vigueur ; exercices anciens, créances, dettes et recours protégés. Les dispenses des articles 221 bis et 111 bis sont étendues au passage à l'exonération du 4° depuis le régime de distribution.",
        "Le suivi temporel est recensé séparément sous la même mesure ; aucun acompte annuel ni investissement obligatoire n'est créé par 207.",
        plain(original[18]),
        plain(new_paragraphs[1]),
    ),
    effect(
        'complexity_added', 'is-distribution',
        "Formalisation d'un suivi temporel des fractions exonérées ou imposables et de leur qualification dans la comptabilité existante ; charge liée à la conservation des avantages et à l'absence de double IS.",
        "La source impose déjà la détermination des résultats avant ristournes et des fractions exonérées, sans prescrire ici leur suivi temporel dans le nouveau régime de distribution.",
        "Le nouveau 4 demande de suivre ces bénéfices selon leur qualification, conformément au XI proposé de 209, sans registre, état ou certificat distinct propre à 207.",
        'legal_duty', "Personnes relevant à la fois des exonérations de 207 et du nouveau régime ordinaire de distribution, pour leurs fractions de bénéfices concernées.",
        "Exercices nouveaux ; les réserves déjà imposées, exonérations définitivement acquises, déficits et crédits suivent leurs règles propres sans double emploi.",
        "Identification dans le temps nouvellement explicitée, même sans support supplémentaire. Les comptes et le rapprochement annuel prévus par 209 sont une charge commune de cette réforme, non une seconde formalité autonome créée par 207. Coût net non établi.",
        plain(original[51]),
        "Les bénéfices sont suivis dans la comptabilité existante selon leur fraction exonérée ou imposable et les conditions attachées à cette qualification, conformément au XI de l'article 209. Aucun registre, état déclaratif ou certificat distinct n'est exigé au titre du présent article.",
    ),
    effect(
        'relief_preserved', 'is-exoneration-organismes-non-lucratifs',
        "Fondement de continuité pour l'exonération du 5° bis lors de l'abrogation ou de la recodification de l'article 261, annoncée par ses notes ; maintien pour les opérations futures.",
        "Exonération d'IS définie par renvoi au 1° du 7 de 261 et à l'exonération de TVA des opérations ; les notes de 261 annoncent l'abrogation différée de la plupart de ses dispositions, sans cible de substitution fournie.",
        "Le champ du renvoi est conservé, avec un plancher autonome fondé sur la rédaction connue au 1er juillet 2026 et maintien du bénéfice lié aux dispositions de TVA qui succèdent à ce même 1° du 7. Aucune fermeture aux opérations nouvelles éligibles.",
        'regime', "Organismes sans but lucratif et opérations du 1° du 7 de l'article 261 ; aucune extension générale à toutes les exonérations de TVA de cet article.",
        "Continuité à compter de l'abrogation ou de la recodification des dispositions visées ; droits afférents aux opérations antérieures préservés. Le 1er juillet 2026 désigne une rédaction source, non la date de la réforme.",
        "Pas de nouvelle demande, certification ou condition d'ancienneté. La concordance détaillée avec le code des impositions sur les biens et services reste à documenter hors de ce lot ; le plancher empêche que cette lacune ferme l'exonération d'IS.",
        plain(original[29]), plain(paragraphs[29]),
    ),
    effect(
        'coordination', 'hlm-exoneration-societes-coordination',
        "Précision du fondement de l'exonération des anciennes sociétés anonymes de coordination maintenues sous leur régime antérieur par la loi de 2018, sans fermeture de l'exonération des organismes HLM actuels.",
        "Le 4° vise les sociétés anonymes de coordination entre organismes HLM par un renvoi à L. 423-1-1, qui traite aujourd'hui des groupes ; les notes de L. 423-1-1 et L. 423-1-2 maintiennent expressément les exonérations des sociétés antérieurement agréées.",
        "Les anciennes sociétés anonymes conservant l'avantage en vertu du troisième alinéa du V de l'article 81 de la loi de 2018 sont expressément couvertes. Les sociétés de coordination actuelles demeurent couvertes comme organismes HLM de L. 411-2, sous les conditions du 4°.",
        'regime', "Sociétés anonymes relevant du maintien légal de 2018 et sociétés de coordination actuelles relevant de L. 411-2 ; pas d'agrément nouveau pour une ancienne société bénéficiaire.",
        "Maintien des droits attachés au régime légal applicable aux sociétés déjà agréées à la date de promulgation de la loi de 2018, y compris pour leurs opérations futures éligibles. Pas de réouverture des anciens agréments pour de nouvelles personnes morales.",
        "Aucune formalité ni condition de fond supplémentaire : le renvoi désigne expressément une transition légale existante. Ce maintien ne compte pas comme nouvelle baisse d'impôt.",
        plain(original[14]), plain(paragraphs[14]),
    ),
]

reason = (
    "Réécriture normative complète, sans toilettage des dispositions utiles : les 58 emplacements d'alinéas sources sont conservés et seules sept positions sont modifiées, puis un 4 de coordination et de transition est ajouté. "
    "Réformes de fond supplémentaires à la seconde passe : suppression du préalable fiscal de programme ou d'autorisation FranceAgriMer pour les opérations entre coopératives de céréales ; suppression du concours obligatoire d'une commune ou d'un département pour l'exonération des manifestations associatives du 5°. Ces concours ne démontrent pas, à eux seuls, une fonction nécessaire à la preuve du caractère coopératif ou non lucratif, déjà vérifiable par les conditions et contrôles conservés. "
    "La suppression déjà acquise de la réquisition documentaire spéciale des coopératives agricoles est maintenue sans déclaration de remplacement. La coordination déjà acquise avec l'IS à la distribution et les dispenses favorables de 221 bis et 111 bis sont conservées. Le renvoi du 5° bis à 261 est sécurisé contre l'abrogation différée annoncée, en maintenant l'accès aux opérations futures éligibles. "
    "La désignation des anciennes sociétés de coordination HLM est rattachée expressément à leur maintien légal de 2018, sans restreindre les exonérations des organismes HLM actuels. "
    "À droit constant, les autres bénéficiaires, activités, exclusions, agréments sectoriels utiles, pourcentages de capital, règles avant ristournes et dispositions historiques sont reproduits intégralement. Les limites au capital extérieur restent nécessaires pour délimiter le régime coopératif plutôt que l'étendre indistinctement à l'investissement commercial ; les mandats et conditions SIEG protègent l'affectation sociale et les exigences européennes. Aucun taux nouveau n'est inventé. "
    "Le classement mixed tient au suivi temporel des fractions de bénéfices nouvellement explicité pour l'IS à la distribution ; les trois allègements identifiés ne prouvent ni un solde net de complexité ni une économie budgétaire nationale."
)

review_notes = (
    "Sources assignées et précédent brouillon lus intégralement, note source comprise ; 58 paragraphes, aucun tableau, aucune formule-image ni pièce source_companions. Le proposed_xml du premier niveau est identique au previous_draft après décodage des entités HTML. La proposition finale conserve dans l'ordre les 58 positions, dont 51 paragraphes source strictement identiques ; les changements portent sur les positions 12, 13, 15, 19, 20, 29 et 30, sans déplacement des alinéas cibles. Quatre paragraphes sont ajoutés au 4. "
    "Contrôle des chiffres et champs : 20 p. 100 au moins au 1 ter et strictement plus de 50 % au 1 quater, droits dans le capital et montant nominal des certificats au 1 bis, détermination avant ristournes, exclusions des non-sociétaires et opérations de détail/transformation au 3° conservés. Le maintien de la disjonction source « autres que ... ou autres que ... » au 1 ter ne tranche pas son ambiguïté préexistante ; une clarification de son champ demande un examen propre, sans élargir silencieusement une exclusion d'exonération. "
    "Les dates du 1er janvier 2005 et du 1er janvier 2006 conservent leur objet historique HLM ; ni l'option anticipée ni l'avantage de transformation du 12° ne sont recréés à chaque distribution. La suppression des conditions céréalières et de concours local vise les opérations nouvelles dès l'entrée en vigueur, y compris dans un exercice en cours ; elle ne rembourse pas les impositions des anciennes opérations. La réquisition spéciale disparaît pour les demandes nouvelles même relatives à d'anciens exercices ; pouvoirs et preuves de droit commun restent. "
    "Renvois supplémentaires vérifiés en lecture seule dans le corpus : 209, XI à XIII, et 219, V et VI, sont des subdivisions proposées, absentes du droit officiel actuel ; elles organisent le compte protégé, les compartiments, les déficits, crédits, taux favorables et le paiement à la distribution. Le 12 proposé de 206 fixe le même passage par exercices ouverts. Le taux français normal du projet est 20 % du bénéfice avant IS distribué, avec maintien du taux réduit PME et des taux de catégorie inférieurs ; ce taux n'est ni ajouté ni recalculé dans 207. Les bénéfices conservés, même en trésorerie, ne supportent pas l'IS ordinaire par le jeu des alinéas maintenus. L'imposition personnelle des associés, les règles de groupes et les régimes distincts restent à leur champ. Aucune contribution additionnelle supprimée par les coordinations de 219 n'est rétablie. "
    "111 bis et 221 bis officiels et proposés lus : le 4° dispense toujours de la deuxième condition de 221 bis, non de la première condition de continuité comptable, et conserve l'exclusion de distribution réputée de 111 bis ; la règle est adaptée aux bénéfices qui quittent le régime de distribution pour l'exonération HLM. Les renvois aux neuvième à treizième et aux neuvième et onzième alinéas de L. 411-2 sont conservés après lecture du corps officiel et proposé : le double élément séparé par des br dans la liste des organismes compte dans la numérotation légale et ne doit pas être omis par un simple comptage de balises p. Les conditions SIEG autonomes, plafonds et comptabilité séparée subsistent. L. 365-2 à L. 365-4 ont été lus : conserver leurs agréments initiaux ne recrée pas les avis, renouvellements, extensions, rapports ou doubles pièces déjà supprimés dans leurs propositions ; pas de second agrément fiscal. "
    "L. 423-1-1 et L. 423-1-2 ont été lus intégralement, propositions et notes comprises. L. 423-1-1 vise aujourd'hui les groupes, tandis que L. 423-1-2 définit les sociétés de coordination actuelles, déjà incluses parmi les organismes HLM de L. 411-2. Le troisième alinéa du V de l'article 81 de la loi n° 2018-1021 maintient explicitement le régime et l'exonération des anciennes sociétés anonymes agréées avant la promulgation de cette loi, selon les notes concordantes des deux articles. Le premier alinéa du 4° rattache ces anciennes sociétés à ce maintien au lieu de faire dépendre leur avantage d'une qualification actuelle de groupe ; leurs opérations futures éligibles restent couvertes. Le texte autonome intégral de cet article 81, hors des cinq codes, n'est pas fourni : la portée retenue est celle de la transition expressément reproduite dans les deux notes et dans les propositions, sans prétendre réécrire toute la loi de 2018. "
    "261 a été lu en entier, y compris ses notes d'abrogation au 1er janvier 2027 et les maintiens transitoires du d du 1° et du 1° ter du 7. Le 5° bis ne renvoie qu'au 1° du 7, pas à tout le 7 ni à tout 261. Le texte prévoit expressément un champ autonome conservé par référence à la rédaction connue au 1er juillet 2026, date de rédaction officielle et non date de promulgation inventée, ainsi que la continuité du bénéfice lié aux seuls successeurs de ce renvoi. La concordance exhaustive TVA/IS avec l'ordonnance n° 2025-1247 du 17 décembre 2025, son article 15 et le code des impositions sur les biens et services n'est pas jointe ; elle reste une coordination précisément identifiée hors des cinq codes. Aucun numéro de remplacement n'est inventé. Le CIBS L. 213-82 et L. 213-107 cités dans les notes de 261 ne suffisent pas à établir toutes les cibles de son 1° du 7. "
    "Les deux extensions fiscales supplémentaires peuvent modifier le périmètre d'aides sectorielles : les règles européennes d'aides d'État, de coopération agricole et de compensations SIEG ne sont pas effacées par la loi nationale proposée ; qualification et éventuelle procédure de mise en conformité du régime modifié restent à coordonner avec les autorités compétentes, sans présumer une exemption de notification ni rétablir un visa FranceAgriMer individuel. Les agréments HLM/SIEG et la validation du projet de santé du 17° gardent une fonction autonome de mission et de protection des bénéficiaires ; pas de suppression aveugle. Aucun impôt sur les capitaux dénoués par décès, CDD, préavis ou indemnité individuelle n'est créé ici. "
    "Renvois ajoutés par rapport à la source officielle, non fournis comme cibles dans reference-targets.json : 209, XI à XIII ; 219, V et VI ; 223 VJ et suivants ; troisième alinéa du V de l'article 81 de la loi n° 2018-1021. Les subdivisions proposées de 209/219 et le corps officiel et proposé de 223 VJ ont été consultés dans le corpus public autorisé ; 223 VJ conserve une imposition minimale annuelle, dont la note source vise les exercices ouverts depuis le 31 décembre 2023. Le chapitre entier 223 VJ et suivants n'est pas déclaré revérifié, et aucune de ses conditions n'est inventée. La transition de l'article 81 est attestée par les notes de L. 423-1-1 et L. 423-1-2 comme précisé ci-dessus. Ces vérifications facultatives restent hors de reference_checks, qui couvre exactement les deux cibles requises. "
    "SRU : texte initial entier de l'article 9 de la loi n° 2000-1208 et toute la piste documentaire fournie lus ; seule la formulation de l'ancien 6° bis y était modifiée. Ce 6° bis est déjà abrogé dans la source assignée. La version LEGIARTI000006308512 ne figure pas dans impots.json et aucune pièce de nom correspondant n'a été trouvée dans le dossier documentaire autorisé ; aucune récupération externe. On ne déduit pas de cette filiation l'origine SRU de toutes les exonérations ni l'achèvement d'un volet non documenté. Les fondements HLM autonomes sont maintenus ; aucun quota communal, rattrapage, prélèvement ou carence SRU n'est réintroduit. TASCOM QPV et dérogations littorales sont hors du champ de cet article, sans modification. "
    "La note assignée mentionne le 1er avril 2026 pour l'ordonnance n° 2021-1843, alors que les métadonnées bornent cette version du 1er juillet 2026 au 1er janvier 2027 et portent ABROGE_DIFF : ces dates ne sont pas celles de la réforme ; le texte entier établissant la version suivante de 207 n'est pas fourni. La conservation des exonérations et le mécanisme de continuité de 261 sont explicités sans présenter cette version future comme lue. L'empreinte source fournie et les view_sha256 requis sont recopiés tels quels ; leur contrôle ne constitue aucune validation juridique. "
    "Chiffrage : pas de rendement inventé. L'extension des exonérations et la dispense documentaire ont des effets non chiffrés. Pour l'IS à la distribution, isoler les gains nouveaux de trésorerie et les fractions déjà exonérées ; comparer le report et la baisse permanente, l'autofinancement, la dette, l'innovation, l'emploi, les recettes induites et les aides effectivement évitées selon scénarios et hypothèses explicites. Aucun retrait de CIR, de crédit ou d'aide n'est décidé par cet article ; le solde public et les coûts comptables restent inconnus."
)

benefit_review = (
    "Examen des avantages de la source entière, sans extinction au seul motif de la distribution ou de l'origine SRU. "
    "1° bis : exonération des syndicats professionnels et unions, toute forme juridique, pour l'étude et la défense des droits et intérêts collectifs de leurs membres ou représentés ; fonctionnement conforme conservé. "
    "2° a et b : sociétés et unions agricoles d'approvisionnement et d'achat restent exonérées hors opérations avec non-sociétaires ; conformité statutaire maintenue. "
    "3° : exonération de production, transformation, conservation et vente agricoles maintenue ; exclusions des magasins distincts, transformations non éligibles et non-sociétaires inchangées. Toutes les opérations céréalières listées avec FranceAgriMer restent couvertes ; l'avantage entre coopératives de céréales est élargi sans programme ni autorisation comme condition fiscale. La suppression documentaire ne supprime pas le bénéfice ni les preuves disponibles de sa condition de fond. "
    "3° bis : coopératives artisanales et unions, entreprises de transports, transport fluvial et coopératives maritimes et unions conservent l'exonération dans leur champ de la loi de 1983 et du code rural, hors affaires avec non-sociétaires. "
    "4° : organismes HLM, SEM et sociétés anonymes de coordination conservent les trois branches de l'exonération : SIEG et certificats d'économies d'énergie, locaux annexes/accessoires nécessaires, produits financiers de trésorerie. Les anciennes sociétés anonymes agréées bénéficiant du maintien légal de 2018 sont expressément couvertes, y compris pour leurs opérations futures éligibles ; les sociétés de coordination actuelles restent couvertes au titre de L. 411-2. Ni nouvelle demande d'agrément ancien ni réouverture du régime historique ne sont imposées ou créées. La fraction des autres activités reste distincte, avec IS ordinaire seulement à la distribution lorsqu'elle y relève. La dispense de la seconde condition du premier alinéa de 221 bis et la non-application de 111 bis sont conservées, y compris en sortie du nouveau régime vers cette exonération. Application aux exercices clos dès le 1er janvier 2006 et option irrévocable pour ceux clos dès le 1er janvier 2005 conservées pour leur objet historique, sans recommencement. "
    "4° quater : unions d'économie sociale à dirigeants de droit ou de fait non rémunérés, activités agréées SIEG et services accessoires, locaux nécessaires et produits financiers restent couverts. Les agréments sectoriels et leurs dispenses restent à leur champ, sans nouveau visa fiscal ni rétablissement des renouvellements déjà retirés. "
    "5° : foires, expositions, réunions sportives et autres manifestations publiques d'associations non lucratives de 1901 conservent leur exonération, leur objet statutaire et l'intérêt économique certain ; retrait favorable de la seule condition de concours local pour les opérations futures. "
    "5° bis : exonération d'IS des organismes non lucratifs et opérations du 1° du 7 de 261 préservée, notamment services aux membres et ventes dans leur limite, œuvres sociales/philanthropiques et franchise indexée, six manifestations de bienfaisance ou de soutien, avec les règles et dérogations de gestion désintéressée du d. Aucune des possibilités favorables de rémunération des dirigeants, y compris pour la jeunesse et l'éducation populaire, n'est retirée. Le renvoi est limité au 1° ; le plancher autonome et les dispositions succédant à ce renvoi empêchent une fermeture lors de l'abrogation de 261 et couvrent les futures opérations éligibles. "
    "6° : toutes les catégories de collectivités, ententes, EPCI à fiscalité propre, syndicats exclusivement publics et régies listées gardent l'exonération. "
    "7° : lotissements et ventes sans but lucratif des coopératives de construction, SEM à clauses types et Castors à apports de travail conservés ; 8° : coopératives de construction de 1378 sexies conservées. "
    "9°, 10° et 11° : établissements publics de recherche et d'enseignement supérieur, gestionnaires des pôles et réseaux mentionnés, communautés d'universités et établissements, fondations reconnues d'utilité publique de recherche et fondations de coopération scientifique restent exonérés pour les missions publiques définies par les codes de l'éducation et de la recherche. "
    "12° : bénéfices, plus-values latentes et profits de la transformation immobilière des houillères du Nord et du Pas-de-Calais conservent leur exonération pour les logements conventionnés à l'APL dans cette transformation ; pas de nouvelle répétition d'un événement historique. "
    "13° : formation professionnelle initiale et continue et recherche des établissements consulaires, ainsi que participation et financement par les organismes du premier alinéa du 1 bis de 206, restent couverts. "
    "14° a à d : société de L. 313-19, opérations SIEG y compris crédits désignés, catégories d'emploi des d à g de L. 313-3, opérations des c et d du 2° du I de L. 313-19-1 et financement du fonds de L. 811-1 : chaque branche demeure, sous conformité de fonctionnement. "
    "15° a et b : société de L. 313-20, subventions destinées aux participations désignées et quote-part de bénéfices SIEG de sociétés relevant de l'article 8 conservées. "
    "16° : exonération du produit de la majoration affectée à la société de transport désignée conservée ; la majoration du CIBS est un prélèvement distinct non supprimé ici. "
    "17° : ressources de missions de service public des CPTS au projet de santé validé et dans le cadre de la convention désignée restent exonérées ; validation sanitaire autonome conservée. "
    "1 bis : seule la fraction liée au nominal des certificats est exclue selon sa règle actuelle ; 1 ter : fraction proportionnelle aux droits des coopérateurs, seuil d'au moins 20 p. 100 et faculté de rémunération conservés ; 1 quater : seuil strictement supérieur à 50 %, rémunération possible et exception des organismes du 4° conservés ; définition des associés non coopérateurs du 1 quinquies et les deux calculs avant ristournes restent entiers. Ces limites ne sont pas des avantages supprimés mais le champ du régime, dont l'ambiguïté disjonctive source reste signalée. "
    "Les rubriques déjà abrogées ou sans objet n'ont pas d'avantage actif autonome à révoquer. Le nouveau 4 maintient toutes les exonérations pour les situations futures éligibles ; réserves déjà taxées et exonérations définitivement acquises sont protégées, sans double emploi des déficits, crédits ou dividendes entre sociétés. Aucun bénéfice n'est fermé par un nouveau délai de réinvestissement ni par une conservation en trésorerie. L'IS ordinaire demeure à la distribution sur les seules fractions non exonérées ; aucune suppression générale de cet impôt ne sert de prétexte à retirer les exonérations. Minimum international et fiscalité propre des associés restent distincts."
)

required = references['requirements'][source['code_id'] + '|' + source['source_id']]
assessments = {
    '206': (
        "Le 13° de 207 vise exactement le premier alinéa du 1 bis de 206 : organismes à gestion désintéressée, activités non lucratives significativement prépondérantes et recettes lucratives sous la limite indexée de 81 051 € de la source, pour leur participation ou financement des établissements consulaires. Ce n'est ni tout 206 ni une catégorie de salariés. Le 12 ajouté dans la proposition, absent de la source officielle, vise les fractions ordinaires des 1 à 4 et 6 à 10, maintient 207 et réserve tonnage, revenus patrimoniaux des 5/5 bis, 5 ter et minimum international. Le nouveau 4 de 207 reprend la même transition par exercices ouverts ; ni calcul des fractions ni renvoi à 206 ne rétablit l'IS annuel sur les bénéfices conservés. Les références syndicales du 1 bis qualifient les organismes et non leurs contrats de travail : aucune condition d'ancienneté, de notification de rupture ou d'ancien CDD n'est applicable à ce renvoi."
    ),
    '261': (
        "Le 5° bis de 207 renvoie au seul 1° du 7 de 261 : a services et ventes aux membres avec plafond de 10 % et exceptions, b œuvres sociales/philanthropiques et franchise indexée à 81 051 € dans cette rédaction, c six manifestations, d gestion désintéressée avec dérogations de rémunération, seuils de ressources et garanties. Il ne vise pas les 1° bis à 1° quater ni toutes les exonérations de TVA. La source intégrale et ses notes sont la seule vue fournie, sans proposition : abrogation différée au 1er janvier 2027, avec certains alinéas du d transitoirement maintenus. Le 5° bis proposé assure donc la continuité par le champ historique connu au 1er juillet 2026 et par les successeurs de ce même renvoi, pour les opérations futures aussi ; une concordance CIBS détaillée reste à documenter, sans cible inventée. Les âges, ressources et durée de rémunération de certains dirigeants relèvent de la gestion désintéressée : ils ne fixent ni durée de l'emploi, ni ancienneté d'indemnité, ni notification de rupture du contrat unique."
    ),
}
reference_checks = [
    dict(target_key=k, view_sha256=references['targets'][k]['view_sha256'],
         assessment=assessments[references['targets'][k]['number']])
    for k in required
]

answer = {
    **{k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']},
    'proposed_xml': proposed,
    'reason': reason,
    'review_notes': review_notes,
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Réquisition documentaire spéciale du 3° du 1 obligeant les coopératives agricoles et leurs unions à produire leur comptabilité et les justifications de conformité sur ce fondement, au-delà des contrôles de droit commun.",
        "Condition fiscale de programme élaboré par FranceAgriMer ou d'autorisation de cet établissement pour l'exonération des opérations entre coopératives de céréales du 3° du 1.",
        "Condition de concours des communes ou des départements pour l'exonération des bénéfices des manifestations associatives du 5° du 1, sans supprimer les critères non lucratifs, statutaires et d'intérêt économique.",
        "Portée d'imposition ordinaire annuelle de la fraction non exonérée du 4° et des résultats calculés aux 1 bis à 1 quater pour les exercices nouveaux : exigibilité coordonnée à la distribution, sans suppression de l'impôt dû à cette distribution.",
    ],
    'benefit_review': benefit_review,
    'reference_checks': reference_checks,
    'substantive_impact': {
        'version': 1,
        'classification': 'mixed',
        'assessment': (
            "Comparaison avec les 58 paragraphes officiels : une obligation spéciale de production documentaire est supprimée, deux conditions d'accès à des exonérations sont retirées, et la continuité de l'exonération fondée sur 261 est assurée. Les deux dernières coupes fiscales sont nouvelles par rapport au brouillon, qui avait déjà retiré la réquisition spéciale. Les conditions statutaires, anti-détournement et SIEG des autres exonérations restent utiles et sont maintenues. L'IS à la distribution est une coordination commune, pas une seconde réduction d'IS attribuable à 207. Le suivi temporel des fractions est nouvellement explicité dans la comptabilité existante : classement mixed et absence de solde net démontré."
        ),
        'scope_limitations': (
            "Aucun montant de baisse d'impôt ni coût de conformité n'est chiffré. Les opérations anciennes ne bénéficient pas rétroactivement des deux extensions ; les exercices ouverts avant la bascule gardent l'ancien IS, sous réserve de ces extensions sur leurs opérations futures. Régimes annuels distincts, minimum international et fiscalité des associés demeurent. Les contraintes européennes des aides sectorielles et la concordance complète de 261 avec le CIBS restent à coordonner. La filiation historique du 6° bis SRU n'est pas soldée par la présence de la piste documentaire, et la version suivante de 207 n'a pas été fournie. Aucun solde de l'ensemble des codes n'est établi."
        ),
        'new_burdens_review': (
            "Le 4 formalise l'identification dans le temps des bénéfices exonérés ou imposables dans la comptabilité existante, en lien avec les comptes et rapprochements du XI proposé de 209 ; cette charge doit être comptée même si elle protège les exonérations et l'absence de double IS. Elle ne remplace pas la réquisition supprimée par un dépôt équivalent. Aucun registre, état déclaratif, certificat, agrément, délai minimum de conservation en trésorerie ou obligation d'investissement supplémentaire propre à 207 n'est créé. Le renvoi historique de 261 conserve des conditions existantes plutôt qu'une nouvelle procédure. Coût de suivi et solde net des charges non établis ; aucune réduction globale de complexité ou économie nationale n'est affirmée."
        ),
        'effects': effects,
    },
}

Path('answer.json').write_text(json.dumps([answer], ensure_ascii=False, indent=2) + '\n')
print(json.dumps({
    'output_file': 'answer.json', 'article_count': 1,
    'source_paragraphs': len(original), 'proposed_paragraphs': len(paragraphs + new_paragraphs),
    'modified_source_positions': [i + 1 for i, (a, b) in enumerate(zip(original, paragraphs)) if a != b],
    'effects': len(effects), 'characters_proposed': len(proposed),
}, ensure_ascii=False))
