# R254-5 et D453-7 — candidats préparés, déblocage primaire non obtenu

**Aucun des deux articles n’est compté comme achevé. Aucun lot numérique créé, aucun enregistrement en base, aucune publication.**

Deux articles entiers sont préparés dans `articles.candidates.json`. Les sources canoniques, leurs empreintes, les notes DILA (vides pour les deux versions) et l’absence initiale de proposition sont conservées dans `source-evidence.json`. Le contrôle final confirme qu’aucune proposition concurrente n’est apparue. Les fichiers `companion-records/r254-5.json` et `companion-records/d453-7.json` suivent le schéma source_assets, mais restent séparés du registre public des pièces. Ils portent explicitement `documentary_recovery_complete=false` et `authenticated_jo_crosscheck_complete=false`.

## Formules retrouvées pour la recherche

- R254-5 : Cheuvreux Notaires, bulletin n°85, octobre 2016, encadré reproduisant l’article, PDF page 3 / page imprimée 10. Deux expressions lues visuellement, dont le taux sous forme de rapport entre loyer annuel moyen au m² et vente moyenne au m², tous deux indexés à N. PDF : `attachments/complements-logement/cheuvreux-formules-bri-2016.pdf`. Source : https://www.cheuvreux.fr/wp-content/uploads/2018/10/decret_brilo_cheuvreux.pdf
- D453-7 : support publié par la fédération Coop’HLM/A.RE.COOP pour la XXIVe rencontre des directeurs, document créé en janvier 2008, PDF page 9. Il cite l’ancien R453-7 et le décret du 26 décembre 2007. La formule comporte le maximum de l’encours réel, le rapport des deux moyennes et le rapport du dernier encours à cinq fois les fonds propres dédiés. PDF : `attachments/complements-logement/coop-hlm-actualite-2008.pdf`. Source : https://www.hlm.coop/file/3990/download?token=D-Mu1X15

Les trois PNG dans `attachments/media/complements-logement/` sont des extractions des formules effectivement visibles, non des images générées. Ils ont été revus à leur taille propre. Les manifestes gardent les pages, les transcriptions et les SHA-256. Le règlement intérieur SGA publié par ESH est également téléchargé pour le contexte, mais **ne reproduit pas la formule** et n’est pas présenté comme sa preuve.

Ces publications professionnelles ne sont ni le JO authentifié ni des consolidations ministérielles. Elles donnent une piste documentaire précise ; elles ne remplissent pas l’exigence de source primaire fixée pour lever le blocage. Les PDF professionnels restent des pièces de recherche, hors des compagnons exportés publiquement dans les ZIP des codes.

## Obstacle établi

Les sources canoniques renvoient respectivement au décret 2016-855 du 27 juin 2016, JO du 29 juin 2016, texte 48 (`JORFTEXT000032791452`), et au décret 2007-1941 du 26 décembre 2007, JO du 30 décembre 2007, texte 157 (`JORFTEXT000017767416`). D453-7 a été transféré de R453-7 par le décret 2019-873.

Les téléchargements normaux des URL observées sur Légifrance donnent 403 ; l’historique est dans `attachments/complements-logement/download-evidence.json`. Une consultation normale des deux textes dans Chrome atteint également « Performing security verification ». Deux captures conservent cette preuve (`browser-jo-2016-block.png`, `browser-jo-2007-block.png`). Aucun export de cookies ou d’en-têtes, aucune résolution de CAPTCHA et aucun contournement n’ont été effectués. L’outil downloadMedia n’a pas été utilisé.

La fiche DILA officielle téléchargée à https://echanges.dila.gouv.fr/OPENDATA/JORF/DILA_JORF_Presentation_20170824.pdf indique que le fonds JORF ouvert fournit le texte intégral **hors format image**. Les catalogues JORF et JORFSIMPLE ont été inspectés et conservés. Recharger ce fonds ne suffirait donc pas à restaurer ces formules. Le document ministériel BRI repéré dans le réseau national des aménageurs décrit les paramètres, mais ne donne pas les expressions ; le lien de téléchargement actuel retourne une page HTML et n’est pas déclaré récupéré comme PDF.

## Choix de fond des candidats

R254-5 conserve le plafond de cession : sa suppression isolée détruirait la cohérence avec L254-1 et la protection attachée à une propriété temporaire financée pour le logement intermédiaire. Aucun nouveau barème chiffré, nouveau justificatif, cas tN=0 ou règle d’arrondi n’est inventé. Le renvoi ancien aux cinquième et sixième alinéas du I de la loi89-462, article17-2, est corrigé par un renvoi fonctionnel aux règles de constitution et de nombre des références : elles figurent aujourd’hui aux troisième et quatrième alinéas du I. Cette correction est justifiée dans review_notes ; elle ne prétend pas réécrire cette loi hors périmètre.

D453-7 supprime uniquement la délibération trimestrielle distincte lorsqu’aucune modification des conditions de garantie n’est nécessaire. L’évaluation trimestrielle, l’information du conseil, les corrections nécessaires, le plafond prudentiel, les pouvoirs du commissaire du Gouvernement, son délai d’opposition d’un mois et la majorité de confirmation sont maintenus. La transition protège les garanties et conventions existantes. La limite du texte canonique interdit de dépasser dix fois les capitaux propres ; le support professionnel résume en «inférieur». Le candidat conserve la formulation canonique et ne transforme pas ce résumé en nouvelle inégalité stricte.

## Contrôles et reprise

`audit.json` confirme : HTML valide, transcriptions professionnelles présentes, toutes les empreintes d’assets correctes, renvois d’articles conservés, sources inchangées, zéro nouvelle proposition enregistrée. Les calculs n’ont pas été certifiés juridiquement ou mathématiquement à partir de leur source officielle.

Pour reprendre : obtenir les trois images/formules depuis le JO ou une reproduction officielle/ministérielle admise, les confronter aux deux candidats et aux expressions professionnelles, puis seulement adapter les manifestes de récupération et déplacer les articles dans les lots numériques après contrôle. En cas de proposition apparue entretemps, utiliser `review_prior.commit` avec l’empreinte antérieure et son archivage. Ne pas déposer les candidats tels quels dans un lot numérique tant que la réserve primaire n’est pas levée.
