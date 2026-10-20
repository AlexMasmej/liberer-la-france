import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}


def base(number, proposed_xml, reason, review_notes, classification, assessment,
         scope_limitations, new_burdens_review, effects):
    source = by_number[number]
    return {
        **{k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': proposed_xml,
        'reason': reason,
        'review_notes': review_notes,
        'status': 'retained_unchanged' if proposed_xml is None else 'rewrite_draft',
        'substantive_impact': {
            'version': 1,
            'classification': classification,
            'assessment': assessment,
            'scope_limitations': scope_limitations,
            'new_burdens_review': new_burdens_review,
            'effects': effects,
        },
    }


def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           replacement_or_new_burdens, source_quote, proposed_quote):
    return dict(
        kind=kind, measure_id=measure_id, description=description,
        before=before, after=after, unit=unit,
        affected_population=affected_population,
        conditions_and_transition=conditions_and_transition,
        replacement_or_new_burdens=replacement_or_new_burdens,
        source_quote=source_quote, proposed_quote=proposed_quote,
    )


p4 = re.findall(r'<p>(.*?)</p>', by_number['L411-4']['source_xml'], re.S)
copy_waiver = (
    "Les règles du premier alinéa s'appliquent de plein droit aux actes qui transfèrent "
    "la propriété ou la jouissance de ces logements ou qui constatent ce transfert, "
    "sans qu'il soit nécessaire de les reproduire. La seule absence de reproduction "
    "de cet alinéa dans un acte n'entraîne pas sa nullité."
)
old_acts = (
    "La dispense de reproduction prévue au deuxième alinéa s'applique aux actes conclus "
    "à compter de l'entrée en vigueur de la présente loi. Pour les actes conclus avant "
    "cette date, l'obligation de reproduction du premier alinéa, la nullité de plein droit "
    "et l'action en nullité pour défaut de reproduction restent régies par les dispositions "
    "antérieures. Cette action peut être intentée par tout intéressé ou par l'autorité "
    "administrative dans un délai de cinq ans à compter de la publication de l'acte au "
    "fichier immobilier, même si cette publication intervient après l'entrée en vigueur "
    "de la présente loi. À Mayotte, ce délai court de l'inscription de l'acte au livre "
    "foncier, même si cette inscription intervient après cette entrée en vigueur ; "
    "pour l'application au présent article du 1° de l'article L. 472-3, le renvoi au "
    "deuxième alinéa s'entend du présent alinéa. Aucun délai de recours expiré n'est "
    "rouvert. Les droits des occupants et les recours fondés sur la violation des "
    "règles de fond sont préservés."
)
proposed4 = '\n'.join('<p>' + p + '</p>' for p in (
    p4[0], copy_waiver,
    p4[2].replace('des III et VI l\'article', 'des III et VI de l\'article'),
    old_acts,
))

answer4 = base(
    'L411-4', proposed4,
    "Réforme de fond conservée du précédent brouillon : pour les actes nouveaux, suppression de la reproduction intégrale obligatoire du premier alinéa et de la nullité attachée à sa seule omission, sans attestation ni déclaration de remplacement. La seconde passe ne justifie pas de supprimer les conditions de ressources et plafonds de loyers après déconventionnement ou transfert : ils maintiennent l'affectation sociale des logements aidés et protègent les occupants, y compris contre une cession non volontaire. Les premier et troisième alinéas sont repris du texte officiel, sous la seule correction grammaticale signalée. Les quatre exclusions favorables restent ouvertes aux opérations futures éligibles. Une coordination de fond manquante au brouillon est ajoutée pour conserver le point de départ mahorais du délai applicable aux actes anciens ; elle ne constitue pas une deuxième suppression d'obligation.",
    "Lecture entière de la source, des notes vides, du previous_draft et du texte initial de SRU 145 joint, identique dans les quatre sru_context. Le texte initial établit la création de L. 411-4, mais ne comporte ni la formalité actuelle de copie ni toutes les exclusions actuelles ; leur filiation détaillée ultérieure n'est pas démontrée par cette seule pièce. Aucun achèvement des 209 articles n'est affirmé. Les trois alinéas initiaux conservent leur position ; la transition est ajoutée au quatrième. Sont conservés le 5 janvier 1977, les constructions, acquisitions et acquisitions-améliorations aidées, L. 831-1, la survie après convention et transfert non volontaire, ainsi que L. 353-19. Les exclusions restent intégrales : fin du bail à construction ou emphytéotique avec retour des constructions au propriétaire du terrain ; ventes SEM du premier alinéa du II et des III et VI de L. 443-11 ; accession progressive par SCI de L. 443-6-2 et suivants une fois le logement devenu propriété d'un associé personne physique ; usufruit temporaire. La seule acquisition de parts ne vaut pas attribution de propriété, comme le confirment L. 443-6-5 et L. 443-6-9. La source écrit « des III et VI l'article » : ajout explicite de « de », sans changement des subdivisions et sans extension aux I ou VII de L. 443-11. L. 443-11 a été lu avec sa proposition : ses dispenses et suppressions de durées acquises restent compatibles, sans être réécrites ni recomptées ici. L. 831-1, L. 353-19 et ses cibles L. 353-17 et L. 353-15-2, L. 365-5, L. 365-2 et R. 491-3 à R. 491-6 ont été lus intégralement avec leurs notes ; le présent allègement ne retire ni le bénéfice des protocoles de rétablissement du bail et de l'aide correspondante, ni l'application aux logements des organismes agréés, ni les plafonds, leur actualisation et les mentions utiles des baux. Les obligations de convention en vigueur de L. 353-17 restent distinctes de la copie du présent alinéa après déconventionnement. La note de 2021 de R. 491-3/4 n'est pas une date de réforme future. L. 472-3 a été lu entièrement : son 1° adapte le deuxième alinéa actuel à l'inscription au livre foncier de Mayotte. Le quatrième alinéa proposé rend expressément cette adaptation applicable à la transition, malgré le déplacement coordonné de la règle ancienne ; harmoniser matériellement ce 1° pour viser cette transition. Le volet de ce même 1° concernant L. 411-3 doit être coordonné séparément avec sa proposition publique, non modifiée ici. Le délai de cinq ans reste celui de la seule ancienne nullité formelle, même si publication ou inscription ultérieure ; aucune prescription expirée n'est rouverte. Les recours pour violation du fond ne reçoivent pas artificiellement ce délai spécial. Aucun prélèvement, nouveau barème ou financement n'est créé.",
    'material_reduction',
    "Par rapport à la source officielle entière, les actes futurs n'ont plus à recopier le premier alinéa et ne sont plus frappés de nullité pour cette seule omission. Les conditions locatives et toutes les exclusions sont maintenues. La coupe existait déjà au brouillon ; la correction du renvoi mahorais sécurise sa transition sans gain supplémentaire revendiqué.",
    "La dispense concerne seulement la reproduction prescrite par cet article pour les actes conclus dès l'entrée en vigueur. Les actes antérieurs, les formalités civiles et de publicité foncière autonomes et les contrôles de fond subsistent. Les effets financiers et le solde de complexité des autres codes ne sont pas chiffrés ; l'harmonisation matérielle de L. 472-3 reste hors lot.",
    "Aucune charge nouvelle identifiée : aucune pièce, attestation, donnée, déclaration, autorisation ou délai ne remplace la copie supprimée. Le régime des actes anciens, y compris le délai mahorais, est conservé ; les obligations locatives et mentions de bail déjà applicables ne sont pas augmentées.",
    [effect(
        'obligation_removed', 'logements-sociaux-actes-sans-reproduction',
        "Suppression de la copie légale obligatoire et de sa nullité purement formelle dans les actes nouveaux du champ SEM et des extensions légales de ce champ.",
        "Tout acte de transfert de propriété ou de jouissance devait reproduire le premier alinéa, à peine de nullité de plein droit ; action de tout intéressé ou de l'administration pendant cinq ans après publication, avec adaptation mahoraise par L. 472-3.",
        "Pour les actes conclus dès l'entrée en vigueur, aucune reproduction obligatoire et aucune nullité pour sa seule absence ; les règles de fond s'appliquent directement. Les actes antérieurs conservent leur régime et leur délai de cinq ans.",
        'legal_duty',
        "Sociétés d'économie mixte, acquéreurs et parties aux actes de transfert des logements visés ; organismes de maîtrise d'ouvrage relevant de l'extension de L. 365-5 et leurs cocontractants.",
        "Actes conclus à compter de l'entrée en vigueur ; actes anciens et droits des occupants protégés, même si publicité ultérieure. À Mayotte, le délai ancien court de l'inscription au livre foncier. Les quatre exclusions de l'article subsistent pour les situations éligibles futures.",
        "Aucun dépôt, certificat ou envoi de remplacement. Plafonds, conditions de ressources, publicité foncière et recours de fond restent à leur champ propre.",
        "Tout acte transférant la propriété ou la jouissance de ces logements ou constatant un tel transfert reproduit, à peine de nullité de plein droit, les dispositions du premier alinéa.",
        copy_waiver,
    )],
)
answer4.update(
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Reproduction obligatoire du premier alinéa dans tout acte nouveau transférant la propriété ou la jouissance des logements ou constatant ce transfert.",
        "Nullité de plein droit et action spéciale de cinq ans fondées sur la seule omission de cette reproduction dans les actes nouveaux, sans suppression des recours de fond ni du régime des actes antérieurs.",
    ],
)


answer6 = base(
    'L411-6', None,
    "Maintien intégral utile de la source officielle, sans reconduire la reformulation stylistique du précédent brouillon. L'application de tout le livre IV dès la cessation de la convention empêche le déconventionnement d'écarter le statut protecteur des logements HLM et les droits de leurs occupants. L'article n'impose pas de prélèvement autonome, d'agrément, de déclaration, de pièce, de délai minimal ou de circuit doublonné à supprimer. Retirer le renvoi entier ferait disparaître des protections et des régimes favorables sans permettre d'isoler une charge dispensable ; les suppressions décidées dans les articles de fond restent applicables au livre IV ainsi visé. Aucune coupe supplémentaire justifiée ni réécriture de fond n'est retenue.",
    "Source entière, notes vides et précédent brouillon entier examinés. Le texte initial entier de SRU 145 contient cette règle, sous L. 411-6, avec l'ancien renvoi à L. 351-2 ; la version assignée vise L. 831-1, lu en entier. Les trois éléments demeurent : cessation d'effet d'une convention de ce champ, logements appartenant à un organisme HLM, application immédiate de l'ensemble du livre IV. L. 411-3, lu intégralement avec sa proposition, protège distinctement les logements aidés ou conventionnés et leurs occupants en cas de transfert. L. 411-5, lu entièrement, prévoit un régime distinct de six ans pour certaines sociétés à participation majoritaire de la Caisse des dépôts : aucune telle durée n'est importée ici. L'article n'est ni une prorogation automatique de la convention expirée ni, à lui seul, une garantie de maintien de l'APL après son terme ; les conditions autonomes de l'aide restent à leur champ propre. Les dispositions du livre IV s'appliquent dans leur état réformé : le renvoi ne fait pas revivre quotas, rattrapages, prélèvements, carence, copie d'acte ou approbations supprimés dans leurs textes opératoires. Aucune filiation de toute la législation actuelle ni aucun examen achevé des 209 articles n'est affirmé. Le corps officiel sera reproduit depuis la source ; ce maintien n'est compté ni comme réécriture ni comme simplification.",
    'retained_necessary',
    "Aucun changement normatif par rapport à la source entière : maintien de la continuité du régime HLM au terme de la convention, nécessaire pour éviter une sortie automatique des protections et de l'affectation sociale. La reformulation antérieure n'apportait aucun allègement démontré et n'est pas conservée comme nouveau texte.",
    "Le maintien ne proroge pas une convention ni ses financements et ne garantit pas l'APL hors de ses conditions propres. Il concerne les logements appartenant aux organismes HLM visés ; le régime distinct des SEM relève notamment de L. 411-4. Aucun solde national de coût ou de complexité n'est établi.",
    "Aucune charge nouvelle identifiée : le texte officiel est maintenu sans dossier, registre, délai, pièce ou condition supplémentaire. Le renvoi au livre IV ne recrée pas une disposition supprimée ; ses obligations substantielles restent soumises aux réformes de leurs articles propres.",
    [],
)
answer6['classification'] = 'retained_necessary'


repeal7 = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi.</p>\n"
    "<p>Les nouvelles attributions de locaux commerciaux ne sont plus soumises, au titre "
    "du présent article, à une prise en compte obligatoire des objectifs de mixité du "
    "quartier ou de l'arrondissement ni à l'avis consultatif préalable du maire. Les "
    "procédures en cours se poursuivent sans cette consultation, sans nouvelle demande "
    "ni remise à zéro des délais.</p>\n"
    "<p>Les décisions d'attribution valablement prises, les contrats conclus, les engagements "
    "acquis et les droits des tiers avant cette entrée en vigueur sont préservés. La "
    "présente abrogation ne dispense pas du respect des conditions attachées aux aides "
    "et au service d'intérêt économique général lorsqu'elles résultent d'un fondement "
    "distinct ; elle ne rétablit aucun quota communal de logements sociaux.</p>"
)
answer7 = base(
    'L411-7', repeal7,
    "Abrogation de fond intégrale conservée du précédent brouillon : suppression de l'obligation de tenir compte des objectifs de mixité du quartier ou de l'arrondissement pour attribuer les locaux commerciaux en pied d'immeubles HLM et de l'avis consultatif préalable du maire. Ce circuit consultatif ne décide pas de la validité commerciale du bail et aucun besoin essentiel autonome ne justifie de le doubler avec les obligations générales des bailleurs. Aucun avis, déclaration ou contrôle préalable de remplacement n'est créé. Les actes et engagements antérieurs restent protégés ; les règles autonomes d'aides, de gestion et de protection contre la discrimination subsistent. Aucune coupe supplémentaire de cet article déjà entièrement abrogé ne reste possible sans toucher à ces régimes distincts.",
    "Les deux alinéas officiels et le previous_draft ont été lus entièrement. Ils correspondent aux deux alinéas créant L. 411-7 dans le texte initial entier de SRU 145 joint. La filiation de ces deux obligations est établie par concordance de contenu, sans étendre ce constat à tout SRU 145 ou aux 209 articles. La proposition conserve l'abrogation antérieure ; son entrée en vigueur est rattachée à la présente loi sans inventer un intitulé officiel de loi future. Les consultations pendantes cessent sans redépôt ni reprise des délais ; les décisions valables, baux et engagements déjà constitués ne sont pas défaits. Aucune taxe ni aucun avantage fiscal n'est institué par la source. L'obligation de mixité des locaux commerciaux n'est pas une exonération ou une faculté favorable de construire ; sa suppression ne ferme pas la compétence de louer ces locaux, l'accès aux aides, ni les droits des occupants. Les règles d'un autre fondement, notamment aides d'État et service d'intérêt économique général, concurrence, comptabilité, non-discrimination et recours, ne sont pas abrogées implicitement. La recherche des renvois à L. 411-7 dans les textes officiels du corpus CCH fourni n'a pas relevé de cible réglementaire à rétablir ; cela ne constitue pas un inventaire exhaustif des textes extérieurs. Aucun contrat ancien n'est modifié sous couvert de suppression d'un quota communal.",
    'material_reduction',
    "La comparaison avec les deux alinéas de la source entière établit la disparition de deux obligations : critère de mixité imposé pour les locaux commerciaux et saisine préalable du maire. L'abrogation était déjà acquise au brouillon ; aucune réduction fiscale ni nouveau gain additionnel de seconde passe n'est revendiqué.",
    "L'allègement ne concerne que les obligations propres de L. 411-7 et les attributions futures ou procédures pendantes. Contrats, décisions et engagements antérieurs sont préservés. Les obligations ayant un fondement autonome, notamment celles des aides et du SIEG, ne sont pas supprimées ; leur coût et le solde global ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : aucun avis de remplacement, déclaration, registre, donnée ou délai supplémentaire n'est prévu. Le bailleur garde sa décision et les procédures pendantes continuent sans nouvelle demande ; les obligations autonomes déjà applicables ne sont pas augmentées.",
    [
        effect(
            'obligation_removed', 'hlm-locaux-commerciaux-liberte-attribution',
            "Suppression du régime propre d'attribution des locaux commerciaux en pied d'immeubles HLM : retrait conjoint du critère obligatoire de mixité et de la saisine pour avis consultatif préalable du maire, regroupés en un seul effet de cette mesure.",
            "Pour les locaux commerciaux en pied des immeubles construits ou acquis par les organismes HLM, chaque attribution doit tenir compte de la mixité urbaine et sociale du quartier ou de l'arrondissement et chaque proposition doit être préalablement soumise à l'avis consultatif du maire. Aucun délai chiffré n'est fixé par cet article.",
            "Pour les attributions nouvelles et les procédures pendantes, ni critère de mixité ni saisine préalable du maire ne sont imposés sur le fondement de L. 411-7 ; aucun nouveau dossier ni reprise des délais. Les règles de gestion ayant un fondement autonome subsistent.",
            'legal_duty',
            "Organismes HLM attribuant des locaux commerciaux en pied d'immeubles construits ou acquis par eux, services communaux et candidats à ces locaux.",
            "Dès l'entrée en vigueur pour les attributions nouvelles et les consultations pendantes ; décisions valables, contrats, engagements acquis et droits des tiers antérieurs préservés.",
            "Aucun critère, déclaration, avis d'une autre autorité ou contrôle préalable ne remplace ces obligations. Conditions autonomes des aides et du SIEG conservées ; aucun nombre de jours économisés n'est inventé.",
            re.sub(r'<[^>]+>', '', by_number['L411-7']['source_xml']).strip(),
            "Les nouvelles attributions de locaux commerciaux ne sont plus soumises, au titre du présent article, à une prise en compte obligatoire des objectifs de mixité du quartier ou de l'arrondissement ni à l'avis consultatif préalable du maire.",
        ),
    ],
)
answer7.update(
    change_type='full_repeal',
    repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression pour les attributions nouvelles et les consultations pendantes de la prise en compte obligatoire des objectifs de mixité et de l'avis consultatif préalable du maire pour les locaux commerciaux en pied d'immeubles HLM ; décisions valables, contrats et engagements antérieurs préservés.",
)


p8 = re.findall(r'<p>(.*?)</p>', by_number['L411-8']['source_xml'], re.S)
voluntary8 = (
    "Les conventions entrent en vigueur à la date qu'elles fixent ou, à défaut, à la date "
    "de leur signature, sans approbation par arrêté ministériel. Elles obligent leurs "
    "signataires et les organismes qui y adhèrent volontairement, dans les limites de "
    "leurs compétences respectives. Elles ne peuvent, par elles-mêmes, imposer "
    "d'obligations aux autres organismes ni modifier les droits des occupants résultant "
    "de la loi ou de leurs contrats. Par dérogation au dernier alinéa de l'article "
    "L. 411-8-1, ces règles s'appliquent également aux conventions de mutualisation "
    "financière prévues à cet article. L'absence d'approbation ministérielle ne fait "
    "obstacle ni aux aides prévues par ces conventions ni aux avantages légaux attachés "
    "aux conventions de mutualisation financière, lorsque leurs autres conditions "
    "sont remplies. Aucune adhésion à ces conventions ne peut être exigée pour bénéficier "
    "d'une exonération fiscale ou d'une aide dont l'attribution repose sur un fondement "
    "légal distinct."
)
transition8 = (
    "Les dispositions du sixième alinéa s'appliquent aux conventions conclues à compter "
    "de l'entrée en vigueur de la présente loi. Les conventions signées avant cette "
    "date et non encore approuvées peuvent entrer en vigueur, à compter de cette date, "
    "selon ces dispositions avec l'accord de leurs signataires. Les conventions "
    "antérieurement approuvées, les droits à aide et les engagements financiers "
    "valablement constitués sont préservés. Cette conservation ne permet pas de "
    "maintenir pour l'avenir les clauses qui ne font que reprendre les quotas, "
    "objectifs de rattrapage, prélèvements ou effets de la carence supprimés par "
    "la présente loi."
)
proposed8 = '\n'.join('<p>' + p + '</p>' for p in (*p8[:5], voluntary8, transition8))
approval_source = (
    "Les stipulations des conventions ainsi conclues par l'Union sociale pour l'habitat "
    "modéré regroupant les fédérations d'organismes d'habitations à loyer modéré entrent "
    "en vigueur et s'imposent après approbation par arrêté du ou des ministres concernés."
)
answer8 = base(
    'L411-8', proposed8,
    "Réforme de fond conservée : suppression de l'approbation ministérielle après signature de l'État et de l'effet obligatoire automatique des conventions sur les organismes non consentants. Aucun visa ni déclaration ne remplace l'arrêté. La dérogation expresse à L. 411-8-1 évite que le doublon d'approbation ne réapparaisse pour la mutualisation financière. Les cinq premiers alinéas officiels, faculté de conventionner, renvoi à L. 301-1 et trois objets compris, sont maintenus sans reformulation de remplissage. La seconde passe n'identifie pas d'autre obligation autonome supprimable dans ces objets facultatifs ; les retirer fermerait une faculté de financement ou de service favorable. La proposition précise que l'absence d'approbation ne prive pas les conventions de leurs aides et avantages légaux, y compris pour les situations futures éligibles. Les droits des occupants, conventions déjà approuvées et engagements anciens sont préservés ; les conventions en attente peuvent bénéficier de la simplification avec l'accord de leurs signataires, sans rétroactivité imposée.",
    "Source entière, notes vides et previous_draft entier confrontés au texte initial entier de SRU 145. Ce texte établit l'origine de la faculté, des trois objets et de l'approbation ; il ne prouve pas que la mutualisation financière de L. 411-8-1, ajoutée ultérieurement, vient entièrement de SRU. Les six alinéas gardent leur ordre, puis une transition est ajoutée ; les trois tirets et la cible « sixième alinéa » sont conservés. La source alterne « Union sociale pour l'habitat » et « Union sociale pour l'habitat modéré » : les cinq premiers alinéas sont inchangés et le sixième ne répète pas cette divergence préexistante, sans changer le signataire. L. 301-1, lu intégralement, maintient les finalités d'aide et les droits des ménages en difficulté. L. 411-8-1 a été lu entièrement avec sa proposition : son dernier alinéa public conserve encore l'arrêté et l'effet obligatoire ; le sixième alinéa proposé y déroge expressément pour les conventions concernées et leur transition. Sa mise en cohérence matérielle reste à rédiger dans cet autre article, sans compter une seconde suppression d'approbation ou d'extension. Le programme, les trois années au maximum, les modalités de révision et les critères d'aides de L. 411-8-1 ne sont pas supprimés par cette dérogation au seul dernier alinéa. Les droits des occupants, loyers, suppléments et charges relevant d'autres fondements ne deviennent pas négociables par cette seule convention. L. 452-4-1 a été lu avec sa proposition : sa source déduit de l'autofinancement les soldes nets reçus au titre de L. 411-8-1 ; sa proposition publique abroge déjà la cotisation additionnelle pour les années commençant le 1er janvier suivant l'entrée en vigueur tout en protégeant les années anciennes et leurs déductions. La présente proposition ne rétablit donc ni cette cotisation ni une nouvelle formalité pour cette déduction ; le maintien des avantages conventionnels ne transforme pas une déduction sans impôt en crédit remboursable. Elle ne remet en cause ni cette suppression acquise ni celles décidées dans les articles financiers distincts ; aucune nouvelle réduction de cotisation n'est comptée ici. Les nouvelles conventions recevables restent utilisables pour les aides et mutualisations volontaires ; l'absence de visa ne leur retire pas leur qualification légale. Les avantages d'un fondement légal distinct ne sont pas soumis à l'adhésion. Les règles budgétaires, compétences de signature, contrôles légaux des fonds et exigences autonomes de SIEG ou du droit de l'Union demeurent ; aucune recette ou enveloppe n'est créée. Les conventions déjà signées mais non approuvées n'entrent dans le nouveau régime qu'avec accord des signataires, au plus tôt à l'entrée en vigueur, sans effacer des créances ni imposer une nouvelle charge. Les clauses purement fondées sur les quotas, le rattrapage, les prélèvements ou la carence supprimés ne sont pas maintenues pour l'avenir. Aucun autre volet de SRU 145 ni l'ensemble des 209 articles n'est déclaré achevé.",
    'material_reduction',
    "Par rapport à la source officielle entière, les conventions nouvelles produisent effet sans arrêté ministériel et ne s'étendent plus obligatoirement aux organismes non consentants. La même règle couvre expressément la mutualisation de L. 411-8-1. Ces coupes figuraient déjà au brouillon ; la garantie des avantages attachés aux conventions et la précision temporelle n'ajoutent pas une autre baisse de prélèvement.",
    "Les conventions déjà approuvées et engagements antérieurs restent protégés. Les aides gardent leurs conditions propres et aucune ressource de financement n'est garantie. L. 411-8-1 doit être harmonisé matériellement avec la dérogation opératoire ; ses autres clauses ne sont pas réécrites ici. Aucun effet budgétaire net ou solde de complexité de l'ensemble des codes n'est établi.",
    "Aucune charge nouvelle identifiée : aucun dépôt, agrément, déclaration, registre ni délai ne remplace l'approbation supprimée. L'adhésion volontaire délimite les obligations contractuelles au lieu d'une extension forcée ; elle n'est pas imposée pour les aides de fondement distinct. L'accord des signataires pour appliquer le nouveau régime à une convention ancienne non approuvée protège leur consentement et ne crée pas de procédure administrative obligatoire.",
    [
        effect(
            'authorization_removed', 'hlm-conventions-suppression-approbation',
            "Suppression de l'arrêté ministériel d'approbation des conventions nationales HLM, avec dérogation à son doublon pour les conventions de mutualisation financière.",
            "Après conclusion avec l'État, les stipulations n'entrent en vigueur qu'après approbation par arrêté du ou des ministres concernés ; L. 411-8-1 répète cette exigence pour la mutualisation.",
            "Les conventions nouvelles entrent en vigueur à la date fixée ou à la signature, sans arrêté ; la même dispense s'applique à la mutualisation par dérogation expresse, sans suppression des autres conditions des aides.",
            'legal_duty',
            "État, Union sociale pour l'habitat, organismes parties aux conventions et organismes HLM participant à leur mutualisation financière.",
            "Conventions conclues dès l'entrée en vigueur ; conventions signées antérieurement non approuvées pouvant opter avec l'accord des signataires, au plus tôt à cette date. Conventions approuvées et droits antérieurs préservés.",
            "Aucun visa, déclaration ou certificat de remplacement. Le programme, la durée maximale et les critères d'aides propres à L. 411-8-1 restent ; l'absence d'approbation ne retire pas les avantages attachés aux conventions.",
            approval_source,
            "Les conventions entrent en vigueur à la date qu'elles fixent ou, à défaut, à la date de leur signature, sans approbation par arrêté ministériel.",
        ),
        effect(
            'obligation_removed', 'hlm-conventions-fin-extension-obligatoire',
            "Fin de l'effet obligatoire automatique des conventions nouvelles sur les organismes qui ne les ont ni signées ni volontairement rejointes.",
            "Les stipulations conventionnelles approuvées s'imposent dans le régime national sans limitation expresse aux organismes consentants, y compris selon le doublon de L. 411-8-1.",
            "Les obligations conventionnelles des nouvelles conventions ne lient que les signataires et adhérents volontaires ; elles ne modifient pas les droits légaux ou contractuels des occupants.",
            'legal_duty',
            "Organismes HLM qui ne sont pas parties ou adhérents volontaires aux conventions nationales, notamment de mutualisation financière.",
            "Même champ temporel que la suppression d'approbation ; les conventions déjà approuvées et engagements financiers antérieurs restent valables, sauf clauses qui ne font que reprendre les obligations SRU supprimées pour l'avenir.",
            "Pas de contribution obligatoire de remplacement ni d'adhésion exigée pour les exonérations ou aides d'un fondement légal distinct ; aucune suppression d'aide n'est décidée.",
            approval_source,
            "Elles obligent leurs signataires et les organismes qui y adhèrent volontairement, dans les limites de leurs compétences respectives. Elles ne peuvent, par elles-mêmes, imposer d'obligations aux autres organismes ni modifier les droits des occupants résultant de la loi ou de leurs contrats.",
        ),
    ],
)
answer8.update(
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Approbation par arrêté du ou des ministres concernés après la signature des conventions nouvelles conclues avec l'État, y compris le doublon prévu pour la mutualisation financière par L. 411-8-1.",
        "Effet obligatoire automatique des conventions nouvelles sur les organismes non signataires et non adhérents volontaires, y compris les conventions nouvelles de mutualisation financière.",
    ],
)

answers = [answer4, answer6, answer7, answer8]
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answers)} articles')
