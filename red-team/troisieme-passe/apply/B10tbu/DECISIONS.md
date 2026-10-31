# B10tbu — variante de B10 issue de la lecture T047 (palier A)

Texte lu en production (lecture seule), le 30 octobre 2026. Contrôle : `python3 -B apply/check_changes.py B10tbu` construit et valide 1 changement, et `problems` est vide. Le seul diagnostic, `explicit_normative_reduction`, reprend la ligne de lot existante.

## TA-T047-01 : 750 ter II et droits de donation dus au décès d'un tiers — **appliquée**, `loophole_closure`

- **Article touché** : CGI 750 ter (LEGIARTI000024453202), mode `replace`. Il appartient à B10 ; la correction de B10 (RT-DOMSUCC-06, crédits de paiement) est déjà en production et reste intacte.
- **Défaut** (F5) : le premier alinéa du II dispose qu'« aucun droit de mutation à titre gratuit n'est dû [...] à raison d'un décès », quel que soit « le lien de parenté des personnes concernées ». Or A7c a appliqué les volets a et b de RT-DOMSUCC-01, sur décision de l'auteur. Les articles 784 C, 792 bis et 792-0 bis soumettent donc aux droits de donation une libéralité dont l'auteur est vivant, même lorsqu'elle s'exécute au décès d'un tiers (premier gratifié, bénéficiaire du trust ou de la fiducie). La règle générale contredit ainsi ces règles spéciales et laisse plaider l'exonération.
- **Changement** : un seul alinéa est ajouté à la fin du II : « Le premier alinéa du présent II ne fait pas obstacle aux droits de donation dus, dans les cas et conditions prévus aux articles 784 C, 792 bis et 792-0 bis, sur une transmission dont l'auteur, donateur ou constituant, est vivant à la date du décès qui la déclenche. » Le motif et les notes sont complétés. Aucun autre mot n'est modifié.
- **Conservé** : l'exonération totale, sans plafond ni condition, des transmissions dont l'auteur est le défunt ; l'absence de déclaration de remplacement ; le régime des décès antérieurs. Le champ de 784 C, 792 bis et 792-0 bis n'est pas élargi.
- **Point laissé à l'auteur** : le volet assurance-vie de RT-DOMSUCC-01 (primes versées par un souscripteur vivant distinct de l'assuré : 750 ter II, deuxième alinéa, 757 B, 990 I) n'est pas tranché, faute de décision de l'auteur. L'alinéa ajouté ne vise pas ces sommes. Le marquage `loophole_closure` permet à l'auteur de revoir la coordination.

Revue IA : rien de ceci ne vaut validation par un juriste.
