#!/usr/bin/env python
import base64
from urllib.parse import unquote


def solve():
    cc = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMzJTM3JTM4JTMwJTM0JTY1JTM3JTM5'

    s = base64.b64decode(cc)
    s = unquote(s.decode('ascii'))
    return 'picoCTF{{{}}}'.format(s)


if __name__ == '__main__':
    print(solve())
