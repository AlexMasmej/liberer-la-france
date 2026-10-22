"""Create an explicitly labelled local extract from unaltered original scan pixels.

Four complete legend portions, original order. No OCR layer, unrelated page,
hidden cropped content, recreated symbol, retouch, rotation or resampling.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (NameObject, NumberObject, ArrayObject, DictionaryObject,
                           DecodedStreamObject)

BASE=Path(__file__).resolve().parent
REG=BASE/'registry-proposal'
spec=json.loads((BASE/'crop-specification.json').read_text())
digest=lambda data:hashlib.sha256(data).hexdigest()
writer=PdfWriter()
for i,item in enumerate(spec):
    source=Image.open(BASE/item['source_path'])
    crop=source.crop(item['crop_box_pixels_left_top_right_bottom'])
    profile=(BASE/'documents'/f"page{item['page']}-image-color-profile.icc").read_bytes()
    target=REG/item['path']
    crop.save(target,icc_profile=profile)
    check=Image.open(target)
    assert check.size==crop.size and check.mode==crop.mode and check.tobytes()==crop.tobytes()
    assert check.info['icc_profile']==profile
    item['sha256']=digest(target.read_bytes())
    item['icc_sha256']=digest(profile)
    item['decoded_pixel_sha256']=digest(crop.tobytes())
    item['icc_profile_preserved']=True
    width,height=crop.size
    # Original scan resolution: 200 dpi, exact integer pixels unchanged.
    w,h=width*72/200,height*72/200
    page=writer.add_blank_page(w,h)
    icc=DecodedStreamObject();icc.set_data(profile)
    icc.update({NameObject('/N'):NumberObject(3),NameObject('/Alternate'):NameObject('/DeviceRGB')})
    icc_ref=writer._add_object(icc.flate_encode())
    img=DecodedStreamObject();img.set_data(crop.tobytes())
    img.update({NameObject('/Type'):NameObject('/XObject'),NameObject('/Subtype'):NameObject('/Image'),
                NameObject('/Width'):NumberObject(width),NameObject('/Height'):NumberObject(height),
                NameObject('/BitsPerComponent'):NumberObject(8),
                NameObject('/ColorSpace'):ArrayObject([NameObject('/ICCBased'),icc_ref])})
    img_ref=writer._add_object(img.flate_encode())
    page[NameObject('/Resources')]=DictionaryObject({NameObject('/XObject'):DictionaryObject({NameObject('/Im1'):img_ref})})
    stream=DecodedStreamObject();stream.set_data(f'q\n{w:.8f} 0 0 {h:.8f} 0 0 cm\n/Im1 Do\nQ\n'.encode())
    page[NameObject('/Contents')]=writer._add_object(stream.flate_encode())
    writer.add_outline_item(f"Extrait POS - page originale {item['printed_page']} - lignes {item['row_range'][0]} a {item['row_range'][1]}",i)

whole_sha='1c7710e196cb6845326ecaa00eda9580ba69cd0a6538e1aac7784d36c1e696ed'
writer.add_metadata({
    '/Title':'EXTRAIT LOCAL - Annexe POS de l’arrete du 11 mai 1984 - JORF NC 17 juillet 1984, p.6186-6189',
    '/Author':'Extraction documentaire locale de scans officiels DILA / Legifrance',
    '/Subject':'Extrait image de l’annexe seule, 40 entrees. Pages PDF originales 14-17. Recadrages verticaux p.6186 et6189 ; pixels, couleurs sRGB et ordre conserves ; aucune recomposition. JO entier SHA256 '+whole_sha,
    '/Keywords':'EXTRAIT LOCAL ; A123-1 ; POS ; 40 entrees ; exclut legende SUP ; JORF_NC_19840717_165.pdf ; SHA256 '+whole_sha,
    '/Creator':'create_excerpt.py - lossless original-pixel documentary extraction; no OCR or redrawing',
})
output=REG/'documents/extrait-annexe-pos-19840717-p6186-6189.pdf'
with output.open('wb') as f:writer.write(f)
read=PdfReader(output)
assert len(read.pages)==4 and not read.trailer['/Root'].get('/AcroForm')
checks=[]
for i,(page,item) in enumerate(zip(read.pages,spec),1):
    assert not page.get('/Annots')
    images=list(page.images);assert len(images)==1
    im=images[0].image
    expected=Image.open(REG/item['path'])
    assert im.mode==expected.mode and im.size==expected.size and im.tobytes()==expected.tobytes()
    assert not page.extract_text().strip()
    obj=page['/Resources']['/XObject']['/Im1'].get_object()
    assert digest(obj['/ColorSpace'][1].get_object().get_data())==item['icc_sha256']
    checks.append({'excerpt_page':i,'original_pdf_page':item['page'],
                   'original_printed_page':item['printed_page'],'row_range':item['row_range'],
                   'width':im.width,'height':im.height,
                   'pdf_embedded_image_pixels_equal_registered_png':True,
                   'icc_profile_identical_to_original':True,'ocr_or_hidden_text_present':False,
                   'no_cropped_away_image_pixels_embedded':True})
(BASE/'crop-specification.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(BASE/'excerpt-integrity.json').write_text(json.dumps({
    'created_at_utc':datetime.now(timezone.utc).isoformat(),'path':str(output.relative_to(REG)),
    'bytes':output.stat().st_size,'sha256':digest(output.read_bytes()),'page_count':4,
    'whole_original_jo_sha256':whole_sha,'title_explicitly_marks_local_extract':True,
    'whole_jo_not_in_public_registry_proposal':True,'only_annexe_pos_original_pixels':True,
    'checks':checks},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'excerpt':str(output),'sha256':digest(output.read_bytes()),'bytes':output.stat().st_size,'pages':4,'all_pixel_and_profile_checks_pass':True}))
