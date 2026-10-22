import hashlib,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import source_assets as assets
from register_batches import Markup


class SourceCompanionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        (self.root/'records').mkdir();(self.root/'media').mkdir()
        self.image=self.root/'media/formula.png';self.image.write_bytes(b'local-test-image')
        self.record={'code_id':'C','source_id':'A','media':[{'path':'media/formula.png','sha256':hashlib.sha256(self.image.read_bytes()).hexdigest()}],'documents':[]}
        (self.root/'records/a.json').write_text(json.dumps(self.record))

    def tearDown(self):self.tmp.cleanup()

    def test_rejects_remote_traversal_and_unregistered_paths(self):
        for value in ['https://example.com/x.png','../secret','media/missing.png','media/../records/a.json']:
            with self.subTest(value=value),self.assertRaises(ValueError):assets.verified_image(value,self.root)

    def test_checks_content_hash_before_accepting_companion(self):
        self.assertEqual(assets.verified_image('media/formula.png',self.root),self.image)
        self.image.write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):assets.load_companions(self.root)

    def test_only_registered_local_image_survives_sanitization(self):
        lookup=lambda value:assets.verified_image(value,self.root)
        with patch.object(assets,'verified_image',side_effect=lambda value: assets.asset_path(value,self.root) if value=='media/formula.png' else (_ for _ in ()).throw(ValueError())):
            result=assets.safe_html('<img src="media/formula.png" alt="Formule &quot;K&quot;" onerror="alert(1)"><img src="https://example.com/x" alt="X">')
        self.assertEqual(result,'<img src="media/formula.png" alt="Formule &quot;K&quot;">')

    def test_draft_validator_rejects_event_handlers_and_missing_alt(self):
        for body in ['<img src="media/formula.png">','<img src="media/formula.png" alt="K" onerror="x()">','<img src="https://example.com/x" alt="K">']:
            with self.subTest(body=body),self.assertRaises(ValueError):Markup().feed(body)

    def test_omitted_norms_are_distinguished_from_ordinary_facsimile_requirements(self):
        self.assertEqual(len(assets.graphic_markers('<p>Formule non reproduite : vous pouvez la consulter au JO.</p>')),1)
        self.assertEqual(assets.graphic_markers("<p>Le dossier comprend le fac-similé d'un billet.</p>"),[])

    def test_manifest_cannot_claim_completion_with_a_missing_formula(self):
        body='<p>Vous pouvez consulter la formule au JO.</p><p>Formule non reproduite.</p>'
        record={'expected_markers':2,'documentary_recovery_complete':True,'documents':[{'path':'source.pdf'}],'transcriptions':[{'marker':1,'text':'K = R/N'}]}
        self.assertFalse(assets.recovery_complete(body,record))
        record['transcriptions'].append({'marker':2,'text':'T = R × N'})
        self.assertTrue(assets.recovery_complete(body,record))
        self.assertFalse(assets.recovered_content_present('<p>K = R/N</p>',record))
        self.assertTrue(assets.recovered_content_present('<p>K = R/N</p><p>T = R × N</p>',record))


if __name__=='__main__':unittest.main()
