# Sources graphiques CSS — passe du 22 octobre 2026

Résultat : **0 des 4 sources certifiée récupérée ; 6 éléments manquent toujours**. La passe a élargi les voies publiques officielles et préserve les réponses entières, dates serveur, URL et empreintes. Aucun candidat normatif n’est activé. Les six rédacteurs CLI et leurs ressources n’ont pas été modifiés.

| Source canonique | Pièce manquante | État documentaire |
|---|---|---|
| D351-9 — LEGIARTI000030400105 | Une expression E mensuelle, indices et bornes compris | Le décret initial 2003-1376 est indexé avec une équation linéarisée et dupliquée. JO 1 janvier et rectificatif 31 janvier 2004 non acquis en fac-similé. L’âge A=62 et la définition canonique de L(A) à 60 ans restent intacts. |
| D643-7 — LEGIARTI000023395852 | Une expression E trimestrielle | Sommaires officiels du JO 29 mai et du rectificatif 4 septembre 2004 identifiés ; ni ces sommaires ni les reproductions textuelles n’apportent le terme manquant. |
| D653-4 — LEGIARTI000038774726 | Deux options et le terme E trimestriel | Le décret 2004-1457 et son ancien D723-7 sont identifiés. Nouvelle piste BO Santé 2005/02, sans PDF effectivement obtenu. Les trois omissions restent réservées. |
| Annexe I R434-32 (7) — LEGIARTI000028675462 | Cliché des quadranopsies AT | Le décret 82-1135 annonce deux JO numérisés, 47,4 et 66,8 Mo ; leur accès reste protégé. CNAM et BNF ne fournissent pas ici le cliché exact. |

## Accès contrôlés et exclusions

La piste nouvellement identifiée `https://temps.travail.gouv.fr/fichiers/bo/2005/05-02/bo0502.pdf` est indexée comme bulletin officiel contenant des textes de retraite. L’accès HTTPS ordinaire échoue avec le code curl 60 : le certificat ne correspond pas au nom d’hôte. La vérification TLS n’a pas été désactivée. L’essai HTTP public se redirige vers le même HTTPS et échoue de même. Une piste indexée n’est pas une pièce obtenue.

Les archives Santé 2004/01, 2004/24 et 2005/02, ainsi que les domaines historiques Solidarités, Solidarités-Santé, Social-Santé et Travail, ont été essayés avec leurs chemins publics. Les réponses réseau conservées portent le statut 503 et le titre **« Maintenance – Alerte Produit Santé »** : ce sont des fichiers HTML de 20 340 octets, pas des bulletins. Le lecteur web voit également une vérification de sécurité avec CAPTCHA sur une URL Santé ; aucun défi n’a été traité.

Le décret 82-1135 retourne 403 avec une vérification Cloudflare. L’interface de continuité publique `https://journal-officiel.legifrance.gouv.fr/` a été découverte et essayée ; elle retourne aussi un blocage Cloudflare. Les ouvertures web des décrets de 2004/2019 et des deux JO rectificatifs échouent. Les corps de réponse sont conservés pour les accès réseau ; les réponses du lecteur web sont dans `web/`. Les anciennes URL `journal-officiel.gouv.fr` déjà auditées ne sont pas présentées comme de nouveaux essais.

La circulaire RSI 2011/017 a été demandée entière à l’URL officielle CNAV : réponse 503, **« Site en maintenance »**, HTML de 4 858 octets. Le fichier a été nommé `.response.html` après contrôle de sa signature. Le COR a de même retourné une réponse HTML **« Erreur serveur »** de 12 053 octets sous un statut 200 ; aucun faux PDF n’est enregistré.

La notice BNF consultée par recherche indexée relie la collection moderne du JO à Légifrance. Elle ne constitue ni un téléchargement du numéro de 1982, ni une preuve d’indisponibilité de toutes les archives BNF. Les recherches CNAM et ministérielles ont été ciblées ; cette passe ne prétend pas avoir épuisé chaque archive possible.

## Contrôle visuel PDF

La compétence PDF a été lue et appliquée au PDF COR déjà disponible, `cor-doc-865.pdf`, empreinte `682509f99704ebfcf11af7eb9efcfe00ad3921e217db1d4e578c0521737d82a3`. La page PDF 45, imprimée 114, a été rendue entière dans `pages/cor865-p45-recheck.png`, lue visuellement puis comparée au texte extrait de la même page. Elle expose une formule de recherche mensuelle en x/60/ω, avec borne inférieure k=1 et correction +11/24. Elle ne reproduit pas la formule canonique actuelle de D351-9 et ne fournit aucune expression trimestrielle. Ce contrôle confirme l’exclusion antérieure ; ce n’est pas une nouvelle récupération normative. Pas de prétention à une lecture juridique des 79 pages.

Les barèmes de droit commun, étrangers et les aides CNAM 2013 ne sont pas transposés au cliché AT. Le résultat indexé de l’arrêté de 2026 comporte lui-même le marqueur dans le passage comparable ; il ne lève pas l’omission historique. Aucune variable, aucun opérateur, aucune borne ni aucun taux n’est déduit ou corrigé.

## Sortie et garde-fous

`report.json` décrit chacune des quatre sources, les pièces exactes encore attendues, les URL, l’absence de transcription normative et l’étendue de lecture. `source-snapshot.json` conserve intégralement leurs corps, XML ARTICLE et notes issus du cliché documentaire antérieur. Les quatre notes sont vides. Il n’y a pas eu de nouvelle lecture de la base active ; aucun contrôle frais de celle-ci n’est revendiqué.

Les quatre notices de `registry-proposal/records/` sont compatibles avec le chargeur `source_assets.load_companions` sur cette racine isolée. Les listes `documents`, `media` et `transcriptions` y sont vides ; `recovery_complete` vaut false pour chacune. Ce sont des notices de réserve, avec `ready_for_activation=false`, et pas des candidats publiables. `companion-validation.json` conserve le contrôle ; `manifest.json` porte les empreintes de toutes les preuves locales.

Aucun fichier sous `sources/`, aucune source synchronisée, aucune base, politique, pièce jointe active, proposition active ou lot actif n’a été modifié. Aucun crédit acheté, aucun processus de rédaction arrêté ou relancé, aucun slot réservé ou réduit, aucun cookie exporté et aucun contournement de CAPTCHA, d’authentification ou de contrôle d’accès.
