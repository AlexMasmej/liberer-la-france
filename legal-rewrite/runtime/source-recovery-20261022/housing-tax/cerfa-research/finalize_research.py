"""Finalize evidence in this isolated research folder; never alter corpus or companions."""
from pathlib import Path
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
NOW = datetime.now(timezone.utc).isoformat()
def sha(data): return hashlib.sha256(data).hexdigest()
def write(name, value):
    (BASE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

history = json.loads((BASE / 'version-history.json').read_text())
versions = history['versions']
guards = []
for row in versions:
    path = BASE / row['xml_file']
    raw = path.read_bytes()
    root = ET.fromstring(raw)
    digest = sha(raw)
    assert digest == row['source_sha256'] == row['document_sha256']
    assert root.findtext('.//ID') == row['id']
    guards.append({
        'id': row['id'], 'xml_file': row['xml_file'], 'sha256': digest,
        'source_sha256_equals_document_sha256_equals_saved_xml_sha256': True,
        'archive': row['archive'], 'document_archive': row['document_archive'],
        'content_xml_sha256': sha(row['content_xml'].encode()),
        'notes_xml_sha256': sha(row['notes_xml'].encode()),
        'notes_xml_exact': row['notes_xml'],
        'valid_from_as_supplied': row['valid_from'],
        'valid_until_as_supplied': row['valid_until'],
        'state_as_supplied': row['state'],
    })
write('source-guards.json', {
    'verified_at_utc': NOW, 'checked_against': 'isolated snapshot values captured in version-history.json',
    'live_database_read_or_modified_by_this_finalizer': False,
    'all_saved_xml_bytes_match_snapshot_source_and_document_hashes': True,
    'records': guards,
})

pdfs = [
    {'file': 'documents/an1960-05-10-curl.pdf',
     'url': 'https://archives.assemblee-nationale.fr/1/cri/1959-1960-ordinaire2/012.pdf',
     'bytes_expected': 1706459, 'pdf_page': 13, 'printed_page': '755',
     'render': 'documents/an1960-05-10-page13.png',
     'identity': 'Assemblée nationale, 2e séance du 10 mai 1960, réponse à la question écrite 3805',
     'proves': 'Renvoi contemporain à l’arrêté du 28 janvier 1960, Journal officiel du 10 février 1960, page 1357 ; la contexture des relevés a été aménagée pour les revenus de 1960.',
     'does_not_prove': 'Aucune image de formulaire, numéro CERFA, révision, recto/verso ni identité avec les modèles de 2008.'},
    {'file': 'documents/an1960-09-03.pdf',
     'url': 'https://archives.assemblee-nationale.fr/1/qst/1-qst-1960-09-03.pdf',
     'bytes_expected': 3684367, 'pdf_page': 30, 'printed_page': '2348',
     'render': 'documents/an1960-09-03-page30.png',
     'identity': 'Assemblée nationale, questions écrites du 3 septembre 1960, réponse à la question 5817',
     'proves': 'Pour 1960, l’arrêté distingue A dividendes et revenus assimilés, B intérêts et produits d’obligations, C distributions des sociétés d’investissement et assimilées, D revenus exonérés. La réponse explique le contrôle et les crédits correspondants.',
     'does_not_prove': 'Aucune image de formulaire, numéro CERFA, révision, recto/verso ni identité avec les modèles de 2008.'},
]
for item in pdfs:
    path = BASE / item['file']
    raw = path.read_bytes()
    assert raw[:5] == b'%PDF-' and len(raw) == item.pop('bytes_expected')
    item.update(bytes=len(raw), sha256=sha(raw), downloaded_at_utc_date='2026-10-22',
                http_status=200, content_type='application/pdf',
                method='ordinary public system curl GET, redirects followed, normal certificate verification, no cookies or authentication')
    info = subprocess.check_output(['pdfinfo', str(path)], text=True)
    info_path = path.with_suffix('.pdfinfo.txt')
    info_path.write_text(info)
    item['metadata_file'] = str(info_path.relative_to(BASE))
    text_path = path.with_suffix('.txt')
    assert text_path.is_file()
    pages = text_path.read_text().split('\f')
    selected = pages[item['pdf_page'] - 1]
    selected_path = path.with_name(path.stem + '-page' + str(item['pdf_page']) + '.extraction.txt')
    selected_path.write_text(selected)
    item['full_extraction'] = str(text_path.relative_to(BASE))
    item['selected_page_extraction'] = str(selected_path.relative_to(BASE))
    item['full_relevant_page_rendered_and_visually_inspected'] = True
    item['inspection_date_utc'] = '2026-10-22'
    item['ocr_is_imperfect_original_scan_controls_reading'] = True
    item['render_sha256'] = sha((BASE / item['render']).read_bytes())
    item['signature_validation_claimed'] = False
write('official-pdf-evidence.json', {'verified_at_utc': NOW, 'documents': pdfs})

events = [
    {'date': '1960-01-28', 'document': 'Arrêté du 28 janvier 1960, JO du 10 février 1960, p.1357',
     'evidence': ['official-pdf-evidence.json', 'documents/an1960-05-10-page13.png', 'documents/an1960-09-03-page30.png'],
     'verified_scope': 'Existence, date/publication et description contemporaine des catégories A/B/C/D établies à partir de 1960.',
     'primary_act_facsimile_obtained': False, 'full_models_obtained': False,
     'limit': 'Les réponses ministérielles sont des preuves officielles du renvoi, pas les annexes graphiques ni une concordance CERFA.'},
    {'date': '1982-12-30', 'article_version': 'LEGIARTI000006301208',
     'verified_scope': 'Texte XML : 1° renvoie aux modèles sans numéro ; 3° vise encore les coupons crédités en compte ; 4° vise 2° et 3° ; abattements 5000 F et 3000 F.',
     'modifier_links_as_supplied': 'Lois 77-1467, art.67, et 82-1126, art.6 ; arrêté de codification du 6 octobre 1983.',
     'full_models_obtained': False},
    {'date': '1985-02-15', 'article_version': 'LEGIARTI000006301209',
     'verified_scope': 'Différence canonique : le 3° devient sans objet et le 4° ne vise plus que le 2°.',
     'modifier': 'Décret n°85-201 du 13 février 1985, art.4, JO15 février1985, JORFTEXT000000703495 ; arrêté de codification du24septembre1985.',
     'modifier_text_status': 'Référence établie par le XML original ; le texte de l’acte n’a pas été récupéré dans cette passe.',
     'limit': 'Ne pas reprendre la date du19février donnée par une piste secondaire ; ne pas déduire quel numéro CERFA correspond à un coupon crédité en compte.',
     'full_models_obtained': False},
    {'date': '1994-09-02', 'article_version': 'LEGIARTI000006301210',
     'verified_scope': 'Le 4°a renvoie à l’abattement du troisième alinéa du3 de l’article158, sans montants fixes ; 1° inchangé.',
     'modifier': 'Arrêté17octobre1994, NOR BUDF9400019A, art.1, JORFTEXT000000165661, JO19octobre1994.',
     'url': 'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000165661',
     'primary_web_text_read': True,
     'limit': 'L’acte officiel cite la loi87-416 du17juin1987, art.28I. Le lien de modification du XML ancien la qualifie par erreur de décret. La note(1) appelée dans le corps de cette version n’est pas renseignée dans sa NOTA XML.',
     'full_models_obtained': False},
    {'date': '2002-01-01', 'article_version_observed': 'LEGIARTI000006301211',
     'snapshot_edition_date': '2002-03-31',
     'verified_scope': 'Arrêté3septembre2001, art.2IIa : contre-valeur en francs devient contre-valeur en euros ; art.8 : entrée1janvier2002. La version conservée du31mars2002 mentionne pour la première fois dans les sept XML les numéros30-0812/30-0813, en précisant qu’ils ne sont pas reproduits.',
     'modifier': 'Arrêté3septembre2001, NOR ECOZ0100005A, JORFTEXT000000591461, JO11septembre2001.',
     'url': 'https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000591461/2025-03-22',
     'primary_web_text_read': True,
     'limit': 'Le texte de l’acte ne crée ni ne renumérote les modèles. La première mention numérique dans le stock ne date donc pas leur création. Intervalle1janvier→31mars2002 absent des bornes conservées ; ne pas le combler par inférence.',
     'full_models_obtained': False},
    {'date': '2005-01-01', 'article_version': 'LEGIARTI000006301212',
     'verified_scope': 'Différence canonique : suppression de l’avoir fiscal au4°d, seul crédit d’impôt conservé ; 1° garde les deux numéros et la mention non reproduits. Le rappel de note relatif aux revenus1996 disparaît.',
     'modifier': 'Arrêté30décembre2004, NOR BUDF0400065A, art.1II, JORFTEXT000000424317, JO31décembre2004 texte106 ; reproduit dans BOI5I-2-05 du11août2005, annexe4, p.41.',
     'url': 'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000424317',
     'official_republication_url': 'https://bofip-archives.impots.gouv.fr/bofip/25904-AIDA.html/identifiant%3D-20050811',
     'official_pdf_url': 'https://www11.minefi.gouv.fr/boi/boi2005/5fppub/textes/5i205/5i205.pdf',
     'primary_publication_metadata_and_official_indexed_republication_text_read': True,
     'primary_local_pdf_obtained': False,
     'access_limit': 'Acte JORF : cache miss du lecteur web. La recherche publique retrouve le texte exact dans deux publications ministérielles. GET PDF Minefi : HTTP503 HTML107octets, conservé comme réponse et non comme PDF.',
     'full_models_obtained': False},
    {'date': '2008-09-18', 'article_version': 'LEGIARTI000019493914',
     'verified_scope': 'Arrêté15septembre2008, art.1a : suppression des mots relatifs à la déduction des seuls frais d’encaissement au4°a. Le 1° n’est pas modifié et garde les numéros30-0812/30-0813, non reproduits. NOTA actuelle vide.',
     'modifier': 'Arrêté15septembre2008, NOR BCFL0818512A, art.1a, JORFTEXT000019491882, JO17septembre2008 texte29.',
     'url': 'https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019491882',
     'primary_web_text_read': True, 'full_models_obtained': False},
]
write('normative-version-map.json', {
    'generated_at_utc': NOW, 'code_id': 'LEGITEXT000006069576', 'article_number': '15',
    'model_graphic_version_identity_verified': False,
    'first_explicit_cerfa_numbers_in_preserved_xml': 'LEGIARTI000006301211',
    'first_explicit_reference_does_not_prove_form_creation_date': True,
    'events': events,
    'data_anomalies': [
        'LEGIARTI000006301207 : état MODIFIE_MORT_NE, début1979-07-01 postérieur à fin1977-12-31. Conservé comme preuve de contenu, sans intervalle juridique déduit.',
        'Les bornes du stock ne donnent pas une chaîne continue avant1982 ni du1janvier au31mars2002 ; aucune version non présente n’a été inventée.',
        'L’identité des numéros avec les deux anciennes fonctions guichet/correspondance et compte reste inconnue.',
    ],
    'contextual_official_doctrine': {
        'url': 'https://bofip-archives.impots.gouv.fr/bofip/27494-AIDA.html/identifiant=4J1342-19951101',
        'date': '1995-11-01',
        'scope': 'La sous-section4J1342 renvoie le modèle à l’annexe de l’article15 et indique le passage à une déclaration annuelle unique depuis1987 ; le texte n’est pas une image des modèles. Il ne permet pas de substituer un imprimé IFU moderne.',
    },
})

missing = [
    {'reference': 'CERFA30-0812', 'full_official_graphic_model_obtained': False,
     'missing': ['Imprimé officiel complet identifiable par son numéro et titre.', 'Toutes faces/pages, notices et annexes appartenant au modèle.', 'Indice ou date de révision et preuve de version applicable au texte2008.', 'Concordance avec l’éventuel modèle publié en1960 et les changements ultérieurs.']},
    {'reference': 'CERFA30-0813', 'full_official_graphic_model_obtained': False,
     'missing': ['Imprimé officiel complet identifiable par son numéro et titre.', 'Toutes faces/pages, notices et annexes appartenant au modèle.', 'Indice ou date de révision et preuve de version applicable au texte2008.', 'Concordance avec l’éventuel modèle publié en1960 et les changements ultérieurs.']},
]
write('report.json', {
    'generated_at_utc': NOW, 'scope': 'complément de recherche CERFA, sans activation ni modification de texte',
    'status': 'textual_history_documented_graphic_models_not_recovered',
    'source_id': 'LEGIARTI000019493914', 'code_id': 'LEGITEXT000006069576',
    'source_xml_sha256': next(x['source_sha256'] for x in versions if x['id']=='LEGIARTI000019493914'),
    'historical_saved_xml_count': 6, 'current_saved_xml_count': 1,
    'all_saved_xml_hashes_match_snapshot': True,
    'official_pdfs_obtained_and_relevant_full_pages_visually_read': 2,
    'official_full_graphical_forms_recovered': 0, 'remaining_form_models': 2,
    'documentary_recovery_complete': False, 'ready_for_companion_activation': False,
    'official_model_identity_1960_to_2008_verified': False,
    'no_missing_image_was_replaced_by_inferred_text_or_a_modern_form': True,
    'newly_verified_primary_act_texts': ['Arrêté17octobre1994, art.1, version1994', 'Arrêté3septembre2001, art.2IIa et8, version2002', 'Arrêté15septembre2008, art.1a, version2008'],
    'official_republication_indexed_text': 'Arrêté30décembre2004, art.1II, BOI5I-2-05 annexe4 ; pas de PDF local récupéré.',
    'missing_graphics': missing,
    'access_outcomes': [
        {'resource': '2 PDF AN', 'initial_python_client': 'local TLS issuer certificate validation error', 'normal_system_curl_result': 'HTTP200 PDF ; no certificate check disabled'},
        {'resource': 'Acte2004 JORFTEXT000000424317', 'web_reader': 'cache miss ; not evidence of remote HTTP403'},
        {'resource': 'PDF Minefi5I-2-05', 'http_status': 503, 'content_type': 'text/html; charset=iso-8859-1', 'bytes': 107, 'body_saved': 'responses/boi5i205-http503.html'},
        {'resource': 'Models30-0812/30-0813', 'result': 'Public official searches and historical text routes did not yield identifiable complete graphics ; absence of search results is not proof of unavailability.'},
        {'resource': 'Protected scans followed by parent', 'result': 'Parent reports pending user authorization for4scans. No protected scan accessed or challenge attempted by this research pass.'},
    ],
    'unresolved_leads': ['JO10février1960p1357 et éventuelles pages annexées : acte et modèles originaux encore à obtenir.', 'Actes1938/1961/1964/1965/1977 mentionnés par une source secondaire : liens de modification des modèles non établis dans cette passe.', 'Archives administratives des modèles CERFA, avec indice/date et tableaux de concordance : aucune pièce graphique trouvée.'],
    'no_state_mutation': ['No live DB writes or article registrations.', 'No active companion records, batches, attachments, policies, writer processes or coordinator slots changed.', 'Only cerfa-research files written during this follow-up.'],
    'artifacts': ['audit.md', 'normative-version-map.json', 'version-history.json', 'version-diffs.json', 'source-guards.json', 'official-pdf-evidence.json', 'web-research-evidence.json', 'web-modifier2004-evidence.json'],
})

manifest = []
for path in sorted(BASE.rglob('*')):
    if path.is_file() and path.name != 'manifest.json':
        raw=path.read_bytes()
        manifest.append({'path':str(path.relative_to(BASE)), 'bytes':len(raw), 'sha256':sha(raw)})
write('manifest.json', {'generated_at_utc': NOW, 'files': manifest})
print(json.dumps({'xml_versions_guarded':len(guards), 'official_pdfs_read':len(pdfs), 'full_models_recovered':0, 'remaining_models':2, 'files_manifested':len(manifest)}, ensure_ascii=False))
