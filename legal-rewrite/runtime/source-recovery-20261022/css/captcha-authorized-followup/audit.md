# Suivi CSS après téléchargements autorisés

**D643-7 est documentalement complété et prêt pour revue. D351-9 a son graphique récupéré, mais demeure réservé pour un conflit précis de consolidation. Le JO du 30 décembre 1982 reçu apporte le décret et un renvoi bibliographique, sans preuve du schéma attendu.** D653-4 reste couvert par le dossier antérieur. Aucun actif, base, source canonique, note, processus ou plafond des six rédacteurs n’est modifié par ce suivi.

## D643-7 : chaîne achevée

- Source canonique LEGIARTI000023395852, version à compter du 1er janvier 2011, intégralement relue avec XML ARTICLE et notes vides ; copie fidèle dans `source-snapshot.json`.
- JO entier 29 mai 2004 : 152 pages, 69 265 786 octets, SHA256 `882cf8ab04ef017015aa1c3427093e9fbf505a77e926f194ab4c551ddc1bceec`. La page PDF97 / imprimée9593 contient tout D643-7. Page entière rendue et lue ; détail de E à 300 dpi. Aucune revue visuelle des 152 pages revendiquée.
- Rectificatif du 4 septembre 2004, texte19, NOR SANS0420911Z, JORFTEXT000000445868 : PDF entier d’une page, 26 933 octets, SHA256 `7f463a4f52808742dc7a4b99d5dd504526b8a8d61500372b5fe46d49aa02732e`. Lecture visuelle de la page entière et de la formule corrigée. La correction ferme la parenthèse du terme sommé **avant** les soustractions séparées −3/8 et −1/4. L’expression erronée de mai n’est pas utilisée comme transcription courante.
- Texte officiel : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000445868. PDF observé par le parent : https://www.legifrance.gouv.fr/download/file/a_urgQLFljTH3a379PKqvLLRPUtKNSw_DzSHjt1DoHk=/JOE_TEXTE. Le texte principal officiel est conservé intégralement dans `primary-texts/rectificatif-2004-461-20040904.txt`.
- Décret2006-879, articles3 et7 : pas de modification des opérateurs E ; règle transitoire2006 concernant B identifiée. Décret2008-1383, article4III : changement des mots relatifs à la date de demande seulement. Décret2010-1737, article1 point6 1°, PDFpage2 : substitutions expresses52→51 et57→55 dans E. Les listes k et A modifiées aux2° et3° concordent avec le corps canonique.

La transcription courante est : `E = [∑_{k=0}^{k=51 à 55} (1/(1+i)^k × L(A+k)/L(A)) − 3/8 − 1/4] × (1/(1+i)^(A−B) × L(A)/L(B))`. Aucun réarrangement de facteurs ni simplification.

La candidate `registry-proposal/records/LEGIARTI000023395852.json` contient le PDF rectificatif entier, le PDF2010 entier de trois pages et une extraction fidèle de la seule page97 du JOmai. L’extraction conserve les objets de la page entière ; son rendu est identique pixel à pixel au rendu de la même page dans le fichier original. Elle est explicitement un **extrait local distinct**, sans signature héritée revendiquée. Le JO entier reste une preuve locale et n’est pas ajouté aux pièces à publier.

Le graphique historique corrigé est préservé directement depuis son image incorporée originale, item pdfimages10 / objet21, 927×126 pixels. Ce stencil est décodé en masque blanc sur noir ; un détail du rendu normal est également conservé dans `pages/d643-E-corrected-2004-detail.png`. Le graphique historique n’est pas enregistré comme image courante, car ses bornes sont celles de2004. La transcription actuelle porte les flags de chaîne primaire expresse et non une fausse certification de fac-similé courant.

`d643-validation.json` : schéma/empreintes valides, `recovery_complete=true`, contenu présent, corps hors marqueur strictement inchangé, notes vides préservées, aucune activation. Le contrôle des signatures cryptographiques n’est pas revendiqué.

## D351-9 : graphique récupéré, réserve motivée

Le JO entier du1erjanvier2004 a176pages, 80 692 660octets et SHA256 `516a4fa89aa3c30784ca3da39149e1a1875a2bea80ad800e38e8323beed9f7f5`. Les pages46 et47 contiennent D351-9 ; elles ont été intégralement rendues et lues puis extraites en deux pages complètes. Leurs rendus sont identiques pixel à pixel aux pages du JOentier. Le détail natif de E confirme k=0, borne k=57, **−11/24−1/12** et exposant A−B. Le rectificatif31janvier2004 ne change pas ce graphique. La substitution57→55 est expressément prescrite en2010.

La version officielle antérieure à2010 a été récupérée dans `web-14.json` et lue entière : LEGIARTI000019993446, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019993446/2009-06-26. La définition L(A) est effectivement l’avant-dernier alinéa. Or2010 impose60→62 à cet endroit tandis que la source canonique courante conserve60. Les vérifications2006/2008/2015 ne résolvent pas cet écart.

`d351-canonical-conflict.md` expose la position exacte, la portée des textes et la réserve ; `d351-definition-correction-proposal.json` contient une proposition textuelle séparée gardée par empreinte, **non appliquée**. Le candidat conserve les octets canoniques hors du marqueur. Il porte `graphic_recovery_complete=true` mais `documentary_recovery_complete=false`, `canonical_version_concordance_complete=false` et `ready_for_activation=false`.

## Schéma des quadranopsies : pièce bibliographique seulement

Le PDF `../documents/JORF_NC_19821230_303.pdf`, 124pages, 70 018 292octets, SHA256 `a5e8b7502320050e4ce1fac34cfdb5b5b097786932d3249895572badeeff16be`, contient le décret82-1135 à la pagePDF75 / imprimée3975 et sa suite. Sa note annonce l’annexe dans le prochain numéro de l’édition des **Documents administratifs** du JO. Aucun cliché des quadranopsies n’a été identifié ni certifié dans ce fichier. L’absence de termes dans l’OCR ne constitue pas à elle seule une preuve d’absence de toute image. Le parent poursuit la piste Documentsadministratifs ; aucune nouvelle résolution de CAPTCHA par ce sous-agent.

## Portée des vérifications

Les téléchargements autorisés, leurs tailles et leurs empreintes sont consignés par le parent dans `../../authorized-downloads.json`. Ce suivi ne leur attribue pas la certification de version qui dépend de la chaîne normative. Les sources officielles textuelles peuvent étayer une correction purement textuelle ; les graphiques ont tous été lus dans leurs pages PDF entières et doublement contrôlés dans un détail fidèle.

Les deux registres candidats sont isolés sous `registry-proposal/`, sans lien symbolique. Seule D643 est activable sur les éléments examinés ; D351 conserve sa réserve. Les pièces de preuve couvrent les pages utiles et conservent la provenance du JO entier. `extract-render-verification.json` consigne l’identité des rendus ; `manifest.json` consigne les empreintes des fichiers de ce suivi.
