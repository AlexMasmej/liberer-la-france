# R4 — demandes de correction des groupes BL1 à BL5 (paquet `audit/baseline/requests-R4.json`)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`, `query_only`), le 31 octobre 2026. Aucun article n'avait de changement en attente dans les dossiers de `audit/baseline/fix-folders.json`. Revue IA, sans validation par un juriste.

Décompte : 6 demandes, 6 appliquées (dont 1 resserrée), 0 non appliquée.

1. **CCH R862-3, version au 1er janvier 2027** (LEGIARTI000054394516, groupe Z05) : demande BL1-R862-3 **appliquée** (`apply/Z05bf`, mode `new`).
   - Le renvoi aux « motifs mentionnés aux 1° et 2° du présent article » devient « aux a et b du présent 1° ». Au 4°, la citation de R824-15 porte « L'organisme payeur adresse », comme R824-15 au 1er janvier 2027 (LEGIARTI000054394490, sans proposition).
2. **CCH D331-80** (LEGIARTI000039048289, sans groupe) : demande BL1-D331-81 **appliquée** (`apply/R4`).
   - Un troisième alinéa limite la section aux prêts consentis jusqu'au 31 décembre 1985 par la caisse de prêts, remplacée en 1986 pour leur seule gestion (L431-3). Les conventions et les droits des occupants sont conservés, sans prêt nouveau ni formalité de remplacement.
   - Ajouts de R4 : l'effet de coordination existant (D331-8 → D331-14) est gardé dans le bilan d'impact ; les phrases périmées des notes et du `benefit_review` (« succession à confirmer, sans suppression du financement ») sont rectifiées.
   - Pour l'auteur : constat déclaratif (aucun prêteur n'existe depuis 1986). À relire si l'on veut rouvrir un financement sur ce fondement.
3. **Travail L323-34** (LEGIARTI000006648694, sans groupe, maintenu) : demande BL1-L323-21 **appliquée** (`apply/R4`).
   - L'alinéa « - les modalités d'application de l'article L. 323-21 ; » est retiré ; le reste est inchangé. À appliquer avec `apply/W08ba` (abrogation de L323-21).
   - Pour l'auteur : L323-34 survit seulement pour les collectivités de L323-2, abrogé au 1er janvier 2020. Son sort d'ensemble n'est pas tranché.
4. **CSS R162-20-2** (LEGIARTI000006747545, sans groupe) : demande BASELINE-BL2-R162-20-1 **appliquée** (`apply/R4`).
   - Les trois mentions du « Comité économique du médicament » deviennent « Comité économique des produits de santé » (L162-17-3), comme à R162-20 et R162-20-1 (BL2). La citation du bilan d'impact est mise à jour.
5. **CCH annexe III à D353-190, article 21** (LEGIARTI000039048922, groupe J06) : demande BASELINE-BL2-D353-137 **appliquée** (`apply/J06bf`).
   - Le cautionnement d'un mois n'est plus « revisable en fonction de l'évolution du loyer » (article 22 de la loi n° 89-462). Les cautionnements des baux en cours sont inchangés. C'est la rédaction déjà retenue à l'article 20 des annexes V à D353-127 et III à D353-32.
6. **CSS R731-1** (LEGIARTI000006752999, sans groupe) : demande BL5-R731-8 **appliquée en version resserrée** (`apply/R4`).
   - L'obligation du premier alinéa est limitée aux institutions autorisées avant l'abrogation de L731-1 (loi n° 94-678, art. 16). Les garanties de L911-1 et les institutions du titre III du livre IX sont hors champ. Droits des adhérents conservés, sans formalité de remplacement.
   - Écart avec la demande : le texte demandé limitait « le présent chapitre » entier. Cela aurait contredit R731-22 proposé, qui ouvre la remise des majorations aux « institutions constituées ultérieurement ». Cela aurait aussi restreint la faculté des collectivités de R731-17, qui ne repose pas sur L731-1. La limitation porte donc sur l'obligation du premier alinéa, et R731-17 et R731-22 sont expressément réservés.

Contrôle : `python3 -B apply/check_changes.py` sur R4, Z05bf et J06bf : `problems` vide. Diagnostics : renvois modifiés seulement, tous voulus.

Revue IA : rien de ceci ne vaut validation par un juriste.
