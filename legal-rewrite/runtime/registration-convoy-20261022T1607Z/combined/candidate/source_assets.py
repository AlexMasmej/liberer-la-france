"""Verified local companions for formulas omitted by the LEGI text export.

Companions supplement the immutable source; their provenance remains explicit.
Only manifest-listed files with matching hashes may appear in legal HTML.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import html
from html.parser import HTMLParser

ATTACHMENTS = Path(__file__).resolve().parent / 'attachments'


def graphic_markers(body):
    """Locate documentary omissions, rather than ordinary references to forms."""
    paragraphs=re.findall(r'<p\b[^>]*>.*?</p>',body,re.S|re.I) or [body]
    pattern=r'non reproduit|vous pouvez (?:la )?consulter|consulter la (?:formule|modification)|consulter le tableau'
    return [html.unescape(re.sub('<[^>]*>',' ',paragraph)).strip() for paragraph in paragraphs if re.search(pattern,html.unescape(re.sub('<[^>]*>',' ',paragraph)),re.I)]


def recovery_complete(body, companion):
    expected=len(graphic_markers(body))
    if not expected:return True
    if not companion or not companion.get('documentary_recovery_complete'):return False
    if companion.get('expected_markers')!=expected:return False
    recovered={item['marker'] for field in ['media','transcriptions'] for item in companion.get(field,[])}
    return recovered==set(range(1,expected+1)) and bool(companion.get('documents'))


def recovered_content_present(body, companion):
    text=' '.join(html.unescape(re.sub('<[^>]*>',' ',body)).split())
    present=set()
    for item in companion.get('media',[]):
        if re.search(r'<img\b[^>]*\bsrc=[\"\']'+re.escape(item['path'])+r'[\"\']',body):present.add(item['marker'])
    for item in companion.get('transcriptions',[]):
        if ' '.join(item['text'].split()) in text:present.add(item['marker'])
    return present==set(range(1,companion['expected_markers']+1))


def asset_path(value, root=ATTACHMENTS):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_./-]+', value):
        raise ValueError('Invalid local companion path')
    parts = PurePosixPath(value)
    if parts.is_absolute() or any(p in {'.', '..'} for p in parts.parts):
        raise ValueError('Companion path escapes attachments')
    path = root / value
    if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Missing or unsafe companion file: ' + value)
    return path


def load_companions(root=ATTACHMENTS):
    records = {}
    for manifest in sorted((root / 'records').glob('*.json')):
        record = json.loads(manifest.read_text())
        key = (record['code_id'], record['source_id'])
        if key in records:
            raise ValueError('Duplicate source companion record')
        for field, suffixes in [('media', {'.png', '.jpg', '.webp'}), ('documents', {'.pdf'})]:
            for item in record.get(field, []):
                path = asset_path(item['path'], root)
                if path.suffix.lower() not in suffixes:
                    raise ValueError('Unexpected companion file type')
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                if actual != item['sha256']:
                    raise ValueError('Companion hash mismatch: ' + item['path'])
        records[key] = record
    return records


def verified_image(value, root=ATTACHMENTS):
    if not value or not value.startswith('media/'):
        raise ValueError('Only registered local formula images are allowed')
    for record in load_companions(root).values():
        if any(item['path'] == value for item in record.get('media', [])):
            return asset_path(value, root)
    raise ValueError('Unregistered formula image: ' + value)


class SafeLegalHTML(HTMLParser):
    tags={'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.result=[]

    def handle_starttag(self, tag, attrs):
        if tag=='img':
            values=dict(attrs)
            try:
                verified_image(values.get('src'))
            except ValueError:
                return
            if values.get('alt'):
                self.result.append('<img src="'+html.escape(values['src'],quote=True)+'" alt="'+html.escape(values['alt'],quote=True)+'">')
        elif tag in self.tags:
            allowed=''.join(f' {k}="{v}"' for k,v in attrs if k in {'rowspan','colspan'} and v and v.isdigit())
            self.result.append('<'+tag+allowed+'>')

    def handle_endtag(self, tag):
        if tag in self.tags and tag!='br':self.result.append('</'+tag+'>')

    def handle_data(self, data):
        self.result.append(html.escape(data))


def safe_html(body):
    parser=SafeLegalHTML()
    parser.feed(body)
    return ''.join(parser.result)
