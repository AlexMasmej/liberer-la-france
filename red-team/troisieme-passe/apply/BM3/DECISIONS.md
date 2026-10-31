# BM3 — défauts grossiers de l'échantillon apparié frais : décisions

Paquet : `audit/baseline/fix-packet-BM3.json` (7 articles). Lecture faite en production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite en `mode=ro` avec `query_only`), le 31 octobre 2026. Contrôle : `python3 -B apply/check_changes.py` sur `BM3`, `T084cc` et `B04cc` → `problems: []`. Les cinq textes déposés sous `requests` ont été validés dans deux dossiers temporaires (`BM3tmp`, `Z04tmp`), supprimés ensuite. Revue IA, sans validation par un juriste.

## Décompte

- **Corrigés : 4.** Annexe II 286 I (`apply/T084cc`), CGI 232 (`apply/B04cc`), CSS L757-3 et code du travail L351-6 (`apply/BM3`).
- **Déjà réglé : 0.**
- **Non corrigés : 3.** CCH L441-11 (le défaut vérifié est dans R441-28, hors paquet : texte complet sous `requests`), code du travail R4313-26 (hors corpus, droit de l'Union à confirmer), code du travail R713-14 (arbitrage).
- **Demandes (`requests`) : 5.** CCH R441-28 (sans propriétaire), code du travail L351-8 et L351-14 (sans propriétaire), L351-5-1 (Z04), CGI 1406 bis (B04).

## Corrections appliquées

### Annexe II 286 I (LEGIARTI000038668407, hérité, groupe T084) → `apply/T084cc`

- **Défaut :** le IX subordonnait encore la validation des documents d'accompagnement aux « obligations mentionnées à l'article 614 du code général des impôts ». CGI 614 (LEGIARTI000006305149) est abrogé depuis le 1er juillet 2025 (ordonnance n° 2023-1210) ; la réserve « dans la mesure où ces dernières demeurent applicables » ne désignait plus rien. Le I gardait le règlement (CE) n° 1234/2007 comme repère de champ, alors qu'il est abrogé par le règlement (UE) n° 1308/2013, ce que dit le texte même de l'ancien article 407 du CGI (LEGIARTI000041985072).
- **Correction :** retrait du renvoi à 614 au IX ; actualisation du repère de champ au règlement (UE) n° 1308/2013 au I. Rien d'autre ne change : la suppression de la déclaration annuelle du IV, sa transition et toutes les échéances conservées restent telles quelles. Moins de conditions, aucune formalité de remplacement.
- **Notes rectifiées :** « 302 D, 407, 450, 302 M/bis/ter et 614 n'y figurent pas » était faux ; ces articles figurent au corpus à l'état ABROGE (302 M et 302 M bis en ABROGE_DIFF). Le bilan d'impact est mis à jour sur le même point.
- **Pour l'auteur :** le texte succédant au règlement (CE) n° 436/2009 et le CIBS restent hors corpus ; l'ordonnance n° 2023-1210 n'a pas été lue.

### CGI 232 (LEGIARTI000046872468, introduit, groupe B04) → `apply/B04cc`

- **Défaut :** la proposition fait de 232 un article durable (zonage « autonome » du I, définitions des V et VI) dont dépendent R642-1, L422-2 et L422-3 du CCH, alors que la source est en ABROGE_DIFF au 1er janvier 2027 (article 108 de la loi n° 2026-103), sans version suivante et sans clause écartant cette abrogation. Le VI disait encore que « la taxe n'est pas due » pour une taxe supprimée.
- **Correction :** un X ajouté maintient l'article, dans sa rédaction issue de la réforme, nonobstant l'article 108 de la loi n° 2026-103, ou le rétablit si l'abrogation est déjà intervenue, sans rétablir aucune imposition et pour les seuls I, V et VI. Le VI dit désormais qu'un logement dont la vacance est indépendante de la volonté du contribuable n'est pas regardé comme vacant, ce que vise la source de 1407 bis (« La vacance s'apprécie au sens des V et VI de l'article 232 »). La suppression de la taxe, sa transition et le II (dérogation à 1406 bis) ne changent pas.
- **Ce qui rend la correction alignée :** elle rend effective une réforme déjà décidée par le projet (zonage autonome) qu'une abrogation programmée aurait défaite.
- **Disposition non codifiée** (`uncodified`) : texte proposé écartant l'article 108 de la loi n° 2026-103 pour 232 dans sa rédaction issue de la réforme, au cas où l'auteur préfère cette voie.
- **Demande à B04 :** préciser dans 1406 bis que l'abrogation « ne remet pas en vigueur la taxe prévue par les dispositions antérieures de l'article 232, dont les I, V et VI demeurent applicables dans leur rédaction résultant de la présente loi ».
- **Pour l'auteur :** le texte de l'article 108 de la loi n° 2026-103 n'a pas été lu (hors corpus).

### CSS L757-3 (LEGIARTI000031324239, introduit) → `apply/BM3`

- **Défaut :** la seconde passe avait remplacé « les collectivités mentionnées à l'article L. 751-1 » par une liste figée de six collectivités « y compris après le 1er janvier 2028 », en lisant l'état ABROGE_DIFF de L751-1 comme une abrogation. Or L751-1 est remplacé au 1er janvier 2028 par une version publiée (LEGIARTI000054466946, ordonnance n° 2026-647) qui ajoute Mayotte, et L757-4 (2028) étend le titre II du livre VIII (AAH) à Mayotte. La liste figée excluait Mayotte de l'habilitation sans décision.
- **Correction :** retour au renvoi dynamique de la source, avec un second alinéa qui en explicite le caractère dynamique (« dans sa rédaction applicable à la date considérée »). Aucune collectivité n'est ajoutée ni retirée par cet article : le champ suit la loi.
- **Notes rectifiées :** « L. 751-1, abrogée en 2028 » était faux.

### Code du travail L351-6 (LEGIARTI000018124358, défaut vu par les deux audits) → `apply/BM3`

- **Défaut :** article de la « Partie législative ancienne », affiché en vigueur depuis le 1er janvier 2011 par l'effet d'une modification différée (loi n° 2008-126, art. 5 I ; décret n° 2009-1708) postérieure à l'abrogation de cette partie (ordonnance n° 2007-329, art. 12, citée par la NOTA de L351-13). Ses renvois (« présent chapitre », « chapitres correspondants des deuxième et troisième parties ») visent l'ancien code. Le même objet est régi par L5422-15 (mise en demeure préalable) et R5422-9 (lettre recommandée avec avis de réception). Le projet le maintenait comme du droit vivant.
- **Correction :** abrogation (`full_repeal`), avec conservation des mises en demeure, actions et régularisations antérieures ; aucune formalité ni sanction de remplacement. Aucune garantie n'est perdue, la mise en demeure par lettre recommandée subsistant à L5422-15 et R5422-9.
- **Sûreté :** la correction vaut dans les deux hypothèses, article fantôme (abrogation déclarative) ou article en vigueur faisant double emploi.
- **Section traitée en entier :** L351-13 est réellement maintenu par la réserve de l'ordonnance (1° marins pêcheurs) et n'est pas touché. L351-8 (qui cite « L. 351-5 à L. 351-6 »), L351-14 et L351-5-1 sont dans la même situation : abrogations demandées sous `requests`, textes complets joints, avec leurs correspondants en vigueur (L5422-20 à L5422-22 ; L5422-6, L5424-20, L5424-22, L5422-16 ; L5422-16).
- **Pour l'auteur :** le texte complet de l'article 12 de l'ordonnance n° 2007-329 (liste des réserves) n'a pas été lu. La proposition antérieure de L351-14 portait une coordination de la suppression de la contribution spécifique du spectacle et une transition du contrat unique ; les deux sont déjà portées par L5424-20 proposé, l'abrogation ne les perd pas.

## Non corrigés

### CCH L441-11 (LEGIARTI000036432651, hérité, groupe B08) : déjà en ordre, défaut déplacé dans R441-28 → `requests`

- L441-11 proposé (abrogation prospective, loi répressive plus douce, sanctions définitives) n'appelle rien. Le défaut vérifié : pour les manquements antérieurs, R441-28 proposé fait encore notifier et prononcer la sanction par le préfet, avec recouvrement au profit de l'Etat, alors que depuis 2015 la loi confie la sanction au ministre chargé du logement sur proposition de l'ANCOLS (L342-14, I, 1°, b), le contradictoire à L342-12 et le recouvrement, comme en matière d'impôts directs, au profit de la CGLLS (L342-16). Deux autorités pour la même sanction.
- **Texte demandé** (R441-28, sans propriétaire) : la phrase préfectorale est remplacée par « la sanction est proposée, prononcée, recouvrée et contestée dans les conditions prévues aux articles L. 342-12 à L. 342-16, après que l'organisme a été mis en mesure de présenter ses observations ». L'abrogation prospective, la transition et l'absence de tout pouvoir de sanction nouveau restent identiques. Validé dans un dossier temporaire.

### Code du travail R4313-26 (LEGIARTI000019761215, hérité) : hors corpus, à confirmer (F9)

- Le défaut (examen « CE » de type des EPI maintenu alors que le règlement (UE) 2016/425 l'a remplacé, comme le reconnaît L4311-6) est confirmé grossier, mais il tient à toute la section R4313-23 à R4313-42 et à R4313-80 à R4313-82, toutes maintenues, et au règlement (UE) 2023/1230 pour les machines (20 janvier 2027). Le règlement 2016/425 n'a pu être lu (EUR-Lex illisible le 31 octobre 2026). Limiter le seul R4313-26 aux machines laisserait la section incohérente ; une réserve « dans la mesure où la procédure demeure applicable » serait vide.
- **Pour l'auteur :** coordination d'ensemble de la section avec les deux règlements, après lecture de leurs champs et transitions.

### Code du travail R713-14 (LEGIARTI000018519056, hérité) : arbitrage

- L'article organise l'élection d'un comité central d'entreprise par les comités d'établissement (industries électriques et gazières), institutions remplacées par le CSE central et les CSE d'établissement (ordonnance n° 2017-1386), et renvoie à l'ancien L435-4 (ABROGE au 1er mai 2008), dont le quatrième alinéa a pour successeur le deuxième alinéa de L2316-8. Le projet n'a fait que figer ce renvoi à sa rédaction de 2008.
- Deux corrections possibles : transposer au CSE central (noms des institutions, renvoi au deuxième alinéa de L2316-8) en gardant la représentation des services communs ; ou abroger. La première adapte un régime spécial des IEG ; la seconde supprime une garantie de représentation des services communs (loi du 8 avril 1946, art. 5 ; service commun maintenu par le code de l'énergie). Le statut national des IEG, le décret n° 2008-244 et l'article 9 de l'ordonnance n° 2017-1386 sont hors corpus. Non appliqué.
- **Pour l'auteur :** même décision d'ensemble pour R713-10, R713-11 (CHSCT) et R713-13, encore affichés en vigueur (R713-1 à R713-9 et R713-12 sont abrogés depuis 2016) ; coquille « aliéna » à corriger si l'article est repris.

## Points laissés à l'auteur (récapitulatif)

1. Article 108 de la loi n° 2026-103 (CGI 232) : clause codifiée (X) ou disposition non codifiée (`uncodified`), au choix.
2. Partie législative ancienne du code du travail : au-delà de L351-6, L351-8, L351-14 et L351-5-1, les autres articles « ancien code » affichés en vigueur (28 selon l'audit officiel) mériteraient le même traitement ; non examinés ici, hors L351-13 (réellement maintenu).
3. R441-28 : si le coordinateur préfère conserver le délai d'un mois de la source pour le stock ancien, il peut l'ajouter à la phrase demandée sans en changer l'autorité compétente ; non retenu ici pour ne pas créer de délai que L342-12 ne prévoit pas.
4. Section « examen CE de type » (R4313-23 et suivants) et section IEG (R713-10 à R713-14) : deux coordinations d'ensemble à décider.
