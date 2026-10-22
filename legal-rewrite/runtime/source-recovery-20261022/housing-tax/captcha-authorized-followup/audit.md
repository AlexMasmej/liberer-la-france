# A123-1 : annexe POS récupérée dans le complément officiel de 1984

**La légende POS complète est récupérée et la notice candidate est prête pour activation documentaire par le coordinateur.** Elle comporte quarante entrées, avec tous les symboles, titres, libellés et mentions, aux pages imprimées 6186 à 6189, pages PDF 14 à 17. Aucun registre actif ni article n’a été modifié par cette passe.

## Pièce officielle et identité

Le PDF entier `JORF_NC_19840717_165.pdf`, téléchargé normalement après l’accord explicite de l’utilisateur pour les contrôles CAPTCHA concernés, contient 48 pages, 21 785 371 octets. Son SHA-256 est `1c7710e196cb6845326ecaa00eda9580ba69cd0a6538e1aac7784d36c1e696ed`. Cette empreinte a été recalculée localement. Le PDF entier reste une preuve locale dans le dossier `housing-tax/documents/` et ne figure pas dans le compagnon destiné aux sites.

La couverture et le sommaire identifient le Journal officiel de la République française, numéro 165, numéro complémentaire daté du 17 juillet 1984. Le sommaire, page PDF 2, distingue l’arrêté POS, page 6186, de l’arrêté SUP, page 6189. « N.C. » signifie ici numéro complémentaire.

La [page officielle de l’arrêté SUP](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000292388) a servi de route d’accès au numéro complémentaire entier. Elle ne constitue pas l’identité normative de la légende POS. La route, le véritable lien de fichier temporaire, l’autorisation et le manifeste de téléchargement sont consignés dans `official-provenance.json` et les copies de preuve. Aucun contournement d’accès ni export de cookies n’est utilisé.

## Rattachement direct à A123-1

L’arrêté intitulé « fixant la légende des différentes servitudes pouvant figurer sur les documents graphiques du plan d’occupation des sols » commence page 6186. Son article premier renvoie à sa légende pour R.123-18 I et II. Son article 2 II insère A123-1 avec la phrase qui figure dans le XML canonique actuel.

Cette phrase a été lue sur la page complète et comparée au corps canonique en entier. Après normalisation exclusivement typographique et retrait, pour comparaison seulement, de la parenthèse d’export signalant la non-reproduction, les textes concordent. La NOTA est vide et reste vide. Le XML original `LEGIARTI000006813811` a le SHA-256 `c58d74ee3fa7ec9e7e634feaa0f1f5005b646a9b5bc77df666685db87c9bb882`, identique aux deux empreintes du snapshot isolé. Version conservée depuis le 17 juillet 1984.

Les deux versions conservées d’A123-1 ont été consultées par clé dans le snapshot en lecture seule. L’ancienne version `LEGIARTI000006813810`, abrogée le 7 juillet 1978, porte sur les établissements dangereux, insalubres ou incommodes ; elle n’est pas une version graphique antérieure de la présente légende et n’est pas importée. Les deux XML sont conservés dans `preuves/`, avec leurs archives et empreintes dans `canonical-history.json`.

L’ouverture web directe de l’article actuel était indisponible et sa recherche exacte n’a rien donné dans cette passe. Aucune actualisation de la version au-delà des données canoniques n’en est déduite. La concordance documentaire demandée est établie entre la version cible immuable et le fac-similé officiel complet.

## Couverture de l’annexe et exclusion SUP

| Page PDF d’origine | Page imprimée | Contenu conservé |
|---|---|---|
| 14 | 6186 | Titre ANNEXE, titre du tableau, partie 1, sections A et B, entrées 1 à 8 |
| 15 | 6187 | Entrées 9 à 20 |
| 16 | 6188 | Entrées 21 à 32 ; partie 2, sections A et B |
| 17 | 6189 | Entrées 33 à 40, avec toutes les instructions relatives aux dates |

La numérotation 1 à 40 est continue. Les motifs, contours, formes pleines ou creuses, lettres, numéros d’opérations, exemple graphique « 15m », variantes de trame et mentions parenthétiques restent les pixels d’origine, sans interprétation normative ajoutée. L’index de lecture des quarante libellés est dans `legend-inventory.json` ; il ne remplace pas les images.

Après l’entrée 40, page 6189, commence un **autre arrêté**, consacré aux servitudes d’utilité publique de R.126-1 et créant A126-1. Sa propre annexe commence page 6190, page PDF 18, avec les colonnes catégories, code alphanumérique et symbole graphique. Cette limite a été contrôlée visuellement. Ni ce texte ni ses symboles ne sont intégrés au compagnon POS.

## Extrait fidèle destiné au compagnon

Le compagnon contient quatre PNG et un **extrait local de quatre pages**, dont le nom, les métadonnées, le libellé et les signets indiquent explicitement la nature d’extrait. Il ne contient ni les pages nominatives étrangères à l’annexe ni le texte SUP voisin.

Les quatre images de scan JPEG2000 incorporées dans le PDF d’origine ont été décodées à leur résolution native de 200 ppp. Les pixels RGB et le profil ICC sRGB d’origine sont conservés. Les seuls recadrages sont des sélections entières de pixels, avec coordonnées `(gauche, haut, droite, bas)` :

- Page 6186 : `(0, 720, 1621, 2315)` ; l’annexe entière, à partir de son titre, est conservée ; le texte de l’arrêté au-dessus est exclu de l’extrait.
- Page 6187 : `(0, 0, 1612, 2316)` ; image entière.
- Page 6188 : `(0, 0, 1612, 2316)` ; image entière.
- Page 6189 : `(0, 0, 1645, 1660)` ; les entrées 33 à 40 sont conservées ; le début de l’arrêté SUP en dessous est exclu.

Aucune rotation, retouche, amélioration de contraste, reconstitution de symbole, recomposition typographique ou mise à l’échelle des pixels n’a été faite. L’extrait PDF réincorpore exactement les mêmes octets de pixels recadrés et le même profil ICC. Les images entières et les données JPEG2000 d’origine sont conservées localement pour vérifier les recadrages.

Le PDF produit ne contient aucune couche OCR, texte masqué, annotation ou image entière demeurée cachée derrière un rectangle de recadrage. Ses quatre images incorporées ont été réouvertes et comparées aux PNG enregistrés : égalité exacte des pixels, dimensions et profil ICC. Toutes ses pages ont ensuite été rendues et lues visuellement ; aucun titre, symbole, libellé ou fin de ligne de l’annexe n’est coupé. Les pages pertinentes du JO original ont été inspectées en entier avant cette vérification.

SHA-256 de l’extrait : `9277d7d1cc3dfdbdee0709335ddf7a60abee36bccff2e7297b2f82ed7326fe62`, 16 899 717 octets. L’origine officielle est établie ; aucune validation cryptographique n’est revendiquée. Le PDF ancien n’a pas d’AcroForm ; `pdfsig` indique aucune signature tout en émettant une erreur NSS locale. Le champ d’authentification cryptographique reste donc faux.

## État de la candidate

`registry-proposal/records/LEGIARTI000006813811.json` est compatible avec `source_assets`. Le chargement isolé, les empreintes des quatre médias et du document, la correspondance à l’unique marqueur et la présence des quatre parties dans le document de revue ont été vérifiés. Voir `companion-validation.json`, `canonical-concordance.json`, `crop-specification.json` et `excerpt-integrity.json`.

`documentary_recovery_complete=true`, `canonical_version_concordance_complete=true`, `ready_for_activation=true`, `proposed_xml=null`, `count_as_completed=false`. L’activation est laissée au coordinateur et ne vaut pas réécriture d’un article. La réserve CERFA terminée précédemment n’a pas été rouverte.
