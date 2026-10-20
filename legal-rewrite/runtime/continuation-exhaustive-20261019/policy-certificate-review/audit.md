# Garde des orientations dans les certificats — proposition v3

Correctif séparé de reference_coherence.py uniquement. Aucune modification canonique, politique, juridique, base ou publication. Le schéma de réponse des modèles et le texte du prompt restent identiques ; seules les métadonnées internes de capture/certificat passent de2 à3.

La fonction policy_state() calcule SHA256 sur les octets exacts de deux chemins fixes, relatifs à HERE : policy-coordinations.json et site-summaries.json. Aucun autre fichier de configuration, fichier caché ou secret n'est consulté. Un fichier absent porte la sentinelle explicite et stable `missing` ; sa création ou sa disparition change donc aussi la garde. Les erreurs de lecture ne sont pas silencieusement converties en approbation.

capture() inscrit ces deux empreintes dans policy_sha256. check_guards() compare cet état aux fichiers actuels et refuse une capture périmée avant l'inscription effectuée par le coordinateur. accept_checks() reporte une copie de la garde capturée dans chaque certificat concerné, sans recalculer et faire passer une politique nouvelle pour celle qui aurait été lue. certificate_current() compare les deux empreintes aux fichiers actuels même si le corps appelant et les cibles restent identiques. Les certificats pertinents v2 sont périmés par le changement de version et doivent être recapturés ; ils ne sont pas automatiquement promus.

Les trois tests isolés passent, avec fichiers et base temporaires uniquement :

1. Politiques inchangées : capture et certificat v3 contiennent exactement les SHA256 attendus, check_guards et certificate_current acceptent. Le cas des deux fichiers absents accepte également la sentinelle stable. Les objets d'analyse conservent leurs trois champs target_key/view_sha256/assessment.
2. Changement après capture de chacun des deux fichiers : check_guards lève ValueError avant tout commit. La création d'un fichier auparavant absent est aussi refusée.
3. Changement après certificat de chacun des deux fichiers : certificate_current devient faux à corps et renvois inchangés. La disparition d'un fichier est aussi détectée.

Résultat :3 tests,0 échec,0 erreur. Voir tests.log et checks.json. La garde du module canonique a été comparée une nouvelle fois à la baseline à l'issue des tests : identité exacte.

Le correctif ne touche pas les règles de prorata : les années incomplètes au prorata des mois complets restent gouvernées par les articles et orientations existants. Le parent peut appliquer le patch après drainage des travaux v2 puis modifier ses orientations selon son propre verrou ; cette revue ne déclenche ni activation ni relance.

Livrables : reference_coherence.baseline.py, reference_coherence.proposed.py, reference_coherence.patch, test_policy_certificate.py, tests.log, checks.json, manifest.json.

SHA256 baseline : `5a4f0e37a450495d0638065a8694b96aed908b0acab5a68f3643396bdf650917`.

SHA256 proposé : `8e54d11001bcfac40b1efc7278962edb783ba4d971509771dee1a04b063d0868`.
