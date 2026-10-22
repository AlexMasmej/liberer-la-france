from pathlib import Path
import json,hashlib,datetime,importlib.util,subprocess,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,data):(P/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
rp=P/'registry-proposal/records'
zzh=json.loads((rp/'LEGIARTI000049362876.json').read_text())
zzh['canonical_version_concordance_notes']='La source actuelle 49 septies ZZH, en vigueur depuis le 4 avril 2024, conserve expressément les deux renvois au JO 2010, texte 67. Ses huit paragraphes textuels correspondent au contexte de 2010, sous réserve de l’ajout actuel « ou la société de financement », qui est conservé. La table historique n’est pas importée : les tranches actuelles 1 / 2 À 4, les primes 75 / 55 points de base et la NOTA du 1er avril 2024 restent exactement celles du XML canonique. Le texte officiel du décret 2024-304, article 9, remplace seulement 3 par 4 dans l’en-tête de la dernière colonne ; l’article 12 fixe l’application aux offres du 1er avril 2024. Voir zzh-concordance.json et la preuve web.'
write('registry-proposal/records/LEGIARTI000049362876.json',zzh)
con=json.loads((P/'zzh-concordance.json').read_text())
con['2024_modification_primary_evidence']['document']='Décret n° 2024-304 du 2 avril 2024, JORF du 3 avril 2024, texte 21, NOR TREL2403702D.'
con['2024_modification_primary_evidence']['article9']='A la dernière colonne de la première ligne du tableau du neuvième alinéa de l’article 49 septies ZZH de l’annexe III au code général des impôts, le chiffre : « 3 » est remplacé par le chiffre : « 4 ».'
con['2024_modification_primary_evidence']['article12']='Les dispositions du présent décret s’appliquent aux offres de prêts émises à compter du 1er avril 2024.'
con['normalization']+=' Les indicateurs ordinaux PDF 1o et 2o sont rapprochés des 1° et 2° canoniques ; aucune valeur numérique ne change.'
write('zzh-concordance.json',con)
for slug in ['r254','zzh','d453']:
    name=slug+'-source-with-recovered-graphics.html'
    shutil.copyfile(P/name,P/'registry-proposal'/name)
for pdf in [P/'documents/joe_20160629_0150_0048.pdf',P/'documents/joe_20101231_0303_0067.pdf',P/'documents/joe_20071230_0303_0157.pdf']:
    data=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
    (P/'documents'/(pdf.stem+'-pdfinfo.txt')).write_text(data.stdout+data.stderr)
records=[json.loads(x.read_text())for x in sorted(rp.glob('*.json'))]
write('companion-record-proposals.json',records)
ready=[x for x in records if x['documentary_recovery_complete']]
write('companion-ready-index.json',{'generated_at_utc':now,'registry_root':str(P/'registry-proposal'),'activation_performed':False,'ready_count':len(ready),'records':[{'code_id':x['code_id'],'source_id':x['source_id'],'number':x['number'],'record_path':'registry-proposal/records/'+x['source_id']+'.json','record_sha256':sha(rp/(x['source_id']+'.json')),'documents':x['documents'],'media_count':len(x['media']),'documentary_recovery_complete':True,'official_jo_crosscheck_complete':True,'cryptographic_signature_validation_complete':False,'count_as_article_rewritten':False}for x in ready],'incomplete_source_ids':[x['source_id']for x in records if not x['documentary_recovery_complete']]})
spec=importlib.util.spec_from_file_location('source_assets_ro',ROOT/'source_assets.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
loaded=m.load_companions(P/'registry-proposal')
src=json.loads((P/'source-snapshot.json').read_text())
checks=[{'source_id':x['source_id'],'source_assets_schema_load_passed':True,'recovery_complete':m.recovery_complete(x['source_xml'],loaded[(x['code_id'],x['source_id'])])}for x in src]
assert sum(x['recovery_complete']for x in checks)==3
write('companion-validation.json',checks)
baseline=json.loads((ROOT/'runtime/poursuite-20261020-d/graphic-sources/source-snapshot.json').read_text());by={x['source_id']:x for x in baseline}
guards=[{'source_id':x['source_id'],'body_unchanged':x['source_xml']==by[x['source_id']]['source_xml'],'notes_unchanged':x['source_notes_xml']==by[x['source_id']]['source_notes_xml'],'whole_article_unchanged':x['raw_document_xml']==by[x['source_id']]['raw_document_xml'],'whole_article_sha256':hashlib.sha256(x['raw_document_xml'].encode()).hexdigest(),'raw_hash_matches':hashlib.sha256(x['raw_document_xml'].encode()).hexdigest()==x['source_sha256'],'companion_source_sha_matches':loaded[(x['code_id'],x['source_id'])]['source_sha256']==x['source_sha256']}for x in src]
assert all(all(v for k,v in x.items()if k not in ['source_id','whole_article_sha256'])for x in guards)
write('reference-final-guards.json',{'captured_at_utc':now,'scope':'Reference snapshot files and isolated companion records only. No active database access or assertion.','checks':guards})
report=json.loads((P/'report.json').read_text())
report.update(report_date_utc=now,source_assets_schema_validation='Cinq notices chargées ; R254-5, D453-7 et 49 septies ZZH ont recovery_complete=true ; A123-1 et article 15 restent false.',expected_markers=7,initial_missing_elements=8,missing_elements=3,unrecovered_markers=2,source_graphic_elements_recovered=5,source_graphic_elements_remaining=3,primary_normative_recoveries_completed=3,pending_parent_attempts=['Le numéro complémentaire du JO du 17 juillet 1984 est identifié mais son accès présente désormais un CAPTCHA explicite ; le parent traite la suite avec l’utilisateur. Aucun contournement par cet agent.','Les deux modèles entiers CERFA 30-0812 / 30-0813 restent non récupérés ; les documents historiques de 1960 ne sont pas promus en modèles applicables.'],ready_index='companion-ready-index.json',signature_policy='Les trois fichiers JOE_TEXTE proviennent des liens publics officiels. Aucune signature PDF incorporée n’a été trouvée et aucune validation cryptographique n’est revendiquée. La récupération documentaire officielle est vérifiée séparément.',review_copies={'r254':'registry-proposal/r254-source-with-recovered-graphics.html','zzh':'registry-proposal/zzh-source-with-recovered-graphics.html','d453':'registry-proposal/d453-source-with-recovered-graphics.html'})
write('report.json',report)
audit='''# Récupération logement et fiscalité — 22 octobre 2026 UTC

**Trois des cinq lacunes sont levées : R254-5, D453-7 et 49 septies ZZH, soit cinq formules.** La légende POS de 1984 et les deux anciens modèles CERFA restent manquants. Sept marqueurs désignaient huit éléments ; cinq marqueurs sont complétés et deux restent réservés, correspondant à trois éléments.

Les trois notices documentaires sont prêtes hors registre dans `registry-proposal/records/`. `companion-ready-index.json` donne les chemins, empreintes et pièces exactes à examiner pour une intégration distincte. `load_companions` charge les cinq notices ; `recovery_complete` est true pour les trois sources récupérées et false pour les deux autres. Les copies de lecture HTML sont placées sous `registry-proposal/`, avec leurs images relatives fonctionnelles. Elles ne constituent pas des propositions de réécriture et aucun article n’est compté réécrit par cette passe.

## Pièces officielles récupérées et réellement contrôlées

Les trois PDF entiers ont été téléchargés par le parent en navigation normale depuis les liens publics explicites **JOE_TEXTE**, puis transmis à ce dossier. La page `download/pdf` est un intermédiaire HTML, pas le PDF lui-même. Les GET directs antérieurs 403 restent au journal ; la récupération effective postérieure est documentée séparément.

| Source | Publication et étendue de lecture | PDF entier et SHA-256 |
|---|---|---|
| R254-5 | Décret 2016-855, NOR LHAL1422063D, JORF 0150 du 29 juin 2016, texte 48/130, art. 2. Les trois pages sont rendues et lues entièrement ; deux formules page 2. | `joe_20160629_0150_0048.pdf`, 198197 octets, `f5ba18bc1ae08e4b6a7a77272f3534135a3829f036cea81d42c5af9d8af2c991` |
| 49 septies ZZH | Décret 2010-1728, NOR EFIE1033033D, JORF 0303 du 31 décembre 2010, texte 67/167, art. 1. Les trois pages sont rendues et lues entièrement ; deux formules page 2. | `joe_20101231_0303_0067.pdf`, 138175 octets, `6e58b9cd2c41d76ce8c274f85c606394ab2d040931483bf62bad152f83511c14` |
| D453-7 | Décret 2007-1941, NOR MLVU0762969D, JORF 0303 du 30 décembre 2007, texte 157/191, art. 1. Les deux pages sont rendues et lues entièrement ; formule page 1. | `joe_20071230_0303_0157.pdf`, 152062 octets, `269015f17a3931e1adbd7cab09fa7920eebf9c45acefb5bf827a2edfed12bbe5` |

Les cinq images ont été exportées des objets originaux incorporés aux PDF, sans recadrage, changement de résolution ou redessin. Les pixels des PNG sont vérifiés identiques aux images PDF décodées. Les images séparées ont aussi été inspectées visuellement après export. Les extractions textuelles complètes, rendus et informations PDF sont dans `documents/` ; elles ne reconstituent pas les formules absentes de la couche texte. Les transcriptions mathématiques viennent de la lecture des images.

### R254-5 : concordance intégrale de la version pertinente

Les douze paragraphes textuels canoniques sont tous présents dans la publication après seule normalisation typographique. Les deux emplacements graphiques correspondent exactement aux deux images de la page 2. Version canonique unique depuis le 30 juin 2016, lien créateur vers le même décret, article, NOR, publication et note vide concordent.

Les expressions récupérées sont `V_N = [VL_N * (1 - (1 + t_N)^(-n))] / t_N` et `t_N = (Valeur du loyer annuel moyen au m²)_N / (Valeur de la vente moyenne au m²)_N`. Le signe *, l’exposant -n, le dénominateur t_N et les indices N des deux valeurs sont conservés. Aucun facteur 100, hypothèse de taux nul ou recalcul n’est ajouté. Voir `r254-concordance.json` et `r254-verified-provenance.json`.

### 49 septies ZZH : graphiques 2010 et paramètres actuels conservés

Les expressions exactes sont `β_t = (1 + z_t)^(-t/12)` et `Σ_(t=1)^T (1 + i)^(-t/12) = Σ_(t=1)^T β_t`. Les deux bornes 1..T, l’exposant annuel -t/12 et les indices t sont lus dans les images, sans conversion en taux mensuel ni déduction financière.

La source actuelle LEGIARTI000049362876, en vigueur depuis le 4 avril 2024, dirige expressément ses deux renvois vers ce JO 2010, texte 67. Les huit paragraphes textuels ont été rapprochés du contexte de 2010 ; l’ajout actuel « ou la société de financement » est conservé. Le tableau historique 2010 en trois tranches 75/55/35 n’est pas importé : le tableau courant 1 / 2 À 4 et 75/55 points de base, ainsi que la NOTA relative aux offres émises à compter du 1er avril 2024, restent exactement ceux du XML canonique.

Le fac-similé officiel du décret 2024-304 est lisible en texte par l’outil web sur EUR-Lex (`NIM:202406063`) : l’article 9 remplace seulement 3 par 4 dans la dernière colonne de la première ligne du tableau ; l’article 12 fixe l’application au 1er avril 2024. Son GET local a renvoyé 202 vide et sa capture PDF n’a pas réussi ; aucun téléchargement ou contrôle visuel de ce support 2024 n’est prétendu. La pièce récupérée et rendue pour les deux graphiques demeure le PDF officiel 2010. Voir `zzh-concordance.json`, `zzh-current-version-web-evidence.json` et `zzh-verified-provenance.json`.

### D453-7 : maintien de la formule et coordination 2019

Le graphique est un produit de trois facteurs : maximum de l’encours sur quatre trimestres, ratio des deux moyennes, puis encours du dernier trimestre divisé par `5 x (somme des fonds propres dédiés)`. Les deux fractions et le coefficient 5 sont conservés. Aucun signe égal ou inégalité ne figure dans l’image et aucun n’est ajouté. Le texte « plus de dix fois » du premier alinéa demeure intact.

Les onze paragraphes textuels du I concordent avec la publication 2007, sous réserve du renvoi R453-2 devenu D453-2. Le texte officiel du décret 2019-873, article 5 II 4°, identifie R453-7 par D ; l’article 6 IV 48° coordonne le renvoi et l’article 8 fixe le 1er septembre 2019. Le décret 2007 remplace seulement le I : les deux paragraphes du II actuel sont préservés intégralement depuis le XML canonique, sans prétendre les extraire de ce PDF. La note canonique est vide. Voir `d453-concordance.json`, `d453-current-version-web-evidence.json` et `d453-verified-provenance.json`.

## Origine officielle et signatures : deux vérifications distinctes

L’origine publique Légifrance, l’identité de chaque texte et son contenu sont vérifiés. Les extraits JOE_TEXTE reçus ne contiennent pas de signature numérique PDF incorporée. Le fichier 2007 possède un AcroForm vide et six annotations de navigation Link, sans champ de signature ; les deux autres n’ont pas d’AcroForm. `pdfsig` indique l’absence de signatures et signale aussi une initialisation NSS indisponible. Aucune validation cryptographique du numéro authentifié signé n’est revendiquée.

En conséquence, `documentary_recovery_complete` et `official_jo_crosscheck_complete` sont true pour les trois sources ; `cryptographic_signature_validation_complete` et, par prudence sémantique, `authenticated_jo_crosscheck_complete` restent false. La distinction est explicite et le contrat `source_assets` valide la récupération documentaire des trois notices. Les rapports `*-signature-information.json` gardent les résultats bruts.

## Deux lacunes toujours réservées

**A123-1.** Il manque l’annexe POS entière de l’arrêté du 11 mai 1984, article 2, publiée au numéro complémentaire du JO du 17 juillet 1984 : symboles, intitulés, notes et couverture complète. Un scan de ce numéro complémentaire de 20,8 Mo est identifié sur Légifrance à partir de l’arrêté SUP distinct JORFTEXT000000292388 ; le parent a ensuite rencontré un CAPTCHA explicite. Aucune légende SUP, adaptation CNIG, représentation locale de PLU ou publication de Nouvelle-Calédonie n’est substituée.

Le seul nouveau PDF Cerema récupéré par GET, `TO2441`, est la circulaire 84-35 du 18 mai 1984 relative aux projets d’intérêt général routiers. Ses neuf pages sont rendues, son texte extrait et sa première page inspectée ; il est hors objet et exclu. SHA-256 : `db8388915c44e468da7d9bc426d99facec9537484fdeb27f8f1be4c459424fb0`. Aucune lecture visuelle des neuf pages n’est revendiquée.

**Article 15, annexe IV.** Aucun modèle officiel entier CERFA 30-0812 ou 30-0813, rattachement exact de chaque numéro, éventuel verso ou concordance de version 2008 n’est vérifié. Les sources officielles retrouvées renvoient seulement aux modèles ; les tableaux Dalloz restent secondaires. La réponse ministérielle AN du 3 septembre 1960 et le compte rendu du 10 mai 1960 identifient un arrêté du 28 janvier 1960 publié au JO du 10 février 1960, page 1357 ; cela reste une piste historique et ne prouve pas les modèles applicables à la source de 2008. Aucun modèle moderne ni composition à partir des 2° et 4° n’est substitué.

## Intégrité et périmètre

Les cinq sources, notes et documents ARTICLE DILA entiers sont conservés dans `source-snapshot.json` et `canonical/`. Les empreintes et les gardes finales concordent au snapshot de référence du 20 octobre 2026. Cette passe n’accède pas à la base active et ne prétend pas en certifier l’état actuel. Aucun registre actif, politique, lot, pièce jointe active ou publication n’est modifié ; les six rédacteurs et leur configuration restent intacts.

Les GET de cet agent sont ordinaires, sans cookies ni en-têtes personnalisés. Le parent atteste des téléchargements navigateur normaux des trois PDF sans résolution de CAPTCHA ni exportation de cookies. Aucun accès intramuros, défi de protection, authentification ou achat de crédits n’est utilisé par cet agent. Les journaux conservent les échecs antérieurs au lieu de les présenter comme des téléchargements réussis. Le manifeste contient les empreintes de toutes les preuves locales.
'''
(P/'audit.md').write_text(audit)
files=[{'path':str(x.relative_to(P)),'bytes':x.stat().st_size,'sha256':sha(x)}for x in sorted(P.rglob('*'))if x.is_file()and x.name!='manifest.json']
write('manifest.json',{'captured_at_utc':now,'files':files})
print(json.dumps({'ready_companions':len(ready),'formula_images':sum(len(x['media'])for x in ready),'unrecovered_sources':5-len(ready),'source_guard_checks':25,'files_hashed':len(files),'active_state_modified':False}))
