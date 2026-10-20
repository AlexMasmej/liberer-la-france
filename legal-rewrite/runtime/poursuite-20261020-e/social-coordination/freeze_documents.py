import json, pathlib, hashlib, datetime, re

H=pathlib.Path('legal-rewrite').resolve(); E=pathlib.Path(__file__).resolve().parent
D=H/'runtime/poursuite-20261020-d/social-context-review/edition001'
def read(p): return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(s):return hashlib.sha256((s or '').encode()).hexdigest()
def fs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def key(x):return x['code_id']+'|'+x['source_id']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=E/'edition001'; C=E/'complement-r243-59/edition001'
S=read(F/'source.json');A=read(F/'answer.json');s59=read(C/'source.json')[0];a59=read(C/'answer.json')[0]
R={x['number']:x for x in read(C/'R243-59-referrers-inventory.json')['records']}
findings={
 '49 septies S':'La lettre et la réponse prévues au III restent les mêmes supports de l’examen fiscal ; aucune nouvelle sanction de 10 % n’est réintroduite par ce renvoi.',
 'R137-2':'Le renvoi général concerne le contrôle et ses agents ; compétences et garanties sont conservées.',
 'R243-17':'Les trois avantages et les exceptions autonomes ou historiques demeurent. Le renvoi général au contrôle ne recrée pas une majoration nouvelle de L243-7-6.',
 'R243-18':'Le point de départ historique vise les observations du deuxième alinéa du IV ; leur communication demeure exactement au même emplacement. La menace de sanction future seule disparaît.',
 'R243-43-2':'Le premier alinéa du I demeure l’avis de contrôle : aucune modification des conditions du rescrit, des délais ou des limites de suspension et prescription.',
 'R243-59-1':'L’exploitation des traitements, opposition et destruction des fichiers continuent de viser les mêmes avis, lettres, observations du IV et avis de crédit. Aucun déplacement de subdivision.',
 'R243-59-2':'Échantillonnage et extrapolation, délais d’opposition, calculs contradictoires et réponse avant recouvrement restent intacts ; la lettre du III reste le même acte.',
 'R243-59-3':'Le contrôle sur pièces des employeurs de moins de onze salariés conserve toutes les garanties de R243-59 et la règle de poursuite sur place.',
 'R243-59-4-1':'La sanction autonome d’obstacle, la défense, les conditions propres aux particuliers et le recouvrement du IV ne sont pas supprimés.',
 'R243-59-5':'Le renvoi aux premier et sixième alinéas du III et au deuxième du IV touche les paragraphes de motivation et d’observations sans redressement. Leur identité, calculs, données et destinataires sont préservés ; la suppression de la seule majoration de 10 % ne crée ni nouveau transfert ni reprise de cette sanction.',
 'R243-59-6-A':'La première visite mentionnée au I commence le contrôle ; la date d’envoi de la lettre d’observations du III y met fin. Ces deux événements demeurent inchangés. Corps source/null et appréciation C inchangés ; seul le certificat ciblant R243-59 devra être réémis après capture réelle.',
 'R243-59-7':'La protection tirée d’une absence d’observation à contrôle antérieur, mêmes circonstances de droit et de fait, reste applicable ; aucune nouvelle observation fictive n’est créée.',
 'R243-59-9':'La faculté de tout moyen donnant date certaine est conservée ; aucune voie exclusive nouvelle.',
 'R243-59-10':'Origine, contenu et identité des documents du groupe, communication et réponse contradictoire restent identiques. Les renvois au neuvième et au dernier alinéas du III ne sont pas déplacés.',
 'R244-1':'La mise en demeure conserve motifs, nature, montant et période, référence aux lettres du III, corrections et paiements ; les règles judiciaires de prescription ne changent pas.',
 'R246-1':'Le renvoi général au contrôle des prestations conserve agents, garanties et assiette ; aucune baisse de financement ou de droits n’est inférée.',
 'R246-2':'Le recouvrement des prestations reste soumis au même contrôle et aux mêmes garanties, sans suppression d’un dispositif distinct.',
 'R711-14':'Le contrôle des régimes spéciaux de prestations continue avec les mêmes garanties et sans changement des droits de retraite.'}
assert len(R)==18 and set(R)==set(findings),(set(R)-set(findings),set(findings)-set(R))
dump(C/'referrer-findings.json',{'scope':'18 sources, notes and effective proposals read in full; bounded consequences of the three R243-59 substitutions only.',
 'catalog_entries_scanned':30317,'records':[{'key':key(r),'number':n,'full_read':True,'source_sha256':r['guard']['source_sha256'],
  'source_body_sha256':sha(r['source_xml']),'source_notes_sha256':sha(r['source_notes_xml']),'proposed_sha256':sha(r['proposed_xml']),
  'subdivision_citations':r['source_and_proposed_subdivision_citations'],'finding':findings[n]} for n,r in R.items()],
 'no_new_referrer_proposals':True,'no_global_juridical_validation':True})

maps=[
 {'number':'R243-18','operative_targets':{'L243-7-6':'suppression future et transition','R243-59 IV deuxième alinéa':'point de départ historique des observations','L244-2 premier alinéa':'autre point de départ historique'},'engine_common_contract_guards':['L1221-2','L1234-1','L1234-9'],'own_change':'Coordination temporelle ; six ans et assiette limitée conservés ; renvoi interne premier alinéa corrigé après insertion de deux paragraphes.'},
 {'number':'R243-17','operative_targets':{'L243-7-6':'plus aucune exception nouvelle sur fondement supprimé ; anciens définitifs légalement dus seulement','R243-16':'majoration initiale et complémentaire ordinaires, distinctes','R243-59':'définition du contrôle inchangée','L243-7-7':'sanctions autonomes distinctes','L244-2':'mise en demeure et délais favorables'},'engine_common_contract_guards':['L1221-2','L1234-1','L1234-9'],'own_change':'Aucun corps ; nouvelle analyse de maintien des trois avantages et de la portée historique des trois renvois.'},
 {'number':'R243-19','operative_targets':{'L243-7-6':'suppression dans la liste ordinaire, compétence historique explicite','R243-15':'aucune réintroduction des accessoires provisoires supprimés ; DOETH distincte','L243-7-7':'sanctions autonomes maintenues','L244-2/L244-3':'paiement, recouvrement, prescription et recours maintenus'},'engine_common_contract_guards':['L1221-2','L1234-1','L1234-9'],'own_change':'Coordination du pouvoir de liquidation ; aucun nouveau délai de notification ni nouvelle sanction.'},
 {'number':'R243-59','operative_targets':{'L243-7-6':'énumération, caractérisation et menace du seul 10 % supprimé','L243-7-1 A':'lettre et contradictoire trente/soixante jours inchangés','L243-7-7':'sanctions autonomes et motivation maintenues','R133-1':'constats et pièces de travail dissimulé maintenus'},'engine_common_contract_guards':['L1221-2','L1234-1','L1234-9'],'own_change':'Trois substitutions de paragraphes à place constante ; I à V et toutes les autres phrases sont identiques.'}]
dump(E/'article-dependency-map.json',{'articles':maps,'scope':'Article-specific legal roles, distinct from the engine shared contract safeguards; not an all-to-all semantic approval.'})

by={a['number']:a for a in A};future_sha=sha(a59['proposed_xml']);future_analysis={
 'R243-17':'La vue réelle post-inscription de R243-59 doit correspondre exactement au SHA futur séparément annoncé. Ses trois substitutions retirent seulement l’énumération, le constat et la menace du 10 % abrogé. Le contrôle I à V, la lettre du III et les étapes du IV demeurent. R243-17 reste intégralement source/null : ses trois avantages et exceptions autonomes ou historiques ne changent pas, et aucun nouveau L243-7-6 ne peut devenir une exception.',
 'R243-18':'La vue réelle post-inscription de R243-59 doit correspondre exactement au SHA futur séparément annoncé. Le deuxième alinéa du IV continue de notifier les observations sans redressement ; le retrait de la menace de 10 % n’en change ni l’identité ni la date. Ce renvoi garde uniquement le point de départ des anciennes majorations définitives légalement dues. Le délai de six ans, l’assiette limitée et les recours ne sont pas rouverts.',
 'R243-59-6-A':'La vue réelle post-inscription de R243-59 doit correspondre exactement au SHA futur séparément annoncé. La première visite prévue au I et l’envoi de la lettre d’observations au III, seuls événements employés pour début et fin du contrôle, sont identiques au texte antérieur. Les trois substitutions ne déplacent aucun de ces actes. Le corps intégral source/null et l’appréciation de maintien de R243-59-6-A doivent rester exactement inchangés ; seule l’attestation de cette cible est réémise.'}
plan={'version':1,'status':'frozen_plan_only_not_a_current_certificate','future_target':{'key':key(s59),'number':'R243-59','expected_source_sha256':s59['source_sha256'],'expected_source_body_sha256':sha(s59['source_xml']),'expected_source_notes_sha256':sha(s59['source_notes_xml']),'future_proposed_sha256':future_sha,'pack_answer_sha256':fs(C/'answer.json')},
 'affected_existing_reference_certificates':['R243-17','R243-18','R243-59-6-A'],
 'unaffected_existing_reference_certificates':'Root inventoried the 36 C certificates: no other pins R243-59 and none pins R243-18/-19. This review does not reattest those certificates.',
 'steps':['Before either inscription, require all current own before-images, policies and target guards exact; reject unlisted concurrent changes.',
 'The current E3 checks target the present R243-59 source/null. Do not replace their hashes or call them post-commit checks in advance.',
 'After actual R243-59 inscription, capture source, complete notes, proposal, status and target view SHA from a new consistent DB read transaction. Compare raw proposal to the separately announced future body hash; block on any delta.',
 'Recapture the complete own source/notes and actual current before-image for R243-17, R243-18 and R243-59-6-A. Their bodies and substantive impacts must remain exact. R243-59-6-A remains source/null, with the exact old assessment.',
 'Re-read the three changed R243-59 paragraphs and the operative unchanged events in the actual committed whole. Turn the proposed assessments below into checks only after that capture; use the actual new view SHA.',
 'Validate the actual new snapshot and checks; under the shared registration lock compare all own and target guards again before metadata-only inscription. Do not reuse a pre-commit target certificate.',
 'For C141 audit renewal separately preserve own body/notes/source/assessment, all unrelated guards and policy SHA; permit only the explicitly approved fiscal/social deltas. Replace the three obsolete C assessments with the E analyses. Do not blanket-renew all144.'],
 'proposed_assessments_not_certificates':[{'number':n,'target_key':key(s59),'expected_future_proposed_sha256':future_sha,'assessment_after_actual_capture_only':txt} for n,txt in future_analysis.items()],
 'no_generated_future_view_certificate':True,'other_E_views':[{'number':a['number'],'key':key(a),'future_proposed_sha256':sha(a['proposed_xml'])} for a in A],
 'C141_proof_file':str((D/'compatibility-141.proposed.json').relative_to(H)), 'C141_proof_sha256':fs(D/'compatibility-141.proposed.json')}
dump(E/'post-commit-reissue-plan.json',plan)
test={'checked_at':now,'command':'python3 legal-rewrite/runtime/poursuite-20261020-e/social-coordination/test_preservation.py','tests':6,'passed':6,'failures':0,'scope':'Exact paragraph substitutions, subdivision positions, historical rules, unchanged guarantees, null retention and measure deduplication; no network or models.'}
dump(E/'preservation-tests.json',test)

(F/'REPORT.md').write_text('''Trois entrées gardées : R243-18, R243-17 et R243-19. Les sources, notes et avant-images courantes ont été lues intégralement. R243-18 et R243-19 coordonnent la suppression législative prospective du seul 10 % ; leurs règles historiques, assiettes, délais et recours sont conservés. R243-17 reste intégralement source/null : ses trois avantages et les sanctions autonomes ou historiques justifient ce maintien. Les trois anciens audits C doivent être remplacés, pas simplement renouvelés.

Les sept cibles complètes ont été lues et les dix-sept checks validés contre les vues réellement présentes. R243-59 est encore source/null dans ces vues. Le plan séparé impose recapture et réémission après son inscription pour R243-17 et R243-18, ainsi que C R243-59-6-A ; aucun certificat futur n’est présenté comme courant. Zéro nouvelle famille d’allègement : même measure_id que la suppression législative. Pas d’économie nationale ni validation par juriste.

Voir ../final-guards.json, ../article-dependency-map.json, ../post-commit-reissue-plan.json et ../preservation-tests.json. Aucune inscription ni mutation canonique effectuée.
''')
(C/'REPORT.md').write_text('''R243-59 entier : exactement trois paragraphes remplacés à leur emplacement. Le III retire la seule majoration de non-conformité de 10 % de l’énumération et du constat destiné à cette sanction ; le IV retire la menace de cette sanction. Le contrôle et les obligations légales autonomes demeurent. Sanctions anciennes définitives légalement dues, loi plus douce selon ses conditions, prescription et recours restent distincts.

Les autres paragraphes, I à V, délais trente/soixante jours, conseil, motivation, réponse et crédit sous un mois sont byte-identiques. Les renvois ordinaux préexistants sont conservés sans revendiquer leur validation globale. Les six tests séparés passent. Sept cibles complètes lues, sept checks contre vues actuelles ; avant-image d’absence de proposition gardée.

Inventaire sur les 30 317 identités canoniques : dix-huit referrers, sources/notes/propositions entières lus. Leurs conséquences sont détaillées dans referrer-findings.json. Parmi C, seuls R243-17, R243-18 et R243-59-6-A renvoient à R243-59. Les deux premiers sont E3 ; le troisième garde son source/null et son appréciation, avec réémission du certificat après capture réelle. Zéro gain nouveau et aucune inscription.
''')
(D/'REPORT.md').write_text('''Contrelecture indépendante bornée du lot CLI securite-sociale-00046 : 24 sources et notes entières, quatre propositions réelles et vingt maintiens source/null lus. Trois familles matérielles : convention sans terme/visa, suppression du seul 10 % de non-conformité, attestation provisoire non subordonnée à toutes les formalités génériques de création. L243-12 est une coordination ; les vingt maintiens protègent des règles nécessaires. Aucun défaut normatif concret supplémentaire relevé dans ce périmètre. Les coordinations réglementaires E sont nécessaires ; la chaîne n’est pas déclarée déjà cohérente.

Le contrôle RO frais trouve les 314 vues et les 144 anciens enregistrements C inchangés depuis capture. Les changements de gardes face au gel C portent sur L243-7-6 et trois cibles fiscales approuvées séparément ; ce contrôle ne transfère pas leur approbation. R243-17/-18/-19 ont des impacts C désormais à remplacer, plutôt qu’à renouveler mécaniquement.

L’accord proposé pour les autres 141 est limité aux conséquences des changements de cibles : recherche de renvois sur leurs sources/propositions, lecture complète des trois C affectés et de R243-59-6-A, plus dix-huit referrers de R243-59. Les 140 autres corps C ne sont pas déclarés relus intégralement. Aucun renvoi de ces141 à L243-7-6/R243-18/R243-19 ; seul R243-59-6-A vise R243-59 et ses événements ne changent pas. Les conditions d’adoption exigent toutes les autres gardes et appréciations exactes, et les vues futures E ne sont pas certifiées courantes. Aucun ledger modifié, aucune économie nationale ni certification juridique globale.
''')

def manifest(folder,extra=()):
    files={p.name:fs(p) for p in sorted(folder.iterdir()) if p.is_file() and p.name!='manifest.json'}
    dump(folder/'manifest.json',{'version':1,'frozen_at':now,'files':files,'external_evidence':{str(p.relative_to(H)):fs(p) for p in extra},'canonical_mutation':False,'semantic_review_by_jurist':False})
manifest(D)
evidence=[E/'final-guards.json',E/'article-dependency-map.json',E/'post-commit-reissue-plan.json',E/'preservation-tests.json',E/'test_preservation.py',D/'compatibility-141.proposed.json',D/'final-guards.json']
manifest(F,evidence);manifest(C,evidence)
for folder in [D,F,C]:
 print(folder.relative_to(H),'manifest',fs(folder/'manifest.json'))
