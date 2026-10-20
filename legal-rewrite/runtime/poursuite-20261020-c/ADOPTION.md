# Adoption bornée des contrelectures phase C — script préparé, non exécuté

`adopt_reviewed.py` n’a pas été lancé. Attendre le signal explicite du parent après enregistrement et activation. Les éditions préparatoires de `certificate-refresh/edition001` et `edition002` sont dépassées par la nouvelle fusion sociale ; ne pas les employer comme preuve finale.

Entrées obligatoires :

- `integration-specs.json`, le `preflight.json` final, les sources/réponses d’intégration et leur `registration.json` ; l’ordre des spécifications détermine les dernières métadonnées, sans écrasement implicite.
- `activation.json`, dont les deux empreintes doivent correspondre aux politiques réellement actives.
- Le plan final explicitement choisi avec `--refresh-plan`, et le `refresh-proof.json` réel choisi avec `--refresh-receipt`. Le second est produit après capture réelle en DB, lecture/approbation du parent des analyses explicitement modifiées dans le plan final et réémission des certificats. Les chemins sont relatifs au dossier phase C. Les simples plans et corps attendus ne suffisent pas.
- Tous les manifestes gelés et rapports indépendants ; leur réponse exacte doit être nommée par empreinte dans les preuves. Le supplément L2262-7/L3243-5 approuvé est obligatoire pour lever la condition Travail21.

Le script ne touche jamais SQLite, les lots, sources, politiques ni sites. Au moment où le parent l’exécutera, il prend le verrou partagé avant le `BEGIN` SQLite en lecture seule, puis recontrôle tous les fichiers avant l’écriture du registre d’audits. Il n’utilise aucun envoi réseau.

Les audits antérieurs restent tous présents. Seules les 204 identités explicitement adoptées par le reçu phase B sont susceptibles de réattestation ; les 80 autres restent périmées, même si leurs gardes sont vides, sauf nouvelle contrelecture phase C. Un document source brut est revérifié contre son empreinte et son corps extrait ; notes, proposition, analyse et chaque garde de dépendance doivent être identiques pour renouveler le seul lien de politique. Sinon l’entrée entière garde son ancien certificat, donc périmé. Une nouvelle contrelecture phase C peut remplacer cette entrée avec son historique conservé. Le registre précédent est archivé octet pour octet sous son SHA256 avant remplacement. Un second appel identique est sans effet ; un registre changé après adoption impose une nouvelle édition revue.

Pour les nouveaux audits, les dépendances conservatrices couvrent tous les frères phase C, la capture finale des renvois et les cibles externes du préflight. Cela peut périmer une lecture plus tôt que nécessaire, jamais prolonger indûment une validation. Les cinq contextes intrapaquet changés ne sont pas assimilés à des sources inchangées ; leur état réel doit apparaître dans la capture approuvée. Les analyses modifiées doivent être exactement celles approuvées dans le plan final, quel que soit leur nombre, sans création de certificat sur les articles qui n’en requéraient pas.

Le bilan reste `global_net_reduction=not_established`, `national_savings=null`, sans validation par un juriste et sans achèvement exhaustif revendiqué.

Vérification réalisée : 17 tests purs de gardes (fonctions extraites par AST), sans appel à `main`, sans import métier, sans ouverture de DB et sans écriture du registre. Ces tests ne simulent pas une intégration achevée et ne constituent pas l’adoption.
