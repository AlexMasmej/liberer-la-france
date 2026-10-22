# Mise à jour après téléchargements autorisés

D643-7 est désormais complété : **2 sources CSS certifiées documentalement sur4, 4éléments sur6** avec D653-4. Le graphique mensuel D351-9 est récupéré, mais la concordance demeure réservée en raison d’un conflit L(A)60/62 avec le décret2010. Le PDF1982 fournit un renvoi à l’édition Documentsadministratifs ; il ne certifie pas le schéma. Voir [audit de suivi](captcha-authorized-followup/audit.md), [D643](captcha-authorized-followup/d643-report.json), [conflit D351](captcha-authorized-followup/d351-canonical-conflict.md). Les JO entiers restent locaux ; les compagnons nouveaux contiennent seulement les pages pertinentes complètes. Aucun actif/DB modifié par ce sous-agent.

Le bilan antérieur ci-dessous est conservé comme état historique ; il n’annule pas cette mise à jour.

# Sources graphiques CSS — bilan du 22 octobre 2026

**D653-4 est documentalement complété : ses trois expressions sont récupérées et contrôlées.** Le candidat reste isolé, sans activation. D351-9, D643-7 et le cliché des quadranopsies restent réservés. Bilan : **1 source sur4 ;3 éléments sur6**.

## Deux pièces réglementaires entières

Le parent a accédé normalement à Légifrance dans son navigateur intégré, suivi «Extrait du Journal officiel électronique authentifié», la page intermédiaire `/download/pdf`, puis son vrai lien `/download/file/.../JOE_TEXTE`. Le navigateur intégré n’était pas disponible au sous-agent ; ses propres essais Chrome sont restés sur une vérification passive. Aucun cookie exporté et aucun CAPTCHA résolu par ce sous-agent.

| Pièce | Fichier entier contrôlé | SHA-256 | Lecture |
|---|---|---|---|
| Décret2004-1457 du23décembre2004, NOR SANS0423730D, JO303du30décembre2004 texte39 | `documents/joe_20041230_0303_0039.pdf` —54 793octets,3pages | `740c8316ba182397f2b0e20414d112033842a274bc543ac2823790c915d55c03` | Trois pages intégralement rendues et lues. Trois images D723-7 page2. |
| Décret2010-1737 du30décembre2010, NOR ETSS1033015D, JO303du31décembre2010 texte83 | `documents/joe_20101231_0303_0083.pdf` —119 779octets,3pages | `94d6d0371ba915b95321e1335dee0248ac53df1df5af76c2ab15741d7199afd8` | Trois pages intégralement rendues, lues et confrontées à l’extraction ; modification D723-7 page3. |

URL2004 : `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000628806`, puis `https://www.legifrance.gouv.fr/download/file/uSNk84CRAvAVN2kVnHsPSR-a2mQGLEMfNcfE5ZmY-HQ=/JOE_TEXTE`.

URL2010 : `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023334387`, puis `https://www.legifrance.gouv.fr/download/file/63svbPxxA_9vv0UbiiKxBdygrRYNmELc4MrM4SFNwfQ=/JOE_TEXTE`.

Les tailles annoncées par le lecteur diffèrent des octets reçus. Seuls les fichiers réels sont hachés et analysés. Signature `%PDF`, pagination, titre, NOR, date et numéro de texte concordent. Comparaison aux fac-similés officiels attestée ; **aucune vérification cryptographique de signature revendiquée**. `official_jo_crosscheck_complete=true`, `authenticated_jo_crosscheck_complete=false` et `cryptographic_signature_validation_complete=false`.

## Trois expressions de D653-4

Les options sont lues page2, puis revérifiées dans deux détails natifs à300dpi :

- a) `P × (1 − 1/D) × C × E × (1 + 10 %)`.
- b) `P × [1 − (1 − 1/D) × (1 − C)] × E × (1 + 10 %)`.

E historique : `E = [∑_{k=0}^{k=52 à57} (1/(1+i)^k × L(A+k)/L(A)) −3/8 −1/4] × (1/(1+i)^(A−B) × L(A)/L(B))`.

Le décret2010, article1, point8,1°, page3, remplace expressément52 et57 dans cette formule par51 et55. Transcription courante : `E = [∑_{k=0}^{k=51 à55} (1/(1+i)^k × L(A+k)/L(A)) −3/8 −1/4] × (1/(1+i)^(A−B) × L(A)/L(B))`.

Parenthèses, ordre des facteurs, exposant A−B, borne inférieure k=0 et deux soustractions séparées contrôlés dans la page entière puis un détail natif. **−3/8−1/4 n’est pas simplifié.** Texte linéaire et LaTeX dans `cnbf2004-transcription.json`. L’image E2004 aux anciennes bornes reste une preuve historique ; elle n’est pas enregistrée comme image courante.

## Concordance normative et notes

Décret2008-1383, article5III : seuls les mots relatifs à la date de présentation de la demande changent dans D723-7. Page officielle complète : `web/open-10-2008-initial.json`. URL : `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019986224`.

Décret2010-1737 : son fac-similé confirme uniquement52→51 et57→55 dans E, ainsi que les listes de k et A présentes dans le corps canonique courant. Point8 lu page3. Aucune formule trimestrielle dérivée d’une formule mensuelle.

Décret2019-718, **article5III4°** : transfert explicite D723-7→D653-4. Son **III12°** change les références environnantes D723-6/D723-5/R723-43 en D653-3/D351-7/R653-7, sans changer les expressions mathématiques. Passages primaires : `web/search-26-2019-transfer.json` et `web/search-27-transfer-mapping.json`, URL `https://www.legifrance.gouv.fr/eli/decret/2019/7/5/SSAS1909535D/jo/texte`. Lecture ciblée des clauses concernées, pas revue de tout le décret2019. Le XML ARTICLE canonique porte aussi CONCORDE vers D723-7, LEGIARTI000023395837.

`canonical_version_concordance_complete=true` désigne ces contrôles2008/2010/2019. Les corps, XML ARTICLE et notes des quatre sources sont conservés dans `source-snapshot.json` ; notes vides. Toutes les définitions de D653-4 sont conservées. Seules les trois omissions sont complétées dans `d653-4-source-completion-candidate.html`, comme preuve isolée. Le contrôle retire ces compléments et vérifie l’égalité exacte avec le corps initial. Aucune base active ouverte ; aucun contrôle frais de celle-ci revendiqué.

## Trois réserves maintenues

| Source | Pièce encore attendue | Limite |
|---|---|---|
| D351-9 —LEGIARTI000030400105 | E mensuel du JO1janvier2004 texte17, rectificatif31janvier2004 texte2 | 2010 prouve57→55 mais ne restitue pas l’expression initiale. L(A) à60ans dans le corps canonique conservé sans correction par déduction. |
| D643-7 —LEGIARTI000023395852 | E du décret2004-461, JO29mai2004 texte55, rectificatif4septembre2004 texte19 | 2010 prouve52/57→51/55 mais ne fournit pas l’image initiale. E de D653-4 n’est pas emprunté comme substitut. |
| AnnexeI R434-32(7) —LEGIARTI000028675462 | Cliché AT quadranopsies, décret82-1135, JO30décembre1982 et complément | Aucun autre barème substitué. Parent signale CAPTCHA interactif sur fac-similé ; aucune résolution par ce sous-agent. |

Les essais CLI et archives ministérielles sont conservés dans `access-attempts.json` et `documents/` :403, maintenance HTML503, certificat incompatible sur ancien domaine Travail. HTML jamais compté comme PDF. `audit-before-browser.md` et `report-before-browser.json` conservent le premier bilan antérieur à IAB. Recherches CNAM/BNF ciblées, sans prétention d’épuiser toutes les archives. Le PDF COR déjà présent a aussi été rendu et relu pagePDF45/imprimée114 : notation x/60/ω et correction mensuelle+11/24 confirment seulement son exclusion.

## Candidats isolés

`registry-proposal/records/LEGIARTI000038774726.json` contient deux PDF entiers, deux images originales inchangées des options, trois transcriptions courantes. `source_assets.load_companions` vérifie chemins/empreintes ; `recovery_complete=true` pour ce seul article. Présence des trois contenus dans le candidat isolé vérifiée. Trois autres notices incomplètes et non activables. `companion-validation.json` et `manifest.json` conservent contrôles et empreintes.

Les deux images et leurs deux transcriptions identiques portent `verified_visually=true` après nouvelle revue. E courant porte `verified_against_explicit_primary_chain=true`, `primary_graphic_verified_visually=true` et `express_amendments_only=true` ; aucun fac-similé courant n’est revendiqué.

Candidat prêt pour revue avant intégration ; `activation_performed=false`, `count_as_completed=false`. Aucun fichier sous `sources/`, source synchronisée, base, politique, pièce jointe active, proposition active ou lot actif modifié. Aucun crédit acheté, processus de rédaction arrêté ou relancé, slot réservé ou réduit, cookie exporté ou contrôle d’accès contourné.
