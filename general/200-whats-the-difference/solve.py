#!/usr/bin/env python
import sys


def solve(fn1='kitters.jpg', fn2='cattos.jpg', ofn='fixed.jpg'):
    with open(fn1, 'rb') as f1, open(fn2, 'rb') as f2:
        data1 = f1.read()
        data2 = f2.read()

    flag = list()
    for i, (a, b) in enumerate(zip(data1, data2)):
        if a != b:
            # print(f'{i:06x}: {a:02x} {b:02x}')
            flag.append(b)

    return bytes(flag)


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
