"""Manifest-first completeness accounting; no inference or clinical claims."""
from fractions import Fraction
from recording_time import exact


def count(value):
    if isinstance(value,bool) or not isinstance(value,int) or value<0:
        raise ValueError('Nonnegative integer count required')
    return value


def coverage_report(expected, receipts):
    manifest={}
    for row in expected:
        key=row['record_id'];person=row['person']
        if not isinstance(key,str) or not key or key in manifest or not isinstance(person,str) or not person:
            raise ValueError('Unique record and explicit person identities required')
        seconds=exact(row['seconds'])
        if seconds<=0:raise ValueError('Known positive duration required')
        manifest[key]=(person,seconds,count(row['events']))
    if not manifest or set(receipts)-set(manifest):
        raise ValueError('Nonempty manifest and no extra receipts required')
    persons={};rows=[]
    for key,(person,seconds,events) in manifest.items():
        receipt=receipts.get(key)
        status='missing' if receipt is None else receipt.get('status')
        if status not in ('missing','failed','scored'):
            raise ValueError('Unknown receipt status')
        if status=='missing' and receipt is not None:
            raise ValueError('Missing is represented by absent receipt, not a payload')
        reason='No receipt' if status=='missing' else receipt.get('reason')
        if status=='failed' and (not isinstance(reason,str) or not reason.strip()):
            raise ValueError('Failure reason required')
        if status=='scored':
            result=receipt['result'];c=result['coverage'];s=result['timely']
            if result['record_id']!=key or exact(c['recorded_seconds'])!=seconds:
                raise ValueError('Scored identity/duration mismatch')
            if c['original_event_count']!=events or count(s['reference_events'])!=events:
                raise ValueError('Scored original event count mismatch')
            # Existing scorer reports finite float duration, integer seconds exact here.
            if Fraction(s['recording_seconds'])!=seconds:
                raise ValueError('Scorer duration mismatch')
            if sum(count(s[k]) for k in ('timely_events','late_events','events_without_fresh_activation'))!=events:
                raise ValueError('Scored event partition mismatch')
        group=persons.setdefault(person,dict(records=0,scored=0,failed=0,missing=0,seconds=Fraction(0),events=0,unassessed_seconds=Fraction(0),unassessed_events=0))
        group['records']+=1;group[status]+=1;group['seconds']+=seconds;group['events']+=events
        if status!='scored':group['unassessed_seconds']+=seconds;group['unassessed_events']+=events
        rows.append(dict(record_id=key,person=person,status=status,seconds=str(seconds),events=events,reason=reason if status!='scored' else None))
    complete=all(r['status']=='scored' for r in rows)
    for group in persons.values():
        group['seconds']=str(group['seconds']);group['unassessed_seconds']=str(group['unassessed_seconds'])
    return dict(expected_records=len(manifest),persons=persons,records=rows,
        expected_seconds=str(sum((v[1] for v in manifest.values()),Fraction())),
        expected_events=sum(v[2] for v in manifest.values()),
        complete=complete,cohort_performance=None,
        interpretation='Completeness only; no clinical/confirmation conclusion or missing-result imputation')
