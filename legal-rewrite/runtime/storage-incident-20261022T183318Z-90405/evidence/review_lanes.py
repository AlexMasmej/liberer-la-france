"""Bounded, non-borrowing queues for the coordinator's explicit role plan.

Admission is delegated to the coordinator before a future is submitted. A
conflicting footprint therefore never occupies an executor thread just waiting
for its lease. This module neither invokes a model nor accepts an article.
"""
import concurrent.futures
import queue
import threading

POOL_LIMITS={'new':6,'review':2}


def completed_futures(scheduled, *, limits, submit, stopped, wait_for_change,
                      describe, state_changed, deferred_changed,
                      unconsumed=None, worker_failed=None, executor_factory=None, poll_seconds=.2):
    """Yield completed futures; paused/stopped jobs remain unattempted for resume.

    ``submit(pool,job,review)`` must reserve all shared capacity/lease guards
    atomically and return None if currently unavailable. It must release any
    reservation if executor submission fails. Limits are read afresh each pass.
    """
    factory=executor_factory or concurrent.futures.ThreadPoolExecutor
    queues={role:[] for role in POOL_LIMITS}
    for ordinal,(job,review) in enumerate(scheduled):
        queues['review' if review else 'new'].append((ordinal,job,review))
    active={};admitted={role:0 for role in POOL_LIMITS}
    deferred=[];last_state=None;failed=False
    closing=threading.Event();fatal_worker=threading.Event();completed=queue.Queue();end=object()
    def should_stop():return closing.is_set() or fatal_worker.is_set() or stopped()
    def error_future(error):
        future=concurrent.futures.Future();future.set_exception(error);return future
    def observe_worker(future):
        # The consumer can be publishing for minutes. Fail closed at the actual
        # completion boundary, without waiting for its next future.result().
        if future.cancelled() or future.exception() is not None:
            fatal_worker.set()
            if worker_failed is not None:worker_failed(future)

    def defer(role,reason):
        if not queues[role]:return
        deferred.extend(describe(job,review)|{'queue_ordinal':ordinal,'reason':reason,
                         'attempted':False,'accepted':False}
                        for ordinal,job,review in queues[role])
        queues[role].clear()
        deferred_changed(list(deferred))

    def notify(action):
        nonlocal last_state
        value={'action':action,'pending_by_kind':{r:len(q) for r,q in queues.items()},
               'reserved_or_running_by_kind':{r:sum(role==r for role in active.values()) for r in POOL_LIMITS},
               'admitted_by_kind':dict(admitted),
               'deferred_by_kind':{r:sum(d['kind']==r for d in deferred) for r in POOL_LIMITS},
               'borrowing_enabled':False,
               'execution_evidence_scope':'Admission only; native session headers and validated answers are required for execution/acceptance claims.'}
        if value!=last_state:state_changed(value);last_state=value

    def dispatch():
        nonlocal failed
        try:
            # Admission/refill is independent of a slow publication checkpoint
            # in the consumer. Only the dispatcher owns its executor contexts.
            with factory(max_workers=6,thread_name_prefix='new-article') as new_pool,\
                 factory(max_workers=2,thread_name_prefix='review-article') as review_pool:
                pools={'new':new_pool,'review':review_pool}
                while active or any(queues.values()):
                    try:
                        if fatal_worker.is_set():failed=True
                        if failed or should_stop():
                            for role in queues:defer(role,'admission_error' if failed else 'stop_requested')
                        else:
                            current=limits();roles=current['role_limits']
                            if roles is None:raise ValueError('Role plan removed while role-separated scheduler is running; restart required')
                            for role in POOL_LIMITS:
                                if roles[role]==0:defer(role,'role_admissions_paused')
                            for role,lane_queue in queues.items():
                                index=0
                                while index<len(lane_queue) and not should_stop():
                                    role_active=sum(r==role for r in active.values())
                                    if role_active>=min(POOL_LIMITS[role],roles[role]) or len(active)>=current['workers']:break
                                    _,job,review=lane_queue[index]
                                    future=submit(pools[role],job,review)
                                    if future is None:
                                        index+=1;continue
                                    lane_queue.pop(index);active[future]=role;admitted[role]+=1
                                    future.add_done_callback(observe_worker)
                        if not failed:
                            notify('draining' if should_stop() else
                                   'review_admissions_paused' if any(d['kind']=='review' and d['reason']=='role_admissions_paused' for d in deferred)
                                   else 'running')
                    except Exception as error:
                        failed=True;completed.put(error_future(error));continue
                    if not active:
                        if any(queues.values()):wait_for_change(poll_seconds)
                        continue
                    done,_=concurrent.futures.wait(active,timeout=poll_seconds,
                                                  return_when=concurrent.futures.FIRST_COMPLETED)
                    for future in done:
                        active.pop(future);completed.put(future)
                if not failed:
                    notify('stopped' if should_stop() else
                           'review_admissions_paused' if deferred else 'finished')
        except BaseException as error:
            failed=True;completed.put(error_future(error))
        finally:
            # Executor contexts have drained before this point, including on a
            # publication consumer's generator.close(). Deliver every result.
            for future in list(active):completed.put(future)
            completed.put(end)

    dispatcher=threading.Thread(target=dispatch,name='review-lane-dispatcher')
    dispatcher.start()
    try:
        while True:
            item=completed.get()
            if item is end:break
            yield item
    finally:
        closing.set()
        dispatcher.join()
        # A closing consumer cannot receive the remaining yielded futures.
        # Preserve their outcomes explicitly rather than silently losing errors.
        remaining=[]
        while not completed.empty():
            item=completed.get_nowait()
            if item is not end:remaining.append(item)
        if remaining and unconsumed is not None:unconsumed(remaining)
