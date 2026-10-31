# BM1 — décisions (troisième passe, réparation de l'échantillon apparié)

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite `mode=ro`). Preuves sous `evidence/cited/production-20261031/`. Une consultation de Légifrance le 31 octobre 2026 : ordonnance n° 2026-648 du 22 juillet 2026 (JORFTEXT000054456926), art. 1er, 4° et 12°.

## Bilan

- 7 articles : 4 corrigés, 1 déjà réglé, 2 non corrigés.
- Dossiers : `apply/BM1` (R2145-4, R4626-27), `apply/T109ca` (annexe III 265), `apply/W03ca` (D752-6). `check_changes.py` : `problems: []` pour les trois.
- 4 requests (R752-20 → W01 ; D3141-37 et R2145-5 → sans groupe ; R315-77 → Z05), 2 skipped (annexe II 202 hors corpus ; R315-78 déjà réglé), 1 texte non codifié (coordination CIBS, non appliqué).

## Article par article

### Annexe II 202 (LEGIARTI000028505612, T080) — introduit — non corrigé (hors corpus)
- La dénonciation « pour tout ou partie des baux » repose sur le 6° de CGI 260 proposé (« un ou plusieurs baux »). 260 (LEGIARTI000025576729) est ABROGE_DIFF au 1er janvier 2027 (ordonnance n° 2025-1247, art. 9) ; le texte successeur du CIBS n'est pas au corpus et aucune proposition ne l'atteint.
- La suppression de la durée minimale relève du décret (260, dernier alinéa) et pourrait tenir seule ; la dénonciation partielle non. Corriger sans le CIBS reviendrait à inventer son contenu ou à retirer un choix de l'auteur.
- Texte non codifié de coordination proposé sous `uncodified` (non appliqué). Point pour l'auteur : reporter la réforme de 260, 194 et 202 dans le CIBS. Dossier `T080ca` non créé.

### Annexe III 265 (LEGIARTI000052219103, T109) — introduit — corrigé (`apply/T109ca`, loophole_closure)
- 1594 F septies maintenu (LEGIARTI000054373157) : affectation « exclusivement et de manière continue » pendant cinq ans ; le décret ne fixe que « les cas dans lesquels le respect de cet engagement n'est pas exigé ». La dispense pour « éloignement entre le logement acquis et le lieu de l'activité », sans seuil ni durée, permettait de ne jamais occuper le logement.
- Changement : « dans la limite d'une durée de trois ans » (texte de la source) est rétabli pour ce seul cas. Tout le reste de la réforme est conservé : mobilité sans seuil de distance, chômage sans durée ni attestation, location sans plafond de durée après un fait énuméré, usage professionnel sans plafond de surface, meublé non saisonnier.
- La seconde puce du 2 (« aucun plafond de durée ») n'est pas une condition ; elle est conservée telle quelle pour ne pas déplacer le « deuxième alinéa du 2 » visé au 5 (défaut mineur signalé).
- Points pour l'auteur : revoir la fermeture de faille ; la tension héritée entre le délai de six ans (retraite) et l'engagement légal de cinq ans n'est pas touchée.

### CCH R315-78 (LEGIARTI000006897048) — hérité — déjà réglé
- La base légale (L315-19 à L315-22) est abrogée depuis le 19 mai 2011. Le dernier alinéa de R315-69 proposé, appliqué le 30 octobre 2026 (W11mc, SWEEP-M03-R315-69), rattache les références de toute la sous-section à la rédaction antérieure et aux seuls comptes ouverts jusqu'au 4 février 1959 non clos. R315-78 ne cite aucun article L.
- Request de notes à Z05 pour R315-77 (« L315-20 absent du corpus » est faux : LEGIARTI000006825106, ABROGE).
- Point pour l'auteur, déjà signalé par W11mc : abroger la sous-section si aucun compte ne subsiste.

### CSS D752-6 (LEGIARTI000038244832, W03) — les deux audits — corrigé (`apply/W03ca`)
- L752-3-1 (LEGIARTI000053280475, TRANSFERE au 23 juillet 2026) est devenu L. 760-15 (ordonnance n° 2026-648, art. 1er, 4°). Le 12° de l'ordonnance ne modifie que le premier alinéa, le V bis et le V ter : le I et son 1° (« Un décret fixe les conditions… passe au-dessous de onze salariés ») subsistent, sans avis préfectoral légal.
- Changement : les deux renvois visent L. 760-15 ; notes et bilan d'impact rectifiés (L752-3-1 n'était pas « absent du corpus »). Réserve documentaire : L. 760-15 hors corpus ; pas de clause générale de substitution dans l'ordonnance.
- Request à W01 : R752-20 (trois renvois), texte complet fourni. W03, M01 et W01 avaient laissé ce point en « pièce manquante » ; la lecture de l'ordonnance (12°) lève l'incertitude sur la structure.

### Travail D3141-11 (LEGIARTI000018534285) — introduit — non corrigé (défaut dans D3141-37, hors paquet)
- D3141-11 (abrogation) est cohérent avec L3141-33 proposé. D3141-37, maintenu, dit encore « contrôleurs agréés » et « justifie à tout moment », contre « n'est soumis ni à un agrément » et « les seules pièces nécessaires … qui ne sont pas déjà légalement à la disposition de la caisse ».
- Request (sans groupe attribué) avec texte complet : justification à tout moment conservée envers l'inspection du travail et les officiers de police judiciaire ; communication aux contrôleurs de la caisse limitée selon L3141-33 ; transition ; aucune formalité de remplacement.

### Travail R2145-4 (LEGIARTI000045680800) — introduit — corrigé (`apply/BM1`)
- Sans délai minimal, et avec la forclusion du refus au début du congé (R2145-5 proposé), une demande déposée moins de trois jours avant rendait impossible l'avis conforme du CSE exigé par L2145-11 (ordre du jour trois jours au moins avant, L2315-30 maintenu) : le refus légal devenait impossible.
- Changement : délai minimal ramené de trente à huit jours, durée déjà fixée par R2145-5 pour notifier le refus (aucune valeur inventée). La réforme (fin des trente jours) est conservée pour l'essentiel ; aucun pouvoir de refus nouveau. `removed_provisions` et bilan d'impact mis à jour ; request de notes pour R2145-5.
- Point pour l'auteur : la valeur de huit jours est une coordination, pas un choix politique ; une autre valeur ou l'alignement de R2315-17 (trente jours, formation des élus imputée sur ce congé) restent possibles.

### Travail R4626-27 (LEGIARTI000031571257) — les deux audits — corrigé (`apply/BM1`)
- « 1° Les agents mentionnés à l'article R. 4624-18 » visait la liste des bénéficiaires de la surveillance renforcée en vigueur jusqu'au 1er janvier 2017 (LEGIARTI000029237332) ; depuis, R4624-18 ne vise que travailleurs de nuit et mineurs. Les agents exposés, les femmes enceintes et les travailleurs handicapés avaient perdu la surveillance renforcée par le seul jeu du renvoi.
- Changement : renvoi redirigé vers R4624-23 (postes à risques particuliers), R4624-18, R4624-19 (maternité) et R4624-20 (handicap, invalidité). Bruit et vibrations, retirés du droit commun en 2017, non réintroduits ; travailleurs de nuit conservés. Article maintenu passé en `replace` (`coordination_only`) ; notes rectifiées.

Revue IA : rien de ceci ne vaut validation par un juriste.
