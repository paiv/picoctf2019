#!/usr/bin/env python
import numpy as np


def solve(fn='whitepages.txt'):
    with open(fn) as f:
        data = f.read()

    xs = np.packbits([x == ' ' for x in data])
    return bytes(xs)


if __name__ == '__main__':
    print(solve())
