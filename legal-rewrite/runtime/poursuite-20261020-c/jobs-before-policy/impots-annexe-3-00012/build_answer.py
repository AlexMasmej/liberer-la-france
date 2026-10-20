import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(index, xml, reason, notes):
    assert index not in drafts
    source = sources[index]
    drafts[index] = {
        key: source[key]
        for key in ('code_id', 'source_id', 'source_sha256', 'number')
    }
    drafts[index].update(
        proposed_xml=xml.strip(), reason=reason, review_notes=notes,
        status='rewrite_draft',
    )


add(0, '''
<p>Pour l'application du 2 du I de l'article 163 quatervicies du code général des impôts, les cotisations ou primes versées au cours d'une année s'imputent d'abord sur le plafond de déduction de cette même année, déterminé conformément au a du 2 du I de cet article. Elles s'imputent ensuite, s'il y a lieu, sur les soldes non utilisés des plafonds de déduction des cinq années précédentes, définis au b du 2 du I du même article, en commençant par le solde le plus ancien.</p>
''',
"Réécriture à droit constant : l'ordre d'imputation est présenté en deux phrases, en distinguant le plafond de l'année des reports des cinq années précédentes. Aucune réforme de fond de l'épargne retraite n'est introduite.",
"Les cinq années de report et la priorité au solde le plus ancien sont maintenues. La note relative à l'article 10-I de la loi n° 2026-103 du 19 février 2026 est historique ; elle ne fixe aucune entrée en vigueur du projet. Le compte de capitalisation projeté par le CSS L. 241-3 ne relève pas automatiquement du CGI 163 quatervicies : son éventuel régime fiscal doit être défini dans une disposition législative expresse et coordonné, si nécessaire, avec les articles 41 ZZ ter à 41 ZZ quinquies.")

add(1, '''
<p>Avant le 1er mars de chaque année, les organismes gestionnaires des plans, contrats ou régimes mentionnés au 1 du I de l'article 163 quatervicies du code général des impôts délivrent à leurs cotisants une attestation. Celle-ci indique le montant des cotisations ou primes versées au cours de l'année civile écoulée qui ouvrent droit à déduction du revenu global. Pour les régimes de retraite complémentaire mentionnés au c du 1 du I de cet article, l'attestation indique distinctement, s'il y a lieu, le montant des cotisations ou primes correspondant aux rachats mentionnés au c du 2 du I du même article.</p>
<p>Les organismes gestionnaires transmettent à l'administration fiscale, dans le même délai, un double de l'attestation mentionnée au premier alinéa.</p>
''',
"Réécriture à droit constant : la date de délivrance est mise en tête, les mentions de l'attestation sont séparées en phrases et l'auteur de la transmission du double est explicité. Aucune réforme de fond.",
"Délai antérieur au 1er mars, période de l'année civile écoulée et distinction des rachats maintenus. Les renvois au 1 et au 2 du I du CGI 163 quatervicies restent distincts. Aucune extension aux nouveaux comptes de capitalisation collective du projet ; une telle extension suppose une définition législative préalable de leur traitement fiscal.")

add(2, '''
<p>Les organismes gestionnaires des plans d'épargne retraite mentionnés à l'article L. 224-1 du code monétaire et financier déclarent à l'administration fiscale, pour chacun de leurs souscripteurs, le montant des versements effectués sur ces plans au cours de l'année civile précédente ou du dernier exercice clos. Cette obligation concerne les versements susceptibles d'être déduits dans les conditions prévues au d du 1 du I de l'article 163 quatervicies, au troisième alinéa du I de l'article 154 bis ou au deuxième alinéa du I de l'article 154 bis-0 A du code général des impôts.<br/><br/>Pour les versements réalisés l'année précédente, ces renseignements doivent parvenir à l'administration fiscale avant le 16 février de chaque année. Ils sont portés sur la déclaration prévue au 1 de l'article 242 ter du code général des impôts.</p>
''',
"Réécriture à droit constant : la déclaration par souscripteur, les périodes de référence et le champ des versements déductibles sont explicités dans des phrases distinctes. Le support déclaratif et son échéance sont conservés ; aucune réforme de fond.",
"Maintien de l'alternative année civile précédente/dernier exercice clos et du délai antérieur au 16 février, formulé dans la source pour les versements de l'année précédente. Les trois fondements de déduction et leurs cibles d'alinéas ne sont pas déplacés. Les plans du code monétaire et financier ne sont pas assimilés au compte projeté par le CSS L. 241-3 ; ce compte appelle, si un traitement fiscal particulier est retenu, une disposition législative propre et sa coordination déclarative.")

add(3, '''
<p>Le contribuable établit la déclaration prévue au 1 de l'article 170 du code général des impôts sur les imprimés établis par l'administration conformément aux modèles arrêtés par le ministre de l'économie et des finances.</p>
<p>Il y indique notamment le montant des éléments composant son revenu brut global. Ce montant est détaillé par nature de revenu et déterminé selon les règles propres à chaque catégorie.</p>
<p>Le contribuable déclare également, de manière séparée, les revenus mentionnés au troisième alinéa du 1 de l'article 49 F.</p>
<p>Il indique séparément dans la déclaration le montant des revenus de toute nature qu'il a encaissés, directement ou indirectement, à Saint-Pierre-et-Miquelon, en Nouvelle-Calédonie, en Polynésie française, dans les îles Wallis et Futuna, dans les Terres australes et antarctiques françaises et à l'étranger.</p>
''',
"Réécriture à droit constant : le contribuable est désigné comme auteur de la déclaration et les obligations de ventilation sont formulées directement, dans les quatre alinéas d'origine. Aucune réforme de fond.",
"Le renvoi initial, écrit dans la source « au 1 l'article 170 », est rendu grammaticalement explicite sans changer sa cible. Le troisième alinéa du 1 de l'article 49 F, vérifié dans le corpus local, vise les produits et revenus imposables ayant déjà supporté les prélèvements sociaux sur les produits de placement. Tous les territoires énumérés et les encaissements indirects sont maintenus. L'articulation avec les modalités générales de déclaration en ligne n'est pas modifiée par cet article.")

add(4, '''
<p>Les déclarants fournissent toutes les indications nécessaires sur leur situation et leurs charges de famille.</p>
<p>Pour bénéficier des déductions ou réductions d'impôt prévues aux articles 156 et 199 septies du code général des impôts, ils produisent également un état des charges à prendre en compte pour déterminer le revenu imposable ou le montant des réductions d'impôt.</p>
<p>Pour les dettes contractées et les rentes payées à titre obligatoire et gratuit, cet état indique le nom et le domicile du créancier, la date et la nature du titre constatant la créance, ainsi que le montant annuel des intérêts ou arrérages. S'il y a lieu, il précise aussi le nom et la résidence de l'officier public qui a dressé l'acte ou la juridiction dont émane le jugement.</p>
<p>Le déclarant fournit les renseignements prévus au troisième alinéa lorsqu'il demande, pour déterminer les revenus nets des propriétés foncières bâties et non bâties, la déduction des intérêts de dettes contractées pour conserver, acquérir, construire, réparer ou améliorer ces propriétés.</p>
''',
"Réécriture à droit constant : les informations justificatives sont ordonnées et la condition relative aux intérêts fonciers est exprimée avec un sujet explicite. Les quatre alinéas et le renvoi au troisième sont conservés. Aucune réforme de fond.",
"Maintien des articles 156 et 199 septies, des rentes obligatoires et gratuites et des cinq objets des dettes foncières. La production de l'état des charges n'est pas supprimée au titre de l'objectif général de réemploi des données : une telle suppression nécessiterait des règles précises sur les données disponibles légalement et leur correction.")

add(5, '''
<p>I. – 1° Chaque époux ou partenaire lié par un pacte civil de solidarité exerce l'option prévue au deuxième alinéa du 5 de l'article 6 du code général des impôts sur sa déclaration d'ensemble des revenus prévue au 1 de l'article 170 du même code.</p>
<p>Il y indique l'identité de son conjoint ou de son partenaire ;</p>
<p>2° Les époux ou partenaires sont soumis à l'imposition commune selon les règles de droit commun si l'un au moins d'entre eux n'a pas exercé l'option dans les conditions du 1° et dans les délais prévus au premier alinéa de l'article 175 du code général des impôts.</p>
<p>II. – 1° En cas d'imposition distincte, les revenus personnels comprennent les traitements et salaires, les pensions et rentes viagères, les rémunérations allouées aux gérants et associés de certaines sociétés, les bénéfices non commerciaux, les bénéfices industriels et commerciaux et les bénéfices agricoles ;</p>
<p>2° Les autres revenus ou profits dont le couple a disposé pendant l'année du mariage, de la séparation, du divorce, de la conclusion ou de la dissolution du pacte civil de solidarité sont réputés être des revenus communs.</p>
<p>III. – 1° Pour justifier la répartition de la quote-part des revenus communs mentionnée au deuxième alinéa du 5 et au premier alinéa du 6 de l'article 6 du code général des impôts, le contribuable démontre la propriété exclusive ou la répartition réelle des revenus et profits. Il s'appuie à cette fin sur tout document permettant d'établir l'origine de propriété des biens ou sommes concernés ;</p>
<p>2° Constituent de tels documents :</p>
<p>a) L'acte authentique qui mentionne l'origine de propriété et, selon le cas, la répartition dans l'indivision ou le démembrement ;</p>
<p>b) Tout justificatif établi au nom du ou des bénéficiaires des revenus ou produits par les établissements payeurs, les prestataires de services d'investissement, les établissements de crédit ou les organismes habilités à détenir et à négocier des valeurs mobilières pour le compte de particuliers. Ce justificatif atteste le montant des revenus ou produits et leur date de mise à disposition ;</p>
<p>c) En cas de cession de droits sociaux ou de valeurs mobilières pendant l'année d'imposition, tout justificatif attestant l'origine de propriété de ces droits ou valeurs, ainsi que la date de réalisation et le montant des gains correspondants.</p>
<p>Les contribuables communiquent ces documents à l'administration fiscale à sa demande.</p>
''',
"Réécriture à droit constant : les conditions de l'option individuelle, les catégories de revenus et les modes de preuve sont formulés en phrases plus courtes. Les I à III, leurs numéros, lettres et alinéas sont maintenus. Aucune réforme de fond.",
"Les deux membres du couple doivent opter dans les délais pour éviter l'imposition commune. Maintien de tous les événements familiaux, des catégories de revenus et des trois types de justificatifs ; leur communication demeure exigible sur demande. Les renvois aux alinéas des articles 6 et 175 ne sont pas modifiés.")

add(6, '''
<p>Dans le délai prévu à l'article 175 du code général des impôts, les contribuables remettent ou adressent leurs déclarations dûment signées au service des impôts du lieu de leur résidence ou de leur principal établissement.</p>
<p>Le service des impôts leur délivre un récépissé.</p>
<p>Les personnes physiques qui résident habituellement dans la principauté de Monaco tout en étant fiscalement domiciliées en France déposent leurs déclarations auprès du service désigné par le ministre chargé du budget.</p>
''',
"Réécriture à droit constant : l'échéance, les modalités de dépôt et l'auteur du récépissé sont rendus explicites. La règle propre aux résidents de Monaco reste dans son alinéa. Aucune réforme de fond.",
"Maintien de la signature, du choix entre remise et envoi et de l'alternative résidence/principal établissement. Les deux conditions cumulatives relatives à Monaco sont conservées. Le délai de l'article 175 reste inchangé ; aucune nouvelle procédure de dépôt n'est créée.")

add(7, '''
<p>Le ministre de l'économie et des finances peut, par arrêté, imposer la remise en plusieurs exemplaires des déclarations mentionnées aux articles 42 à 45 et des déclarations spéciales prévues aux articles 53 A et 97 du code général des impôts.</p>
''',
"Réécriture à droit constant : la faculté ministérielle est exprimée directement et son champ déclaratif est regroupé dans une seule phrase. Aucune réforme de fond.",
"Le pouvoir reste facultatif et subordonné à un arrêté. Le périmètre 42 à 45, 53 A et 97 est conservé. L'objectif de suppression des demandes en double ne fournit pas à lui seul les modalités nécessaires pour supprimer ce pouvoir réglementaire ou les obligations existantes.")

add(8, '''
<p>L'administration fiscale ne met pas à la disposition du contribuable le document prévu au premier alinéa de l'article 171 du code général des impôts si celui-ci se trouve dans au moins l'une des situations suivantes :<br/><br/>1° Son impôt sur le revenu de l'année précédente n'a pas été établi ;<br/><br/>2° Son impôt sur le revenu de l'année précédente a été établi en tenant compte de l'un des revenus suivants :<br/><br/>a) Bénéfices industriels et commerciaux, bénéfices agricoles ou bénéfices non commerciaux ;<br/><br/>b) Revenus fonciers ;<br/><br/>c) Rentes viagères à titre onéreux ;<br/><br/>d) Revenus mentionnés à l'article 62 du même code ;<br/><br/>e) Revenus mentionnés aux 1 bis, 1 ter ou 1 quater de l'article 93 du même code, lorsqu'ils ont été imposés selon les règles applicables aux traitements et salaires ;<br/><br/>f) Revenus ayant bénéficié de l'article 80 sexies du même code ou de la deuxième phrase du premier alinéa du 1° de l'article 81 du même code ;<br/><br/>g) Revenus de source étrangère ;</p>
<p>h) Pensions alimentaires ;<br/><br/>3° Il a déclaré, au titre de l'année précédente, un changement d'adresse, l'un des changements de situation mentionnés aux 1° à 3° du 1 de l'article 204 I du même code ou, selon les modalités de l'article 204 K du même code, un montant d'acompte pour un revenu mentionné au 2° du présent article. Relève également de ce 3° le contribuable qui a déclaré, au titre de l'avant-dernière année, des revenus soumis au versement libératoire prévu à l'article 151-0 du même code ;<br/><br/>4° Au cours de l'avant-dernière année, il a ouvert, détenu, utilisé ou clos un compte, un contrat ou un placement mentionnés aux articles 1649 A et 1649 AA du même code ;<br/><br/>5° Il a été passible de l'impôt sur la fortune immobilière au titre de l'année précédente ;<br/><br/>6° Au 31 décembre de l'avant-dernière année, il était fiscalement domicilié hors de France, résident de la principauté de Monaco, du département de Mayotte ou des collectivités de Saint-Martin ou Saint-Barthélemy, ou relevait du 2 de l'article 4 B du même code ;<br/><br/>7° Il a perçu des produits de contrats et bons de capitalisation et des produits d'assurance-vie de plus de huit ans afférents à des versements effectués à compter du 27 septembre 2017, ou il a effectué des versements sur un plan d'épargne retraite individuel mentionné à l'article L. 224-28 du code monétaire et financier ;<br/><br/>8° Les éléments détenus par l'administration fiscale lors de la mise à disposition du document mentionné au premier alinéa du présent article ne permettent pas d'identifier correctement le contribuable ou les membres de son foyer fiscal.</p>
''',
"Réécriture à droit constant : les huit causes d'exclusion sont rattachées explicitement au contribuable ; le 3° distingue les déclarations de l'année précédente de celles de l'avant-dernière année. Les lettres a à h, les deux paragraphes XML et les renvois sont maintenus. Aucune réforme de fond.",
"Contrôle particulier des années de référence : année précédente aux 1°, 2°, première partie du 3° et 5° ; avant-dernière année à la fin du 3°, au 4° et au 6°. La date du 27 septembre 2017 et la durée de plus de huit ans sont conservées. Le 7° ne reçoit pas de période de référence supplémentaire, absente de la source. Le renvoi à l'article 151-0 est confirmé par le corpus local. Le 8° conserve la formulation source relative au moment de mise à disposition, bien que l'article règle précisément les exclusions de cette mise à disposition.")

add(9, '''
<p>I. – Pour l'application du cinquième alinéa de l'article 199 decies E du code général des impôts, le contribuable joint les pièces suivantes à sa déclaration des revenus de l'année au titre de laquelle il demande la réduction d'impôt :</p>
<p>1° Une note annexe, conforme au modèle fixé par l'administration, qui indique :</p>
<p>a) L'identité et l'adresse du contribuable ;</p>
<p>b) L'adresse du logement concerné ;</p>
<p>c) Le prix d'acquisition du logement ;</p>
<p>d) La date d'achèvement du logement ou, si elle est postérieure, la date de son acquisition ;</p>
<p>e) L'engagement de louer le logement nu à l'exploitant de la résidence de tourisme pendant au moins neuf ans ;</p>
<p>2° Une copie du bail conclu avec l'exploitant de la résidence de tourisme. Ce bail mentionne la date d'effet de la location et, s'il y a lieu, la durée totale, pour chaque année civile, des périodes pendant lesquelles le propriétaire se réserve l'occupation du logement.</p>
<p>3° S'il y a lieu, une copie de l'engagement de l'exploitant de la résidence de tourisme de réserver au logement des saisonniers une proportion significative de son parc immobilier, au moins équivalente au nombre de salariés de la résidence.</p>
<p>II. – Si l'exploitant de la résidence change pendant la période couverte par l'engagement mentionné au I, le contribuable joint à sa déclaration des revenus de l'année de ce changement une copie du bail conclu avec le nouvel exploitant. Ce bail comporte les mentions prévues au 2° du I.</p>
<p>III. – Pour l'application du septième alinéa de l'article 199 decies E du code général des impôts, le conjoint survivant joint une note conforme au modèle fixé par l'administration à la déclaration des revenus qu'il souscrit pour la période de l'année du décès postérieure à celui-ci. Dans cette note, il s'engage à louer le logement nu à l'exploitant de la résidence de tourisme pendant la fraction de la période initiale de neuf ans restant à courir à la date du décès.</p>
<p>Si l'exploitant de la résidence change, le II s'applique.</p>
''',
"Réécriture à droit constant : les pièces à joindre, les mentions du bail et les obligations en cas de changement d'exploitant ou de décès sont énoncées directement. Les I à III et chaque pièce numérotée restent à leur place. Aucune réforme de fond.",
"Engagement de location nue d'au moins neuf ans, occupation réservée décomptée par année civile et reprise limitée à la durée restant à courir maintenus. Renvois aux cinquième et septième alinéas du CGI 199 decies E vérifiés dans le corpus local. La comparaison entre une proportion de parc et un nombre de salariés est une formulation préexistante, également présente dans le CGI 199 decies E ; elle est conservée et appelle clarification normative. Aucun élargissement du dispositif historique à de nouveaux investissements.")

add(10, '''
<p>I. – Si le logement appartient à une société non soumise à l'impôt sur les sociétés, celle-ci accomplit les obligations prévues à l'article 46 AGD. Elle joint l'engagement prévu par cet article à sa déclaration du résultat de l'année d'achèvement du logement ou, si elle est postérieure, de l'année de son acquisition.</p>
<p>II. – Avant le 16 février de chaque année, la société fait parvenir à ses associés un document établi en double exemplaire selon le modèle fixé par l'administration. Ce document indique, pour l'année précédente :</p>
<p>a) L'identité et l'adresse de l'associé ;</p>
<p>b) Le nombre et les numéros des parts détenues au 1er janvier et au 31 décembre et, s'il y a lieu, des parts souscrites, acquises et transmises au cours de l'année, ainsi que la date de ces opérations ;</p>
<p>c) L'attestation que l'acquisition de l'immeuble et les conditions de location respectent les conditions d'application de la réduction d'impôt. L'attestation précise que la société s'engage à louer l'immeuble nu à l'exploitant de la résidence de tourisme pendant au moins neuf ans ;</p>
<p>d) Le montant de la fraction du prix d'acquisition du logement correspondant aux droits de l'associé.</p>
<p>La société joint un exemplaire de ce document à sa déclaration de résultat.</p>
''',
"Réécriture à droit constant : la société est désignée comme responsable des formalités ; les échéances et le contenu du document aux associés sont exprimés directement. La structure I, II et a à d est conservée. Aucune réforme de fond.",
"La règle ne vise que les sociétés non soumises à l'IS : le taux national proposé à l'article 219 ne s'applique pas ici. Maintien de l'année d'acquisition si elle est postérieure à l'achèvement, du délai antérieur au 16 février, du double exemplaire, des positions au 1er janvier et au 31 décembre et de la location nue d'au moins neuf ans. Le document du II reste la cible des articles 46 AGF et 46 AGF quater.")

add(11, '''
<p>I. – Pour bénéficier de la réduction d'impôt mentionnée à l'article 199 decies E du code général des impôts, l'associé fait constater l'engagement de conserver la totalité des titres prévu à l'article 199 decies G du même code lors du dépôt de sa déclaration des revenus de l'année de souscription ou d'acquisition des parts ou, si elle est postérieure, de l'année de l'acquisition ou de l'achèvement de l'immeuble. Le conjoint survivant joint son engagement de conservation des titres à la déclaration des revenus qu'il souscrit pour la période de l'année du décès de son conjoint postérieure à celui-ci.</p>
<p>II. – Dans les trente jours suivant la date limite de dépôt de la déclaration des revenus mentionnée au I, les parts des associés qui souhaitent bénéficier de la réduction d'impôt sont inscrites sur un compte ouvert au nom de l'associé dans la comptabilité de la société ou sur un registre spécial. Les documents relatifs aux opérations qui ont affecté ce compte sont conservés jusqu'à la fin de la troisième année suivant celle où l'engagement mentionné au I expire.</p>
<p>III. – Chaque associé joint à chacune de ses déclarations des revenus un exemplaire du document mentionné au II de l'article 46 AGE.</p>
''',
"Réécriture à droit constant : le moment de constatation de l'engagement et la déclaration du conjoint survivant sont précisés par des constructions directes. Le délai d'inscription et la durée de conservation des pièces restent distincts. Aucune réforme de fond.",
"Maintien de la totalité des titres, de l'alternative entre les années prévues au I, des trente jours suivant la date limite de dépôt et de la conservation jusqu'à la fin de la troisième année suivant l'expiration. Le II conserve la référence source aux opérations affectant le compte, sans lui substituer une obligation nouvelle concernant le registre. Renvois aux articles 199 decies E, 199 decies G et 46 AGE inchangés.")

add(12, '''
<p>Pour l'application de l'article 199 decies EA du code général des impôts, les travaux de réhabilitation sont ceux qui permettent au logement, une fois les travaux réalisés, de satisfaire à toutes les performances techniques mentionnées au II de l'article 2 quindecies B. Après leur achèvement, le coût de ces travaux doit être au moins égal à 20 % du prix d'acquisition du logement avant travaux.</p>
''',
"Réécriture à droit constant : la définition des travaux est rattachée explicitement aux performances du logement après travaux et le seuil de coût est formulé directement. Aucune réforme de fond.",
"Toutes les performances du II de l'article 2 quindecies B restent exigées. Le seuil de 20 % est un rapport entre coût des travaux achevés et prix d'acquisition avant travaux, et non un taux d'impôt sur les sociétés. Il n'est pas modifié par le taux national de 20 % proposé pour l'IS. Aucune extension au parcours de rénovation locative de vingt-quatre mois du projet.")

add(13, '''
<p>I. – Pour l'application de l'article 199 decies EA du code général des impôts, le contribuable joint à sa déclaration des revenus de l'année au titre de laquelle il demande la réduction d'impôt tous les engagements, documents et éléments prévus au I de l'article 46 AGD, sauf ceux mentionnés au d du 1° et au 3° de ce I. Il indique en outre, dans la note annexe prévue au 1° du I de cet article, la date et le prix d'acquisition du logement, les dates d'achèvement du logement et des travaux de réhabilitation, ainsi que le montant effectivement payé pour ces travaux.</p>
<p>Le contribuable joint une copie des factures des entreprises qui ont réalisé les travaux. Ces factures indiquent l'adresse où les travaux ont été réalisés, leur nature et leur montant. Il joint également une copie de l'engagement mentionné à l'article 46 AGF sexies.</p>
<p>II. – Les II et III de l'article 46 AGD s'appliquent au présent article.</p>
''',
"Réécriture à droit constant : les exceptions à la liste des pièces, les mentions complémentaires et les factures sont formulées avec un responsable explicite. Les deux alinéas du I et le II sont maintenus. Aucune réforme de fond.",
"L'exception porte sur le d du 1° et sur le 3° du I de l'article 46 AGD. Elle ne dispense pas de la copie de l'engagement propre à l'article 46 AGF sexies. Les dates d'achèvement du logement et des travaux sont toutes deux conservées ; le montant déclaré reste celui effectivement payé. Les coordinations de changement d'exploitant et de conjoint survivant passent toujours par les II et III de 46 AGD.")

add(14, '''
<p>I. – Si le logement appartient à une société non soumise à l'impôt sur les sociétés, celle-ci accomplit les obligations prévues à l'article 46 AGF ter. Elle joint l'engagement prévu par cet article à sa déclaration du résultat de l'année d'achèvement des travaux de réhabilitation.</p>
<p>II. – Avant le 16 février de chaque année, la société fait parvenir à ses associés un document établi en double exemplaire selon le modèle fixé par l'administration. Ce document comporte, pour l'année précédente, les éléments mentionnés aux a et b du II de l'article 46 AGE ainsi que les renseignements suivants :</p>
<p>a) L'attestation que l'acquisition de l'immeuble, la réalisation des travaux de réhabilitation et les conditions de location respectent les conditions d'application de la réduction d'impôt. L'attestation précise que la société s'engage à louer l'immeuble nu à l'exploitant de la résidence de tourisme pendant au moins neuf ans ;</p>
<p>b) Le montant correspondant aux droits de l'associé dans le prix de revient du logement majoré des travaux de réhabilitation.</p>
<p>La société joint un exemplaire de ce document à sa déclaration de résultat.</p>
''',
"Réécriture à droit constant : les obligations de la société et les mentions du document annuel sont formulées directement, avec conservation des I et II et de leurs alinéas. Aucune réforme de fond.",
"Maintien des sociétés non soumises à l'IS, de l'année d'achèvement des travaux, du délai antérieur au 16 février, du double exemplaire et de la location nue d'au moins neuf ans. La base du b demeure le prix de revient majoré des travaux, et non le seul prix d'acquisition visé à l'article 46 AGE. Le II reste la cible de l'article 46 AGF quinquies.")

add(15, '''
<p>I. – Pour bénéficier de la réduction d'impôt mentionnée à l'article 199 decies EA du code général des impôts, l'associé fait constater l'engagement de conserver la totalité des titres prévu à l'article 199 decies G du même code lors du dépôt de sa déclaration des revenus de l'année de souscription ou d'acquisition des parts ou, si elle est postérieure, de l'année d'achèvement des travaux de réhabilitation. Le conjoint survivant joint son engagement de conservation des titres à la déclaration des revenus qu'il souscrit pour la période de l'année du décès de son conjoint postérieure à celui-ci.</p>
<p>II. – Dans les trente jours suivant la date limite de dépôt de la déclaration des revenus mentionnée au I, les parts des associés qui souhaitent bénéficier de la réduction d'impôt sont inscrites sur un compte ouvert au nom de l'associé dans la comptabilité de la société ou sur un registre spécial. Les documents relatifs aux opérations qui ont affecté ce compte sont conservés jusqu'à la fin de la troisième année suivant celle où l'engagement mentionné au I expire.</p>
<p>III. – Chaque associé joint à chacune de ses déclarations des revenus un exemplaire du document mentionné au II de l'article 46 AGF quater.</p>
''',
"Réécriture à droit constant : l'engagement de l'associé, sa date de constatation et l'obligation du conjoint survivant sont exposés directement. Les délais d'inscription et de conservation sont rendus plus lisibles, sans changement de fond.",
"La référence temporelle propre à la réhabilitation demeure l'année d'achèvement des travaux, si elle est postérieure à la souscription ou à l'acquisition des parts. Maintien de la totalité des titres, des trente jours et de la fin de la troisième année suivant l'expiration. Les renvois aux articles 199 decies EA, 199 decies G et au II de 46 AGF quater sont conservés ; aucune modification des engagements en cours.")

add(16, '''
<p>Pour l'application du cinquième alinéa de l'article 199 decies EA du code général des impôts, l'exploitant de la résidence de tourisme s'engage par écrit à réserver au moins 15 % des logements aux salariés saisonniers. Il joint cet engagement à sa déclaration de résultat et en délivre une copie à l'acquéreur d'un logement dans la résidence.</p>
<p>Sont des salariés saisonniers les salariés qui occupent un emploi au sens du 3° de l'article L. 1242-2 du code du travail et qui sont liés par un contrat de travail à au moins une entreprise, une association ou un organisme établis dans la commune d'implantation de la résidence, dans une commune limitrophe ou dans une commune membre du groupement de communes.</p>
<p>Le pourcentage prévu au premier alinéa est calculé en tenant compte du nombre de logements situés dans la résidence de tourisme réhabilitée. Les logements réservés peuvent se trouver dans cette résidence ou dans d'autres résidences gérées par le même exploitant. Dans ce dernier cas, ces autres résidences doivent respecter les mêmes normes de classement et être situées dans la même commune ou dans une commune limitrophe incluse dans une zone mentionnée au premier alinéa de l'article 199 decies EA du code général des impôts.</p>
''',
"Réécriture à droit constant : les formalités de l'exploitant sont exprimées directement et les conditions d'utilisation d'autres résidences sont réparties en plusieurs phrases au même alinéa. La définition des saisonniers et les trois alinéas sont conservés. Aucune réforme de fond.",
"Le minimum de 15 % porte sur les logements de la résidence réhabilitée, même si les logements réservés sont ailleurs. Les conditions territoriales relatives à l'employeur du saisonnier restent distinctes de celles relatives aux autres résidences. Le cinquième alinéa du CGI 199 decies EA a été vérifié dans le corpus local. La note concernant l'ordonnance n° 2007-329 du 12 mars 2007 explique une coordination historique avec le code du travail ; elle ne date pas la réforme projetée.")

add(17, '''
<p>I. – Pour l'application des sixième et septième phrases du cinquième alinéa de l'article 199 decies E du code général des impôts, les copropriétaires qui détiennent au moins 50 % des appartements de la résidence peuvent confier à une ou plusieurs entreprises l'ensemble des prestations additionnelles à l'hébergement mentionnées au b du 4° de l'article 261 D du même code. Ils procèdent selon l'une des modalités suivantes :</p>
<p>1° Chacun contracte directement avec les entreprises qu'ils ont choisies conjointement ;</p>
<p>2° Ils créent une entreprise qui contracte avec les entreprises chargées des prestations.</p>
<p>II. – Dans les cas prévus au I, une dérogation est possible à l'obligation de faire gérer la résidence de tourisme par une seule personne physique ou morale, prévue à la dernière phrase de l'article D. 321-1 du code du tourisme.</p>
''',
"Réécriture à droit constant : les deux modalités de contractualisation sont présentées avec des sujets explicites et l'objet de la dérogation de gestion est clarifié. Les I et II et les deux options numérotées sont maintenus. Aucune réforme de fond.",
"Maintien du seuil d'au moins 50 % des appartements et de la réalisation de l'ensemble des prestations visées. Les sixième et septième phrases du cinquième alinéa du CGI 199 decies E, vérifiées dans le corpus local, conservent notamment les conditions du remplacement du gestionnaire défaillant ; le présent article ne les écarte pas. La soudure typographique source « E du » est rétablie. Les références au b du 4° de l'article 261 D et à la dernière phrase de D. 321-1 sont maintenues.")

add(18, '''
<p>I. – Pour l'application des 1°, 4° et 6° du II de l'article 200 quindecies du code général des impôts, les contribuables tiennent à la disposition de l'administration fiscale une note conforme au modèle fixé par celle-ci. Cette note comporte les éléments suivants :</p>
<p>a. L'identité et l'adresse du contribuable ;</p>
<p>b. La désignation de la ou des parcelles concernées, qu'il s'agisse de terrains en nature de bois et forêts ou de terrains nus à boiser ;</p>
<p>c. Pour l'application du 1° du II de l'article 200 quindecies du code général des impôts, le prix et la date d'acquisition du ou des terrains concernés ;</p>
<p>d. Pour l'application du 4° du II de l'article 200 quindecies du code général des impôts, la nature, le montant et la date de paiement des travaux forestiers réalisés. S'il y a lieu, les contribuables tiennent aussi à la disposition de l'administration fiscale le document du fournisseur des matériels forestiers de reproduction utilisés, mentionné à l'article R. 153-16 du code forestier, et une attestation sur l'honneur du respect de l'arrêté régional relatif aux matériels forestiers de reproduction éligibles aux aides de l'Etat à l'investissement forestier. Si le contribuable est titulaire d'un compte d'investissement forestier et d'assurance prévu à l'article L. 352-1 du code forestier, il tient également à disposition une attestation sur l'honneur selon laquelle les sommes dépensées pour les travaux et pour lesquelles il demande le crédit d'impôt ne proviennent pas de ce compte ;</p>
<p>e. Pour l'application du 4° du II de l'article 200 quindecies du code général des impôts, la nature de la garantie de gestion durable applicable à la propriété concernée ;</p>
<p>f. Pour l'application des 1° et 4° du II de l'article 200 quindecies du code général des impôts, la déclaration d'engagement prévue par ces dispositions.</p>
<p>II. – a. Pour l'application du 6° du II de l'article 200 quindecies du code général des impôts, le contribuable présente à l'administration fiscale, à sa demande, une attestation de l'entreprise d'assurance. Celle-ci précise l'identité et l'adresse de l'assureur, la nature des risques couverts, le nombre d'hectares assurés contre le risque de tempête ou d'incendie et le montant de la cotisation d'assurance versée au titre de l'année civile pour couvrir notamment au moins l'un de ces risques. Si le contribuable est titulaire d'un compte d'investissement forestier et d'assurance prévu à l'article L. 352-1 du code forestier, il présente également une attestation sur l'honneur selon laquelle les sommes dépensées pour payer les cotisations de ce contrat d'assurance et pour lesquelles il demande le crédit d'impôt ne proviennent pas de ce compte.</p>
<p>b. (Abrogé)</p>
''',
"Réécriture à droit constant : les pièces forestières, les attestations et leurs conditions sont réparties en phrases courtes à l'intérieur de chaque alinéa d'origine. La distinction entre tenue à disposition et présentation sur demande est conservée. Aucune réforme de fond.",
"Les 1°, 4° et 6° du II du CGI 200 quindecies demeurent distincts. Maintien des deux attestations de non-financement par le compte forestier, de l'arrêté régional, des références R. 153-16 et L. 352-1 et de l'alternative tempête/incendie. Le b abrogé demeure en place. La note source rend ces dispositions applicables aux opérations forestières réalisées à compter du 1er janvier 2023, conformément à l'article 2 du décret n° 2023-524 du 29 juin 2023 ; cette portée temporelle reste à conserver avec le texte. Les mentions de l'ordonnance n° 2012-92 et du décret n° 2012-836 sont historiques.")

add(19, '''
<p>I. – Le contribuable qui souhaite bénéficier du crédit d'impôt en application des 2° et 3° du II de l'article 200 quindecies du code général des impôts en informe le groupement forestier ou la société d'épargne forestière dont il a souscrit ou acquis les parts. Il le fait au plus tard le 31 décembre de l'année de souscription ou d'acquisition. Le groupement ou la société joint à sa déclaration de résultat de cette même année les déclarations d'engagement prévues par ces dispositions, établies selon les modèles fixés par l'administration.</p>
<p>Pour l'application du 5° du II de l'article 200 quindecies du code général des impôts, le groupement ou la société joint à sa déclaration de résultat de l'année de paiement des travaux les déclarations d'engagement prévues par ces dispositions, établies selon les modèles fixés par l'administration. Si le groupement n'est pas tenu de souscrire une déclaration de résultat, il produit ces déclarations d'engagement auprès du service des impôts dont dépend son siège social ou, à défaut de siège social, la commune dans le ressort de laquelle se situe la surface la plus importante de ses bois et forêts. Il les produit au plus tard le deuxième jour ouvré suivant le 1er mai de l'année qui suit celle du paiement des travaux.</p>
<p>II. – Le groupement ou la société délivre à ses associés ou membres qui souhaitent bénéficier du crédit d'impôt un document conforme au modèle fixé par l'administration. Il le délivre avant le 16 février de l'année civile suivant celle de la souscription ou de l'acquisition des parts, celle du paiement des travaux forestiers réalisés par le groupement ou la société ou celle du versement de la cotisation d'assurance. Toutefois, si les travaux forestiers sont réalisés par un groupement d'intérêt économique et environnemental forestier dont le contribuable est membre indirectement, par l'intermédiaire d'un groupement forestier ou d'une société d'épargne forestière, le document est délivré à ce groupement forestier ou à cette société d'épargne forestière. Le groupement forestier ou la société d'épargne forestière utilise ce document pour établir, dans les conditions du présent alinéa, le document de même nature à délivrer à ses propres associés. Le document comporte les renseignements suivants pour l'année précédente :</p>
<p>a. La raison sociale et l'adresse du siège social du groupement ou de la société. Si le groupement est un groupement d'intérêt économique et environnemental forestier sans siège social, le document identifie aussi la commune dans le ressort de laquelle se situe la surface la plus importante de ses bois et forêts ;</p>
<p>b. Dans les cas prévus aux 2°, 3° et 5° du II de l'article 200 quindecies du code général des impôts, l'attestation que les engagements mentionnés au I ont été pris et sont respectés.</p>
<p>c. Dans le cas prévu au 5° du II de l'article 200 quindecies du code général des impôts, la nature de la garantie de gestion durable applicable à la propriété concernée, ainsi que la nature, le montant total et la date de paiement des travaux forestiers. S'il y a lieu, le groupement ou la société délivre aussi le document du fournisseur des matériels forestiers de reproduction utilisés, mentionné à l'article R. 153-16 du code forestier, et une attestation sur l'honneur du respect de l'arrêté régional relatif aux matériels forestiers de reproduction éligibles aux aides de l'Etat à l'investissement forestier ;</p>
<p>c bis. (Abrogé) ;</p>
<p>d. Dans les cas prévus au 5° du II de l'article 200 quindecies du code général des impôts, le nombre et le pourcentage des parts du groupement ou de la société détenues par l'associé ou le membre ou, si un groupement d'intérêt économique et environnemental forestier n'émet pas de parts, la quote-part du montant des travaux forestiers affectée au membre ;</p>
<p>e. Dans le cas prévu au 6° du II de l'article 200 quindecies du code général des impôts, l'attestation de l'entreprise d'assurance. Celle-ci précise l'identité et l'adresse de l'assureur, la nature des risques couverts, le nombre d'hectares assurés contre le risque de tempête ou d'incendie et le montant de la cotisation d'assurance versée au titre de l'année civile pour couvrir notamment au moins l'un de ces risques.</p>
<p>III. – Chaque année, le groupement ou la société joint à sa déclaration de résultat un document conforme au modèle fixé par l'administration. Si le groupement n'est pas tenu de souscrire une déclaration de résultat, il produit ce document auprès du service des impôts dont dépend son siège social ou, à défaut de siège social, la commune dans le ressort de laquelle se situe la surface la plus importante de ses bois et forêts, au plus tard le deuxième jour ouvré suivant le 1er mai de l'année suivant celle du paiement des travaux. Ce document comporte les renseignements suivants :</p>
<p>a. La raison sociale et l'adresse du siège social du groupement ou de la société. Si le groupement est un groupement d'intérêt économique et environnemental forestier sans siège social, le document identifie aussi la commune dans le ressort de laquelle se situe la surface la plus importante de ses bois et forêts ;</p>
<p>b. L'attestation que les engagements mentionnés au I ont été pris et sont respectés ;</p>
<p>c. L'identité et l'adresse de chacun des associés ou membres ;</p>
<p>d. Le nombre, les numéros et les valeurs nominales des parts détenues par chacun des associés ou membres au 1er janvier et au 31 décembre de l'année précédente. Le document indique aussi, s'il y a lieu, le nombre, les numéros et les valeurs nominales des parts souscrites, acquises et transmises au cours de l'année, ainsi que la date de ces opérations. Si le groupement n'émet pas de parts, le document comporte la liste de ses membres au 1er janvier et au 31 décembre de l'année précédente et précise, s'il y a lieu, les dates d'adhésion au groupement et de sortie de celui-ci au cours de l'année ;</p>
<p>e. Pour l'application des 4° et 5° du II de l'article 200 quindecies du code général des impôts, la nature, le montant et la date de paiement des travaux forestiers éligibles au crédit d'impôt, ainsi que la désignation des parcelles concernées, qu'il s'agisse de terrains en nature de bois et forêts ou de terrains nus à boiser. S'il y a lieu, le groupement ou la société joint le document du fournisseur des matériels forestiers de reproduction utilisés, mentionné à l'article R. 153-16 du code forestier, et une attestation sur l'honneur du respect de l'arrêté régional relatif aux matériels forestiers de reproduction éligibles aux aides de l'Etat à l'investissement forestier ;</p>
<p>f. (Abrogé) ;</p>
<p>g. L'attestation de l'entreprise d'assurance précisant l'identité et l'adresse de l'assureur mentionné au 6° du II de l'article 200 quindecies du code général des impôts, la nature des risques couverts, le nombre d'hectares assurés contre le risque de tempête ou d'incendie et le montant de la cotisation d'assurance versée au titre de l'année civile pour couvrir notamment au moins l'un de ces risques.</p>
<p>IV. – Dans les trente jours suivant la date limite de dépôt de la déclaration des revenus de l'année au cours de laquelle le crédit d'impôt a été demandé, les parts des associés ou membres qui souhaitent en bénéficier sont inscrites sur un compte ouvert au nom de l'associé ou du membre dans la comptabilité du groupement ou de la société ou sur un registre spécial. Si le groupement est un groupement d'intérêt économique et environnemental forestier qui n'émet pas de parts, l'identité et l'adresse des membres qui souhaitent bénéficier du crédit d'impôt sont inscrites sur un registre spécial dans le même délai. Le groupement ou la société tient ce compte ou ces registres et conserve les documents relatifs aux opérations qui les affectent jusqu'à la fin de la troisième année suivant celle de l'expiration de l'engagement de conservation des parts ou de l'engagement de rester membre du groupement d'intérêt économique et environnemental forestier prévus aux 2°, 3° et 5° du II de l'article 200 quindecies du code général des impôts.</p>
''',
"Réécriture à droit constant : chaque procédure distingue l'auteur, le document, son destinataire et son échéance. Les longues phrases des I à IV sont divisées dans leurs alinéas, en conservant les obligations des groupements sans siège ou sans parts et la transmission aux membres indirects. Aucune réforme de fond.",
"Les quatre subdivisions, toutes les lettres, c bis et f abrogés sont maintenus. Contrôle des échéances : 31 décembre, avant le 16 février, deuxième jour ouvré suivant le 1er mai, trente jours et fin de la troisième année suivant l'expiration de l'engagement. Le III associe dans la source une obligation annuelle et, pour le groupement sans déclaration de résultat, une échéance liée à l'année du paiement des travaux : cette articulation reste à clarifier par une coordination expresse, sans la remplacer par un délai nouveau. Les deux situations de membre indirect et de groupement sans parts restent distinctes. Selon la note source, l'article 2 du décret n° 2023-524 du 29 juin 2023 rend ces dispositions applicables aux opérations forestières réalisées à compter du 1er janvier 2023 ; cette portée temporelle est conservée.")

add(20, '''
<p>I. – Les contribuables conservent à la disposition de l'administration fiscale l'engagement de conserver les parts ou de rester membre du groupement d'intérêt économique et environnemental forestier prévu aux 2°, 3° et 5° du II de l'article 200 quindecies du code général des impôts. Cet engagement est établi selon le modèle fixé par l'administration.</p>
<p>II. – Les associés ou membres conservent à la disposition de l'administration fiscale le document mentionné au II de l'article 46 AGI.</p>
''',
"Réécriture à droit constant : les deux formes d'engagement et l'exigence de conformité au modèle sont présentées en phrases distinctes. Le document des associés ou membres reste traité séparément au II. Aucune réforme de fond.",
"Les contribuables restent tenus de garder les pièces à disposition, sans nouvelle obligation de les joindre systématiquement à une déclaration. Renvois aux 2°, 3° et 5° du II du CGI 200 quindecies et au II de 46 AGI maintenus. La note source, fondée sur l'article 2 du décret n° 2023-524 du 29 juin 2023, prévoit l'application aux opérations forestières réalisées à compter du 1er janvier 2023 ; cette règle temporelle est conservée.")

add(21, '''
<p>I. – Pour l'application des 4° et 5° du II de l'article 200 quindecies du code général des impôts, le crédit d'impôt peut porter sur les travaux suivants : plantation, reconstitution, renouvellement, sauvegarde et amélioration des peuplements, ainsi que création et amélioration des dessertes.</p>
<p>II. – Le contrat d'assurance mentionné au 6° du II de l'article 200 quindecies du code général des impôts doit garantir notamment le risque de tempête ou le risque d'incendie affectant des terrains en nature de bois et forêts.</p>
''',
"Réécriture à droit constant : la liste des travaux éligibles est introduite explicitement et la couverture d'assurance est formulée comme une obligation du contrat. Les deux subdivisions sont conservées. Aucune réforme de fond.",
"Tous les travaux énumérés sont conservés, sans ajout d'une nouvelle catégorie. Le contrat doit couvrir notamment la tempête ou l'incendie : le texte n'impose pas de cumuler les deux risques. Le régime d'assurance du 6° reste distinct des travaux des 4° et 5°. La note relative à l'article 2 du décret n° 2023-524 du 29 juin 2023 conserve l'application aux opérations forestières réalisées à compter du 1er janvier 2023.")

add(22, '''
<p>I. – Pour l'application de l'article 199 decies I du code général des impôts, le contribuable joint à sa déclaration des revenus de l'année au titre de laquelle il demande la réduction d'impôt une note annexe conforme au modèle fixé par l'administration. Cette note indique :</p>
<p>a) L'identité et l'adresse du contribuable ;</p>
<p>b) L'adresse du logement concerné ;</p>
<p>c) Le prix d'acquisition du logement ;</p>
<p>d) Selon le cas, la date :</p>
<p>– d'achèvement du logement neuf ou, si elle est postérieure, de son acquisition ;</p>
<p>– de réception des travaux du logement rénové dans les conditions de l'article L. 262-2 du code de la construction et de l'habitation ;</p>
<p>e) L'engagement de louer le logement nu à l'exploitant de la résidence hôtelière à vocation sociale pendant au moins neuf ans ;</p>
<p>f) Le numéro, la date et le lieu de signature de l'arrêté d'agrément de la résidence hôtelière à vocation sociale prévu à l'article R. 631-9 du code de la construction et de l'habitation ;</p>
<p>g) Le numéro, la date et le lieu de signature de l'arrêté d'agrément de l'exploitant de la résidence hôtelière à vocation sociale prévu à l'article R. 631-12 du code de la construction et de l'habitation ;</p>
<p>h) La date de conclusion du bail avec l'exploitant de la résidence hôtelière à vocation sociale et la date d'effet de la location.</p>
<p>II. – Si l'exploitant de la résidence change pendant la période couverte par l'engagement mentionné au e du I, le contribuable joint à sa déclaration des revenus de l'année de ce changement une note annexe conforme au modèle fixé par l'administration. Cette note indique :</p>
<p>1° La date de conclusion du bail avec le nouvel exploitant de la résidence hôtelière à vocation sociale et la date d'effet de la location ;</p>
<p>2° Le numéro, la date et le lieu de signature de l'arrêté d'agrément du nouvel exploitant de la résidence hôtelière à vocation sociale prévu à l'article R. 631-12 du code de la construction et de l'habitation.</p>
<p>III. – Pour justifier le bien-fondé de la réduction d'impôt sur le revenu prévue à l'article 199 decies I du code général des impôts, les contribuables qui en bénéficient conservent les pièces suivantes jusqu'à l'expiration du délai pendant lequel l'administration peut exercer son droit de reprise :</p>
<p>1° Une copie de l'arrêté d'agrément de la résidence hôtelière à vocation sociale prévu à l'article R. 631-9 du code de la construction et de l'habitation ;</p>
<p>2° Une copie de l'arrêté d'agrément de l'exploitant de la résidence hôtelière à vocation sociale prévu à l'article R. 631-12 du même code ;</p>
<p>3° Le bail conclu avec l'exploitant de la résidence hôtelière à vocation sociale, qui mentionne la date d'effet de la location.</p>
<p>IV. – Pour l'application du VI de l'article 199 decies I du code général des impôts, le conjoint survivant joint une note conforme au modèle fixé par l'administration à la déclaration des revenus qu'il souscrit pour la période de l'année du décès postérieure à celui-ci. Dans cette note, il s'engage à louer le logement nu à l'exploitant de la résidence hôtelière à vocation sociale pendant la fraction de la période initiale de neuf ans restant à courir à la date du décès.</p>
<p>Si l'exploitant de la résidence change, le II s'applique.</p>
''',
"Réécriture à droit constant : les mentions de la note initiale, celles exigées lors d'un changement d'exploitant et les pièces à conserver sont exposées avec des sujets explicites. Les I à IV, les lettres, les numéros et les alinéas sont maintenus. Aucune réforme de fond.",
"Maintien des deux agréments distincts, des dates de bail et de prise d'effet, de la location nue d'au moins neuf ans et de la conservation jusqu'à l'expiration du droit de reprise. Le conjoint survivant ne s'engage que sur la fraction restant à courir, pour la période déclarative postérieure au décès. Les renvois au VI du CGI 199 decies I, à L. 262-2, R. 631-9 et R. 631-12 du CCH sont conservés. La note du décret n° 2019-873 du 21 août 2019 est historique ; aucune date future n'en est tirée.")

add(23, '''
<p>Pour l'application du troisième alinéa du 4 de l'article 199 undecies du code général des impôts :</p>
<p>1. Les organismes publics ou privés signataires du bail sont l'Etat et ses organismes ainsi que les personnes de droit public ou privé dotées de la personnalité morale.</p>
<p>2. Le personnel de ces organismes, sous-locataire du logement, est constitué des personnes qu'ils emploient et dont les rémunérations principales relèvent des traitements et salaires au sens de l'article 79 du code général des impôts. Sont toutefois exclus :</p>
<p>Les personnes mentionnées à l'article 80 ter du même code, ainsi que leurs conjoints, descendants et ascendants ;</p>
<p>Les conjoints, descendants ou ascendants des associés des sociétés mentionnées à l'article 8 du même code.</p>
<p>Ces dispositions s'appliquent aux investissements réalisés jusqu'au 31 décembre 2000.</p>
''',
"Réécriture à droit constant : les organismes et les personnes concernées sont définis directement ; les deux exclusions familiales sont conservées dans leurs alinéas. Le champ historique est formulé en phrase normative complète. Aucune réforme de fond.",
"Maintien du troisième alinéa du 4 du CGI 199 undecies, des articles 79, 80 ter et 8 et des deux exclusions distinctes. La date du 31 décembre 2000 demeure la borne des investissements concernés : le dispositif n'est ni rouvert ni étendu aux contrats ou investissements nouveaux. Le terme sous-locataire conserve son sens, sans création d'un droit nouveau à sous-louer.")

assert len(sources) == 24
assert sorted(drafts) == list(range(24))
Path('answer.json').write_text(
    json.dumps([drafts[i] for i in range(24)], ensure_ascii=False, indent=2) + '\n'
)
