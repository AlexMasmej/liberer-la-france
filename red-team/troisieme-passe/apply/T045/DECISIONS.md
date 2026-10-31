# T045 : décisions (lecture systématique, palier A)

Ce groupe couvre les articles 638 à 680 du CGI : enregistrement, délais, services compétents, champ des droits et de la TPF, tarifs généraux. La production a été lue le 2026-10-30.

## TA-T045-01 : CGI 648 (LEGIARTI000006305185), appliquée

- **Défaut (G, F8/F5).** Le premier alinéa proposé retire « ou celui de l'ouverture de la succession » pour tous les nouveaux décès.
  - Or le projet conserve un délai d'enregistrement qui court d'un décès futur : le délai d'un mois suivant le décès du donateur, prévu au a de 635 A pour les dons manuels, sur option du donataire.
  - Le jour du décès entre donc dans le calcul de ce délai, qui est raccourci d'un jour. Ce délai est sanctionné par 1728.
  - Les notes affirmaient le contraire.
- **Correction (mode replace, ligne successions/204).**
  - La règle source du premier alinéa est rétablie.
  - La garde « ne crée aucun délai de déclaration ou de paiement de droits de mutation par décès » pour les nouveaux décès est conservée.
  - Le texte précise que l'article s'applique aux délais qui subsistent, notamment celui de 635 A, a, ainsi qu'aux délais des décès antérieurs.
- **Champs de la ligne.**
  - `change_type`, `reform_policy_id` et `removed_provisions` sont mis à null : plus aucune disposition n'est retirée.
  - `substantive_impact` est mis à jour, avec une citation exacte. `benefit_review` aussi.
- Aucune taxe, aucun délai, aucune formalité ni sanction nouvelle.
- **Pour l'auteur :** rien.

## TA-T045-02 : CGI 654 (LEGIARTI000006305195) et annexe III 281 P (LEGIARTI000048806797), demande au groupe Y17

- **Défaut (G, F1/F5).** L'article 654 proposé ouvre le dépôt dans « tous les services des impôts indistinctement ». Il rend inopposables les restrictions réglementaires de lieu.
  - Or 281 P proposé impose encore le dépôt de la déclaration de 639 au service du domicile de l'une des parties.
  - Les articles 281 E et 281 N ont été alignés (RT-P1-CGI-C-11). 281 P a été omis.
- **Demande.** Remplacer seulement ce rattachement par « auprès de tout service des impôts, dans les conditions de l'article 654 du même code ». Le texte complet figure dans `requests`.
- L'article n'appartient pas au paquet : il n'est donc pas modifié ici.
- **Pour l'auteur :** la désignation de l'annexe IV 60 A, maintenue, pourrait être harmonisée de la même façon. C'est un point résiduel, non corrigé.

## Autres articles

- **CGI 678 :** `m` (F7). La première phrase d'abrogation est circulaire, sans effet. L'article n'est pas modifié.
- **27 articles notés `0`.** Les articles 641 (B10) et 650 (B05) sont à `0` : aucun dossier de variante n'a été créé.

## Résumé

| | |
|---|---|
| Décompte | 2 G, 1 m, 27 × 0 |
| Corrections | 1 (648) |
| Demandes | 1 (281 P, groupe Y17) |
| Écarts (`skipped`) | aucun |
| Validation | `check_changes.py T045` : `problems` vide |

Revue IA : ce n'est pas une validation par un juriste.
