# Groupe T044ia — variante de T044 pour l'issue GitHub #17 : décisions

Base : production en lecture seule, 4 novembre 2026. Contrôle : `python3 -B apply/check_changes.py T044ia` → 1 ligne construite, 1 validée, `problems: []`. Le diagnostic `explicit_normative_reduction` est voulu : il ne liste plus que les réductions du 5° du 1 et du 7° du 2. Dossier principal et vérifications : `apply/I17/DECISIONS.md`.

**Revue IA : rien de ceci ne vaut validation par un juriste.**

## RT-ISS17-01 — appliquée

**CGI 635** (LEGIARTI000042911346, lot `automatic-impots/00090.json`), mode `replace`.

- Corps : seul le 9° du 1 change. Il redevient « 9° La transaction prévoyant, en contrepartie du versement d'une somme d'argent ou de l'octroi d'un avantage en nature, le désistement du recours pour excès de pouvoir formé contre un permis de construire, de démolir ou d'aménager. » Le reste du texte est identique au lot de production (vérifié par diff).
- `removed_provisions` : la ligne « Enregistrement au seul titre du désistement des nouvelles transactions couvertes par L600-8. » est retirée. Les lignes du 5° et du 7° restent.
- `substantive_impact` : l'effet `transactions-urbanisme-dispense-enregistrement` est retiré. Les effets `operations-sociales-sans-droits-dispense` et `cessions-droits-sociaux-hors-immobilier-exoneration` restent. La classification `material_reduction` est inchangée.
- `reason` et `assessment` : la phrase sur la « contradiction effective avec L600-8 proposé » et la phrase « Le 9° est borné aux anciennes transactions » sont retirées. La coordination du 7° avec 726 IV est conservée.
- `review_notes` et `scope_limitations` : les phrases « Transition compatible : L600-8 garde pour les seules anciennes transactions… » et « Différence de champ : … sa dispense directe… » sont remplacées par une phrase de coordination exacte. L600-8 est maintenu en vigueur, et 680 garde l'exonération de droit fixe. La différence de champ préexistante reste signalée. La phrase « Correction de la troisième passe » est ajoutée à la fin des notes.
- Points laissés à l'auteur : aucun propre à cette variante.
