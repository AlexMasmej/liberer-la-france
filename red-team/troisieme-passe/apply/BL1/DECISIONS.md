# BL1 — corrections des défauts grossiers de l'échantillon apparié (paquet `audit/baseline/fix-packet-BL1.json`)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`, `query_only`), le 31 octobre 2026. Revue IA, sans validation par un juriste.

Décompte : 2 corrigés, 6 déjà réglés, 3 non corrigés (2 corrections rédigées et validées, déposées sous `requests` ; 1 arbitrage).

## Corrections appliquées

1. **CSS D134-4** (LEGIARTI000006735260) : appliquée (`apply/BL1`).
   - Défaut : le dernier alinéa compte encore les effectifs dont les cotisations sont prises en charge par le fonds du chapitre V du titre III du livre Ier. Ce fonds, le FSV, est supprimé au 1er janvier 2026 (L135-1 à L135-5 en état ABROGE).
   - Correction : le renvoi désigne désormais la branche vieillesse (3° de L200-2), au titre de L222-2-1. C'est la solution déjà retenue en production pour R135-16 (X8).
   - Les exercices antérieurs à 2026 gardent leur régime. Cette transition figure dans le même dernier alinéa, pour que le renvoi de D134-2 au « dernier alinéa » reste juste.
   - Le renvoi à la section 3 (étudiants), dont tous les articles sont abrogés, est retiré.
   - Mode `replace` d'un article maintenu, `coordination_only`, avec bilan d'impact.
   - Pour l'auteur : l'article 24 de la loi n° 2025-199 n'a pas été relu. Une clause générale de substitution rendrait cette correction simplement déclarative.
2. **Travail L323-21** (LEGIARTI000006648776, groupe W08) : appliquée (`apply/W08ba`).
   - Correction : abrogation (`full_repeal`). Le seul alinéa survivant est une habilitation réglementaire qui renvoie aux alinéas 1 à 4, abrogés en 2008, pour les collectivités de L323-2, abrogé le 1er janvier 2020.
   - Aucune restriction maladie n'est rétablie. Les situations antérieures sont préservées. Les notes qui disaient L323-2 « non fourni » sont rectifiées.
   - Pour l'auteur : W08 avait classé ce point en faux positif. L'audit apparié et sa vérification le jugent grossier.

## Corrections rédigées, hors de mon périmètre (`requests`)

3. **CCH D331-81** (paquet) → **D331-80** (LEGIARTI000039048289, sans groupe propriétaire).
   - D331-81 est déjà abrogé : le visa ministériel est supprimé.
   - Le défaut s'est déplacé. La section 4 organise toujours des prêts accordés par la caisse de prêts aux organismes HLM. Or cette caisse a été remplacée au 1er janvier 1986, pour les seuls prêts consentis jusqu'au 31 décembre 1985 (L431-3).
   - Texte demandé : un troisième alinéa limite la section à ces prêts, aux conventions et aux droits des occupants (D331-79), sans prêt nouveau ni formalité de remplacement.
   - Texte complet, motif, notes et bilan d'impact sont joints. Ils ont été validés dans un dossier temporaire, depuis supprimé.
4. **CCH R862-3**, version au 1er janvier 2027 (LEGIARTI000054394516, groupe Z05), proposition `new`.
   - Le renvoi « aux 1° et 2° du présent article » devient « aux a et b du présent 1° ».
   - Au 4°, la citation « L'organisme adresse » devient « L'organisme payeur adresse », comme dans R824-15 (2027), pour que la suppression du délai de cinq jours ouvrés s'opère.
   - Écarts mineurs laissés au 2° : citations de R824-13 légèrement inexactes, sans effet sur le sens.
   - Le texte a été validé dans un dossier temporaire.
   - Pour l'auteur : Z05 avait qualifié la piste S19b de faux positif. Ce défaut est d'une autre nature (F3, renvoi décalé).
5. **Travail L323-34** (LEGIARTI000006648694, sans groupe) : retrait demandé de l'alinéa « les modalités d'application de l'article L. 323-21 », mort après l'abrogation ci-dessus.
   - Pour l'auteur : L323-34 a la même limite de survie (L323-2). Son sort d'ensemble reste à trancher.

## Non appliquée (arbitrage)

6. **CSS R313-6** (LEGIARTI000031827945).
   - Le renvoi au « a » inexistant est déjà corrigé.
   - « Cette année civile » reste sans antécédent aux 5° et 6°. Le texte est identique sur Légifrance (consulté le 31 octobre 2026).
   - Choisir l'année de référence (année du décès, année précédente ou 365 jours) étend ou restreint l'accès au capital décès. C'est donc un choix pour l'auteur.

## Déjà réglés en production

- **Annexe II 371 A** (M05) : toute la section des centres de gestion agréés est abrogée avec transition (371 F à K compris). Les versions 2030 de CGI 1649 quater E et H sont déclarées sans objet.
- **Annexe III 178-0 bis** : article abrogé ; seules les opérations antérieures gardent leur régime.
- **CSS D531-5** : les plafonds sont rétablis et le renvoi à 204-0 bis est remplacé par CGI 81, 1°.
  - Note périmée restante, de niveau m, dans L531-4 (hors paquet).
- **CSS R135-8** : la suppression du FSV est constatée ; l'article est limité à la clôture et à la liquidation (X8).
- **CSS R752-18-5** : présidence nommée selon L145-6 (R752-18-4 aussi).
  - R752-18-7, pour les pharmaciens, est conforme à L145-6-2.
- **Travail R5212-2-4** (Y06) : R5212-2-3 à 2-5 sont abrogés ; le rescrit relève de L243-6-3 CSS.

## Réserve de méthode

Ces 11 articles viennent de l'échantillon apparié qui sert à mesurer le taux de défauts grossiers. Les corriger ne mesure pas une baisse du taux du corpus. Seule une nouvelle mesure sur un échantillon frais, tiré hors de ces articles, peut l'établir.

Revue IA : rien de ceci ne vaut validation par un juriste.
