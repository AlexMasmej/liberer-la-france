"""Concurrency and failure checks for the coordinator's JSON checkpoint writer."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase,main
from unittest.mock import patch
import json
import threading
import run_exhaustive as coordinator


class AtomicStatus(TestCase):
    def test_concurrent_writers_and_continuous_reader_observe_whole_json(self):
        writers=8;rounds=25
        with TemporaryDirectory() as directory:
            path=Path(directory)/'status.json'
            def value(writer,sequence):
                return {'writer':writer,'sequence':sequence,
                        'payload':('État %s:%s — '%(writer,sequence))*1024,
                        'counts':list(range(256))}
            coordinator.atomic(path,value(-1,-1))
            stop=threading.Event();started=threading.Event();barrier=threading.Barrier(writers)
            errors=[];observations=[];names=[];guard=threading.Lock()
            original_replace=Path.replace
            def synchronized_replace(temporary,target):
                self.assertEqual(temporary.parent,path.parent)
                self.assertEqual(target,path)
                with guard:names.append(temporary.name)
                barrier.wait(timeout=10)
                return original_replace(temporary,target)
            def read():
                try:
                    while not stop.is_set():
                        current=json.loads(path.read_text(encoding='utf-8'))
                        self.assertEqual(current,value(current['writer'],current['sequence']))
                        self.assertIn(current['writer'],range(-1,writers))
                        self.assertIn(current['sequence'],range(-1,rounds))
                        observations.append((current['writer'],current['sequence']))
                        started.set()
                except BaseException as error:
                    errors.append(error);started.set();barrier.abort()
            def write(writer):
                try:
                    for sequence in range(rounds):coordinator.atomic(path,value(writer,sequence))
                except BaseException:
                    barrier.abort()
                    raise
            reader=threading.Thread(target=read,daemon=True);reader.start()
            try:
                self.assertTrue(started.wait(timeout=10))
                with patch.object(Path,'replace',synchronized_replace):
                    with ThreadPoolExecutor(max_workers=writers) as pool:
                        futures=[pool.submit(write,writer) for writer in range(writers)]
                        for future in futures:future.result(timeout=30)
            finally:
                stop.set();reader.join(timeout=10)
            self.assertFalse(reader.is_alive());self.assertFalse(errors,errors)
            self.assertGreater(len(observations),10)
            self.assertTrue(any(writer>=0 for writer,sequence in observations))
            self.assertEqual(len(names),writers*rounds)
            self.assertEqual(len(set(names)),writers*rounds)
            current=json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(current,value(current['writer'],current['sequence']))
            self.assertEqual(current['sequence'],rounds-1)
            self.assertEqual(list(path.parent.iterdir()),[path])

    def test_serialization_failure_keeps_old_json_and_cleans_temporary(self):
        with TemporaryDirectory() as directory:
            path=Path(directory)/'nested/status.json'
            coordinator.atomic(path,{'status':'before'})
            with self.assertRaises(TypeError):coordinator.atomic(path,{'partial':'écrit','invalid':object()})
            self.assertEqual(json.loads(path.read_text()),{'status':'before'})
            self.assertEqual(list(path.parent.iterdir()),[path])

    def test_replace_failure_keeps_old_json_and_cleans_temporary(self):
        with TemporaryDirectory() as directory:
            path=Path(directory)/'status.json'
            coordinator.atomic(path,{'status':'before'})
            with patch.object(Path,'replace',side_effect=OSError('replacement rejected')):
                with self.assertRaisesRegex(OSError,'replacement rejected'):
                    coordinator.atomic(path,{'status':'after'})
            self.assertEqual(json.loads(path.read_text()),{'status':'before'})
            self.assertEqual(list(path.parent.iterdir()),[path])

    def test_initial_serialization_failure_leaves_no_partial_target(self):
        with TemporaryDirectory() as directory:
            path=Path(directory)/'new/status.json'
            with self.assertRaises(TypeError):coordinator.atomic(path,{'invalid':object()})
            self.assertFalse(path.exists());self.assertEqual(list(path.parent.iterdir()),[])


if __name__=='__main__':main(verbosity=2)
