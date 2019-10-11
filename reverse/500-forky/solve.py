#!/usr/bin/env python

#             a
# fork:       a                b
# fork:       a        c       b        d
# fork:       a    e   c   f   b    g   d   h
# fork:       a i  e j c k f l b m  g n d o h p

def solve():
    x = 0x3b9aca00
    for i in range(10, 17):
        y = 0x3b9aca00 + 0x499602d2 * i
        flag = 'picoCTF{{{}}}'.format(u32(y))
        print(i, flag, len(flag))
        flag = 'picoCTF{{{}}}'.format(i32(y))
        print('  ', flag, len(flag))


def u32(x):
    return x % 0x100000000

def i32(x):
    x = u32(x)
    return x if x < 0x80000000 else x - 0x100000000


if __name__ == '__main__':
    solve()
