# J16tet — variante de T124 pour l'annexe IV 41 septies A (LEGIARTI000054606058, ancien propriétaire J16)

Revue IA, sans validation par un juriste.

## TIERA-T124-02 — appliquée (absorbe la demande TA-T041-02 de T041 à J16)

### Défaut (G, F1 + F5)

1. **Liste récapitulative EDI.** Le 3° b du I exigeait encore de la plateforme de « tenir et conserver en matière d'échange de données informatisé, une liste récapitulative séquentielle de tous les messages émis et reçus et de leurs anomalies éventuelles, par utilisateur ». Or cette liste est supprimée par l'annexe III 96 G proposée, qui interdit à l'arrêté de l'imposer « ni un registre équivalent ». 41 septies la supprime aussi (TIERA-T124-01).
2. **Renouvellement du numéro.** CGI 290 B proposé attribue le numéro d'immatriculation « sans limitation de durée. Aucun renouvellement périodique de ce numéro n'est exigé ». L'article organisait pourtant encore l'audit de renouvellement (II 2°) et renvoyait deux fois à 242 nonies C (chapeau du I et III). L'abrogation de 242 nonies C est proposée par TIERA-T082-01.

### Correction

- Le tiret sur la liste EDI est supprimé.
- Le renvoi au « 1° du I de l'article 242 nonies C » est retiré du chapeau du I.
- Le 2° du II est abrogé.
- Le renvoi au « IV de l'article 242 nonies C » est retiré du III.
- Deux phrases de transition sont ajoutées au IV :
  - l'audit de renouvellement prend fin à l'entrée en vigueur de 290 B réformé, audits en cours compris, et les rapports remis gardent leurs effets ;
  - le contrôle de la liste prend fin pour les rapports remis après la suppression de la liste dans 96 G.
- Aucun contrôle ni registre de remplacement n'est créé.
- La partie « renouvellement » reprend mot pour mot le texte demandé par T041.

### Ce qui ne change pas

L'audit initial (II 1°), la piste d'audit fiable, la signature électronique, la sécurité, le RGPD et l'annuaire restent en place.

### Pièces mises à jour

- Motif et notes.
- `removed_provisions` : deux entrées ajoutées.
- `substantive_impact` : deux coordinations ajoutées, `factures-edi-suppression-liste-sequentielle` et `plateformes-tva-fin-renouvellement-triennal`. La citation de l'effet « fichier partenaires » est réancrée sur le IV.

### Dépendances

- Appliquer avec TIERA-T082-01 (242 nonies C) et TIERA-T124-01 (41 septies).
- La demande TA-T041-02 adressée à J16 n'a plus à être traitée séparément.

### Diagnostic du validateur

Le diagnostic `references_changed` signale le retrait de R123-221. Il vient de l'abrogation, antérieure, du 4° du I (comparaison avec la source) : ce n'est pas un effet de la présente correction.
