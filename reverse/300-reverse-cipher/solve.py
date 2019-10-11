#!/usr/bin/env python
import sys


def solve(fn='rev_this'):
    with open(fn, 'rb') as f:
        data = f.read()

    xs = list(data)
    for i in range(8, 23):
        xs[i] += (2 if i % 2 else -5)
    return bytes(xs)


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
