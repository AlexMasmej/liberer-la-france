import unittest,tempfile,tarfile,io,gzip,sqlite3,json
from pathlib import Path
from ingest import open_db,import_archive,inventory,export_snapshot,source_notes,source_evidence

CODE='LEGITEXT000006072050'
def doc(i,kind,body):
    return f'<{kind}><META><META_COMMUN><ID>{i}</ID></META_COMMUN></META>{body}</{kind}>'.encode()
def article(i,number,start,end,text):
    return f'<ARTICLE><META><META_COMMUN><ID>{i}</ID></META_COMMUN><META_SPEC><META_ARTICLE><NUM>{number}</NUM><DATE_DEBUT>{start}</DATE_DEBUT><DATE_FIN>{end}</DATE_FIN><ETAT>VIGUEUR</ETAT></META_ARTICLE></META_SPEC></META><BLOC_TEXTUEL><CONTENU><p>{text}</p><table><tr><td>A</td><td>B</td></tr></table></CONTENU></BLOC_TEXTUEL></ARTICLE>'.encode()
class ImportTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.db=open_db(self.root/'test.sqlite')
 def tearDown(self):self.db.close();self.tmp.cleanup()
 def archive(self,name,docs):
  path=self.root/name
  with tarfile.open(path,'w:gz') as t:
   for key,value in docs.items():
    item=tarfile.TarInfo(f'../../not-extracted/{CODE}/{key}.xml');item.size=len(value);t.addfile(item,io.BytesIO(value))
  return path
 def docs(self):return {
  'root':doc(CODE,'TEXTELR','<STRUCT><LIEN_SECTION_TA id="S1" debut="2020-01-01" fin="2999-01-01">Législatif</LIEN_SECTION_TA></STRUCT>'),
  'S1':b'<SECTION_TA><ID>S1</ID><STRUCTURE_TA><LIEN_ART id="A1" debut="2020-01-01" fin="2999-01-01"/></STRUCTURE_TA></SECTION_TA>',
  'A1':article('A1','L1','2020-01-01','2999-01-01','Texte source')}
 def test_lossless_versioned_inventory(self):
  path=self.archive('base.gz',self.docs());import_archive(self.db,path,'https://echanges.dila.gouv.fr/official-base.tar.gz')
  self.assertEqual(inventory(self.db,CODE,'2026-10-18')['article_ids'],['A1'])
  self.assertIn('<table>',self.db.execute('SELECT content_xml FROM articles').fetchone()[0])
  self.assertEqual(self.db.execute('SELECT name FROM archives').fetchone()[0],'official-base.tar.gz')
  self.assertFalse((self.root/'not-extracted').exists())
 def test_truncation_rolls_back(self):
  path=self.archive('bad.gz',self.docs());path.write_bytes(path.read_bytes()[:-8])
  with self.assertRaises((EOFError,tarfile.ReadError)):import_archive(self.db,path,'https://example.com/bad.gz')
  self.assertEqual(self.db.execute('SELECT count(*) FROM articles').fetchone()[0],0)
 def test_missing_and_out_of_date_articles_are_visible(self):
  docs=self.docs();del docs['A1'];path=self.archive('base.gz',docs);import_archive(self.db,path,'https://example.com/base.gz')
  self.assertEqual(inventory(self.db,CODE,'2026-10-18')['missing_articles'],['A1'])
 def test_stale_draft_is_not_published(self):
  path=self.archive('base.gz',self.docs());import_archive(self.db,path,'https://example.com/base.gz')
  self.db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',(CODE,'A1','incorrect-source-hash','reviewed','Changed','reason','review'));self.db.commit()
  export_snapshot(self.db,'2026-10-18',self.root/'export')
  r=json.loads((self.root/'export/travail.json').read_text())[0]
  self.assertEqual(r['status'],'source_changed_review_required');self.assertIsNone(r['proposed_xml'])
 def test_metadata_only_update_keeps_exact_body_draft(self):
  path=self.archive('base.gz',self.docs());import_archive(self.db,path,'https://example.com/base.gz')
  body,start,end=self.db.execute('SELECT content_xml,valid_from,valid_until FROM articles').fetchone()
  self.db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',(CODE,'A1','old-metadata-hash','rewrite_draft','<p>Proposition</p>','reason','review'))
  self.db.execute('INSERT INTO draft_sources VALUES(?,?,?,?,?)',(CODE,'A1',body,start,end));self.db.commit()
  export_snapshot(self.db,'2026-10-18',self.root/'export')
  r=json.loads((self.root/'export/travail.json').read_text())[0]
  self.assertEqual(r['status'],'rewrite_draft');self.assertEqual(r['proposed_xml'],'<p>Proposition</p>')
 def test_application_note_change_requires_draft_review(self):
  docs=self.docs();docs['A1']=docs['A1'].replace(b'</ARTICLE>',b'<NOTA><CONTENU><p>Condition A</p></CONTENU></NOTA></ARTICLE>')
  path=self.archive('base.gz',docs);import_archive(self.db,path,'https://example.com/20260101.tar.gz')
  body,start,end=self.db.execute('SELECT content_xml,valid_from,valid_until FROM articles').fetchone()
  self.db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',(CODE,'A1','old-hash','rewrite_draft','<p>Proposition</p>','reason','review'))
  self.db.execute('INSERT INTO draft_sources VALUES(?,?,?,?,?)',(CODE,'A1',source_evidence(body,source_notes(self.db,CODE,'A1')),start,end));self.db.commit()
  docs['A1']=docs['A1'].replace(b'Condition A',b'Condition B')
  path=self.archive('update.gz',docs);import_archive(self.db,path,'https://example.com/20260102.tar.gz')
  export_snapshot(self.db,'2026-10-18',self.root/'export')
  r=json.loads((self.root/'export/travail.json').read_text())[0]
  self.assertEqual(r['status'],'source_changed_review_required');self.assertIsNone(r['proposed_xml'])
if __name__=='__main__':unittest.main()
