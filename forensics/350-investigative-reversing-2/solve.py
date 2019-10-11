#!/usr/bin/env python
import numpy as np


def solve(fn='encoded.bmp'):
    with open(fn, 'rb') as f:
        f.seek(2000)
        data = f.read(50 * 8)

    xs = [(x & 1) for x in data]
    flag = np.packbits(xs, bitorder='little')
    flag = bytes((x + 5) for x in flag)
    return flag


if __name__ == '__main__':
    print(solve())
