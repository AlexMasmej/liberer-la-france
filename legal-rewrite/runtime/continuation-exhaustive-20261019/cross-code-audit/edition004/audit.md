# Concordance004 — douze examens et trois coordinations entières

Les12articles confiés sont capturés et lus intégralement, notes et projets antérieurs compris, dans `audited-source.json`. Les sources et projets des cibles utiles sont joints dans `references.json`. La décision article par article figure dans `review-decisions.json` ; aucun article déclaré compatible n'est compté comme nouvelle rédaction.

## Propositions

Trois articles entiers dans `source.json` et `answer.json` :

- **D241-10** : conserve le facteur favorable1,1 pour les rémunérations de mission des futurs CDI intérimaires, dans le calcul distinct plus favorable. Les intermissions restent comptées selon leurs règles propres. Aucune indemnité salariale nouvelle n'est créée et la formule principale, les facteurs45/35,40/35,100/90 et toutes les autres règles sont intégralement conservés.
- **L241-13**, coordination expressément autorisée par le parent après le premier lot : seul le2° duIV est complété pour donner une base légale au maintien de ce facteur malgré l'exclusion deL1251-19 parL1251-58-4. Tous les autres alinéas de la proposition intermédiaire001 sont strictement identiques, dont le choix plus favorable duIII. Ce n'est pas une remise en cause du paquet28.
- **L1251-54**, cible expressément autorisée par le parent : conserve le seuil de trois mois de missions de l'année civile précédente en prenant les lettres de mission du contrat unique en compte. Le seulCDI ne transforme pas automatiquement l'intérimaire en personnel permanent. Les proratisations/exclusions restent dans leur champ propre et aucun salarié n'est compté deux fois. R752-20 et l'annexeIII49Q bénéficient de cette correction centrale sans nouvelle rédaction locale.

## Ordre d'intégration impératif

**Les28articles des éditions001/002/003 doivent être inscrits avant004.** La proposition intermédiaire entière deL241-13 provient d'`edition001/answer.json` ; elle n'était pas enDB lors de la capture004. Cette distinction est conservée par `captured_database_draft=null`, `beforeimage_status` et `expected_predecessor`.

L'avant-image attendue après inscription du premier lot porte le SHA256 :

`82b9deea2bea9c319ac01ec157540a93d49ff5b118c1a659b77f7cb253e10a0c`

Le champ `previous_draft` deL241-13 représente **cette garde attendue**, pas une assertion de son existence enDB à la capture. `expected.json` porte les gardes à contrôler après le premier lot. `validate.py` distingue explicitement le stade « prédécesseur en attente » du stade « avant-image inscrite exactement ». Il ne valide pas une insertion prématurée de004.

Sources, notes et documents sont inchangés ; les validations structurelles passent sans conflit non prévu au dernier contrôle. Aucun fichier gelé antérieur, base, lot actif, politique ou site n'est modifié par l'auteur.

## Onze articles sans nouveau correctif local

L136-5 ; L161-22 ; L161-22-1-5 ; L315-1 ; L433-1 ; L932-41 ; R243-26 ; R752-20 ; D133-13-4 ; D433-5 ; annexeIII49Q.

Les décisions détaillées préservent les garanties de salaire/cotisations, indemnités d'inaptitude et de retraite, droits sociaux, exonérations ultramarines, absence de doubles attestations et conditions de croissanceJEI. Les conclusions concernantR752-20 et49Q sont conditionnées à l'inscription duL1251-54 coordonné ; elles ne prétendent pas que son ancien texte était déjà suffisamment explicite.

Le délai d'un mois d'inaptitudeL1226-11, les délais médicaux, les pénalités de recouvrement et les échéances de déclaration ne sont pas remplacés par le préavis individuel15jours. L'indemnitémaladieL1226-1 et les prestations d'inaptitude ne sont pas assujetties au seuil d'ancienneté ni au plafond de l'indemnité ordinaire. Les régimes publics, agricoles et les prestations de retraite gardent leurs règles propres, notamment les notes temporelles2027.

## Réserve distincte non résolue

D241-10 renvoie au « septième alinéa duIV » deD241-7 pour une variation de la valeura en cours d'année. LeIV de la source2026 deD241-7 ne contient que cinq alinéas. Ce renvoi pendant est **préexistant** à notre réécriture ; il était également conservé et signalé dans le premier lot. Aucun contenu historique n'a été reconstitué ou présenté comme retrouvé. La formule et l'avantage existants sont conservés, mais cette autre réserve de concordance demeure à traiter sur preuve primaire.

## Restant

Le delta de file est dans `queue-delta.json`. Parmi les1187résultats encore en attente après le premier lot, ces12articles sont désormais examinés ; **1175restent explicitement non étudiés** dans cette file, souvent après un simple résultat large sur « indemnité » ou un contrat financier/locatif. Aucun achèvement juridique de cette file ou des autres codes horscorpus n'est revendiqué.
