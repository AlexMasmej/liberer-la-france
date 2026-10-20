import hashlib
import html
import json
import re
from pathlib import Path


def plain(xml):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", " ", xml))).strip()


sources = json.loads(Path("source.json").read_text())
a, b = sources

old_b = "b) Le renouvellement urbain, le développement urbain et rural maîtrisé, la restructuration des espaces urbanisés, la revitalisation des centres urbains et ruraux, la lutte contre l'étalement urbain ;"
new_b = "b) La restructuration des espaces urbanisés, la revitalisation des centres urbains et ruraux, la lutte contre l'étalement urbain ;"
old_2 = "2° La qualité urbaine, architecturale et paysagère, notamment des entrées de ville ;"
new_2 = "2° Abrogé ;"
old_3 = "3° La diversité des fonctions urbaines et rurales et la mixité sociale dans l'habitat, en prévoyant des capacités de construction et de réhabilitation suffisantes pour la satisfaction, sans discrimination, des besoins présents et futurs de l'ensemble des modes d'habitat, d'activités économiques, touristiques, sportives, culturelles et d'intérêt général ainsi que d'équipements publics et d'équipement commercial, en tenant compte en particulier des objectifs de répartition géographiquement équilibrée entre emploi, habitat, commerces et services, notamment les services aux familles, d'amélioration des performances énergétiques, de développement des communications électroniques, de diminution des obligations de déplacements motorisés et de développement des transports alternatifs à l'usage individuel de l'automobile ;"
new_3 = "3° Des capacités de construction et de réhabilitation suffisantes pour la satisfaction, sans discrimination, des besoins présents et futurs de l'ensemble des modes d'habitat, d'activités économiques, touristiques, sportives, culturelles et d'intérêt général ainsi que d'équipements publics et d'équipement commercial, en tenant compte en particulier des objectifs d'amélioration des performances énergétiques, de développement des communications électroniques, de diminution des obligations de déplacements motorisés et de développement des transports alternatifs à l'usage individuel de l'automobile ;"

transition = "À compter de l'entrée en vigueur de la loi portant la présente rédaction, le seul renvoi au présent article ou à sa rédaction antérieure ne peut plus imposer les objectifs généraux de renouvellement urbain, de développement urbain et rural maîtrisé, de qualité urbaine, architecturale et paysagère, notamment des entrées de ville, de diversité des fonctions urbaines et rurales ou de mixité sociale dans l'habitat, ni l'objectif de répartition géographiquement équilibrée entre emploi, habitat, commerces et services, notamment les services aux familles. Les dispositions des documents d'urbanisme et les stipulations contractuelles qui se bornent à rappeler ces objectifs ne les rendent pas applicables pour l'avenir. Ces suppressions s'appliquent aux procédures en cours, sans nouveau dépôt de dossier ni reprise des délais ou des consultations régulièrement accomplis. Elles ne remettent pas en cause les actes légalement pris, les contrats valablement conclus, les créances antérieurement nées, les droits acquis des occupants et des tiers ni les autorisations régulièrement délivrées. Les prescriptions de ces autorisations restent soumises à leurs procédures ordinaires de modification et à leurs voies de recours. L'objectif maintenu de capacités suffisantes de construction et de réhabilitation n'institue aucun quota communal de logements sociaux et ne rétablit pas les objectifs de mixité ou de répartition géographique retirés par la présente rédaction. Les règles reposant sur un fondement distinct demeurent applicables dans leur champ propre."

proposed = a["source_xml"]
for before, after in [(old_b, new_b), (old_2, new_2), (old_3, new_3)]:
    assert proposed.count(before) == 1
    proposed = proposed.replace(before, after)
proposed += "<p>" + transition + "</p>\n"

source_text = plain(a["source_xml"])
source_quote = source_text[source_text.index(old_b):source_text.index(old_3) + len(old_3)]
proposed_quote = transition.split(". Les dispositions", 1)[0] + "."

first = {
    **{key: a[key] for key in ("code_id", "source_id", "source_sha256", "number")},
    "proposed_xml": proposed,
    "reason": "Réduction de fond, comparée à l'intégralité de la source officielle : les suppressions déjà acquises au b du 1° et au 3° sont conservées (objectifs généraux de renouvellement, de développement maîtrisé, de diversité fonctionnelle, de mixité et de répartition géographique). La seconde passe retire aussi le 2° : l'obligation générale de poursuivre une qualité urbaine, architecturale et paysagère ajoute un critère indéterminé aux objectifs conservés, sans fonction essentielle distincte démontrée dans cet article. Les protections précises des sites, paysages, patrimoine, sécurité, salubrité, risques, environnement et accessibilité subsistent ; les règles autonomes de qualité et les dérogations favorables ne sont pas abrogées. L'objectif de capacités suffisantes de construction et de réhabilitation reste opposable pour les besoins futurs aussi. Hors ces coupes et leur transition, le texte source est conservé mot pour mot : aucune réécriture stylistique n'est comptée comme réduction. Aucun impôt, taux, agrément ou délai n'est supprimé par cet article d'objectifs généraux.",
    "review_notes": "Lecture intégrale des deux sources assignées, de leurs notes vides, des propositions antérieures et des textes initiaux SRU joints (article 1 entier et article 202 I à XXXIX entier). Aucun tableau ni compagnon d'image n'est présent. Le rapprochement entre l'ancien L121-1 reproduit par SRU1 et certains objectifs actuels est matériel ; il ne fait pas de tout L101-2 un apport de SRU. Le 6° bis et les autres apports ultérieurs conservés ne sont pas effacés. Le 2° est retiré sur le fondement de l'orientation générale de réduction des contraintes, sans lui attribuer une origine SRU non démontrée. Les versions historiques LEGIARTI000006814369 et LEGIARTI000006814664, signalées comme pistes, ne figurent pas dans le corpus d'articles local consulté ; aucune vérification externe n'est autorisée et la chaîne historique complète n'est pas déclarée établie. Renvois source lus en entier dans le corpus : L101-1, L101-2-1, L111-4, L112-3, L113-8, L132-1, L141-1, L141-4, L143-25, L146-1, L151-1, L151-8, L153-25, L153-27, L161-2, L161-3, L331-1, R151-49 et R161-2 ; également L131-1, L151-5, L111-6 à L111-10, L151-18 et R111-27. Les renvois généraux restent cohérents vers les objectifs subsistants ; ils ne recréent pas ceux retirés. Coordination rédactionnelle à effectuer hors de ce lot : retirer au c de CCH R302-1-1 la seconde phrase imposant de rendre compte de la mixité expressément rattachée à L101-2 ; les autres analyses du diagnostic, toutes lues, gardent leur objet autonome. La transition empêche déjà le seul renvoi de rétablir cet objectif. L101-2-1 2° et 4° conserve ses leviers de renouvellement et de qualité dans le régime propre de lutte contre l'artificialisation ; L153-25 5°, L151-18 et R111-27 conservent leurs fondements spécifiques. Les dérogations L111-7 à L111-10 ne sont ni fermées ni privées de leurs conditions ; aucune suppression générale des études ou prescriptions architecturales n'est revendiquée. Le délai de six ans de L153-27, les contrôles préfectoraux, la taxe d'aménagement L331-1 et les protections littorales ne sont pas abolis ici. La numérotation 1° a à e, 2°, 3° à 8°, dont 6° bis, et tous les alinéas maintenus sont conservés. La transition reprend les garanties antérieures, sans date de promulgation inventée. Aucun des renvois lus n'est compté comme une seconde suppression ; les objectifs retirés sont regroupés en un seul effet. Ces deux articles ne soldent ni SRU1 ni SRU202 ni l'examen des 209 articles ; aucune validation juridique indépendante ou économie globale n'est déclarée.",
    "status": "rewrite_draft",
    "change_type": "normative_reduction",
    "reform_policy_id": "editorial_direction_2026_10_19",
    "removed_provisions": [
        "Au b du 1°, suppression des objectifs généraux de renouvellement urbain et de développement urbain et rural maîtrisé ; les possibilités de ces opérations et les règles autonomes ne sont pas interdites.",
        "Au 2°, suppression de l'objectif général de qualité urbaine, architecturale et paysagère, notamment des entrées de ville ; les protections spécifiques et les dérogations favorables demeurent.",
        "Au 3°, suppression des objectifs généraux de diversité des fonctions urbaines et rurales, de mixité sociale dans l'habitat et de répartition géographiquement équilibrée entre emploi, habitat, commerces et services, notamment les services aux familles."
    ],
    "benefit_review": "Le levier favorable identifiable est l'objectif de capacités de construction et de réhabilitation suffisantes : il reste entier, pour tous les modes d'habitat, activités et équipements énumérés, sans discrimination et pour les besoins présents comme futurs. Le retrait des objectifs généraux ne prohibe ni renouvellement ni développement urbain ; leurs possibilités et les fondements autonomes restent ouverts. Les protections des occupants, des tiers, des actes, contrats, créances et autorisations antérieurs sont expressément reprises. Les dérogations de construction de L111-7 à L111-10, dont les conditions ont été lues, gardent leur fondement pour les futures opérations éligibles. Le schéma de plage, ses dérogations littorales et la franchise TASCOM ne relèvent pas du 2° supprimé et ne sont pas fermés. L'article ne contient aucune exonération fiscale propre à supprimer.",
    "substantive_impact": {
        "version": 1,
        "classification": "material_reduction",
        "assessment": "Par rapport à la source officielle entière, une obligation de poursuivre plusieurs objectifs généraux est retirée du cadre de l'action publique d'urbanisme : renouvellement et développement maîtrisé au 1° b, qualité générale au 2°, diversité, mixité et répartition géographique au 3°. Les effets de cette même réduction sur les renvois sont regroupés. Le retrait du 2° est la coupe supplémentaire par rapport au précédent brouillon ; les capacités suffisantes de construction, les autres objectifs et leurs protections demeurent. Il s'agit d'une diminution du champ des objectifs à respecter, sans suppression prétendue d'un permis, d'une taxe ou d'un nombre chiffré de pièces.",
        "scope_limitations": "L'allègement porte sur le seul fondement général L101-2 et les rappels qui en dépendent exclusivement. Les fondements autonomes, notamment qualité et renouvellement de L101-2-1, règles architecturales et paysagères spécifiques, études ouvrant des dérogations et droits des tiers, subsistent. La rédaction de CCH R302-1-1 c reste à coordonner hors lot. Les prescriptions des autorisations déjà délivrées ne sont pas automatiquement effacées. La filiation complète des articles SRU et le coût net pour les collectivités ou les constructeurs ne sont pas établis ; aucun solde global des codes ni effet budgétaire national n'est chiffré.",
        "new_burdens_review": "Aucune charge nouvelle n'est identifiée : le texte ne crée ni autorisation, déclaration, attestation, registre, collecte de données, étude, délai ou condition de remplacement. Les capacités suffisantes de construction et les protections conservées existent dans la source. La transition interdit un nouveau dossier et la reprise des délais ou consultations pour les seules suppressions. Les obligations fondées sur d'autres articles demeurent à leur champ propre ; leur maintien n'est pas présenté comme une baisse nette de l'ensemble des contraintes.",
        "effects": [
            {
                "kind": "obligation_removed",
                "measure_id": "urbanisme-objectifs-generaux-allegement",
                "description": "Suppression groupée des objectifs généraux retirés aux 1° b, 2° et 3°, ainsi que de leur imposition par un simple renvoi ou rappel, sans compter chaque objectif ou renvoi comme une mesure distincte.",
                "before": "L'action des collectivités publiques doit viser l'ensemble des objectifs de L101-2, dont renouvellement urbain, développement urbain et rural maîtrisé, qualité urbaine, architecturale et paysagère, diversité fonctionnelle, mixité sociale et répartition géographique équilibrée ; les documents et contrôles renvoyant à cet article les prennent en compte selon leur régime.",
                "after": "Ces objectifs généraux ne sont plus imposés par L101-2 ni par les seuls renvois ou rappels de sa rédaction antérieure. Tous les autres objectifs, dont les capacités suffisantes de construction et de réhabilitation, restent applicables ; les prescriptions et garanties ayant un fondement autonome demeurent.",
                "unit": "legal_duty",
                "affected_population": "Collectivités publiques et autorités chargées de l'urbanisme ; indirectement porteurs de projets et personnes concernées par les documents ou décisions renvoyant à L101-2.",
                "conditions_and_transition": "Application à l'entrée en vigueur de la loi proposée, y compris aux procédures en cours sans nouveau dépôt ni reprise des délais ou consultations. Actes réguliers, contrats valables, créances antérieures et droits acquis des occupants et tiers sont préservés ; les permis délivrés gardent leurs prescriptions et voies ordinaires de modification et de recours. Les règles autonomes ne sont pas abrogées.",
                "replacement_or_new_burdens": "Aucune formalité ou obligation de remplacement. Maintien des objectifs non retirés et des fondements spécifiques ; aucun quota, financement de substitution ou coût national chiffré n'est créé.",
                "source_quote": source_quote,
                "proposed_quote": proposed_quote
            }
        ]
    }
}

second = {
    **{key: b[key] for key in ("code_id", "source_id", "source_sha256", "number")},
    "proposed_xml": None,
    "reason": "Maintien intégral utile de la source, après lecture de ses deux règles, du brouillon antérieur et de SRU202 entier. L101-3 délimite la matière régie par l'urbanisme et son champ territorial ; il ne crée à lui seul ni taxe, autorisation, déclaration, délai minimal ou justificatif redondant. L'exclusion des productions agricoles empêche une extension du code aux choix de production ; elle n'exonère pas toutes les constructions agricoles. Les exclusions des collectivités de l'article 74, de la Nouvelle-Calédonie et des Terres australes et antarctiques françaises protègent leurs régimes spécifiques. Retrancher ces exceptions serait défavorable ; retirer la délimitation générale laisserait la portée du code incertaine sans abolir une obligation concrète. La proposition antérieure était uniquement stylistique : le texte officiel est donc maintenu sans nouveau corps et sans allègement revendiqué.",
    "review_notes": "Source_xml de 550 caractères, source_notes_xml vide et previous_draft entier relus. Les deux phrases source, l'article 74 de la Constitution et tous les territoires exclus sont maintenus sans changement ; aucun chiffre ou renvoi n'est corrigé silencieusement. Les renvois actuels de L112-3 et L161-2 à L101-3, et de L141-1, L146-1, L151-1 et L151-8 à la plage L101-1 à L101-3, ont été lus en entier et restent cohérents. La lecture intégrale de SRU202 montre que son I remplace une référence aux POS par une référence aux POS ou PLU dans l'ancien L111-1 ; ces mots n'existent pas dans L101-3 actuel. Cette substitution ne permet donc pas d'attribuer ses deux règles de champ à SRU ni de les abroger par filiation nominale. La piste LEGIARTI000006814664 a été examinée comme référence documentaire ; son texte historique intégral n'est pas dans le corpus d'articles local consulté. La préexistence exacte des deux phrases et la concordance complète de l'ancien L111-1 restent non établies ; ce volet historique n'est pas déclaré achevé. Aucun accès externe ni rétablissement des POS ou d'anciens articles abrogés. Aucune transition nouvelle n'est nécessaire pour ce maintien. Cet article ne compte ni comme réécrit ni comme simplifié, et aucune validation par un juriste n'est annoncée.",
    "status": "retained_unchanged",
    "classification": "retained_necessary",
    "benefit_review": "L'exclusion des productions agricoles est conservée mot pour mot, sans la transformer en immunité des bâtiments agricoles. Toutes les exclusions territoriales restent applicables, y compris aux futures situations relevant des régimes spécifiques de ces territoires. Le champ général ne contient aucun prélèvement ni avantage fiscal propre ; sa conservation n'abolit aucune exonération ou dérogation établie par un autre texte. La seule reformulation antérieure n'apportait aucun avantage supplémentaire à préserver.",
    "substantive_impact": {
        "version": 1,
        "classification": "retained_necessary",
        "assessment": "Aucun changement normatif par rapport à la source officielle entière : le champ matériel du droit de l'urbanisme, l'exclusion des productions agricoles et toutes les exclusions territoriales sont intégralement maintenus. Aucun prélèvement ou devoir autonome supprimable n'est identifié dans ces deux phrases ; le maintien protège notamment leurs limites de champ.",
        "scope_limitations": "Cette décision ne valide pas les obligations particulières des autres articles et ne démontre aucune économie ou simplification. La concordance historique complète avec l'ancien L111-1 signalé par SRU202 n'est pas disponible dans le corpus local ; l'examen de SRU202 et de ses autres descendants n'est pas déclaré achevé.",
        "new_burdens_review": "Aucune charge nouvelle n'est identifiée puisque la source reste intégralement inchangée : aucun registre, renseignement, dépôt, autorisation, délai ou condition ne lui est ajouté. Le renvoi constitutionnel et les limites territoriales sont ceux de la source, sans extension du champ du code.",
        "effects": []
    }
}

answer = [first, second]
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")

# Contrôles de traçabilité ; ils ne constituent pas une validation juridique.
assert len(answer) == len(sources) == 2
for item, source in zip(answer, sources):
    for key in ("code_id", "source_id", "source_sha256", "number"):
        assert item[key] == source[key]
    impact = item["substantive_impact"]
    assert impact["version"] == 1
    for key in ("assessment", "scope_limitations", "new_burdens_review"):
        assert len(impact[key]) >= 40
    seen = set()
    for effect in impact["effects"]:
        identity = (effect["measure_id"], effect["kind"])
        assert identity not in seen, identity
        seen.add(identity)
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", effect["measure_id"])
        assert 6 <= len(effect["measure_id"]) <= 96
        assert len(effect["source_quote"]) >= 12
        assert len(effect["proposed_quote"]) >= 12
        assert effect["source_quote"] in plain(source["source_xml"])
        assert effect["proposed_quote"] in plain(item["proposed_xml"])
    if source.get("benefit_check_required"):
        assert len(item["benefit_review"]) >= 100
    if item["status"] == "retained_unchanged":
        assert item["proposed_xml"] is None
        assert impact["effects"] == []
    if item.get("change_type") == "normative_reduction":
        assert all(len(s) >= 30 for s in item["removed_provisions"])

restored = proposed.removesuffix("<p>" + transition + "</p>\n")
for before, after in [(old_b, new_b), (old_2, new_2), (old_3, new_3)]:
    assert restored.count(after) == 1
    restored = restored.replace(after, before)
assert restored == a["source_xml"]
assert a["previous_draft"]["proposed_xml"].find("capacités de construction et de réhabilitation suffisantes") >= 0
assert all(s["source_notes_xml"] == "" for s in sources)

print(json.dumps({"output_file": "answer.json", "article_count": len(answer), "effects": sum(len(x["substantive_impact"]["effects"]) for x in answer), "bytes": Path("answer.json").stat().st_size}, ensure_ascii=False))
