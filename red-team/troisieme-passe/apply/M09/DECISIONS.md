# M09 — cinquième balayage (CGI : S2c, S8c) — décisions

Lecture : production, en lecture seule, le 29 octobre 2026 (`CITE_PRODUCTION=1 tools/cite.py`, exports dans `evidence/cited/production-20261029/`, et sqlite en mode=ro). Légifrance a été consulté le 29 octobre 2026 pour 1795 bis et 1791. La page de l'ordonnance n° 2026-265 a répondu 403 ; ce refus n'a pas été contourné.

Bilan : 111 pistes sur 43 articles. 71 faux positifs, 35 déjà réglées, 4 m, 1 G.

## Défaut G

- **CGI 1795 bis** (LEGIARTI000048639271, maintenu, sans propriétaire antérieur). L'article punit les manœuvres sur le contingent des rhums « des sanctions prévues à l'article 1791 ». Or 1791 (LEGIARTI000048639291) est abrogé depuis le 1er mai 2026 par l'ordonnance n° 2026-265, art. 6. C'est un défaut de la source : F3, avec un effet F2, car la sanction devient indéterminée.
  - **Non corrigé sur le fond (hors corpus).** La matière est reprise au code des douanes (L. 531-1 et suivants d'après les liens LEGI). Ces articles sont hors corpus et leur contenu n'est pas vérifié. Aucun tarif ni aucune destination n'est inventé.
  - **Retirer la sanction n'est pas aligné.** Cela supprimerait la protection du contingent favorable de 362.
  - **Correction faite (SWEEP-M09-1795bis) :** les notes seules sont rectifiées, sans proposition. Elles disaient 1791 « absent du corpus consulté » ; elles indiquent maintenant que 1791 est au corpus et abrogé au 1er mai 2026.
  - **Laissé à l'auteur :** désigner la sanction applicable, soit l'article du code des douanes, soit la clause de renvoi de l'ordonnance n° 2026-265.

## Défauts m (non corrigés : articles non modifiés)

- **217 undecies** (LEGIARTI000046893133). La règle d'anti-cumul vise encore 199 undecies, périmé en 2003. Le renvoi est inerte, hérité de la source.
- **302 G** (LEGIARTI000050085168, abrogation à prise d'effet conditionnelle). L'article renvoie au document de 302 M ter, abrogé en 2023. C'est un régime résiduel repris au CIBS (hors corpus).
- **1791 bis** (LEGIARTI000053881343), deux pistes, S2c et S8c :
  - le I renvoie au 1° de 1791, abrogé le même jour que la prise d'effet de cette version ; c'est une incohérence de la source ;
  - la proposition limite la fourchette favorable au reliquat ;
  - la note dit à tort que 1791 n'est pas au corpus (F10).

## Variantes et demandes

Aucun dossier de variante n'a été créé. Les articles à propriétaire antérieur sont 232, 1649 quater B quater, 1600, 289 bis et 1736 (B04), 1727, 31, 1754, 1744 et 1518 A quinquies (A1), 1737 (W14), 286 (A2), 158 (B06), 1763 C (B05) et 219 (B07). Leurs pistes sont des faux positifs ou sont déjà réglées : aucune modification n'est nécessaire. Aucune demande (`requests`).

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| 80 undecies (LEGIARTI000046861333) | S8c/F3 | 9 | faux positif | — |
| 232 (LEGIARTI000046872468) | S2c/F2+F3 | 1406 bis | déjà réglé | — |
| 232 (LEGIARTI000046872468) | S2c/F2+F3 | 1407 bis | déjà réglé | — |
| 217 undecies (LEGIARTI000046893133) | S8c/F3 | 199 undecies | m | non (m) |
| 1640 C (LEGIARTI000047623370) | S8c/F3 | 1648 D | faux positif | — |
| 1795 bis (LEGIARTI000048639271) | S8c/F3 | 1791 | G | notes rectifiées ; fond hors corpus |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1650 | faux positif | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1737 | faux positif | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1741 | faux positif | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1754 | faux positif | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1771 | faux positif | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1788 A | déjà réglé | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1837 | faux positif | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1747 | déjà réglé | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1751 | déjà réglé | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1738 | déjà réglé | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1774 | déjà réglé | — |
| 1753 (LEGIARTI000048639294) | S2c/F2+F3 | 1789 | déjà réglé | — |
| 1396 (LEGIARTI000048704443) | S2c/F2+F3 | 1609 C | déjà réglé | — |
| 1396 (LEGIARTI000048704443) | S2c/F2+F3 | 1609 G | déjà réglé | — |
| 1396 (LEGIARTI000048704443) | S2c/F2+F3 | 1609 H | déjà réglé | — |
| 1729 F bis (LEGIARTI000048804263) | S2c/F2+F3 | 223 WW | faux positif | — |
| 995 (LEGIARTI000048835759) | S8c/F3 | 9 | faux positif | — |
| 293 A (LEGIARTI000048838508) | S8c/F3 | 77 | faux positif | — |
| 286 ter A (LEGIARTI000048856703) | S8c/F3 | 135 | faux positif | — |
| 1740-00 A (LEGIARTI000049641115) | S2c/F2+F3 | 199 undecies B | faux positif | — |
| 1740-00 A (LEGIARTI000049641115) | S2c/F2+F3 | 217 undecies | faux positif | — |
| 1740-00 A (LEGIARTI000049641115) | S2c/F2+F3 | 244 quater Y | faux positif | — |
| 302 G (LEGIARTI000050085168) | S8c/F3 | 302 M ter | m | non (m) |
| 793 (LEGIARTI000051149498) | S8c/F3 | 199 undecies | faux positif | — |
| 793 (LEGIARTI000051149498) | S8c/F3 | 710 | faux positif | — |
| 793 (LEGIARTI000051149498) | S8c/F3 | 199 decies B | faux positif | — |
| 44 octies A (LEGIARTI000051217764) | S2c/F2+F3 | 44 octies | faux positif | — |
| 1636 B octies (LEGIARTI000051219300) | S2c/F2+F3 | 1607 ter | déjà réglé | — |
| 1636 B octies (LEGIARTI000051219300) | S2c/F2+F3 | 1407 ter | faux positif | — |
| 1730 (LEGIARTI000051219475) | S2c/F2+F3 | 1729 G | faux positif | — |
| 1764 (LEGIARTI000051219760) | S2c/F2+F3 | 210 F | faux positif | — |
| 1764 (LEGIARTI000051219760) | S2c/F2+F3 | 231 ter | déjà réglé | — |
| 1764 (LEGIARTI000051219760) | S2c/F2+F3 | 231 quater | déjà réglé | — |
| 1649 quater B quater (LEGIARTI000051764508) | S2c/F2+F3 | 1586 ter | déjà réglé | — |
| 1649 quater B quater (LEGIARTI000051764508) | S2c/F2+F3 | 568 | faux positif | — |
| 1649 quater B quater (LEGIARTI000051764508) | S2c/F2+F3 | 1673 bis | faux positif | — |
| 1649 quater B quater (LEGIARTI000051764508) | S2c/F2+F3 | 990 I | déjà réglé | — |
| 150-0 B ter (LEGIARTI000053542872) | S2c/F2+F3 | 199 | faux positif | — |
| 150-0 B ter (LEGIARTI000053542872) | S2c/F2+F3 | 92 B | faux positif | — |
| 150-0 B ter (LEGIARTI000053542872) | S2c/F2+F3 | 92 B decies | faux positif | — |
| 150-0 B ter (LEGIARTI000053542872) | S2c/F2+F3 | 160 | faux positif | — |
| 150-0 B ter (LEGIARTI000053542872) | S2c/F2+F3 | 150-0 D bis | faux positif | — |
| 219 (LEGIARTI000053542939) | S2c/F2+F3 | 235 ter ZAA | faux positif | — |
| 1763 (LEGIARTI000053543089) | S2c/F2+F3 | 54 octies | déjà réglé | — |
| 1763 (LEGIARTI000053543089) | S2c/F2+F3 | 53 A | déjà réglé | — |
| 1840 G ter (LEGIARTI000053543390) | S2c/F2+F3 | 1135 bis | déjà réglé | — |
| 199 terdecies-0 A (LEGIARTI000053543691) | S2c/F2+F3 | 200-0 A | déjà réglé | — |
| 1763 C (LEGIARTI000053543723) | S2c/F2+F3 | 38 | faux positif | — |
| 1763 C (LEGIARTI000053543723) | S2c/F2+F3 | 163 quinquies B | faux positif | — |
| 1763 C (LEGIARTI000053543723) | S2c/F2+F3 | 199 | faux positif | — |
| 1763 C (LEGIARTI000053543723) | S2c/F2+F3 | 1763 B | déjà réglé | — |
| 199 terdecies-0 AB (LEGIARTI000053543929) | S2c/F2+F3 | 199 | faux positif | — |
| 199 terdecies-0 AB (LEGIARTI000053543929) | S2c/F2+F3 | 200-0 A | déjà réglé | — |
| 31 (LEGIARTI000053544761) | S2c/F2+F3 | 199 nonies | faux positif | — |
| 31 (LEGIARTI000053544761) | S2c/F2+F3 | 199 undecies | faux positif | — |
| 31 (LEGIARTI000053544761) | S8c/F3 | 199 nonies | faux positif | — |
| 31 (LEGIARTI000053544761) | S8c/F3 | 199 undecies | faux positif | — |
| 289 bis (LEGIARTI000053546660) | S2c/F2+F3 | 289 E | déjà réglé | — |
| 1737 (LEGIARTI000053546686) | S2c/F2+F3 | 289 | faux positif | — |
| 1737 (LEGIARTI000053546686) | S2c/F2+F3 | 290 quinquies | faux positif | — |
| 1728 (LEGIARTI000053546784) | S2c/F2+F3 | 1635 quater A | faux positif | — |
| 1728 (LEGIARTI000053546784) | S2c/F2+F3 | 800 | déjà réglé | — |
| 1728 (LEGIARTI000053546784) | S2c/F2+F3 | 641 | déjà réglé | — |
| 1728 (LEGIARTI000053546784) | S2c/F2+F3 | 982 | faux positif | — |
| 1728 (LEGIARTI000053546784) | S2c/F2+F3 | 1649 A | faux positif | — |
| 1600 (LEGIARTI000053562172) | S2c/F2+F3 | 1600 A | déjà réglé | — |
| 1518 A quinquies (LEGIARTI000053589332) | S2c/F2+F3 | 1530 | faux positif | — |
| 1791 bis (LEGIARTI000053881343) | S2c/F2+F3 | 290 quater | déjà réglé | — |
| 1791 bis (LEGIARTI000053881343) | S2c/F2+F3 | 1791 | m | non (m) |
| 1791 bis (LEGIARTI000053881343) | S8c/F3 | 1791 | m | non (m) |
| 1754 (LEGIARTI000053881346) | S2c/F2+F3 | 298 bis | faux positif | — |
| 1754 (LEGIARTI000053881346) | S2c/F2+F3 | 1729 C | faux positif | — |
| 1754 (LEGIARTI000053881346) | S2c/F2+F3 | 1594 F quinquies | faux positif | — |
| 1754 (LEGIARTI000053881346) | S2c/F2+F3 | 1736 | faux positif | — |
| 1744 (LEGIARTI000054334864) | S2c/F2+F3 | 1741 | faux positif | — |
| 1758 (LEGIARTI000054336658) | S2c/F2+F3 | 1649 A | déjà réglé | — |
| 1758 (LEGIARTI000054336658) | S2c/F2+F3 | 1649 AA | déjà réglé | — |
| 1758 (LEGIARTI000054336658) | S2c/F2+F3 | 1649 quater A | déjà réglé | — |
| 1740 A bis (LEGIARTI000054337014) | S2c/F2+F3 | 1729-0 A | faux positif | — |
| 1740 A bis (LEGIARTI000054337014) | S2c/F2+F3 | 1650 | faux positif | — |
| 286 (LEGIARTI000054337091) | S2c/F2+F3 | 9 | faux positif | — |
| 1729-0 A (LEGIARTI000054373048) | S2c/F2+F3 | 1649 A | faux positif | — |
| 1729-0 A (LEGIARTI000054373048) | S2c/F2+F3 | 1649 AA | faux positif | — |
| 1729-0 A (LEGIARTI000054373048) | S2c/F2+F3 | 1736 | faux positif | — |
| 158 (LEGIARTI000054373673) | S2c/F2+F3 | 150 duodecies | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 240 | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 242 ter | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 158 | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 243 bis | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 1649 A | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 1649 A ter | déjà réglé | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 1649 A quater | déjà réglé | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 1649 ter | faux positif | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 235 ter ZD | déjà réglé | — |
| 1736 (LEGIARTI000054373979) | S2c/F2+F3 | 242 quater | déjà réglé | — |
| 231 ter (LEGIARTI000054713030) | S2c/F2+F3 | 1599 quater C | déjà réglé | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 199 septies | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 200 quater | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 244 quater B | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 244 quater B bis | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 223 A | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 150 U | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 201 | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 793 | faux positif | — |
| 1727 (LEGIARTI000051213330) | S2c/F2+F3 | 795 A | faux positif | — |

Validation : `python3 -B apply/check_changes.py M09` → problems vide (1 changement validé, 2 skipped motivés).

Revue IA : ce document ne vaut pas validation par un juriste.
