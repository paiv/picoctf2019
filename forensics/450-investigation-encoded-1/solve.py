#!/usr/bin/env python3
import string
import sys


VERBOSE = 2


def trace(*args, **kwargs):
    if VERBOSE > 1: print(*args, file=sys.stderr, flush=True, **kwargs)


def solve(fn='output'):
    matrix = [8, 0, 12, 8, 14, 20, 10, 34, 4, 44, 12, 48, 12, 60, 10, 72, 6,
        82, 16, 88, 12, 104, 12, 116, 10, 128, 8, 138, 14, 146, 14, 160, 16, 174,
        10, 190, 8, 200, 6, 208, 10, 214, 12, 224, 12, 236, 14, 248, 16, 262, 14, 278, 4, 292]

    secret = [184, 234, 142, 186, 58, 136, 174, 142, 232, 170, 40, 187, 184,
        235, 139, 168, 238, 58, 59, 184, 187, 163, 186, 226, 232, 168, 226, 184,
        171, 139, 184, 234, 227, 174, 227, 186, 128]

    ssecret = ''.join(f'{x:08b}' for x in secret)
    tr = {ssecret[i:i+n]:chr(k+ord('a')) for k, (n, i) in enumerate(zip(matrix[::2], matrix[1::2]))}

    with open(fn, 'rb') as fp:
        data = fp.read()

    s = ''.join(f'{x:08b}' for x in data)
    flag = ''.join(tr[x+'000'] for x in s.rstrip('0').split('000'))
    return flag


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
