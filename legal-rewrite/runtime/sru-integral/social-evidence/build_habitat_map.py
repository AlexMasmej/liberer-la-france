import pathlib,json,hashlib,xml.etree.ElementTree as E,collections,re
P=pathlib.Path(__file__).parent;ROOT=P.parent
orig={a['number']:a for a in json.load(open(ROOT/'original-articles.json'))}
# Each mapping is an editorial classification after full reading of the initial article.
D='''55|Quotas, inventaire, prélèvement, rattrapage et bilan PLH|CCH:L302-5,L302-6,L302-7,L302-8,L302-9|CCH:L302-5,L302-6,L302-7,L302-7-1,L302-8,L302-8-1,L302-9,L302-9-1,L302-9-1-1,L302-9-1-2|Quotas déjà traités ; bilan L302-9 confié au parent. L302-9-2 était une habilitation préexistante seulement renumérotée. Carence initialement censurée, recréée par lois postérieures : distinguer.
56|Modification forcée du PLH pour le rattrapage|CCH:L302-4|CCH:L302-4|Proposition quota déjà retire II ; pas d'abrogation du I préexistant.
57|Attribution de compensation liée à la contribution logement|CGI:1609 nonies C|CGI:1609 nonies C|Frontière fiscalité ; ne pas attribuer tout le mécanisme d'attribution de compensation à SRU.
58|Participation des maires d'arrondissement au PLH|CCH:L302-1|CCH:L302-1|Phrase SRU encore identifiable au I, distincte du PLH préexistant et des exigences récentes de densification.
59|Conventions de réservation en contrepartie d'apports locaux|CCH:L441-1|CCH:L441-1|Filiation de la phrase de contrepartie ; règles d'attribution et réservations antérieures/ultérieures à isoler.
60|Représentation EPCI dans conférence logement|CCH:L441-1-4|CCH:L441-1-5|Ancien système des conférences réorganisé ; L441-1-4 actuel concerne les délais DALO. Cible fonctionnelle L441-1-5 à examiner, pas équivalence automatique.
61|Extension du conventionnement APL à catégories de bailleurs|CCH:L351-2|CCH:L831-1|Recodification2019 ; le2° actuel reprend les bailleurs de41ter. Avantage ajouté à examiner sans supprimer toutes les APL.
62|Aides des collectivités aux SEM logement|CGCT:L1523-5,L1523-6|CGCT:L1523-5,L1523-6|Aides, plafonds et conventions propres aux SEM ; validation des conventions anciennes à traiter comme droits acquis.
63|Exception au régime des SEM pour aides logement|CGCT:L1525-3|CGCT:L1525-3|Vigueur et éventuelle abrogation à vérifier dans le CGCT extérieur au corpus, pas supposées.
64|Interventions foncières et compétences habitat EPCI|CGCT:L2254-1,L5216-5,L5214-16,L5215-20|CGCT:L2254-1,L5216-5,L5214-16,L5215-20|Mixte : dispositions modifiées et transition des EPCI existants. Les compétences ont été remaniées depuis2000 ; traiter les seules extensions SRU vérifiées.
65|Collectivités pouvant financer/garantir HLM|CCH:L431-4|CCH:L431-4|Chapeau élargi aux régions/départements/communes/EPCI ; avantage financier, pas simple charge.
66|Organismes bénéficiaires du financement local|CCH:L431-4|CCH:L431-4|Précision de champ parL411-2, même descendant que65 ; une seule future réécriture.
67|Locaux HLM mis à disposition d'associations|CCH:L443-11|CCH:L443-11|Faculté avec paiement éventuel des charges, bénéfice SRU à examiner séparément des ventes HLM préexistantes.
68|Franchise de taxe commerciale en ZUS|LOI1972:3|LOI1972:3|Frontière fiscale ; franchise commerciale, aucun quota. État et montants actuels à vérifier par le rédacteur fiscal.
69|Actions sociales des organismes HLM|CCH:L424-2|CCH:L424-2|Article créé par SRU, faculté sociale non limitée à l'article55.
70|Agrément immobilier et développement logement social|CU:L510-1|CU:L510-1|Frontière urbanisme :1°/2° censurés initialement,3° modificatif exécuté.
71|Associations de locataires dans conférence régionale|CCH:L441-1-6|CCH:L441-1-5|La conférence ancienne a disparu ; L441-1-6 actuel est une convention d'attribution issue de lois ultérieures, pas l'ancien article à abroger au seul numéro.
72|Rétractation acquéreur, versements et engagements unilatéraux|CCH:L271-1,L271-2;CIVIL:1589-1;LOI1989SURENDET:20|CCH:L271-1,L271-2;CIVIL:1589-1|Mixte avec entrée1juin2001 ; protection de rétractation préexistante de1989 élargie par SRU, aujourd'hui10jours par loi ultérieure. Pas d'abolition automatique de toute protection actuelle.
73|Promesse de vente d'un lot à bâtir|CU:L316-3-1|CU:L442-8|Frontière protection acquéreur/urbanisme : recodification du mécanisme, pas tout le droit des lotissements.
74|Interdictions de division et diagnostic de mise en copropriété|CCH:L111-6-1,L111-6-2;LOI1953:1|CCH:L126-17,L126-21,L126-22,L731-1,L731-4|Division recodifiée2020 ; diagnostic de15ans remplacé ALUR par DTG de10ans. L126-18 à20 sont des autorisations issues de lois ultérieures, à ne pas attribuer àSRU. Abrogation1953 ne fait pas renaître sa norme.
75|Budget et comptes de copropriété, syndicat coopératif|COPRO:14-1,14-2,14-3,17,17-1,18|COPRO:14-1,14-3,17-1,18|Ancien14-2 budgettravaux repris en14-1II. Le14-2 actuel est un PPT de2021, pas le texte SRU. Dates de comptes reportées ultérieurement à2007 ; transition autonome épuisée à vérifier.
76|Information sur calcul des quotes-parts et charges|COPRO:10|COPRO:10|Obligation créée dans le règlement pour publications depuis31décembre2002, encore repérable.
77|Compte séparé du syndicat et nullité du mandat|COPRO:18|COPRO:18|Mixte : obligation et transition anciens mandats. Régime remplacé/renforcé par ALUR et2019 ; isoler la filiation, ne pas attribuer tout compte séparé à un état2000 figé.
78|Carnet d'entretien de copropriété|COPRO:18|COPRO:18|Nouvelle obligation de tenue créée par SRU ; décret2001-477 compagnon à inventorier.
79|Communication du carnet et diagnostic à l'acquéreur|COPRO:45-1|CCH:L721-2|45-1 abrogé en2014 ; obligations d'information remplacées par ALUR/L721-2. Entrée1juin2001 épuisée ; ne pas abroger automatiquement la nouvelle règle indépendante.
80|Information notariale sur diagnostic avant copropriété|COPRO:46-1|CCH:L731-4,L721-2|Ancien46-1 abrogé2014. Le46-1 actuel recréé2020 traite la réunion des lots et dissolution, sans filiation avec le diagnostic SRU.
81|Charges, recouvrement, majorités et copropriétés en difficulté|COPRO:10-1,19-2,20,21,25,25-1,24,26,26-3,28,29-1,29-4,29-5,29-6,29,49|COPRO:10-1,19-2,20,21,25,25-1,24,26,26-3,28,29-1,29-8,29|49 abrogé2014. Ancien29-4 division relève désormais29-8 ;29-4/29-5/29-6 actuels ont d'autres fonctions issues d'ALUR. Ventiler les17opérations ; les majorités24/25/26 préexistaient, seuls leurs changements SRU sont attribuables.
82|Portage HLM des copropriétés et plan de sauvegarde|CCH:L421-1,L422-2,L422-3,L615-1,L615-2|CCH:L411-2,L421-1,L422-2,L422-3,L615-1,L615-2|Les compétences ont été réorganisées et élargies ; ne pas supprimer les missions HLM préexistantes. Plan sauvegarde antérieur1996 : extension SRU et durée5ans seulement à isoler.
83|Exonération TFPB en plan de sauvegarde|CGI:1384 A|CGI:1384 A|Avantage fiscal et transmission annuelle. Transition initiale2001 modifiée dèsfin2000 : source actuelle indispensable avant décision.
84|Aides FSL aux copropriétaires occupants|LOI1990:6|LOI1990:6|FSL préexistant ; seule extension charges collectives/emprunts en plan sauvegarde est SRU, avec réécritures ultérieures à vérifier.
85|Exonération de partage et redistribution de copropriété|CGI:749 A|CGI:749 A|Avantage maintenu dans le corpus actuel ; pas rétablissement automatique d'une taxe antérieure par suppression éditoriale.
89|Sociétés d'investissement régional et renouvellement habitat|SRU:89|SRU:89|Disposition autonome mixte habitat/économie ; à partager avec champ financement/urbanisme, y compris bénéfices et subventions.
140|Politique aides, FSL, OPAH et conventionnement|CCH:L301-1,L301-2,L301-4,L303-1,L353-7;LOI1990:6|CCH:L301-1,L301-2,L301-4,L303-1,L353-7;LOI1990:6|Les politiques/aides préexistaient ; isoler chaque rédaction et extension SRU, y compris droits/bénéfices et acceptation de bail sans travaux.
141|Activités d'utilité sociale agréées logement|CCH:L365-1|CCH:L365-1,L365-2,L365-3,L365-4|L365-1 a été remplacé par loi2009, régime d'agréments ventilé. Correspondance fonctionnelle, pas équivalence de toute la législation actuelle.
142|Rapport triennal offre et besoins logement|SRU:142||Article autonome déjà abrogé au14mai2009 selon DILA ; pas de nouvelle abolition à compter comme norme supprimée.
143|Absences et indemnités administrateurs HLM|CCH:L423-13|CCH:L423-13|Création SRU identifiable : charge employeur et indemnités. Examiner droits déjà acquis et réunions antérieures.
144|Location libre et révocable des parkings HLM vacants|CCH:L411-1|CCH:L411-1|Faculté créée en2000, priorité du locataire ; bénéfice à examiner, non obligation de quota.
145|SIEG, actifs sociaux, conventionnement et représentation locale|CCH:L411-2,L411-3,L411-4,L411-5,L411-6,L411-7,L411-8|CCH:L411-2,L411-3,L411-4,L411-6,L411-7,L411-8|L411-5 initial censuré ; L411-5 actuel vient d'une autre loi et n'est pas supprimé automatiquement. SIEG/exonérations modifiés ensuite et contraintes UE à isoler ; droits patrimoniaux acquis distincts.
146|Missions et rattachement des offices publics|CCH:L421-1,L421-2,L421-4|CCH:L421-1,L421-3,L421-4,L421-7|OPAC/OPHLM remplacés par OPH en2007. NumérosL421-2/L421-4 actuels n'ont pas les mêmes fonctions : mapping par clause nécessaire.
147|Affiliation des offices aux centres de gestion|LOI1984:15|CGFP:L452-14|Loi1984 recodifiée ; cible CGFP à vérifier avant rédaction. Règle comprend aussi caisses créditmunicipal, pas uniquement habitat.
148|Carrières des fonctionnaires lors de transformation offices|LOI1984:120|CCH:L421-23;CGFP:statut offices|Transformation historique OPHLM/OPAC dépassée par2007 et recodification2022 : droits acquis et texte statutaire actuel à vérifier, pas retour automatique au régime2000.
149|Compétences HLM, sanctions, liquidation, coopératives|CCH:L422-2,L422-7,L422-8,L422-8-1,L422-3,L422-3-1|CCH:L422-2,L342-14,L422-8,L422-8-1,L422-3,L422-3-1|L422-7 sanctions remplacé par ANCOLS, L422-8/81 subsistent avec renvois modifiés. L422-3 a déjà reçu coupes radicales : partir de la nouvelle baseline enregistrée, jamais de la source ancienne.
150|Sociétés communes de coordination HLM|CCH:L423-1 A|CCH:L423-1-2|AncienL423-1A abrogé2018 ; sociétés coordination ELAN ultérieures à distinguer, ne pas supprimer les nouvelles normes au seul motif de fonction analogue.
151|Mandats de maîtrise d'ouvrage privée HLM|LOI1985MOP:4|CCP:L2422-5|LoiMOP abrogée et recodifiée2019 ; les règles actuelles du mandat de maîtrise d'ouvrage nécessitent preuve de concordance, pas retrait global du mandat.
152|Aménagement et location par coopératives HLM|CCH:L422-3,L422-3-2|CCH:L422-3|AncienL422-3-2 abrogé ; numéro actuel recréé2020 concerne les coopératives d'intérêt collectif, pas l'ancienne norme abrogée. Facultés nouvelles SRU à isoler.
153|Conférences logement et commissions d'attribution|CCH:L441-1-4,L441-1-5,L441-2|CCH:L441-1-5,L441-2|Conférence communale francilienne à20% supprimée/réorganisée ; les commissions et conférences actuelles viennent de plusieurs lois. Pas d'abrogation du délai DALO actuelL441-1-4.
154|Sous-location sociale et saisonnière|CCH:L442-8-1,L442-8-2,L353-19-2|CCH:L442-8-1,L442-8-2,L353-19-2|Facultés pour associations/CCAS/personnes vulnérables/saisonniers et bénéfice APL ; mécanismes modifiés depuis2000, droits contractuels acquis à réserver.
155|Mandats de gérance HLM et SEM/collectivités|CCH:L442-9|CCH:L442-9|Faculté et délégations ajoutées par SRU, conditions et autorisations réformées ensuite à isoler.
156|Exclusion gérance sociale du régime DSP|LOI1993SAPIN:41|CCP:L3211-1|Ancienne dérogation recodifiée/supprimée avec ordonnances2016/2018 : texte actuel et régime inhouse à vérifier avant toute assimilation.
157|Versement APL au mandataire de gérance|CCH:L351-9|CCH:L832-1|Phrase identifiable dansL832-1 après recodification2019, faculté de versement au mandataire, pas toutes les APL.
158|Commission attribution en mandat de gérance|CCH:L441-2|CCH:L441-2|Membre de droit de la commission du gérant pour les logements confiés, clause créée SRU à isoler.
159|Location-accession et SCI de location HLM|CCH:L443-7,L443-7-1|CCH:L443-7,L443-6-2|Faculté locationaccession subsiste ; ancienL443-7-1 abrogé/replacé par accession progressive2006. L443-6-2 est un descendant fonctionnel ultérieur, pas la règle2000 entière.
160|Plafonds ressources des acquéreurs HLM|CCH:L443-11|CCH:L443-11|Substitution de l'autorité fixant les plafonds ; pas toute la vente HLM préexistante.
161|Hypothèques de prêts logement social|CCH:L431-1|CCH:L431-1|Deux phrases SRU encore identifiables. Retirer la faculté nouvelle CDC ne doit pas rétablir le droit antérieur du fonds de garantie ni effacer sûretés acquises.
162|Contrôle administratif du logement social|CCH:L451-1,L451-2,L451-2-1,L441-2-1|CCH:L342-2,L342-5,L342-8,L342-9,L342-10,L342-12,L342-14,L441-2-1|Ancien contrôle MIILOS remplacé par ANCOLS en2015 ; l'origine SRU ne suffit pas à abolir les nouvelles compétences/garanties ANCOLS. Correspondances par mission à vérifier.
163|CGLLS, cotisations et droits transférés|CCH:L452-1,L452-2,L452-3,L452-4,L452-5,L452-6,L452-7,L451-3,L451-4|CCH:L452-1,L452-2,L452-3,L452-4,L452-5,L452-6,L452-7|Création/réorganisation2000 avec transition institutionnelle2001 ; nombreuses missions/cotisations ultérieures. Ne pas restaurer anciens articles abrogés ni effacer garanties/prêts acquis.
164|Garantie accession sociale et comptabilité séparée|CCH:L453-1,L453-2,L453-3,L222-2,L222-6,L422-3|CCH:L453-1,L453-2,L453-3,L222-2,L222-6,L422-3|Création de garantie et comptabilitédistincte ; VEFA/contratspromotion avaient des garanties antérieures, isoler extension HLM. Entrée initiale2002 reportée2003.
165|Contrôles et cotisation des SEM outre-mer|CCH:L472-1-2,L472-1-5|CCH:L472-1-2,L472-1-5|L472-1-5 crééSRU toujours identifiable, contrôles renumérotés et cotisations remaniées à coordonner.
166|Cotisation, contrôle et comptabilité SEM|CCH:L481-1-1|CCH:L481-2,L481-8,L452-4,L342-2|L481-1-1 actuel concerne agrément de petits bailleurs, fonction différente de celui créé2000. Contrôle/cotisation/comptes ventilés ultérieurement.
167|Suppression taxe droitbail, plafond SLS et anciennes caisses|CGI:302 bis ZC;CCH:L441-3,L451-3,L451-4,L481-1,L481-2|CCH:L441-3|Dispositions abrogatives exécutées sans résurrection. Plafond40→60% remanié ensuite ; lesL481-1/2 actuels ont été recréés, ne pas les abroger automatiquement.
168|Insalubrité et commission hygiène|CSP:L1331-26,L1416-2|CCH:L511-1,L511-2,L511-3,L511-4,L511-5,L511-6,L511-7,L511-8,L511-9,L511-10|Police2000 remplacée par ordonnance2020-1144, commissions hygiène remplacées. Correspondance fonctionnelle, normes2020 indépendantes à isoler ; transition institutionnelle ancienne épuisée.
169|Contradictoire en insalubrité|CSP:L1331-27|CCH:L511-10,L511-11,L511-12|Ancien article abrogé avec réforme2020 ; procédure actuelle nouvelle, pas simple renumérotation à retrancher sans lecture.
170|Suppression d'un alinéa santé publique|CSP:L1331-32||Abrogation exécutée ; aucune restauration automatique de l'ancien alinéa, ni obligation autonome restant dans SRU170.
171|Mesures insalubrité, travaux/interdiction/démolition|CSP:L1331-28|CCH:L511-11,L511-12,L511-13,L511-14,L511-15|Régime réécrit2020 ; filiation fonctionnelle seulement, obligations antérieures à2000 à ne pas abolir globalement.
172|Publicité, baux et mainlevée d'insalubrité|CSP:L1331-28-1,L1331-28-2,L1331-28-3|CCH:L511-12,L511-14,L511-16,L521-2|Anciennes procédures abrogées2020 ; garanties et droits acquis des occupants à séparer de la police nouvelle.
173|Exécution d'office et sanction d'interdiction|CSP:L1331-29,L1336-2|CCH:L511-15,L511-22|Régime et incriminations remplacés ; loi pénale plus douce à réserver si nouvelle suppression après partition.
174|Hypothèque des frais d'office et relogement|CSP:L1331-30|CCH:L511-15,L541-1,L541-2,L541-3|Ancienne sûreté réorganisée avec privilèges2007/2020 ; cette liste est une piste fonctionnelle à contrôler, pas concordance certifiée.
175|Relogement/hébergement insalubrité|CSP:L1331-31|CCH:L521-1,L521-3-1,L521-3-2|Ancienne clause remplacée ; descendant de protectionlocative à examiner avec SRU181 et dispositifs postérieurs.
176|État amiante lors des ventes|CSP:L1334-7|CCH:L271-4;CSP:L1334-13|Ancien numéroL1334-7 a changé de fonction ; étatamiante recodifié et règles postérieures à isoler. Ne pas supprimer un diagnostic sur un autre sujet au même numéro.
177|Abrogations santé et sanctions antiéviction|CSP:L1331-17,L1331-18,L1331-19,L1331-20,L1331-21,L1331-22,L1331-23,L1336-3,L1336-4|CCH:L511-22|Abrogations exécutées sans renaissance ; sanctions2000 remplacées par polices/incriminations ultérieures. Aucune assimilation au seul numéro actuel.
178|Travaux d'office hôtels/ERP hébergement|CCH:L123-3|CCH:L184-1,L184-2,L184-3,L184-4,L184-5,L184-6,L184-7,L184-8,L184-9|Recodification2020 mais renforcements ultérieurs ; isoler pouvoir d'office2000 et obligations préexistantes de sécurité.
179|Péril, publicité, travaux, sûretés et sanctions|CCH:L511-1-1,L511-2,L511-3,L511-4,L511-5,L511-6|CCH:L511-1,L511-2,L511-3,L511-4,L511-5,L511-6,L511-7,L511-8,L511-9,L511-10,L511-11,L511-12,L511-13,L511-14,L511-15,L511-16,L511-17,L511-18,L511-19,L511-20,L511-21,L511-22|Même numérotation partielle mais régime unifié2020 différent. Ne pas abolir la police du péril qui préexistait àSRU ; seulement effetsSRU encore identifiés après audit.
180|Démolition HLM et maintien dans les lieux|CCH:L442-6,L353-15|CCH:L442-6,L353-15|Faculté bailleur et relogement ajoutés2000, remplacés notamment par règle des trois offres et conventionsANRU ultérieures. Les protections peuvent avoir plusieurs origines.
181|Droits occupants, loyers, hébergement et relogement|CCH:L521-1,L521-2,L521-3,L521-4|CCH:L521-1,L521-2,L521-3-1,L521-3-2,L521-3-3,L521-3-4,L521-4|Nouvelles protections créées/renforcéesSRU, élargies ensuite. Examiner dans allSRU, sans effacer droits déjà nés ni attribuer tous les ajouts2005–2024 à2000.
182|Reprise APL/AL sans carence après insalubrité|CCH:L351-3-1;CSS:L542-2,L831-4-1|CCH:L823-5,R823-10|Anciens articles supprimés/recodifiés2019 ; règle actuelle de réouverture à retrouver dans le réglementaire. R823-10 est une piste à vérifier avant rédaction, pas certitude.
183|Occupants protégés lors d'aménagement|CU:L314-1|CU:L314-1|Frontière droitsdesoccupants/urbanisme ; englobe bauxprofessionnelscommerciauxruraux, pas uniquement SRUquota.
184|Cession de biens expropriés en sauvegarde/restauration|EXPRO:L21-1|EXPRO:L411-1|Ancien code remplacé2014 ; liste actuelle de cessions de gréàgré doit être vérifiée dans le code extérieur avant abrogation.
185|Missions et sanctions Anah|CCH:L321-1,L321-2,L322-1,L322-2,L322-3|CCH:L321-1,L321-2|Agence antérieure1971 : les seules extensionsetmodificationsSRU sont attribuables, pas l'ensemble de l'agence et de ses aides. AbrogationsL322 ne font rien renaître.
186|Réhabilitation immobilier de loisir|CU:L318-5;CGI:261 D|CU:L318-5;CGI:261 D|Frontière habitat touristique/urbanisme/fiscalité ; bénéficesetconditions des ORIL à examiner, pas le droitcommun des locations saisonnières.
187|Décence, actions locataires et allocations logement|CIVIL:1719;BAIL:2,6,20-1,24-1,41-1;CSS:L542-2,L542-6,L553-4,L831-3,L831-7,L835-2|CIVIL:1719;BAIL:2,6,20-1,24-1,41-1;CCH:L822-9,L832-1,L842-1,L843-1,L843-2,L843-3|Décence/recours créésSRU à examiner ; critèresénergétiques2015–2021 indépendants, actions et loyers ont évolué. Décret2002-120 et conditions d'aides recodifiées2019 doivent figurer dans chaîne.
188|Conciliation et résiliation pour dette locative|BAIL:20,24,40|BAIL:20,24,40|Extension des compétences de conciliation et notifications, règles modifiées depuis. Les procédures de dette et expulsions préexistaient ; pas leur suppressionglobale.
189|Opposabilité notifications conjoint/PACS non signalé|BAIL:9-1|BAIL:9-1|RègleSRU encore identifiable ; droitsdesdestinataires et notifications déjà accomplies à réserver.
190|Congévente et Carrez, validation anciens congés|BAIL:15;SRU:190|BAIL:15;SRU:190|I modificatif ; II validation autonome d'actes anciens sous réserve décisionspasséesenforcedechosejugée. Abrogationprospective ne doit pas rouvrirautomatiquement lesancienslitiges.
191|Établissement public immobilier minier NordPasdeCalais|SRU:191|SRU:191|Dispositionautonome encoreen vigueurau dernierfondsDILA, modifiée2006/2015. Structure, garanties, fiscalité et droitsstatutairesminiers à examiner avec transitioninstitutionnelle ; pas disparitiondesactifs/dettesparsimplephrase.
192|DSU et parcminier Epinorpa|CGCT:L2334-17|CGCT:L2334-17|Extensiondécompte DSU distinctequota, actuelle à vérifierhorscorpus avantretrait.
193|Accords et concertation locative|LOI1986:42,44,44 bis,44 ter,44 quater|LOI1986:42,44,44 bis,44 ter,44 quater|Plans/conseils/consultations et moyens créésSRU, associations et accordsontévolué. Ne pas lesprésumer maintenus parcequ'horsquota ; droitscontractuelsacquis séparés.
194|Logementsfoyers, contratécrit et concertation|CCH:L633-1,L633-2,L633-3,L633-4,L633-5|CCH:L633-1,L633-2,L633-4,L633-5|L633-3 initialestseulementtransitiondescontrats, remplacéen2016parrègledifférente. Contrat, durée,résiliation,concertationetexclusionsontétéremaniés ; protectionscrééesen2000danslechamplarge.
195|Représentation locataires au CA des SEM|CCH:L481-5|CCH:L481-6|Transfert parloi2006 versL481-6, droitsdevote renforcésensuite. L481-5 actuelestunautrerenvoi, ne pasleconfondreaveccréation2000.
196|Offrepréemption locataire dans ventesdivisées|LOI1975:10|LOI1975:10|La règle de préemption existait ; SRU a rédigé la phrase notificationvalantoffre. Aucunretourpré2000automatique ; texteactuelhorscorpusàvérifier.
197|Catégories bailleurs et accords collectifs|LOI1986:41 ter|LOI1986:41 ter|Deuxcatégoriesréécrites parSRU ; typologiebailleurs etrenvoiscascadesàventiler, pasabrogationentièrede41terpréexistant.
198|Reconductioncourteterme avant ventepardécoupe|BAIL:11-1|BAIL:11-1|ArticlecrééSRU, seuil>10devenu>5parloiultérieure ; facultéetprotection àexaminer, aucuneabrogationrédigéeici.
199|Dissociation congé et offre d'achat en ventepardécoupe|BAIL:15|BAIL:15|PhraseSRU liée11-1 ; coordinationnécessaireavec198et196.
200|Bilanbiennal contingent préfectoral|SRU:200|SRU:200|Obligationautonome encoreenvigueuraufondsDILA, bénéficiairedevenucomitérégionalen2004. Cibleindépendantedel'article55 maisdansallSRU.
201|ADIL et information gratuite|CCH:L366-1|CCH:L366-1|CadrelégislatifcrééSRU maisassociations antérieures ; examinerhabilitationconventions/missions sanssupposersuppriméstousorganismespréexistants.
208|Abrogation disposition loi orientationville|LOI1991VILLE:4||Frontièreurbanisme/logement : abrogationexécutée, ne pasfaire renaîtrearticle4 parsimpleabrogationSRU208.'''
manual={}
for line in D.splitlines():
 n,topic,old,new,note=line.split('|');manual[n]=(topic,old,new,note)
# Load official extracted laws and current five-code public inventory.
def parse_files(d):
 out=collections.defaultdict(list)
 for f in d.glob('LEGIARTI*.xml'):
  raw=f.read_bytes();r=E.fromstring(raw);m=r.find('META/META_SPEC/META_ARTICLE')
  if m is None:continue
  num=m.findtext('NUM','');body=r.find('BLOC_TEXTUEL/CONTENU')
  out[num].append({'number':num,'source_id':r.findtext('META/META_COMMUN/ID') or f.stem,'state':m.findtext('ETAT',''),'valid_from':m.findtext('DATE_DEBUT',''),'valid_until':m.findtext('DATE_FIN',''),'source_path':str(f),'source_sha256':hashlib.sha256(raw).hexdigest(),'text':''.join(body.itertext()) if body is not None else ''})
 return out
catalog={};catalog['SRU']=parse_files(P/'JORFTEXT000000207538');catalog['BAIL']=parse_files(P/'JORFTEXT000000509310');catalog['COPRO']=parse_files(P/'JORFTEXT000000880200');catalog['CIVIL']=parse_files(P/'LEGITEXT000006070721')
public={}
for label,slug in [('CCH','construction-habitation'),('CGI','impots'),('CSS','securite-sociale'),('CU','urbanisme')]:
 path=pathlib.Path('sites/liberer-la-retraite/dist/corpus')/(slug+'.json')
 if path.exists():
  public[label]={a['number']:a for a in json.load(open(path))}
def split(spec):
 out=[]
 for group in spec.split(';'):
  if not group:continue
  text,nums=group.split(':',1)
  for num in nums.split(','):out.append((text,num))
 return out
def current(text,num):
 if text in public and num in public[text]:
  a=public[text][num];return {'text':text,'number':num,'source_id':a['source_id'],'code_id':a['code_id'],'state':a['source_state'],'valid_from':a['valid_from'],'valid_until':a['valid_until'],'source_sha256':a['source_sha256'],'source_url':a['source_url'],'evidence':'canonical_public_inventory_2026_10_18','current_slot_verified':True,'normative_filiation_not_implied_by_number':True}
 if text in catalog and num in catalog[text]:
  versions=catalog[text][num];active=[v for v in versions if v['valid_from']<='2026-10-19'<v['valid_until'] and v['state'] not in ['ABROGE','TRANSFERE','MODIFIE']]
  a=max(active or versions,key=lambda a:a['valid_from']);return {k:v for k,v in a.items() if k!='text'}|{'text':text,'source_url':'https://www.legifrance.gouv.fr/loda/article_lc/'+a['source_id']+'/','current_slot_verified':bool(active),'evidence':'DILA_extraction_with_2025_2026_updates_when_complete','normative_filiation_not_implied_by_number':True}
 return {'text':text,'number':num,'current_slot_verified':False,'evidence':'Original official act identifies target; current consolidation/correspondence still requires verification before drafting','source_url':orig[next(n for n,v in manual.items() if text+':'+num in v[1] or text+':'+num in v[2])]['source_url'] if False else None}
rows=[]
for n in sorted(manual,key=int):
 topic,old,new,note=manual[n];a=orig[n];vs=catalog['SRU'].get(n,[]);active=[v for v in vs if v['valid_from']<='2026-10-19'<v['valid_until'] and v['state'] not in ['ABROGE','TRANSFERE','MODIFIE']];lawv=max(active or vs,key=lambda a:a['valid_from']) if vs else None
 status='modificatif_exécute_effets_dans_textes_cibles'
 if n in ['64','72','75','77','79','83','163','164','168','190']:status='mixte_modificatif_et_transition_ou_validation_autonome'
 if n in ['89','191','200']:status='autonome_normatif_a_traiter'
 if n=='142':status='autonome_deja_abroge'
 if n in ['170','208']:status='abrogatif_execute_sans_restauration'
 if n=='70':status='partiellement_censure_et_modificatif'
 scope='habitat_social_CCH_baux_copropriete_protections'
 if n in ['57','68','70','73','83','85','89','183','184','186','208']:scope='frontiere_a_partager_avec_fiscalite_urbanisme_expropriation'
 rows.append({'sru_article':n,'topic':topic,'scope':scope,'initial_operation_class':status,'initial_source':{k:a[k] for k in ['source_url','version','first_page_line','last_page_line']}|{'path':str(ROOT/'original-articles.json'),'article_text_sha256':hashlib.sha256(a['text'].encode()).hexdigest(),'article_fully_read':True},'consolidated_SRU_status_evidence':({k:v for k,v in lawv.items() if k!='text'} if lawv else None),'original_targets':[{'text':t,'number':q} for t,q in split(old)],'current_review_targets':[current(t,q) for t,q in split(new)],'filiation_decision_notes':note,'drafting_decision':'No new candidate yet in this inventory; isolate surviving SRU-created clause, acquired rights and independent later law before proposing removal.','automatic_restoration_of_pre2000_law':False})
updates=P/'dila-updates.json';finished=updates.exists()
summary={'title':'Cartographie de la loiSRU2000 : logement/CCH, baux, copropriété, protections des occupants','mode':'read_only_normative_sources; inventory_only_no_proposal','as_of':'2026-10-19','initial_articles_examined':len(rows),'scope_included':'55–85,89,140–201,208 ; entrées frontières explicitement séparées','source_initial':'Official JORF original-articles.json recovered by parent; all selected articles read in full','DILA_updates_complete':finished,'coverage_warning':'Current-slot identity is not proof that the entire current article was created by SRU. Some external-code targets are provisional and explicitly flagged. No blanket repeal or restoration is inferred.','articles':rows}
(ROOT/'habitat-inventory.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
exact=[]
for row in rows:
 for a in row['current_review_targets']:
  if a.get('current_slot_verified') and a.get('state')=='VIGUEUR':exact.append((a['text'],a['number'],a['source_id']))
(ROOT/'habitat-current-targets.json').write_text(json.dumps({'status':'Review queue, not authorization to repeal each entire article','targets':[{'text':t,'number':n,'source_id':i} for t,n,i in sorted(set(exact))]},ensure_ascii=False,indent=2)+'\n')
print('inventory',len(rows),'original articles;',len(set(exact)),'verified current review slots; updates complete',finished)
