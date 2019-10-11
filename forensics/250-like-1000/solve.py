#!/usr/bin/env python
import subprocess
import sys
from pathlib import Path


VERBOSE = 1


def trace(*args, **kwargs):
    if VERBOSE: print(*args, file=sys.stderr, flush=True, **kwargs)


def solve(fn='1000.tar'):
    temp = Path('./files')
    temp_in = temp / 'in'
    temp_out = temp / 'out'
    temp.mkdir(exist_ok=True)
    temp_in.mkdir(exist_ok=True)
    temp_out.mkdir(exist_ok=True)

    while fn:
        trace(fn)
        fn = Path(fn)
        src = temp_in / fn.name
        fn.rename(src)

        proc = subprocess.run([*'tar -vxC ../out -f'.split(), src.name], cwd=str(temp_in), stderr=subprocess.PIPE)
        trace(proc.stderr)

        for fn in temp_out.rglob('*.tar'):
            break
        else:
            return


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
