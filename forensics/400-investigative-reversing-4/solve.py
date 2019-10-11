#!/usr/bin/env python
import numpy as np


def solve():
    def unpack1(fn):
        with open(fn, 'rb') as f:
            f.seek(2019)
            data = f.read(10 * 8 + 40)
        xs = [(x & 1) for i in range(0, len(data), 12) for x in data[i:i+8]]
        flag = np.packbits(xs, bitorder='little')
        return bytes(flag)

    fns = [f'Item0{i+1}_cp.bmp' for i in reversed(range(5))]
    flag = b''.join(map(unpack1, fns))
    return flag.decode('ascii')


if __name__ == '__main__':
    print(solve())
