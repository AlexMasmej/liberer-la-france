# Y11 : troisième balayage (S9, S10), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, SQLite `mode=ro`, `query_only`), le 29 octobre 2026. Paquet : `audit/sweeps/packet-Y11.json`, 48 articles et 61 pistes, toutes portées par des articles du code de la construction et de l'habitation (46 S9, 15 S10) ; une seule vise un autre code (article 1384 A du CGI). Chaque article du paquet a été lu en entier (source, proposition, motif), ainsi que chaque cible avec la ligne `removed_provisions` de son lot. Les notes ont été lues quand elles servaient à la qualification. Les versions suivantes des articles à abrogation différée cités (R711-9, L861-5, L183-4, CGI 1384 A) ont toutes un brouillon. Exports : `evidence/cited/production-20261029/`. Le détail de chaque piste, avec ses citations exactes, figure dans `audit/sweeps/Y11.json`.

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 0 |
| m | 1 (L126-35-2, S10) |
| déjà réglé | 25 |
| faux positif | 35 |

Corrections : aucune. `apply/Y11/changes.json` ne contient ni changement, ni demande, ni renonciation. `python3 -B apply/check_changes.py Y11` donne `problems` vide.

Constat général. Chaque décret ou annexe qui organisait la formalité retirée d'une loi réduite porte déjà sa coordination, avec sa transition. Exemples : second agrément SCIC (R422-16), agrément spécial et accord territorial des sociétés de coordination (R423-85, annexes I et II à R423-86), avis du CRHH et extension territoriale de l'agrément de maîtrise d'ouvrage (R365-2, R365-6-1), déclarations financières et techniques du registre des copropriétés (R711-9), transmissions ministérielles des solutions d'effet équivalent (R112-5), dispenses ERP de L122-3 (R122-9, R122-16, R143-14, D165-4), accord temporaire-saisonnier de L162-1 (R162-4, R162-7), déclaration et contravention termites (R126-3, R184-8), imputation du retard d'Ad'AP (R165-9), labels du carnet (R126-34), agrément fiscal de 1384 A (D331-76-5-1), attestation de décence à Saint-Pierre-et-Miquelon (R863-13). Les faux positifs S9 viennent de mots-clés homonymes : un agrément maintenu (L365-2, L365-3, L365-4), un rapport maintenu (L511-8), l'attestation de L112-9 elle-même (seule sa transmission est retirée), un renvoi seulement définitoire (R441-5, annexe à R373-3). Les faux positifs S10 sont des dérogations ou exceptions dont la règle visée existe encore, au même alinéa.

## Défaut mineur (non corrigé : article non modifié par ailleurs)

- **L126-35-2** (LEGIARTI000043966759), S10 vers L126-35-4 : « par dérogation aux articles L. 126-35-4 et L. 126-35-5, le propriétaire n'est tenu ni d'établir ni de mettre à jour ce carnet ». L126-35-4 proposé garde « Le carnet d'information est établi pour chaque logement », neutralisé par son troisième alinéa : la dérogation vise donc une règle encore écrite. Mais L126-35-5 proposé ne contient plus d'obligation (« Le propriétaire du logement peut établir et mettre à jour le carnet ») : la dérogation à cet article est redondante. F5 sans effet, les trois articles concordant sur le carnet facultatif.

## Observation hors piste (m, pour l'auteur)

- **L301-5-1** (LEGIARTI000045211697), V bis : la délégation peut porter « sur la délivrance aux organismes d'habitations à loyer modéré des agréments d'aliénation de logements prévue aux articles L. 443-7, L. 443-8 et L. 443-9 ». Or L443-7 proposé dispense ces ventes « d'autorisation administrative préalable », L443-8 proposé écarte « une autorisation du représentant de l'Etat dans le département ou du président du conseil de la métropole », et L443-9 (maintenu) ne prévoit aucun agrément. La compétence déléguable est devenue sans objet (F1/F5). Effet neutralisé : L443-7 proposé dispose qu'« aucune demande d'autorisation ni consultation préalable au titre de cette compétence n'est exigée pour les ventes bénéficiant de la dispense », et le deuxième alinéa de L443-8 garde au président de la métropole le seul rôle de fixer les conditions de remboursement des aides. Non corrigé. Deux retouches sont possibles : réserver V bis aux délégations antérieures, ou le réécrire autour de ce rôle résiduel. Elles touchent l'étendue de la délégation possible et sont laissées à l'auteur.

## Pistes

| Article | Piste | Cible | Qualification | Corrigé |
|---|---|---|---|---|
| R422-16 (LEGIARTI000039652794) | S9/F1+F5 | cch L422-3-2 (LEGIARTI000041715834) | déjà réglé | non |
| R423-85 (LEGIARTI000039652810) | S9/F1+F5 | cch L423-1-2 (LEGIARTI000037668094) | déjà réglé | non |
| R441-5 (LEGIARTI000041615478) | S9/F1+F5 | cch L741-1 (LEGIARTI000049399282) | faux positif | non |
| R441-5 (LEGIARTI000041615478) | S9/F1+F5 | cch L741-2 (LEGIARTI000049399333) | faux positif | non |
| R441-5 (LEGIARTI000041615478) | S9/F1+F5 | cch L443-7 (LEGIARTI000045211315) | faux positif | non |
| R441-9 (LEGIARTI000041615492) | S9/F1+F5 | cch L365-3 (LEGIARTI000020465506) | faux positif | non |
| R365-2 (LEGIARTI000041715841) | S9/F1+F5 | cch L365-2 (LEGIARTI000041715812) | déjà réglé | non |
| R365-6-1 (LEGIARTI000041715888) | S9/F1+F5 | cch L365-2 (LEGIARTI000041715812) | déjà réglé | non |
| R422-36-1 (LEGIARTI000042022236) | S9/F1+F5 | cch L423-1-2 (LEGIARTI000037668094) | déjà réglé | non |
| R711-9 (LEGIARTI000042078909) | S9/F1+F5 | cch L711-2 (LEGIARTI000049398053) | déjà réglé | non |
| Annexe à l'article R443-9-4 (LEGIARTI000042116925) | S10/F5 | cch L481-2 (LEGIARTI000037668295) | faux positif | non |
| D331-76-5-1 (LEGIARTI000042524283) | S9/F1+F5 | cgi 1384 A (LEGIARTI000046900644) | déjà réglé | non |
| R511-3 (LEGIARTI000042877906) | S9/F1+F5 | cch L511-8 (LEGIARTI000049398539) | faux positif | non |
| R372-3 (LEGIARTI000043708895) | S9/F1+F5 | cch L365-2 (LEGIARTI000041715812) | faux positif | non |
| R112-1 (LEGIARTI000043818269) | S9/F1+F5 | cch L112-9 (LEGIARTI000041587597) | faux positif | non |
| R112-4 (LEGIARTI000043818277) | S9/F1+F5 | cch L112-9 (LEGIARTI000041587597) | faux positif | non |
| R112-5 (LEGIARTI000043818281) | S9/F1+F5 | cch L112-10 (LEGIARTI000041587589) | déjà réglé | non |
| R122-9 (LEGIARTI000043818433) | S9/F1+F5 | cch L122-3 (LEGIARTI000054142549) | déjà réglé | non |
| R122-16 (LEGIARTI000043818451) | S9/F1+F5 | cch L122-3 (LEGIARTI000054142549) | déjà réglé | non |
| R126-3 (LEGIARTI000043818557) | S9/F1+F5 | cch L126-6 (LEGIARTI000041565129) | déjà réglé | non |
| R143-14 (LEGIARTI000043818965) | S9/F1+F5 | cch L122-3 (LEGIARTI000054142549) | déjà réglé | non |
| R146-14 (LEGIARTI000043819107) | S10/F5 | cch D122-12 (LEGIARTI000043818441) | faux positif | non |
| R146-14 (LEGIARTI000043819107) | S10/F5 | cch R122-11 (LEGIARTI000052644802) | faux positif | non |
| R146-17 (LEGIARTI000043819113) | S9/F1+F5 | cch L122-3 (LEGIARTI000054142549) | faux positif | non |
| R162-4 (LEGIARTI000043819259) | S9/F1+F5 | cch L162-1 (LEGIARTI000041569527) | déjà réglé | non |
| R162-7 (LEGIARTI000043819267) | S9/F1+F5 | cch L162-1 (LEGIARTI000041569527) | déjà réglé | non |
| R165-1 (LEGIARTI000043819311) | S9/F1+F5 | cch L165-6 (LEGIARTI000041569727) | faux positif | non |
| D165-4 (LEGIARTI000043819321) | S9/F1+F5 | cch L122-3 (LEGIARTI000054142549) | déjà réglé | non |
| D165-5 (LEGIARTI000043819323) | S10/F5 | cch R122-11 (LEGIARTI000052644802) | faux positif | non |
| R165-9 (LEGIARTI000043819335) | S9/F1+F5 | cch L165-6 (LEGIARTI000041569727) | déjà réglé | non |
| R173-8 (LEGIARTI000043819431) | S10/F5 | cch R173-6 (LEGIARTI000043819425) | faux positif | non |
| R184-8 (LEGIARTI000043819581) | S9/F1+F5 | cch L126-6 (LEGIARTI000041565129) | déjà réglé | non |
| R126-10 (LEGIARTI000043824305) | S9/F1+F5 | cch L122-3 (LEGIARTI000054142549) | faux positif | non |
| L126-35-2 (LEGIARTI000043966759) | S10/F5 | cch L126-35-4 (LEGIARTI000043966763) | m | non |
| L861-5 (LEGIARTI000044405110) | S10/F5 | cch L823-1 (LEGIARTI000038814920) | faux positif | non |
| R863-13 (LEGIARTI000044636801) | S9/F1+F5 | cch L863-3 (LEGIARTI000038814737) | déjà réglé | non |
| R353-165 (LEGIARTI000044845851) | S9/F1+F5 | cch L365-4 (LEGIARTI000020465504) | faux positif | non |
| L303-3 (LEGIARTI000045202347) | S10/F5 | cch L303-2 (LEGIARTI000054142528) | faux positif | non |
| L364-1 (LEGIARTI000045211301) | S10/F5 | cch L302-13 (LEGIARTI000028533964) | faux positif | non |
| L353-15 (LEGIARTI000045211517) | S10/F5 | cch L443-7 (LEGIARTI000045211315) | faux positif | non |
| L353-9-3 (LEGIARTI000045211572) | S10/F5 | cch L321-8 (LEGIARTI000038833957) | faux positif | non |
| L301-5-1 (LEGIARTI000045211697) | S10/F5 | cch L313-26-2 (LEGIARTI000033972018) | faux positif | non |
| L661-1 (LEGIARTI000045213005) | S10/F5 | cch L651-2 (LEGIARTI000050623451) | faux positif | non |
| R172-6 (LEGIARTI000045292852) | S9/F1+F5 | cch L112-9 (LEGIARTI000041587597) | faux positif | non |
| Annexe I à l'article R423-86 (LEGIARTI000045646952) | S9/F1+F5 | cch L411-2 (LEGIARTI000038834254) | faux positif | non |
| Annexe I à l'article R423-86 (LEGIARTI000045646952) | S9/F1+F5 | cch L365-2 (LEGIARTI000041715812) | faux positif | non |
| Annexe I à l'article R423-86 (LEGIARTI000045646952) | S9/F1+F5 | cch L423-1-2 (LEGIARTI000037668094) | déjà réglé | non |
| Annexe I à l'article R423-86 (LEGIARTI000045646952) | S9/F1+F5 | cch L422-2 (LEGIARTI000053546225) | déjà réglé | non |
| Annexe I à l'article R423-86 (LEGIARTI000045646952) | S9/F1+F5 | cch L422-11 (LEGIARTI000028808832) | déjà réglé | non |
| Annexe II à l'article R423-86 (LEGIARTI000045646995) | S9/F1+F5 | cch L411-2 (LEGIARTI000038834254) | faux positif | non |
| Annexe II à l'article R423-86 (LEGIARTI000045646995) | S9/F1+F5 | cch L365-2 (LEGIARTI000041715812) | faux positif | non |
| Annexe II à l'article R423-86 (LEGIARTI000045646995) | S9/F1+F5 | cch L423-1-2 (LEGIARTI000037668094) | déjà réglé | non |
| Annexe II à l'article R423-86 (LEGIARTI000045646995) | S9/F1+F5 | cch L422-2 (LEGIARTI000053546225) | déjà réglé | non |
| Annexe II à l'article R423-86 (LEGIARTI000045646995) | S9/F1+F5 | cch L421-1 (LEGIARTI000053546314) | faux positif | non |
| Annexe II à l'article R423-86 (LEGIARTI000045646995) | S9/F1+F5 | cch L422-11 (LEGIARTI000028808832) | déjà réglé | non |
| L183-4 (LEGIARTI000046123749) | S10/F5 | cch L163-1 (LEGIARTI000041569531) | faux positif | non |
| D331-25-1 (LEGIARTI000046332092) | S10/F5 | cch L442-8-1-1 (LEGIARTI000038834136) | faux positif | non |
| R126-34 (LEGIARTI000046825220) | S9/F1+F5 | cch L126-35-8 (LEGIARTI000043966771) | déjà réglé | non |
| R321-18 (LEGIARTI000047215794) | S9/F1+F5 | cch L741-1 (LEGIARTI000049399282) | faux positif | non |
| Annexe I à l'article R. 373-3 (LEGIARTI000047400121) | S9/F1+F5 | cch L301-5-1 (LEGIARTI000045211697) | faux positif | non |
| Annexe I à l'article R. 373-3 (LEGIARTI000047400121) | S9/F1+F5 | cch L301-5-2 (LEGIARTI000033974121) | faux positif | non |

## Non traité

Rien. Les 61 pistes sont qualifiées.
