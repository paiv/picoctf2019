#!/usr/bin/env python
import struct


def solve():
    data = [
        0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0,
        0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xF1,
        0xC1, 0xD1, 0xA5, 0xD1, 0xD2, 0xD0, 0xA4, 0xC0
    ]

    def swap(x, a, b):
        xs = [0] * 8
        for i in range(8):
            x, xs[i] = divmod(x, 2)
        xs[a], xs[b] = xs[b], xs[a]
        return sum((x * (1 << i)) for i, x in enumerate(xs))

    def tr(x):
        x = swap(x, 6, 7)
        x = swap(x, 2, 5)
        x = swap(x, 3, 4)
        x = swap(x, 0, 1)
        x = swap(x, 4, 7)
        x = swap(x, 5, 6)
        x = swap(x, 0, 3)
        x = swap(x, 1, 2)
        return x

    s = bytes(map(tr, data)).decode('ascii')
    return 'picoCTF{{{}}}'.format(s)


if __name__ == '__main__':
    print(solve())
