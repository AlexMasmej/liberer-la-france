"""Exact physical macOS Python launcher/image binding for this one release."""
from pathlib import Path
import hashlib,subprocess

WRAPPER=Path('/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/bin/python3.14')
IMAGE=Path('/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python')
WRAPPER_SHA='f13707ff725eb3675d57e0f04527a4dada0511cebfb7cbd80f5cab72733a2a9d'
IMAGE_SHA='6cf88920bb89d3db7cb8bad4b09ad793143e37b00c60a8b37baa435071fcae03'

def sha(data):return hashlib.sha256(data).hexdigest()
def loaded_images(pid):
    result=subprocess.run(['/usr/sbin/lsof','-a','-p',str(pid),'-d','txt','-Fn'],text=True,capture_output=True,timeout=15)
    if result.returncode!=0 or not result.stdout.startswith('p'+str(pid)+'\n'):
        raise ValueError('Loaded process images are unknown')
    return result.stdout

def bind_interpreter(observed,requested,observed_tail,requested_tail,pid):
    if type(pid) is not int or pid<=0 or observed_tail!=requested_tail:
        raise ValueError('Actual process arguments or PID differ')
    actual,launcher=Path(observed).resolve(),Path(requested).resolve()
    if actual!=IMAGE or launcher!=WRAPPER:
        raise ValueError('Unreviewed interpreter launcher/image pair')
    for path,h in [(WRAPPER,WRAPPER_SHA),(IMAGE,IMAGE_SHA)]:
        if not path.is_file() or path.is_symlink() or sha(path.read_bytes())!=h:
            raise ValueError('Pinned physical interpreter changed')
    loaded=loaded_images(pid)
    if 'n'+str(IMAGE) not in loaded.splitlines():raise ValueError('Actual process did not load the pinned image')
    for path,h in [(WRAPPER,WRAPPER_SHA),(IMAGE,IMAGE_SHA)]:
        if sha(path.read_bytes())!=h:raise ValueError('Interpreter changed during process observation')
    return dict(requested_launcher=str(WRAPPER),launcher_sha256=WRAPPER_SHA,
                observed_loaded_image=str(IMAGE),image_sha256=IMAGE_SHA,
                actual_pid=pid,lsof_sha256=sha(loaded.encode()),argument_tail_identical=True)
