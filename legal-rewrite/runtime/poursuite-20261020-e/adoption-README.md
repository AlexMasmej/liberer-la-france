# Adoption E52 et mise à jour contextuelle bornée C141

`adopt_reviewed.py` est préparé, jamais lancé ni importé par son auteur. Il n’écrit ni base, politique, sites, lots canoniques ou certificats de référence. Son seul effet actif, après lancement explicite du parent, est le remplacement atomique du registre d’audits, avec archive des anciens octets et des trois audits remplacés, puis reçu d’adoption.

La commande future est :

```sh
python3 legal-rewrite/runtime/poursuite-20261020-e/adopt_reviewed.py --root-approval <approbation-root-réelle.json> --execute-approved-adoption
```

Ne pas la lancer avant l’inscription E52, la vraie recapture des cinq identités, l’approbation root de cette capture et de ses analyses, puis l’inscription des cinq réémissions. Le fichier modèle fourni porte `approved: false`. Il ne constitue aucune autorisation. Les chemins qui y seront renseignés sont relatifs à `legal-rewrite/` et doivent rester dans ce dossier.

## Conditions vérifiées

- Registre antérieur exactement453, SHA8b036b9f… ; politique et sites C inchangés, primitives C inchangées et épinglées. Aucun audit CLI46 n’est ajouté.
- Préflight E52, quatre paquets sources/réponses, carte normalisée173arêtes et trois contrelectures indépendantes exacts, avec leurs manifestes. Reçu réel52 :49premières entrées et3révisions.
- Recapture/staging réels sur cinq identités : R243-17, R243-18, R243-19, R243-59 et R243-59-6-A. Capture, approbation root, sources, réponse, snapshot, preuve de staging, producteur et reçu final sont liés par leurs SHA. Le snapshot et chaque certificat natif doivent être actuels en DB après inscription. Aucun certificat futur ne peut remplir cette condition.
- Seuls `reference_checks` et `reference_coherence` peuvent varier entre la ligne canonique capturée et le staging. La ligne C R243-59-6-A vient du C final effectivement inscrit et de son ledger, jamais de l’ancien C/social002. Son impact et son certificat d’impact restent ceux du ledger453.
- Le retrait d’un check natif optionnel ne peut viser que L243-7-6 et doit correspondre, identité par identité, à l’approbation root. Cette dépendance juridique demeure obligatoire dans les quatre audits E sociaux et leur carte. Tous les autres changements de checks sont soumis au validateur natif et à la capture approuvée.
- Les cinq vraies lignes propriétaires de lot après inscription doivent correspondre au staging. Les éventuels champs `policy_review_id` et `prior_proposal_sha256`, actualisés par le mécanisme de révision, sont comparés séparément aux valeurs explicitement approuvées par root ; aucun autre champ n’est exempté de l’égalité.
- Les52audits E épinglent seulement leurs dépendances juridiques normalisées par article ; les contrôles natifs de référence sont vérifiés séparément. Les dépendances documentaires restent liées aux preuves figées. Aucun épinglage global tous-à-tous.
- Les141audits C conservent intégralement corps/source/notes/impact/certificat et tous autres champs. Seuls les `proposed_sha256` de gardes déjà présentes peuvent être remplacés, sur sept cibles exactes et approuvées :1133ter/quater/1704D, L243-7-6, R243-18/-19/-59E. Une modification de source, notes, identité, autre cible ou impact bloque toute l’adoption avant écriture. Les preuves de compatibilité sociale141 et fiscaleD sont séparées et épinglées.
- Les trois anciens audits C R243-17/-18/-19 sont remplacés par les nouvelles analyses E, avec historique. Les309autres audits antérieurs restent entièrement identiques. Résultat attendu :502audits (49ajouts,3remplacements ;141contextes seulement, sans nouvelle lecture sémantique141 annoncée).

Toutes les gardes, preuves et politiques sont revérifiées sous le verrou partagé et une transaction de lecture cohérente. Le registre est archivé avant écriture. Toute divergence autre que les sept gardes approuvées exige une nouvelle décision/revue ; le script ne propose pas de substitution automatique.

Le bilan sémantique global et les montants nationaux restent inconnus. Les nombres d’articles ne deviennent pas des nombres de simplifications.

## Approbation réelle à renseigner par root

Le modèle contient les SHA fixes connus. Root doit y ajouter ses propres approbations des vrais états : le SHA du présent helper figé, les chemins/SHA du reçu52 et de chaque fichier de recapture/staging/inscription, la liste des cinq identités, la carte exacte des retraits optionnels (y compris les listes vides) et les cinq cartes de provenance finales. Les valeurs ne sont pas déduites d’une hypothèse de succès.

Vérification de l’auteur : analyse syntaxique AST et dix tests de la seule transformation pure des gardes (non approuvée, source différente, notes différentes, doublon, pin manquant et autre cible sont bloquants). Le helper complet n’a été ni importé ni lancé ; aucun accès DB ou mutation active par ces tests.
