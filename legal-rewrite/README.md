# Réécriture intégrale des textes officiels

Le périmètre confirmé par l’utilisateur comprend intégralement le Code du
travail, le Code général des impôts, le Code de la sécurité sociale, le Code de
l’urbanisme et le Code de la construction et de l’habitation. Les quatre
annexes du CGI sont incluses. Les anciennes synthèses de 18 ou 40 articles ne
sont pas une réécriture de ces codes.

## État conservé

- Source : fonds officiel LEGI de la DILA, stock du 13 juillet 2025 et 466
  mises à jour, jusqu’au 18 octobre 2026 inclus.
- Base `corpus.sqlite` : XML officiel intégral, versions, structure, notes et
  provenance ; propositions stockées séparément de la source.
- Inventaire publié : 30 317 entrées d’articles, dont certaines correspondent
  à des annexes ou à des versions concurrentes signalées.
- Les compteurs du dernier export sont dans `progress.json` ; l’avancement
  de la rédaction active est dans `runtime/exhaustive/status.json`.
  Aucun article n’est présenté comme validé par un juriste.
- Lecteur : https://libererlaretraite.com/corpus/
- Exemple fiscal complet :
  https://libererlaretraite.com/corpus/?code=impots&article=219

La réécriture exhaustive n’est PAS terminée. Les colonnes sans proposition
restent explicitement « À réécrire ». Il faut continuer à partir de la source,
pas remplacer les articles manquants par des résumés ou une copie déclarée
comme réécriture IA.

## Règles de rédaction

Depuis le 19 octobre 2026, l'auteur demande une suppression plus radicale des
charges, doublons, obligations et prélèvements. Cette décision prime la
préférence antérieure pour le simple toilettage rédactionnel. Chaque article
doit faire l'objet d'un choix de fond explicite ; les protections essentielles
et les contraintes européennes sont examinées et coordonnées. La source reste
toujours intégralement conservée, même lorsque la proposition abroge la norme.

Les droits de succession français et les prélèvements de substitution au décès
sont supprimés dans le projet, sans plafond ni condition de parenté ou de
résidence. L'assurance-vie, les plans retraite dénoués au décès et les trusts
sont inclus. Les donations entre vifs et les impôts dont le fait générateur
est distinct restent séparés. Les anciens décès conservent leur régime ; la
perte de recettes n'est ni chiffrée ni déclarée compensée sans preuve.
Les textes et coordinations sont dans `batches/successions/`.

Les articles déjà rédigés avant ce changement ne sont pas réputés avoir subi
cette seconde passe : l'inventaire à réexaminer est conservé dans
`runtime/radical-review-20261019.json`.
L'option `--review-prior-after` fait exécuter cette seconde passe après la file
des articles manquants. Les anciens textes proposés sont archivés avant toute
révision ; une modification intervenant entretemps bloque leur remplacement.
`--review-prior-first` traite cette reprise en priorité, avant de continuer
les articles manquants, et respecte les créneaux réservés aux agents spécialisés.
Les abrogations intégrales et les suppressions partielles portent des
métadonnées explicites de justification. La longueur de la proposition ne
doit pas servir à maintenir une obligation que l'auteur demande de supprimer.

1. Lire l’article source entier, ses notes d’application et les renvois utiles.
2. Conserver son numéro et l’identifiant de sa version d’origine.
3. Rédiger l’article proposé entier, même s’il est très long. Distinguer la
   simplification rédactionnelle et le changement de fond. Les mesures déjà
   définies constituent les orientations de réforme.
4. Conserver les tableaux et les autres éléments nécessaires. Identifier les
   coordinations, dispositions transitoires et renvois affectés.
5. Lier la proposition à la source exacte, avec une justification et des
   points à vérifier. Une source substantiellement modifiée invalide le
   brouillon lié à la version antérieure.
6. Ne compter ni la source importée ni un article inchangé comme une
   réécriture. Ne pas déclarer un code terminé avant contrôle de toute la
   couverture.

## Continuer

`first_drafts.json` et `apply_tax_drafts.py` sont des étapes historiques
d'amorçage. Ne pas les réexécuter sur les propositions courantes : des révisions
archivées leur ont succédé, notamment pour l'IS et la déductibilité de la CSG.
Les orientations actuelles figurent dans `policy-coordinations.json`.

L'IS ordinaire proposé est désormais dû à la distribution : les bénéfices
conservés, même en trésorerie, ne sont pas imposés chaque année. Le taux normal
français proposé de 20 % porte sur le bénéfice avant IS distribué, soit 20/80
du dividende net d'IS, avant fiscalité personnelle de l'associé. Les avantages
de taux réduits sont conservés. La transition doit éviter de taxer une seconde
fois les réserves déjà imposées et les dividendes transmis entre sociétés.
Le minimum international conserve son champ ; le régime français nouveau
n'est pas automatiquement admissible au dispositif réservé aux régimes de
distribution en vigueur au plus tard le 1er juillet 2021.

Les remplacements de propositions existantes passent par `review_prior.commit`
avec les empreintes de la source et de la proposition antérieure. Les articles
nouveaux suivent le registre ordinaire des lots. Les coordinations non rédigées
ne sont pas déclarées achevées.

La dernière consigne conserve expressément la franchise TASCOM et les
dérogations littorales, y compris pour les opérations futures recevables.
L’objectif est moins d’impôts et moins de contraintes : l’examen de toute la
loi SRU ne commande pas de supprimer les avantages qu’elle a créés. Les
anciennes suppressions de ces deux bénéfices sont retirées du projet.

La demande SRU a été précisée : elle couvre toute la loi n°2000-1208 du
13 décembre2000, ses209articles et leurs effets actuels, et non le seul
article55. Le premier lot de82articles codifiés et7textes complémentaires
supprime les quotas et leurs dépendances ; il ne clôt pas le périmètre
intégral. La filiation se suit par identifiant, texte et concordance, jamais
par le seul numéro recyclé. Les dispositions remplacées, censurées ou éteintes
restent identifiées, sans restauration automatique du droit antérieur à2000.
La reprise donne priorité aux pistes SRU présentes dans les cartes, avec les textes initiaux complets joints aux sources assignées. Ces concordances sont des pistes de revue, jamais une preuve automatique de filiation normative.
Le suivi se trouve dans `runtime/sru-integral/`. L’option `--deploy-on-export` publie chaque jalon vérifié lorsque `--export-every` est activé, sur les cinq projets existants. Les abrogations portent sur
les normes actuelles réellement identifiées, avec transitions explicites et
protection des droits déjà acquis. Un article simplement cartographié ne
compte pas comme réécrit.

Les dates et certaines métadonnées LEGI présentent quelques incohérences de
versions. Les deux identifiants sont conservés et les conflits sont signalés
au lecteur. Ne pas les résoudre par une sélection silencieuse.

Après rédaction et contrôle :

```sh
python3 legal-rewrite/register_batches.py --commit
python3 legal-rewrite/build_reader.py
python3 -m unittest discover -s legal-rewrite -p 'test_*.py'
```

Publier depuis `sites/liberer-la-retraite/dist`, lié au projet Vercel
`prj_9PB01NleDnTt1V2QqsH8gwRrHIPb` de `personal-9062d8ea`, après vérification
du projet. Le lecteur est relié depuis les cinq sites. Les autres projets
préservent leurs ressources publiques et leur présentation initiale, avec
un encart identifiant clairement le chantier intégral et l’avant-projet court.

Le projet est éditorial et juridique. Conserver le crédit aux agents IA
d’@alexmasmej et les sources des orientations retenues. Les appels d’adhésion
politique ont été retirés de la présentation.

## Rédaction répartie et reprise

L’utilisateur a autorisé explicitement plusieurs agents. Les lots rédigés
sont conservés dans `batches/`, reliés aux identifiants et empreintes de la
source. Le validateur refuse les sources simplement recopiées, les lots
incomplets, les tableaux amputés et les écrasements de propositions non
enregistrées par ce workflow.

`run_exhaustive.py` exécute une file ponctuelle et reprenable avec la
connexion Codex existante. Il ne crée aucun calendrier et n’achète aucun
crédit. Chaque agent lit son lot entier, écrit des articles complets et
documente les coordinations. Les erreurs d’authentification ou de quota
arrêtent la file. Après trois échecs de validation d’un même lot, celui-ci
reste non accepté et à réécrire, avec les motifs conservés dans
`runtime/exhaustive/failed-jobs.json` ; les autres lots continuent. Une
modification des orientations pendant un lot empêche son acceptation et
demande une reprise avec les règles à jour. Un arrêt demandé laisse finir
les lots déjà en cours. Les dispositions nouvelles ne sont pas réputées
financées ou validées juridiquement du fait de leur rédaction.

```sh
python3 legal-rewrite/run_exhaustive.py --workers 3 --interleave-review --export-every 200 --publish-at-end
```

La reprise alterne deux lots d’articles jamais réécrits et un lot de seconde
passe, en parcourant les codes à tour de rôle. Une file épuisée ne bloque pas
l’autre. Les sources longues restent entières. Le statut distingue les
articles rédigés et ceux déjà réexaminés ; la seconde passe ne gonfle pas le
compteur de réécriture. `--review-prior-first` reste disponible pour une reprise
qui doit exceptionnellement terminer toute la seconde passe avant de rédiger.

Le fichier `runtime/exhaustive/worker-limit.json` permet de réduire le nombre
de rédacteurs simultanés pour réserver un créneau à une vérification manuelle.
Un verrou empêche deux coordinateurs et un second verrou protège les écritures
en base et le registre de lots. Les réformes et leurs coordinations sont dans
`site-summaries.json` et `policy-coordinations.json`.

## Supervision de la poursuite exhaustive

Le service macOS de cet utilisateur `com.libererfrance.exhaustive-rewrite`
exécute `supervise_exhaustive.py` chaque minute, indépendamment de la durée
du chat. Il est installé dans `~/Library/LaunchAgents/` et reprend à la
prochaine ouverture de session. Il adopte le coordinateur actif sans
l'interrompre et relance un coordinateur disparu avec les trois agents, les
cinq codes, les annexes et la seconde passe. L'identité du processus et les
verrous sont contrôlés avant tout lancement. Les tentatives antérieures sont
conservées dans des dossiers distincts, sans acceptation automatique.

Le suivi vérifié des processus est dans `runtime/supervision/status.json` et
son historique dans `runtime/supervision/events.jsonl`. Le compteur d'articles
reste dans `runtime/exhaustive/status.json` : son ancienne mention `running`
ne prouve pas à elle seule qu'un processus travaille. Les futurs arrêts
propres et erreurs Python produisent `runtime/exhaustive/coordinator-exit.json`;
un arrêt externe brutal peut toujours empêcher cette écriture.

Un contrôle horaire de ce chat, « Poursuivre les cinq codes », examine les
blocages qui nécessitent une intervention de l'agent : agents orphelins,
validations refusées, reprises documentaires ou audits finaux. Il reste
silencieux lors d'un fonctionnement normal. La supervision ne contourne
aucun contrôle juridique et ne déclare jamais l'achèvement à partir d'une
sortie réussie ou d'une file vide. Les quotas, connexions nécessaires et
sources indisponibles restent signalés. Le traitement local reprend au réveil
de la machine; il ne travaille pas pendant son extinction ou sa veille.

Pour une pause demandée par l'utilisateur, créer d'abord
`runtime/supervision/disabled`, puis arrêter proprement le coordinateur.
Le marqueur empêche toute relance du service. Suspendre également le contrôle
horaire dans l'application. La suppression de ce marqueur réactive la reprise
au prochain contrôle. Aucun fichier `sources/` n'est modifié par ce dispositif.

## Formules, tableaux et autres éléments non reproduits

Le fonds texte contient 18 articles qui renvoient à des formules, images,
tableaux ou modèles non reproduits. Ils sont recensés dans
`source-image-gaps.json` et ne sont pas traités comme de simples paragraphes
réécrits. La file les réserve pour une récupération documentaire distincte.
Les fichiers officiels complémentaires, images et transcriptions se trouvent
dans `attachments/`, avec manifeste par article dans `attachments/records/`.
Le lecteur et les ZIP incluent ces compagnons et leur provenance, sans
modifier le XML canonique. Les consolidations documentaires ministérielles et
la doctrine historique BOFiP ne sont jamais présentées comme un JO authentifié.
Les contrôles de couverture documentaire et la confrontation au JO restent
deux indicateurs distincts. Un manifeste sans ses fichiers et empreintes
corrects ne suffit pas à compléter un article.

## Présentation courte et téléchargements

Les cinq pages d’accueil présentent les idées sur l’équivalent d’une à deux
pages, puis les téléchargements des codes complets. Les anciennes pages
longues restent accessibles dans `avant-projet.html`. Le lecteur comparatif
est un accès secondaire.

`site-summaries.json` contient les synthèses. Pour les reconstruire :

```sh
python3 legal-rewrite/build_downloads.py
python3 legal-rewrite/build_compact_sites.py
```

Les cinq ZIP par code sont publiés dans `/downloads/` sur le site retraite ;
le CGI inclut les annexes I à IV. Un ZIP commun les rassemble. Chaque archive
contient les sources complètes en HTML, une version de travail complète,
les données JSON et le sommaire. La version de travail remplace uniquement
les articles disposant d’une proposition et conserve les autres sources
explicitement marquées « À réécrire ». Elle ne doit jamais être présentée
comme une réécriture intégrale terminée. Les inventaires et empreintes sont
dans `/downloads/manifest.json`, et le catalogue dans `/telechargements/`.
