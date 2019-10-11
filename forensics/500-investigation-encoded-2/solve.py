#!/usr/bin/env python3
import string
import struct
import sys


VERBOSE = 2


def trace(*args, **kwargs):
    if VERBOSE > 1: print(*args, file=sys.stderr, flush=True, **kwargs)


def solve(app='mystery', fn='output'):
    with open(app, 'rb') as fp:
        fp.seek(0x12e0)
        secret = fp.read(0x46)
        fp.seek(0x1340)
        indexTable = fp.read(0x98)

    ssecret = ''.join(f'{x:08b}' for x in secret)
    matrix = struct.unpack('<' + 'I' * (len(indexTable) // 4), indexTable)

    tr = {ssecret[i:n]: chr(k + (ord('a') if k < 26 else (ord('0') - 26)))
        for k, (i, n) in enumerate(zip(matrix, matrix[1:]))}

    trace(tr)

    with open(fn, 'rb') as fp:
        data = fp.read()

    s = ''.join(f'{x:08b}' for x in data)
    flag = ''.join(tr[x+'000'] for x in s.rstrip('0').split('000'))

    abc = string.ascii_lowercase + string.digits
    tr = str.maketrans(abc[18:]+abc[:18], abc)
    return flag.translate(tr)


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
