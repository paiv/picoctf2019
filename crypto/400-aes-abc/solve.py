#!/usr/bin/env python
import binascii
import sys


def solve(fn='body.enc.ppm', ofn='fixed.ppm'):
    with open(fn, 'rb') as f:
        data = f.read()

    n = data.index(b'\n')
    n = data.index(b'\n', n + 1)
    n = data.index(b'\n', n + 1)
    n += 1
    header, data = data[:n], data[n:]

    blocks = [data[i:i+16] for i in range(0, len(data), 16)]
    xs = list()
    for i in reversed(range(1, len(blocks))):
        xs.append(diff(blocks[i], blocks[i-1]))

    with open(ofn, 'wb') as f:
        f.write(header)
        for x in reversed(xs):
            f.write(x)


BLOCK_SIZE = 16
UMAX = int(pow(256, BLOCK_SIZE))

def diff(a, b):
    a = int(binascii.hexlify(bytes(a)), 16)
    b = int(binascii.hexlify(bytes(b)), 16)
    x = (a - b) % UMAX
    return binascii.unhexlify(f'{x:032x}')


if __name__ == '__main__':
    solve(*sys.argv[1:])
