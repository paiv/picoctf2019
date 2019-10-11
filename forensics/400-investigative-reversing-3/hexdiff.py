#!/usr/bin/env python3
import sys


def main(fn1, fn2):
    with open(fn1, 'rb') as fp1, open(fn2, 'rb') as fp2:
        data1 = fp1.read()
        data2 = fp2.read()

    for i, (a, b) in enumerate(zip(data1, data2)):
        if a != b:
            print('{:06x}: {:02x} {:02x} {}'.format(i, a, b, a^b))


if __name__ == '__main__':
    main(*sys.argv[1:])
