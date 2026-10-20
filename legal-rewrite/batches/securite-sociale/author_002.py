"""Full C3S texts: remove future liability, preserve historic liquidation rules.

All sixteen source articles and application notes were read before authoring.
The old calculation text is deliberately preserved for historic liabilities.
This is a substantive temporal-scope reform, not a cosmetic bulk rewrite.
"""
from pathlib import Path
import html,json,re
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
source=json.loads((ROOT/'sites/liberer-la-retraite/dist/corpus/securite-sociale.json').read_text())
by_number={a['number']:a for a in source}
records=[]
assessments={
'L137-31':'Conserve toutes les catégories exonérées, les numéros abrogés 6° et 9°, les champs d’activité et les renvois aux codes de la construction, monétaire et financier et aux lois spéciales.',
'L137-32':'Conserve le fait générateur au 1er janvier, le taux de 0,16 %, l’abattement de 19 millions, l’exigibilité au 15 mai, les plafonnements, les refacturations et toutes les exclusions de chiffre d’affaires. Le premier alinéa reste le premier alinéa pour les renvois des autres articles.',
'L137-33':'Conserve la déclaration hors taxes, les régimes bancaire/assurance, les quatre conditions cumulatives des commissionnaires, les règles pharmaceutiques de 2 500 euros, la dispense sous abattement et la taxation provisionnelle. Aucun alinéa n’est ajouté ou retiré afin de préserver les renvois aux cinquième à neuvième alinéas et à l’avant-dernier alinéa.',
'L137-34':'Conserve les quatre parties, les délais de soixante et trente jours, l’interruption de reprise, la majoration plafonnée à 5 %, le contradictoire et l’interdiction de recouvrer avant expiration du délai. La limitation temporelle est insérée dans le I sans déplacer les alinéas du II ou du IV.',
'L137-35':'Conserve la date du 15 mai, la télédéclaration et le télérèglement, et les deux majorations distinctes de 0,2 %. Le premier alinéa demeure la cible du renvoi du troisième alinéa.',
'L137-36':'Conserve les deux parties : défaut déclaratif et rectification, chacune dans la limite de 10 %. Les droits de reprise et les règles d’application dans le temps des sanctions restent à contrôler.',
'L137-37':'Conserve la majoration initiale plafonnée à 10 % et la majoration supplémentaire plafonnée à 4,8 % par année ou fraction au-delà d’un an de retard. La suppression ne crée pas de nouvelle majoration pour une période sans dette.',
'L137-38':'Conserve le champ exact des majorations utilisables lors de la taxation provisionnelle : L. 137-35, I de L. 137-36 et L. 137-37 ; le II de L. 137-36 n’est pas ajouté.',
'D137-30':'Conserve le seuil de marge de 4 %, le plafond de contribution de 3,08 %, le critère de plus de la moitié des achats ou ventes hors de France, les cinq postes et la non-déduction du déficit. Les reprises restent déductibles seulement à concurrence des charges déjà retenues.',
'D137-31':'Conserve le champ agricole/cooperatives, les seuils de 4 % et 3,08 %, la prise en compte de seulement 20 % des salaires, les cinq postes de marge et la règle du déficit et des reprises.',
'D137-32':'Conserve les activités combustibles/carburants, les seuils de 4 % et 3,08 %, les 20 % de salaires retenus, les autres composantes de la marge et la limite des reprises.',
'D137-33':'Conserve l’autorité du directeur, le délai d’un mois après notification, le recouvrement comme la contribution et la modulation limitée à L. 137-34 et L. 137-36 à L. 137-37. Le L. 137-35 n’entre pas dans la faculté de modulation.',
'D137-34':'Conserve l’information de l’organisme après rectification fiscale et le supplément éventuel à verser sous trois mois ; en cas de contestation, le point de départ reste la notification de la décision définitive.',
'D137-35':'Conserve la dette du successeur en cas de fusion/absorption et le maintien de la dette sur le chiffre d’affaires antérieur à un changement de forme. Un fait générateur postérieur à la suppression ne peut renaître du seul fait d’une restructuration.',
'D137-36':'Conserve l’exigibilité anticipée en cas de cessation, cession totale ou dissolution entre le 1er janvier et l’échéance annuelle, sur le chiffre d’affaires de l’année précédente ; limitée aux contributions dont le fait générateur précède la suppression.'
}
main=by_number['L137-30']
body=main['source_xml']
old='<p>Il est institué une contribution sociale de solidarité à la charge : </p>'
assert old in body
body=body.replace(old,'<p>I. — Pour les faits générateurs antérieurs à la date de suppression définie au II, la contribution sociale de solidarité à la charge des sociétés s’applique aux personnes suivantes :</p>',1)
body+='''<p>II. — La contribution est supprimée pour les faits générateurs intervenant à compter du 1er janvier d’une année fixée par une loi de financement de la sécurité sociale.</p><p>Cette loi évalue la perte de recettes pour l’année de suppression et les années suivantes et prévoit sa compensation durable à l’assurance vieillesse, ou les réductions de dépenses récurrentes qui la financent. Les recettes seulement espérées d’une croissance supplémentaire et les produits de cessions d’actifs ne sont pas réputés constituer un financement récurrent. Une économie déjà affectée à une autre réforme ne peut être comptabilisée une seconde fois.</p><p>III. — Les contributions dont le fait générateur est antérieur à la date de suppression, ainsi que leurs majorations et accessoires, demeurent régies par les dispositions applicables à ce fait générateur. La suppression ne fait obstacle ni à leur contrôle ou à leur recouvrement, ni aux réclamations, restitutions et recours qui s’y rapportent. Elle ne réduit pas, par elle-même, les droits à pension des assurés.</p>'''
records.append({k:main[k] for k in ['code_id','source_id','source_sha256','number']}|{'proposed_xml':body,'reason':'Changement de fond : suppression de la C3S pour les nouveaux faits générateurs à une date fixée par une LFSS financée. La liste complète des redevables est maintenue pour les faits générateurs antérieurs, sans remise implicite des dettes anciennes. Il ne s’agit pas d’un simple changement de taux ou d’un résumé.','review_notes':'Évaluer le rendement perdu et le calendrier réel de compensation ; aucun montant n’est inventé. Le fait générateur annuel du 1er janvier, et non la seule année du chiffre d’affaires d’assiette, délimite la transition. Contrôler la compatibilité organique de la condition de financement et la portée des règles de sanctions plus douces. Les codes fiscaux et les textes hors CSS doivent supprimer les renvois créateurs de nouvelle dette tout en conservant le traitement des périodes anciennes.'})
for number,review in assessments.items():
 a=by_number[number]
 clause='Le présent article ne s’applique qu’aux contributions dont le fait générateur est antérieur à la date de suppression fixée au II de l’article L. 137-30. '
 body=a['source_xml']
 if '<p>' in body:
  body=body.replace('<p>','<p>'+clause,1)
 else:
  # These three sources contain one paragraph separated only by HTML breaks.
  assert number in {'L137-37','D137-34','D137-36'}
  plain=html.unescape(re.sub('<[^>]*>',' ',body))
  body='<p>'+clause+html.escape(' '.join(plain.split()))+'</p>'
 records.append({k:a[k] for k in ['code_id','source_id','source_sha256','number']}|{'proposed_xml':body,'reason':'Coordination de fond de la suppression de C3S : le champ temporel de l’article est limité aux faits générateurs antérieurs à la date fixée par L. 137-30. Le texte entier des règles de liquidation, protection ou contrôle est conservé pour ces dettes historiques ; il n’est pas prétendu reformulé à droit constant.','review_notes':review+' Conserver les notes officielles avec la source ; la date d’application historique de cette source n’est pas la date de la suppression proposée. Les garanties, prescriptions et règles d’application des sanctions dans le temps ne sont pas écartées.'})
target=HERE/'002.json';temp=target.with_suffix('.json.tmp');temp.write_text(json.dumps(records,ensure_ascii=False,indent=2));temp.replace(target)
print(len(records),'complete C3S article proposals with substantive temporal coordination.')
