# T083 — lecture systématique, palier A (annexe II, articles 242-0 C à 272)

Paquet : 23 articles, lus en production. Résultat : 2 G, 4 m et 17 sans défaut (détail dans `audit/tier-a/T083.json`).

## TIERA-T083-01 : annexe II 242-0 C (LEGIARTI000030066036), appliquée dans la variante `apply/Y15tde/`
- L'article appartenait déjà au groupe Y15. La décision est détaillée dans `apply/Y15tde/DECISIONS.md`.
- Le III vise désormais le 3 de l'article 287 « dans sa rédaction en vigueur avant le 1er janvier 2027 », pour les exercices que le 8 de 287 proposé maintient sous ce régime.
- Cette correction exécute la demande TIERA-T081-02, que T081 avait adressée au groupe Y15. Le coordinateur ne doit pas l'appliquer deux fois.

## TIERA-T083-02 : annexe II 244 (LEGIARTI000030974877) et annexe III 266 bis (LEGIARTI000030829535), demande au groupe T109
- Défaut G (F1, F5). Le I de 244 proposé supprime la déclaration spéciale d'achèvement. Pourtant, le 1° du I de 266 bis proposé fait encore de son dépôt la justification des travaux exigée par le A de 1594-0 G.
- Demande : le 1° vise la déclaration de l'article 287, qui porte déjà le montant de la livraison à soi-même et la liquidation de la taxe. Les déclarations spéciales antérieures restent valables.
- La correction n'ajoute aucune formalité. L'article 244 n'est pas modifié.

## Défauts mineurs, non corrigés (articles non modifiés)
- 260 G (groupe J09) et 260 J (groupe Y15) : les notes disent que l'option quinquennale de 1693 bis I est « non modifiée ». Or 1693 bis proposé la rend « sans durée minimale d'engagement ».
- 266 : la réserve des « obligations autonomes de délivrance des attestations » est ambiguë face à 290 bis proposé.
- 267 quinquies : sa base, 302 septies A, est abrogée au 1er janvier 2027. Les articles D. 162-10 à D. 162-12 du CIBS, hors corpus, organisent aussi cette option.
- Hors paquet : la transition de 242 septies J dit encore que « Les montants minimaux [...] demeurent inchangés », alors que 242-0 C les supprime.

## Point pour l'auteur
- Après la LF 2025, 242-0 C (I, 2) garde la voie du régime simplifié pour les seuls exercices résiduels. Sa reprise par le CIBS reste hors corpus.

Contrôle : `python3 -B apply/check_changes.py T083` renvoie `problems` vide (aucune modification, 1 demande).

Revue IA : ce n'est pas une validation par un juriste.
