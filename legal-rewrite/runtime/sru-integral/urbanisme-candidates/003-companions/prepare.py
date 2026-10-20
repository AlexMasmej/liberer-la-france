import json,sqlite3,hashlib,sys,html,zlib,xml.etree.ElementTree as E
from pathlib import Path
sys.path.insert(0,'legal-rewrite')
from run_exhaustive import validate_answer
P=Path(__file__).parent;EV=P.parents[1]/'urbanisme-evidence'
db=sqlite3.connect('file:'+str(EV/'external-evidence.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
count=db.execute('select count(*) from archives where complete=1').fetchone()[0]
if count!=467:raise SystemExit('Wait for all 467 official archives, currently '+str(count))
sources=[]
def inner(el):return '' if el is None else (el.text or '')+''.join(E.tostring(x,encoding='unicode') for x in el)
for n in ['L341-16','R122-17']:
 rs=db.execute("select * from documents where code_id=? and kind='ARTICLE' and number=? and start<=? and end>? and state!='ABROGE'",('LEGITEXT000006074220',n,'2026-10-19','2026-10-19')).fetchall()
 if len(rs)!=1:raise ValueError('Ambiguous current source '+n)
 a=dict(rs[0]);raw=zlib.decompress(a.pop('xml_zlib'));r=E.fromstring(raw)
 if hashlib.sha256(raw).hexdigest()!=a['sha256']:raise ValueError('XML SHA mismatch')
 target=P/(a['id']+'.xml');target.write_bytes(raw)
 a.update(source_id=a.pop('id'),source_sha256=a.pop('sha256'),source_xml=inner(r.find('./BLOC_TEXTUEL/CONTENU')),source_notes_xml=inner(r.find('./NOTA/CONTENU')),source_document_xml=raw.decode(),previous_draft=None,previous_proposed_sha256=None,source_document_path=str(target),source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+target.stem,archive_provenance=dict(db.execute('select * from archives where name=?',(a['archive'],)).fetchone()))
 sources.append(a)
def atomic(n,obj):
 p=P/n;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');t.replace(p)
atomic('source.json',sources)
rows=[]
def add(n,ps,reason,notes,removed):
 s=next(a for a in sources if a['number']==n);r={k:s[k] for k in ['code_id','source_id','source_sha256','number']};r.update(proposed_xml='\n'.join('<p>'+html.escape(p,quote=False)+'</p>' for p in ps),reason=reason,review_notes=notes,status='rewrite_draft',change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=[removed]);rows.append(r)
add('L341-16',[
 "Dans chaque département siège une commission compétente en matière de nature, de paysages et de sites.",
 "Le représentant de l'État dans le département préside cette commission. Pour les interventions prévues aux articles L. 111-9, L. 121-10, L. 121-12, L. 121-27, L. 121-39, L. 121-41, L. 122-7, L. 122-11, L. 122-14 et L. 122-21 du code de l'urbanisme, sa formation réunit des représentants de l'État, des représentants élus des collectivités territoriales et des établissements publics de coopération intercommunale, ainsi que des personnalités qualifiées en sciences de la nature ou en protection des sites ou du cadre de vie.",
 "En Corse, le conseil des sites de Corse prévu à l'article L. 4421-4 du code général des collectivités territoriales exerce les attributions dévolues à la commission des sites, perspectives et paysages.",
 "La suppression du renvoi à l'article L. 121-29 du code de l'urbanisme prend effet en même temps que l'abrogation du schéma d'aménagement de plage prévu aux articles L. 121-28 à L. 121-30 de ce code. Aucun nouvel avis ne peut être exigé au seul titre de ce schéma supprimé. Les avis régulièrement rendus avant cette date ne sont pas rétroactivement annulés et n'autorisent pas la poursuite d'une procédure d'approbation supprimée. Les autres attributions de la commission, ainsi que les autorisations et prescriptions antérieures préservées par l'article L. 121-30, ne sont pas remises en cause."
],"Retirer de la formation spécialisée de la commission le seul renvoi au schéma de plage SRU abrogé ; conserver la commission, toutes ses autres compétences, sa présidence et le régime corse.","Source DILA actuelle LEGIARTI000033746363, intégralement lue avec sa note non vide : loi 2016-1888 article 71 et décret 2017-1039 article 10, entrée le premier jour du troisième mois suivant publication du décret. Cette note porte sur des attributions montagne autonomes, qui demeurent maintenues ; aucun effet rétroactif nouveau. Source XML originale et provenance archive/SHA incluses. Consolidation documentaire sur le stock officiel DILA du 13 juillet 2025 et 466 mises à jour jusqu'au 18 octobre 2026 ; aucun candidat antérieur dans la base canonique des cinq codes, cet article étant extérieur au corpus. Article initial SRU42 et concordances de L146-6-1 vers L121-28/29/30 vérifiés dans le lot003. La commission préexistante n'est pas un organisme créé par SRU ; son abolition serait hors décision de coordination. Les dix autres renvois urbanisme et L4421-4 CGCT sont intégralement maintenus. Le renvoi L111-9 n'est pas supprimé sur la seule similitude avec SRU12, dont la filiation de fond nécessite une décision distincte après la substitution législative de 2005. Aucun enregistrement ni publication. Pas de validation juridique revendiquée.","Suppression de la seule attribution de formation spécialisée liée à l'avis sur les schémas de plage de L121-29, sans supprimer la commission ni ses autres attributions autonomes.")
add('R122-17',[
 "I. – Les plans et programmes énumérés ci-après sont soumis à une évaluation environnementale :",
 "1° Les programmes opérationnels élaborés par les autorités de gestion établies pour le Fonds européen de développement régional, le Fonds européen agricole et de développement rural et le Fonds de l'Union européenne pour les affaires maritimes et la pêche. Sont exclus, pour le Fonds européen de développement régional, les programmes opérationnels de coopération territoriale européenne ne relevant pas du II de l'article L. 122-4 du présent code ;",
 "2° Le schéma décennal de développement du réseau de l'article L. 321-6 du code de l'énergie ;",
 "3° Le schéma régional de raccordement au réseau des énergies renouvelables de l'article L. 321-7 du code de l'énergie ;",
 "4° Le schéma directeur d'aménagement et de gestion des eaux des articles L. 212-1 et L. 212-2 du code de l'environnement ;",
 "5° Le schéma d'aménagement et de gestion des eaux des articles L. 212-3 à L. 212-6 du code de l'environnement ;",
 "6° Le document stratégique de façade de l'article L. 219-3, y compris le chapitre consacré au plan d'action pour le milieu marin ;",
 "7° Le document stratégique de bassin maritime des articles L. 219-3 et L. 219-6 ;",
 "8° La programmation pluriannuelle de l'énergie des articles L. 141-1 et L. 141-5 du code de l'énergie ;",
 "8° bis La stratégie nationale de mobilisation de la biomasse de l'article L. 211-8 du code de l'énergie ;",
 "8° ter Le schéma régional de biomasse de l'article L. 222-3-1 du code de l'environnement ;",
 "9° Le schéma régional du climat, de l'air et de l'énergie de l'article L. 222-1 du code de l'environnement ;",
 "9° bis La stratégie nationale bas carbone de l'article L. 222-1 B ;",
 "10° Le plan climat air énergie territorial de l'article R. 229-51 du code de l'environnement ;",
 "11° La charte de parc naturel régional du II de l'article L. 333-1 du code de l'environnement ;",
 "12° La charte de parc national de l'article L. 331-3 du code de l'environnement ;",
 "13° Le plan départemental des itinéraires de randonnée motorisée de l'article L. 361-2 du code de l'environnement ;",
 "14° Les orientations nationales pour la préservation et la remise en bon état des continuités écologiques de l'article L. 371-2 du code de l'environnement ;",
 "15° Le schéma régional de cohérence écologique de l'article L. 371-3 du code de l'environnement ;",
 "16° Les plans, schémas, programmes et autres documents de planification soumis à une évaluation des incidences Natura 2000 au titre de l'article L. 414-4 du code de l'environnement, à l'exception de ceux visés au VI de l'article L. 122-4 du même code ;",
 "17° Le schéma de l'article L. 515-3 du code de l'environnement ;",
 "18° Le plan national de prévention des déchets de l'article L. 541-11 du code de l'environnement ;",
 "19° Le plan national de prévention et de gestion de certaines catégories de déchets de l'article L. 541-11-1 du code de l'environnement ;",
 "20° Le plan régional de prévention et de gestion des déchets de l'article L. 541-13 du code de l'environnement ;",
 "21° Le plan national de gestion des matières et déchets radioactifs de l'article L. 542-1-2 du code de l'environnement ;",
 "22° Le plan de gestion des risques d'inondation de l'article L. 566-7 du code de l'environnement ;",
 "22° bis Les programmes d'actions de prévention des inondations ;",
 "23° Le programme d'actions national pour la protection des eaux contre la pollution par les nitrates d'origine agricole du IV de l'article R. 211-80 du code de l'environnement ;",
 "24° Le programme d'actions régional pour la protection des eaux contre la pollution par les nitrates d'origine agricole du IV de l'article R. 211-80 du code de l'environnement ;",
 "25° Le programme national de la forêt et du bois de l'article L. 121-2-2 du code forestier ;",
 "26° Le programme régional de la forêt et du bois de l'article L. 122-1 du code forestier et, en Guyane, le schéma pluriannuel de desserte forestière ;",
 "27° Les directives d'aménagement du 1° de l'article L. 122-2 du code forestier ;",
 "28° Le schéma régional du 2° de l'article L. 122-2 du code forestier ;",
 "29° Le schéma régional de gestion sylvicole du 3° de l'article L. 122-2 du code forestier ;",
 "30° Le schéma départemental d'orientation minière de l'article L. 621-1 du code minier ;",
 "31° Les 4° et 5° du projet stratégique des grands ports maritimes prévus à l'article R. 5312-63 du code des transports ;",
 "32° La réglementation des boisements de l'article L. 126-1 du code rural et de la pêche maritime ;",
 "33° Le schéma régional de développement de l'aquaculture marine de l'article L. 923-1-1 du code rural et de la pêche maritime ;",
 "34° Le schéma national des infrastructures de transport de l'article L. 1212-1 du code des transports ;",
 "35° Le schéma régional des infrastructures de transport de l'article L. 1213-1 du code des transports ;",
 "36° Le plan de mobilité des articles L. 1214-1 et L. 1214-9 du code des transports ;",
 "37° Le contrat de plan État-région de l'article 11 de la loi n° 82-653 du 29 juillet 1982 portant réforme de la planification ;",
 "38° Le schéma régional d'aménagement, de développement durable et d'égalité des territoires de l'article L. 4251-1 du code général des collectivités territoriales ;",
 "39° Le schéma de mise en valeur de la mer élaboré selon les modalités de l'article 57 de la loi n° 83-8 du 7 janvier 1983 relative à la répartition des compétences entre les communes, les départements et les régions ;",
 "40° Le schéma d'ensemble du réseau de transport public du Grand Paris et les contrats de développement territorial des articles 2, 3 et 21 de la loi n° 2010-597 du 3 juin 2010 relative au Grand Paris ;",
 "41° Le schéma des structures des exploitations de cultures marines de l'article D. 923-6 du code rural et de la pêche maritime ;",
 "42° Le schéma directeur territorial d'aménagement numérique de l'article L. 1425-2 du code général des collectivités territoriales ;",
 "43° La directive territoriale d'aménagement et de développement durable de l'article L. 102-4 du code de l'urbanisme ;",
 "43° bis La directive territoriale d'aménagement de l'article L. 172-1 du code de l'urbanisme ;",
 "44° Le schéma directeur de la région d'Ile-de-France de l'article L. 123-1 du code de l'urbanisme ;",
 "45° Le schéma d'aménagement régional de l'article L. 4433-7 du code général des collectivités territoriales ;",
 "46° Le plan d'aménagement et de développement durable de Corse de l'article L. 4424-9 du code général des collectivités territoriales ;",
 "47° Le schéma de cohérence territoriale ;",
 "48° Le plan local d'urbanisme ;",
 "49° Les prescriptions particulières de massif de l'article L. 122-24 du code de l'urbanisme ;",
 "49° bis Les unités touristiques nouvelles structurantes du second alinéa de l'article L. 122-20 du code de l'urbanisme mentionnées à l'article R. 104-17-1 et aux a et c du 1° de l'article R. 104-17-2 de ce code ;",
 "49° ter Les unités touristiques nouvelles locales du second alinéa de l'article L. 122-21 du code de l'urbanisme permettant la réalisation de travaux, aménagements, ouvrages ou installations susceptibles d'affecter de manière significative un site Natura 2000 ;",
 "50° Abrogé ;",
 "51° La carte communale permettant la réalisation de travaux, aménagements, ouvrages ou installations susceptibles d'affecter de manière significative un site Natura 2000 ;",
 "52° Le schéma territorial d'aménagement et d'urbanisme prévu par le code local de l'urbanisme de la collectivité de Saint-Pierre-et-Miquelon ;",
 "53° Les plans d'exposition au bruit de l'article L. 112-6 du code de l'urbanisme pour les aérodromes des catégories A et B de l'article R. 222-5 du code de l'aviation civile.",
 "II. – Les plans et programmes suivants relèvent d'un examen au cas par cas pouvant conduire à une évaluation environnementale :",
 "1° La directive de protection et de mise en valeur des paysages de l'article L. 350-1 du code de l'environnement ;",
 "2° Abrogé ;",
 "3° La stratégie locale de développement forestier de l'article L. 123-1 du code forestier ;",
 "4° Les zones des 1° à 4° de l'article L. 2224-10 du code général des collectivités territoriales ;",
 "5° Abrogé ;",
 "6° La zone spéciale de carrière de l'article L. 321-1 du code minier ;",
 "7° La zone d'exploitation coordonnée des carrières de l'article L. 334-1 du code minier ;",
 "8° Le plan de sauvegarde et de mise en valeur de l'article L. 631-3 du code du patrimoine ;",
 "8 bis Le plan de valorisation de l'architecture et du patrimoine de l'article L. 631-4 du code du patrimoine ;",
 "9° Le plan local de mobilité de l'article L. 1214-30 du code des transports ;",
 "10° Le plan de sauvegarde et de mise en valeur de l'article L. 313-1 du code de l'urbanisme ;",
 "11° Les plans d'exposition au bruit de l'article L. 112-6 du code de l'urbanisme qui ne relèvent pas du I ;",
 "12° La carte communale qui ne relève pas du I du présent article ;",
 "12° bis Les unités touristiques nouvelles structurantes du second alinéa de l'article L. 122-20 du code de l'urbanisme qui ne relèvent pas du I du présent article ;",
 "12° ter Les unités touristiques nouvelles locales du second alinéa de l'article L. 122-21 du code de l'urbanisme qui ne relèvent pas du I du présent article ;",
 "13° Le plan de protection de l'atmosphère de l'article L. 222-4 du code de l'environnement ;",
 "14° Les programmes opérationnels de coopération territoriale européenne mentionnés au 1° du I qui remplissent les critères du III de l'article L. 122-4 du présent code ;",
 "15° Les avenants à la convention passée entre l'État et la Compagnie nationale du Rhône au titre de la concession prévue par la loi du 27 mai 1921 approuvant le programme des travaux d'aménagement du Rhône, de la frontière suisse à la mer, au triple point de vue des forces motrices, de la navigation et des irrigations et autres utilisations agricoles, et créant les ressources financières correspondantes.",
 "III. – Pour un plan ou programme relevant du II ou du III de l'article L. 122-4 et absent des listes du présent article, le ministre chargé de l'environnement procède à un examen, de sa propre initiative ou à la demande de l'autorité responsable de son élaboration. Cet examen détermine si, en application du IV de l'article L. 122-4, il relève de l'évaluation environnementale systématique ou d'un examen au cas par cas.",
 "L'arrêté ministériel qui le soumet à une évaluation systématique ou à un examen au cas par cas est publié au Journal officiel de la République française et mis en ligne sur le site internet du ministère chargé de l'environnement.",
 "Cet arrêté cesse de produire ses effets au plus tard un an après son entrée en vigueur, ou dès l'entrée en vigueur de la révision des listes des I et II si celle-ci intervient auparavant.",
 "IV. – L'autorité environnementale compétente pour les plans et programmes soumis à évaluation en vertu des I, II ou III est :",
 "1° La formation d'autorité environnementale de l'inspection générale de l'environnement et du développement durable lorsque le périmètre du plan ou programme dépasse une région ou qu'il donne lieu à approbation par décret ou décision ministérielle, à l'exception des plans et programmes du 53° du I et du 11° du II. Cette formation est également compétente pour ceux mentionnés aux 1°, 4°, 8°, 8° ter, 9°, 11°, 15°, 17°, 22°, 24°, 30°, 37° et 38° du I et au 13° du II ;",
 "2° La mission régionale d'autorité environnementale de cette inspection générale pour les autres plans et programmes des I et II.",
 "La formation d'autorité environnementale de l'inspection générale peut, de sa propre initiative, exercer une compétence dévolue à une mission régionale d'autorité environnementale. La mission régionale lui transmet alors le dossier sans délai. Les délais des articles R. 122-18 et R. 122-21 commencent à courir à la réception du dossier par la formation d'autorité environnementale de l'inspection générale de l'environnement et du développement durable, qui notifie ce nouveau délai à la personne publique responsable.",
 "V. – Lorsqu'une révision est prévue par la législation ou la réglementation applicable, la révision d'un plan, schéma, programme ou document de planification du I donne lieu à une nouvelle évaluation. Pour un document du II, cette nouvelle évaluation est précédée d'un examen au cas par cas.",
 "VI. – En l'absence de disposition particulière, les modifications autres que les révisions d'un plan, schéma, programme ou document de planification du I ou du II ne donnent lieu à une évaluation environnementale qu'après un examen au cas par cas. Celui-ci détermine, s'il y a lieu, si l'évaluation initiale doit être actualisée ou si une nouvelle évaluation est nécessaire.",
 "VII. – Par dérogation à la présente section, le chapitre IV du titre préliminaire du code de l'urbanisme régit l'évaluation environnementale des plans et programmes des rubriques 43° à 51° du I et 12° à 12° ter du II.",
 "L'abrogation du 50° du I prend effet en même temps que l'abrogation des articles L. 121-28 à L. 121-30 du code de l'urbanisme : elle supprime une rubrique devenue sans objet du fait de la disparition du schéma de plage et ne dispense aucun autre plan, programme, projet ou autorisation de l'évaluation imposée par son régime propre. Les évaluations ou avis régulièrement intervenus ne sont pas rétroactivement invalidés ; ils ne permettent pas d'approuver un schéma dont la procédure a été supprimée. Les prescriptions et droits des autorisations antérieures restent préservés dans les conditions de l'article L. 121-30 du même code."
],"Supprimer exclusivement la rubrique I50° du schéma de plage SRU et réécrire l'article entier en conservant ses autres listes, exceptions, compétences, délais et règles d'actualisation, dans leur version documentaire à jour de 2026.","Source complète LEGIARTI000053610559, version depuis le 4 mars 2026, entièrement lue avec toutes les rubriques I à VII et sa note DILA non vide : troisième alinéa de l'article 9 du décret 2026-146 du 2 mars 2026, rédaction issue de son article 7 applicable aux demandes d'examen au cas par cas et d'avis environnemental déposées à compter du 1er mai 2026. Les rubriques II2° et II5° déjà abrogées ne sont pas rétablies. Le pouvoir d'évocation de la formation d'autorité environnementale provient de la rédaction 2026 et demeure exercé de sa propre initiative : aucune réintroduction du mécanisme ministériel d'une version ancienne. La note de 2026 et son champ temporel demeurent applicables aux normes conservées. Les titres officiels, références, catégories A/B, cas Natura2000, références 4°/5°, a/c et exceptions ont été contrôlés. L'exception FEDER pour les programmes de coopération territoriale ne relevant pas du II de L122-4 est conservée au I1° ; les programmes remplissant le III restent au II14°. Le délai plafond d'un an, la fin anticipée en cas de révision des listes, la nouvelle origine des délais en cas d'évocation et la notification sont maintenus. Les rubriques 43° à 51° sont conservées comme plage au VII, même si le 50° est abrogé, sans renumérotation. La coordination ne prétend pas que l'ensemble de cet article environnemental dérive de SRU : seule la rubrique visant le dispositif SRU supprimé est retirée. Source XML originale, archive, chemin membre et SHA inclus ; copie documentaire externe, aucun enregistrement dans la base canonique ni publication. Pas de validation juridique revendiquée.","Suppression de la seule rubrique I50° relative à l'évaluation systématique des schémas de plage L121-28, parce que ce régime de schéma lui-même est abrogé, avec maintien de toutes les évaluations autonomes.")
atomic('answer.json',rows);validate_answer(rows,sources)
audit={'articles':2,'validate_answer':'passed','registered':False,'published':False,'external_to_five_code_corpus':True,'canonical_database_modified':False,'source_files_modified':False,'archive_count':count,'as_of':'2026-10-19','answer_sha256':hashlib.sha256((P/'answer.json').read_bytes()).hexdigest(),'initial_to_current':[{'initial_article':'42','original_target':'L146-6-1','dependent_current_article':s['number'],'source_id':s['source_id'],'source_sha256':s['source_sha256'],'decision':'Coordination exclusivement dépendante du schéma supprimé ; autres normes autonomes conservées.'} for s in sources],'all_sru_complete':False}
atomic('audit.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
