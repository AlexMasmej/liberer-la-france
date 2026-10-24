"""Pure disposition guard: a changed rejected result needs a complete fresh proof."""
FIELDS=['source_sha256','status','proposed_xml','reason','review_notes']
def values(row):return tuple(row[k] for k in FIELDS)

def rejected_disposition(key,previous,current,review_status,fully_verified):
    if key in fully_verified:
        proof=fully_verified[key]
        if values(proof['previous_draft'])!=values(previous):
            raise ValueError('Fresh review beforeimage is not the rejected whole five-field beforeimage')
        if values(proof['answer'])!=current or review_status!='completed':
            raise ValueError('Fresh accepted answer/DB/completed proof changed')
        return 'freshly_recovered_under_full_native_DB_owner_registry_archive_proof'
    if current!=values(previous) or review_status!='pending':
        raise ValueError('Unknown change to rejected beforeimage/pending; complete fresh recovery proof required')
    return 'pending_whole_beforeimage_preserved'
