"""Rebind only drafts whose entire source evidence and dates are identical.

LEGI document metadata can change the full XML hash while the article body,
application notes and validity period remain byte-identical. All other
changes remain unresolved; no proposal is edited by this migration.
"""
import argparse,hashlib,json
from ingest import HERE,open_db,source_evidence,source_notes
from register_batches import writer_lock


def equivalent_evidence(db,code,identifier,body,start,end):
    previous=db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?',(code,identifier)).fetchone()
    current=source_evidence(body,source_notes(db,code,identifier))
    return previous==(current,start,end),hashlib.sha256(current.encode()).hexdigest()


def main(commit=False):
    with writer_lock():
        db=open_db(HERE/'corpus.sqlite')
        report={'proposal_text_changed':False,'committed':commit,'rebound':[],'not_equivalent':[]}
        rows=db.execute('SELECT d.code_id,d.source_id,a.number,d.source_sha256,a.source_sha256,a.content_xml,a.valid_from,a.valid_until FROM drafts d JOIN articles a ON a.code_id=d.code_id AND a.id=d.source_id WHERE d.source_sha256<>a.source_sha256').fetchall()
        try:
            db.execute('BEGIN IMMEDIATE')
            for code,ident,number,old,new,body,start,end in rows:
                equivalent,evidence_sha=equivalent_evidence(db,code,ident,body,start,end)
                record={'code_id':code,'source_id':ident,'number':number,'previous_document_sha256':old,'canonical_document_sha256':new,'source_body_notes_and_dates_identical':equivalent,'source_evidence_sha256':evidence_sha,'valid_from':start,'valid_until':end}
                if not equivalent:report['not_equivalent'].append(record);continue
                if commit:db.execute('UPDATE drafts SET source_sha256=? WHERE code_id=? AND source_id=? AND source_sha256=?',(new,code,ident,old))
                report['rebound'].append(record)
            if commit:db.commit()
            else:db.rollback()
        except Exception:db.rollback();raise
        finally:db.close()
        if commit:
            p=HERE/'metadata-rebindings.json'
            previous=json.loads(p.read_text()) if p.exists() else []
            previous.append(report);p.write_text(json.dumps(previous,ensure_ascii=False,indent=2))
        print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--commit',action='store_true');args=parser.parse_args();main(args.commit)
