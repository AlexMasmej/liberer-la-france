import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []

def plain(xml):
    return ' '.join(html.unescape(re.sub(r'<[^>]*>', ' ', xml or '')).split())

def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)

def impact(classification, assessment, scope, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=scope, new_burdens_review=burdens, effects=effects or [])

def effect(kind, measure, description, before, after, unit, population, transition,
           source_quote, proposed_quote, replacement='Aucune formalité, taxe ou pièce de remplacement n’est créée.'):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)

def add(i, proposed, reason, notes, assessment, scope, burdens, effects=None,
        removed=None, benefit=None, classification=None, repeal=None):
    s = sources[i]
    a = {k:s[k] for k in ('code_id','source_id','source_sha256','number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    cls = classification or ('retained_necessary' if proposed is None else 'material_reduction')
    if proposed is None:
        a['classification'] = 'retained_necessary'
        assert not effects
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    if benefit:
        a['benefit_review'] = benefit
    a['substantive_impact'] = impact(cls, assessment, scope, burdens, effects)
    a['reference_checks'] = []
    answers.append(a)
    return a

# 0 — Affectation temporaire à l’habitation : droit direct, sans dépôt local.
p0 = """<p>Des locaux destinés à un usage autre que l'habitation peuvent être temporairement affectés à l'habitation pour une durée n'excédant pas quinze ans. Cette affectation est de droit, sans délibération locale instituant ce régime ni autorisation ou déclaration préalable au titre de la présente section.</p>
<p>(Abrogé).</p>
<p>Jusqu'à l'expiration du délai mentionné au premier alinéa, les locaux peuvent, par dérogation à l'article L. 631-7, retrouver leur usage antérieur, sans autorisation ni déclaration de retour au titre de la présente section.</p>
<p>En cas de location d'un local temporairement affecté à l'habitation en application du présent article, le contrat doit mentionner le caractère temporaire de cette affectation. Sous cette réserve, le retour des locaux à leur usage antérieur est un motif légitime et sérieux, au sens de l'article 15 de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986. Il ne constitue pas un événement au sens de l'article 11 de cette même loi.</p>
<p>Ces dispositions s'appliquent aux affectations nouvelles et à celles en cours à compter de l'entrée en vigueur de la loi. Pour les affectations en cours, le délai maximal de quinze ans reste calculé depuis leur commencement, sans remise à zéro. Les déclarations déjà déposées n'ont pas à être renouvelées ; les dépôts et instructions de déclaration d'affectation ou de retour en cours au seul titre de la présente section deviennent sans objet. Les contrats valablement conclus, les droits des occupants et des tiers et les créances antérieures sont préservés. Les règles d'urbanisme, de sécurité, de salubrité et de décence ainsi que les droits civils sur les locaux demeurent applicables.</p>"""
add(0, p0,
    "Réforme de fond : l'affectation temporaire à l'habitation devient directement accessible, sans création facultative d'un régime local ni déclaration préalable. Le retour à l'usage antérieur est expressément dispensé de formalité de changement d'usage. Le plafond de quinze ans, l'information contractuelle du locataire, le congé soumis à l'article 15 et l'exclusion de l'article 11 de la loi de 1989 sont maintenus, sans simple changement de vocabulaire.",
    "Les quatre positions initiales sont conservées ; le deuxième alinéa, devenu sans objet avec la disparition de la délibération, reste identifié comme abrogé. R631-6 et R631-7, lus intégralement dans le corpus, renvoient encore aux premier et deuxième alinéas d'un ancien L631-7-1 : incohérence préexistante à corriger par leur abrogation pour les déclarations futures de ce dispositif, sans rétablir leurs listes de pièces, plans, mandats ou attestation sur l'honneur. Ces règlements ne sont pas réécrits dans ce lot. Aucun délai de quinze ans n'est rouvert pour un local déjà temporairement affecté. Les lois civiles et les autorisations de travaux ne sont pas supprimées par la dispense propre à la présente section.",
    "La source entière conditionnait l'accès au mécanisme à une délibération instituant une déclaration. La proposition supprime ce circuit et sécurise le retour sans dépôt, tout en maintenant les garanties du bail temporaire.",
    "La dispense porte sur le changement d'usage de cette section, pas sur les autorisations de travaux ni sur la décence. Les règlements R631-6 et R631-7 restent à coordonner ; aucun effet budgétaire national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun registre, constat administratif, attestation ou dépôt ne remplace la déclaration. La mention du bail, les règles de sécurité et la durée maximale sont celles du régime conservé.",
    [effect('obligation_removed','habitation-temporaire-sans-declaration',
            "Suppression du circuit local de déclaration pour l'affectation temporaire et son retour.",
            "Accès subordonné à une délibération communale ou intercommunale instituant une déclaration ; affectation limitée à quinze ans.",
            "Accès de droit sans délibération, autorisation ni déclaration dans cette section ; retour également sans dépôt ; même maximum de quinze ans.",
            'legal_duty', "Titulaires du droit d'affecter temporairement des locaux non résidentiels à l'habitation et leurs locataires.",
            "Dès l'entrée en vigueur, y compris affectations en cours, sans recommencer les quinze ans ; droits locatifs et créances antérieures préservés.",
            "Une délibération du conseil municipal peut définir un régime de déclaration préalable permettant d'affecter temporairement à l'habitation des locaux destinés à un usage autre que l'habitation, pour une durée n'excédant pas quinze ans.",
            "Cette affectation est de droit, sans délibération locale instituant ce régime ni autorisation ou déclaration préalable au titre de la présente section.")],
    removed=["La délibération communale ou intercommunale conditionnant l'ouverture du régime d'affectation temporaire à l'habitation.",
             "La déclaration préalable d'affectation temporaire et toute déclaration de retour exigée au seul titre de cette section."],
    benefit="L'avantage est la faculté de loger temporairement dans des locaux non résidentiels puis de retrouver leur usage antérieur par dérogation à L631-7. Il demeure ouvert aux opérations futures, désormais de droit, avec le même maximum de quinze ans. Le motif légitime et sérieux de congé est conservé sous la réserve de la mention au bail ; il ne devient pas une fin automatique du bail ni l'événement de l'article 11. Aucun impôt ni avantage fiscal n'est retiré.")

# 1 — Un avis consultatif obligatoire est retiré ; le contrôle de la pénurie reste.
p1 = replace_once(sources[1]['source_xml'],
    "après avis, à Paris, Marseille et Lyon, du maire d'arrondissement concerné",
    "sans avis préalable obligatoire du maire d'arrondissement, y compris à Paris, Marseille et Lyon")
p1 += "<p>La dispense d'avis s'applique aux demandes déposées ou en cours d'instruction à compter de l'entrée en vigueur de la loi, sans nouveau dépôt ni reprise des délais déjà courus. Les autorisations régulièrement délivrées et les droits qui en résultent demeurent valables.</p>"
add(1, p1,
    "Réforme de fond ciblée : retrait de l'avis obligatoire du maire d'arrondissement, sans avis ou déclaration de remplacement. La décision du maire, la compensation éventuelle, le caractère personnel ou réel du titre, la publicité foncière et les critères tenant au marché et à la pénurie sont intégralement maintenus ; ils protègent le parc d'habitation sans être un quota communal SRU.",
    "La note de la loi 2008-776 sur la bascule du 1er janvier 2009 et sa réserve financière est historique, sans fixer l'entrée de cette réforme. L425-9 urbanisme, source et proposition lues dans le corpus, permet une décision commune sous accord de l'autorité sectorielle : sa réserve des avis légalement requis doit être entendue hors de l'avis ici supprimé ; la note antérieure qui maintenait cet avis est dépassée sur ce point. R631-6 et R631-7, lus, visent une ancienne numérotation de L631-7-1 et non ses alinéas actuels ; ne pas importer leurs déclarations dans cette autorisation. Aucune suppression de compensation ni de son inscription au fichier immobilier n'est opérée.",
    "Une consultation préalable obligatoire disparaît à Paris, Marseille et Lyon. L'autorisation de changement d'usage elle-même demeure, ainsi que ses effets sur les locaux de compensation ; aucune baisse de taxe n'est revendiquée.",
    "Le gain concerne seulement l'avis d'arrondissement. Il ne mesure pas le délai total d'instruction, ne supprime ni compensation ni autorisation communale et requiert l'actualisation de la coordination L425-9.",
    "Aucune charge nouvelle n'est identifiée : le maire conserve sa compétence et les informations du dossier ; aucun nouveau visa, délai ou circuit consultatif ne remplace l'avis retiré.",
    [effect('obligation_removed','changement-usage-avis-arrondissement',
            "Retrait de la consultation obligatoire du maire d'arrondissement.",
            "À Paris, Marseille et Lyon, avis préalable obligatoire du maire d'arrondissement avant la décision du maire communal.",
            "Décision du maire sans avis obligatoire d'arrondissement, à conditions de fond et compensation inchangées.",
            'legal_duty', "Communes de Paris, Marseille et Lyon et demandeurs d'une autorisation de changement d'usage.",
            "Demandes nouvelles ou en cours dès l'entrée en vigueur ; titres antérieurs préservés.",
            "après avis, à Paris, Marseille et Lyon, du maire d'arrondissement concerné",
            "sans avis préalable obligatoire du maire d'arrondissement, y compris à Paris, Marseille et Lyon")],
    removed=["La consultation préalable obligatoire du maire d'arrondissement à Paris, Marseille et Lyon pour cette autorisation de changement d'usage."])

# 2 — L’activité dans une partie de la résidence principale est de droit.
p2 = """<p>Par dérogation à l'article L. 631-7, dès lors qu'aucune stipulation contractuelle prévue dans le bail ou le règlement de copropriété ne s'y oppose, l'exercice d'une activité professionnelle, y compris commerciale, dans une partie d'un local d'habitation utilisé par l'intéressé comme sa résidence principale est de droit, sans autorisation du maire ni déclaration de remplacement, pourvu que cette activité n'engendre ni nuisance, ni danger pour le voisinage et qu'elle ne conduise à aucun désordre pour le bâti.<br /><br />Le bail d'habitation de cette résidence principale n'est pas soumis aux dispositions du chapitre V du titre IV du livre Ier du code de commerce et ne peut être un élément constitutif du fonds de commerce.</p>
<p>Ces dispositions s'appliquent aux activités nouvelles et en cours à compter de l'entrée en vigueur de la loi, lorsqu'elles remplissent les conditions du premier alinéa. Les demandes d'autorisation de changement d'usage portant sur ces activités et en cours d'instruction deviennent sans objet. Les contrats, les droits des tiers et les créances nés antérieurement demeurent préservés ; les pouvoirs de police et les recours relatifs aux nuisances, aux dangers et aux désordres pour le bâti restent applicables.</p>"""
add(2,p2,
    "Réforme de fond : suppression de l'autorisation municipale pour l'activité professionnelle exercée dans une partie de la résidence principale. Les conditions de respect du bail et de la copropriété, l'absence de nuisance, de danger et de désordre du bâti et l'exclusion du statut des baux commerciaux sont maintenues. Leur contrôle peut intervenir sans cet agrément préalable ; aucune déclaration ne le remplace.",
    "Le renvoi explicite à L631-7 est une dérogation de fond nouvelle : cible non incluse dans reference-targets.json pour cet article, mais source entière lue dans le corpus, y compris sa note sur 2027 qui ne fixe pas la date de la présente réforme. Coordonner le régime HLM de L631-7-5 dans ce lot ; les régimes déjà directs de L631-7-3 et L631-7-4 restent utiles et ne sont pas comptés comme de nouvelles suppressions. La note de 2008 conserve son seul objet historique. La dispense n'autorise pas l'occupation de tout le local à usage professionnel ni la méconnaissance des autres règles de sécurité ou d'urbanisme.",
    "La source exigeait une décision discrétionnaire du maire. La proposition la supprime effectivement pour une activité accessoire compatible avec l'habitation et garde les exigences protégeant voisins, occupants et immeuble.",
    "Le gain ne couvre que l'usage mixte décrit, dans la résidence principale, et ne supprime pas les règles professionnelles, les droits du bailleur ou les autorisations de travaux. Aucun délai global ni coût national n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : les critères de fond existaient et aucun dépôt, attestation, registre ou contrôle préalable de remplacement n'est créé.",
    [effect('authorization_removed','usage-mixte-sans-autorisation',
            "Suppression de l'autorisation municipale pour l'usage professionnel partiel de la résidence principale.",
            "Le maire pouvait autoriser l'activité accessoire, y compris commerciale, sous respect des contrats et absence de nuisance, danger ou désordre du bâti.",
            "Même activité de droit, sans autorisation ni déclaration, sous les mêmes conditions civiles et de protection.",
            'legal_duty', "Occupants exerçant une activité professionnelle dans une partie de leur résidence principale.",
            "Activités nouvelles et en cours dès l'entrée en vigueur ; demandes pendantes sans objet et droits antérieurs préservés.",
            "le maire peut autoriser, dans une partie d'un local d'habitation utilisé par le demandeur comme sa résidence principale, l'exercice d'une activité professionnelle, y compris commerciale",
            "est de droit, sans autorisation du maire ni déclaration de remplacement")],
    removed=["L'autorisation municipale préalable pour exercer une activité professionnelle dans une partie du logement constituant la résidence principale."])

add(3,None,
    "Maintien intégral nécessaire : ce texte ouvre déjà directement l'usage professionnel, y compris commercial, sans clientèle ni marchandises, aux occupants et aux représentants légaux de personnes morales. Il ne contient ni agrément ni déclaration à retirer. Les conditions d'occupation principale et de respect du bail et de la copropriété délimitent cette dispense favorable.",
    "La note de 2008 sur le 1er janvier 2009 est lue et reste historique. L631-7-2 proposé élargit la liberté d'usage mixte dans un autre champ ; il n'abolit pas cette dispense autonome sans clientèle ni marchandises. L631-7-5 conserve son application au parc HLM. Aucun renvoi au travail ni aucune durée d'emploi ne figurent ici.",
    "La source entière contient une permission légale existante, et non un circuit préalable. La conserver n'est ni une nouvelle suppression d'autorisation ni une réduction de prélèvement.",
    "Les restrictions contractuelles et la limitation aux occupants principaux subsistent ; l'effet économique des libertés d'usage déjà existantes n'est pas évalué dans ce lot.",
    "Aucune charge nouvelle n'est identifiée, puisque le corps officiel demeure intégralement applicable sans ajout de pièce, de registre ni de déclaration.")

add(4,None,
    "Maintien intégral de la permission directe d'usage professionnel en rez-de-chaussée et de l'exclusion du bail commercial. Les conditions relatives aux occupants principaux, aux stipulations civiles, aux nuisances, aux dangers et au bâti assurent la coexistence de l'activité et de l'habitation ; aucune autorisation ou formalité distincte n'est imposée par cet article.",
    "La note de création en 2008 et sa condition d'entrée au 1er janvier 2009 sont historiques. La dispense s'applique aux opérations futures admissibles. L631-7-5 est coordonné dans le lot pour étendre cette application de droit au parc HLM sans avis. L443-15-1-1, lu dans le corpus, traite la location de locaux pour des usages autres que l'habitation et demeure un dispositif distinct, avec sa dérogation expresse à cet article.",
    "Le régime de rez-de-chaussée est déjà une liberté légale. Le maintien de toutes ses conditions et de l'avantage locatif ne constitue aucune simplification nouvelle démontrée.",
    "L'article ne couvre que l'activité partielle des occupants de leur résidence principale ; les locations de locaux entiers pour activité économique restent distinctes. Aucun solde national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : le texte officiel est conservé en entier et ne reçoit ni demande, ni attestation, ni information de remplacement.")

p5 = """<p>I.-L'article L. 631-7-2 est applicable aux logements appartenant aux organismes mentionnés à l'article L. 411-2, y compris pour l'exercice d'une activité commerciale.<br /><br />L'article L. 631-7-3 est applicable aux logements appartenant à ces mêmes organismes.<br /><br />L'article L. 631-7-4 est applicable aux logements appartenant à ces mêmes organismes et situés au rez-de-chaussée, dans les conditions qu'il prévoit, sans autorisation préalable particulière à ces logements.<br /><br />II.-Aucun avis préalable du propriétaire du local n'est requis au titre du présent article. Les stipulations du bail et du règlement de copropriété demeurent opposables dans les conditions prévues aux articles mentionnés au I.</p>
<p>Ces dispositions s'appliquent aux activités nouvelles et en cours à compter de l'entrée en vigueur de la loi. Les demandes d'autorisation et les consultations du propriétaire en cours au seul titre du présent article deviennent sans objet, sans déclaration ou attestation de remplacement. Les contrats valablement conclus, les droits des occupants et des tiers et les créances antérieures sont préservés.</p>"""
add(5,p5,
    "Réforme de fond : alignement de l'usage mixte des logements HLM sur les permissions générales, avec ouverture de l'activité commerciale du premier alinéa, suppression de l'autorisation spéciale au rez-de-chaussée et de l'avis du propriétaire. Le délai d'un mois et son avis tacite favorable deviennent sans objet parce qu'aucun avis n'est requis, et non parce que l'avantage est fermé. Les conditions civiles et de sécurité des articles de rattachement restent applicables.",
    "Les trois alinéas du I et le II sont conservés dans leur position. L631-7-2 est réécrit dans ce lot ; L631-7-3 et L631-7-4 sont maintenus entiers. La suppression générale d'autorisation de L631-7-2 n'est pas comptée une seconde fois : l'effet propre est le retrait des exceptions et restrictions HLM. L443-15-1-1, lu en entier, reste autonome pour les locations de locaux entiers à usage non résidentiel et exclut déjà L631-7-5 dans son propre champ. La note d'entrée de 2008 n'est pas une date future. Aucun quota SRU ni nouvel agrément n'est substitué à l'avis retiré.",
    "La source traitait moins favorablement certains usages du parc HLM. La proposition retire cette surcouche et ouvre le commerce accessoire sous les conditions ordinaires, tout en gardant les garanties du bail et de la copropriété.",
    "Le gain propre est limité aux restrictions HLM ; il n'est pas additionné à la même autorisation générale supprimée à L631-7-2. Les règles des aides et des baux sociaux ne sont pas globalement supprimées.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration ni attestation ne remplace l'avis ou l'autorisation. Le respect des stipulations civiles demeure une condition existante de ces permissions.",
    [effect('relief_extended','usage-mixte-hlm-alignement',
            "Extension des libertés d'usage mixte au parc HLM par retrait de ses restrictions particulières.",
            "Commerce exclu du premier renvoi, autorisation spéciale au rez-de-chaussée et avis du propriétaire avec délai d'un mois.",
            "Application des trois permissions générales aux logements HLM, commerce accessoire inclus, sans autorisation spéciale ni avis du propriétaire.",
            'regime', "Occupants de logements appartenant aux organismes de L411-2 qui exercent une activité professionnelle accessoire.",
            "Activités nouvelles et en cours à l'entrée en vigueur, sous les conditions des articles de rattachement et sans réexamen des contrats valables.",
            "L'article L. 631-7-2 est applicable aux logements appartenant aux organismes mentionnés à l'article L. 411-2, sauf pour l'exercice d'une activité commerciale.",
            "L'article L. 631-7-2 est applicable aux logements appartenant aux organismes mentionnés à l'article L. 411-2, y compris pour l'exercice d'une activité commerciale.")],
    removed=["L'exclusion des activités commerciales du premier alinéa du I applicable aux logements des organismes de L411-2.",
             "L'autorisation spéciale des activités professionnelles en rez-de-chaussée dans les logements HLM, en dérogation à L631-7-4.",
             "L'avis préalable du propriétaire et l'attente d'un mois pour l'acquisition de son caractère réputé favorable."],
    benefit="Les trois voies favorables d'activité dans le logement HLM restent ouvertes aux situations futures. L'avis réputé favorable après un mois n'est pas remplacé par un refus possible : l'avis et son attente disparaissent entièrement. L'extension aux activités commerciales élargit la première voie et ne retire ni l'accès de L631-7-3, ni celui du rez-de-chaussée ; leurs conditions civiles et de protection subsistent.")

p6 = """<p>Lorsque le changement d'usage est soumis à autorisation et fait l'objet de travaux entrant dans le champ d'application du permis de construire, la demande de permis de construire ou la déclaration préalable vaut demande de changement d'usage.</p>
<p>Ces travaux ne peuvent être exécutés qu'après l'obtention de l'autorisation mentionnée à l'article L. 631-7, lorsqu'elle est requise. Le présent article ne rétablit aucune autorisation ni déclaration de changement d'usage pour les usages qui en sont dispensés par la présente section.</p>"""
add(6,p6,
    "Coordination nécessaire : la demande d'urbanisme vaut déjà demande de changement d'usage dans la source. La proposition conserve cette mutualisation et précise qu'elle n'impose pas d'autorisation aux usages désormais dispensés, notamment par L631-7-2 et L631-7-5. Aucun second allègement de dossier n'est revendiqué.",
    "L425-9 urbanisme, source et proposition lues, distingue l'existence de l'autorisation sectorielle de la possibilité future de décision commune après sa transition de six mois. Le présent article ne rend pas facultatif le bénéfice légal existant de la demande valant demande et ne supprime pas l'autorisation pour les changements qui y restent soumis. La mention source du permis de construire avec une alternative de déclaration préalable est conservée sans étendre silencieusement son champ. Les notes successives de 2005, 2007 et du report au 1er octobre 2007 restent historiques, sans reporter les nouvelles dispenses d'usage mixte.",
    "Le changement explicite seulement le champ résiduel de l'autorisation et prévient sa reconstitution par renvoi. Le dépôt mutualisé existait déjà dans la source entière : aucun gain supplémentaire de dépôt n'est compté.",
    "Coordination du seul régime d'usage mixte ; les autorisations de travaux et les autres changements d'usage conservent leur régime. La décision commune de L425-9 garde sa transition propre.",
    "Aucune charge nouvelle n'est identifiée : les demandes déjà communes le restent et les personnes dispensées ne produisent ni dossier de substitution ni attestation de dispense.",
    [effect('coordination','usage-mixte-sans-autorisation',
            "Limitation du renvoi à l'autorisation aux seuls changements qui y demeurent soumis.",
            "Interdiction d'exécuter les travaux avant l'autorisation de L631-7 formulée sans réserve expresse des dispenses.",
            "Même interdiction lorsqu'une autorisation reste requise, sans reconstitution de celle supprimée pour l'usage mixte.",
            'legal_duty', "Demandeurs de travaux comportant un changement d'usage et occupants bénéficiant d'une dispense.",
            "Application avec les dispenses de la présente section ; transition autonome de la décision commune conservée.",
            "Ces travaux ne peuvent être exécutés qu'après l'obtention de l'autorisation mentionnée à l'article L. 631-7.",
            "Le présent article ne rétablit aucune autorisation ni déclaration de changement d'usage pour les usages qui en sont dispensés par la présente section.")],
    classification='coordination_only')

add(7,None,
    "Maintien nécessaire après examen : la délibération motivée par des difficultés sérieuses d'accès au logement assure une adaptation territoriale du contrôle de changement d'usage. La possibilité de ne viser qu'une partie de la commune permet de limiter cette contrainte. Ce fondement n'est ni un quota SRU ni une formalité du demandeur à supprimer ; il reste soumis aux dispenses favorables de la section.",
    "L631-7, lu intégralement dans le corpus, délimite le premier groupe de communes ; sa version locale comporte une note d'application fiscale en 2027 dont la portée sur la chronologie de la section doit être vérifiée séparément, sans la transposer au présent article. Le renvoi reste de délimitation territoriale, non de taux fiscal. Les dispenses réécrites à L631-7-1 B, L631-7-2 et L631-7-5 s'appliquent sans nouvelle délibération de rétablissement. Aucune origine SRU de la norme actuelle n'est présumée.",
    "La source complète conserve un contrôle local motivé par une pénurie sérieuse et permet un champ infracommunal proportionné. Son maintien ne constitue pas une suppression d'autorisation et aucune réduction fiscale n'en résulte.",
    "La charge résiduelle de changement d'usage subsiste dans les communes l'ayant légalement instaurée, hors dispenses. L'inventaire des délibérations locales et leur impact économique ne sont pas disponibles.",
    "Aucune charge nouvelle n'est identifiée : aucun motif, document, transmission ou délai n'est ajouté au texte officiel maintenu intégralement.")

p8 = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi.</p>
<p>À compter de cette date, la délivrance d'une autorisation de changement d'usage en vue d'une mise en location de meublés de tourisme ne peut être subordonnée, sur le seul fondement du présent article, ni à la présentation d'un diagnostic de performance énergétique ni à l'appartenance du logement à une classe de performance énergétique. Cette règle s'applique aux demandes en cours, sans nouveau dépôt ni reprise des délais, et aux effets futurs des prescriptions fondées exclusivement sur le présent article, y compris pour les autorisations déjà délivrées.</p>
<p>Les autres obligations de diagnostic, d'information, de sécurité, de salubrité et de décence ayant un fondement autonome restent applicables. Les actes, droits et créances légalement constitués avant l'entrée en vigueur ainsi que les recours relatifs aux périodes antérieures demeurent régis par les dispositions antérieurement applicables, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives. Aucune restitution générale ni taxe de remplacement n'est instituée.</p>"""
add(8,p8,
    "Abrogation de fond : retrait du DPE et des classes A à E, puis A à D à compter de 2034, comme conditions propres à l'autorisation touristique. Ce filtre d'usage n'est pas une mesure de danger immédiat ; les obligations autonomes de diagnostic et les polices de sécurité, salubrité et décence ne sont pas abolies. La suppression s'applique aussi aux prescriptions futures fondées exclusivement sur cet article, sans maintenir indirectement le filtre par un ancien titre.",
    "L126-26 et L173-1-1, lus intégralement dans le corpus, définissent le diagnostic et les sept classes : ils ne sont pas abrogés, pas plus que leurs applications autonomes. L631-7-1 A a été lu en entier : l'autorisation temporaire, les dispenses de résidence principale et les autres règles touristiques conservent leur champ. L'abrogation ne s'étend pas hors de l'ancien champ métropolitain et ne crée aucune obligation outre-mer. Les obligations européennes autonomes de performance et de certification énergétique exigent leur propre confrontation ; leur suppression n'est pas affirmée par ce seul retrait du filtre national de changement d'usage. Aucun tableau maintenu n'est omis, la source assignée ne contenant que I et II.",
    "La condition spéciale de présentation du DPE et d'éligibilité énergétique disparaît entièrement pour l'autorisation touristique. Il s'agit d'une contrainte retirée, non d'une abrogation des DPE imposés par d'autres textes ni d'une baisse de taxe.",
    "Le gain vise le seul fondement de L631-10, dans son champ métropolitain. Les exigences énergétiques autonomes et les contraintes européennes restent à coordonner et aucune économie de travaux ou de recettes n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation, classe alternative, autorisation additionnelle ou déclaration ne remplace la condition abrogée. Les contrôles conservés ont une base autonome.",
    [effect('obligation_removed','tourisme-fin-condition-dpe-changement-usage',
            "Suppression du filtre DPE propre à l'autorisation de changement d'usage touristique.",
            "En métropole, présentation d'un DPE de classe A à E, puis A à D au 1er janvier 2034, pour l'autorisation touristique de L631-7 ou L631-7-1 A.",
            "Aucun DPE ni seuil de classe exigible sur ce fondement pour l'autorisation ; les diagnostics et normes d'autres fondements demeurent.",
            'legal_duty', "Propriétaires métropolitains sollicitant une autorisation de changement d'usage en meublé de tourisme.",
            "Dès l'entrée de la loi, demandes pendantes et prescriptions futures de titres anciens incluses ; périodes antérieures réservées et loi répressive plus douce applicable dans son champ.",
            "les propriétaires des locaux concernés présentent un diagnostic de performance énergétique mentionné à l'article L. 126-26 du présent code, dont le niveau, au sens de l'article L. 173-1-1, doit être compris entre les classes A et E ou, à compter du 1er janvier 2034, entre les classes A et D.",
            "la délivrance d'une autorisation de changement d'usage en vue d'une mise en location de meublés de tourisme ne peut être subordonnée, sur le seul fondement du présent article, ni à la présentation d'un diagnostic de performance énergétique ni à l'appartenance du logement à une classe de performance énergétique.")],
    repeal="Suppression pour l'avenir des conditions de diagnostic et de classement énergétique propres à l'autorisation touristique de changement d'usage en France métropolitaine, sans suppression de leurs fondements autonomes.")

# 9 — Fusion des deux agréments, sans perte des conditions sociales ou de sécurité.
p9 = replace_once(sources[9]['source_xml'],
    "L'exploitant d'une résidence hôtelière à vocation sociale est agréé par le représentant de l'Etat dans le département dans lequel la résidence est implantée.",
    "L'agrément de la résidence porte également sur son exploitant lorsque celui-ci est désigné dans la demande ; la résidence et son exploitant font alors l'objet d'une seule demande et d'une décision unique, sans agrément distinct de l'exploitant. La résidence peut être agréée avant la désignation de l'exploitant ; celui-ci fait alors l'objet d'un examen complémentaire portant sur ses seules conditions propres, sans nouvel agrément de la résidence.")
p9 = replace_once(p9,
    "les modalités relatives à l'agrément respectif des résidences et de leurs exploitants",
    "les modalités relatives à l'agrément unique des résidences et de leurs exploitants, en conservant les conditions de fond propres à chacun, sans double dépôt des pièces communes,")
p9 += """<p>La réunion des agréments n'ajoute aucune condition de fond à celles applicables à la résidence et à l'exploitant. Le renouvellement de la composante relative à l'exploitant ne soumet pas l'agrément de la résidence à un renouvellement. En cas de changement d'exploitant, seules les conditions propres au nouvel exploitant sont examinées, sans nouvel agrément de la résidence, sous réserve des contrôles légalement applicables et des modifications apportées à celle-ci.</p>
<p>Ces dispositions s'appliquent aux demandes déposées à compter de l'entrée en vigueur de la loi. Les demandes en cours sont réunies lorsqu'elles concernent la même résidence et son exploitant, sans nouveau dépôt des pièces déjà produites ni reprise des délais déjà courus. Les agréments en cours de validité sont reconnus comme les composantes d'un même agrément, sans nouvelle demande et sans réduction de leur durée, de leur champ ou de leurs effets. Les dérogations techniques, droits de réservation, aides, conventions, créances et droits des occupants valablement constitués sont préservés.</p>"""
add(9,p9,
    "Réforme de fond procédurale : fusion des agréments de la résidence et de l'exploitant dans une demande et une décision uniques lorsque l'exploitant est désigné. La faculté de faire agréer la résidence avant de choisir l'exploitant est conservée, pour ne pas créer d'attente ou condition de financement supplémentaire. Les critères propres à chacun restent distincts sur le fond ; la résidence n'est pas soumise au renouvellement de la composante exploitant. Le contingent d'au moins 30 %, l'engagement de plus de 80 %, les catégories de personnes, l'accompagnement social, la restauration ou les cuisines, le service d'intérêt général, la destination d'urbanisme et l'exemption d'autorisation commerciale restent intégralement maintenus.",
    "R631-8-1 à R631-15 et R631-17 à R631-26 ont été lus dans leurs textes et notes disponibles. Coordonner précisément les demandes et décisions R631-9/10/11 et R631-12/14/15, les changements d'exploitant R631-13/17 et le cahier des charges R631-18, sans retirer les garanties de qualification, les interdictions L241-3/4, le certificat technique indépendant ni le contrôle des fonds. Le terme de neuf ans et son renouvellement tacite, actuellement propres à l'exploitant dans R631-12, ne doivent pas être étendus à la résidence. Les dérogations R631-21 et R631-18 demeurent accessibles aux situations futures, comme les tarifs et droits de réservation R631-22 à R631-26. Les 30 % et plus de 80 % relèvent de cette qualification sociale et de ses financements, non des quotas communaux SRU abrogés. La note du 1er mai 2021 reste historique. Aucun chiffrage de réduction de délais ou d'aide publique n'est avancé.",
    "La source entière imposait deux agréments distincts. La proposition retire leur séparation procédurale lorsque l'exploitant est connu et le double dépôt des pièces communes, en maintenant les deux contrôles de fond dans un acte. Elle conserve l'agrément anticipé de la résidence si l'exploitant n'est pas encore choisi.",
    "Le gain ne porte que sur le circuit des agréments de la même résidence et de son exploitant. Les règlements de dossier et de décision doivent être coordonnés ; les coûts publics et privés nets ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : une demande et un acte remplacent les deux circuits lorsque l'exploitant est connu, sans pièce supplémentaire ni désignation anticipée obligatoire. Les conditions de qualification, de sécurité, d'accueil et de financement restent celles du régime existant.",
    [effect('obligation_merged','residence-hoteliere-agrement-unique',
            "Fusion des agréments de la résidence et de son exploitant dans un seul circuit.",
            "Agrément de l'établissement et agrément distinct de l'exploitant, délivrés par le même représentant de l'État dans le département.",
            "Une seule demande et une décision unique si l'exploitant est désigné, conditions propres conservées et pièces communes déposées une fois ; agrément anticipé de la résidence toujours possible.",
            'legal_duty', "Propriétaires, maîtres d'ouvrage et exploitants de résidences hôtelières à vocation sociale.",
            "Demandes nouvelles et réunion des demandes pendantes sans reprise des délais ; agréments valides, dérogations et droits des occupants préservés.",
            "L'exploitant d'une résidence hôtelière à vocation sociale est agréé par le représentant de l'Etat dans le département dans lequel la résidence est implantée.",
            "la résidence et son exploitant font alors l'objet d'une seule demande et d'une décision unique, sans agrément distinct de l'exploitant.",
            "Maintien des contrôles de fond dans une décision commune ; aucun nouveau registre, déclaration ou renouvellement de la résidence.")],
    removed=["La demande et la décision d'agrément obligatoirement distinctes pour l'exploitant de la même résidence hôtelière à vocation sociale lorsqu'il est désigné avec la demande de la résidence.",
             "Le double dépôt des pièces communes dans les circuits d'agrément de la résidence et de son exploitant."])

# 10 — Universités : retrait de deux autorisations spéciales, avantages conservés.
p10 = replace_once(sources[10]['source_xml'],
    "Ces résidences peuvent faire l'objet d'une convention conclue en application de l'article L. 831-1 lorsqu'elles bénéficient d'une autorisation spécifique délivrée par le représentant de l'Etat dans le département. Les modalités d'octroi de cette autorisation spécifique sont définies par décret..",
    "Ces résidences peuvent faire l'objet d'une convention conclue en application de l'article L. 831-1 sans autorisation spécifique au titre du présent article.")
p10 = replace_once(p10,
    "d'une convention conclue en application de l'article L. 351-2 peuvent, après agrément du projet de l'organisme",
    "d'une convention relevant des dispositions alors codifiées à l'article L. 351-2, dont les règles relatives au conventionnement sont désormais reprises à l'article L. 831-1, peuvent, sans agrément supplémentaire du projet de l'organisme")
p10 += """<p>L'accueil des personnes en contrat de professionnalisation ou d'apprentissage reste ouvert lorsque la formation correspondante s'inscrit dans le contrat de travail unique à durée indéterminée. La durée de la formation et celle du bail ne déterminent pas la durée de l'emploi. Les contrats de travail antérieurs à l'entrée en vigueur de la loi instituant ce contrat unique et les droits qui s'y attachent restent régis par leurs dispositions transitoires.</p>
<p>Les dispenses d'autorisation spécifique et d'agrément supplémentaire s'appliquent aux demandes nouvelles et aux procédures en cours à compter de l'entrée en vigueur de la loi, sans formalité de remplacement ni nouvelle production des pièces déjà versées. Les décisions de financement et les conventions restent soumises à leurs conditions propres. Les conventions, autorisations et agréments déjà valables, les baux en cours et les droits et créances antérieurs sont préservés.</p>"""
add(10,p10,
    "Réforme de fond : suppression de l'autorisation spécifique préalable au conventionnement et de l'agrément supplémentaire de conversion des immeubles conventionnés à la date historique fixée par le dernier alinéa. La convention et ses conditions financières demeurent. Le public bénéficiaire, l'accueil exceptionnel des enseignants et chercheurs, le bail maximal d'un an renouvelable, l'absence de maintien, l'interdiction de cession et de sous-location, la dispense de L441-2 et l'absence de nouveau concours d'État sont conservés. Coordination explicite de l'accès des apprentis et personnes en professionnalisation dans le contrat unique.",
    "L831-1, L831-2, L353-1 et L821-2 ont été lus dans le corpus : le renvoi pertinent pour une convention locative est L831-1, non une juxtaposition des quatre articles de la note de 2019. La situation à la publication de la loi 2017-86 reste décrite sous son ancien fondement L351-2 ; aucune convention postérieure n'est réputée exister en 2017. Ce renvoi historique n'est pas une réouverture des aides à l'accession fermées par L831-2. D331-6, lu en entier, intègre déjà l'autorisation spécifique à la décision de financement : son cinquième alinéa et la liste de pièces du sixième sont à coordonner sans compter un second dossier supprimé pour les opérations qui avaient déjà ce dépôt intégré. Les décisions de financement et les autres autorisations de L441-2 ne disparaissent pas. D331-4, lu, conserve l'exception favorable de location meublée pour L631-12. Les renvois des délégations L301-5-1/2 à l'autorisation supprimée appellent coordination, sans suppression des compétences d'aide. Les cibles nouvelles L831-1 et historiques L351-2 ne sont pas de nouvelles cibles du fichier contractuel ; leur objet et la recodification sont explicités ici.",
    "Deux conditions administratives spéciales sont retirées de la source complète, sans suppression de convention, d'aide ou de contrôle des financements. L'accès dans le contrat unique est une coordination de bénéficiaires, pas une nouvelle réduction du coût du travail.",
    "Aucun second dossier n'est prétendu supprimé lorsque D331-6 l'intégrait déjà au financement. Les règlements et délégations restent à coordonner ; la durée d'un an concerne le bail et non l'emploi.",
    "Aucune charge nouvelle n'est identifiée : les dispenses ne sont assorties d'aucune déclaration ni attestation. Les critères de public, les conditions des conventions et les décisions de financement demeurent ; aucun justificatif d'ancienneté salariale n'est ajouté.",
    [effect('authorization_removed','residence-universitaire-fin-autorisations-speciales',
            "Suppression des autorisations spéciales de conventionnement et d'accès au statut universitaire.",
            "Autorisation spécifique préfectorale pour conventionner ; agrément du projet pour les immeubles déjà conventionnés au jour de publication de la loi du 27 janvier 2017.",
            "Conventionnement sans autorisation spécifique et bénéfice du régime historique sans agrément supplémentaire, sous les autres conditions inchangées.",
            'legal_duty', "Gestionnaires de résidences universitaires et organismes des immeubles relevant du dernier alinéa historique.",
            "Dispenses pour demandes nouvelles et en cours ; conventions, financements, baux et créances antérieurs préservés.",
            "lorsqu'elles bénéficient d'une autorisation spécifique délivrée par le représentant de l'Etat dans le département.",
            "Ces résidences peuvent faire l'objet d'une convention conclue en application de l'article L. 831-1 sans autorisation spécifique au titre du présent article."),
     effect('coordination','contrat-unique-duree-indeterminee',
            "Maintien de l'accès au logement pour apprentissage et professionnalisation dans le contrat unique.",
            "Accueil des personnes titulaires d'un contrat de professionnalisation ou d'apprentissage, sans qualification expresse du futur contrat unique.",
            "Même accès lorsque cette formation s'inscrit dans le contrat unique ; durée du bail et durée de l'emploi distinctes.",
            'regime', "Personnes en apprentissage ou professionnalisation accueillies en résidence universitaire.",
            "Futurs contrats uniques couverts ; anciens contrats et leurs droits conservés dans leur transition propre.",
            "Cet établissement accueille des étudiants, des personnes de moins de trente ans en formation ou en stage et des personnes titulaires d'un contrat de professionnalisation ou d'apprentissage.",
            "L'accueil des personnes en contrat de professionnalisation ou d'apprentissage reste ouvert lorsque la formation correspondante s'inscrit dans le contrat de travail unique à durée indéterminée.")],
    removed=["L'autorisation spécifique préfectorale conditionnant la possibilité de conventionner la résidence universitaire au titre de L831-1.",
             "L'agrément supplémentaire du projet de l'organisme pour accéder au régime à partir des immeubles déjà conventionnés à la date historique conservée."])

# 11 — Pas d’attente jusqu’au 31 décembre pour des locaux déjà vacants.
p11 = """<p>Par dérogation à l'article L. 631-12, le gestionnaire d'une résidence universitaire qui n'est pas totalement occupée peut, à tout moment de l'année, louer les locaux inoccupés pour des séjours d'une durée inférieure à trois mois s'achevant au plus tard le 1er octobre qui suit leur date de prise d'effet, particulièrement à des publics reconnus prioritaires par l'Etat au sens de l'article L. 441-1.<br /><br />Lorsque les logements loués en application du premier alinéa du présent article sont libérés, ils sont proposés en priorité aux personnes mentionnées au premier alinéa de l'article L. 631-12.</p>
<p>La suppression de l'attente du 31 décembre s'applique aux locations conclues à compter de l'entrée en vigueur de la loi. Les locations déjà conclues et leurs échéances restent valables ; la présente disposition ne les prolonge ni ne les raccourcit automatiquement.</p>"""
add(11,p11,
    "Réforme de fond : retrait de l'attente calendaire du 31 décembre avant de louer temporairement les logements inoccupés. L'avantage de location dérogatoire reste ouvert aux futures situations, pour moins de trois mois, avec fin au prochain 1er octobre et priorité de retour aux publics universitaires. Ce n'est pas une réécriture stylistique ni une réduction du préavis d'emploi.",
    "L631-12 est examiné intégralement dans ce lot : la priorité du deuxième alinéa vise exclusivement les personnes de son premier alinéa, non les règles du bail annuel. Le rattachement ancien au 31 décembre de chaque année est remplacé par le prochain 1er octobre suivant la prise d'effet du séjour ; le plafond de moins de trois mois et la disponibilité pour la rentrée restent explicites. L441-1 désigne les publics prioritaires du logement, pas une condition d'ancienneté au travail. Aucun nouveau constat, dossier de vacance ou justificatif salarial n'est institué. Les autres règles des conventions de financement ne sont pas abolies.",
    "La proposition autorise l'occupation temporaire des locaux vacants sans attendre la date imposée par la source. Elle conserve l'usage universitaire prioritaire à la libération et n'affaiblit pas les contrats déjà conclus.",
    "Le gain porte sur l'ouverture calendaire, non sur une augmentation du plafond de séjour ni sur un droit de maintien permanent. Les recettes locatives supplémentaires et l'incidence sur les aides ne sont pas chiffrées.",
    "Aucune charge nouvelle n'est identifiée : la vacance reste une condition matérielle existante, sans nouveau registre ou attestation ; les locations restent brèves et les priorités de retour demeurent.",
    [effect('obligation_removed','residence-universitaire-location-vacance-sans-attente',
            "Suppression de l'attente du 31 décembre avant la location temporaire des logements universitaires vacants.",
            "Dérogation ouverte lorsque la résidence n'est pas totalement occupée après le 31 décembre de chaque année, séjours inférieurs à trois mois et fin au 1er octobre de l'année suivante.",
            "Dérogation ouverte à tout moment de l'année pour les locaux inoccupés, séjours toujours inférieurs à trois mois et fin au prochain 1er octobre après leur début.",
            'legal_duty', "Gestionnaires de résidences universitaires et occupants temporaires, notamment publics prioritaires de L441-1.",
            "Locations conclues après l'entrée en vigueur ; locations anciennes et priorité universitaire à la libération préservées.",
            "le gestionnaire d'une résidence universitaire qui n'est pas totalement occupée après le 31 décembre de chaque année peut louer les locaux inoccupés",
            "le gestionnaire d'une résidence universitaire qui n'est pas totalement occupée peut, à tout moment de l'année, louer les locaux inoccupés")],
    removed=["L'attente obligatoire du 31 décembre de chaque année pour ouvrir la faculté de louer les locaux inoccupés de la résidence universitaire."],
    benefit="L'avantage est la faculté dérogatoire de louer les logements universitaires vacants à d'autres publics, particulièrement prioritaires. Il est élargi aux vacances constatées à tout moment de l'année, sans formalité supplémentaire. La durée inférieure à trois mois, le retour disponible au prochain 1er octobre et la priorité universitaire à la libération demeurent ; les nouvelles formations sous contrat unique restent dans le public de L631-12. Les locations anciennes ne sont pas raccourcies par la réforme.")

add(12,None,
    "Maintien intégral nécessaire : la distinction entre services non individualisables et services souscrits individuellement évite une facturation indistincte ; la souscription de ces derniers reste une faculté. Le préavis plafonné à un mois protège l'occupant lors de la résiliation d'un service. Il ne s'agit ni du contrat de travail ni d'un minimum légal d'attente à réduire à quinze jours.",
    "Les cibles L1234-1, L1221-2 et L1234-9 ont été lues dans leurs sources et propositions : aucune n'est appelée par ce contrat de services au résident. Le décret de catégories et l'avis de la Commission nationale de concertation délimitent une facturation collective opposable ; leur fonction d'information et de protection justifie ce maintien, sans compter comme nouvelle simplification l'option de service déjà offerte. L631-15 conserve le détail de quittance et le paiement mensuel à la demande.",
    "Le texte officiel contient déjà un choix de souscription et un plafond favorable de préavis de service. Aucune obligation redondante démontrée n'est retirée ; maintien intégral sans effet nouveau compté.",
    "Le mois concerne la résiliation des services individualisables, pas l'emploi ni le bail. Les tarifs concrets et les prestations réglementaires ne sont pas évalués financièrement.",
    "Aucune charge nouvelle n'est identifiée : le texte officiel reste entier, sans nouvelle catégorie de données, pièce, registre ni condition de résiliation.")

p13 = replace_once(sources[13]['source_xml'],
    "qui est cosigné par le gérant de la résidence et adressé à tous les résidents",
    "qui est adressé à tous les résidents sans cosignature obligatoire du gérant de la résidence")
p13 += "<p>La dispense de cosignature s'applique aux comptes rendus établis à compter de l'entrée en vigueur de la loi. Les comptes rendus déjà établis restent valables et ne sont pas refaits.</p>"
add(13,p13,
    "Réforme de fond limitée : suppression de la cosignature obligatoire du gérant sur le compte rendu rédigé par le secrétaire. Le droit de discussion des résidents, la réunion annuelle, l'information comptable, la désignation d'un secrétaire, l'envoi à tous les résidents et la remise des comptes rendus des trois années précédentes aux candidats locataires demeurent intégralement, car ils protègent leur consentement et le contrôle des services facturés.",
    "L631-16, maintenu, réserve ce régime au gérant également bailleur et évite le doublon du conseil de copropriété ; aucune seconde instance n'est créée. Les trois années de comptes rendus et le minimum d'une réunion annuelle restent inchangés. La suppression ne donne pas au gérant un visa de remplacement ni un pouvoir de bloquer l'envoi. Elle ne dispense pas le secrétaire de rédiger fidèlement le compte rendu ni le gérant de fournir les données sur les services.",
    "Une formalité de cosignature disparaît dans la source complète. Les autres tâches d'information restent nécessaires aux résidents et sont conservées ; le gain est limité à cette signature, sans suppression fictive du conseil.",
    "Ni la périodicité annuelle ni la remise de trois années de comptes rendus ne sont supprimées. Le temps effectivement économisé et les coûts globaux des résidences ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : le même secrétaire rédige et le même compte rendu est envoyé ; aucune attestation, validation ou signature supplémentaire ne remplace celle du gérant.",
    [effect('obligation_removed','residences-services-compte-rendu-sans-cosignature',
            "Suppression de la cosignature du gérant sur le compte rendu du conseil des résidents.",
            "Compte rendu rédigé par le secrétaire, cosigné obligatoirement par le gérant et envoyé aux résidents.",
            "Même compte rendu rédigé et envoyé sans cosignature obligatoire du gérant.",
            'legal_duty', "Secrétaires des conseils de résidents et gérants bailleurs des résidences-services relevant de L631-16.",
            "Comptes rendus établis après l'entrée en vigueur ; comptes rendus antérieurs valables sans réfection.",
            "qui est cosigné par le gérant de la résidence et adressé à tous les résidents",
            "qui est adressé à tous les résidents sans cosignature obligatoire du gérant de la résidence")],
    removed=["La cosignature obligatoire par le gérant de la résidence du compte rendu établi par le secrétaire du conseil des résidents."])

add(14,None,
    "Maintien intégral nécessaire : les services dus et payés sont convenus au bail, le paiement mensuel est un droit du locataire et la quittance sépare loyer, charges et services. La clause résolutoire reste facultative et soumise aux garanties de l'article 24 de la loi de 1989. Ces mentions permettent un consentement éclairé et ne constituent pas des justificatifs administratifs redondants.",
    "Le 4° demeure abrogé, sans renumérotation. La note de la loi 2015-1776 conserve le champ des contrats conclus à compter du 30 décembre 2015 ; aucune rétroactivité nouvelle n'est opérée. Le renvoi à L631-13 vise les services non individualisables et non le préavis des services individualisables. Les dispositions du travail sur quinze jours, l'ancienneté d'un an et l'indemnité de rupture sont sans application à ces dettes locatives. Les modalités judiciaires de l'article 24 de la loi de 1989, extérieur aux cinq codes, ne sont ni remplacées ni réputées réécrites.",
    "La source entière organise la transparence de la dette et protège le paiement mensuel à la demande. Elle ne fait pas double emploi avec une autorisation ou une déclaration retirée ; son maintien n'est pas compté comme un allègement nouveau.",
    "Les obligations de contrat et de quittance demeurent pour les baux de son champ historique. Aucun effet sur les loyers, les impayés ou les frais judiciaires n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée, puisque toutes les mentions et garanties restent celles de la source, sans nouveau document, registre ou délai imposé.")

add(15,None,
    "Maintien nécessaire de la règle de champ : les articles L631-14 et L631-15 s'appliquent au gérant qui est également bailleur, et le conseil des résidents de la loi sur la copropriété n'est alors pas applicable. Cette exclusion évite déjà un doublon institutionnel. La retirer ou la reformuler ne créerait aucun allègement supplémentaire démontré.",
    "L631-14 est allégé dans ce lot pour la seule cosignature ; le renvoi au même article reste exact sans changement de numéro ni nouvelle formalité. L631-15 conserve les droits contractuels, les services et la quittance. L'article 41-7 de la loi 65-557 est une règle extérieure de conseil des résidents, pas une règle de rupture d'emploi ; son exclusion limitée reste utile, sans prétendre réécrire cette loi.",
    "Le texte source écarte déjà l'application simultanée de deux régimes de conseil dans son champ. Ce bénéfice demeure intégralement sans nouvelle fusion à compter.",
    "Les autres situations de copropriété restent régies par la loi de 1965 ; ce lot ne mesure pas leurs coûts de gouvernance et ne les supprime pas.",
    "Aucune charge nouvelle n'est identifiée : le renvoi et l'exclusion existants sont conservés, sans instance, document ni transmission supplémentaires.")

# 16 — Bail de mobilité, sans semaine minimale et sans terme de l’emploi.
p16 = re.sub(r' align="left"', '', sources[16]['source_xml'])
p16 = replace_once(p16, "pour une durée d'une semaine à dix-huit mois", "pour une durée n'excédant pas dix-huit mois")
p16 = replace_once(p16,
    "le bail conclu avec le locataire est un bail mobilité régi par le titre I<sup>er</sup> ter de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986.",
    "le bail conclu avec le locataire est un bail mobilité régi par le titre I<sup>er</sup> ter de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986. Les dispositions de ce titre fixant une durée minimale au bail ne sont pas applicables à ces locations.")
p16 += """<p>Les situations d'apprentissage, de formation ou de mission temporaire mentionnées au premier alinéa ouvrent droit au présent régime lorsqu'elles s'inscrivent dans un contrat de travail unique à durée indéterminée. La durée de la formation, de la mission, du bail ou de la sous-location ne fixe aucun terme au contrat de travail. Les contrats de travail antérieurs à l'entrée en vigueur de la loi instituant ce contrat unique et les droits qui s'y attachent demeurent régis par leurs dispositions transitoires.</p>
<p>La suppression de la durée minimale d'une semaine s'applique aux baux conclus à compter de l'entrée en vigueur de la loi et, avec l'accord des parties, aux baux en cours. Elle ne raccourcit pas automatiquement un bail existant. Les conditions de ressources, les plafonds de loyers, les conventions, les aides et les droits et créances antérieurement constitués sont préservés.</p>"""
add(16,p16,
    "Réforme de fond : suppression du minimum d'une semaine du bail en résidence à vocation d'emploi, en conservant son maximum de dix-huit mois et le régime du bail mobilité sous ses dispositions propres. Coordination nécessaire : une phase de formation, d'apprentissage ou de mission temporaire reste éligible dans le contrat unique sans déterminer la durée de l'emploi. Le quota propre de 80 % de logements sous plafonds de ressources et de loyers protège cet accès abordable et n'est pas le quota communal SRU ; il demeure avec les neuf alinéas initiaux et leurs deux numéros.",
    "Les attributs de présentation align ont seuls été retirés hors des changements explicités. Le renvoi à la loi 89-462, titre Ier ter, demeure subordonné aux dispositions propres de la résidence, dont le maximum de dix-huit mois : cette dérogation existait déjà et n'est pas étendue à tous les baux mobilité. L'exclusion expresse de toute durée minimale issue de ce titre évite que le renvoi rétablisse un plancher après la suppression de la semaine ; elle coordonne la même mesure et n'est pas une seconde baisse. Le service civique du II de L120-1 du code du service national reste une situation distincte, pas un contrat privé converti artificiellement. Les études, stages, mutations et possibilité de sous-location par personnes morales demeurent. L632-3 et L633-5, ce dernier lu dans le corpus, conservent leurs exclusions de champ. Les décrets de prix et de facturation appellent coordination du seul minimum supprimé, sans nouvelle pièce ni agrément. Les règles législatives de rupture d'emploi, notamment notification et ancienneté, ne sont pas des conditions du bail.",
    "Le minimum d'une semaine est effectivement retiré pour les nouveaux baux, sans baisse de plafond de ressources ou de protection locative. L'éligibilité des personnes sous contrat unique est coordonnée séparément et ne constitue pas une nouvelle suppression de charge salariale.",
    "Le bail conserve un maximum de dix-huit mois et son champ de mobilité. Les garanties tarifaires de 80 % demeurent ; aucun coût de nuitée ni solde public national n'est calculé.",
    "Aucune charge nouvelle n'est identifiée : ni ancienneté d'emploi, ni notification de rupture, ni registre supplémentaire ne conditionnent l'accès. L'accord des parties empêche seulement que l'allègement raccourcisse un bail existant contre leur volonté.",
    [effect('obligation_removed','residence-emploi-fin-duree-minimale-bail',
            "Suppression de la durée minimale d'une semaine du bail en résidence à vocation d'emploi.",
            "Bail d'une semaine au moins, soit sept jours calendaires, et de dix-huit mois au plus pour les locataires éligibles.",
            "Aucun minimum d'une semaine au titre de cet article ; maximum de dix-huit mois et autres protections conservés.",
            'calendar_days', "Locataires et bailleurs des résidences à vocation d'emploi répondant aux conditions du premier alinéa.",
            "Nouveaux baux dès l'entrée en vigueur et baux en cours avec accord des parties ; pas de raccourcissement automatique.",
            "loués pour une durée d'une semaine à dix-huit mois",
            "loués pour une durée n'excédant pas dix-huit mois"),
     effect('coordination','contrat-unique-duree-indeterminee',
            "Maintien de l'accès au bail de mobilité pour les formations et missions dans le contrat unique.",
            "Éligibilité liée notamment à l'apprentissage, à la formation et à la mission temporaire ; aucune règle de rupture d'emploi dans l'article.",
            "Même éligibilité dans un contrat unique indéterminé ; terme du bail ou de la mission sans effet automatique sur l'emploi.",
            'regime', "Apprentis et personnes en formation ou mission temporaire relevant de cette résidence.",
            "Futurs contrats uniques inclus ; anciens contrats et droits antérieurs conservés selon leur transition.",
            "en cours de mutation professionnelle ou en mission temporaire dans le cadre de leur activité professionnelle.",
            "La durée de la formation, de la mission, du bail ou de la sous-location ne fixe aucun terme au contrat de travail.")],
    removed=["La durée minimale légale d'une semaine imposée à la location d'un logement en résidence à vocation d'emploi."])

p17 = replace_once(sources[17]['source_xml'],
    "elle informe préalablement le bailleur de son intention de sous-louer une partie de son logement à une personne de moins de trente ans dans le cadre d'un contrat de cohabitation intergénérationnelle solidaire, sans que le bailleur puisse s'y opposer.",
    "elle peut sous-louer une partie de son logement à une personne de moins de trente ans dans le cadre d'un contrat de cohabitation intergénérationnelle solidaire, sans information préalable du bailleur et sans que celui-ci puisse s'y opposer.")
p17 += """<p>La dispense d'information préalable s'applique aux contrats nouveaux et aux contrats en cours à compter de l'entrée en vigueur de la loi, sans déclaration, attestation ou autorisation de remplacement. Aucune information de régularisation n'est exigée sur ce seul fondement après cette date. Les droits et créances antérieurement constitués et les recours relatifs aux périodes antérieures sont préservés.</p>"""
add(17,p17,
    "Réforme de fond : suppression de l'information préalable du bailleur, qui ne disposait déjà d'aucun droit d'opposition. La sous-location solidaire reste ouverte aux personnes futures éligibles, sans formalité de remplacement. Les seuils de soixante ans et de moins de trente ans, la contrepartie modeste, la liberté de durée et de prix, le préavis civil d'un mois, le code civil, l'exclusion de la loi de 1989 et la charte sont entièrement conservés.",
    "L631-18, maintenu, exclut le lien de subordination et le code du travail ; le préavis d'un mois ne devient pas quinze jours et aucune indemnité ordinaire de licenciement n'est créée ou supprimée. L631-19 est coordonné dans le lot, avec sa référence de prix au dernier alinéa du II de L442-8-1. La proposition fournie de cette dernière cible supprime également l'information dans son propre champ ; la dispense présente a son fondement autonome pour toute cohabitation éligible et ne supprime pas les autres conditions du parc social. L'arrêté de charte, extérieur au corpus d'articles, doit être coordonné s'il réimpose l'information retirée ; aucune purge de son contenu n'est déclarée accomplie.",
    "La proposition retire une information préalable légalement obligatoire malgré l'absence de droit d'opposition. Elle maintient toutes les conditions et protections du contrat civil solidaire ; il n'y a aucun transfert de ce contrat vers le droit du travail.",
    "La suppression vise cette information au bailleur, pas les garanties civiles, les conditions d'âge ou la contrepartie modeste. La charte reste à coordonner dans son champ ; aucun gain financier national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : l'information disparaît sans registre, notification, attestation ni consentement de remplacement. Les contrats en cours ne doivent pas être refaits ou régularisés.",
    [effect('obligation_removed','sous-location-solidaire-sans-information',
            "Suppression de l'information préalable du bailleur pour la cohabitation intergénérationnelle solidaire.",
            "Locataire de soixante ans ou plus tenu d'informer préalablement le bailleur de la sous-location solidaire à une personne de moins de trente ans ; aucune opposition possible.",
            "Même faculté de sous-location et mêmes âges, sans information préalable ni formalité de remplacement ; absence de droit d'opposition maintenue.",
            'legal_duty', "Locataires de soixante ans ou plus et personnes de moins de trente ans concluant une cohabitation intergénérationnelle solidaire.",
            "Contrats nouveaux et en cours dès l'entrée en vigueur ; pas d'information de régularisation, droits et recours des périodes antérieures préservés.",
            "elle informe préalablement le bailleur de son intention de sous-louer une partie de son logement à une personne de moins de trente ans dans le cadre d'un contrat de cohabitation intergénérationnelle solidaire, sans que le bailleur puisse s'y opposer.",
            "elle peut sous-louer une partie de son logement à une personne de moins de trente ans dans le cadre d'un contrat de cohabitation intergénérationnelle solidaire, sans information préalable du bailleur et sans que celui-ci puisse s'y opposer.")],
    removed=["L'information préalable obligatoire du bailleur sur l'intention de sous-louer dans le cadre d'une cohabitation intergénérationnelle solidaire."],
    benefit="La dérogation à l'interdiction de sous-location et l'absence de droit d'opposition du bailleur sont conservées pour les futurs binômes éligibles comme pour les contrats actuels. La contrepartie financière modeste, la liberté de convenir la durée, le préavis civil d'un mois et le cadre de charte restent applicables. L'avantage est élargi par le retrait de la seule information préalable ; aucune condition d'ancienneté salariée ni indemnité d'emploi ne le remplace.")

add(18,None,
    "Maintien intégral nécessaire : des menus services sans but lucratif peuvent compléter la contrepartie financière, mais le contrat doit exclure toute subordination. Cette délimitation protège les deux occupants contre l'assimilation de la cohabitation à un emploi domestique déguisé ; ce n'est pas une exonération de charges à supprimer ni une autorisation administrative.",
    "Le contrat est celui de L631-17, dont les règles d'âge, de prix et de préavis civil restent distinctes du travail. L1234-1 et L1234-9 ne sont pas des renvois de cet article ; L1221-2 proposé ne transforme pas la collaboration civile sans subordination en contrat unique. L'exclusion ne fait pas obstacle à l'application du droit du travail à une relation qui serait réellement salariée ; aucune dispense d'impôt ou cotisation pour un emploi dissimulé n'est créée. Aucune durée nouvelle de service n'est imposée.",
    "La source entière permet des menus services et borne leur nature civile. Ce maintien protège la qualification de la cohabitation et ne démontre aucune baisse supplémentaire de prélèvement ou de contrainte.",
    "L'exclusion ne vaut que pour la collaboration sans subordination décrite ; les emplois réels et leurs protections restent dans leur champ. L'incidence sociale n'est pas chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration, feuille de temps, liste de services ou autorisation ne s'ajoute aux deux alinéas officiels maintenus.")

p19 = replace_once(sources[19]['source_xml'],
    "une convention conclue en application de l'article L. 351-2",
    "une convention conclue en application de l'article L. 831-1, y compris une convention relevant des dispositions antérieurement codifiées à l'article L. 351-2,")
add(19,p19,
    "Coordination de fond nécessaire du renvoi de conventionnement après la recodification de 2019 : rattachement à L831-1, avec maintien explicite des conventions historiques de L351-2. La faculté favorable de sous-location solidaire dans le parc social reste ouverte aux nouveaux bénéficiaires, et le calcul au prorata de L442-8-1, II, dernier alinéa, demeure inchangé. Aucun nouveau régime de prix ou d'emploi n'est inventé.",
    "La note de l'ordonnance 2019-770 a été lue : la liste L353-1/L821-2/L831-1/L831-2 indique une recodification répartie, pas quatre conditions cumulatives. Ces quatre sources ont été lues dans le corpus ; L831-1 est la cible de conventionnement locatif pertinente. Ce nouveau renvoi n'est pas une cible contractuelle requise supplémentaire dans reference-targets.json et est signalé ici. La source et la proposition de L442-8-1 montrent que son dernier alinéa du II reste le prorata loyer et charges/surface habitable, et non l'information du bailleur ni les suppléments du III. L631-17 retire l'information préalable dans ce lot ; le renvoi de prix ne la rétablit pas. La liberté de sous-location ne dépend pas du préavis ou de l'ancienneté d'un salarié.",
    "La modification sécurise le champ des logements conventionnés et le maintien des anciennes conventions. La source accordait déjà la sous-location et le prorata : aucune seconde suppression d'information, nouvelle aide ou baisse de loyer n'est comptée ici.",
    "La coordination porte sur le renvoi de conventionnement, pas sur les plafonds, taxes distinctes ou montants de services. La loi extérieure de recodification n'est pas présentée comme réécrite.",
    "Aucune charge nouvelle n'est identifiée : les conventions anciennes restent valables et aucune nouvelle signature, preuve d'emploi ou procédure de conventionnement n'est imposée par cet article.",
    [effect('coordination','conventions-apl-recodification-2019',
            "Actualisation du fondement de conventionnement, sans fermer les conventions antérieures.",
            "Référence au seul L351-2 alors que la note source signale sa recodification en 2019.",
            "Référence à L831-1 pour le conventionnement et maintien explicite des conventions relevant de l'ancien L351-2.",
            'regime', "Locataires des logements sociaux ou conventionnés souhaitant une cohabitation solidaire.",
            "Conventions actuelles et futures éligibles couvertes, anciennes conventions maintenues ; calcul du prix inchangé.",
            "une convention conclue en application de l'article L. 351-2",
            "une convention conclue en application de l'article L. 831-1, y compris une convention relevant des dispositions antérieurement codifiées à l'article L. 351-2")],
    classification='coordination_only')

# 20 — Maintien des protections, renvoi de procédure rendu fonctionnel.
p20 = replace_once(sources[20]['source_xml'],
    "selon les modalités définies à l'article 828 du code de procédure civile",
    "selon les règles de procédure applicables à l'assistance et à la représentation devant la juridiction saisie")
add(20,p20,
    "Coordination nécessaire du renvoi procédural : le renvoi figé à l'article 828 est remplacé par les règles d'assistance et de représentation applicables devant la juridiction saisie. Le droit des associations d'agir sur mandat écrit et d'assister ou représenter reste expressément entier. Toutes les autres dispositions sont maintenues : régime des baux meublés, dérogation liée à la cessation d'activité, prolongation à un an, information préfectorale un mois avant l'audience, exceptions du II et équipements nécessaires à la vie courante.",
    "Le renvoi source à l'article 828 du code de procédure civile appartient à l'ancienne procédure devant le tribunal d'instance ; il appelle confrontation au régime actuel de la juridiction saisie. Le CPC n'est pas une cible fournie et n'a pas été lu en entier : aucune concordance numérique de remplacement n'est affirmée, ni nouvel article inventé. La proposition utilise un renvoi fonctionnel, sans ajouter de pouvoir d'association hors des catégories prévues. Le recommandé avec avis de réception et le mois avant l'audience sont conservés : l'alerte des aides au logement et du fonds de solidarité prévient une éviction sans traitement social ; ce n'est pas le préavis du travail. L632-2 maintient la continuité des baux et le relogement. Les exceptions énumérées 3-2, 3-3, 18, 24-1, 25-4 et 25-11 de la loi de 1989 sont reproduites sans suppression favorable ni extension. Les règles extérieures ne sont pas déclarées intégralement coordonnées.",
    "La source entière conserve ses obligations essentielles contre l'éviction et l'insalubrité ainsi que ses exceptions favorables. Seul le rattachement procédural de l'assistance associative change ; aucune réduction matérielle de charge n'est revendiquée.",
    "Le contenu actuel des règles de procédure civiles extérieures reste à confronter ; le renvoi fonctionnel ne fixe aucun nouveau délai ni nouveau mode de représentation. Aucun effet de coût ou de durée n'est mesuré.",
    "Aucune charge nouvelle n'est identifiée : mêmes associations, même mandat écrit et mêmes litiges, sans pièce ni autorisation ajoutée. Les garanties et la notification préfectorale demeurent à leur charge existante.",
    [effect('coordination','representation-associative-renvoi-procedure',
            "Remplacement du renvoi numérique ancien par les règles procédurales de la juridiction saisie.",
            "Assistance ou représentation associative pour la décence du logement rattachée expressément aux modalités de l'article 828 du CPC.",
            "Même droit associatif rattaché aux règles applicables devant la juridiction saisie, sans nouvelle concordance numérique présumée.",
            'regime', "Locataires de certains meublés et associations légalement habilitées à les assister ou représenter.",
            "Application selon les règles procédurales propres à la juridiction ; aucun délai expiré ni décision définitive n'est rouvert.",
            "selon les modalités définies à l'article 828 du code de procédure civile",
            "selon les règles de procédure applicables à l'assistance et à la représentation devant la juridiction saisie")],
    classification='coordination_only')

add(21,None,
    "Maintien intégral nécessaire des protections en cas de cessation d'hébergement : information trois mois avant, poursuite jusqu'à l'échéance des contrats ou relogement hors force majeure et procédures d'insolvabilité, reconduction si la destination demeure et relogement aux frais de l'opérateur en urbanisme. Ces obligations préviennent la perte brutale du domicile ; elles ne doublonnent ni une autorisation d'activité ni un préavis d'emploi.",
    "L632-1 demeure la cible locative exacte après la coordination procédurale du lot. L314-1 et L314-2 urbanisme ont été lus en entier, notes comprises : relogement et propositions conservent leur champ, sans confondre leur durée maximale propre avec une rénovation locative de vingt-quatre mois. La note de L314-1 sur Mayotte et la référence d'habitabilité de L314-2 appellent leurs vérifications extérieures sans modification ici. Les procédures de sauvegarde et de redressement restent les exceptions précisément nommées ; aucune liquidation ou exception supplémentaire n'est ajoutée.",
    "La source entière assure la continuité du logement et désigne le financeur du relogement. Son maintien n'est pas un transfert nouveau de dépense ni une baisse de contrainte démontrée.",
    "Les trois mois et les droits locatifs sont conservés dans ce seul régime de meublés. Les coûts de relogement et les procédures commerciales distinctes ne sont pas chiffrés ou réformés par ce lot.",
    "Aucune charge nouvelle n'est identifiée : les délais, cas d'exception, reconductions et obligations de relogement sont intégralement ceux du texte officiel.")

add(22,None,
    "Maintien intégral nécessaire de l'ordre public protecteur et de la séparation des régimes : logements-foyers, logements conventionnés avec l'État pour occupation et attribution et résidences à vocation d'emploi sont exclus du chapitre sur certains meublés. Cette délimitation évite déjà un cumul de règles ; l'abroger retirerait des dérogations utiles ou créerait des doublons.",
    "Le renvoi à L631-16-1 a été confronté au texte officiel fourni et à la proposition du présent lot. Il désigne un type de résidence, non la durée d'un emploi ; l'abandon du minimum d'une semaine ne supprime pas l'exclusion de ce chapitre. L633-5, lu dans le corpus, assure aussi la délimitation correspondante des logements-foyers. Les autres exclusions de cet article ne sont pas des dispenses générales de décence, de sécurité ou de recours judiciaire. Aucune condition salariale d'ancienneté ou de notification n'est importée.",
    "L'article source contient déjà les exclusions de cumul et l'ordre public du chapitre. Les conserver intégralement protège les régimes spéciaux et ne produit pas une nouvelle fusion ou baisse de prélèvement.",
    "L'exclusion renvoie aux régimes propres, sans les rendre facultatifs. Les incidences financières des différents types d'hébergement ne sont pas établies dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : aucun registre, certificat d'exclusion, autorisation ou formalité de classement n'est ajouté au maintien de la source.")

add(23,None,
    "Maintien intégral nécessaire d'une simplification déjà existante : dans les établissements sociaux et médico-sociaux visés, le contrat de séjour peut intégrer toutes les clauses du contrat de logement-foyer et son règlement de fonctionnement tient lieu de règlement intérieur. L'alignement de durée évite un double contrat contradictoire ; le supprimer enlèverait un avantage documentaire aux résidents et gestionnaires.",
    "L633-2, source et proposition lues dans le corpus, garde le contrat écrit, ses mentions et les protections du domicile ; la présente faculté d'intégration n'en supprime pas les garanties. Les 6°, 7° et 12° du I de L312-1 CASF et les articles L311-4, L342-1 et L311-7 désignent un champ médico-social extérieur aux cinq codes ; leur contenu n'est pas présenté comme réécrit. La fusion de supports est déjà acquise et ne doit pas être recomptée avec la dispense de paraphe proposée à L633-2. Aucun contrat de travail, préavis salarial ou indemnité ordinaire de rupture n'est visé.",
    "Les deux alinéas officiels offrent déjà une intégration contractuelle et une substitution de règlement. Leur maintien protège ces facultés favorables sans leur attribuer un nouveau gain de conformité.",
    "Le bénéfice reste borné aux catégories médico-sociales expressément énumérées et aux garanties du logement-foyer. Les textes du CASF et les économies existantes de support ne sont pas audités financièrement ici.",
    "Aucune charge nouvelle n'est identifiée : le texte intégralement maintenu n'ajoute ni double contrat, ni second règlement, ni pièce, ni condition de durée supplémentaire.",
    benefit="Les avantages possibles sont la durée du contrat de logement alignée sur le séjour, l'insertion facultative de ses mentions dans le contrat de séjour et le règlement de fonctionnement tenant lieu de règlement intérieur. Ils sont tous conservés intégralement pour les futurs résidents éligibles des catégories 6°, 7° et 12° comme pour les résidents actuels, sans imposer un second support ou fermer ces facultés après la réforme. Aucune exonération fiscale n'est retirée.")

# Les vues de référence sont immuables : leurs empreintes ne décrivent pas le
# résultat rédigé ci-dessus et ne sont jamais recalculées sur notre proposition.
work_checks = {
    10: [
        "L1234-1 règle le préavis de licenciement : la source distingue l'ancienneté et la proposition donne quinze jours calendaires aux nouveaux contrats, avec notification selon sa coordination. L631-12 règle un bail maximal d'un an, sans renvoi à ce préavis ; ni cette durée ni le renouvellement du bail ne rompent l'emploi d'un apprenti ou d'une personne en professionnalisation.",
        "L1221-2 proposé interdit un nouveau terme d'emploi, même fixé par la fin d'une formation ; les CDD antérieurs suivent leur transition. Le public du premier et du sixième alinéas de L631-12 garde l'accès au logement lorsque la formation se déroule en contrat unique indéterminé, sans exiger qu'il soit un nouveau CDD ni confondre le bail annuel avec l'emploi.",
        "L1234-9 porte sur l'indemnité de rupture patronale, non sur l'accès universitaire : source à huit mois, proposition à un an au terme effectif préavis inclus, puis 0,20 mois par année totale au prorata des mois complets, plafond de six mois et exceptions conservées. Aucun de ces seuils n'est importé dans l'éligibilité des étudiants, apprentis ou personnes en professionnalisation."
    ],
    11: [
        "Le préavis de L1234-1, variable avec l'ancienneté dans la source puis de quinze jours pour les nouveaux emplois dans la proposition, ne vise pas les séjours universitaires de moins de trois mois. La suppression du verrou du 31 décembre à L631-12-1 ne modifie ni la notification d'une rupture d'emploi ni le préavis d'un salarié.",
        "L1221-2 proposé sépare la durée d'une formation ou mission de celle de l'emploi ; les anciens CDD restent dans leur transition. Le renvoi au premier alinéa de L631-12 conserve la priorité des apprentis et personnes en professionnalisation éligibles, y compris en contrat unique, lorsque les logements temporaires se libèrent ; aucune fin d'emploi n'est créée au 1er octobre.",
        "L1234-9 proposé calcule l'indemnité ordinaire à partir d'un an au terme effectif, préavis inclus, sur l'ancienneté totale, avec prorata en mois complets et plafond de six mois. Cette règle patronale et la transition des anciens contrats n'ont aucun rôle dans la priorité de retour aux publics universitaires ou dans la durée de moins de trois mois du séjour."
    ],
    12: [
        "L1234-1 vise la rupture par l'employeur, avec ancienneté dans la source et quinze jours dans la proposition pour les nouveaux emplois. Le mois maximal de L631-13 concerne la résiliation d'un contrat de services individualisables souscrit par l'occupant : aucun renvoi ne l'assimile au préavis salarial ni à sa notification écrite.",
        "L1221-2 proposé impose le contrat unique indéterminé aux nouvelles relations salariées, avec maintien des contrats antérieurs. Les prestataires choisis par les occupants de L631-13 fournissent un service au résident ; ce contrat de clientèle n'est pas un CDD et n'est pas converti en emploi. La durée de souscription reste dans son régime propre.",
        "L1234-9, source à huit mois puis proposition à un an et 0,20 mois par année totale plafonné à six mois, concerne une indemnité patronale. Ni l'ancienneté d'un an, ni le préavis inclus, ni les indemnités d'illégalité ne déterminent le prix ou la résiliation du service au résident ; aucune indemnité d'emploi n'est supprimée par le maintien de L631-13."
    ],
    14: [
        "Le préavis de licenciement de L1234-1 ne régit pas les services collectifs payés avec le bail de L631-15. La proposition de quinze jours et sa notification d'emploi ne modifient ni le paiement mensuel à la demande, ni la clause résolutoire locative soumise à l'article 24 de la loi de 1989, même si le locataire est salarié.",
        "L1221-2 proposé supprime les nouveaux CDD dans les seules relations de travail ; les anciens contrats conservent leurs droits. Le contrat de location et ses services non individualisables à L631-15 restent des obligations civiles du bailleur et du locataire, sans terme d'emploi ni critère de forme du contrat salarié à ajouter.",
        "L1234-9 proposé, avec seuil d'un an au terme effectif préavis inclus, 0,20 mois par année totale, prorata en mois complets et plafond légal de six mois, n'est pas visé par les sommes locatives de L631-15. Ces dettes restent distinctes des salaires, congés, dommages d'une rupture illicite et indemnités spéciales, qu'aucune quittance de services n'éteint."
    ],
    16: [
        "L1234-1 proposé donne quinze jours calendaires de préavis patronal aux nouveaux contrats, sans condition d'ancienneté, selon les règles de notification propres à l'emploi. Les dix-huit mois de L631-16-1 sont le maximum du bail ; supprimer sa semaine minimale ne modifie ni ce préavis d'emploi ni les procédures collectives et autorisations spéciales distinctes.",
        "L1221-2 proposé interdit que fin de mission ou de formation termine automatiquement l'emploi ; les anciens CDD demeurent sous leur transition. L631-16-1 est donc coordonné expressément : apprentissage, formation et mission temporaire dans un contrat unique conservent l'accès au bail, dont le terme ne termine pas l'emploi. Le service civique reste un engagement distinct.",
        "L1234-9 proposé réserve l'indemnité ordinaire à la rupture patronale dès un an d'ancienneté au terme effectif avec préavis, puis 0,20 mois par année totale, mois complets au prorata et plafond de six mois, sous ses exceptions. Ni l'accès à cette résidence ni la durée de son bail ne dépend de cette ancienneté ou indemnité ; les anciens droits salariaux ne sont pas touchés."
    ],
    17: [
        "L1234-1 traite du préavis de licenciement, anciennement lié à l'ancienneté et proposé à quinze jours pour les nouveaux emplois. Le mois de L631-17 reste celui d'une cohabitation civile et réciproque, sans salarié ni employeur ; sa notification et sa durée ne sont pas remplacées par la règle salariale lorsque l'information du bailleur est supprimée.",
        "L1221-2 proposé transforme les nouvelles embauches privées en contrats uniques indéterminés, avec transition des anciens CDD. La cohabitation de L631-17, à durée libre et contrepartie modeste, est civile et L631-18 exclut la subordination ; elle ne devient pas un emploi indéterminé et ses futurs binômes éligibles gardent la dérogation de sous-location.",
        "L1234-9 porte sur une indemnité à la charge de l'employeur, avec seuil proposé d'un an au terme effectif préavis inclus, puis ancienneté totale et plafond de six mois. Les parties au contrat solidaire de L631-17 ne sont pas dans cette relation : aucune condition d'ancienneté ni indemnité salariale n'est ajoutée ou retirée, et le préavis civil d'un mois demeure."
    ],
    18: [
        "L1234-1 est une règle de licenciement et la proposition de quinze jours est réservée à l'emploi. L631-18 exige une collaboration sans subordination : ses menus services ne créent ni employeur, ni ancienneté salariale, ni obligation de notification de licenciement. Le préavis de cohabitation reste celui, civil, de L631-17.",
        "L1221-2 proposé impose une durée indéterminée aux nouveaux contrats de travail, pas aux collaborations civiles de L631-18. Le texte conservé exclut expressément subordination et code du travail ; il n'autorise toutefois pas à masquer un emploi réel. Ni le contrat unique ni les transitions des anciens CDD n'altèrent cette délimitation de champ.",
        "L1234-9, à huit mois dans la source puis à un an au terme effectif dans la proposition, indemnise une rupture patronale sous ses conditions et exceptions. Les menus services civils sans but lucratif ni subordination de L631-18 ne sont pas une année de travail à indemniser : le maintien ne supprime aucun salaire, congé acquis, réparation ou indemnité spéciale d'un véritable salarié."
    ],
    19: [
        "L1234-1 régit le préavis patronal, variable selon l'ancienneté dans la source et proposé à quinze jours pour les nouveaux emplois. L631-19 ne vise que la sous-location d'une partie du logement social et son prix ; le renvoi à L631-17 conserve le mois de préavis civil, sans importer la notification du licenciement.",
        "L1221-2 proposé ne s'applique qu'aux nouvelles relations de travail, avec conservation transitoire des anciens contrats. Les sous-locations civiles permises par L631-19 restent accessibles aux futurs binômes éligibles indépendamment de leur statut salarié ; ni leur durée ni le prorata de loyer ne déterminent un terme d'emploi ou un cas de CDD spécial.",
        "L1234-9 proposé prévoit l'indemnité patronale dès un an au terme effectif préavis inclus, à 0,20 mois par année totale et plafond de six mois, en préservant les champs spéciaux. Cette indemnité n'est pas le coût de la sous-location calculé par L631-19 ; aucune condition d'ancienneté, remise d'indemnité ou compensation sur le loyer n'est créée."
    ],
    22: [
        "L1234-1 proposé donne quinze jours de préavis d'emploi selon ses règles de notification, et non un préavis universel d'occupation. L632-3 délimite le chapitre des meublés et exclut notamment L631-16-1 ; ni la durée du bail de cette résidence ni l'ordre public locatif ne se règlent par l'ancienneté salariale de la source de L1234-1.",
        "L1221-2 proposé laisse une mission ou une formation limitée se dérouler dans un emploi indéterminé, avec droits des contrats antérieurs conservés. L'exclusion des résidences à vocation d'emploi à L632-3 reste applicable à ces locataires : elle vise la résidence définie à L631-16-1, pas l'existence d'un nouveau CDD ou la fin de l'emploi.",
        "L1234-9 proposé conditionne l'indemnité patronale à un an au terme effectif préavis inclus, puis 0,20 mois par année totale au prorata des mois complets, plafond de six mois et transitions propres. L632-3 ne renvoie pas à cette indemnité ; ses exclusions locatives ne réduisent ni droits salariaux acquis, ni réparations, ni indemnités spéciales."
    ]
}

extra_checks = {
    (11,'L631-12'): "La vue fournie est le texte officiel intégral de L631-12, pas une proposition : son premier alinéa énumère étudiants, moins de trente ans en formation ou stage, apprentis, professionnalisation et accueil exceptionnel des enseignants et chercheurs. C'est exactement ce public qui bénéficie de la priorité à libération prévue à L631-12-1. Le bail annuel et la suppression des autorisations proposée dans ce lot ne changent pas ce renvoi ; la formation sous contrat unique demeure éligible, sans préavis ni ancienneté salariale à exiger.",
    (14,'L631-13'): "La cible officielle distingue services non individualisables, bénéficiant à tous, et services individualisables souscrits à part, avec préavis maximal d'un mois pour ces derniers. Les 1° et 2° de L631-15 visent les premiers ; la quittance du 5° les distingue du loyer et des charges. Aucun renvoi n'importe le préavis des services individuels dans la clause résolutoire du bail ou dans le contrat unique de travail.",
    (19,'L631-17'): "La vue fournie est officielle et comporte encore l'information préalable du bailleur ; la proposition de ce lot la supprime sans fermer la sous-location aux futurs binômes. Le renvoi au chapitre maintient les seuils de soixante ans et moins de trente ans, la contrepartie modeste, la liberté de durée et le préavis civil d'un mois. Ce dernier ne devient pas quinze jours et aucune ancienneté de travail n'est requise pour le locataire social.",
    (19,'L442-8-1'): "La source et la proposition fournies conservent au dernier alinéa du II le coût au prorata du loyer et des charges rapporté à la surface habitable : c'est la seule règle de calcul appelée par la seconde phrase de L631-19. L'information du bailleur est située au début du II et est supprimée dans la proposition cible ; le renvoi de prix ne la rétablit pas. Les taxes et prestations du III ne sont pas confondues avec ce prorata, et le caractère saisonnier du I, coordonné au contrat unique, n'est pas une condition de cette cohabitation.",
    (22,'L631-16-1'): "La vue fournie est la source officielle, à bail d'une semaine à dix-huit mois, et non une proposition. L632-3 vise la résidence définie dans son ensemble, avec public de mobilité et conditions de 80 % sous plafonds ; il ne vise pas un alinéa de rupture d'emploi. La proposition du lot retire la semaine minimale et confirme l'accès en contrat unique, sans changer cette identité de résidence ni son exclusion du chapitre des meublés ; les baux anciens ne sont pas raccourcis automatiquement."
}

for i,a in enumerate(answers):
    key = a['code_id'] + '|' + a['source_id']
    for target_key in references['requirements'][key]:
        target = references['targets'][target_key]
        n = target['number']
        if n in ('L1234-1','L1221-2','L1234-9'):
            assessment = work_checks[i][('L1234-1','L1221-2','L1234-9').index(n)]
        else:
            assessment = extra_checks[(i,n)]
        a['reference_checks'].append(dict(target_key=target_key,
                                           view_sha256=target['view_sha256'],
                                           assessment=assessment))

assert len(answers) == len(sources) == 24
for s,a in zip(sources,answers):
    for k in ('code_id','source_id','source_sha256','number'):
        assert a[k] == s[k]
    if s.get('benefit_check_required'):
        assert len(a.get('benefit_review','')) >= 100
    imp = a['substantive_impact']
    for k in ('assessment','scope_limitations','new_burdens_review'):
        assert len(imp[k]) >= 40
    seen = set()
    seen_measures = set()
    for e in imp['effects']:
        pair = (e['measure_id'],e['kind'])
        assert pair not in seen, (a['number'],pair)
        seen.add(pair)
        # The stricter unique-measure check also catches accidental effects
        # split into several entries for the same measure inside one article.
        assert e['measure_id'] not in seen_measures, (a['number'],e['measure_id'])
        seen_measures.add(e['measure_id'])
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        for field,xml in [('source_quote',s['source_xml']),('proposed_quote',a['proposed_xml'])]:
            q=e[field]
            assert len(q)>=12
            assert q in plain(xml), (a['number'],field,q,plain(xml))
    for v in a.get('removed_provisions',[]):
        assert len(v)>=30
    assert [x['target_key'] for x in a['reference_checks']] == references['requirements'][a['code_id']+'|'+a['source_id']]
    for check in a['reference_checks']:
        assert len(check['assessment'])>=80
        assert check['view_sha256']==references['targets'][check['target_key']]['view_sha256']

Path('answer.json').write_text(json.dumps(answers,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'articles':len(answers), 'statuses':{x:sum(a['status']==x for a in answers) for x in ['rewrite_draft','retained_unchanged']}, 'effects':sum(len(a['substantive_impact']['effects']) for a in answers)},ensure_ascii=False))
