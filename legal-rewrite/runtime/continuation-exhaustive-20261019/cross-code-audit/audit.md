# Concordance des quatre autres codes avec le contrat unique — remise bornée

Recherche canonique en lecture seule : **18 724 articles courants** de CSS, CCH, Urbanisme, CGI et annexesIàIV. **1 246 entrées** correspondent soit au texte recherché, soit à un lien DILA sortant vers le Code du travail. Les liens entrants seuls n'ont pas été interprétés comme des renvois normatifs. Les corps, notes, documentsARTICLE et éventuels projets antérieurs sont capturés dans `edition001/all-captured-sources.json` ; ce nombre ne désigne pas1 246 lectures juridiques achevées.

Inventaire compact demandé : `edition001/reference-inventory.json`. État de concordance explicite : `concordance-queue.json`. Empreintes et règle de fusion : `handoff.json`.

## Livraison normative

**28 identifiants distincts**, en trois paquets figés. Ils ne sont ni enregistrés ni publiés par l'auteur.

| Paquet | Contenu | Règle d'intégration |
|---|---|---|
| edition001 |20articles entiers : santé complémentaire, allègements sociaux, recrutement public/privé distinct, logement, PAS et exonérations apprentissage/transmission | Garder19articles ; remplacer AnnIII39 par002 |
| edition002 |5articles : L231-11,1609quinvicies,R822-18,L241-10 et AnnIII39 corrigé | AnnIII39 remplace le même identifiant de001 ; les4autres s'ajoutent |
| edition003 |4articles : L752-3-2,L752-3-3,D752-7,D752-8 | Ensemble ultramarin coordonné, avecIVbis législatifs autonomes |

Chaque paquet comporte `source.json`, `answer.json`, script de validation et `validation.json`. Les sources/notes/documents et avant-images correspondent exactement à la base au dernier contrôle enregistré ; toute rédaction concurrente impose une nouvelle comparaison, pas un écrasement. Les trois validations structurelles passent, sans conflit à ces contrôles. Cela ne remplace pas la revue juridique indépendante demandée à l'agent logement.

Les seuils et paramètres existants sont conservés : versement santé125% pour les futures périodes temporaires équivalentes,105% autresCDI, seuils3mois/12mois/15heures et10% du brut ; PAS½SMIC pendant les deux premiers mois avec trois grilles entières ; exonérationSMICannuel apprentissage ; abattement500000€ de transmission ; taxe sursalaires apprentis≤10salariés/11%SMIC. Les affectations/périodes limitées ne deviennent jamais des termes d'emploi.

L241-13/D241-7/D241-5-2 conservent le calcul distinct favorable auparavant lié auCDD/mission : choix seulement s'il est supérieur au calcul ordinaire, rémunération/SMIC affectés à la même période et aucun double compte. Les quatre textes ultramarins appliquent le même principe avec leurs propres territoires, secteurs, périodes annuelles ou mensuelles, formules et plafonds ; ils ne créent pas une exonération automatique d'intermissions qui seraient inéligibles selon les autres règles. LeIVbis deL752-3-3 est autonome afin de ne pas limiter ce choix au seul régime renforcé de sonIV.

Deux corrections identifiées par la revue indépendante sont matérialisées dans002 : donnéesCPF-CDD alignées sur les **périodes de travail** deL6331-6 plutôt que la date de paiement ; futursCDD de droitpublic de remplacement maintenus dansL241-10, alors que la suppression des nouveauxCDD concerne le droitprivé. Le texte de001 demeure intact pour la traçabilité.

1609quinvicies conserve l'année de décompte favorable après la fin de la formation sans exiger une rupture/réembauche désormais inutile. L231-11 conserve la protection6mois aprèsmandat/3mois candidature, la prolongation saisonnière et les protections plus favorables du délégué syndical : il ne transforme pas un ancien renvoi abrogéL412-18 en perte de garanties. R822-18 préserve les revenus de professionnalisation, y compris différés ou examinés après la fin de la phase.

## Contrôles sans nouveau candidat

21entrées de l'inventaire ont fait l'objet d'une lecture entière sans coordination nouvelle nécessaire identifiée ; la raison précise figure dans `concordance-queue.json`. Elles couvrent notamment80duodecies/L242-1 (exonérations d'indemnités, distinctes du montant de droit du travail), le directeurOPH et son statut propre, les logements de formation, les abattements assistantsmaternels, les réductionsCFE artisanales et les anciennes déclarationsCVAE déjà supprimées. Elles ne sont pas comptées comme de nouvelles réécritures.

11autres entrées restent strictement identiques aux précédents lots contratunique intégrés à la capture. Ce constat d'identité ne vaut pas une nouvelle relecture juridique complète et périme si un texte dépendant change. L241-10, douzième article précédemment coordonné, reçoit au contraire le correctif002.

Les contrats financiers à terme, les préavis locatifs, les garanties de vente/construction, les indemnités d'expropriation et l'intérim d'une fonction de direction produisent des résultats de recherche sans être automatiquement des contrats d'emploi. Leur classification résiduelle reste dans la file ; aucun préavis de bail n'est réduit à15jours par cette recherche.

## File restante et limites

**1 187 entrées restent explicitement en attente de concordance**, dont de nombreux résultats larges sur « indemnité » ou sur des renvois sans lien avec la rupture. Aucun examen juridique complet, compatibilité ou correction n'est revendiqué pour elles. Les cas à forte priorité comportent un indicateur `contract_or_employment_context`, les autres `outgoing_reference_or_broad_indemnity_filter`. Le prochain lot doit recevoir les textes complets réellement liés et périmer tout contrôle lorsque ces dépendances changent. Aucune exploration supplémentaire n'est ouverte après le paquet ultramarin, conformément au checkpoint demandé par le parent.

Les frontières horscorpus demeurent explicites :

- Le CASF, notamment les statuts d'assistantsmaternels/familiaux auxquels renvoient L531-5 et80sexies, n'est pas réécrit ici. Aucun barème privé ne remplace silencieusement leurs règles spécifiques de retrait d'enfant, préavis ou indemnité. Les abattements fiscaux et aides du présent corpus restent conservés.
- Les régimes d'agentspublics/CGFP, les statuts de détachement et la rupture du directeurOPH restent distincts. Le fondsL135-9 et leCLEISS L767-1 distinguent expressément leurs recrutementsprivés futurs des contrats publics qui peuvent encore être à durée déterminée.
- Les arrêtés de revalorisation annuelle du versement santéD911-8 et les modalités extérieures référencées par les déclarations ne sont pas prétendus réécrits. La règle d'indexation et les garanties existantes restent entières.
- Les autres codes évoqués dans les textes (rural, éducation, mutualité, commerce,LPF) ne sont pas réputés coordonnés intégralement. Les renvois utiles sont conservés ; leur suppression ne découle pas du seul remplacement desCDD.

Les propositions reprennent les avant-images existantes lorsqu'elles contiennent déjà une réforme : annexeIII39 conserve exactement la suppressionCVAE et le réemploi des informations. Aucune ISannuelle, succession taxable nouvelle ou CVAE n'est restaurée. Il n'est pas fait de bilan financier ou de compensation inventée.
