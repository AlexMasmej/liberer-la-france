# Y09b : variante pour le groupe Y09, rédigée par X2 (troisième audit aléatoire, Q158)

## Q158 — CCH R452-25 (LEGIARTI000032193202) : appliqué

- **Défaut confirmé (F4).** La proposition disposait : « Le présent article ne prolonge pas l'application de l'article L. 452-5 au-delà de son abrogation prévue au 1er janvier 2027. » C'est inexact :
  - la version LEGIARTI000048839976 de L452-5 est `ABROGE_DIFF` seulement parce qu'elle est remplacée au 1er janvier 2027 ;
  - elle est remplacée par la version LEGIARTI000053151495, issue de l'ordonnance n° 2025-1247 ;
  - cette version maintient l'article et porte une proposition (lot `third-pass-corrections/00006.json`).
- **Correction.** La phrase est remplacée par : « Les renvois du présent article à l'article L. 452-5 visent cet article dans ses rédactions successives, y compris celle applicable à compter du 1er janvier 2027. »
- **Notes.** Les affirmations « support successeur non fourni » et « Point non vérifiable : le texte successeur et l'acte d'abrogation de L452-5 au 1er janvier 2027 manquent » sont rectifiées.
- **Ce qui ne change pas.** La suppression du modèle de déclaration obligatoire, le calcul de référence des versements favorables et la préservation des années antérieures.
- **Contrôle.** `python3 -B apply/check_changes.py Y09b` donne `problems: []`.

Revue IA : ce n'est pas une validation par un juriste.
