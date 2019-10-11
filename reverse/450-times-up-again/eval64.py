#!/usr/bin/env python

def solve():
    return eval(input()) % 0x8000000000000000

if __name__ == '__main__':
    print(solve())
