"""Fetch only attempt 1 from the pinned primary source; never clone the dataset."""
import hashlib, json, time, urllib.request
from pathlib import Path
from explore import allowed

def main(root='.'):
    root=Path(root);(root/'data').mkdir(exist_ok=True)
    for item in json.loads((root/'source_manifest.json').read_text()):
        name=Path(item['path']).name
        if not allowed(name): raise ValueError('forbidden holdout path')
        url='https://raw.githubusercontent.com/EnzeXu/Damped_Pendulum_Dataset/'+item['source_commit']+'/'+item['path']
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url,timeout=20) as response: data=response.read()
                break
            except (OSError,TimeoutError):
                if attempt==2: raise
                time.sleep(1)
        sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if sha != item['git_blob_sha']: raise ValueError('source checksum mismatch')
        (root/'data'/name).write_bytes(data)
    print('Verified 15 development files. No holdout download.')

if __name__=='__main__': main()
