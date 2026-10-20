"""Activate the coherent, already registered phase C decisions and short summaries."""
from pathlib import Path
from datetime import datetime, timezone
import fcntl, hashlib, json, sys
P=Path(__file__).resolve().parent;B=P.parents[1]
sys.path.insert(0,str(B))
from run_exhaustive import atomic
from register_batches import writer_lock
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
reg=load(P/'integration/edition001/registration.json')
pre=load(P/'integration/edition001/preflight.json')
assert reg['registered_articles']==pre['articles']
for package in pre['packages']:
    assert (P/package['review']).exists()
    assert sha(P/package['folder']/package.get('answer','answer.json'))==package['answer_sha256']
amendment=load(P/'fiscal/edition001/policy-amendment.proposed.json')
with (B/'runtime/publication.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    with writer_lock():
        assert sha(B/'policy-coordinations.json')==amendment['active_policy_sha256']
        assert sha(B/'site-summaries.json')==amendment['active_site_summaries_sha256']
        policy=load(B/'policy-coordinations.json');sites=load(B/'site-summaries.json')
        atomic(P/'policy-before.json',policy);atomic(P/'site-summaries-before.json',sites)
        for k,v in amendment['proposed_additions'].items():
            assert k not in policy
            policy[k]=v
        policy['travail'].extend([
            'Phase C : L2262-6 supprime la liste annuelle des modifications de conventions/accords non encore échue, sans rapport périodique de remplacement. L2262-7 conserve l’information immédiate sur la démission d’une organisation signataire et explicite ses destinataires, sans renvoi vide. Les textes actuels, copies aux représentants et informations de mise à jour distinctes restent.',
            'Phase C : L3243-2, R3243-9 et L5151-6 II2° retirent le raccordement obligatoire des bulletins électroniques au CPA pour les remises futures. Accès direct sûr et gratuit pour le salarié, intégrité/confidentialité, opposition et conservation D3243-8 demeurent, ainsi que les droits sur les bulletins antérieurs. Pas de nouvelle obligation de plateforme, d’équipement ou d’abonnement salarié.',
            'Phase C : D3243-7 retire seulement le mois d’anticipation obligatoire avant la première remise électronique aux salariés déjà présents. Information prouvable avant remise, opposition à tout moment et délai maximal de trois mois pour y donner effet restent. L’embauche bénéficiait déjà de sa règle, pas de nouveau gain. D3243-8 reste entier ; aucune réduction des cinquante ans ni de l’âge de disponibilité.',
            'Phase C : R2262-4 est seulement coordonné à l’information déjà possible par tout moyen ; R2262-1 conserve l’option de support unique proposée auparavant. Ne pas inventer une nouvelle fusion de fichiers ou un nouveau gain CRPA. L3243-5 ne corrige qu’un renvoi ordinal inexistant vers L8113-6, sans nouvelle dispense d’archives.'
        ])
        policy['reporting_social'].extend([
            'Phase C : L242-12-1 et R243-15 prennent en compte dans le calcul provisoire les seules exonérations dont conditions et montant sont établis par des informations exactes, à jour et légalement disponibles. Les données manquantes restent déclarées et le principal définitif reste identique. La prise en compte anticipée des exonérations est seulement trésorerie ; distinctement, retirer les majorations automatiques de base (25/50% et incréments5points) du I et la pénalité propre à cette taxation, y compris le relèvement8% du IV. Les pénalités autonomes de déclaration et majorations ordinaires de paiement gardent leur champ ; ne pas ressusciter une sanction propre retirée sous un autre nom. Ne pas étendre ce calcul à la contribution DOETH distincte du III. R243-15 V coordonne la dispense DSN à néant déjà proposée ; dernier mois, régularisations, emplois en cours et données annuelles dues restent.',
            'Phase C : L243-6-5 et R243-45-1 ouvrent la négociation transactionnelle pendant le recours amiable et sans saisine judiciaire, même avant mise en demeure si l’objet est identifiable. Retirer la caducité automatique à vingt jours du dossier incomplet. Garder écrit, concessions réciproques, conditions de déclaration/paiement, exclusions fraude/manœuvres dilatoires et liberté d’abandon. Supprimer aussi l’approbation particulière de transaction et les rapports annuels spécifiques, y compris R243-45-1 IV/V/VIII ; maintenir communication et contrôles légaux autonomes, sans nouveau visa de remplacement. Ne pas promettre interruption de tous délais judiciaires.',
            'Phase C : L243-6 conserve le remboursement AT-MP d’office déjà proposé par le lot automatique lorsque décision rectificative, montant et bénéficiaire sont établis. Quatre mois courent de la disponibilité légale des éléments suffisants ; conserver toutes prescriptions, totalité de la période rectifiée, droits aux prestations et recours, sans double remboursement. Classer mixed : démarche privée retirée mais traitement d’office ajouté à l’organisme, coût net inconnu ; ne pas le confondre avec un nouveau taux de cotisation.',
            'Phase C : L243-13 retire la prorogation à la seule demande de l’organisme pour les contrôles des moins de vingt salariés et indépendants. Trois mois et prorogation demandée par le cotisant demeurent, ainsi que les exceptions 1°à5°, les groupes du II, les bornes R243-59-6-A et garanties R243-59-6. Ce délai de contrôle ne doit jamais être confondu avec le préavis individuel de quinze jours.',
            'Phase C : R243-6-3 permet le changement d’interlocuteur unique par option sans deuxième autorisation, au 1er janvier suivant, sans recommencer les quatre années de régime. Garder VLU obligatoire initial et affectations L243-1-2/R243-8-1 ; même famille versement-unique-fin-autorisation que R243-8 déjà allégé, sans compter une deuxième procédure générale supprimée.',
            'Phase C : R243-11 retire la condition sans retard depuis vingt-quatre mois pour la dispense des accessoires de paiement régularisé sous trente jours ou plan respecté ; plafond et obligations déclaratives restent. R243-12 retire la répétition mensuelle pour le même défaut déclaratif, pas la pénalité initiale ni les échéances distinctes ; taux par salarié, plafond favorable cinq jours et non-cumul R243-14 restent. Ne pas confondre ces pénalités avec les cotisations.',
            'Phase C : L244-2/R243-48 reprennent des moyens de notification dont des alternatives électroniques sont déjà ouvertes par CRPA L112-15, avec accord exprès préalable du destinataire. Aucun gain supplémentaire propre aux autres supports n’est démontré : coordination_only, zéro allègement nouveau compté. Conserver réception certaine, consentement légalement requis, motif/montants/périodes, délai de régularisation et recours ; aucun simple courriel présumé reçu.'
        ])
        policy['logement'].extend([
            'Phase C logement social : L481-1-1/2 retirent les concentrations/cessions forcées et leurs contraintes non exécutées, y compris décisions anciennes définitives. Ne défaire ni contrat de cession déjà conclu ni transfert déjà exécuté, ni aide, droit acquis ou recours historique. Les opérations volontaires restent possibles ; aucune nouvelle procédure de concentration obligatoire de remplacement.',
            'Phase C : R365-1 retire les pièces organiques expressément visées dans la demande d’agrément, R365-7 l’envoi annuel prévu par ce texte. R365-6 change seulement le libellé des voies de saisine déjà ouvertes par le CRPA : coordination_only, zéro gain nouveau. Les conditions utiles, contrôles, garanties SIEG, aides et accès légaux aux données restent.',
            'Phase C : retirer l’avis régional d’agrément initial SEM, permettre un agrément territorial unique et la libre périodicité des comptes de mandat dans le champ proposé. Préserver agréments acquis, comptabilité séparée, fonds dédiés, assurance, droits des mandants, ANCOLS/CGLLS/ANAH, plafonds/réductions de loyers et protections de relogement/mobilité. Les envois ministériels annuels et avis L365-2 déjà retirés ne sont pas de nouvelles coupes.',
            'Phase C : R362-2 n’est coordonné que pour son8°, le reste de sa proposition courante est conservé. D481-5-7 ne corrige que R→D481-5-6 et article3loi1991→CPCE L111-3 1°à5°, concordance primaire lue ; aucun nouveau titre exécutoire. R481-3 garde sa plage utile après lecture des huit cibles actives et règles de commande publique. Les deux coordinations ne sont pas des simplifications matérielles nouvelles.'
        ])
        policy['substantive_outcomes_2026_10_19'].append(
            'Phase C : les propositions nouvelles sont dédupliquées par mesure ; ni les 19 gratuités fiscales maintenues, ni les 29 maintiens CCH, ni les coordinations de renvois ou droits CRPA existants ne sont autant de taxes/obligations supprimées. Une avance réduite sans baisse de dette finale est seulement trésorerie. Aucune réduction nette globale de complexité ni économie nationale n’est présumée établie.'
        )
        work=next(s for s in sites if s['slug']=='embauche')
        work['ideas'][-1]=[
            'Moins de rapports et de circuits imposés',
            'Retirer les doubles et accusés DPAE à conserver et la liste annuelle des modifications d’accords. Pour les bulletins électroniques, supprimer le raccordement obligatoire au compte personnel d’activité et le mois d’attente avant la première remise. Garder l’information préalable, le droit d’opposition, un accès gratuit et les garanties d’archivage.'
        ]
        company=next(s for s in sites if s['slug']=='entreprise')
        company['ideas'].append([
            'Moins d’obstacles dans les démarches sociales',
            'Permettre une transaction avec l’Urssaf sans devoir d’abord saisir le tribunal. Retirer la prolongation unilatérale de certains contrôles des petites entreprises et la pénalité mensuelle répétée pour un même retard déclaratif. Supprimer aussi les majorations et la pénalité propres aux calculs provisoires. Garder les exonérations connues dès ce calcul et rembourser d’office certains indus AT-MP établis ; le principal réellement dû reste inchangé.'
        ])
        company['finance']+=' Les remises d’accessoires et le traitement des remboursements d’office ont aussi un coût à évaluer. La prise en compte anticipée d’exonérations déjà acquises est un gain de trésorerie, pas une baisse de cotisations.'
        housing=next(s for s in sites if s['slug']=='logement')
        housing['ideas'][-1][1]+=' Supprimer la contribution de sécurité immobilière sur les nouvelles demandes de publication, inscription, radiation ou copie. Retirer plusieurs droits fixes de 25 € ou 125 € et le minimum général de perception de 25 €, sans toucher les exonérations ni les garanties civiles.'
        housing['ideas'].append([
            'Laisser les organismes du logement agir',
            'Retirer les concentrations et cessions forcées des sociétés d’économie mixte encore à exécuter. Alléger les pièces d’agrément, les avis et les envois annuels ciblés. Garder les aides, les contrôles des fonds et les protections des locataires.'
        ])
        housing['finance']+=' La suppression de la contribution de sécurité immobilière et des droits fixes réduit les recettes ; le service de publicité foncière continue de fonctionner. Son financement et le solde public net restent à chiffrer, sans taxe de remplacement présumée.'
        atomic(B/'policy-coordinations.json',policy);atomic(B/'site-summaries.json',sites)
        atomic(P/'activation.json',dict(activated_at=datetime.now(timezone.utc).isoformat(),
            registered_reviewed_articles=reg['registered_articles'],
            policy_sha256=sha(B/'policy-coordinations.json'),site_summaries_sha256=sha(B/'site-summaries.json'),
            national_net_savings=None,global_net_complexity_reduction='not_established',
            exhaustive_rewriting_complete=False))
print('Reviewed phase C decisions and concise site summaries activated.')
