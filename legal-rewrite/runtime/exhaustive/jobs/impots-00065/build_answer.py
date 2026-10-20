import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

S = json.loads(Path('source.json').read_text())
R = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in S}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


def paragraphs(*ps):
    return '\n'.join('<p>' + p + '</p>' for p in ps)


def base(number, proposed, reason, review, classification, assessment, scope, burdens):
    s = by_number[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=review,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        a['classification'] = 'retained_necessary'
    a['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=scope,
        new_burdens_review=burdens, effects=[])
    answers[number] = a
    return a


def repeal(a, scope):
    a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=scope)


def reduction(a, *removed):
    a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=list(removed))


def effect(a, kind, measure, description, before, after, unit, population, transition, replacement, sq, pq):
    assert len(sq) >= 12 and sq in plain(by_number[a['number']]['source_xml']), (a['number'], 'source quote', sq)
    assert len(pq) >= 12 and pq in plain(a['proposed_xml']), (a['number'], 'proposed quote', pq)
    a['substantive_impact']['effects'].append(dict(kind=kind, measure_id=measure,
        description=description, before=before, after=after, unit=unit,
        affected_population=population, conditions_and_transition=transition,
        replacement_or_new_burdens=replacement, source_quote=sq, proposed_quote=pq))


NO_NEW = "Aucune charge nouvelle n'est identifiée : aucun prélèvement, formulaire, registre, agrément ou délai de remplacement n'est créé. Les seules obligations anciennes conservées servent les créances antérieures et leurs recours ; le solde de l'ensemble des codes n'est pas chiffré."

p = paragraphs(
    "Le présent article est abrogé pour les acquisitions de titres réalisées à compter de l'entrée en vigueur de la loi portant cette abrogation. Aucune taxe sur les acquisitions de titres n'est due sur le fondement du présent article pour ces acquisitions, y compris lorsqu'elles résultent d'un contrat conclu antérieurement. Cette suppression s'applique également aux titres représentant des titres de capital.",
    "Pour ces acquisitions, aucune liquidation, déclaration, transmission d'informations, désignation d'adhérent, autorisation de prélèvement, comptabilité séparée ou remise de rapport ne peut être exigée sur le seul fondement du présent article ou d'un renvoi à celui-ci. Les obligations autonomes de tenue de compte, de règlement-livraison, de surveillance des marchés et de lutte contre la fraude demeurent applicables.",
    "Pour l'application du d du II de l'article 726, demeurent exonérées des perceptions mentionnées aux 1° et 1° bis du I de cet article les acquisitions qui auraient été taxées en application du présent article selon ses règles de champ et d'exonération en vigueur la veille de la présente abrogation, appréciées pour l'opération concernée. Cette exonération reste ouverte aux opérations futures et n'est subordonnée à aucune liquidation, déclaration ou paiement de la taxe supprimée. Les autres exonérations de droits d'enregistrement restent applicables dans leur champ propre.",
    "Les acquisitions réalisées avant cette entrée en vigueur restent régies par les dispositions qui leur étaient applicables, notamment leurs exclusions et les neuf catégories d'exonération du II, leurs règles d'assiette, de taux, de liquidation, de déclaration, de paiement, de contrôle, de prescription et de recours. Les régularisations et restitutions légalement ouvertes restent possibles, y compris lorsque l'imputation sur une taxe ultérieure n'est plus possible ; aucune somme ne peut être imputée ou restituée deux fois. La présente abrogation n'ouvre pas de droit général à restitution des taxes légalement dues.",
    "Les sanctions relatives aux obligations antérieures restent soumises aux règles d'application dans le temps de la loi répressive plus douce. Aucun renvoi au présent article ni aucune disposition réglementaire prise pour son application ne peut rétablir la taxe ou les formalités exclusivement liées aux acquisitions réalisées à compter de cette entrée en vigueur.")
a = base('235 ter ZD', p,
    "Réforme de fond : suppression intégrale, pour les acquisitions nouvelles, de la taxe de 0,4 % sur la valeur d'acquisition des titres entrant dans son champ et de son circuit fiscal de collecte. La surveillance des marchés n'exige pas de conserver ce prélèvement fiscal national ; les obligations financières autonomes restent distinctes. Les neuf exonérations et les droits de restitution demeurent pour les acquisitions anciennes. Pour les acquisitions futures, la taxe disparaît pour tous, sans substitution ni extension d'assiette, de sorte qu'aucun bénéficiaire d'exonération ne perd cet avantage.",
    "La source est intégralement lue, I à XIII, sans tableau ni note jointe. Le seuil d'un milliard au 1er décembre et les renvois financiers ne deviennent pas des obligations nouvelles. ABROGE_DIFF et valid_until au 1er janvier 2027 signalent une fin de version, sans note permettant d'en déduire une abolition économique : identifier la recodification éventuelle dans le CIBS et sa loi d'entrée en vigueur, hors du présent lot, pour empêcher une renaissance autonome. Nouveau renvoi au d du II de CGI 726, cible non fournie dans reference-targets mais lue intégralement dans le corpus public : ce d exonère les opérations effectivement taxées de perceptions à 0,1 % ou 3 %. La proposition maintient expressément cette exemption pour les futures opérations qui auraient été taxées, sans taxe fictive à liquider, et laisse les autres exonérations de 726 intactes ; une réécriture corrélative de 726 reste nécessaire dans son lot. Autres coordinations identifiées : CGI 1736 et 1788 C ; annexe III 58 Q, 58 R et 406 terdecies. Ces textes ne sont pas modifiés ici. Les garanties de confidentialité et de conservation des données déjà collectées subsistent sur leurs fondements propres. Pas de recette compensatrice ni de chiffrage national. Le texte ne modifie pas les règles de l'Union sur les marchés ou les abus de marché.",
    'material_reduction',
    "La comparaison avec les treize subdivisions de la source établit le retrait du prélèvement de 0,4 % et des tâches exclusivement fiscales portant sur les acquisitions nouvelles. Ce n'est ni un report du paiement ni une simple coordination de renvoi.",
    "Acquisitions antérieures, autres droits d'enregistrement et surveillance financière restent hors de la coupe. La fin de version 2027 et ses éventuels successeurs hors corpus appellent une coordination distincte ; le rendement et le solde public net ne sont pas établis.", NO_NEW)
repeal(a, "Taxe de 0,4 % sur les acquisitions de titres du I, ainsi que ses déclarations, transmissions, prélèvements, comptes et rapports exclusivement fiscaux, pour les acquisitions à compter de l'entrée en vigueur ; créances et avantages anciens conservés.")
a['benefit_review'] = "Les neuf avantages du II ont été examinés : émissions et prise ferme (1°), compensation et dépôt central (2°), tenue de marché et ses trois branches (3°), contrats de liquidité admis (4°), acquisitions intragroupe et restructurations 210 A/210 B (5°), cessions temporaires (6°), FCPE, SICAV d'actionnariat salarié et acquisitions directes des salariés (7°), rachats destinés aux adhérents PEE (8°), obligations échangeables ou convertibles (9°). Ils restent applicables sans restriction aux acquisitions anciennes, y compris pour les demandes futures de régularisation recevables. La dispense déclarative du 9° constatée à l'annexe III 58 Q doit aussi être conservée pour ce stock. Pour toutes les acquisitions futures, même éligibles à ces régimes, l'absence totale de la taxe rend ces exonérations sans objet sans les remplacer par un droit équivalent. La proposition garantit expressément l'exonération du d du II de 726 pour les futures acquisitions qui auraient été taxées et maintient les autres exonérations de cet article : l'abolition ne les fait pas basculer vers 0,1 % ou 3 % de droits d'enregistrement. Les régularisations, excédents et restitutions restent ouverts, sans double emploi. Les avantages autonomes d'épargne salariale, de groupe ou de restructuration ne sont pas supprimés."
effect(a, 'tax_removed', 'transactions-financieres-taxe-suppression',
    "Suppression de la taxe d'acquisition sur les titres de capital et titres représentatifs dans son champ.",
    "0,4 % de la valeur d'acquisition ; titres admis sur un marché réglementé, émetteur français dépassant un milliard d'euros au 1er décembre précédent, titres représentatifs inclus, sous exclusions du II.",
    "Aucune taxe de cet article pour les acquisitions à compter de l'entrée en vigueur ; aucune assiette ou taxe de remplacement.",
    'percent', "Acquéreurs, opérateurs d'investissement et teneurs de compte concernés par les I et VI.",
    "Bascule à la date d'acquisition, même si le contrat est ancien ; dettes, exonérations et recours des acquisitions antérieures préservés.",
    "Aucune taxe de remplacement ; droits d'enregistrement autonomes à coordonner sans hausse.",
    "Le taux de la taxe est fixé à 0,4 %.", "Aucune taxe sur les acquisitions de titres n'est due sur le fondement du présent article pour ces acquisitions")
effect(a, 'obligation_removed', 'transactions-financieres-taxe-suppression',
    "Retrait du circuit de déclaration, centralisation, comptabilité et rapport exclusivement lié à la même taxe, sans compter une seconde taxe supprimée.",
    "Déclarations et transmissions mensuelles avant le 5 ou le 25, option annuelle, compte de collecte, comptabilité séparée et rapport annuel des VI à X.",
    "Aucune de ces tâches fiscales pour les acquisitions nouvelles ; seules les tâches nécessaires aux acquisitions anciennes demeurent.",
    'legal_duty', "Redevables, acquéreurs sans opérateur, adhérents et dépositaires centraux.",
    "Acquisitions réalisées dès l'entrée en vigueur ; les informations anciennes restent protégées et disponibles pour les contrôles légalement ouverts.",
    "Pas de déclaration, rapport ou registre de remplacement ; surveillance financière autonome maintenue.",
    "Un rapport annuel est remis à l'administration sur la nature et l'ampleur des contrôles mis en œuvre.",
    "aucune liquidation, déclaration, transmission d'informations, désignation d'adhérent, autorisation de prélèvement, comptabilité séparée ou remise de rapport ne peut être exigée")


p = paragraphs(
    "Le présent article est abrogé pour les ordres, modifications et annulations transmis à compter de l'entrée en vigueur de la loi portant cette abrogation. Aucune taxe sur les opérations à haute fréquence n'est due sur le fondement du présent article à raison de ces événements, même lorsque l'ordre initial a été transmis avant cette date.",
    "Pour la journée de bourse au cours de laquelle intervient cette entrée en vigueur, seuls les ordres transmis antérieurement à celle-ci et leurs modifications ou annulations antérieures sont retenus dans les calculs de la taxe. Les ordres, modifications et annulations postérieurs sont exclus de l'assiette et du calcul du taux d'annulation ou de modification.",
    "Aucune déclaration, liquidation ou information exclusivement nécessaire à cette taxe n'est exigée pour les opérations ainsi exclues. Les obligations autonomes de surveillance des opérations algorithmiques, de prévention des abus de marché et de sécurité des marchés restent applicables.",
    "Les opérations antérieures restent soumises aux règles qui leur étaient applicables, notamment les exclusions des dispositifs d'optimisation, d'acheminement et de confirmation des ordres, l'exonération de tenue de marché définie par le 3° du II de l'article 235 ter ZD dans sa rédaction applicable à ces opérations, les seuils, les règles de déclaration, de paiement, de contrôle, de restitution, de prescription et de recours. Aucune restitution générale de la taxe légalement due n'est créée. Les sanctions restent soumises aux règles d'application dans le temps de la loi répressive plus douce.")
a = base('235 ter ZD bis', p,
    "Réforme de fond : retrait du prélèvement national de 0,01 % sur les ordres annulés ou modifiés au-delà du seuil quotidien et des rubriques déclaratives qui lui sont propres. Les règles financières autonomes assurant la sécurité et l'intégrité des marchés sont expressément réservées. Les dispositifs exclus et l'exonération de tenue de marché restent protégés pour les opérations anciennes ; aucun ordre nouveau ne supporte la taxe. Le renvoi à 235 ter ZD est figé au droit applicable aux anciennes opérations pour ne pas perdre cette exonération lors de son abrogation.",
    "Source I à VII et note d'application aux déclarations du 1er février 2014 lues. Les maxima et minima législatifs sont respectivement une seconde et deux tiers ; l'annexe III 58 S lue fixe une demi-seconde et 80 %. Ils ne constituent pas de nouveaux seuils proposés. La coupure intrajournalière exclut les événements nouveaux au lieu de les utiliser pour créer une dette après abolition. Le marqueur ABROGE_DIFF/2027 n'est pas une preuve de suppression économique : successeur éventuel du CIBS à identifier et coordonner hors lot. Annexe III 58 S et supports TVA à coordonner, sans supprimer la déclaration TVA générale. La fiscalité de la société au titre de 209 ne conditionne plus la suppression de cette taxe. Aucun changement des règles européennes de marché n'est présumé.",
    'material_reduction',
    "Le prélèvement de 0,01 % et son calcul fiscal sur les opérations futures sont réellement supprimés. La préservation des contrôles de marché ne recrée pas le circuit fiscal supprimé.",
    "Les opérations anciennes, les autres taxes financières et les contraintes européennes de négociation restent distinctes. Un éventuel transfert légal vers le CIBS après cette version n'est pas déclaré traité ; aucun rendement n'est évalué.", NO_NEW)
repeal(a, "Taxe de 0,01 % sur les ordres à haute fréquence annulés ou modifiés dépassant le seuil quotidien et obligations exclusivement liées, pour les événements nouveaux ; maintien des dettes, exclusions et exonérations anciennes.")
a['benefit_review'] = "Bien que le signalement ne soit pas obligatoire, les exclusions des systèmes d'optimisation, d'acheminement et de confirmation et l'exonération de tenue de marché du III restent applicables aux faits anciens, sous le renvoi historique explicite à 235 ter ZD II 3°. Le seuil réglementaire de 80 % conserve son effet favorable dans ces calculs. Pour les nouveaux événements, la taxe entière disparaît et aucune taxe équivalente ne remplace ces avantages."
effect(a, 'tax_removed', 'haute-frequence-taxe-suppression',
    "Suppression de la taxe sur les ordres à haute fréquence annulés ou modifiés.",
    "0,01 % du montant des ordres annulés ou modifiés au-delà du seuil quotidien (80 % selon annexe III 58 S), pour les entreprises exploitées en France ; tenue de marché et systèmes exclus hors champ.",
    "Aucune taxe du présent article sur les ordres et événements nouveaux ; événements anciens seuls dans l'éventuelle journée mixte.",
    'percent', "Entreprises exploitées en France opérant pour compte propre au moyen de dispositifs automatisés.",
    "Entrée en vigueur de la loi, avec séparation des événements de la journée de bascule ; dettes et recours anciens conservés.",
    "Aucune taxe ou rubrique fiscale de remplacement ; règles autonomes de marché maintenues.",
    "la taxe due est égale à 0,01 % du montant des ordres annulés ou modifiés excédant ce seuil.",
    "Aucune taxe sur les opérations à haute fréquence n'est due sur le fondement du présent article à raison de ces événements")


p = paragraphs(
    "Le présent article est abrogé pour le produit des primes ou cotisations additionnelles relatives à la garantie contre le risque de catastrophes naturelles encaissé à compter de l'entrée en vigueur de la loi portant cette abrogation, y compris lorsque le contrat d'assurance a été conclu avant cette date. Aucun prélèvement de 12 % n'est dû sur ce produit en application du présent article.",
    "Aucune liquidation, déclaration ou information exclusivement nécessaire à ce prélèvement n'est exigée au titre de ce produit. Les garanties d'assurance contre les catastrophes naturelles, les primes ou cotisations additionnelles qui les financent et les obligations des assureurs envers les assurés demeurent régies par leurs dispositions propres.",
    "Le produit encaissé avant cette entrée en vigueur reste soumis aux règles antérieurement applicables de liquidation, de déclaration, de recouvrement, de contrôle, de restitution, de prescription et de recours. Pour l'année de la bascule, seul ce produit entre dans l'assiette du prélèvement. La taxe distincte prévue à l'article 991 et ses avantages ne sont pas supprimés par le présent article. Aucune restitution générale du prélèvement légalement dû n'est créée. Les sanctions restent soumises aux règles d'application dans le temps de la loi répressive plus douce.")
a = base('235 ter ZE', p,
    "Réforme de fond : suppression du prélèvement accessoire de 12 % sur le produit des surprimes de catastrophes naturelles encaissé à compter de l'entrée en vigueur. Le financement fiscal est retiré, sans supprimer la garantie d'assurance ni les obligations d'indemnisation. La règle de bascule est explicitement l'encaissement, contrats anciens compris, et non une exonération limitée aux nouveaux souscripteurs. Les dettes sur les encaissements antérieurs et leurs recours sont conservés.",
    "Les deux subdivisions et la note d'entrée en vigueur au 1er janvier 2021 sont lues. Aucune date future de promulgation n'est déduite de cette note. L.125-2 assurances et 991 CGI ne servent plus à collecter ce seul prélèvement sur les produits nouveaux ; ils conservent leurs objets autonomes. L'affectation et le financement public de la prévention des risques doivent être coordonnés dans les lois financières et, le cas échéant, les dispositions relatives au fonds de prévention des risques naturels majeurs ; leur texte intégral n'est pas fourni ici et leur réécriture n'est pas revendiquée. La suppression n'établit pas une diminution automatique de 12 % de la prime payée par chaque assuré : assiette de la taxe et tarification contractuelle sont distinctes. Besoin public de financement et effet net à chiffrer, sans compensation inventée.",
    'material_reduction',
    "Le prélèvement annuel de 12 % est retiré sur les produits futurs, et non simplement payé plus tard. Le gain légal est celui de l'assureur redevable ; sa répercussion sur les primes des assurés n'est pas démontrée.",
    "La garantie de catastrophes naturelles, les surprimes contractuelles et la taxe autonome 991 subsistent. Le financement des actions publiques reste à coordonner hors lot ; le solde consolidé et la répercussion économique sont inconnus.", NO_NEW)
repeal(a, "Prélèvement annuel de 12 % sur le produit des primes et cotisations additionnelles de catastrophes naturelles encaissé dès l'entrée en vigueur, avec retrait des seules formalités correspondantes ; encaissements antérieurs et garanties d'assurance préservés.")
effect(a, 'tax_removed', 'catastrophes-naturelles-prelevement-suppression',
    "Suppression du prélèvement sur les surprimes de catastrophes naturelles, distinct de la prime d'assurance et de la taxe 991.",
    "12 % du produit des primes ou cotisations additionnelles de L.125-2 assurances, versés par les entreprises d'assurance.",
    "Aucun prélèvement de cet article sur le produit encaissé à compter de l'entrée en vigueur, même sous contrat antérieur.",
    'percent', "Entreprises d'assurance redevables ; aucun gain contractuel automatique affirmé pour les assurés.",
    "Produit ancien conservé dans l'assiette de l'année mixte ; créances, restitutions et recours anciens maintenus.",
    "Aucun impôt ou formulaire de remplacement ; financement public autonome à coordonner.",
    "Le taux de ce prélèvement est fixé à 12 %.",
    "Aucun prélèvement de 12 % n'est dû sur ce produit en application du présent article.")


p = paragraphs(
    "Le présent article est abrogé pour les faits générateurs intervenant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant cette abrogation. Aucune taxe pour le financement du fonds de soutien aux collectivités territoriales, y compris sa contribution additionnelle calculée sur base sociale ou sous-consolidée, n'est due sur le fondement du présent article à raison de l'activité exercée à compter de cette date.",
    "Aucune déclaration, liquidation, transmission d'appel à contribution ou information exclusivement nécessaire à cette taxe n'est exigée pour ces faits générateurs. Les exigences prudentielles, les contributions autonomes et les pouvoirs de contrôle de l'Autorité de contrôle prudentiel et de résolution demeurent régis par leurs dispositions propres.",
    "Pour les faits générateurs antérieurs, les dispositions applicables à leur date restent en vigueur pour la liquidation, les déclarations, les rectifications d'assiette, le recouvrement, le contrôle, les prescriptions et les recours. Elles conservent notamment les exclusions des personnes établies dans un autre Etat de l'Espace économique européen opérant exclusivement par succursale ou libre prestation de services, le seuil de 500 millions d'euros, l'exclusion de l'Agence française de développement, les exclusions et diminutions d'assiette évitant un cumul entre bases sociales et consolidées et les droits à restitution en cas de révision à la baisse. Ces droits restent exerçables après la présente abrogation dans leurs délais propres, sans restitution générale ni double restitution.",
    "L'abrogation ne remet pas en cause les aides, conventions et engagements valablement accordés au titre du fonds de soutien créé par l'article 92 de la loi n° 2013-1278 du 29 décembre 2013 de finances pour 2014, ni les droits des situations futures qui restent éligibles selon les règles propres à ce fonds. Elle ne proroge aucune période d'imposition et ne rétablit aucune taxe déjà supprimée. Les sanctions restent soumises aux règles d'application dans le temps de la loi répressive plus douce.")
a = base('235 ter ZE bis', p,
    "Réforme de fond : suppression anticipée de cette taxe sectorielle assise sur les exigences minimales en fonds propres et de sa composante additionnelle, à partir du prochain fait générateur annuel après la loi. La taxe finance un fonds ; elle ne constitue pas l'exigence prudentielle elle-même. La suppression laisse cette exigence et les engagements d'aide autonomes en place. Les exonérations, le seuil de 500 millions et les mécanismes anti-cumul sont maintenus pour toutes les années anciennes, avec leurs rectifications et remboursements, y compris futurs et recevables.",
    "Source I à VIII lue intégralement. Son III écrit littéralement « 0,05 05 % » pour 2026 à 2028 : graphie non normalisée signalée, sans fixer un taux intermédiaire ni corriger silencieusement l'ancien calcul. La note cite une abrogation au 1er janvier 2029 par l'article 26 II E de la loi 2014-1655, tandis que valid_until/ABROGE_DIFF donne 2027 : conflit de calendrier de version à confronter à une éventuelle recodification, pas preuve de suppression économique en 2027. La proposition n'autorise aucune prolongation d'une abolition antérieure. Coordonner la loi 2013-1278 article 92, la loi 2014-1655 article 26 II E et les éventuelles dispositions de transfert au CIBS, hors lot ; préserver aides et engagements sans recette de remplacement inventée. CGI 39, 1, 4° et V.3 du présent article conservent la non-déductibilité des dettes anciennes : aucun remboursement d'IS automatique. Distinguer coût brut de la taxe, financement du fonds et effet net ; aucun rendement n'est fourni.",
    'material_reduction',
    "La charge fiscale sur les fonds propres réglementaires et son circuit annuel disparaissent pour les faits générateurs nouveaux. Les ratios prudentiels ne sont pas supprimés et aucune seconde réduction n'est imputée à leurs renvois.",
    "Faits générateurs au 1er janvier antérieur à la bascule, même si les paiements ou rectifications sont ultérieurs, restent couverts par le droit ancien. Le calendrier de recodification et le financement des aides hors lot restent à coordonner ; aucun solde budgétaire n'est démontré.", NO_NEW)
repeal(a, "Taxe annuelle sur les exigences minimales en fonds propres des établissements financiers et composante additionnelle sur base sociale ou sous-consolidée, pour les faits générateurs dès le 1er janvier suivant la loi, sans supprimer les aides ni les régimes prudentiels.")
a['benefit_review'] = "Les trois exclusions du I.2 sont maintenues pour les faits anciens : établissements EEE intervenant exclusivement par succursale ou libre prestation de services, exigences minimales inférieures à 500 millions d'euros et Agence française de développement. Les exclusions de contribution additionnelle et la minoration de l'assiette consolidée empêchant une double perception au II restent également applicables. Les demandes de restitution après révision à la baisse conservent les deux délais d'un mois du VII.3 ; les conventions d'aide valablement accordées restent protégées. Pour les années nouvelles, aucune personne de ces catégories ne devient imposable : la taxe entière disparaît sans remplacement, les garanties prudentielles étant distinctes."
effect(a, 'tax_removed', 'fonds-soutien-collectivites-taxe-suppression',
    "Abolition prospective de la taxe finançant le fonds de soutien, composante additionnelle comprise.",
    "Assiette : exigences minimales en fonds propres sociales ou consolidées, sous seuil de 500 millions et exclusions. Taux source : 0,0642 % en 2016-2025 et « 0,05 05 % » en 2026-2028, graphie à contrôler.",
    "Aucune taxe ni contribution additionnelle du présent article sur les faits générateurs nouveaux ; pas de base ou de taux de remplacement.",
    'percent', "Etablissements financiers relevant du I, à l'exclusion des catégories exonérées.",
    "Bascule au 1er janvier suivant l'entrée en vigueur, sans proroger une suppression déjà intervenue ; dettes annuelles anciennes, rectifications et restitutions conservées.",
    "Aucune nouvelle formalité fiscale ; exigences prudentielles et aides autonomes préservées.",
    "Le taux de la taxe est fixé à 0,0642 % pour les années 2016 à 2025 et à 0,05 05 % pour les années 2026 à 2028.",
    "Aucune taxe pour le financement du fonds de soutien aux collectivités territoriales, y compris sa contribution additionnelle calculée sur base sociale ou sous-consolidée, n'est due")


p = paragraphs(
    "Le présent article est abrogé pour les opérations dont le fait générateur de la taxe d'archéologie préventive intervient à compter de l'entrée en vigueur de la loi portant cette abrogation. La taxe d'archéologie préventive de 0,40 % n'est pas due pour ces opérations, y compris lorsqu'une demande d'autorisation ou une déclaration préalable a été déposée antérieurement.",
    "Pour l'application du premier alinéa, sans préjudice de l'avant-dernier alinéa de l'article L. 524-4 du code du patrimoine, la date du fait générateur reste celle déterminée par le I de l'article 1635 quater F. La seule modification d'une autorisation antérieure ou l'achèvement ultérieur des travaux ne transforme pas un fait générateur antérieur en fait générateur nouveau.",
    "Aucune déclaration ni donnée exclusivement nécessaire à la taxe supprimée ne peut être exigée pour les opérations nouvelles. La taxe d'aménagement, ses exonérations et abattements, les autorisations d'urbanisme, les prescriptions de protection du patrimoine et les diagnostics et opérations archéologiques légalement requis conservent leur régime propre. La redevance d'archéologie préventive relevant du code du patrimoine n'est pas supprimée par le présent article.",
    "Les opérations dont le fait générateur est antérieur restent soumises aux règles qui leur étaient applicables, même lorsque l'achèvement ou le recouvrement est postérieur. Sont notamment conservés les exonérations du III, les abattements et règles favorables d'assiette des articles 1635 quater H à 1635 quater K, les règles favorables résultant d'un certificat d'urbanisme, la déduction de la redevance d'archéologie préventive antérieurement acquittée dans les conditions du dernier alinéa du VIII et les droits à dégrèvement, restitution et recours. Les demandes futures recevables portant sur ces opérations restent ouvertes. Une même somme ne peut être déduite ou restituée deux fois.",
    "Les dispositions antérieures continuent de régir les déclarations, la liquidation, les titres de perception, le recouvrement, le contrôle et les prescriptions relatifs à ces opérations anciennes. La présente abrogation ne crée ni restitution générale des taxes légalement dues ni remboursement d'une redevance légalement due du seul fait qu'aucune taxe nouvelle n'est exigible. Les sanctions restent soumises aux règles d'application dans le temps de la loi répressive plus douce.")
a = base('235 ter ZG', p,
    "Réforme de fond : suppression de la taxe d'archéologie préventive de 0,40 % pour les nouveaux faits générateurs et des données qui ne servent qu'à cette taxe. Elle retire un prélèvement sur la construction sans retirer les diagnostics et protections du patrimoine. La date de bascule reste le fait générateur légal, non la date ultérieure d'achèvement ou de paiement, ce qui évite une extinction implicite du stock. Les exonérations et déductions anciennes restent pleinement exerçables et la taxe d'aménagement conserve tous ses avantages pour les opérations futures.",
    "Les huit subdivisions et la note d'application au 1er janvier 2024 sont lues. Lecture complémentaire entière dans le corpus : 1635 quater F et H à K, annexe III 54 et 344 N. Coordination requise de 1691 bis, 1679 octies, annexe III 54/344 N et LPF L.255 A pour séparer stock ancien, taxe supprimée et taxe d'aménagement conservée ; ces textes ne sont pas réécrits ici. L.524-4 patrimoine est un renvoi déjà présent dans la source, non une nouvelle cible : son champ spécial n'est pas inventé ni abrogé. Le financement de l'archéologie, les redevances du patrimoine et les règles européennes ou internationales de protection nécessitent leurs coordinations propres hors des cinq codes ; aucune recette compensatrice ni suppression de prescription de fouille n'est présumée. Les numéros 1635 quater F et H à K étaient déjà fournis par la source et ont été lus, mais ne font pas partie des reference_checks imposés. Le taux de 0,40 % porte sur la valeur fiscale de l'ensemble immobilier, pas sur le coût réel de chaque chantier.",
    'material_reduction',
    "La taxe de 0,40 % et ses rubriques exclusivement fiscales sont supprimées pour les nouveaux faits générateurs. L'avantage est fiscal ; il ne dispense pas de protéger le patrimoine ni de payer une redevance autonome.",
    "Le stock ancien et les prélèvements du code du patrimoine demeurent. Les données communes à la taxe d'aménagement restent nécessaires ; aucun gain sur ces données n'est compté. Coût du service archéologique et solde public non chiffrés.", NO_NEW)
repeal(a, "Taxe d'archéologie préventive de 0,40 % et obligations déclaratives exclusivement correspondantes pour les opérations à fait générateur nouveau ; exonérations et déduction de redevance anciennes, taxe d'aménagement et protection du patrimoine conservées.")
a['benefit_review'] = "Le III renvoie aux 1° à 4° et 8° à 11° du I de 1635 quater D : services publics ou utilité publique, logements et hébergements sociaux, surfaces agricoles, centres équestres, aménagements de prévention des risques, reconstructions éligibles, constructions d'au plus 5 m² et stationnements intégrés. S'y ajoute l'exonération des câbles sous-marins d'information ; les conditions européennes ou de SIEG des catégories 2° à 4° demeurent pour les anciennes opérations. Les abattements de 50 % de 1635 quater I (logements éligibles, cent premiers m² d'habitation principale sans cumul, locaux industriels/artisanaux, entrepôts et stationnements commerciaux et transformations éligibles sans cumul), les valeurs forfaitaires, les arrondis favorables et la stabilisation plus favorable par certificat d'urbanisme sont préservés dans le stock. La déduction sur demande de la redevance déjà acquittée au VIII demeure, même pour une réclamation future recevable, sans double remboursement. Pour les faits générateurs futurs, la taxe entière disparaît sans taxe équivalente ni élargissement de la taxe d'aménagement ; tous ces bénéficiaires restent donc au moins aussi favorisés au regard du prélèvement supprimé. Les exonérations de la taxe d'aménagement, y compris OIN, ZAC et PUP non visées par le III de cet article, restent autonomes pour les opérations futures. La redevance patrimoniale ne devient pas remboursable du seul fait de l'abolition de la taxe."
effect(a, 'tax_removed', 'archeologie-preventive-taxe-suppression',
    "Suppression de la taxe fiscale de construction d'archéologie préventive, distincte de la redevance patrimoniale.",
    "0,40 % de la valeur fiscale de l'ensemble immobilier déterminée par 1635 quater H à K, pour les opérations du I affectant le sous-sol, sous exonérations et abattements.",
    "Aucune taxe du présent article pour les faits générateurs dès l'entrée en vigueur ; taxe d'aménagement et redevance autonome non augmentées par ce texte.",
    'percent', "Personnes réalisant les constructions et aménagements du I, y compris dans le domaine maritime prévu au IV.",
    "Fait générateur légal conservé ; anciennes autorisations et faits anciens restent au droit ancien avec leurs avantages, même si l'exigibilité est postérieure.",
    "Pas de taxe ou déclaration de remplacement ; données nécessaires à la taxe d'aménagement et prescriptions patrimoniales maintenues.",
    "Son taux est égal à 0,40 %.", "La taxe d'archéologie préventive de 0,40 % n'est pas due pour ces opérations")


s = by_number['235 quater']['source_xml']
p = s.replace(
    "L'imposition mentionnée au premier alinéa du présent II est établie, contrôlée et recouvrée comme l'impôt sur les sociétés et sous les mêmes garanties et sanctions.",
    "L'imposition mentionnée au premier alinéa du présent II est établie, contrôlée et recouvrée comme l'impôt sur les sociétés et sous les mêmes garanties et sanctions, sous réserve du IV du présent article. Ce renvoi procédural ne modifie ni les règles d'assiette et de taux définies au premier alinéa du présent II ni les causes de fin de report et les dates d'exigibilité définies au V. Il ne subordonne pas cette imposition distincte à une distribution par le bénéficiaire.")
p = p.replace(
    "Un état de suivi des revenus et profits dont l'imposition est reportée en application du premier alinéa du II est joint en annexe des déclarations mentionnées au III et au premier alinéa du présent IV sur un formulaire conforme au modèle établi par l'administration.",
    "Le suivi des revenus et profits dont l'imposition est reportée en application du premier alinéa du II est intégré aux déclarations mentionnées au III et au premier alinéa du présent IV. Aucun état annexé distinct ni formulaire exclusif n'est exigé ; le bénéficiaire peut utiliser tout support comportant les informations nécessaires à ce suivi. Une même information n'est fournie qu'une fois pour une même déclaration.")
p = p.replace(
    "Lorsque le bénéficiaire n'a pas déposé la déclaration ou l'état mentionnés aux deux premiers alinéas du présent IV dans le délai prévu au premier alinéa ou a déposé une déclaration ou un état incomplets, l'administration fiscale lui adresse une mise en demeure de respecter les obligations déclaratives qui lui incombent en application du présent IV dans un délai de trente jours, en précisant, le cas échéant, les compléments déclaratifs requis. Le non-respect des obligations déclaratives à l'issue de cette mise en demeure entraîne la fin du report d'imposition en application du 3° du V.",
    "Lorsque le bénéficiaire n'a pas déposé la déclaration mentionnée au premier alinéa du présent IV dans le délai qui y est prévu ou a déposé une déclaration incomplète, y compris pour les informations de suivi prévues au deuxième alinéa, l'administration fiscale lui adresse une mise en demeure de respecter ses obligations déclaratives dans un délai de trente jours, en précisant, le cas échéant, les compléments requis. Le non-respect des obligations déclaratives à l'issue de cette mise en demeure entraîne la fin du report d'imposition en application du 3° du V.")
p = p.replace(
    "Le fait, pour le bénéficiaire, de satisfaire à ses obligations déclaratives à la suite de la réception de la mise en demeure prévue au troisième alinéa du présent IV et dans le délai de trente jours prévu par celle-ci entraîne l'application d'une amende, due par le bénéficiaire, égale à 5 % des impositions placées en report à la date du manquement mentionné au même troisième alinéa.",
    "Aucune amende propre au présent article n'est due au seul motif que le bénéficiaire régularise sa déclaration dans les trente jours suivant la réception de la mise en demeure prévue au troisième alinéa du présent IV. Les sanctions légalement applicables à des faits distincts de fraude demeurent réservées.")
p = p.replace("de la mise en demeure mentionnée au dernier alinéa du même IV", "de la mise en demeure mentionnée au troisième alinéa du même IV")
p += paragraphs(
    "VI.-Les dispositions du IV relatives au support unique et à l'absence d'amende de régularisation s'appliquent aux déclarations et compléments déposés à compter de l'entrée en vigueur de la loi portant leur modification, y compris pour des reports antérieurs. Les déclarations et états déjà régulièrement déposés ne sont pas à refaire. Les sanctions antérieures restent soumises aux règles d'application dans le temps de la loi répressive plus douce ; aucun délai de réclamation ou de report expiré n'est rouvert du seul fait de cette modification.")
a = base('235 quater', p,
    "Réforme de fond ciblée : le suivi de l'imposition reportée est intégré aux déclarations initiale et annuelles, sans état annexe distinct ni formulaire imposé ; l'amende de 5 % frappant une régularisation dans les trente jours est supprimée. La preuve d'un déficit à chaque exercice reste nécessaire pour le report : l'identité, les conditions territoriales, la base historique, les six mois, la mise en demeure et la fin du report en cas de bénéfice ou de défaut persistant sont conservés. Coordination nécessaire du V.3, qui visait à tort le dernier alinéa du IV au lieu de son troisième alinéa. Le renvoi procédural à l'IS ne transforme pas cette imposition de non-résident en IS à la distribution.",
    "Lecture complète des I à V et de la note d'application aux retenues dont le fait générateur intervient dès le 1er janvier 2022. Les I, III et les causes et plafonds matériels du V sont conservés, y compris transfert des déficits, dégrèvement lors d'une dissolution sans transfert si dernier résultat déficitaire, plafond au bénéfice, exigibilité et priorité aux impositions anciennes. Au V.3, incohérence préexistante du renvoi à « dernier alinéa » : corrigée vers le troisième, sans déplacement des quatre alinéas du IV. Les déclarations annuelles ne reconstituent pas un IS ordinaire sur des bénéfices conservés : elles servent un régime distinct de restitution/report de retenues françaises. Adapter le modèle administratif de suivi et les éventuelles instructions de procédure hors de ce lot ; ne pas rétablir l'état séparé ni l'amende par renvoi au II. Aucune suppression des conventions d'assistance, des garanties européennes ou des recours. Coût de suppression de l'amende non chiffré.",
    'material_reduction',
    "Deux contraintes propres à la source sont retirées : le support de suivi obligatoirement annexé sur modèle exclusif et l'amende automatique de 5 % malgré régularisation dans les trente jours. Le report et ses conditions matérielles ne sont ni un nouvel avantage inventé ni une réduction du taux des retenues.",
    "Le contenu utile du suivi, la demande initiale, la déclaration de déficit à six mois et la déchéance après mise en demeure infructueuse demeurent. Aucun gain budgétaire ou gain sur le montant final des retenues n'est démontré ; le stock définitivement clos n'est pas rouvert.",
    "Aucune charge nouvelle n'est identifiée : le suivi déjà exigé est intégré au support existant, sans nouvelle donnée ni nouvel accès à des fichiers ; les six mois et trente jours restent identiques. La précision procédurale et la transition ne créent aucun paiement de remplacement.")
reduction(a,
    "Obligation de joindre un état de suivi distinct sur formulaire administratif exclusif aux déclarations initiale et annuelles du report.",
    "Obligation d'acquitter l'amende propre de 5 % des impositions en report malgré régularisation dans les trente jours de la mise en demeure.")
a['benefit_review'] = "La restitution initiale et le report demeurent ouverts aux personnes morales et organismes déficitaires remplissant le I, y compris les bénéficiaires de certains Etats tiers pour 119 bis. La reprise limitée au bénéfice, la continuation en cas de transfert des déficits à l'absorbante et le dégrèvement sans transfert lorsque le dernier résultat est déficitaire sont intégralement préservés. Les situations futures éligibles bénéficient du même régime et du support allégé ; les reports en cours bénéficient aussi de la suppression de l'amende de régularisation. Aucun taux de retenue ou plafond favorable n'est relevé."
effect(a, 'obligation_merged', 'non-residents-report-suivi-integre',
    "Fusion du support annuel ou initial de suivi avec la déclaration de restitution/report correspondante.",
    "Déclaration plus état de suivi annexé distinct sur formulaire conforme au modèle de l'administration, au III et IV.",
    "Même contenu nécessaire dans une seule déclaration ; aucun état distinct ni formulaire exclusif.",
    'legal_duty', "Bénéficiaires non résidents de revenus et profits français placés en restitution/report selon le I.",
    "Dépôts futurs, reports anciens inclus ; dépôts réguliers déjà effectués non refaits, délais expirés non rouverts.",
    "Pas de nouvelle donnée, d'attestation ou de dépôt supplémentaire ; données de suivi utiles conservées.",
    "Un état de suivi des revenus et profits dont l'imposition est reportée en application du premier alinéa du II est joint en annexe des déclarations",
    "Aucun état annexé distinct ni formulaire exclusif n'est exigé")
effect(a, 'obligation_removed', 'non-residents-amende-regularisation-suppression',
    "Suppression de l'obligation d'acquitter l'amende spéciale de régularisation ; il s'agit d'une sanction accessoire et non du taux de l'impôt principal.",
    "Amende automatique de 5 % du montant des impositions placées en report à la date du manquement, même si régularisation sous trente jours.",
    "Aucune amende pour cette régularisation sous trente jours ; principal et fraude distincte inchangés.",
    'percent', "Bénéficiaires régularisant dans le délai de la mise en demeure du IV.",
    "Dépôts futurs et règle répressive plus douce dans son champ ; pas de remboursement général de sanctions définitives décidé.",
    "Aucune pénalité spécifique de remplacement ; déchéance pour défaut persistant et fraude distincte demeurent.",
    "une amende, due par le bénéficiaire, égale à 5 % des impositions placées en report à la date du manquement",
    "Aucune amende propre au présent article n'est due au seul motif que le bénéficiaire régularise sa déclaration dans les trente jours")


a = base('235 quinquies', None,
    "Maintien intégral nécessaire, sans reformulation : l'article ouvre une restitution sur base nette aux personnes morales et organismes non résidents, pour éviter une retenue définitive sur des charges qui seraient déductibles en France. Les trois conditions territoriale, de déductibilité et de non-imputation étrangère préviennent les doubles avantages tout en maintenant l'accès des futurs bénéficiaires éligibles. La réclamation et les seules pièces nécessaires au calcul ont une fonction probatoire concrète ; la source n'impose ni agrément, ni état annuel, ni justification sans objet identifié. Aucun doublon précis retirable n'est établi.",
    "I, ses trois conditions, II et note de 2022 lus en entier. Ne pas confondre 119 bis, 2 avec l'ensemble de 119 bis ni la restitution des frais nets avec le report pour déficit de 235 quater. La comparaison avec la déductibilité en France ne rétablit pas un fait générateur annuel d'IS : elle permet de déterminer l'assiette nette d'une retenue autonome de non-résident. La fiscalité du bénéficiaire étranger et les conventions ne sont pas supprimées par l'IS français à la distribution. La clause de pièces « nécessaires » doit s'appliquer selon les règles de réemploi légal existantes ; une simple répétition de ces règles ne serait pas une nouvelle coupe. Aucun taux, délai supplémentaire ou document de remplacement proposé.",
    'retained_necessary',
    "Le texte entier est un droit à restitution conservé : aucune baisse nouvelle n'est revendiquée. Les justificatifs sont limités au calcul d'un remboursement réel et les conditions évitent de cumuler restitution française et imputation étrangère.",
    "Le maintien ne démontre ni suppression de la retenue générale ni réduction de son taux. Les contribuables hors du champ territorial ou sans charges éligibles restent hors de ce mécanisme ; aucune extension ni estimation budgétaire n'est décidée.",
    "Aucune charge nouvelle n'est identifiée : texte source intégralement conservé, sans formulaire, donnée, registre ou délai ajouté. Les preuves nécessaires à la restitution restent exigibles selon le droit existant et ses règles de réemploi.")
a['benefit_review'] = "La restitution de la différence entre retenue brute et imposition calculée sur charges nettes d'acquisition et de conservation est conservée pour toutes les futures situations recevables : personnes morales ou organismes non transparents du champ UE/EEE et, pour 119 bis, 2, certains Etats tiers sans participation de contrôle. Les frais doivent rester déductibles s'ils étaient exposés en France et la retenue non imputable dans l'Etat de résidence ; ces limites ne sont ni durcies ni étendues. Le délai de réclamation et les justificatifs seulement nécessaires ne sont pas modifiés."


a = base('236', None,
    "Maintien intégral nécessaire de l'option favorable permettant l'immobilisation ou la déduction immédiate des dépenses de fonctionnement de recherche scientifique et technique, étendue aux logiciels. L'interdiction de reprendre dans les stocks les dépenses déjà déduites prévient une double déduction, sans formalité distincte. Le rattachement des subventions au rythme des amortissements préserve la symétrie et l'étalement existants ; leur suppression pourrait rendre les aides moins favorables ou produire un double avantage non décidé. Aucun agrément, dépôt ou délai minimal propre n'est imposé par cet article.",
    "I, I bis, alinéa disjoint et II abrogé lus. Le texte fixe des règles de résultat et une option, non un acompte ni une exigibilité annuelle d'IS. Dans le régime à la distribution, ces règles restent utiles aux bénéfices, pertes, subventions et crédits suivis selon le noyau IS ; elles ne suffisent pas à imposer les réserves ou la trésorerie conservées. L'impôt sur le revenu conserve son champ. Aucun CIR ni aide de recherche n'est supprimé par le cadre de chiffrage : il faut, pour l'évaluation seulement, distinguer autofinancement, dette, innovation, emplois, impôts et aides effectivement évitées selon des hypothèses explicites, sans compter une économie de dispositif maintenu. Aucun effet national chiffré.",
    'retained_necessary',
    "Le choix fiscal favorable et le traitement des subventions sont maintenus sans nouveau corps stylistique. L'anti-double compte des stocks a une utilité essentielle à la cohérence du bénéfice fiscal ; aucun allègement nouveau ne peut être revendiqué.",
    "Le maintien ne vaut ni suppression de l'IR, ni création d'un crédit de recherche, ni validation du chiffrage net de l'IS. L'exigibilité de l'IS à la distribution et le minimum international relèvent de leurs articles propres.",
    "Aucune charge nouvelle n'est identifiée : l'option, les dépenses éligibles et les règles de stocks et subventions restent identiques. Aucun suivi, registre, agrément, délai d'investissement ni déclaration supplémentaire n'est ajouté.")
a['benefit_review'] = "L'option de déduction immédiate ou d'immobilisation des dépenses de fonctionnement de recherche et de conception de logiciels reste ouverte aux dépenses futures éligibles, sans condition de distribution, de réinvestissement ni agrément ajouté. Le rattachement des subventions UE, institutions européennes, Etat, collectivités et établissements spécialisés aux amortissements des dépenses immobilisées reste intact, ce qui préserve l'étalement favorable. Seul le double emploi dans le coût des stocks reste exclu ; ce n'est pas un avantage autonome supprimé. Les dispositions disjointes ou abrogées ne sont pas réactivées."


s = by_number['236 bis']['source_xml']
ps = [q.strip() for q in re.split(r'<br\s*/?>', s) if q.strip()]
assert len(ps) == 5
assert '; elle est au minimum de sept mois.' in ps[0]
ps[0] = ps[0].replace(' ; elle est au minimum de sept mois.', '.')
p = paragraphs(*ps,
    "La suppression du minimum de sept mois s'applique aux opérations dont la date d'effet intervient à compter de l'entrée en vigueur de la loi portant cette suppression. En cas d'effet rétroactif, la date d'effet de l'opération remplace celle de la fusion. Les opérations dont la date d'effet est antérieure restent régies par les dispositions qui leur étaient applicables, avec leurs droits à déduction, rectification et recours.",
    "Pour les bénéfices relevant de l'impôt sur les sociétés à la distribution, les calculs de neutralisation et de réintégration prévus au présent article servent à déterminer les bénéfices imposables lors de leur distribution et les droits antérieurs conservés. Ils ne rendent pas exigible un impôt ordinaire sur les bénéfices conservés. Les droits des salariés aux congés payés, leur ancienneté et les sommes qui leur sont dues ne sont pas modifiés.")
a = base('236 bis', p,
    "Réduction de fond ciblée : retrait du minimum forfaitaire de sept mois de période fiscale neutralisée lors d'un transfert entre entreprises ayant des options différentes sur les congés payés. La période des droits réellement acquis et non utilisés et sa comparaison avec les droits non utilisés à la clôture restent entières, ainsi que la déduction réputée opérée, la réintégration différentielle et les charges sociales et fiscales. Cette coupe retire le calcul d'un plancher arbitraire, sans abroger la protection contre la double déduction. La date d'effet rétroactif reprend la règle existante de l'annexe III 49 octies A. L'absence d'IS annuel ordinaire sur les bénéfices conservés est explicitée sans modifier les congés ni les règles de rupture.",
    "Les cinq alinéas sources sont intégralement lus et maintenus dans leur ordre ; seule la proposition imposant sept mois est retirée, puis deux alinéas de transition et de coordination sont ajoutés. Le deuxième alinéa de 39, 1, 1° bis est une option historique irrévocable réservée aux entreprises d'avant 1987, non une autorisation de CDD ou une indemnité de licenciement. Le présent dispositif reste nécessaire aux opérations futures de ces entreprises encore sous option. L'annexe III 49 octies A lue confirme la date d'effet rétroactif ; les modalités réglementaires ne devront pas rétablir le minimum supprimé. La durée des congés ou de leurs périodes d'acquisition n'est pas raccourcie. L'économie d'impôt éventuelle dépend des droits effectivement transférés, de ceux de clôture, de l'option et des règles de réintégration : aucun montant ni diminution nette définitive de taux ou d'assiette n'est démontré. Les contrats antérieurs, conversions conservant l'ancienneté et indemnités spéciales restent à leur champ propre.",
    'material_reduction',
    "Un plancher fiscal explicite de sept mois est effectivement supprimé par rapport à la source entière ; les autres calculs anti-double déduction restent. Le gain démontré porte sur cette contrainte de calcul, sans revendiquer une baisse générale ou définitive de l'impôt.",
    "Seules les opérations à date d'effet nouvelle sont concernées. La comparaison avec la période de clôture peut rendre la coupe sans effet dans certains cas ; l'impact fiscal net et le coût de conformité restant ne sont pas quantifiés.",
    "Aucune charge nouvelle n'est identifiée : la neutralisation, la réintégration et leurs données préexistent ; aucun registre ou justificatif de remplacement n'est créé. La transition emploie la date d'effet déjà prévue par l'annexe III et protège les opérations anciennes.")
reduction(a, "Plancher forfaitaire de sept mois imposé à la période fiscalement neutralisée pour les congés payés transférés entre entreprises ayant des options fiscales différentes.")
a['benefit_review'] = "La déduction fiscalement réputée opérée pour les droits non utilisés à la clôture reste expressément conservée au premier alinéa. L'option historique de l'entreprise absorbée au 39, 1, 1° bis, les droits à congés payés des salariés et le traitement des charges sociales et fiscales restent intacts, y compris pour les futures fusions, scissions, apports et transferts recevables. La réintégration reste limitée à la différence prévue au deuxième alinéa ; seule la borne forfaitaire de sept mois est supprimée. Le minimum fondé sur la période d'acquisition des droits encore inutilisés à la clôture demeure. Aucune ancienneté salariale ou indemnité de rupture n'est réduite par cette mesure fiscale."
effect(a, 'obligation_removed', 'conges-transferes-neutralisation-fin-plancher',
    "Suppression de l'obligation d'appliquer une période fiscale fictive d'au moins sept mois ; ce n'est ni un délai de préavis ni une réduction de congés.",
    "Calcul de la période neutralisée soumis à un plancher autonome de sept mois, en plus de la comparaison aux droits non utilisés à la clôture.",
    "Plus de plancher autonome de sept mois ; calcul sur les droits transférés et comparaison de clôture conservés, sans taux fiscal modifié.",
    'legal_duty', "Entreprises absorbantes ou bénéficiaires de transferts de salariés lorsque l'entreprise d'origine avait l'option historique de 39, 1, 1° bis et la bénéficiaire ne l'avait pas.",
    "Opérations à date d'effet dès l'entrée en vigueur ; date rétroactive prise en compte selon la règle réglementaire existante, opérations anciennes conservées.",
    "Aucune période ou attestation de remplacement ; neutralisation anti-double déduction et réintégration existantes restent.",
    "elle est au minimum de sept mois.",
    "La suppression du minimum de sept mois s'applique aux opérations dont la date d'effet intervient à compter de l'entrée en vigueur")


s = by_number['236 ter']['source_xml']
ps = [q.strip() for q in re.split(r'<br\s*/?>', s) if q.strip()]
assert len(ps) == 2
ps[0] = "Pour l'établissement de l'impôt sur le revenu ou de l'impôt sur les sociétés, les dépenses exposées à l'occasion d'études archéologiques préalables ou d'opérations archéologiques qui constituent un élément du prix de revient d'une immobilisation peuvent être déduites des résultats de l'exercice au cours duquel elles sont engagées. Cette faculté est ouverte que les études ou opérations soient obligatoires ou volontaires, sans condition tenant à leur réalisation en application d'une loi déterminée."
p = paragraphs(*ps,
    "L'élargissement de cette faculté s'applique aux dépenses engagées à compter de l'entrée en vigueur de la loi qui le prévoit. Les dépenses engagées auparavant et les déductions déjà pratiquées restent régies par les dispositions qui leur étaient applicables, y compris pour leurs reprises ultérieures et leurs recours.",
    "Pour les bénéfices relevant de l'impôt sur les sociétés à la distribution, les déductions et reprises prévues au présent article sont prises en compte pour déterminer les bénéfices imposables lors de leur distribution. Leur calcul ne rend pas exigible un impôt ordinaire sur les bénéfices conservés. Aucune dépense ne peut être déduite deux fois. La présente faculté fiscale ne dispense d'aucune autorisation, prescription ou protection patrimoniale requise pour réaliser les études ou opérations.")
a = base('236 ter', p,
    "Réforme de fond favorable : suppression de la condition limitant la déduction anticipée aux dépenses effectuées en application des trois lois anciennes citées, au profit de toutes les études préalables et opérations archéologiques constituant réellement un élément du prix de revient d'une immobilisation. Les opérations volontaires peuvent ainsi utiliser la même faculté. Le second alinéa est conservé intégralement : reprises au rythme de l'amortissement et solde à la cession. Il s'agit d'un avantage de calendrier élargi, pas d'une exonération définitive de la dépense ou d'une baisse de taux. Les anciens droits restent protégés et la coordination IS exclut une imposition annuelle implicite des réserves.",
    "Les deux alinéas sources, sans note, sont lus entièrement. Les références aux lois du 27 septembre 1941, du 10 juillet 1976 et du 31 décembre 1976 ne sont pas laissées comme critères fermés potentiellement recodifiés : la condition est effectivement retirée. Aucun nouveau numéro du code du patrimoine n'est inventé. Le contenu matériel des obligations patrimoniales hors corpus n'est pas réécrit et reste applicable sur ses fondements propres ; une opération fiscale éligible n'est pas autorisée à fouiller illégalement. La reprise au même exercice et aux suivants, et la distinction immobilisation amortissable ou non à la cession, sont maintenues mot pour mot. Le gain de trésorerie dépend de l'amortissement, des résultats et, pour le nouvel IS, des distributions ; aucune baisse définitive ni recette nette n'est chiffrée. La suppression distincte de la taxe 235 ter ZG ne supprime ni ce droit à déduction ni la reprise de dépenses antérieurement déduites.",
    'payment_timing_relief',
    "Le droit à déduction anticipée est ouvert à des dépenses auparavant exclues par la condition des trois lois. Comme toutes les reprises de la source restent en place, l'effet démontré est un allègement de calendrier potentiel, non une réduction définitive d'impôt.",
    "Les dépenses doivent toujours entrer dans le prix de revient d'une immobilisation ; aucune dépense fictive ou déjà déduite n'est couverte. L'ampleur du report dépend des amortissements, cessions, résultats et distributions ; aucun montant de trésorerie ou rendement n'est établi.",
    "Aucune charge nouvelle n'est identifiée : ni agrément, justificatif légal supplémentaire, déclaration ni registre spécial n'est créé. Les reprises et la preuve du coût immobilisé existaient ; les protections patrimoniales demeurent sans procédure fiscale de remplacement.")
reduction(a, "Condition subordonnant la déduction anticipée des dépenses archéologiques à leur exécution en application des seules lois du 27 septembre 1941, du 10 juillet 1976 et du 31 décembre 1976.")
a['benefit_review'] = "La déduction immédiate optionnelle des dépenses archéologiques immobilisables est maintenue pour tous les anciens bénéficiaires et étendue aux dépenses futures sans condition d'origine dans une des trois lois, y compris opérations volontaires. Les dépenses anciennes conservent leur régime et les reprises prévues. Le maintien du second alinéa signifie que l'avantage reste un décalage de déduction : ni suppression d'amortissement légitime ni exonération définitive inventée. La suppression de la taxe d'archéologie préventive n'éteint pas cet avantage autonome portant sur des dépenses réelles."
effect(a, 'payment_deferred', 'archeologie-deduction-anticipee-elargissement',
    "Extension du calendrier favorable de déduction immédiate aux dépenses archéologiques immobilisables hors des trois fondements législatifs anciens.",
    "Déduction anticipée réservée aux dépenses immobilisables réalisées en application des trois lois citées ; autres dépenses non admises par cet article à cette anticipation, taux IR/IS non modifiés.",
    "Déduction possible dès l'exercice d'engagement pour toutes les dépenses archéologiques immobilisables nouvelles, obligatoires ou volontaires, avec les mêmes reprises à l'amortissement et à la cession ; taux inchangés par cet article.",
    'financing', "Entreprises soumises à l'IR ou à l'IS engageant des dépenses archéologiques qui entrent dans le prix de revient d'une immobilisation.",
    "Dépenses engagées dès l'entrée en vigueur ; anciens droits et reprises conservés, sans remboursement rétroactif général. Pour le nouvel IS, effet à apprécier lors des distributions.",
    "Aucune procédure nouvelle ; coût réel, non-double déduction et reprises existantes restent requis.",
    "si elles sont effectuées en application des dispositions de la loi du 27 septembre 1941 modifiée portant réglementation des fouilles archéologiques, de la loi n° 76-629 du 10 juillet 1976 modifiée relative à la protection de la nature et de la loi n° 76-1285 du 31 décembre 1976 portant réforme de l'urbanisme.",
    "Cette faculté est ouverte que les études ou opérations soient obligatoires ou volontaires, sans condition tenant à leur réalisation en application d'une loi déterminée.")


a = base('237', None,
    "Maintien intégral nécessaire de la non-déductibilité des publicités pour l'alcool prohibées par les trois articles sanitaires cités. Cette règle ne finance pas l'activité par une taxe distincte : elle évite que l'impôt subventionne une dépense illégale relevant d'une protection de santé publique. La retirer créerait un avantage pour l'illégalité sans retirer la prohibition sanitaire. Aucun agrément, délai minimal, formulaire ni doublon documentaire propre n'a été identifié à supprimer.",
    "Source entière de deux lignes, sans note, lue. Les renvois L.3323-2, L.3323-4 et L.3323-5 santé publique ne sont pas attribués au code du travail ni au contrat unique. Leur contenu n'est pas joint dans les cibles : aucune extension des publicités prohibées n'est décidée ni présentée comme vérifiée article par article hors corpus. Le renvoi conserve son objet de publicités légalement prohibées ; il ne vise pas toutes les dépenses commerciales. Le calcul du bénéfice fiscal n'est pas un fait générateur annuel d'IS : les bénéfices conservés restent sous le régime de distribution du noyau IS et le minimum international reste distinct. La conservation de cette protection ne constitue ni une réduction fiscale ni une validation indépendante de ses renvois sanitaires.",
    'retained_necessary',
    "La norme nécessaire de non-subvention fiscale d'une publicité illégale est maintenue intégralement. Aucun gain nouveau, suppression de taxe ou simplification matérielle n'est compté sur cet article.",
    "Le champ des prohibitions sanitaires relève d'un code extérieur non fourni ; leur modification et la mesure économique de l'effet de cette non-déductibilité ne sont pas entreprises. La non-déductibilité ne concerne que les dépenses prohibées visées.",
    "Aucune charge nouvelle n'est identifiée : la règle d'assiette reste identique sans nouvelle donnée, pièce, autorisation ou échéance. L'obligation sanitaire autonome n'est ni élargie ni remplacée par une déclaration fiscale.")


a = base('237 bis', None,
    "Maintien intégral nécessaire de la déductibilité des contributions patronales d'assurance chômage et de l'allocation complémentaire : il s'agit d'un avantage fiscal utile, applicable aussi aux futurs employeurs et emplois éligibles au contrat unique. Le renvoi à L.5422-1 désigne la prestation d'assurance financée, non une indemnité ordinaire de rupture. Il n'impose ni nouveau CDD ni seuil d'un an ni préavis supplémentaire. Aucun dépôt ou agrément propre à retirer ; supprimer cet article ferait disparaître une garantie explicite de déduction sans supprimer les contributions correspondantes.",
    "Article et note de recodification de l'ordonnance 2007-329 lus. Les sources et propositions des quatre cibles requises sont lues et distinguées. Lecture complémentaire intégrale de L.5422-10 et L.3232-6 dans le corpus : le premier alinéa de L.5422-10 porte bien sur les contributions patronales et leur déductibilité ; L.3232-6 raccorde l'allocation complémentaire au régime fiscal et social de L.5428-1. Aucun renvoi ordinal devenu vide n'est constaté ici. Le maintien de la déduction pour l'IS est une règle de calcul des bénéfices, pertes ou droits antérieurs, sans acompte annuel ni imposition des bénéfices conservés. La réforme des contrats et de l'accès à l'assurance chômage ne transforme pas ces contributions en indemnité de rupture. Aucun transfert vers la capitalisation ni baisse de cotisation n'est compté ; charges autonomes et conditions de l'assurance restent à leur champ.",
    'retained_necessary',
    "L'avantage fiscal de déduction est conservé pour les contributions patronales et l'allocation complémentaire, sans nouveau texte stylistique. Sa conservation ne vaut pas une baisse nouvelle des contributions ni un allègement d'obligations déclaratives.",
    "Le taux des contributions, les règles d'assurance chômage, les emplois publics éventuels et les droits à indemnité de rupture demeurent distincts. Aucun rendement, gain de financement ou résultat d'ensemble des codes n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : déductibilité et renvois sont intégralement conservés, sans condition d'ancienneté, notification, document ou délai supplémentaire. Aucun registre de transition au contrat unique n'est créé par cet article.")
a['benefit_review'] = "La déduction des contributions des employeurs au financement de l'allocation d'assurance L.5422-1 et celle de l'allocation complémentaire L.3232-6 restent entières, aussi bien pour les charges anciennes que pour les futures situations éligibles. L'accès aux aides ou allocations ne devient pas réservé aux anciens CDD ; le contrat unique est sans effet restrictif sur cette déduction. Le renvoi au premier alinéa de L.5422-10 confirme la déductibilité patronale, distincte de celle des travailleurs à son second alinéa. Aucun taux, plafond ou justificatif restrictif n'est ajouté."


checks = {
    '235 ter ZD': {
        '223 A': "Le renvoi du II, 5° vise le périmètre d'intégration fiscale pour exonérer les acquisitions intragroupe ; il ne vise aucune ancienneté ni notification de rupture. La source de 223 A exige notamment 95 % et organise l'intégration annuelle ; sa proposition organise le paiement de l'IS à la distribution et préserve les exercices anciens. La taxe d'acquisition est ici supprimée pour l'avenir indépendamment de l'option de groupe. Pour les acquisitions anciennes, le périmètre et l'exonération restent ceux applicables à leur date, sans substitution rétroactive de la proposition de 223 A ni rétablissement d'un IS annuel.",
        'L1234-1': "Aucun renvoi de 235 ter ZD ne vise le préavis de licenciement : les renvois au code du travail de ses II, 7° et 8° concernent l'épargne et l'actionnariat salariés. Les quinze jours calendaires du contrat unique et les préavis historiques de L1234-1 n'affectent ni le transfert de propriété des titres ni l'exonération ancienne. La suppression de la taxe n'ajoute aucune condition d'ancienneté ou de notification, et ne supprime aucune procédure collective ou autorisation de salarié protégé.",
        'L1221-2': "L'exonération des acquisitions d'actionnariat salarié n'est pas un cas de recours au CDD. La source et la proposition de L1221-2 sont distinguées : nouveaux emplois à durée indéterminée, anciens contrats et leurs droits préservés. Les futures acquisitions de tous les salariés échappent à la taxe supprimée, sans ancienneté supplémentaire et sans condition de forme du contrat ; l'ancien avantage d'épargne salariale n'est pas fermé aux nouveaux contrats uniques.",
        'L1234-9': "La cible porte sur l'indemnité ordinaire de rupture et non sur le II, 7° ou 8° d'actionnariat salarié. Le seuil d'un an au terme effectif préavis inclus, le barème de 0,20 mois sur toute l'ancienneté par mois complets, le plafond de six mois et les anciens droits n'entrent pas dans l'assiette des acquisitions de titres. Aucune règle de rupture n'est introduite dans cette abrogation ; congés, indemnités spéciales et recours restent autonomes."
    },
    '235 ter ZD bis': {
        '235 ter ZD': "Le III renvoie précisément au 3° du II de 235 ter ZD pour la définition de la tenue de marché, et non à tout son champ fiscal. Cette définition couvre cotations régulières, exécution d'ordres ou réponses aux clients et couverture des positions associées. L'abrogation concomitante de la taxe d'acquisition ne doit pas priver les faits anciens de cette exonération : la proposition fige expressément le renvoi à la rédaction applicable aux opérations anciennes. Pour les faits nouveaux, la taxe haute fréquence entière disparaît ; aucune ancienneté ou notification de rupture n'est pertinente."
    },
    '235 ter ZG': {
        '1635 quater D': "Le III, 1° renvoie aux seuls 1° à 4° et 8° à 11° du I, complétés pour 2° à 4° par leurs conditions d'exonération, non aux 5° à 7° OIN/ZAC/PUP. La cible officielle entière et ses II et III sont lus : services publics, logements sociaux, agriculture, centres équestres, prévention des risques, reconstructions, petites surfaces et stationnements intégrés sont concernés ; les règles SIEG et de minimis conservent leur champ. Ces exonérations restent appliquées aux faits anciens et la taxe d'aménagement demeure pour les opérations futures avec ses propres exonérations. La taxe archéologique future est entièrement supprimée, sans condition d'ancienneté salariale ou de notification."
    },
    '236 bis': {
        '39': "Le renvoi vise exactement le deuxième alinéa du 1° bis du 1 de 39 : option irrévocable du régime de déduction lors de la prise effective du congé, non ouverte aux entreprises créées après le 31 décembre 1986 et exercée au dépôt historique de 1987. La source et la proposition fournies maintiennent ce régime. L'article 236 bis coordonne des options différentes lors de la fusion ou du transfert, sans rouvrir l'option ni modifier les congés payés. La coupe porte uniquement sur les sept mois, avec neutralisation et réintégration restantes et absence d'IS annuel sur les bénéfices conservés ; aucun seuil d'indemnité de rupture n'est transposé.",
        'L1234-1': "Le transfert de salariés avec maintien des contrats visé au troisième alinéa n'est pas un licenciement et ne déclenche aucun préavis individuel. La période neutralisée de congés payés ne correspond ni aux quinze jours du nouveau contrat ni aux préavis des contrats antérieurs. L'ancienneté et les droits transférés sont conservés ; si une rupture distincte intervient, notification, préavis et protections spéciales s'apprécient selon L1234-1 et les dispositions applicables, sans incidence du minimum fiscal supprimé.",
        'L1221-2': "Le maintien des contrats lors d'une fusion, scission, apport ou transfert ne constitue pas une nouvelle embauche à terme. L1221-2 proposé interdit les nouveaux CDD et protège les anciens contrats ; 236 bis reste applicable aux congés transférés dans chaque situation sans limiter l'emploi à la période neutralisée. La date d'effet fiscale ne remet à zéro ni contrat ni ancienneté et ne ferme pas les déductions favorables aux futures opérations éligibles.",
        'L1234-9': "Les indemnités ici neutralisées sont celles de congés payés, pas l'indemnité ordinaire de licenciement. Le zéro avant un an ne peut donc les supprimer. La proposition de L1234-9 mesure son seuil au terme effectif avec préavis inclus, puis 0,20 mois pour toute l'ancienneté, fractions en mois complets et plafond six mois, avec anciens droits et indemnités spéciales réservés. Aucune de ces conditions ne devient une condition de congés ni de déduction de 236 bis ; aucune notification de rupture n'est créée par un transfert."
    },
    '237 bis': {
        'L1234-1': "La déduction des contributions finançant le chômage n'est pas calculée en fonction du préavis de licenciement. Le préavis nouveau de quinze jours calendaires et les préavis des contrats anciens demeurent au champ de L1234-1, avec notification selon leurs règles et procédures collectives distinctes. L'article fiscal maintenu ne supprime ni contributions ni droits de déduction durant ces périodes et ne conditionne la déduction à aucune ancienneté supplémentaire.",
        'L1221-2': "Le renvoi fiscal vise des contributions et une allocation, non un terme d'emploi. Les nouveaux contrats uniques à durée indéterminée restent éligibles à la déduction, comme les anciens contrats, sans rouvrir les CDD ni limiter le contrat à une période d'indemnisation ou d'aide. La proposition de L1221-2 et ses transitions sont distinguées de la source officielle ; aucune conversion ou remise à zéro d'ancienneté n'est exigée fiscalement.",
        'L1234-9': "L'indemnité patronale ordinaire de rupture (zéro avant un an au terme effectif préavis inclus, puis 0,20 mois pour toute l'ancienneté au prorata des mois complets et plafond six mois) n'est ni la contribution d'assurance chômage ni l'allocation complémentaire de 237 bis. Sa réforme ne retire donc aucune déduction de cet article. Les anciens droits, salaires et congés, dommages d'illégalité et indemnités spéciales restent autonomes ; aucune condition d'un an ou notification n'est ajoutée à la déductibilité.",
        'L5422-1': "Le renvoi désigne la prestation d'assurance chômage financée par les contributions patronales ; la source distingue privation involontaire, ruptures conventionnelles ou collectives et certaines démissions pour reconversion, avec conditions d'âge, d'activité et de projet. La proposition retire la restriction liée à deux refus de CDI et les signalements associés, sans assimiler toute démission à un droit au chômage. La déductibilité de 237 bis est maintenue pour les futurs emplois éligibles ; seuil d'un an d'indemnité ordinaire et préavis de quinze jours ne remplacent aucune condition d'activité antérieure de l'assurance."
    }
}

for s in S:
    a = answers[s['number']]
    required = R['requirements'][s['code_id'] + '|' + s['source_id']]
    a['reference_checks'] = []
    for key in required:
        target = R['targets'][key]
        assessment = checks[s['number']][target['number']]
        assert len(assessment) >= 80
        a['reference_checks'].append(dict(target_key=key, view_sha256=target['view_sha256'], assessment=assessment))

output = [answers[s['number']] for s in S]
assert len(output) == len(S) == 12


class CheckMarkup(HTMLParser):
    allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
    def handle_starttag(self, tag, attrs):
        assert tag in self.allowed, tag
        for key, value in attrs:
            assert key in {'rowspan', 'colspan'} and value.isdigit(), (key, value)


for a, s in zip(output, S):
    assert all(a[k] == s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
    assert a['status'] in {'rewrite_draft', 'retained_unchanged'}
    imp = a['substantive_impact']
    assert imp['version'] == 1
    assert all(len(imp[k]) >= 40 for k in ('assessment', 'scope_limitations', 'new_burdens_review'))
    assert [c['target_key'] for c in a['reference_checks']] == R['requirements'][s['code_id'] + '|' + s['source_id']]
    if s['benefit_check_required']:
        assert len(a.get('benefit_review', '')) >= 100
    if a['proposed_xml'] is None:
        assert a['status'] == 'retained_unchanged' and a['classification'] == 'retained_necessary'
        assert imp['classification'] == 'retained_necessary' and not imp['effects']
    else:
        CheckMarkup(convert_charrefs=True).feed(a['proposed_xml'])
        if a.get('change_type') == 'full_repeal':
            assert plain(a['proposed_xml']).startswith('Le présent article est abrogé')
            assert len(a['repeal_scope']) >= 30
        if a.get('change_type') == 'normative_reduction':
            assert all(len(v) >= 30 for v in a['removed_provisions'])

Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(articles=len(output), statuts={status:sum(a['status']==status for a in output) for status in ['rewrite_draft','retained_unchanged']}, abrogations=sum(a.get('change_type')=='full_repeal' for a in output), reductions=sum(a.get('change_type')=='normative_reduction' for a in output)), ensure_ascii=False))
