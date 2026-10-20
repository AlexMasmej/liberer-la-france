# Revue indépendante de382-0Cter — édition002 du parent

Source, note DILA vide et proposition antérieure entières lues. Les quatre références1679quinquies,1681ter,1681quaterA et1724quinquies, ainsi que les deux entrées canoniques382-0Cbis et leurs propositions, ont également été lues entièrement. Les deuxCbis sont conservés séparément dans la preuve : ils ont des identifiants distincts et des sources différentes mais la même proposition actuelle ; aucune version n'a été choisie silencieusement.

L'édition002 examinée est celle du parent : sourceSHA25653767105ea941d1caa29f664bab4c4e52ad30c330ed59033c9089a6ca19bcf8b ; réponseSHA25607ed3c9f6921cbe2f5f85d797bc0652ad3e772b88d278160fdb9c00986956fb8. Le seul changement du corps par rapport au candidat fiscal initial est la précision «y compris les parts non encore prélevées, sans avancer leurs échéances» dans le calcul du solde. Les copies sont figées dans edition002/.

## Constat concret à coordonner

Cette précision protège contre une deuxième perception et contre l'anticipation des parts futures lors du calcul du solde. Elle ne tranche toutefois pas explicitement le plafond législatif de novembre fixé auC de1681quaterA :

> Le solde des taxes est prélevé en novembre à concurrence du montant de l'un des prélèvements visé au B. Le complément éventuel est prélevé en décembre.

Le B définit les mensualités ordinaires de janvier à octobre. Les deuxCbis proposés permettent une prise d'effet au mois suivant pour les échéances mensuelles encore ouvertes ; la dernière première échéance ordinaire est donc octobre. L'étalement d'un rattrapage qui commence alors conduit à des parts en octobre, novembre et décembre. Cela ne crée pas une première échéance ordinaire en novembre ou décembre.

Contre-exemple illustratif, sans chiffrage budgétaire : mensualitéB de100€, rattrapage déjà déterminé de400€, premier prélèvement en octobre. La seule deuxième part du rattrapage vaut environ133,33€ en novembre. Elle dépasse100€, même en réservant toutes les parts futures dans le calcul du solde ordinaire et même si ce dernier est nul. L'égalité exacte des parts et l'arrondi de centimes ne changent pas cette difficulté : dès que le rattrapage dépasse trois mensualitésB, sa part de novembre dépasse le plafond.

LeF autorise un décret à fixer les modalités. Il ne dit pas expressément que des parts de rattrapage échappent au plafond duC. Le texte légal ne distingue pas à cet endroit un «solde ordinaire» d'un rattrapage qui pourrait s'y ajouter sans limite. La distinction de ces étiquettes ne suffit donc pas à certifier une dérogation réglementaire certaine. Aucune doctrine ou décision primaire établissant cette exclusion n'a été fournie ; le rédacteur fiscal a confirmé ce point et rejoint la recommandation d'une coordination législative expresse. Le calendrier ancien deCbis, qui fermait la prise d'effet la même année après les options du premier semestre, n'exposait pas de la même manière les trois parts au mois de novembre.

**Recommandation : coordonner expressément leC de1681quaterA**, de manière limitée aux parts de rattrapage étalées régulièrement, afin de permettre leur perception aux échéances choisies y compris en novembre, sans les confondre avec le solde ordinaire plafonné. Le calcul du solde doit réserver les parts encore dues sans en avancer les échéances ni créditer fictivement un paiement déjà encaissé. Il faut garder leD : arrêt lorsque les sommes effectivement prélevées atteignent l'impôt, remboursement du trop-perçu et aucune double imputation. Une disposition législative ciblée suffit ; cette revue ne propose pas d'abroger ni de réécrire sans étude tout le régime de1681.

La conclusion n'est pas que tout étalement de trois versements est interdit. Le cas doit être sécurisé au bon niveau normatif ; le seul Cter002 ne peut pas être déclaré sans réserve entièrement opérant pour la dernière première échéance d'octobre.

## Autres points examinés

- L'étalement est facultatif pour les redevables d'acompte et demeure la solution par défaut pour ceux qui n'y sont pas soumis : aucune facilité existante n'est retirée.
- Le paiement immédiat reste possible ; le choix ne requiert ni nouveau formulaire ni preuve supplémentaire.
- L'excédent d'acompte reste remboursable avant la fin du mois suivant l'option ; les imputations et remboursements déjà acquis et l'acompte dont le contribuable était dispensé ne sont pas recréés.
- Les échéances ordinaires de novembre/décembre duC, le cas de rôle émis après le31octobre et les sanctions de1724quinquies restent des régimes distincts ; une option ne fait pas disparaître rétroactivement une dette ou un retard antérieur. Le respect des nouvelles parts ne doit pas, en lui-même, être sanctionné comme défaut de paiement.
- La fin d'année ne doit pas transformer une option d'octobre en une première mensualité ordinaire de novembre : lesCbis renvoient aux échéances mensuelles restantes, puis à janvier suivant lorsqu'il n'en reste aucune. Le regroupement de janvier avec février pour certaines options de fin décembre est préservé.
- Le montant final de l'impôt, l'assiette, le taux, les exonérations, le plafonnementCFE et la suppression de laCVAE ne changent pas.

La classification **payment_timing_relief**, effet **payment_deferred**, est correcte pour cette proposition. Ce n'est ni une taxe supprimée, ni une baisse de taux, ni une économie nationale chiffrée. L'effet de trésorerie pour les contribuables peut avoir un coût de trésorerie pour la personne publique, non mesuré ici.

## Gardes et portée

Les sept corps source, leurs documentsARTICLE et empreintes, notes et avant-images concordent au contrôle en lecture seule enregistré dans checks.json. validate_answer et substantive_impact.validate passent, et les fichiers002 sont identiques à ceux du parent. Ces contrôles d'intégrité ne lèvent pas la coordination de fond ci-dessus. Aucun fichier de l'auteur, base, politique, lot, module ou site n'a été modifié.
