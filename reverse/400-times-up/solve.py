#!/usr/bin/env python3
import subprocess as sub
import sys
from subprocess import PIPE


def solve(fn='./times-up'):
    t = None
    x = None
    while True:
        proc = sub.run([fn], stdout=PIPE, encoding='utf-8', input=str(x))
        so = proc.stdout
        print(so)
        s = so.splitlines()[0]
        if s == t:
            break
        if s.startswith('Challenge: '):
            x = eval(s[11:])
            t = s


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
