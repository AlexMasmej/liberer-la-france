# IS à la distribution — contrôle fiscal

Proposition du 19 octobre 2026, non adoptée. Ce rapport distingue l’intégrité des textes, les contrôles arithmétiques et la validation juridique restant nécessaire.

## Textes confiés au rédacteur fiscal

20 articles complets :

- CGI206,209,1668,221,221 bis : lot 200.
- CGI238,220 quinquies,220 : lot 201.
- CGI223,235 terZC,1668 B,1668 D ; annexeIII358,359,360,360 bis,366 L,366 M : lot 202.
- CGI219 et 38 : propositions antérieures remplacées dans leurs lots propriétaires par `review_prior.commit`, avec archive de chaque version antérieure et contrôle de son empreinte. Le fichier non numéroté `fiscal-revisions-preview.json` est un aperçu des deux propositions, pas un lot supplémentaire enregistré.

Les autres articles des groupes, les qualifications personnelles de distribution, mère-fille, l’annexeII et le minimum mondial ont été confiés à un autre rédacteur. Aucun texte de succession à 0 % ni aucune source canonique n’a été modifié par ce lot.

## Règles centrales effectivement proposées

- 20612 : l’assujettissement personnel demeure, mais aucun IS ordinaire ne devient exigible sur un bénéfice conservé, y compris en trésorerie, sans obligation de réinvestissement.
- 209 XI : compte des bénéfices protégés d’un second IS, compartiments de taux, pertes, déficits, rapprochement annuel. Les montants anciens doivent être justifiés et ne sont ni recréés par un apport ni comptés deux fois. Les anciens déficits d’ensemble restent chez leur titulaire et peuvent couvrir le seul ancien périmètre autorisé par 223 I, sous un plafond unique ; les pertes nouvelles ne sont pas librement mutualisées.
- 209 XII/XIII et 221/221 bis : distinction entre réorganisation conservant la compétence fiscale française, imposition de sortie à perte effective de compétence et dette ancienne. Le simple passage à la distribution ne devient pas une cessation. Un ancien sursis se dénouant sans sortie ni régime annuel distinct alimente le compartiment et attend la distribution.
- 219 V : mise à disposition effective de dividendes ou biens, avantages personnels, prêts simulés, rachats et remboursements dépassant les apports réels. Les salaires et achats professionnels et les prêts commerciaux réels ne sont pas des distributions.
- 219 V/VI :20 % du bénéfice avant IS distribué, soit 20/80 du net, PME15/85 sous plafond 42 500 € avant IS et conditions antérieures. Les taux favorables 10/15/19/0 %, exonérations et quote-part 12 % ne sont pas silencieusement relevés. Leur exigibilité est elle aussi différée jusqu’à distribution et leur consommation est tracée.
- 1668 : paiement mensuel au 15 du mois suivant la distribution, aucun acompte ordinaire sur une trésorerie conservée, rapprochement et régularisation annuels. Crédits, acomptes antérieurs et créances légalement acquises restent utilisables dans leurs conditions propres. La correction d’une avance réellement remboursée est limitée à l’IS effectivement payé, sans crédit fictif.
- 223 et annexeIII : la déclaration annuelle conserve les résultats de référence et les comptes ; elle ne recrée pas une assiette annuelle d’IS ordinaire. Les dispositions trimestrielles 358–360 bis sont expressément écartées du régime nouveau, tout en demeurant complètes pour les dettes anciennes et régimes annuels distincts.
- 235 terZC,1668 B/D et annexeIII366 L/M : contributions et acomptes additionnels écartés des nouveaux faits du régime ordinaire. Les contributions de faits antérieurs demeurent dues.235 terZAA, encore cité par 1668 B, n’est pas dans le corpus canonique ; son renvoi n’est pas présenté comme un article intégralement réécrit.

## Arithmétique

Douze cas contrôlés dans `controle-arithmetique.json` : taux normal, PME, propriété intellectuelle, PV15/19 %, quote-part 12 % avec taux normal et PME, pertes totales/partielles, exonération, franchissement du plafond PME et plafond annuel des déficits 1 M€+50 %.

Pour un montant net N, une fraction taxable q, un taux t et un déficit imputé D, le texte fixe S=max(0,t×(qN−D)/(1−tq)). Le déficit est plafonné, utilisé une fois et ne peut excéder q(N+S). Pour une quote-part 12 % et un taux 20 %,97,60 € nets correspondent à 2,40 € d’IS et 100 € avant IS ; il n’est pas appliqué 20 % à l’ensemble d’un gain dont seule une fraction est taxable.

Ces contrôles valident les identités et plafonds arithmétiques ; ils ne remplacent pas une revue juridique du droit aux taux et déficits dans chaque dossier.

## Coordination non codifiée concrète

`legal-rewrite/coordinations/is-distribution/manifest.json` contient :

- L’article 48 entier de la loi 2025-127, dans sa version en vigueur depuis le 21 février 2026, avec source intégrale et proposition intégrale. Le nouveauX exclut les exercices et cotisations nouveaux d’IS ordinaire à la distribution, y compris le risque de reprise d’un IS ancien par la moyenne d’assiette. Les faits antérieurs sont maintenus.
- L’article 12 entier de la loi 2026-103, lu pour vérifier la prorogation à deux exercices et le seuil/lissage du second exercice. Il est une source modificatrice ; aucune modification distincte de cet article 12 n’est proposée.

Le manifeste et les fichierssource/proposition sont hors inventaire des 30317 entrées des cinq codes. Les empreintes portent explicitement sur les transcriptions source_xml du texte officiel rendu, pas sur un XMLDILA ou un PDFauthentifié. La formule du IVB est conservée littéralement ; l’unité du CA dit exprimé en milliards, puis soustrait à 3 milliards et divisé par 100 millions, reste à confronter au JO authentifié. Aucune formule n’a été reconstruite d’après un graphique absent.

Source canonique : https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000053542882/2026-06-20
Source modificatrice : https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053508208
Inspiration estonienne : https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends

## Limites et contrôles juridiques restants

Le taux français proposé 20 % est distinct du taux estonien actuel 22/78. L’impôt personnel et les prélèvements sociaux des associés ne sont pas supprimés. Le minimum international des articles 223 VJ et suivants garde son champ et son calendrier propres : un régime français nouveau ne satisfait pas automatiquement la condition d’antériorité au 1 erjuillet 2021 de l’article 40 de la directive 2022/2523.

Les régimes expressément distincts, notamment tonnage et revenus non lucratifs 2065/219 bis, les sorties fiscales légitimes et les autres impôts non assis sur cet IS restent applicables. AnnexeIII361/362 a été lue : ces articles relèvent de paiements de régimes particuliers maintenus et ne sont pas présentés comme supprimés.

À vérifier dans leurs textes complets et les instruments de promulgation avant adoption : conventions de crédit d’impôt et d’établissement stable ; directive 2016/1164 article 5 et garanties de paiement des sorties ; directive mère-fille et qualification autonome de la cotisation de société ; cohérence des normes comptables et de distribution commerciale ; dates, clauses de reprise et écritures de transition des régimes sectoriels ; formulaires et instructions administratives devenant incompatibles. Ces réserves ne signifient pas que ces instruments hors corpus ont été intégralement réécrits ici.

La perte et le décalage de recettes ne sont pas chiffrés dans ce lot ; aucun rendement espéré de réinvestissement n’est présenté comme financement démontré. Aucune publication n’a été effectuée par cet agent.
