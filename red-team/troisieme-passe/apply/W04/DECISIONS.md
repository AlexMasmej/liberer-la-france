# W04 — balayage par famille de défauts (code de la sécurité sociale)

J'ai lu le texte en production avec `CITE_PRODUCTION=1 tools/cite.py`, ou dans `corpus.sqlite` ouvert en `mode=ro` et `query_only`. Je n'ai rien écrit en production. Le contrôle `python3 -B apply/check_changes.py W04` a validé les 6 lignes, avec `problems` vide.

Le paquet compte 54 articles et 62 pistes. Bilan :
- 35 faux positifs ;
- 16 pistes déjà réglées ;
- 8 défauts G confirmés, sur 6 articles, tous corrigés ;
- 3 défauts m, non corrigés.

## Corrections appliquées (changes.json)

| Article (version) | Piste | Correction | Mode |
|---|---|---|---|
| R652-2 (LEGIARTI000038788600) | S8/F3, renvoi à L653-7 | L653-7 est abrogé au 31 décembre 2025 (loi n° 2025-1403, art. 102). Le renvoi vise maintenant l'ancien L653-7 « dans sa rédaction en vigueur avant son abrogation », ou le cumul intégral du III de L161-22. Les collèges ne changent pas et aucune condition n'est ajoutée. Les notes, qui disaient « L653-7 absent du corpus », sont corrigées. | replace |
| R612-8 (LEGIARTI000042363339) | S8/F3, renvoi à L723-1 | L723-1 a été transféré en 2018 (ordonnance n° 2018-470) et devient L652-1, la CNBF. Le champ de l'exclusion est inchangé et les notes sont corrigées. | replace |
| D160-14 (LEGIARTI000041967944) | S8/F3, renvois à L712-1 et L712-2 | Ces deux articles sont abrogés au 1er septembre 2023 (loi n° 2023-270). Ils sont remplacés par L712-13, qui vise les mêmes personnes : fonctionnaires et anciens fonctionnaires civils de l'État, magistrats de l'ordre judiciaire. La caisse compétente est inchangée. | replace |
| R644-3 (LEGIARTI000039620303), auparavant maintenu | S8/F3, renvoi à L142-2 | Le « 1° de L142-2 », abrogé en 2020, devient le « 4° de L142-1 », qui a le même objet (invalidité et inaptitude). Le statut passe de `retained_unchanged` à `rewrite_draft`, avec l'impact `coordination_only`. | replace |
| D766-25 (LEGIARTI000041968250), auparavant maintenu | S8/F3, renvois à D253-12 et D253-14 | La plage vide « D. 253-12 à D. 253-14 » est remplacée par D122-10 et D122-10-1, ses concordances depuis le décret n° 2020-621. La plage abrogée « D. 253-59 à D. 253-60 » est retirée. Statut et impact sont traités comme pour R644-3. | replace |
| R652-26, version de 2029 (LEGIARTI000052846149) | S5/F4 | Cette version n'avait pas de proposition et rétablissait l'exigibilité du droit de plaidoirie au 1er janvier 2029. La proposition reporte sur elle l'abrogation déjà proposée pour la version en vigueur (`full_repeal`, impact `coordination_only`, même `measure_id`, pour ne pas compter la réduction deux fois). La version est à inscrire à l'inventaire. | new |

Pour chaque correction, la référence est la piste du balayage (`SWEEP-W04-…`). Aucune objection du registre n'est concernée. Aucune n'est une fermeture de faille. Aucune ne crée de formalité, d'impôt ou de sanction.

## Pistes non corrigées : défauts m

- **R135-6 (LEGIARTI000038789272), maintenu ; renvoi à L135-1.**
  - L135-1 à L135-5 (fonds de solidarité vieillesse) sont abrogés au 1er janvier 2026 (loi n° 2025-199, art. 24).
  - Pourtant, R135-16-2, en vigueur depuis le 1er janvier 2026, vise encore le « versement du Fonds de solidarité vieillesse ». Le sort réglementaire du fonds n'est donc pas établi au corpus.
  - **Point pour l'auteur :** coordonner l'ensemble du chapitre R135 du FSV, dont R135-1 à R135-19, avec l'abrogation légale. Je ne l'ai pas fait article par article.
- **D162-1-11 (LEGIARTI000041430437), maintenu ; renvoi à L162-5-19.**
  - L162-5-19 est abrogé au 1er janvier 2026 (loi n° 2025-1403, art. 65). Il concernait une aide réservée aux installations faites jusqu'en 2022.
  - Le renvoi reste utile pour les aides déjà ouvertes. Je n'ai pas lu la transition de l'article 65.
- **R931-12-7 (LEGIARTI000041921981) ; renvoi à L951-36-1.**
  - L951-36-1 n'existe dans le corpus à aucune date, pas plus que L931-36-2, visé aussi par R931-12-5 et R931-12-6.
  - C'est une pièce manquante. Je n'ai inventé aucune cible.

## Pistes déjà réglées (16)

- R382-100 (L133-4-10) ;
- R133-9-1 (R133-7) ;
- R653-4 (L653-1) ;
- R862-11-3 (L862-4-1) ;
- R380-6 (L380-2) ;
- R815-50 (L815-13) ;
- D552-6 (L552-4, trois pistes) ;
- L137-26 (successeur 2027, traité par A4 sous RT-FUTCSS-04) ;
- D634-11-5 (L634-6) ;
- D134-44 (L134-8) ;
- R161-48-1 (L162-1-7-1) ;
- R138-19 (L245-1 et L245-5-1) ;
- R147-15 (L645-3).

Chaque proposition borne déjà le renvoi aux périodes antérieures à l'abrogation.

## Faux positifs (35)

- **Renvois à un autre code :**
  - code rural : R161-10, R413-15, R123-56, L491-2, D815-16, L133-1, D531-9 ×2 ;
  - CASF (L. 262-2, RSA, ou L. 245-1, PCH) : R861-7, L613-11, R532-7, D622-9, R582-1, D356-3 ;
  - code des assurances : L942-9, R932-3-2 ×2, R932-3-1, D169-3 ;
  - code de commerce : R243-24, R243-23 ;
  - code de l'éducation : D162-1-6 ;
  - code de l'organisation judiciaire : R142-1-A ;
  - code de la santé publique : L221-1, que le lien LEGI confirme ; la source ne nomme pas le code.
- **Transition utile :** R821-2 et R821-5, car le complément de ressources est maintenu dix ans par la loi n° 2018-1317, art. 266 V.
- **Plage encore vivante :** D133-2-2 (R861-6 à R861-10).
- **Alinéa visé toujours exact (S7) :** R613-8, R226-1, R612-7, R351-37-2, R815-31, L613-11, L133-5-4, D221-2.

## Points pour l'auteur et le coordinateur

1. **R652-2 :** l'extension du renvoi au cumul intégral du III de L161-22 reprend la logique de l'ancien L653-7. Je n'ai pas lu le texte de l'article 102 de la loi n° 2025-1403 au JORF ; j'ai seulement lu la NOTA de L161-22.
2. **Lignes `retained_unchanged` passées en `rewrite_draft` (R644-3, D766-25) :** leur `substantive_impact` est remplacé par une évaluation `coordination_only`. Les certificats sont à recalculer par le coordinateur.
3. **`reference_coherence` de D160-14 et R612-8 :** ce bloc porte un `referrer_sha256` calculé sur l'ancienne proposition. Le validateur ne l'a pas refusé ; à rafraîchir si l'outil d'application l'exige.
4. **Hors paquet :**
   - R382-84 vise encore R. 244-4 et R. 244-5 ;
   - L311-3, versions 2027 et 2030, vise encore « L. 723-1 » pour la CNBF ;
   - parmi R652-20 à R652-39 et L652-6, seul R652-26 a une version future au corpus : aucun autre report n'est nécessaire.

Ceci est une revue par IA, pas une validation par un juriste.
