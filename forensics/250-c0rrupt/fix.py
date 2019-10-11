#!/usr/bin/env python
import struct
import sys


VERBOSE = 1


def trace(*args, **kwargs):
    if VERBOSE: print(*args, file=sys.stderr, flush=True, **kwargs)


def main(fn='mystery', ofn='fixed.png'):
    with open(fn, 'rb') as f:
        data = f.read()

    with open(ofn, 'wb') as f:
        f.write(b'\x89PNG\x0d\x0a\x1a\x0a')
        i = 8
        while i + 12 <= len(data):
            n, = struct.unpack('>I', data[i:i+4])
            t = data[i+4:i+8]
            trace('{}: {} {}'.format(i, n, t))
            if t == b'C"DR':
                t = b'IHDR'
            elif t == b'\xabDET':
                t = b'IDAT'
                n = len(data) - i - 12 - 12
            d = data[i+8:i+8+n]
            i += 8 + n
            x = data[i:i+4]
            i += 4

            f.write(struct.pack('>I', n))
            f.write(t)
            f.write(d)
            f.write(x)


if __name__ == '__main__':
    main(*sys.argv[1:])
