#!/usr/bin/env python

def solve():
    buf = 'jU5t_a_sna_3lpm1eg34a_u_4_m4ra40'
    pwd = [None] * len(buf)

    for i in reversed(range(17, 32, 2)):
        pwd[i] = buf[i]

    for i in range(16, 32, 2):
        pwd[46-i] = buf[i]

    for i in range(8, 16):
        pwd[23-i] = buf[i]

    for i in range(8):
        pwd[i] = buf[i]

    flag = 'picoCTF{{{}}}'.format(''.join(pwd))
    return flag


if __name__ == '__main__':
    print(solve())
