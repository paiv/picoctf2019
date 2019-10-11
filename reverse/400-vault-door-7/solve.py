#!/usr/bin/env python
import struct


def solve():
    data = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293046, 926180660, 862348336]

    s = struct.pack('>8I', *data).decode('ascii')
    return 'picoCTF{{{}}}'.format(s)


if __name__ == '__main__':
    print(solve())
