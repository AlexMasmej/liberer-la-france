from pathlib import Path
import json,re,html,hashlib

HERE=Path(__file__).resolve().parent
SOURCES=json.loads((HERE/'sources.json').read_text())
BY={a['number']:a for a in SOURCES}
ROWS=[];AUDIT=[]
POLICY='editorial_direction_2026_10_19'
TRANSITION='Les dispositions transitoires du V de l’article L. 302-5 du code de la construction et de l’habitation sont applicables.'

def paragraphs(items):return '\n'.join('<p>'+html.escape(t,quote=False)+'</p>'for t in items)
def old(number):
    a=BY[number]
    return html.unescape(a['previous_draft']['proposed_xml'])if a['previous_draft']else a['source_xml']
def replace(body,before,after):
    if body.count(before)!=1:raise ValueError('Expected exactly one match: '+before[:140])
    return body.replace(before,after)
def add(number,body,reason,review,removed=None,repeal=None):
    a=BY[number];row={k:a[k]for k in ('code_id','source_id','source_sha256','number')}
    row.update(status='rewrite_draft',proposed_xml=body,reason=reason,review_notes=review,prior_proposal_sha256=a['previous_draft']['proposed_sha256']if a['previous_draft']else None)
    if removed:row.update(change_type='normative_reduction',reform_policy_id=POLICY,removed_provisions=removed)
    if repeal:row.update(change_type='full_repeal',repeal_policy_id=POLICY,repeal_scope=repeal)
    ROWS.append(row)
    AUDIT.append({'code_id':a['code_id'],'source_id':a['source_id'],'number':number,'action':'full_repeal'if repeal else'rewrite','refs_before':a.get('refs',[]),'reason':reason,'notes':review})
def repeal(number,scope,notes):
    add(number,paragraphs(['Le présent article est abrogé à compter de l’entrée en vigueur de la loi supprimant les quotas communaux obligatoires de logements sociaux.',TRANSITION]),scope,notes,repeal=scope)

repeal('L111-24',
    'Supprimer les obligations de25% ou30% de logements sociaux imposées aux opérations collectives du seul fait du classement SRU ou de la carence communale, ainsi que les demandes de dérogation correspondantes.',
    'Source et précédent projet lus entièrement. Les seuils de douze logements/800m² et l’exception défense ne justifient plus de règle autonome une fois les deux obligations supprimées. Les permis et opérations déjà valablement engagés suivent le V proposé de L302-5 ; aucune autorisation décidée après la réforme ne peut exiger ces quotas de rattrapage. Les servitudes locales de mixité indépendantes de SRU ne sont pas supprimées ici.')

repeal('L131-9',
    'Supprimer l’obligation d’adapter le PLU tenant lieu de PLH sous deux ou trois ans au rattrapage SRU et les conséquences financières attachées à son absence de modification.',
    'Source et précédent projet lus entièrement. Le renvoi au dernier alinéa duII deL302-4 ne portait que sur l’affectation de prélèvementsSRU ; les autres obligations de compatibilité des documents et la politique locale de l’habitat restent distinctes. Coordination deR151-3 fournie dans le même lot.')

a=BY['L151-22'];body=old('L151-22')
before="II. – Dans les communes appartenant à une zone d'urbanisation continue de plus de 50 000 habitants qui figurent sur la liste prévue à l'article 1406 bis du code général des impôts, ainsi que dans les communes de plus de 15 000 habitants en forte croissance démographique qui figurent sur la liste prévue au dernier alinéa du II de l'article L. 302-5 du code de la construction et de l'habitation, le règlement doit définir une part minimale de surfaces non imperméabilisées ou éco-aménageables dans les secteurs qu'il délimite. Il applique les modalités prévues au I du présent article."
after="II. – Dans les communes appartenant à une zone d’urbanisation continue de plus de 50 000 habitants figurant sur la liste prévue à l’article1406bis du code général des impôts, ainsi que dans les communes figurant sur la liste des communes de plus de15000habitants en forte croissance démographique en vigueur la veille de l’entrée en vigueur de la loi supprimant les quotas communaux obligatoires de logements sociaux, le règlement définit une part minimale de surfaces non imperméabilisées ou éco-aménageables dans les secteurs qu’il délimite, selon les modalités duI. Le périmètre de cette dernière liste est maintenu à la seule fin de la présente règle d’urbanisme et de l’articleL151-36-1, indépendamment de tout quota communal, constat de carence ou inventaireSRU ; cette mention ne crée aucune collecte supplémentaire de données ni aucune nouvelle procédure de classementSRU."
body=replace(body,before,after)
add('L151-22',body,
    'Maintenir la protection environnementale distincte et son périmètre géographique existant, sans renvoi pendant auII supprimé deL302-5.',
    'Les I/II/III et l’exclusion des rénovations sans changement d’emprise au sol sont conservés. La liste des communes de plus de15000habitants est figée au périmètre en vigueur à la veille de la réforme ; aucune extension automatique à toutes les communes en croissance. Source R302-14III lue entière : croissance d’au moins5% sur cinq ans ou dernier recensement général, et critère distinct de pression sur la demande sociale à moyenne triennale ; ces paramètres ne sont pas recréés comme procédure d’inventaire ou de quota. Les notes fiscales2027 associées à la source ne constituent pas la date d’effet de cette réforme d’urbanisme.')

body=replace(old('L151-28'),"au sens de l'article L. 302-5 du code de la construction et de l'habitation","au sens du IV de l'article L. 302-5 du code de la construction et de l'habitation")
add('L151-28',body,
    'Rattacher la majoration volontaire de constructibilité à la définition autonome du logement social conservée auIV, sans supprimer cette aide à la construction.',
    'Source et précédent projet complets lus. Les1°à4°, plafonds20/50/30/30%, rapports de logements et résidences universitaires sont inchangés. Aucun quota communal n’est créé ; les seuils par opération sont ceux d’un avantage facultatif local indépendant deSRU. Les réservesL151-29/L151-43 sont maintenues.')

add('L151-36-1',paragraphs([
    'Nonobstant toute disposition du plan local d’urbanisme, les travaux de transformation ou d’amélioration de logements existants qui ne créent aucune surface de plancher supplémentaire sont dispensés de l’obligation de réaliser des aires de stationnement lorsque les logements sont situés dans une commune appartenant à une zone d’urbanisation continue de plus de50000habitants figurant sur la liste prévue à l’article1406bis du code général des impôts ou dans une commune de plus de15000habitants appartenant au périmètre géographique autonome maintenu auII de l’articleL151-22 du présent code. Cette dispense ne dépend ni d’un quota communal de logements sociaux ni d’un constat de carence.'
]),
    'Préserver la dispense de stationnement et son périmètre antérieur sans conserver la classification communaleSRU abolie.',
    'Source et projet antérieur lus intégralement. Même absence de surface supplémentaire, mêmes deux branches géographiques ; la seconde est figée parL151-22II et non élargie à toutes les communes de15000habitants. Les notes fiscales de2027 restent distinctes.')

body=replace(old('L152-6'),"Une dérogation aux règles prises selon l'article L. 151-15 est également possible si la commune n'est pas visée par un arrêté de l'article L. 302-9-1 du code de la construction et de l'habitation","Une dérogation aux règles prises selon l'article L. 151-15 est également possible, sans condition tenant à un ancien constat de carence communale")
add('L152-6',body,
    'Ouvrir la dérogation facilitant la transformation d’immeubles aux communes anciennement carencées, sans supprimer les autres conditions du dispositif.',
    'Source et précédent projet lus entièrement. Les1°à6°,5°bis, plafonds30/15/50/5%, distance800m, intégration urbaine, avis patrimonial et motifs de mixité indépendants sont conservés. L’extension aux communes anciennement carencées est explicite et ne crée pas un droit automatique à la dérogation.',
    removed=['Suppression de l’exclusion des communes carencées du bénéfice de la dérogation aux règles locales de mixité pour convertir un immeuble en logements.'])

body=replace(old('L152-6-3'),"des articles L. 111-24 et L. 151-15 et du 4° de l'article L. 151-41","de l'article L. 151-15 et du 4° de l'article L. 151-41")
add('L152-6-3',body,
    'Retirer le renvoi à l’obligationSRU abrogée sans réduire la dispense propre aux logements des agents de la défense.',
    'Source et précédent projet complets lus. Les seules règles restantes sont les règles locales indépendantes deL151-15 et4°L151-41 ; terrains défense, agents et autorisation d’urbanisme inchangés.')

body=old('L210-1');parts=re.findall(r'<p>(.*?)</p>',body,re.S)
if len(parts)!=4:raise ValueError('L210-1 paragraph count')
parts[1]='La substitution du représentant de l’État au titulaire du droit de préemption, ainsi que les délégations et transferts de compétence fondés exclusivement sur un ancien constat de carence au regard des quotas communaux de logements sociaux, cessent de produire effet à l’entrée en vigueur de la loi supprimant ces quotas. '+TRANSITION+' Les acquisitions déjà valablement réalisées, les droits des tiers et les opérations déjà engagées ne sont pas annulés de ce seul fait ; les autres titres légaux de compétence demeurent applicables.'
body='\n'.join('<p>'+p+'</p>'for p in parts)
add('L210-1',body,
    'Supprimer la substitution préfectorale et ses délégations de préemption ou d’autorisation fondées sur la seule carenceSRU.',
    'Les quatre alinéas sont maintenus à leur place. Le deuxième devient la fin opératoire du mécanisme antérieur ; finalités ordinairesL300-1, motivation et délibérations locales restent intactes. Les biens acquis et opérations valablement engagées suivent leV proposé deL302-5 ; aucune compétence nouvelle ne résulte d’une ancienne convention de carence.',
    removed=['Suppression de la préemption préfectoraleSRU, des délégations correspondantes, de la renonciation préfectorale ponctuelle et du transfert d’autorisations fondés seulement sur la carence.'])

body=replace(old('L211-2'),"ou déterminés en application du premier alinéa de l'article L. 302-8 du code de la construction et de l'habitation, ","")
body=replace(body,"à un organisme de foncier solidaire mentionné à l'article L. 329-1 dudit code","à un organisme de foncier solidaire mentionné à l'article L. 329-1 du présent code")
add('L211-2',body,
    'Retirer les objectifs obligatoires de rattrapageSRU de l’affectation des biens préemptés ; conserver les compétences et opérations locales indépendantes.',
    'Source et précédent projet lus entièrement. Quatre alinéas, bénéficiaires des délégations, PLH,OPAH,plans de sauvegarde,requalification et grandes opérations restent. Correction expresse du renvoi OFS :L329-1 appartient au code de l’urbanisme, non au CCH ; l’erreur était signalée dans le projet antérieur.',
    removed=['Suppression de l’affectation des biens préemptés aux objectifs communaux de rattrapage imposés par l’ancienL302-8, sans suppression des programmes locaux et opérations autonomes.'])

body=replace(old('L211-1'),"Toutefois, dans le cas prévu au deuxième alinéa de l'article L. 210-1, le représentant de l'État dans le département peut instituer ou rétablir ce droit par arrêté. Dans les parties actuellement urbanisées des communes dont le plan d'occupation des sols est devenu caduc en application de l'article L. 174-1, le droit de préemption prévu au deuxième alinéa de l'article L. 210-1 est maintenu.","L’institution, le rétablissement ou le maintien d’un droit de préemption par le représentant de l’État ne peut plus être fondé sur un ancien constat de carence au regard des quotas communaux de logements sociaux. "+TRANSITION)
add('L211-1',body,
    'Supprimer la création, le rétablissement et le maintien d’un droit de préemption préfectoral fondés sur l’ancienne carenceSRU.',
    'Source et projet antérieur lus intégralement. Les cinq alinéas sont conservés ; compétences communales, périmètres environnementaux, carte communale, exclusions de lots et finalités de relocalisation demeurent. La caducité desPOS n’est plus contournée pour maintenir un seul droit de préemptionSRU.',
    removed=['Suppression de l’institution ou du maintien préfectoral du droit de préemptionSRU, y compris dans les communes dont lePOS est devenu caduc.'])

body=old('L211-4');parts=re.findall(r'<p>(.*?)</p>',body,re.S)
if len(parts)!=6:raise ValueError('L211-4 paragraph count')
parts[5]='Le représentant de l’État ne peut plus étendre ce droit aux aliénations et cessions mentionnées au présent article sur le seul fondement d’un ancien constat de carence au regard des quotas communaux de logements sociaux. '+TRANSITION
body='\n'.join('<p>'+p+'</p>'for p in parts)
add('L211-4',body,
    'Supprimer le droit de préemption renforcé préfectoral lié à la carence, tout en préservant les exclusions et le pouvoir ordinaire motivé de la commune.',
    'Source et précédent projet lus entièrement. Six alinéas conservés ; lettresa/b/c, dix ans de copropriété, quatre ans après achèvement, et cinquième alinéa communal inchangés. Le renvoi deL211-2-3 est coordonné vers ce cinquième alinéa et ne redonne aucun pouvoir préfectoral.',
    removed=['Suppression du pouvoir préfectoral d’étendre le droit de préemption urbain aux opérations normalement exclues au seul titre de la carenceSRU.'])

body=replace(old('L211-2-3'),"dans les conditions prévues aux deux derniers alinéas du même article L. 211-4","dans les conditions prévues au cinquième alinéa du même article L. 211-4")
add('L211-2-3',body,
    'Coordonner le renvoi à l’extension communale du droit de préemption sans réintroduire l’extension préfectoraleSRU supprimée.',
    'Source et précédent projet entiers lus. Les trois alinéas et l’attribution du patrimoine au délégataire sont maintenus. Le cinquième alinéa deL211-4 reste la délibération motivée de la commune ; son sixième ne porte plus un pouvoir préfectoral actif.')

body=old('L213-2');parts=re.findall(r'<p>(.*?)</p>',body,re.S)
if len(parts)!=8:raise ValueError('L213-2 paragraph count')
parts[0]=replace(parts[0],'Dans le délai de deux mois prévu au troisième alinéa du présent article','Dans le délai de deux mois prévu au quatrième alinéa du présent article')
parts[2]='L’obligation spéciale de transmission au représentant de l’État dans les sept jours ouvrés, ainsi que l’amende forfaitaire de1000euros sanctionnant sa méconnaissance, sont supprimées lorsqu’elles étaient fondées sur l’exercice du droit de préemption au titre de l’ancienne carenceSRU. '+TRANSITION+' Les recours contre les décisions antérieures et l’application de la loi répressive plus douce aux sanctions non définitives sont préservés ; aucun nouveau procès-verbal ni aucune nouvelle sanction ne peut être fondé sur cette obligation supprimée.'
body='\n'.join('<p>'+p+'</p>'for p in parts)
add('L213-2',body,
    'Supprimer l’obligation spéciale de transmission deDIA au préfet et son amende de1000euros attachées à la préemptionSRU.',
    'Source,notes et précédent projet lus intégralement. Huit alinéas conservés, dont un troisième transitoire ; correction expresse du premier renvoi au délai de deux mois vers le quatrième alinéa, déjà erroné dans la source. Demande unique, suspension, délai résiduel d’un mois, notifications,droit de visite et prescription cinq ans inchangés. Les conventions anciennes de requalification de quartiers mentionnées dans la note2018 demeurent distinctes.',
    removed=['Suppression de la transmission spéciale en sept jours au préfet, du procès-verbal de non-transmission et de l’amende communale de1000euros exclusivement attachés à la carenceSRU.'])

body=old('L324-1')
body=replace(body,"Le droit de préemption exercé en application du deuxième alinéa de l'article L. 210-1 s'inscrit dans le cadre de conventions conclues avec le représentant de l'État dans le département.","La délégation à l’établissement d’un droit de préemption fondée exclusivement sur l’ancienne carence communale au regard des quotas de logements sociaux cesse de produire effet à l’entrée en vigueur de la loi supprimant ces quotas. "+TRANSITION)
body=replace(body,"Sauf convention prévue au sixième alinéa du présent article, la réalisation de toute opération","La réalisation de toute opération")
add('L324-1',body,
    'Supprimer les délégations de préemptionSRU aux établissements fonciers et la dispense d’avis communal qui n’existait que pour ces conventions.',
    'Source et précédent projet complets lus. Dix alinéas conservés ; objectifs de logement, environnement, activités économiques,réserves foncières,observation et autres délégations demeurent. Le sixième alinéa porte la fin du seul mécanismeSRU ; le dernier retrouve son régime commun d’avis favorable de la commune, avec le délai de deux mois existant.',
    removed=['Suppression des conventions préfectorales de préemptionSRU et de leur dérogation particulière à l’avis communal favorable pour les opérations futures.'])

body=replace(old('L324-8'),"2° La contribution prévue à l'article L. 302-7 du code de la construction et de l'habitation ;","2° Les versements correspondant aux seules créances antérieures légalement conservées dans les conditions du V de l’article L. 302-5 du code de la construction et de l’habitation ; aucune contribution nouvelle n’est due au titre des quotas communaux supprimés ;")
add('L324-8',body,
    'Supprimer la contributionSRU comme recette future récurrente et ne conserver que l’encaissement des véritables créances antérieures sauvegardées.',
    'Source et projet antérieur entiers lus. Rubriques1°à6° et renvois budgétaires conservés ; aucun financement nouveau ou compensation budgétaire inventé. Le2° n’autorise pas une contribution due à un fait postérieur à la réforme.',
    removed=['Suppression de la contributionSRU future comme recette de fonctionnement des établissements publics fonciers locaux ; seuls droits de créance antérieurs légalement sauvegardés.'])

body=old('L422-2');parts=re.findall(r'<p>(.*?)</p>',body,re.S)
idx=next(i for i,p in enumerate(parts)if p.startswith('d)'))
parts[idx]='d) Abrogé ;'
add('L422-2','\n'.join('<p>'+p+'</p>'for p in parts),
    'Supprimer la compétence préfectorale de délivrance des autorisations d’urbanisme fondée uniquement sur l’ancienne carenceSRU.',
    'Source et précédent projet lus entièrement. Lettresaàh et alinéas conservés avecd abrogé ; compétences étatiques pour énergie,OIN,SNCF et autres projets indépendants intactes. La transition deL302-5V protège les permis déjà délivrés sans imposer un rattrapage aux décisions nouvelles. CoordinationR*422-2g fournie.',
    removed=['Suppression de la substitution préfectorale pour les secteurs et opérations de logement désignés uniquement par un arrêté ou une convention de carenceSRU.'])

body=replace(old('R151-37'),"au sens de l'article L. 302-5 du code de la construction et de l'habitation","au sens du IV de l'article L. 302-5 du code de la construction et de l'habitation")
add('R151-37',body,
    'Conserver la majoration locale facultative de volume en utilisant la définition autonome du logement social auIV.',
    'Source complète lue. Les1°à7°, mixité fonctionnelle, commerce, logements intermédiaires et renvois aux majorations deL151-28 demeurent inchangés ; ce dispositif facultatif n’est pas un quota communalSRU.')

add('R151-3',paragraphs([
    'Au titre de l’évaluation environnementale, le rapport de présentation :',
    '1° Décrit l’articulation du plan avec les documents d’urbanisme, plans ou programmes mentionnés aux articlesL131-4àL131-6 etL131-8 avec lesquels il doit être compatible ou qu’il doit prendre en compte ;',
    '2° Analyse l’état initial de l’environnement et ses perspectives d’évolution, notamment les caractéristiques des zones susceptibles d’être touchées de façon notable par la mise en œuvre du plan ;',
    '3° Analyse les incidences notables probables du plan sur l’environnement, notamment, s’il y a lieu, sur la santé humaine, la population, la diversité biologique, la faune, la flore, les sols, les eaux, l’air, le bruit, le climat, le patrimoine culturel architectural et archéologique et les paysages, ainsi que les interactions entre ces facteurs. Il expose les problèmes posés par l’adoption du plan pour les zones présentant une importance particulière pour l’environnement, notamment l’évaluation des incidencesNatura2000 prévue à l’articleL414-4 du code de l’environnement ;',
    '4° Explique les choix retenus au premier alinéa de l’articleL151-4 au regard des objectifs de protection de l’environnement fixés au niveau international, de l’Union européenne ou national et les raisons du choix effectué parmi les solutions de substitution raisonnables, compte tenu des objectifs et du champ géographique du plan ;',
    '5° Présente les mesures envisagées pour éviter, réduire et, si possible, compenser les conséquences dommageables éventuelles de la mise en œuvre du plan sur l’environnement ;',
    '6° Définit les critères, indicateurs et modalités de l’analyse des résultats de l’application du plan prévue à l’articleL153-27 et, le cas échéant, du bilan relatif à l’habitat prévu à l’articleL153-29. Ils permettent notamment de suivre les effets environnementaux du plan, d’identifier assez tôt les impacts négatifs imprévus et d’envisager les mesures appropriées ;',
    '7° Comprend un résumé non technique des éléments précédents et décrit la méthode d’évaluation.',
    'Le rapport est proportionné à l’importance du plan local d’urbanisme, aux effets de sa mise en œuvre et aux enjeux environnementaux de la zone considérée.',
    'Lorsque l’approbation du plan local d’urbanisme vaut création d’une zone d’aménagement concerté, la procédure commune d’évaluation d’un plan ou programme et d’un projet prévue auII de l’articleR122-25 du code de l’environnement est mise en œuvre.'
]),
    'Retirer de l’évaluation environnementale le renvoi à la seule mise en compatibilitéSRU abrogée deL131-9, sans supprimer l’évaluation elle-même.',
    'Source et note2021 lues entièrement. Les1°à7°,Natura2000,proportionnalité,évitement/réduction/compensation et procédure communeZAC sont maintenus. La note du décret2021-1345,article26, distingue les procédures bénéficiant d’une dispense antérieure et les autres décisions antérieures ; ces conditions temporelles ne sont pas transformées en date de la réformeSRU.',
    removed=['Suppression du seul renvoi de l’évaluation environnementale à l’adaptation obligatoire duPLU au rattrapageSRU deL131-9 abrogé.'])

body=old('R329-11');parts=re.findall(r'<p>(.*?)</p>',body,re.S)
idx=next(i for i,p in enumerate(parts)if p.startswith('8°'))
parts[idx]='8° Abrogé ;'
add('R329-11','\n'.join('<p>'+p+'</p>'for p in parts),
    'Supprimer la rubrique du rapportOFS dédiée exclusivement au décompte et à l’inventaireSRU.',
    'Source complète lue. Date31juillet, rubriques1°à10° autres que8°, comptes certifiés, suivi des preneurs, dons et mise en demeure d’un mois conservés. Les données d’activitéOFS indépendantes deSRU ne sont pas abolies ; aucune information individuelle supplémentaire n’est demandée pour la seule définition deL302-5IV.',
    removed=['Suppression des données du rapportOFS destinées exclusivement au décompteSRU des logements en bail réel solidaire, avec retrait du renvoi àR302-15 inventaire.'])

add('R*422-2',paragraphs([
    'Le préfet délivre les permis de construire, d’aménager et de démolir et statue sur les déclarations préalables dans les communes mentionnées aub de l’articleL422-1 et dans les cas de l’articleL422-2, pour les hypothèses suivantes :',
    'a) Les projets réalisés pour le compte d’États étrangers, d’organisations internationales, de l’État, de ses établissements publics ou de ses concessionnaires ;',
    'b) Les ouvrages de production, de transport, de distribution et de stockage d’énergie lorsque celle-ci n’est pas destinée principalement à l’utilisation directe du demandeur ;',
    'b bis) Les installations, ouvrages et constructions que le demandeur présente comme agrivoltaïques au sens de l’articleL314-36 du code de l’énergie ;',
    'c) Les installations nucléaires de base ;',
    'd) Les travaux soumis à autorisation du ministre de la défense ou du ministre chargé des sites, ou évoqués par le ministre chargé de la protection de la nature ou par celui chargé des monuments historiques et espaces protégés ;',
    'e) Le désaccord entre le maire et le responsable du service de l’État chargé de l’instruction mentionné à l’articleR423-16 ;',
    'f) Les ouvrages, constructions ou installations de l’articleL2124-18 du code général de la propriété des personnes publiques ;',
    'g) Abrogé ;',
    'h) Les travaux, constructions et installations réalisés pour le compte deSNCFRéseau mentionnée à l’articleL2111-9 du code des transports, ou de sa filiale mentionnée au5° de cet article, dans le cadre des missions de service public confiées par ce même article ;',
    'i) Les travaux, installations, constructions et aménagements d’un projet industriel qualifié par décret de projet d’intérêt national majeur pour la transition écologique ou la souveraineté nationale.',
    'Le préfet peut déléguer sa signature au responsable du service de l’État chargé de l’instruction ou à ses subordonnés, sauf dans le cas due ci-dessus.'
]),
    'Supprimer la compétence préfectorale réglementaire fondée sur un arrêté ou une convention de carenceSRU.',
    'Source et note du décret2024-704,article4,lues entièrement. Lettres et nombre d’alinéas conservés, g abrogé ; aucune renumérotation du h ou du i. Le renvoi deR*427-1 après le huitième alinéa reste après le f ; l’exception de délégation de signature au e reste à sa place. La coquille source«articl» est corrigée en«article». Les autres compétences préfectorales restent distinctes.',
    removed=['Suppression de la compétence préfectorale réglementaire pour les constructions et conventions de logement liées à la seule carence communaleSRU.'])

repeal('R*431-16-3',
    'Supprimer le tableau supplémentaire du dossier de permis exigé uniquement pour vérifier le quotaSRU dans les communes carencées.',
    'Source entière lue. Aucune pièce de remplacement n’est imposée au titre deSRU. Le tableau distinct deR*431-17 reste utile à une majoration volontaire de constructibilité et n’est pas supprimé.')

add('R*431-17',paragraphs([
    'Lorsque la demande de permis de construire porte sur des constructions qui bénéficient, dans les conditions du2° de l’articleL151-28, d’un dépassement du volume constructible résultant des règles de gabarit, de hauteur et d’emprise au sol, le dossier est complété :',
    '1° Soit par un tableau indiquant le nombre de logements prévus et la part de logements locatifs sociaux définis auIV de l’articleL302-5 du code de la construction et de l’habitation ;',
    '2° Soit par une attestation du demandeur prévoyant la réalisation d’une résidence universitaire définie à l’articleL631-12 du même code.'
]),
    'Conserver la justification d’une majoration volontaire de volume, avec renvoi à la définition sociale autonome duIV.',
    'Source et note du décret2026-674,article10,II,lues entièrement.1°et2° demeurent des pièces alternatives. La date source28septembre2026 reste celle de cette version réglementaire ; elle n’est pas la date d’une abolitionSRU. Ce tableau ne sert pas à un inventaire communal et n’est pas celui deR*431-16-3 supprimé.')

add('D411-2',paragraphs([
    'La notification du bailleur prévue à l’articleL411-5-1 est délivrée à chaque locataire de l’immeuble ou du groupe d’immeubles par lettre recommandée avec demande d’avis de réception.',
    'Au plus tard deux mois après l’envoi de cette notification, le bailleur propose une réunion d’information à l’ensemble des locataires.',
    'La prévision d’augmentation des loyers jointe à la notification respecte les dispositions desc etd de l’article17 de la loi du6juillet1989 tendant à améliorer les rapports locatifs et portant modification de la loi n°86-1290 du23décembre1986.'
]),
    'Supprimer la vérification du passage sous quotaSRU et le calendrier d’avis communal qui n’existait que pour ce seuil, en maintenant les protections des locataires.',
    'Source entière lue. Coordination avec le rédacteur deL411-5-1 : information des locataires/maires/préfet conservée ; son ancien quatrième alinéa d’avis conformeSRU est supprimé. Les deux derniers alinéas deD411-2 deviennent donc sans objet et sont supprimés, sans supprimerLRAR,réunion à deux mois ni prévision de loyer. Le renvoi historiquec/d de l’article17 de la loi1989 reste à contrôler dans ce texte hors corpus et n’est pas réinterprété silencieusement.',
    removed=['Suppression de la demande de vérification préfectorale du seuil communalSRU, de l’information spécifique du maire et du calendrier d’avis lié à ce seul seuil.'])

add('R411-3',paragraphs([
    'Pour constituer et actualiser le répertoire des logements locatifs de l’articleL411-10, les bailleurs sociaux mentionnés à cet article transmettent chaque année au service statistique ministériel du logement, avant le1ermars, les informations suivantes pour chacun des logements locatifs sur lesquels ils détiennent un droit réel immobilier ou un usufruit au1erjanvier de l’année ou de l’année précédente :',
    'a) L’identifiant du logement dans le répertoire de l’administration et son identifiant dans le système du bailleur ;',
    'b) L’identité du bailleur et, s’il y a lieu, du gestionnaire ;',
    'c) L’identité du précédent bailleur lorsque le logement est entré dans le patrimoine au cours de l’année civile précédente ;',
    'd) La localisation, les caractéristiques principales et les équipements techniques du logement, y compris, s’il y a lieu, les éléments de son diagnostic de performance énergétique ;',
    'e) L’année et le mode d’entrée dans le patrimoine, le type de droit détenu et les transferts de propriété ou d’usufruit intervenus l’année civile précédente ;',
    'f) Les fusions, éclatements et changements d’usage du logement intervenus l’année civile précédente ;',
    'g) Le financement initial, le numéro et la date d’effet de la convention pour les logements conventionnés des2°et3° de l’articleL831-1 et, s’il y a lieu, leur catégorie de financement lorsque les loyers prennent en compte le classement des immeubles ou groupes d’immeubles de l’articleL445-1 dans la convention d’utilité sociale du même article ;',
    'h) Le mode d’occupation au1erjanvier de l’année, la dernière date à laquelle le logement a pu être offert à la location et la date de prise d’effet du bail en cours ;',
    'i) Le loyer, avant toute modulation liée à la situation du locataire, et son mode de calcul ;',
    'j) Abrogé ;',
    'k) Pour les logements relevant de l’articleL443-11, les informations sur leur mise en commercialisation effective l’année civile précédente et les conditions financières de la vente ;',
    'l) Le contingent d’appartenance des logements réservés au sens de l’articleR441-5.',
    'La liste détaillée des informations restantes et leurs modalités de collecte et de transmission sont fixées par arrêté conjoint du ministre chargé du logement et du ministre ayant autorité sur le service statistique ministériel du logement. Cet arrêté ne peut rétablir une collecte destinée exclusivement à un inventaire ou un quota communalSRU supprimé.'
]),
    'Supprimer les données complémentaires exclusivement destinées à l’inventaireSRU, en conservant le répertoire statistique et de gestion locative indépendant.',
    'Source et note du décret2021-1750,article6,lues entièrement. Les lettresaàl sont conservées avecj abrogé, ainsi que les dates de référence, la transmission au1ermars et les données de contingent/vente. La note évoque les contributions et prestations à compter du1erjanvier2022 ; elle n’est pas transformée en date de la présente réforme. Pas de collecte supplémentaire attachée à la seule définition deL302-5IV.',
    removed=['Suppression des données complémentairesj du répertoireRPLS entrant exclusivement dans le champ de l’ancien inventaireSRU.'])

body=old('150 U')
cut="Lorsque les biens ou droits sont situés dans une commune mentionnée au I de l'article L. 302-5 du même code qui n'atteint pas les seuils fixés aux I et II du même article L. 302-5, le cessionnaire s'engage également à affecter aux logements sociaux définis au présent alinéa une surface habitable représentant au moins 25 % de la surface totale des constructions du programme immobilier."
body=replace(body,cut,'La cession n’est soumise à aucun engagement supplémentaire de proportion de logements sociaux fondé exclusivement sur le non-respect d’un ancien quota communalSRU.')
body+='\n'+paragraphs([
    'V. – La suppression du seul engagement supplémentaire de proportion de logements sociaux lié à un ancien quota communalSRU s’applique aux cessions dont le fait générateur est postérieur à l’entrée en vigueur de la loi supprimant ces quotas. Elle ne modifie pas les autres dates, durées, conditions ou engagements du présent article et ne crée pas un droit général au remboursement des impositions relatives aux faits générateurs antérieurs.',
    'Les engagements valablement pris et les droits relatifs aux opérations antérieures sont traités dans les conditions transitoires duV de l’articleL302-5 du code de la construction et de l’habitation. L’application de la loi répressive plus douce aux sanctions non définitives demeure réservée.'
])
add('150 U',body,
    'Supprimer l’engagement supplémentaire de25% de logements sociaux conditionné au déficit communalSRU, en maintenant les exonérations de plus-values et les autres engagements de construction.',
    'Source et précédent projet complets lus. Les27paragraphesXML et séparations internes du7°/8° sont conservés, ainsi que toutes les cibles d’alinéas. Délais, gabarit75%, prorata et exonération totale au-delà de80%, exclusionsANRU, amendes liées aux engagements indépendants, 9°surélévation etIVpartages successoraux restent inchangés. La suppression ciblée ne crée ni taux ni exonération générale des plus-values ; opérations engagées et sanctions non définitives suiventL302-5V.',
    removed=['Suppression de l’engagement supplémentaire de25% de surface sociale exigé du cessionnaire uniquement parce que la commune n’atteignait pas son ancien quotaSRU.'])

body=old('150 VE')
cut="Lorsque les biens ou droits sont situés dans une commune mentionnée au I de l'article L. 302-5 du même code qui n'atteint pas les seuils fixés aux I et II du même article L. 302-5, le cessionnaire s'engage également à affecter aux logements sociaux définis à la première phrase du présent alinéa une surface habitable représentant au moins 25 % de la surface totale des constructions du programme immobilier prévu au II du présent article."
body=replace(body,cut,'Le bénéfice de l’abattement ne dépend d’aucun engagement supplémentaire de proportion de logements sociaux fondé exclusivement sur le non-respect d’un ancien quota communalSRU.')
body+='\n'+paragraphs([
    'VII. – La suppression du seul engagement supplémentaire de proportion de logements sociaux lié à un ancien quota communalSRU s’applique aux cessions dont le fait générateur est postérieur à l’entrée en vigueur de la loi supprimant ces quotas. Les périodes de signature des promesses, délais de cession ou d’achèvement et autres conditions du présent article restent inchangés. Aucun droit général à restitution n’est créé pour les faits générateurs antérieurs.',
    'Les engagements antérieurement valablement pris et les droits relatifs aux opérations antérieures sont traités dans les conditions transitoires duV de l’articleL302-5 du code de la construction et de l’habitation, sous réserve de la loi répressive plus douce applicable aux sanctions non définitives.'
])
add('150 VE',body,
    'Supprimer l’engagement additionnel de25% lié au déficit communalSRU sans réduire les abattements existants pour les opérations de construction.',
    'Source et précédent projet entiers lus. Dix-sept alinéas, subdivisionsIàVI et renvois au dernier alinéa duIII restent ; abattements60/75/85%, affectation autonome50%,gabarit75%,calendrier2024–2027,quatre ans,exclusion familiale/ANRU/Corse et reprises d’engagement maintenus. Le seuil autonome50% permettant un abattement majoré n’est pas un quota communalSRU et reste applicable.',
    removed=['Suppression de la condition de25% de surface sociale supplémentaire attachée uniquement au déficit communalSRU pour bénéficier de l’abattement majoré de plus-value.'])

body=BY['279-0 bis A']['source_xml'];parts=re.findall(r'<p>(.*?)</p>',body,re.S)
idx=next(i for i,p in enumerate(parts)if p.startswith('4°'))
parts[idx]='4° Abrogé ;'
idx=next(i for i,p in enumerate(parts)if p.startswith('II.'))
parts[idx]='II. – Abrogé.'
body='\n'.join('<p>'+p+'</p>'for p in parts)
body+='\n'+paragraphs([
    'III. – La suppression des conditions du4°duI et duII s’applique aux livraisons et travaux dont le fait générateur est postérieur à l’entrée en vigueur de la loi supprimant les quotas communaux obligatoires de logements sociaux. Elle ne crée aucun droit général au remboursement de la taxe afférente aux faits générateurs antérieurs.',
    'Les autres dates d’application, conditions de ressources, de loyer, de localisation, de destination et de réalisation des logements et travaux restent inchangées. Les opérations, contrats et droits déjà valablement engagés sont préservés dans les conditions duV de l’articleL302-5 du code de la construction et de l’habitation.',
    'Lors de la reprise des présentes dispositions dans le code des impositions sur les biens et services et de leurs mesures réglementaires d’application, la suppression de ces seules conditions est maintenue pour les faits générateurs postérieurs à l’entrée en vigueur de la présente réforme. Cette coordination n’avance ni ne reporte les autres dates de la recodification et ne rétablit aucune condition communale ou de mixité du programme supprimée au présent article.'
])
add('279-0 bis A',body,
    'Supprimer la condition de25% de logements sociaux au niveau de la commune ou du programme pour bénéficier du taux existant de10% sur les logements intermédiaires.',
    'Source et notes entières lues. Extension explicite : dans tout le périmètre géographique duI3°, les livraisons respectant les autres conditionsI1°/2°/5° bénéficient du10% sans condition de quota communal ni de mixité sociale du programme. C’est une ouverture de l’avantage, pas le retrait du régime aux communes anciennement au-dessus de25%. Ressources,loyers,personne morale,localisation,construction/acquisition-amélioration etIbis maintenus. Suppression ciblée4°I/II sans nouveau taux. Notes ordonnance2025-1247 : abrogation2027 et maintien3°I/II jusqu’à reprise réglementaireCIBSL221-66 ; un candidat compagnon hors corpus coordonne cette recodification afin d’éviter le rétablissement de la condition supprimée.',
    removed=['Suppression duI4°etduII imposant un quota social communal ou une condition alternative de mixité du programme pour le taux réduit existant de10%, extension expressément assumée.'])

for number in ('1384 B','1384 C'):
    body=replace(BY[number]['source_xml'],"au sens de l'article L. 302-5 du code de la construction et de l'habitation"if number=='1384 C'else"au sens de l'article L. 302-5 du même code", "au sens du IV de l'article L. 302-5 du code de la construction et de l'habitation"if number=='1384 C'else"au sens du IV de l'article L. 302-5 du même code")
    add(number,body,
        'Coordonner la définition du logement social vers leIV autonome, en préservant les exonérationsTFPB et leur régime indépendant.',
        'Source complète et notes lues. Le seuil de50% de parc social, les délibérations locales et leurs effets prospectifs, durées/dates et mécanismes de compensation existants restent conservés : ce seuil n’est pas un quotaSRU20/25%. Aucune compensation budgétaire nouvelle n’est inventée. Les références historiques à l’article191 de la loiSRU dans1384C concernent l’établissement immobilier duNord-Pas-de-Calais et restent maintenues.')

add('1384 G',paragraphs([
    'Les constructions neuves affectées à l’habitation principale issues d’opérations de démolition et de reconstitution de logements locatifs sociaux, réalisées dans les conditions des articles6et9-1 de la loi n°2003-710 du1eraoût2003 et prévues par une convention de son article10-3, ne bénéficient pas des exonérations des articles1384à1384F si les deux conditions suivantes sont réunies : les immeubles auxquels elles se substituent dans le même quartier prioritaire délimité par la convention ont bénéficié d’une de ces exonérations ; les logements locatifs sociaux définis auIV de l’articleL302-5 du code de la construction et de l’habitation représentent au moins50% des résidences principales de la commune où se trouvent les nouvelles constructions.',
    'Cette règle s’applique aux opérations de reconstitution de l’offre démolie agréées à compter du1erjanvier2017.'
]),
    'Coordonner le renvoi définitionnel auIV deL302-5 sans modifier la restrictionTFPB distincte liée à la reconstitution en quartier prioritaire.',
    'Source complète lue. Les deux conditions cumulatives, le seuil50%, le périmètre du même quartier, les conventionsANRU et la date1erjanvier2017 restent. Il ne s’agit pas du quota communalSRU20/25% aboli ; aucune suppression fiscale supplémentaire n’est glissée dans cette coordination.')

for number,why in [
    ('L311-6','La référence à l’article7 de la loi2000-1208 constate un régime historique des cahiers des chargesZAC ; aucun quota ni carenceSRU.'),
    ('L311-7','La référence à la loi2000-1208 n’est qu’une règle historique d’entrée en vigueur des plans d’aménagementZAC ; aucune obligationSRU à conserver.'),
    ('1388 bis','L’article191 de la loi2000-1208 identifie l’établissement immobilier duNord-Pas-de-Calais ; ni quota ni carence. L’abattement30%enQPV, les contrats/conventions et dates2025–2030 restent indépendants.'),
    ('1391 D','Renvoi déjà explicite aux3°et4°duIV deL302-5 conservés ; le dégrèvement pour travaux prescrits et les conditions de réclamation sont indépendants du quota communal.')]:
    a=BY[number];AUDIT.append({'code_id':a['code_id'],'source_id':a['source_id'],'number':number,'action':'unchanged','reason':why,'source_read_complete':True,'previous_draft_read_complete':bool(a['previous_draft'])})

def spaces(text):
    text=text.replace('SNCFRéseau','SNCF Réseau')
    text=re.sub(r'(?<=[A-Za-zÀ-ÿ])(?=\d)|(?<=\d)(?=[A-Za-zÀ-ÿ])',' ',text)
    text=re.sub(r'(?<=[a-zà-ÿ])(?=[A-Z])',' ',text)
    text=re.sub(r'\b(articles?)(?=[A-Z])',r'\1 ',text)
    text=re.sub(r'\b([LRD])\s+(?=\d)',r'\1. ',text)
    text=re.sub(r'(?<=\d)%',' %',text)
    text=re.sub(r'(?<=°)(?=[A-Za-zÀ-ÿ])',' ',text)
    text=re.sub(r'(?<=n°)(?=\d)',' ',text)
    text=re.sub(r'([,;:])(?=\S)',r'\1 ',text)
    text=re.sub(r'\b(\d+) er(?=\b|[a-zÀ-ÿ])',r'\1er ',text)
    for a,b in {'duI':'du I','duII':'du II','auI':'au I','auII':'au II','duIV':'du IV','auIV':'au IV','duIII':'du III','duV':'du V','auV':'au V','deSNCFRéseau':'de SNCF Réseau','due ci-dessus':'du e ci-dessus','desc etd':'des c et d','c/d':'c/d','inventaireSRU':'inventaire SRU','communalSRU':'communal SRU','carenceSRU':'carence SRU','quotaSRU':'quota SRU','quotasSRU':'quotas SRU','classementSRU':'classement SRU','duPLU':'du PLU','rapportOFS':'rapport OFS','proposéde':'proposé de','alinéaSRU':'alinéa SRU','d’inventaireSRU':'d’inventaire SRU'}.items():text=text.replace(a,b)
    return text

for row in ROWS:
    row['reason']=spaces(row['reason']);row['review_notes']=spaces(row['review_notes'])
    # Do not rewrite HTML entity encodings inside the preserved old paragraphs.
    row['proposed_xml']=''.join(part if part.startswith('<')else spaces(part)for part in re.split(r'(<[^>]+>)',row['proposed_xml']))

(HERE/'candidates.json').write_text(json.dumps(ROWS,ensure_ascii=False,indent=2)+'\n')
(HERE/'reference-audit.json').write_text(json.dumps(AUDIT,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidates':len(ROWS),'unchanged':sum(a['action']=='unchanged'for a in AUDIT),'numbers':[a['number']for a in ROWS]},ensure_ascii=False))
