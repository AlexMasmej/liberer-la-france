# Diagnostic local des modèles CCH — 22 octobre 2026

**Conclusion : les deux échecs finaux sont des faux positifs lexicaux sur cinq champs authentiques du modèle. Aucun correctif actif, enregistrement, modification de DB, changement de capacité ou appel à un autre modèle n’a été effectué. Les quatre articles restent non traités.**

## Preuves et déclencheurs exacts

Les copies intégrales des deux lots sont sous `evidence/`; `manifest.json` donne chemin original, SHA-256 et taille de chaque fichier. Les textes sources, notes et propositions sont aussi extraits sous `articles/`, avec leurs différences exhaustives. Les offsets ci-dessous sont des caractères Python, origine zéro, dans le XML décodé ; les lignes sont à origine un. `inventory.json` contient les métadonnées et les positions.

| Lot | Article | Champ | Source : ligne / offset | Proposition : ligne / offset |
|---|---|---|---|---|
| 00194 | LEGIARTI000045646952, annexe I R423-86 | montant du capital `[…]` | 46 / 4928 | 46 / 5498 |
| 00194 | même article | nombre d’actions `[…]` | 48 / 4969 | 48 / 5539 |
| 00194 | même article | valeur nominale `[…]` | 48 / 5018 | 48 / 5588 |
| 00195 | LEGIARTI000045646995, annexe II R423-86 | capital statutaire `[…]` | 51 / 5322 | 51 / 6345 |
| 00195 | même article | valeur nominale des parts `[…]` | 55 / 6012 | 55 / 7035 |

Phrases probantes de l’annexe I : « Le capital est fixé à la somme de […] euros. » et « Il est divisé en […] actions nominatives d'une valeur nominale de […] euros chacune, toutes entièrement libérées. » Annexe II : « Le capital statutaire est fixé à la somme de […] euros. » et « La valeur nominale des parts sociales est de […] euros. » Les clauses 5 complètes sont strictement conservées, y compris les contraintes et facultés de détention du capital. Aucune valeur ne peut être inventée pour remplir ces champs.

Les deux premiers articles de 00194, LEGIARTI000039049511 et LEGIARTI000032660331, ne contiennent **aucune** occurrence du motif bloquant. Le premier utilise cinq blancs à points dans territoire, siège et capital ; le second utilise notamment `(nom de la société)`, `(...)` pour les compétences et des points pour siège et capital. Ces formes sont également héritées, mais ne correspondent pas à l’expression régulière actuelle. L’échec du lot 00194 intervient sur son troisième article.

## Contrôles actuels et historique

`controls/run_exhaustive.py:187-231` est la copie du contrôle en place. Ligne 228, `TODO|\[(?:…|\.\.\.|à compléter|texte inchangé)\]` est cherché dans le texte normalisé, sans comparaison avec la source. Le premier champ officiel suffit donc à lever « Incomplete placeholder ». La normalisation de `Markup.result()` conserve les crochets et l’ellipse.

Le second verrou `controls/register_batches.py:107` refuse aussi ces champs avec un motif plus large (espaces internes et `<placeholder>`). Corriger seulement le coordinateur ne permettrait pas une admission cohérente. Il faut une même décision fondée sur les preuves aux deux points, sans toucher aux autres contrôles : identité, versions, intégrité HTML, impact, avantages, graphiques, tableaux, longueur, renvois et protections d’enregistrement.

Les deux `validation-failure.json` portent `attempt: 3` et exactement « Incomplete placeholder ». Les six exécutions observées sont vérifiées ; les six processus ont un code de sortie 0 et chaque résultat annonce respectivement 3 ou 1 article. Cela prouve une réponse produite, pas sa validation. Les journaux et leurs métadonnées sont conservés en entier ; les fichiers `*-log-audit.json` indexent les lignes d’erreurs et de validation. Une `AssertionError` de construction apparaît en 00194/errors-1.log:1475-1481 : remplacement d’une chaîne absente dans le premier article. La commande suivante corrige ce problème et écrit trois articles. Ce défaut transitoire n’est pas l’erreur finale. Il n’existe pas trois instantanés séparés d’answer.json dans les lots : la présente comparaison des textes porte sur leur dernière version copiée, pas une reconstitution garantie des trois réponses intermédiaires.

## Champs, troncatures, sources absentes, omissions

- **Champs officiels exacts :** les cinq occurrences du tableau, les autres blancs typographiques, les variantes de gouvernance et notes « Rayer la mention inutile » sont des éléments de modèle. Les options ne sont pas des permissions pour le rédacteur de supprimer une version du modèle entier.
- **Anomalie source préexistante :** annexe II, clause 6.1, `articles/LEGIARTI000045646995/source.xml:95`, contient déjà « période de préavis de mois ». La proposition le conserve et `review_notes` le signale. Aucun nombre ne doit être déduit du préavis salarial de quinze jours. La preuve locale établit l’antériorité du blanc ; elle ne permet pas de certifier une durée manquante ni de trancher entre blanc volontaire et anomalie de publication.
- **Notes :** les quatre `source_notes_xml` sont vides. Les notes normatives visibles sont dans `source_xml` et sont conservées : notamment les quatre notes des annexes I et II. Notes séparées vides ne signifie donc pas modèle dépourvu de notes.
- **Troncature introduite :** aucune des cinq ellipses ne remplace du texte source supprimé. Les diffs exhaustifs montrent des modifications ponctuelles de charges, puis transitions, et non le remplacement d’une section par un blanc. Les clauses finales 16, 11, 13 et 15 restent présentes. Ce constat local ne vaut pas approbation de fond de toute réforme.
- **Sources extérieures manquantes :** les métadonnées de R423-85 signalent que les versions historiques complètes des articles renumérotés ne sont pas fournies ; l’annexe II réserve les règles impératives de notification de la loi de 1947 et du code de commerce hors lot. Ce sont des limites de concordance, à ne pas transformer en champs authentifiés. Les notes relèvent aussi une discordance entre la faculté de détention à 50 % des annexes de 2022 et la version législative fournie. Aucun droit favorable n’est retiré pour masquer cette discordance.
- **Omission des rédacteurs :** aucun champ numérique n’a été oublié par rapport aux sources copiées. Les `reference_checks` correspondent aux exigences enregistrées du snapshot (aucune cible manquante ou supplémentaire dans ce contrôle statique), y compris les listes vides exigibles pour les deuxième et troisième articles de 00194. Cela ne remplace pas `accept_checks` avec catalogue courant ni son contrôle de fraîcheur. Les limites de concordance explicitement reconnues restent ouvertes.

## Conservation des clauses favorables

Le diff préserve les dispenses de cession intrafamiliale/successorale, dérogation au prix et garanties de rachat, agrément réputé donné, plafonds 35/49 %, absence de quorum, facultés de dividendes et transferts de réserves de R422-37. R423-85 garde notamment la non-application de L443-14 et ses deux gouvernances. Les annexes I/II gardent la non-application de L443-14, capital ouvert à 50 %, droits préférentiels et exceptions de L423-5, cession libre entre associés, prix minimal de rachat, agrément acquis, vote par correspondance, distributions et affectation sociale. L’annexe II conserve la dispense de dépôt/publication des variations de capital, retrait/remboursement et caractère facultatif de sa clause 11 selon la note 4. Les notes de transition protègent les situations éligibles futures et régimes historiques. Cette vérification documentaire n’est pas une certification juridique.

## Proposition strictement limitée, hors production

`prototype.py` et `certified-fields.proposed.json` démontrent une **validation positive des cinq intervalles**, pas une liste blanche de mots. Le registre proposé est limité aux deux identités/version source exactes ; il distingue le `source_sha256` du corpus du SHA-256 des octets de `source_xml` (ces deux empreintes ne sont pas interchangeables). Il scelle également les notes, la clause 5 entière, ses bornes uniques et la liste exacte des positions/champs. Une autre source, un changement de version, une clause tronquée, une valeur inventée, un nouveau champ ou marqueur hors des cinq positions est refusé. Le texte juridique n’est jamais réécrit ni nettoyé pour satisfaire le test.

À intégrer seulement dans un futur correctif examiné : extraire cette décision en fonction partagée des deux contrôles, produire un certificat traçable et conserver tous les autres verrous. Le registre ne doit pas être fourni librement par le rédacteur ni être dérivé automatiquement de toute ellipse présente dans n’importe quelle source. Les notes ne doivent pas pouvoir justifier une ellipse introduite. Tout changement de clause/corpus exige une nouvelle preuve, pas une tolérance générale. Aucune généralisation à tous les statuts ou à tout le CCH.

**Limites du prototype :** c’est seulement le verrou lexical isolé. Il ne vérifie pas l’ordre global des clauses, ni les suppressions sans marqueur, ni la validité juridique. Le futur raccordement doit maintenir les contrôles de complétude et de subdivisions et tester le déplacement de la clause entière ; l’identité de la clause ne suffit pas à autoriser un déplacement. Il ne faut pas utiliser son retour positif comme certificat d’article traité. Un résumé sans marqueur doit continuer à être refusé par les autres contrôles et la revue de contenu ; aucune expression régulière ne garantit seule l’absence d’omission.

`tests.json` : **32 cas isolés réussis**, sans DB et sans pipeline actif. Cas positifs : quatre propositions au seul verrou des champs. Cas négatifs : ellipses nouvelles, ellipses avec espaces/entités HTML, TODO, texte inchangé, à compléter, placeholder, montant inventé, mots de capital supprimés, borne supprimée, source modifiée, identité inconnue et registre absent. Aucun test n’a déclaré un article complet.

## Périmètre et état de livraison

Seul ce dossier de diagnostic a été écrit. Les preuves sont copiées byte-for-byte et hachées ; `sources/`, lots originaux, catalogue, politiques, DB, run_exhaustive.py actif, coordinateur unique58514 et limites 6+2 n’ont pas été modifiés. La saturation disque signalée pendant le travail a interrompu une lecture par heredoc ; la lecture a été reprise sans fichier temporaire. Aucun test créant une base n’a été lancé. Le dossier est un diagnostic et une proposition à examiner, aucune activation.
