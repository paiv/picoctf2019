#!/usr/bin/env python
import numpy as np


def solve(fn='encoded.bmp'):
    with open(fn, 'rb') as f:
        f.seek(723)
        data = f.read(50 * 8 + 49)

    xs = [(x & 1) for i, x in enumerate(data) if (i + 1) % 9]
    flag = np.packbits(xs, bitorder='little')
    return bytes(flag).decode('ascii')


if __name__ == '__main__':
    print(solve())
